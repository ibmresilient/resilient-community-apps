# -*- coding: utf-8 -*-
# Copyright © IBM Corporation 2010, 2020
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.

import six
from paramiko import SSHClient, AutoAddPolicy, ProxyCommand
from paramiko_expect import SSHClientInteraction


class ParamikoSSH(SSHClient):
    """
    A class that represents an SSH Paramiko connection.  Class object type is 'SSHClient' (from Paramiko).
    """

    def __init__(self, host, username, password, port=None, timeout=None, missing_host_key_policy=True, sock=None):
        """

        Args:
            host: IP or hostname of the host that is being connected to via SSH.
            port: SSH port number (SSH default is 22).
            username:
            password:
            timeout(int; seconds): SSH connection timeout.  Default is 30 seconds.
            missing_host_key_policy:
            sock (channel paramiko): paramiko socket or proxy command to be in transport.
        """
        if six.PY3:
            super().__init__()
        else:
            super(ParamikoSSH, self).__init__()

        self.host = host
        self.username = username
        self.password = password
        self.port = port or 22
        self.timeout = timeout or 30
        self.sock = ProxyCommand(sock) if sock else sock
        self.prompt = '.*> $'

        if missing_host_key_policy:
            self.set_missing_host_key_policy(AutoAddPolicy())

        self.connect(self.host, port=self.port, username=self.username, password=self.password, timeout=self.timeout,
                     sock=self.sock)
        self.interact = SSHClientInteraction(self, display=False, newline='\n')

        self.interact.expect('.*$')
        self.interact.send('')
        self.interact.expect(self.prompt)

    def exec_cmd(self, command, print_stdout=True):
        """
        Executes a command within a paramiko SSH connection.

        Args:
            command(str):
            print_stdout(True/False):

        Returns: stdout

        """
        self.interact.send(command)
        self.interact.expect(self.prompt)
        stdout = self.interact.current_output_clean

        if print_stdout:
            print(stdout)

        return stdout

    def open_direct_tcpip_channel(self, dest_ssh_host, dest_ssh_port, local_ssh_host, local_ssh_port):
        """
        Opens a channel based on an existing SSH connection so that 'nested' SSH connections can be made

        Args:
            dest_ssh_host(str): hostname/IP of remote ssh server
            dest_ssh_port(int): port of remote ssh server
            local_ssh_host (str): hostname/IP of local ssh connection; 127.0.0.1
            local_ssh_port(int): port of local ssh connection

        Returns: channel

        """
        __dest_ssh = (dest_ssh_host, dest_ssh_port)  # (tuple): hostname/IP, port of remote ssh server
        __local_ssh = (local_ssh_host, local_ssh_port)  # local_ssh (tuple): hostname/IP, port of local ssh connection

        transport = self.get_transport()
        channel = transport.open_channel("direct-tcpip", __dest_ssh, __local_ssh)

        return channel
