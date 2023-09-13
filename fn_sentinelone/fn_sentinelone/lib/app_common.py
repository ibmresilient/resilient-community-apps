# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
# Generated with resilient-sdk v50.0.151

import logging
from urllib.parse import urljoin

from requests.exceptions import JSONDecodeError
from resilient_lib import IntegrationError, readable_datetime, str_to_bool, validate_fields

#----------------------------------------------------------------------------------------
# This module is an open template for you to develop the methods necessary to interact
# with your endpoint solution. The only required method is:
#  query_entities_since_ts: get your entities (alerts, events, etc.) based on a timestamp
#       since the last time the poller ran
# Helper functions:
#  _make_headers: create the necessary API header for your endpoint communication
#  make_linkback_url: create a url for your alert, event, etc. to navigate back to your endpoint console
#  _get_uri: assemble the parts of your URL (base address, version information, command and arguments)
#  _api_call: perform the API call, passing parameters and check the returned status code before
#      returning the response object
#
# Review these functions which need modification. Currently they `raise IntegrationError("UNIMPLEMENTED")`
#   _make_headers,
#   query_entities_since_ts,
#   make_linkback_url,
#   _get_uri
#   _api_call

LOG = logging.getLogger(__name__)

PACKAGE_NAME = "fn_sentinelone"

# change the header as necessary
HEADER = { 'Content-Type': 'application/json' }

# URL prefix to refer back to your console for a specific alert, event, etc.
LINKBACK_URL = "https://{server}/incidents/threats/{threat_id}/overview"

IBM_SOAR = "IBM SOAR" # common label
SOAR_HEADER = "Created by {}".format(IBM_SOAR)
ENTITY_COMMENT_HEADER = "Created by SentinelOne"

DEFAULT_LIMIT = 25
DEFAULT_SORT_BY = "createdDate"
DEFAULT_SORT_ORDER = "desc"

# E N D P O I N T S
# define the endpiont api calls your app will make to the endpoint solution. Below are examples
#ALERT_URI = "alert/{}/"
#POLICY_URI = "policy/"

