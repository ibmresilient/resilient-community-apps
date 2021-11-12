# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.

"""SentinelOne REST API client"""

import os
import datetime
import logging 
from resilient_lib import validate_fields, IntegrationError

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
        self.cafile = options.get("cafile")
        self.bundle = os.path.expanduser(self.cafile) if self.cafile else False
        self.polling_lookback = int(options.get("polling_lookback", DEFAULT_POLLER_LOOKBACK_MINUTES))

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

    def get_threats(self, last_poller_time):
        """ Return the SentinelOne threats that have been created or updated
            since the last poll time
        """
        url = u"{0}/threats".format(self.base_url)

        # build filter information

        last_poller_datetime_string = self._make_createdate_filter(last_poller_time)
        LOG.debug("last_poller_time: %s", last_poller_datetime_string)

        params = {
            'siteIds': ["607447413779893818"],
            'createdAt__gte': last_poller_datetime_string,
            'updatedAt__gte': last_poller_datetime_string
        }

        response = self.rc.execute("GET", url, headers=self.headers, params=params, 
                                    verify=self.bundle, proxies=self.rc.get_proxies())
        response.raise_for_status()
        return response.json()

    def get_threat_notes(self, threat_id):
        """ Get threat notes for a given threat
        """
        url = u"{0}/threats/{1}/notes".format(self.base_url, threat_id)

        params = {
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

    def query_threats(self, profile_data):
        """Query SentinelOne for all threats created within the last polling window. If first time,
              then use a lookback value.

        Args:
            profile_data ([dict]): [profile to query incidents]

        Returns:
            result [dict]: API results
            status [bool]: True if API call was successful
            reason [str]: Reason of error when status=False
        """

        url = u"{0}/threats".format(self.base_url)

        # build filter information
        last_poller_datetime = self._get_last_poller_date(profile_data)
        last_poller_datetime_string = self._make_createdate_filter(last_poller_datetime)

        params = {
            'siteIds': ["607447413779893818"],
            'createdAt__gte': last_poller_datetime_string
        }

        response = self.rc.execute("GET", url, headers=self.headers, params=params, 
                                    verify=self.bundle, proxies=self.rc.get_proxies())
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

    def _get_last_poller_date(self, profile_data):
        """get the last poller datetime based on a profile. If first time, use the lookback
             parameter to calculate it from the current datetime.

        Args:
            profile_data ([str]): profile to get last poller runtime

        Returns:
            [datetime]: [datetime to use for last poller run time]
        """
        if profile_data.get('last_poller_time'):
            last_poller_datetime = profile_data['last_poller_time']
            LOG.debug("last_poller_time: %s", last_poller_datetime.isoformat())
        else:
            # use lookback value
            last_poller_datetime = datetime.datetime.utcnow() - datetime.timedelta(minutes=self.polling_lookback)

        return last_poller_datetime