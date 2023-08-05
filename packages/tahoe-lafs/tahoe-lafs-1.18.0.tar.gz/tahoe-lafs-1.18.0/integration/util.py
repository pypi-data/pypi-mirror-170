"""
Ported to Python 3.
"""
from __future__ import unicode_literals
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from future.utils import PY2
if PY2:
    from future.builtins import filter, map, zip, ascii, chr, hex, input, next, oct, open, pow, round, super, bytes, dict, list, object, range, str, max, min  # noqa: F401

import sys
import time
import json
from os import mkdir, environ
from os.path import exists, join
from io import StringIO, BytesIO
from functools import partial
from subprocess import check_output

from twisted.python.filepath import (
    FilePath,
)
from twisted.internet.defer import Deferred, succeed
from twisted.internet.protocol import ProcessProtocol
from twisted.internet.error import ProcessExitedAlready, ProcessDone
from twisted.internet.threads import deferToThread

import requests

from paramiko.rsakey import RSAKey
from boltons.funcutils import wraps

from allmydata.util.configutil import (
    get_config,
    set_config,
    write_config,
)
from allmydata import client

import pytest_twisted


def block_with_timeout(deferred, reactor, timeout=120):
    """Block until Deferred has result, but timeout instead of waiting forever."""
    deferred.addTimeout(timeout, reactor)
    return pytest_twisted.blockon(deferred)


class _ProcessExitedProtocol(ProcessProtocol):
    """
    Internal helper that .callback()s on self.done when the process
    exits (for any reason).
    """

    def __init__(self):
        self.done = Deferred()

    def processEnded(self, reason):
        self.done.callback(None)


class _CollectOutputProtocol(ProcessProtocol):
    """
    Internal helper. Collects all output (stdout + stderr) into
    self.output, and callback's on done with all of it after the
    process exits (for any reason).
    """
    def __init__(self, capture_stderr=True):
        self.done = Deferred()
        self.output = BytesIO()
        self.capture_stderr = capture_stderr

    def processEnded(self, reason):
        if not self.done.called:
            self.done.callback(self.output.getvalue())

    def processExited(self, reason):
        if not isinstance(reason.value, ProcessDone):
            self.done.errback(reason)

    def outReceived(self, data):
        self.output.write(data)

    def errReceived(self, data):
        print("ERR: {!r}".format(data))
        if self.capture_stderr:
            self.output.write(data)


class _DumpOutputProtocol(ProcessProtocol):
    """
    Internal helper.
    """
    def __init__(self, f):
        self.done = Deferred()
        self._out = f if f is not None else sys.stdout

    def processEnded(self, reason):
        if not self.done.called:
            self.done.callback(None)

    def processExited(self, reason):
        if not isinstance(reason.value, ProcessDone):
            self.done.errback(reason)

    def outReceived(self, data):
        data = str(data, sys.stdout.encoding)
        self._out.write(data)

    def errReceived(self, data):
        data = str(data, sys.stdout.encoding)
        self._out.write(data)


class _MagicTextProtocol(ProcessProtocol):
    """
    Internal helper. Monitors all stdout looking for a magic string,
    and then .callback()s on self.done and .errback's if the process exits
    """

    def __init__(self, magic_text):
        self.magic_seen = Deferred()
        self.exited = Deferred()
        self._magic_text = magic_text
        self._output = StringIO()

    def processEnded(self, reason):
        self.exited.callback(None)

    def outReceived(self, data):
        data = str(data, sys.stdout.encoding)
        sys.stdout.write(data)
        self._output.write(data)
        if not self.magic_seen.called and self._magic_text in self._output.getvalue():
            print("Saw '{}' in the logs".format(self._magic_text))
            self.magic_seen.callback(self)

    def errReceived(self, data):
        data = str(data, sys.stderr.encoding)
        sys.stdout.write(data)