class AppCommon():
    def __init__(self, rc, package_name, app_configs):
        """
        Initialize the parameters needed to communicate to the endpoint solution

        :param rc: object to resilient_lib.requests_common for making API calls
        :type rc: ``resilient_lib.RequestsCommon``
        :param package_name: name of the package to be created
        :type package_name: str
        :param app_configs: app.config parameters in order to authenticate and access the endpoint
        :type app_configs: dict
        """

        # Read the configuration options
        required_fields = ["sentinelone_server", "api_token", "api_version"]
        validate_fields(required_fields, app_configs)
        self.rc = rc
        self.api_version = app_configs.get("api_version")
        self.server = app_configs.get("sentinelone_server")
        self.base_url = u"https://{0}/web/api/v{1}".format(self.server, self.api_version)
        self.api_token = app_configs.get("api_token")

        site_ids = app_configs.get("site_ids")
        self.site_ids = site_ids if site_ids else []
        account_ids = app_configs.get("account_ids")
        self.account_ids = account_ids if account_ids else []
        self.limit = app_configs.get("limit", DEFAULT_LIMIT)
        self.sort_by = app_configs.get("sort_by", DEFAULT_SORT_BY)
        self.sort_order = app_configs.get("sort_order", DEFAULT_SORT_ORDER)
        self.query_param = app_configs.get("query_param", None)
        self.incident_statuses = app_configs.get("incident_statuses", "in_progress,unresolved")
        self.send_soar_link_to_sentinelone = str_to_bool(app_configs.get("send_soar_link_to_sentinelone", "true"))
        self.headers = self._make_headers(self.api_token)

        self.verify = _get_verify_ssl(app_configs)

        # Specify any additional parameters needed to communicate with your endpoint solution

    def _get_uri(self, cmd):
        """
        Build API url
        <- ::CHANGE_ME:: change this to reflect the correct way to build an API call ->

        :param cmd: portion of API: alerts, endpoints, policies
        :type cmd: str
        :return: complete URL
        :rtype: str
        """
        raise IntegrationError("UNIMPLEMENTED")
        return urljoin(self.endpoint_url, cmd)

    def _make_headers(self, token):
        """Build API header using authorization token

        :param token: authorization token
        :type token: str
        :return: complete header
        :rtype: dict
        """
        headers = {
            'Authorization': u'ApiToken {0}'.format(token),
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        return headers
    
    def make_linkback_url(self, entity_id: str) -> str:
        """
        Create a url to link back to the endpoint entity

        :param entity_id: id representing the entity
        :type entity_id: str
        :param linkback_url: _description_, defaults to LINKBACK_URL
        :type linkback_url: str|int, optional
        :return: completed url for linkback
        :rtype: str
        """
        return LINKBACK_URL.format(server=self.server, threat_id=entity_id)

    def query_entities_since_ts(self, timestamp, *args, **kwargs):
        """
        Get changed entities since last poller run

        :param timestamp: datetime when the last poller ran
        :type timestamp: datetime
        :param *args: additional positional parameters needed for endpoint queries
        :param **kwargs: additional key/value pairs needed for endpoint queries
        :return: changed entity list
        :rtype: list
        """
        # Build filter information
        #last_poller_datetime_string = self._make_createdate_filter(timestamp)
        readable_time = readable_datetime(timestamp)
        LOG.debug("last_poller_time: %s", readable_time)

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
            'updatedAt__gte': readable_time
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
            'createdAt__gte': readable_time
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
        response_json = response.json()

        # create linkback url
        response_json["entity_url"] = self.make_linkback_url(threat_id)
        return response_json

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

    def format_threat_note(self, comment: dict) -> str:
        """Format a Salesforce comment 
        Args:
            comment (_type_): Salesforce comment (json object)
        Returns:
            str : formatted string
        """
        comment_body = comment.get('text', None)
        if comment_body:
            created_at = comment.get('createdAt',"NA")
            creator = comment.get("creator", None)
            created_by_id = comment.get('creatorId', None)
            if creator:
                created_by = creator
            elif created_by_id:
                created_by = created_by_id
            else:
                created_by = "Not available"

            text = f"{comment_body}<br><br>Created at: {created_at}<br>By: {created_by}"

            # Add entity comment header
            note = "<b>{}:</b><br>{}".format(ENTITY_COMMENT_HEADER, text)
            return note
        return None
 
    def add_threat_note(self, threat_id: str, note_text: str, comment_header: str) -> dict:
        """ Add threat note to a threat
        """
        url = u"{0}/threats/notes".format(self.base_url, threat_id)

        if comment_header:
            note_text = "{}:\n  {}".format(comment_header, note_text)

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

def _download_callback(self, response):
    """
    callback to review status code, 200 - Success
    :param response:
    :return: response
    """
    if response.status_code in [200]:
        return response.json()
    
    raise IntegrationError(response.content)


def callback(response):
    """
    Callback needed for certain REST API calls to return a formatted error message

    :param response: the requests response object
    :type response: ``requests.Response``
    :return: response, error_msg
    :rtype: tuple(``requests.Reponse``, str)
    """
    error_msg = None
    if response.status_code >= 300 and response.status_code <= 500:
        try:
            resp = response.json()
            msg = resp.get('messages') or resp.get('message')
            details = resp.get('details')
        except JSONDecodeError as err:
            msg = str(err)
            details = response.text

        error_msg  = u"Error: \n    status code: {0}\n    message: {1}\n    details: {2}".format(
            response.status_code,
            msg,
            details)

    return response, error_msg

def _get_verify_ssl(app_configs):
    """
    Get ``verify`` parameter from app config.
    Value can be set in the [fn_my_app] section

    :param opts: All of the app.config file as a dict
    :type opts: dict
    :param app_options: App specific configs
    :type app_options: dict
    :return: Value to set ``requests.request.verify`` to. Either a path or a boolean. Defaults to ``True``
    :rtype: bool|str(path)
    """
    # start checking the app specific settings
    verify = app_configs.get("verify")

    # because verify can be either a boolean or a path,
    # we need to check if it is a string with a boolean 
    # value first then, and only then, we convert it to a bool
    # NOTE: that this will then only support "true" or "false"
    # (case-insensitive) rather than the normal "true", "yes", etc...
    if isinstance(verify, str) and verify.lower() in ["false", "true"]:
        verify = str_to_bool(verify)

    return verify