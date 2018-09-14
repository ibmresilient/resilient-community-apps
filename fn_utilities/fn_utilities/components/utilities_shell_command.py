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
import winrm
import re
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
            shell_command = kwargs.get('shell_command')  # text
            shell_remote = kwargs.get("shell_remote")  # boolean
            shell_param1 = kwargs.get("shell_param1")  # text
            shell_param2 = kwargs.get("shell_param2")  # text
            shell_param3 = kwargs.get("shell_param3")  # text

            log = logging.getLogger(__name__)
            log.info("shell_command: %s", shell_command)
            log.info("shell_remote: %s", shell_remote)
            log.info("shell_param1: %s", shell_param1)
            log.info("shell_param2: %s", shell_param2)
            log.info("shell_param3: %s", shell_param3)

            # Options keys are lowercase, so the shell command name needs to be lowercase
            if shell_command:
                shell_command = shell_command.lower()

            # Escape the input parameters
            escaping = self.options.get("shell_escaping", "sh")
            escaped_args = {
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
                                             "%s was specfied" % remote)

                # Get remote credentials
                remote_config = re.split(':|@', remote)
                if len(remote_config) != 3:
                    raise ValueError('Remote machine %s must be of the format username:password@server, '
                                     "'%s' was specified" % remote)
                else:
                    remote_user = remote_config[0]
                    remote_password = remote_config[1]
                    remote_server = remote_config[2]

            # Check if command is configured
            if shell_command not in self.options:
                if ':' in shell_command:
                    raise ValueError("Syntax for a remote command '%s' was used but remote_shell was set to False"
                                     % shell_command)
                raise ValueError('%s command not configured' % shell_command)

            shell_command_base = self.options[shell_command].strip()

            # Remote commands must wrap a path with []
            if shell_command_base.startswith('[') and shell_command_base.endswith(']'):
                if shell_remote:
                    extension = shell_command_base[1:-1].strip().split('.')[-1]
                    if extension not in self.options.get('remote_powershell_extensions'):
                        raise ValueError("The specified file must be have extension %s but %s was specified" %
                                         (str(self.options.get('remote_powershell_extensions')), extension))

                    # Format shell parameters
                    shell_command_base = shell_command_base[1:-1].strip()
                    if shell_param1:
                        shell_command_base = shell_command_base + ' "{{shell_param1}}"'
                    else:
                        shell_command_base = shell_command_base + ' $null'
                    if shell_param2:
                        shell_command_base = shell_command_base + ' "{{shell_param2}}"'
                    else:
                        shell_command_base = shell_command_base + ' $null'
                    if shell_param3:
                        shell_command_base = shell_command_base + ' "{{shell_param3}}"'
                    else:
                        shell_command_base = shell_command_base + ' $null'

                else:
                    raise ValueError("A remote command '%s' was specified but shell_remote was set to False"
                                     % shell_command)
            elif shell_remote:
                raise ValueError('A remote command must specify a remote path wrapped in square brackets [], '
                                 "'%s' was specified" % shell_command)

            if shell_command_base.startswith('(') and shell_command_base.endswith(')') and not shell_remote:
                raise ValueError('Please specify a valid shell command that is not wrapped in parentheses or brackets'
                                 'when shell_remote is False')

            commandline = render(shell_command_base, escaped_args)

            if shell_remote:
                session = winrm.Session(remote_server,
                                        auth=(remote_user, remote_password),
                                        transport=self.options.get('remote_auth_transport'))
                tstart = time.time()
                if escaping == "sh":
                    r = session.run_cmd(commandline)
                elif escaping == "ps":
                    r = session.run_ps(commandline)
                retcode = r.status_code
                stdoutdata = r.std_out
                stderrdata = r.std_err
                tend = time.time()
            else:
                commandline = os.path.expandvars(commandline)
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
                "elapsed": int((tend - tstart) * 1000.0),
                "exitcode": retcode,  # Nonzero exit code indicates error
                "stdout": result,
                "stderr": output,
                "stdout_json": result_json,  # May be null
                "stderr_json": output_json  # May be null
            }

            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