def _cleanup_tahoe_process(tahoe_transport, exited):
    """
    Terminate the given process with a kill signal (SIGKILL on POSIX,
    TerminateProcess on Windows).

    :param tahoe_transport: The `IProcessTransport` representing the process.
    :param exited: A `Deferred` which fires when the process has exited.

    :return: After the process has exited.
    """
    from twisted.internet import reactor
    try:
        print("signaling {} with TERM".format(tahoe_transport.pid))
        tahoe_transport.signalProcess('TERM')
        print("signaled, blocking on exit")
        block_with_timeout(exited, reactor)
        print("exited, goodbye")
    except ProcessExitedAlready:
        pass


def _tahoe_runner_optional_coverage(proto, reactor, request, other_args):
    """
    Internal helper. Calls spawnProcess with `-m
    allmydata.scripts.runner` and `other_args`, optionally inserting a
    `--coverage` option if the `request` indicates we should.
    """
    if request.config.getoption('coverage'):
        args = [sys.executable, '-b', '-m', 'coverage', 'run', '-m', 'allmydata.scripts.runner', '--coverage']
    else:
        args = [sys.executable, '-b', '-m', 'allmydata.scripts.runner']
    args += other_args
    return reactor.spawnProcess(
        proto,
        sys.executable,
        args,
        env=environ,
    )


class TahoeProcess(object):
    """
    A running Tahoe process, with associated information.
    """

    def __init__(self, process_transport, node_dir):
        self._process_transport = process_transport  # IProcessTransport instance
        self._node_dir = node_dir  # path

    @property
    def transport(self):
        return self._process_transport

    @property
    def node_dir(self):
        return self._node_dir

    def get_config(self):
        return client.read_config(
            self._node_dir,
            u"portnum",
        )

    def kill(self):
        """Kill the process, block until it's done."""
        _cleanup_tahoe_process(self.transport, self.transport.exited)

    def __str__(self):
        return "<TahoeProcess in '{}'>".format(self._node_dir)


def _run_node(reactor, node_dir, request, magic_text, finalize=True):
    """
    Run a tahoe process from its node_dir.

    :returns: a TahoeProcess for this node
    """
    if magic_text is None:
        magic_text = "client running"
    protocol = _MagicTextProtocol(magic_text)

    # "tahoe run" is consistent across Linux/macOS/Windows, unlike the old
    # "start" command.
    transport = _tahoe_runner_optional_coverage(
        protocol,
        reactor,
        request,
        [
            '--eliot-destination', 'file:{}/logs/eliot.json'.format(node_dir),
            'run',
            node_dir,
        ],
    )
    transport.exited = protocol.exited

    if finalize:
        request.addfinalizer(partial(_cleanup_tahoe_process, transport, protocol.exited))

    # XXX abusing the Deferred; should use .when_magic_seen() pattern

    def got_proto(proto):
        transport._protocol = proto
        return TahoeProcess(
            transport,
            node_dir,
        )
    protocol.magic_seen.addCallback(got_proto)
    return protocol.magic_seen


def _create_node(reactor, request, temp_dir, introducer_furl, flog_gatherer, name, web_port,
                 storage=True,
                 magic_text=None,
                 needed=2,
                 happy=3,
                 total=4,
                 finalize=True):
    """
    Helper to create a single node, run it and return the instance
    spawnProcess returned (ITransport)
    """
    node_dir = join(temp_dir, name)
    if web_port is None:
        web_port = ''
    if exists(node_dir):
        created_d = succeed(None)
    else:
        print("creating", node_dir)
        mkdir(node_dir)
        done_proto = _ProcessExitedProtocol()
        args = [
            'create-node',
            '--nickname', name,
            '--introducer', introducer_furl,
            '--hostname', 'localhost',
            '--listen', 'tcp',
            '--webport', web_port,
            '--shares-needed', str(needed),
            '--shares-happy', str(happy),
            '--shares-total', str(total),
            '--helper',
        ]
        if not storage:
            args.append('--no-storage')
        args.append(node_dir)

        _tahoe_runner_optional_coverage(done_proto, reactor, request, args)
        created_d = done_proto.done

        def created(_):
            config_path = join(node_dir, 'tahoe.cfg')
            config = get_config(config_path)
            set_config(
                config,
                u'node',
                u'log_gatherer.furl',
                flog_gatherer,
            )
            write_config(FilePath(config_path), config)
        created_d.addCallback(created)

    d = Deferred()
    d.callback(None)
    d.addCallback(lambda _: created_d)
    d.addCallback(lambda _: _run_node(reactor, node_dir, request, magic_text, finalize=finalize))
    return d


