# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

"""Function implementation"""

import os
import logging
import time
import shlex
import subprocess
import json
import chardet
import paramiko
import winrm
import re
from fn_utilities.util.utils_common import s_to_b, b_to_s
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_circuits.template_functions import render

LOG = logging.getLogger(__name__)

class FunctionComponent(ResilientComponent):
    """Component that implements SOAR function 'shell_command"""

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
            shell_command = kwargs.get('shell_command')  # text
            shell_remote = kwargs.get("shell_remote")  # boolean
            shell_param1 = kwargs.get("shell_param1")  # text
            shell_param2 = kwargs.get("shell_param2")  # text
            shell_param3 = kwargs.get("shell_param3")  # text

            LOG.info("shell_command: %s", shell_command)
            LOG.info("shell_remote: %s", shell_remote)
            LOG.info("shell_param1: %s", shell_param1)
            LOG.info("shell_param2: %s", shell_param2)
            LOG.info("shell_param3: %s", shell_param3)

            # Options keys are lowercase, so the shell command name needs to be lowercase
            if shell_command:
                shell_command = shell_command.lower()

            # Escape the input parameters
            escaping = self.options.get("shell_escaping", "sh")
            rendered_shell_params = {
                "shell_param1": render(u"{{shell_param1|%s}}" % escaping, kwargs),
                "shell_param2": render(u"{{shell_param2|%s}}" % escaping, kwargs),
                "shell_param3": render(u"{{shell_param3|%s}}" % escaping, kwargs)
            }

            # If running a remote script, get the remote computer and the remote command
            if shell_remote:
                colon_split = shell_command.split(':')
                if len(colon_split) != 2:
                    raise ValueError("Remote commands must be of the format remote_command_name:remote_computer_name, "
                                     "'%s' was specified" % shell_command)
                else:
                    shell_command = colon_split[0].strip()
                    if self.options.get(colon_split[1]) is None:
                        raise ValueError('The remote computer %s is not configured' % colon_split[1])
                    else:
                        remote = self.options.get(colon_split[1]).strip()
                        if remote.startswith('(') and remote.endswith(')'):
                            remote = remote[1:-1]
                        else:
                            raise ValueError('Remote computer configurations must be wrapped in parentheses (), '
                                             "%s was specified" % remote)

            # Check if command is configured
            if shell_command not in self.options:
                if ':' in shell_command:
                    raise ValueError("Syntax for a remote command '%s' was used but remote_shell was set to False"
                                     % shell_command)
                raise ValueError('%s command not configured' % shell_command)

            shell_command_base = self.options[shell_command].strip()

            # Remote commands must wrap a path with []
            if shell_remote:
                if shell_command_base.startswith('[') and shell_command_base.endswith(']'):
                    run_cmd = RunCmd(remote, shell_command_base[1:-1].strip(), rendered_shell_params)

                    run_cmd.run_windows_cmd(self.options.get('remote_auth_transport'),
                                            self.options.get('remote_powershell_extensions', '').strip(","))

                # linux remote cmd
                elif shell_command_base.startswith('(') and shell_command_base.endswith(')'):
                    run_cmd = RunCmd(remote, shell_command_base[1:-1].strip(), rendered_shell_params)
                    run_cmd.run_remote_linux()

                else:
                    raise ValueError('A remote command must specify a remote path wrapped in square brackets [] for Windows and parentheses () for Linux, '
                                     "'%s' was specified" % shell_command)

            # local command
            else:
                run_cmd = RunCmd(None, shell_command_base, rendered_shell_params)
                run_cmd.run_local_cmd()

            yield FunctionResult(run_cmd.make_result())
        except Exception:
            yield FunctionError()

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


    def run_windows_cmd(self, remote_auth_transport, ps_extensions):

        # Format shell parameters
        shell_command_base = self.shell_command
        extension = shell_command_base[1:-1].strip().split('.')[-1]

        session = winrm.Session(self.remote_server,
                                auth=(self.remote_user, self.remote_password),
                                transport=remote_auth_transport, server_cert_validation="ignore")

        self.commandline = render(shell_command_base, self.rendered_shell_params)
        LOG.debug("Windows cmd: %s", self.commandline)

        if extension in ps_extensions:
            shell_command_base = shell_command_base + (' "{{shell_param1}}"' if self.rendered_shell_params['shell_param1'] else ' $null')
            shell_command_base = shell_command_base + (' "{{shell_param2}}"' if self.rendered_shell_params['shell_param2'] else ' $null')
            shell_command_base = shell_command_base + (' "{{shell_param3}}"' if self.rendered_shell_params['shell_param3'] else ' $null')
            self.commandline = render(shell_command_base, self.rendered_shell_params)

            r = session.run_ps(self.commandline)
        else:
            self.commandline = render(shell_command_base, self.rendered_shell_params)
            r = session.run_cmd(self.commandline)

        self.retcode = r.status_code
        self.stdoutdata = r.std_out
        self.stderrdata = r.std_err


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

    def run_remote_linux(self):
        self.commandline = render(self.shell_command, self.rendered_shell_params)
        LOG.debug("Remote cmd: %s", self.commandline)

        # initialize the SSH client
        client = paramiko.SSHClient()
        # add to known hosts
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            client.connect(hostname=self.remote_server, username=self.remote_user, 
                           password=self.remote_password)

            stdin, stdout, stderr = client.exec_command(self.commandline) # nosec
            self.stdoutdata = stdout.read().decode()
            self.stderrdata = stderr.read().decode()
            self.retcode = stdout.channel.recv_exit_status()
        except Exception as err:
            self.stderrdata = str(err)
            LOG.error(str(err))
            LOG.error("Unable to run cmd: %s on remote server: %s", self.commandline,
                                                                    self.remote_server)


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
