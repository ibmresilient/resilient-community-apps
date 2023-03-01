# -*- coding: utf-8 -*-

"""AppFunction implementation"""

import os
import logging
import time
import shlex
import subprocess
import json
import chardet
from fn_network_utilities.util.utils_common import remove_punctuation
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import IntegrationError, validate_fields, render, b_to_s
from resilient_lib.components.templates_common import sh_filter, ps_filter

PACKAGE_NAME = "fn_network_utilities"
FN_NAME = "network_utilities_local_shell_command"

LOG = logging.getLogger(__name__)

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'network_utilities_local_shell_command'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: This function allows your workflows to execute shell-scripts locally, and return the result into the workflow.
        The results include the `stdout` and `stderr` streams, the return code, and information about the execution time.
        If the output of the shell script is JSON, it is returned as structured data. Results can then be added to the incident as file attachments,
        artifacts, data tables, or any other uses.
        Inputs:
            -   fn_inputs.network_utilities_shell_params
            -   fn_inputs.network_utilities_shell_command
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        try:
            # Get the function parameters:
            shell_command = fn_inputs.network_utilities_shell_command  # text
            shell_params = getattr(fn_inputs, "network_utilities_shell_params", None)  # text

            LOG.info("network_utilities_shell_command: %s", shell_command)
            LOG.info("network_utilities_shell_params: %s", shell_params)

            validate_fields(["network_utilities_shell_command"], fn_inputs)

            params_list = shell_params.split(",")
            rendered_shell_params = {}
            for i, param in enumerate(params_list):
                param_name = f"shell_param{i+1}"
                escaping = self.options.get("shell_escaping", "sh")
                if escaping == "sh":
                    rendered_shell_params[param_name] = sh_filter(param)
                else:
                    rendered_shell_params[param_name] = ps_filter(param)

            # Options keys are lowercase, so the shell command name needs to be lowercase
            if shell_command:
                shell_command = shell_command.lower()

            # Check if command is configured
            if shell_command not in self.options:
                if ':' in shell_command:
                    raise ValueError("Syntax for a remote command '%s' was used but remote_shell was set to False"
                                     % shell_command)
                raise ValueError('%s command not configured' % shell_command)

            shell_command_base = self.options[shell_command].strip()

            # Previous version required parentheses around command for linux, this is for backwards compatability
            shell_command_base = remove_punctuation(shell_command_base, "parentheses")

            # Previous version required brackets around command for powershell, this is for backwards compatability
            shell_command_base = remove_punctuation(shell_command_base, "brackets")


            run_cmd = RunCmd(None, shell_command_base, rendered_shell_params)
            run_cmd.run_local_cmd()

            yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

            yield FunctionResult(run_cmd.make_result())
        except Exception as e:
            yield IntegrationError(e)

class RunCmd():
    def __init__(self, remote, shell_command, rendered_shell_params):
        # Get remote credentials
        if remote:
            self.get_creds(remote)

        self.shell_command = shell_command
        self.rendered_shell_params = rendered_shell_params

        self.tstart = time.time()
        self.retcode = None
        self.stdoutdata = None
        self.stderrdata = None

    def get_creds(self, remote):
        server_splits = remote.rsplit('@', 1) # get last separator to avoid '@' in passwords
        if len(server_splits) != 2:
            raise ValueError("Incorrect format for remote. Ex. username:password@server, "
                             "'%s' was specified", remote)

        self.remote_server = server_splits[1]

        user_pswd_splits = server_splits[0].split(':')
        if len(user_pswd_splits) != 2:
            raise ValueError("Incorrect format for remote. Ex. username:password@server, "
                             "'%s' was specified", remote)

        self.remote_user = user_pswd_splits[0]
        self.remote_password = user_pswd_splits[1]


    def run_local_cmd(self):
        shell_command_base = render(self.shell_command, self.rendered_shell_params)

        self.commandline = os.path.expandvars(shell_command_base)
        LOG.debug("local cmd: %s", self.commandline)
        # Set up the environment
        env = os.environ.copy()

        # Execute the command line process (NOT in its own shell)
        cmd = shlex.split(self.commandline, posix=True)
        call = subprocess.Popen(cmd,
                                shell=False,
                                stderr=subprocess.PIPE,
                                stdout=subprocess.PIPE,
                                env=env)
        self.stdoutdata, self.stderrdata = call.communicate()
        self.retcode = call.returncode

        encoding = chardet.detect(self.stdoutdata)["encoding"] or "utf-8"
        self.result = self.stdoutdata.decode(encoding)


    def make_result(self):
        #encoding = chardet.detect(s_to_b(self.stdoutdata))["encoding"] or "utf-8"
        self.tend = time.time()

        result = b_to_s(self.stdoutdata)
        result_json = None
        try:
            # Let's see if the output can be decoded as JSON
            result_json = json.loads(result)
        except:
            pass

        output = b_to_s(self.stderrdata)
        output_json = None
        try:
            # Let's see if the output can be decoded as JSON
            output_json = json.loads(output)
        except:
            pass

        results = {
            "commandline": self.commandline,
            "start": int(self.tstart * 1000.0),
            "end": int(self.tend * 1000.0),
            "elapsed": int((self.tend - self.tstart) * 1000.0),
            "exitcode": self.retcode,  # Nonzero exit code indicates error
            "stdout": result,
            "stderr": output,
            "stdout_json": result_json,  # May be null
            "stderr_json": output_json  # May be null
        }

        return results