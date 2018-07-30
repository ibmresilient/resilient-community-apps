# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2018. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

"""Function implementation"""

import os
import logging
import time
import shlex
import subprocess
import json
import chardet
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_circuits.template_functions import render


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'shell_command"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_utilities", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_utilities", {})

    @function("utilities_shell_command")
    def _shell_command_function(self, event, *args, **kwargs):
        """Function: Runs a shell command."""
        try:
            # Get the function parameters:
            shell_command = self.get_select_param(kwargs.get("shell_command"))  # select, values: "cmdscan", "netscan", "sockscan", "malfind"
            shell_param1 = kwargs.get("shell_param1")  # text
            shell_param2 = kwargs.get("shell_param2")  # text
            shell_param3 = kwargs.get("shell_param3")  # text

            log = logging.getLogger(__name__)
            log.info("shell_command: %s", shell_command)
            log.info("shell_param1: %s", shell_param1)
            log.info("shell_param2: %s", shell_param2)
            log.info("shell_param3: %s", shell_param3)

            # Escape the input parameters
            escaping = self.options.get("shell_escaping", "sh")
            escaped_args = {
                "shell_param1": render(u"{{shell_param1|%s}}" % escaping, kwargs),
                "shell_param2": render(u"{{shell_param2|%s}}" % escaping, kwargs),
                "shell_param3": render(u"{{shell_param3|%s}}" % escaping, kwargs)
            }

            # Substitute parameters into the shell command
            if shell_command not in self.options:
                yield FunctionError(u"Command is not configured: '{}'".format(shell_command))
                return
            shell_command_base = self.options[shell_command]
            commandline = render(shell_command_base, escaped_args)
            commandline = os.path.expandvars(commandline)

            yield StatusMessage(u"Running: {}".format(commandline))

            # Set up the environment
            env = os.environ.copy()

            # Execute the command line process (NOT in its own shell)
            cmd = shlex.split(commandline, posix=True)
            tstart = time.time()
            call = subprocess.Popen(cmd,
                                    shell=False,
                                    stderr=subprocess.PIPE,
                                    stdout=subprocess.PIPE,
                                    env=env)
            stdoutdata, stderrdata = call.communicate()
            retcode = call.returncode
            tend = time.time()

            encoding = chardet.detect(stdoutdata)["encoding"] or "utf-8"
            result = stdoutdata.decode(encoding)
            result_json = None
            try:
                # Let's see if the output can be decoded as JSON
                result_json = json.loads(result)
            except:
                pass

            output = stderrdata.decode(encoding)
            output_json = None
            try:
                # Let's see if the output can be decoded as JSON
                output_json = json.loads(output)
            except:
                pass

            results = {
                "commandline": commandline,
                "start": int(tstart * 1000.0),
                "end": int(tend * 1000.0),
                "elapsed": int((tend-tstart) * 1000.0),
                "exitcode": retcode,            # Nonzero exit code indicates error
                "stdout": result,
                "stderr": output,
                "stdout_json": result_json,     # May be null
                "stderr_json": output_json      # May be null
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
