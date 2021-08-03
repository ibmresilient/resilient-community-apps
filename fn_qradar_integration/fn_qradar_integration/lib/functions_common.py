# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.

import re

PACKAGE_NAME = "fn_qradar_integration"

class QRadarServers():
    def __init__(self, opts, options):
        self.servers, self.server_name_list = self._load_servers(opts, options)

    def _load_servers(self, opts, options):
        servers = {}
        server_name_list = self._get_server_name_list(opts)
        for server in server_name_list:
            server_name = u"{}".format(server)
            server_data = opts.get(server_name)
            if not server_data:
                raise KeyError(u"Unable to find QRadar server: {}".format(server_name))
            
            servers[server] = server_data
        
        return servers, server_name_list

    def _get_server_name_list(self, opts):
        """
        Return the list of QRadar server names defined in the app.config in fn_qradar_integration. 
        """
        server_list = []
        for key in opts.keys():
            if key.startswith("fn_qradar_integration:"):
                server_name = key
                if len(server_name):
                    server_list.append(server_name)
        return server_list

    def get_server(self, server_name):
        """collect the settings for a QRadar server: host, username, password
        Args:
            server_name ([str]): [name of server in app.config]
        Raises:
            KeyError: [server not found]
        Returns:
            [dict]: [settings for a QRadar server]
        """
        server_name = "fn_qradar_integration"+server_name
        if not server_name in self.servers:
            raise KeyError(u"Unable to find server: {}".format(server_name))

        return self.servers[server_name]

    def get_servers(self):
        """
        Return all servers
        """
        return self.servers

    def get_server_name_list(self):
        """
        Return list of all server names
        """
        return self.server_name_list