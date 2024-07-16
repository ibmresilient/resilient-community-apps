# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.

"""
Function implementation test.
Usage: 
    resilient-circuits selftest -l fn-network-utilities
    resilient-circuits selftest --print-env -l fn-network-utilities
Return examples:
    return {
        "state": "success",
        "reason": "Successful connection to third party endpoint"
    }
    return {
        "state": "failure",
        "reason": "Failed to connect to third party endpoint"
    }
"""

import logging
import paramiko
import time
from resilient_circuits.template_functions import render
import winrm

LOG = logging.getLogger(__name__)

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Placeholder for selftest function for a remote computer. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    app_configs = opts.get("fn_network_utilities", {})
    try:
        if app_configs.get("shell_escaping") == "sh":
            run_cmd = RunCmd(app_configs.get("remote_computer"), "ls", {})
            run_cmd.run_remote_linux()
        else:
            run_cmd = RunCmd(app_configs.get("remote_computer"), "dir", {})
            run_cmd.run_windows_cmd(app_configs.get("remote_auth_transport"),
                                    app_configs.get("remote_powershell_extensions").strip(","))
        return {
            "state": "success",
            "reason": "Connected to remote_computer"
        }
    except Exception as e:
        return{
        "state": "failure",
        "reason": e
    }

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