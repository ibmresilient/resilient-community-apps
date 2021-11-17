# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.

"""SentinelOne REST API client"""

import os
import datetime
import logging 
from resilient_lib import validate_fields, IntegrationError, str_to_bool

LOG = logging.getLogger(__name__)

DEFAULT_POLLER_LOOKBACK_MINUTES = 120

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

        self.verify = str_to_bool(options.get("verify", "true"))

        self.polling_lookback = int(options.get("polling_lookback", DEFAULT_POLLER_LOOKBACK_MINUTES))
        site_ids = options.get("site_ids")
        self.site_ids = site_ids.split(",") if site_ids else []
        account_ids = options.get("account_ids")
        self.account_ids = account_ids.split(",") if account_ids else []        
        self.query_param = options.get("query_param", None)

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
                                    verify=self.verify, proxies=self.rc.get_proxies())
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
                                    verify=self.verify, proxies=self.rc.get_proxies())
        response.raise_for_status()
        return response.json()

    def get_agents_passphrases(self):
        """ Return the list of agents matching the filter 
        """
        url = u"{0}/agents/passphrases".format(self.base_url)
        params = {
            'accountIds': self.account_ids,
            'siteIds': self.site_ids
        }
        response = self.rc.execute("GET", url, headers=self.headers, params=params, 
                                    verify=self.verify, proxies=self.rc.get_proxies())
        response.raise_for_status()
        return response.json()

    def get_threat_details(self, threat_id):
        """ Return the details of a threat
        """
        url = u"{0}/threats".format(self.base_url)

        params = {
            'ids': threat_id
        }

        response = self.rc.execute("GET", url, headers=self.headers, params=params, 
                                    verify=self.verify, proxies=self.rc.get_proxies())
        response.raise_for_status()
        return response.json()

    def get_threats(self, last_poller_time):
        """ Return the SentinelOne threats that have been created or updated
            since the last poll time
        """
        # Build filter information
        last_poller_datetime_string = self._make_createdate_filter(last_poller_time)
        LOG.debug("last_poller_time: %s", last_poller_datetime_string)

        # Get the newly created threats
        params = {
            'accountIds': self.account_ids,
            'siteIds': self.site_ids,
            'query': self.query_param,
            'createdAt__gte': last_poller_datetime_string
        }

        threats = []
        new_threat_ids = []
        threats = (self._get_threats(params))

        # Create a list of new threat ids to compare against updated threat ids so there are no duplicates
        for threat in threats:
            threat_info = threat.get("threatInfo")
            threat_id = threat_info.get("threatId")
            new_threat_ids.append(threat_id)

        # Get the updated threats
        params = {
            'accountIds': self.account_ids,
            'siteIds': self.site_ids,
            'query': self.query_param,
            'updatedAt__gte': last_poller_datetime_string
        }

        updated_threats = self._get_threats(params)

        for updated_threat in updated_threats:
            threat_info = updated_threat.get("threatInfo")
            threat_id = threat_info.get("threatId")
            if threat_id not in new_threat_ids:
                threats.append(updated_threat)
        return threats

    def _get_threats(self, params):
        """ Return the SentinelOne threats that match the filter
        """
        url = u"{0}/threats".format(self.base_url)
        threats = []

        # nextCursor is a pagination field that points to the next page of threats
        # Set it to non null string so we go through the while loop at least once
        nextCursor = "true"

        while nextCursor:
            response = self.rc.execute("GET", url, headers=self.headers, params=params, 
                                        verify=self.verify, proxies=self.rc.get_proxies())
            response.raise_for_status()
            response_json = response.json()
            pagination = response_json.get("pagination")
            nextCursor = pagination.get("nextCursor")
            # Update the url to get the next page of threats next time through the loop
            if nextCursor:
                url = u"{0}/threats?cursor={1}".format(self.base_url, nextCursor)
            data = response_json.get("data")
            for threat in data:
                threats.append(threat)
        return threats

    def get_threat_notes(self, threat_id):
        """ Get threat notes for a given threat
        """
        url = u"{0}/threats/{1}/notes".format(self.base_url, threat_id)

        params = {
        }

        response = self.rc.execute("GET", url, headers=self.headers, params=params, 
                                    verify=self.verify, proxies=self.rc.get_proxies())
        response.raise_for_status()
        return response.json()


    def get_system_info(self):
        """ Get threat notes for a given threat
        """
        url = u"{0}/system/info".format(self.base_url)

        params = {
        }

        response = self.rc.execute("GET", url, headers=self.headers, params=params, 
                                    verify=self.verify, proxies=self.rc.get_proxies())
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
                                    verify=self.verify, proxies=self.rc.get_proxies())
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
                                    verify=self.verify, proxies=self.rc.get_proxies())
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
                                    verify=self.verify, proxies=self.rc.get_proxies())
        response.raise_for_status()
        return response.json()

    def _make_createdate_filter(self, last_poller_datetime):
        """build the $filter parameter to find incidents by last poller run datetime

        Args:
            last_poller_datetime ([datetime]): [last poller time]

        Returns:
            [str]: [$filter string to use]
        """
        last_poller_datetime_iso = last_poller_datetime.isoformat()

        # remove milliseconds
        return "{lookback_date}Z".format(lookback_date=last_poller_datetime_iso[:last_poller_datetime_iso.rfind('.')])