class UnwantedFilesException(Exception):
    """
    While waiting for some files to appear, some undesired files
    appeared instead (or in addition).
    """
    def __init__(self, waiting, unwanted):
        super(UnwantedFilesException, self).__init__(
            u"While waiting for '{}', unwanted files appeared: {}".format(
                waiting,
                u', '.join(unwanted),
            )
        )


class ExpectedFileMismatchException(Exception):
    """
    A file or files we wanted weren't found within the timeout.
    """
    def __init__(self, path, timeout):
        super(ExpectedFileMismatchException, self).__init__(
            u"Contents of '{}' mismatched after {}s".format(path, timeout),
        )


class ExpectedFileUnfoundException(Exception):
    """
    A file or files we expected to find didn't appear within the
    timeout.
    """
    def __init__(self, path, timeout):
        super(ExpectedFileUnfoundException, self).__init__(
            u"Didn't find '{}' after {}s".format(path, timeout),
        )



class FileShouldVanishException(Exception):
    """
    A file or files we expected to disappear did not within the
    timeout
    """
    def __init__(self, path, timeout):
        super(FileShouldVanishException, self).__init__(
            u"'{}' still exists after {}s".format(path, timeout),
        )


def await_file_contents(path, contents, timeout=15, error_if=None):
    """
    wait up to `timeout` seconds for the file at `path` (any path-like
    object) to have the exact content `contents`.

    :param error_if: if specified, a list of additional paths; if any
        of these paths appear an Exception is raised.
    """
    start_time = time.time()
    while time.time() - start_time < timeout:
        print("  waiting for '{}'".format(path))
        if error_if and any([exists(p) for p in error_if]):
            raise UnwantedFilesException(
                waiting=path,
                unwanted=[p for p in error_if if exists(p)],
            )
        if exists(path):
            try:
                with open(path, 'r') as f:
                    current = f.read()
            except IOError:
                print("IOError; trying again")
            else:
                if current == contents:
                    return True
                print("  file contents still mismatched")
                print("  wanted: {}".format(contents.replace('\n', ' ')))
                print("     got: {}".format(current.replace('\n', ' ')))
        time.sleep(1)
    if exists(path):
        raise ExpectedFileMismatchException(path, timeout)
    raise ExpectedFileUnfoundException(path, timeout)


def await_files_exist(paths, timeout=15, await_all=False):
    """
    wait up to `timeout` seconds for any of the paths to exist; when
    any exist, a list of all found filenames is returned. Otherwise,
    an Exception is raised
    """
    start_time = time.time()
    while time.time() - start_time < timeout:
        print("  waiting for: {}".format(' '.join(paths)))
        found = [p for p in paths if exists(p)]
        print("found: {}".format(found))
        if await_all:
            if len(found) == len(paths):
                return found
        else:
            if len(found) > 0:
                return found
        time.sleep(1)
    if await_all:
        nice_paths = ' and '.join(paths)
    else:
        nice_paths = ' or '.join(paths)
    raise ExpectedFileUnfoundException(nice_paths, timeout)


def await_file_vanishes(path, timeout=10):
    start_time = time.time()
    while time.time() - start_time < timeout:
        print("  waiting for '{}' to vanish".format(path))
        if not exists(path):
            return
        time.sleep(1)
    raise FileShouldVanishException(path, timeout)


def cli(node, *argv):
    """
    Run a tahoe CLI subcommand for a given node in a blocking manner, returning
    the output.
    """
    arguments = ["tahoe", '--node-directory', node.node_dir]
    return check_output(arguments + list(argv))


def node_url(node_dir, uri_fragment):
    """
    Create a fully qualified URL by reading config from `node_dir` and
    adding the `uri_fragment`
    """
    with open(join(node_dir, "node.url"), "r") as f:
        base = f.read().strip()
    url = base + uri_fragment
    return url


