# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""
This module contains ProxySMTP class which is derived from the Python smtplib.SMTP (Simple Mail Transport Protocol)
class. If proxy parameters are defined when the ProxySMTP class is initialized, then it will call the
appropriate
"""
import sys
import smtplib
import socket
import socks


# CRLF binary representation for compatibility with Python 3
if sys.version_info.major >= 3:
    bCRLF = smtplib.bCRLF
else:
    bCRLF = smtplib.CRLF

class NotSupportedProxyType(socks.ProxyError):
    """Not supported proxy type provided
    Exception is raised when provided proxy type is not supported.
    See socks.py for supported types.
    """

class ProxySMTP(smtplib.SMTP):
    """This class manages a connection to an SMTP or ESMTP server.
    HTTP/SOCKS4/SOCKS5 proxy servers are supported
    For additional information see smtplib.py
    """

    def __init__(self, host='', port=0, proxy_host='', proxy_port=0, proxy_username=None, proxy_password=None,
                 proxy_type=socks.HTTP, local_hostname=None, timeout=socket._GLOBAL_DEFAULT_TIMEOUT,
                 source_address=None):
        """Initialize a new instance.
        If a host is specified the connect method is called, and if it returns anything other than a
        success code an SMTPConnectError is raised
        :param host: Hostname of SMTP server
        :type host: string
        :param port: Port of SMTP server, by default smtplib.SMTP_PORT is used
        :type port: int
        :param proxy_host: Hostname of proxy server
        :type proxy_host: string
        :param proxy_port: Port of proxy server, by default port for specified  proxy type is used
        :type proxy_port: int
        :param proxy_username: Username of proxy server
        :type proxy_username: string
        :param proxy_password: Password of proxy server
        :type proxy_password: string
        :param proxy_type: Proxy type to use (see socks.PROXY_TYPES for details)
        :type proxy_type: int
        :param local_hostname: Local hostname is used as the FQDN of the local host for the
            HELO/EHLO command, if not specified the local hostname is found using socket.getfqdn()
        :type local_hostname: string
        :param timeout: Connection timeout
        :type timeout: int
        :param source_address: Host and port for the socket to bind to as its source address before
            connecting
        :type source_address: tuple
        """
        self._host = host
        self.timeout = timeout
        self.esmtp_features = {}
        self.command_encoding = 'ascii'
        self.source_address = source_address
        if host:
            if proxy_host:
                (code, msg) = self.connect_proxy(proxy_host, proxy_port, proxy_type, proxy_username, proxy_password,
                                                 host, port)
            else:
                (code, msg) = self.connect(host, port)
            if code != 220:
                raise smtplib.SMTPConnectError(code, msg)
        if local_hostname is not None:
            self.local_hostname = local_hostname
        else:
            # RFC 2821 says we should use the fqdn in the EHLO/HELO verb, and
            # if that can't be calculated, that we should use a domain literal
            # instead (essentially an encoded IP address like [A.B.C.D]).
            fqdn = socket.getfqdn()
            if '.' in fqdn:
                self.local_hostname = fqdn
            else:
                # We can't find an fqdn hostname, so use a domain literal
                addr = '127.0.0.1'
                try:
                    addr = socket.gethostbyname(socket.gethostname())
                except socket.gaierror:
                    pass
                self.local_hostname = '[%s]' % addr

    def _get_socket(self, host, port, timeout):
        # This makes it simpler for SMTP_SSL to use the SMTP connect code
        # and just alter the socket connection bit.
        return socket.create_connection((host, port), timeout, self.source_address)

    def connect_proxy(self, proxy_host='localhost', proxy_port=0, proxy_type=socks.HTTP, proxy_username='',
                      proxy_password='', host='localhost', port=0):
        """Connect to a host on a given port via proxy server
        If the hostname ends with a colon (`:') followed by a number, and
        there is no port specified, that suffix will be stripped off and the
        number interpreted as the port number to use.
        Note: This method is automatically invoked by __init__, if a host and proxy server are
        specified during instantiation.
        :param proxy_host: Hostname of proxy server
        :type proxy_host: string
        :param proxy_port: Port of proxy server, by default port for specified  proxy type is used
        :type proxy_port: int
        :param proxy_type: Proxy type to use (see socks.PROXY_TYPES for details)
        :type proxy_type: int
        :param host: Hostname of SMTP server
        :type host: string
        :param port: Port of SMTP server, by default smtplib.SMTP_PORT is used
        :type port: int
        :return: Tuple of (code, msg)
        :rtype: tuple
        """
        if proxy_type not in socks.DEFAULT_PORTS.keys():
            raise NotSupportedProxyType

        if not proxy_port:
            proxy_port = socks.DEFAULT_PORTS[proxy_type]

        try:
            # Create the socket and set the proxy and timeout parameter
            self.sock = socks.socksocket()
            self.sock.set_proxy(proxy_type=proxy_type, addr=proxy_host, port=proxy_port, rdns=True,
                                username=proxy_username, password=proxy_password)
            self.sock.settimeout(self.timeout)

            #
            if self.source_address is not None:
                self.sock.bind(self.source_address)

            # Connect to the host through the proxy
            self.sock.connect((host, port))

            # Send CRLF in order to get first response from destination server.
            self.sock.sendall(bCRLF)

        except OSError as err:
            if self.sock:
                self.sock.close()
            self.sock = None
            raise err

        (code, msg) = self.getreply()
        return code, msg
