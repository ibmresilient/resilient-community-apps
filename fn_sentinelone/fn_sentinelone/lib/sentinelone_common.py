# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

"""SentinelOne REST API client"""

from io import BytesIO
import logging 
from resilient_lib import RequestsCommon, IntegrationError, validate_fields, str_to_bool
from resilient_lib.components.requests_common import DEFAULT_TIMEOUT

LOG = logging.getLogger(__name__)

DEFAULT_POLLER_LOOKBACK_MINUTES = 120
DEFAULT_LIMIT = 25
DEFAULT_SORT_BY = "createdDate"
DEFAULT_SORT_ORDER = "desc"

class SentinelOneClient(object):
    def __init__(self, opts, options):
        # Read the configuration options
        required_fields = ["sentinelone_server", "api_token", "api_version"]
        validate_fields(required_fields, options)
        self.rc = RequestsCommon(opts, options)
        self.api_version = options.get("api_version")
        self.server = options.get("sentinelone_server")
        self.base_url = u"https://{0}/web/api/v{1}".format(self.server, self.api_version)
        self.api_token = options.get("api_token")

        self.verify = str_to_bool(options.get("verify", "true"))

        self.polling_lookback = int(options.get("polling_lookback", DEFAULT_POLLER_LOOKBACK_MINUTES))
        site_ids = options.get("site_ids")
        self.site_ids = site_ids if site_ids else []
        account_ids = options.get("account_ids")
        self.account_ids = account_ids if account_ids else []
        self.limit = options.get("limit", DEFAULT_LIMIT)
        self.sort_by = options.get("sort_by", DEFAULT_SORT_BY)
        self.sort_order = options.get("sort_order", DEFAULT_SORT_ORDER)
        self.query_param = options.get("query_param", None)
        self.incident_statuses = options.get("incident_statuses", "in_progress,unresolved")
        self.send_soar_link_to_sentinelone = str_to_bool(options.get("send_soar_link_to_sentinelone", "true"))
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

        return response.json()

    def get_threat_details(self, threat_id):
        """ Return the details (JSON object) of a threat
        """
        url = u"{0}/threats".format(self.base_url)

        params = {
            'ids': threat_id
        }

        response = self.rc.execute("GET", url, headers=self.headers, params=params, 
                                    verify=self.verify, proxies=self.rc.get_proxies())

        return response.json()

    def get_threats_by_time(self, last_poller_time):
        """ Return the a list of SentinelOne threats that have been created or updated
            since the last poll time.
        """
        # Build filter information
        last_poller_datetime_string = self._make_createdate_filter(last_poller_time)
        LOG.debug("last_poller_time: %s", last_poller_datetime_string)

        # Return newly created and updated threats in a single update_threats list.
        # Seems like we need to make two separate API calls to get both lists.
        updated_threats = []

        # Get the updated threats
        params = {
            'accountIds': self.account_ids,
            'siteIds': self.site_ids,
            'query': self.query_param,
            'limit': self.limit,
            'sortBy': self.sort_by,
            'sortOrder': self.sort_order,
            'incidentStatuses': self.incident_statuses,
            'updatedAt__gte': last_poller_datetime_string
        }

        updated_threats = self.get_threats(params)

        # Get the newly created threats
        params = {
            'accountIds': self.account_ids,
            'siteIds': self.site_ids,
            'query': self.query_param,
            'limit': self.limit,
            'sortBy': self.sort_by,
            'sortOrder': self.sort_order,
            'incidentStatuses': self.incident_statuses,
            'createdAt__gte': last_poller_datetime_string
        }

        created_threats = self.get_threats(params)

        updated_threat_ids = []
        # Create a list of updated threat ids to compare against created threat ids so 
        # there are no duplicates
        for threat in updated_threats:
            threat_info = threat.get("threatInfo")
            threat_id = threat_info.get("threatId")
            updated_threat_ids.append(threat_id)

        # Add created threats to the update threats list
        for threat in created_threats:
            threat_info = threat.get("threatInfo")
            threat_id = threat_info.get("threatId")
            if threat_id not in updated_threat_ids:
                updated_threats.append(threat)
        return updated_threats

    def get_threats(self, params):
        """ Return the SentinelOne threats that match the filter
        """
        url = u"{0}/threats".format(self.base_url)
        threats = []

        # nextCursor is a pagination field that points to the next page of threats
        # Set it to non null string so we go through the while loop at least once.
        # nextCursor will equal null when list of threats is complete. 
        nextCursor = "true"

        while nextCursor:
            response = self.rc.execute("GET", url, headers=self.headers, params=params, 
                                        verify=self.verify, proxies=self.rc.get_proxies())

            response_json = response.json()
            pagination = response_json.get("pagination")
            nextCursor = pagination.get("nextCursor")
            data = response_json.get("data")
            for threat in data:
                threats.append(threat)
            # Update the url to get the next page of threats next time through the loop
            if nextCursor:
                url = u"{0}/threats?cursor={1}".format(self.base_url, nextCursor)

        return threats

    def get_threat_notes(self, threat_id):
        """ Get threat notes for a given threat
        """
        url = u"{0}/threats/{1}/notes".format(self.base_url, threat_id)

        params = {
        }

        threat_notes = []
        nextCursor = "true"
        
        # nextCursor will be null when the list of threat notes is complete.
        while nextCursor:
            response = self.rc.execute("GET", url, headers=self.headers, params=params, 
                                        verify=self.verify, proxies=self.rc.get_proxies())

            response_json = response.json()
            pagination = response_json.get("pagination")
            nextCursor = pagination.get("nextCursor")
            data = response_json.get("data")
            for note in data:
                threat_notes.append(note)
            # Update the url to get the next page of threat notes next time through the loop
            if nextCursor:
                url = u"{0}/threats/{1}/notes?cursor={2}".format(self.base_url, threat_id, nextCursor)

        return threat_notes

    def add_threat_note(self, threat_id, note_text):
        """ Add threat note to a threat
        """
        url = u"{0}/threats/notes".format(self.base_url, threat_id)

        payload = {
            "filter": {
                "ids": threat_id
            },
            "data": {
                "text": note_text
            }
        }

        response = self.rc.execute("POST", url, headers=self.headers, json=payload, 
                                    verify=self.verify, proxies=self.rc.get_proxies())
        return response.json()

    def get_system_info(self):
        """ Get SentinelOne management console sytem info.
        """
        url = u"{0}/system/info".format(self.base_url)

        params = {
        }

        response = self.rc.execute("GET", url, headers=self.headers, params=params, 
                                    verify=self.verify, proxies=self.rc.get_proxies())

        return response.json()

    def download_from_cloud(self, threat_id):
        """ Get download a threat file from cloud
        """
        url = u"{0}/threats/{1}/download-from-cloud".format(self.base_url, threat_id)

        response = self.rc.execute("GET", url, headers=self.headers,
                                    verify=self.verify, proxies=self.rc.get_proxies())
        
        response_json = response.json()
        
        data = response_json.get("data")
        download_url = data.get("downloadUrl")
        threat_filename = data.get("fileName")

        response = self.rc.execute("GET", download_url, timeout=self.download_timeout, headers=self.headers, 
                                    verify=self.verify, proxies=self.rc.get_proxies(),
                                    callback=_download_callback)

        datastream = BytesIO(response.content)

        return {"threat_filename": threat_filename,
                "datastream": datastream,
                "download_url": download_url 
            }

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

        return response.json()

    def abort_scan(self, agents_id):
        """ Abort disk scan of the agent
        """
        url = u"{0}/agents/actions/abort-scan".format(self.base_url)

        payload = {
            "filter": {
                "ids": agents_id
            },
            "data": {}
        }

        response = self.rc.execute("POST", url, headers=self.headers, json=payload, 
                                    verify=self.verify, proxies=self.rc.get_proxies())

        return response.json()

    def initiate_scan(self, agents_id):
        """ Initiate Full Disk Scan of the agent
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

        return response.json()

    def restart_agent(self, agents_id):
        """ Restart an agent
        """
        url = u"{0}/agents/actions/restart-machine".format(self.base_url)

        payload = {
            "filter": {
                "ids": agents_id
            },
            "data": {}
        }

        response = self.rc.execute("POST", url, headers=self.headers, json=payload, 
                                    verify=self.verify, proxies=self.rc.get_proxies())

        return response.json()

    def shutdown_agent(self, agents_id):
        """ Initiate shutdown of the agent
        """
        url = u"{0}/agents/actions/shutdown".format(self.base_url)

        payload = {
            "filter": {
                "ids": agents_id
            },
            "data": {}
        }

        response = self.rc.execute("POST", url, headers=self.headers, json=payload, 
                                    verify=self.verify, proxies=self.rc.get_proxies())

        return response.json()

    def update_threat_analyst_verdict(self, threat_id, analyst_verdict):
        """ Update analystVerdict of a threat
        """
        url = u"{0}/threats/analyst-verdict".format(self.base_url)

        payload = {
            "filter": {
                "ids": threat_id
            },
            "data": {
                "analystVerdict": analyst_verdict
            }
        }

        response = self.rc.execute("POST", url, headers=self.headers, json=payload, 
                                    verify=self.verify, proxies=self.rc.get_proxies())

        return response.json()

    def update_threat_status(self, threat_id, threat_status):
        """ Update the incidentStatus of a threat
        """
        url = u"{0}/threats/incident".format(self.base_url)

        payload = {
            "filter": {
                "ids": threat_id
            },
            "data": {
                "incidentStatus": threat_status
            }
        }

        response = self.rc.execute("POST", url, headers=self.headers, json=payload, 
                                    verify=self.verify, proxies=self.rc.get_proxies())
        return response.json()

    def get_hash_reputation(self, s1_hash):
        """ Get the SentinelOne reputation value for a hash
        """
        url = u"{0}/hashes/{1}/reputation".format(self.base_url, s1_hash)

        params = {
        }

        response = self.rc.execute("GET", url, headers=self.headers, params=params, 
                                    verify=self.verify, proxies=self.rc.get_proxies())

        return response.json()

    def _make_createdate_filter(self, last_poller_datetime):
        """Convert epoch to iso format "Z" time.
        """
        last_poller_datetime_iso = last_poller_datetime.isoformat()

        # remove milliseconds
        return "{lookback_date}Z".format(lookback_date=last_poller_datetime_iso[:last_poller_datetime_iso.rfind('.')])

def _download_callback(self, response):
    """
    callback to review status code, 200 - Success
    :param response:
    :return: response
    """
    if response.status_code in [200]:
        return response.json()
    
    raise IntegrationError(response.content)
