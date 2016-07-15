#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Resilient Systems, Inc. ("Resilient") is willing to license software
# or access to software to the company or entity that will be using or
# accessing the software and documentation and that you represent as
# an employee or authorized agent ("you" or "your") only on the condition
# that you accept all of the terms of this license agreement.
#
# The software and documentation within Resilient's Development Kit are
# copyrighted by and contain confidential information of Resilient. By
# accessing and/or using this software and documentation, you agree that
# while you may make derivative works of them, you:
#
# 1)  will not use the software and documentation or any derivative
#     works for anything but your internal business purposes in
#     conjunction your licensed used of Resilient's software, nor
# 2)  provide or disclose the software and documentation or any
#     derivative works to any third party.
#
# THIS SOFTWARE AND DOCUMENTATION IS PROVIDED "AS IS" AND ANY EXPRESS
# OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL RESILIENT BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
# STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
# OF THE POSSIBILITY OF SUCH DAMAGE.

"""Shell-runner (PowerShell, bash, etc) component"""

from __future__ import print_function
from circuits import task, Component, Timer, Debugger, Event
from circuits.core.handlers import handler
from resilient_circuits.actions_component import ResilientComponent, ActionMessage
from lib.disposition import Disposition
import resilient_circuits.template_functions as template_functions
import os
import tempfile
import json
import subprocess
import shlex
import logging
LOG = logging.getLogger(__name__)


def _shell_run(action_template, action_data):
    """Render and run the `action_template` command"""
    try:
        # Resolve the commandline by rendering the commandline template
        commandline = template_functions.render(action_template, action_data)

        # Write a temporary file containing the action_data
        with tempfile.NamedTemporaryFile(mode="w", delete=False) as temp_file:
            temp_filename = temp_file.name
            temp_file.write(json.dumps(action_data, indent=2, sort_keys=True))

        env = os.environ.copy()
        env["EVENTDATA"] = temp_filename

        # Execute the command line process (NOT in its own shell)
        commandline = os.path.expandvars(commandline)
        LOG.info("Run: %s (%s)", commandline, temp_filename)
        cmd = shlex.split(commandline, posix=True)
        call = subprocess.Popen(cmd,
                                shell=False,
                                stderr=subprocess.PIPE,
                                stdout=subprocess.PIPE,
                                env=env)
        stdoutdata, stderrdata = call.communicate()
        retcode = call.returncode
        output = stderrdata.decode()

        # Nonzero exit code indicates error; leave the temp file in place to ease debugging the script
        if retcode is not 0:
            raise OSError("'{}' failed: {}".format(cmd[0], output))

        result = stdoutdata.decode()

        # Clean up the temporary file
        os.remove(temp_filename)

    except Exception as exc:
        # Return (don't raise)
        return exc

    # Return the results
    LOG.debug("Run result: %s", result)
    return result


class Shell(ResilientComponent):
    """Execute shell commands from custom actions"""

    # This component supports running a very general set of shell scripts
    # when custom actions (manual or automatic) are triggered.
    # To do this,
    # - The action name is mapped to a shell command-line, using
    #   the JINJA template lanuguage to substitute values such as the
    #   incident id, artifact value, and so on
    # - The action event, which includes parameters from the event and
    #   incident (and also artifact, task, etc depending on context)
    #   is written to a temporary JSON file.  The path to this file is
    #   set in the environment ($EVENTDATA).
    # - The shell command is executed
    # - The results (stdout) are collected, and can then be used for
    #   whatever disposition is configured.  This includes the ability to
    #   add notes, tasks, attachments, or to update the incident's field values.
    #
    # ANY action on the chosen queue ("shell" by default) will run a command,
    # as long as it has been mapped to a command in the configuration file.
    # The config file mapping is just
    #   <lowercase_action_name>=<shell_command_template>
    # The disposition is
    #   <lowercase_action_name>_disposition=<add_attachment, etc>

    def __init__(self, opts):
        super(Shell, self).__init__(opts)
        self.options = opts.get("shell", {})
        LOG.debug(self.options)

        # Channel name beginning "actions." is a Resilient queue or topic
        # The queue name can be specified in the config file, or default to 'default'
        self.channel = "actions." + self.options.get("queue", "shell")

    # Handle any actions (not specific to the action name)

    @handler()
    def _shell_action(self, event, *args, **kwargs):
        """The @handler() annotation without an event name makes this
           a default handler - for all events on this component's queue.
           This will be called with some "internal" events from Circuits,
           so you must declare the method with the generic parameters
           (event, *args, **kwargs), and ignore any messages that are not
           from the Actions module.
        """
        if not isinstance(event, ActionMessage):
            # Some event we are not interested in
            return

        # Based on the action name,
        # find the commandline template for this action
        action_name = event.name
        action_template = self.options.get(action_name, self.options.get("command"))

        # Disposition can vary too
        disposition_args = self.options.get(action_name + "_result_disposition",
                                            self.options.get("result_disposition",
                                                             "new_attachment"))
        # The disposition arguments can use template features
        # Add a few convenience properties
        event.message["properties"] = event.message.get("properties") or {}
        event.message["action_name"] = action_name
        event.message["properties"]["_message_headers"] = event.hdr()

        disposition_args = template_functions.render(disposition_args, event.message)
        # Construct the disposition
        result_disposition = Disposition(self.rest_client(), disposition_args)

        # Run the action based on the template and data;
        # the result is returned as a string.
        evt = task(_shell_run, action_template, event.message)
        LOG.info("shell: %s", action_name)
        ret = yield self.call(evt, "worker")
        result = ret.value
        if isinstance(result, Exception):
            raise result

        if result is None:
            LOG.debug("No result.")
            yield "No result."
        else:
            # Process the result according to the chosen disposition
            LOG.debug("Result: %s", result)
            result_disposition.call(event, result)
            yield "Found result"



class ShellHarness(Component):
    def __init__(self, opts):
        super(ShellHarness, self).__init__()
        self.shell = Shell(opts).register(self)
        logger = logging.getLogger("debugger")
        # logger.setLevel(logging.DEBUG)
        Debugger(logger).register(self)

    def started(self, component):
        print("started")
        Timer(20, Event.create("end")).register(self)
        # Fire some test events
        N = 3
        for loop in range(1, N):
            self.fire(ActionMessage(source="test_thing", headers=None, message={"who": "you"}))
            Timer(1, ActionMessage(source="test_thing", headers=None, message={"who": "me"})).register(self)
            Timer(2, ActionMessage(source="test_thing", headers=None, message={"who": "us"})).register(self)

    def end(self):
        self.stop()
        print("ended")


def main():
    """Tests (for unix)"""
    from app import AppArgumentParser
    opts = AppArgumentParser().parse_args()
    harness = ShellHarness(opts)
    data = {"who": "mister jones", "this": "is the data"}

    # Test basic execution internals (synchronous)
    result = _shell_run('echo "hello there"', {})
    LOG.debug(result)
    assert result == 'hello there\n'

    result = _shell_run('echo "hello {{who}} you"', data)
    LOG.debug(result)
    assert result == 'hello mister jones you\n'

    # Run and block
    harness.run()

    print("done")


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    main()