def _check_status(response):
    """
    Check the response code is a 2xx (raise an exception otherwise)
    """
    if response.status_code < 200 or response.status_code >= 300:
        raise ValueError(
            "Expected a 2xx code, got {}".format(response.status_code)
        )


def web_get(tahoe, uri_fragment, **kwargs):
    """
    Make a GET request to the webport of `tahoe` (a `TahoeProcess`,
    usually from a fixture (e.g. `alice`). This will look like:
    `http://localhost:<webport>/<uri_fragment>`. All `kwargs` are
    passed on to `requests.get`
    """
    url = node_url(tahoe.node_dir, uri_fragment)
    resp = requests.get(url, **kwargs)
    _check_status(resp)
    return resp.content


def web_post(tahoe, uri_fragment, **kwargs):
    """
    Make a POST request to the webport of `node` (a `TahoeProcess,
    usually from a fixture e.g. `alice`). This will look like:
    `http://localhost:<webport>/<uri_fragment>`. All `kwargs` are
    passed on to `requests.post`
    """
    url = node_url(tahoe.node_dir, uri_fragment)
    resp = requests.post(url, **kwargs)
    _check_status(resp)
    return resp.content


def await_client_ready(tahoe, timeout=10, liveness=60*2, minimum_number_of_servers=1):
    """
    Uses the status API to wait for a client-type node (in `tahoe`, a
    `TahoeProcess` instance usually from a fixture e.g. `alice`) to be
    'ready'. A client is deemed ready if:

      - it answers `http://<node_url>/statistics/?t=json/`
      - there is at least one storage-server connected (configurable via
        ``minimum_number_of_servers``)
      - every storage-server has a "last_received_data" and it is
        within the last `liveness` seconds

    We will try for up to `timeout` seconds for the above conditions
    to be true. Otherwise, an exception is raised
    """
    start = time.time()
    while (time.time() - start) < float(timeout):
        try:
            data = web_get(tahoe, u"", params={u"t": u"json"})
            js = json.loads(data)
        except Exception as e:
            print("waiting because '{}'".format(e))
            time.sleep(1)
            continue

        if len(js['servers']) < minimum_number_of_servers:
            print("waiting because insufficient servers")
            time.sleep(1)
            continue
        server_times = [
            server['last_received_data']
            for server in js['servers']
        ]
        # if any times are null/None that server has never been
        # contacted (so it's down still, probably)
        if any(t is None for t in server_times):
            print("waiting because at least one server not contacted")
            time.sleep(1)
            continue

        # check that all times are 'recent enough'
        if any([time.time() - t > liveness for t in server_times]):
            print("waiting because at least one server too old")
            time.sleep(1)
            continue

        # we have a status with at least one server, and all servers
        # have been contacted recently
        return True
    # we only fall out of the loop when we've timed out
    raise RuntimeError(
        "Waited {} seconds for {} to be 'ready' but it never was".format(
            timeout,
            tahoe,
        )
    )


def generate_ssh_key(path):
    """Create a new SSH private/public key pair."""
    key = RSAKey.generate(2048)
    key.write_private_key_file(path)
    with open(path + ".pub", "wb") as f:
        s = "%s %s" % (key.get_name(), key.get_base64())
        f.write(s.encode("ascii"))


def run_in_thread(f):
    """Decorator for integration tests that runs code in a thread.

    Because we're using pytest_twisted, tests that rely on the reactor are
    expected to return a Deferred and use async APIs so the reactor can run.

    In the case of the integration test suite, it launches nodes in the
    background using Twisted APIs.  The nodes stdout and stderr is read via
    Twisted code.  If the reactor doesn't run, reads don't happen, and
    eventually the buffers fill up, and the nodes block when they try to flush
    logs.

    We can switch to Twisted APIs (treq instead of requests etc.), but
    sometimes it's easier or expedient to just have a blocking test.  So this
    decorator allows you to run the test in a thread, and the reactor can keep
    running in the main thread.

    See https://tahoe-lafs.org/trac/tahoe-lafs/ticket/3597 for tracking bug.
    """
    @wraps(f)
    def test(*args, **kwargs):
        return deferToThread(lambda: f(*args, **kwargs))
    return test
