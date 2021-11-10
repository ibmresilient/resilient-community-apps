# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.

"""SentinelOne REST API client"""

import os
import logging 
from resilient_lib import validate_fields, IntegrationError

LOG = logging.getLogger(__name__)


class SentinelOneClient(object):
    def __init__(self, options, rc):
        # Read the configuration options
        required_fields = ["sentinelone_server", "api_token", "api_version"]
        validate_fields(required_fields, options)
        self.rc = rc
        self.api_version = options.get("api_version")
        self.server = options.get("sentinelone_server")
        self.base_url = u"https://{0}/web/api/v{1}".format(self.server, self.api_version)
        self.api_token = options.get("api_token")
        self.cafile = options.get("cafile")
        self.bundle = os.path.expanduser(self.cafile) if self.cafile else False

        self.headers = self.get_headers(self.api_token)
    

    def get_headers(self, auth_token):
        """ Return the authorization header.
        """
        headers = {
            'Authorization': u'ApiToken {0}'.format(auth_token),
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        return headers

    def get_agents(self, params):
        """ Return the list of agents matching the filter 
        """
        url = u"{0}/agents".format(self.base_url)

        response = self.rc.execute("GET", url, headers=self.headers, params=params, 
                                    verify=self.bundle, proxies=self.rc.get_proxies())
        response.raise_for_status()
        return response.json()

    def get_agent_details(self, agent_id):
        """ Return the details of an agent
        """
        url = u"{0}/agents".format(self.base_url)

        params = {
            'ids': agent_id
        }

        response = self.rc.execute("GET", url, headers=self.headers, params=params, 
                                    verify=self.bundle, proxies=self.rc.get_proxies())
        response.raise_for_status()
        return response.json()

    def get_threats(self):
        """ Return the details of an agent
        """
        url = u"{0}/threats".format(self.base_url)

        params = {
            'siteIds': ["607447413779893818"]
        }

        response = self.rc.execute("GET", url, headers=self.headers, params=params, 
                                    verify=self.bundle, proxies=self.rc.get_proxies())
        response.raise_for_status()
        return response.json()

    def connect_to_network(self, agents_id):
        """ Connect the endpoint to the network
        """
        url = u"{0}/agents/actions/connect".format(self.base_url)

        payload = {
            "filter": {
                "ids": agents_id
            },
            "data": {}
        }

        response = self.rc.execute("POST", url, headers=self.headers, json=payload, 
                                    verify=self.bundle, proxies=self.rc.get_proxies())
        response.raise_for_status()
        return response.json()

    def disconnect_from_network(self, agents_id):
        """ Disconnect the endpoint from the network
        """
        url = u"{0}/agents/actions/disconnect".format(self.base_url)

        payload = {
            "filter": {
                "ids": agents_id
            },
            "data": {}
        }

        response = self.rc.execute("POST", url, headers=self.headers, json=payload, 
                                    verify=self.bundle, proxies=self.rc.get_proxies())
        response.raise_for_status()
        return response.json()

    def initiate_scan(self, agents_id):
        """ Disconnect the endpoint from the network
        """
        url = u"{0}/agents/actions/initiate-scan".format(self.base_url)

        payload = {
            "filter": {
                "ids": agents_id
            },
            "data": {}
        }

        response = self.rc.execute("POST", url, headers=self.headers, json=payload, 
                                    verify=self.bundle, proxies=self.rc.get_proxies())
        response.raise_for_status()
        return response.json()
