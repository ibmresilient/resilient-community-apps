# -*- coding: utf-8 -*-

"""AppFunction implementation"""

import logging
import time
import shlex
import json
import paramiko
from fn_network_utilities.util.utils_common import remove_punctuation
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import IntegrationError, validate_fields, render, b_to_s
from resilient_lib.components.templates_common import sh_filter

PACKAGE_NAME = "fn_network_utilities"
FN_NAME = "network_utilities_linux_shell_command"
DEFAULT_TIMEOUT_SEC = 20

LOG = logging.getLogger(__name__)

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'network_utilities_linux_shell_command'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: This function allows your workflows/playbooks to execute shell-scripts remotely via a linux machine, and return the result into the workflow/playbook.
        The results include the `stdout` and `stderr` streams, the return code, and information about the execution time. If the output of the shell script is JSON,
        it is returned as structured data. Results can then be added to the incident as file attachments, artifacts, data tables, or any other uses.
        Inputs:
            -   fn_inputs.network_utilities_shell_params
            -   fn_inputs.network_utilities_shell_command
            -   fn_inputs.network_utilities_remote_computer
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        # Get the function parameters:
        shell_command = fn_inputs.network_utilities_shell_command  # text
        shell_params = getattr(fn_inputs, "network_utilities_shell_params", None)  # text
        remote_computer = getattr(fn_inputs, "network_utilities_remote_computer", None) #text
        if self.options.get("timeout_linux") is not None:
            timeout_sec = int(self.options.get("timeout_linux"))
        else: 
            timeout_sec = DEFAULT_TIMEOUT_SEC

        LOG.info(f"network_utilities_shell_command: {shell_command}")
        LOG.info(f"network_utilities_shell_params: {shell_params}")
        LOG.info(f"network_utilities_remote_computer: {remote_computer}")
        LOG.info(f"network_utilities_timeout_sec: {timeout_sec}")

        validate_fields(["network_utilities_shell_command"], fn_inputs)


        params_list = shell_params.split(",")
        rendered_shell_params = {}
        for i, param in enumerate(params_list):
            param_name = f"shell_param{i+1}"
            rendered_shell_params[param_name] = sh_filter(param)

        # Options keys are lowercase, so the shell command name needs to be lowercase
        if shell_command:
            shell_command = shell_command.lower()

        # Get the remote computer and the remote command
        colon_split = shell_command.split(':')
        if len(colon_split) != 2 and remote_computer is None:
            raise ValueError(f"Remote commands must be of the format remote_command_name:remote_computer_name"
                                "or have remote_computer defined, {shell_command} was specified")
        elif len(colon_split) == 2:
            if remote_computer:
                raise ValueError('A remote computer is configured in both network_utilities_remote_computer and network_utilities_shell_command. Choose one to use.')
            elif self.options.get(colon_split[1]) is None:
                raise ValueError(f'The remote computer {colon_split[1]} is not configured')
            else:
                remote = self.options.get(colon_split[1]).strip()
        else:
            remote = remote_computer

        shell_command = colon_split[0].strip()

        # Previous version required parenthesis around remote computer, this is for backwards compatability
        remote = remove_punctuation(remote, True)

        # Check if command is configured
        if shell_command not in self.options:
            if ':' in shell_command:
                raise ValueError(f"Syntax for a remote command {shell_command} was used but remote_shell was set to False")
            raise ValueError(f"{shell_command} command not configured")

        shell_command_base = self.options[shell_command].strip()

        # Previous version required parenthesis around command, this is for backwards compatability
        shell_command_base = remove_punctuation(shell_command_base, True)

        run_cmd = RunCmd(remote, shell_command_base.strip(), rendered_shell_params)
        run_cmd.run_remote_linux(timeout_sec)

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        yield FunctionResult(run_cmd.make_result())

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
                             f"{remote} was specified")

        self.remote_server = server_splits[1]

        user_pswd_splits = server_splits[0].split(':')
        if len(user_pswd_splits) != 2:
            raise ValueError("Incorrect format for remote. Ex. username:password@server, "
                             f"{remote} was specified")

        self.remote_user = user_pswd_splits[0]
        self.remote_password = user_pswd_splits[1]


    def run_remote_linux(self, timeout_sec):
        self.commandline = render(self.shell_command, self.rendered_shell_params)
        LOG.debug("Remote cmd: %s", self.commandline)

        # initialize the SSH client
        client = paramiko.SSHClient()
        # add to known hosts
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            client.connect(hostname=self.remote_server, username=self.remote_user, 
                        password=self.remote_password)

            stdin, stdout, stderr = client.exec_command(self.commandline, timeout=timeout_sec) # nosec
            self.stdoutdata = stdout.read().decode()
            self.stderrdata = stderr.read().decode()
            self.retcode = stdout.channel.recv_exit_status()
        except Exception as err:
            self.stderrdata = str(err)
            LOG.error(str(err))
            LOG.error(f"Unable to run cmd: {self.commandline} on remote server: {self.remote_server}")


    def make_result(self):
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