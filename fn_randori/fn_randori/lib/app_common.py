# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

import json
from datetime import datetime, timedelta
from base64 import b64encode
import logging
from urllib.parse import urljoin

from resilient_lib import str_to_bool, eval_mapping, RequestsCommon
from resilient_lib.components.templates_common import iso8601


#----------------------------------------------------------------------------------------
# This module is an open template for you to develop the methods necessary to interact
# with your endpoint solution. The only required method is:
#  query_entities_since_ts: get your entities (alerts, events, etc.) based on a timestamp
#       since the last time the poller ran
# Helper functions:
#  authenticate: authenticate to your endpoint solution, yielding a token for ongoing API calls
#  _make_header: create the necessary API header for your endpoint communication
#  make_linkback_url: create a url for your alert, event, etc. to navigate back to your endpoint console
#  _get_uri: assemble the parts of your URL (base address, version information, command and arguments)
#  _api_call: perform the API call, passing parameters and check the returned status code before
#      returning the response object

LOG = logging.getLogger(__name__)

PACKAGE_NAME = "fn_randori"

# Randori REST API header
HEADER = { 'Content-Type': 'application/json' }

# URL prefix to refer back to your console for a specific alert, event, etc.
LINKBACK_URL = "{organization_name}/targets/{target_id}"

# E N D P O I N T S
GET_COMMENT_URI = "/recon/api/{api_version}/entity/{target_id}/comment"
GET_ALL_DETECTIONS_FOR_TARGET_URI = "/recon/api/{api_version}/all-detections-for-target"
GET_PATHS_URI = "/recon/api/{api_version}/paths"
GET_SINGLE_TARGET_URI = "/recon/api/{api_version}/target/{target_id}"
GET_SINGLE_DETECTION_FOR_TARGET_URI = "/recon/api/{api_version}/single-detection-for-target"
GET_VALIDATE_URI = "/auth/api/{api_version}/validate"
PATCH_TARGET_URI = "/recon/api/{api_version}/target"
POST_COMMENT_URI = "/recon/api/{api_version}/entity/{target_id}/comment"
POST_LOGIN_API_KEY_URI = "/auth/api/{api_version}/login-api-key"

TARGET_LIMIT = 2000
COMMENT_LIMIT = 100

IBM_SOAR = "IBM SOAR" # common label
SOAR_HEADER = f"Created by {IBM_SOAR}"
ENTITY_COMMENT_HEADER = "Created by Randori"

# The Randori authorization token is viable for 24 hours, but regenerate after 
# 12 hours so there is no issue with it not being viable.
AUTH_TOKEN_EXPIRY_TIME_IN_HOURS = 12

class AppCommon():
    def __init__(self, rc: RequestsCommon, package_name: str, app_configs: dict) -> None:
        """
        Initialize the parameters needed to communicate to the endpoint solution

        :param rc: object to resilient_lib.requests_common for making API calls
        :type rc: ``resilient_lib.RequestsCommon``
        :param package_name: name of the package to be created
        :type package_name: str
        :param app_configs: app.config parameters in order to authenticate and access the endpoint
        :type app_configs: dict
        """
        self.rc = rc
        self.package_name = package_name

        # required configs
        self.api_token = app_configs.get("api_token", None)
        self.api_key = app_configs.get("api_key", None)
        self.endpoint_url = app_configs.get("endpoint_url")
        self.api_version = app_configs.get("api_version")
        self.organization_name = app_configs.get("organization_name")
        self.verify = _get_verify_ssl(app_configs)
        self.polling_filters = eval_mapping(app_configs.get('polling_filters', ''), wrapper='[{}]')
        self.auth_token_expiry_time = datetime.now()
        self.auth_token = None

        self.header = self._make_header(generate_auth_token=False)

    def _get_uri(self, cmd: str) -> str:
        """
        Build API url

        :param cmd: portion of API: alerts, endpoints, policies
        :type cmd: str
        :return: complete URL
        :rtype: str
        """
        return urljoin(self.endpoint_url, cmd.format(api_version=self.api_version))

    def _make_header(self, generate_auth_token:bool) -> dict:
        """Build API header using API token or API key
           NOTE: Generated auth token is only passed in the header when calling GET method to Randori API
        :param generate_auth_token: whether to generate an auth token (only True with calls using GET method)
        :type generate_auth_token: bool
        :return: complete header
        :rtype: dict
        """
        header = HEADER.copy()
        if self.api_key:
            if generate_auth_token:
                token = self._generate_auth_token(self.api_key)
            else:
                token = self.api_key
        elif self.api_token:
            token = self.api_token
        else:
            raise ValueError("No API token or API key provided")

        # modify to represent how to build the header
        header['Authorization'] = f"Bearer {token}"

        return header

    def _generate_auth_token(self, api_key: str) -> str:
        """ Generate authorization token from Randori API key
            Generated auth token is only passed in the header when calling GET method to Randori API
        Args:
            api_key (str): Randori API key

        Returns:
            str: Randori JWT authorization token
        """
        now = datetime.now()

        # If current token expiry time is less than 24 hours,
        # then use the current authorization token.
        if self.auth_token and now < self.auth_token_expiry_time:
            return self.auth_token

        self.auth_token_expiry_time = now + timedelta(hours=AUTH_TOKEN_EXPIRY_TIME_IN_HOURS)

        url = self._get_uri(POST_LOGIN_API_KEY_URI)
        data = {"api_key": f"{api_key}"}

        response = self.rc.execute("POST",
                                   url=url,
                                   json=data,
                                   headers=self.header,
                                   verify=self.verify)
        response_json = response.json()

        self.auth_token = response_json.get("authorization")
        return self.auth_token

    def query_entities_since_ts(self, timestamp: datetime, *_args, **_kwargs) -> list:
        """
        Get changed entities since last poller run

        :param timestamp: datetime when the last poller ran
        :type timestamp: datetime
        :param *args: additional positional parameters needed for endpoint queries
        :param **kwargs: additional key/value pairs needed for endpoint queries
        :return: changed entity list
        :rtype: list of targets
        """
        iso_timestamp = iso8601(timestamp)

        # Base query used by the poller to get new and updated targets based on last poll time.
        query =  {
            'condition': "AND",
            'rules': [
                {
                    'condition': "OR",
                    'rules': [
                        {
                            'field': "table.target_first_seen",
                            'operator': "greater_or_equal",
                            'value': iso_timestamp
                        },
                        {
                            'field': "table.temptation_last_modified",
                            'operator': "greater_or_equal",
                            'value': iso_timestamp
                        }
                    ]
                }
            ]
        }

        # Add optional query filters if defined.
        if self.polling_filters:
            query = self._build_query_filters(query, self.polling_filters)

        targets = self.get_detections_for_target(query)
        return targets
        
    def get_detections_for_target(self, query: dict) -> list:
        """get_detections_for_target

        Args:
            query (json object): Randori query string for searching for targets.

        Returns:
            list : List of targets matching the query parameters
        """
        # Endpoint expects query to be base64 encoded.
        query_string = json.dumps(query)
        b64_query = b64encode(query_string.encode())

        params = {
            'q': b64_query, 
            'limit': TARGET_LIMIT
        }

        LOG.debug("Querying endpoint with %s", query)

        # Make at least one call to the get-all-detections-for-target endpoint to 
        # get the complete list of targets to be updated or created.  Keep looping
        # till we get the complete list.
        total_targets = -1
        offset = 0
        targets = []
        while offset > total_targets:
            params['offset'] = offset
            response = self.rc.execute("GET",
                                   url=self._get_uri(GET_ALL_DETECTIONS_FOR_TARGET_URI),
                                   params=params,
                                   headers=self._make_header(generate_auth_token=True),
                                   verify=self.verify)
            response_json = response.json()
            if response_json.get('count')  <= 0:
                break
            data = response_json.get('data')

            # Append targets found to the list of targets to be returned from this function.
            for target in data:
                targets.append(target)
            offset = offset + response_json.get('count')
            total_targets = response_json.get('total')
        return targets

    def _build_query_filters(self, query: dict, filters: list) -> dict:
        """Build query filter json object from the list of filter tuples.

        Args:
            query (json object): json containing base query
            filters (list of tuples) : List of tuples.  Each tuple specifies a filter containing
                Randori "field", "operator" and "value"

        Returns:
            json object: newly formulated query with the specified filters added
        """

        for filter_tuple in filters:
            if not isinstance(filter_tuple, tuple) or len(filter_tuple) != 3:
                LOG.error("polling_filters tuple %s : invalid format or does not contain 3 elements - skipping this filter", filter_tuple)
                continue
            if isinstance(filter_tuple[2], list) :
                # If "value" is a list of values then create a rule (json object) for each 
                # value and use "OR" condition.
                condition = {'condition': "OR",
                                 'rules': []}
                for value in filter_tuple[2]:
                    rule = {}
                    # Prepend fieldname with "table." string
                    rule['field'] = f"table.{filter_tuple[0]}"
                    rule['operator'] = filter_tuple[1]
                    rule['value'] = value
                    condition['rules'].append(rule)
                query['rules'].append(condition)
            else:
                # Create a single rule for this tuple
                rule = {}
                field_name = f"table.{filter_tuple[0]}"
                rule['field'] = field_name
                rule['operator'] = filter_tuple[1]
                rule['value'] = filter_tuple[2]
                query['rules'].append(rule)
        return query

    def make_linkback_url(self, entity_id: str, linkback_url : str = LINKBACK_URL) -> str:
        """
        Create a url to link back to the endpoint entity

        :param entity_id: id representing the entity
        :type entity_id: str
        :param linkback_url: _description_, defaults to LINKBACK_URL
        :type linkback_url: str|int, optional
        :return: completed url for linkback
        :rtype: str
        """
        return urljoin(self.endpoint_url, linkback_url.format(organization_name=self.organization_name, 
                                                              target_id=entity_id))

    def get_randori_base_url(self) -> str:
        """
        Create a base URL string for Randori

        :rtype: str
        """
        return urljoin(self.endpoint_url, self.organization_name)


    def get_target_comments(self, target_id: str) -> list:
        """
        Call Randori endpoint to get commments for the specified target.
        """

        url = self._get_uri(GET_COMMENT_URI.format(api_version=self.api_version, target_id=target_id))
        params = {'limit': COMMENT_LIMIT}
        response = self.rc.execute("GET",
                                   url=url,
                                   params=params,
                                   headers=self._make_header(generate_auth_token=True),
                                   verify=self.verify)
        response_json = response.json()

        comment_list = response_json.get('comments', [])

        return comment_list

    def post_target_comment(self, target_id: str, comment_text: str, comment_header: str) -> dict:
        """ Post a comment to the specified target.

        Args:
            target_id (str): Randori target id
            comment_text (str): Comment text
            comment_header (str): Comment header

        Returns:
            dict: Results of posting the comment to Randori target
        """

        url = self._get_uri(POST_COMMENT_URI.format(api_version=self.api_version, target_id=target_id))
        if comment_header:
            comment_text = f"{comment_header}:  {comment_text}"
        data = {'comment': comment_text}

        response = self.rc.execute("POST",
                                   url=url,
                                   json=data,
                                   headers=self._make_header(generate_auth_token=True),
                                   verify=self.verify)
        response_json = response.json()

        return response_json

    def get_target(self, target_id: str) -> dict:
        """ Get the specified target from Randori

        Args:
            target_id (str): Randori target id

        Returns:
            dict: Information on the target from Randori
        """
        url = GET_SINGLE_TARGET_URI.format(api_version=self.api_version, target_id=target_id)
        response = self.rc.execute("GET",
                                   self._get_uri(url),
                                   headers=self._make_header(generate_auth_token=True),
                                   verify=self.verify)
        return response.json()

    def get_detections_for_single_target(self, target_id: str) -> list:
        """
        Get changed entities

        :return: changed entity list
        :rtype: list of targets
        """

        # Base query used by the poller to get new and updated targets based on last poll time.
        query =  {
            'condition': "OR",
            'rules': [
                {
                'field': "table.target_id",
                'operator': "equal",
                'value': target_id
                }
              ]
         }

        detections = self.get_detections_for_target(query)

        return detections

    def update_target_impact_score(self, target_id: str, impact_score: str) -> dict:
        """ Update the Randori target impact_score field in Randori

        Args:
            target_id (string_): Randori target id
            impact_score (string): String indicating the impact_score of the target in Randori.
        """
        data = {
            "data": {"impact_score": impact_score},
            "q": {
                  "condition": "OR",
                  "rules": [
                            {
                              "id": "table.id",
                              "field": "table.id",
                              "type": "object",
                              "input": "text",
                              "operator": "equal",
                              "value": target_id
                            }
                  ]
                }
            }
        data_string = json.dumps(data)

        response = self.rc.execute("PATCH",
                                   self._get_uri(PATCH_TARGET_URI),
                                   data=data_string,
                                   headers=self._make_header(generate_auth_token=True),
                                   verify=self.verify)
        return response.json()

    def update_target_status(self, target_id: str, status: str) -> dict:
        """ Update the Randori target status field in Randori

        Args:
            target_id (string_): Randori target id
            status (string): String indicating the status of the target in Randori.
        """
        status_data = {
            "data": {"status": status},
            "q": {
                  "condition": "OR",
                  "rules": [
                            {
                              "id": "table.id",
                              "field": "table.id",
                              "type": "object",
                              "input": "text",
                              "operator": "equal",
                              "value": target_id
                            }
                  ]
                }
            }
        status_string = json.dumps(status_data)

        response = self.rc.execute("PATCH",
                                   self._get_uri(PATCH_TARGET_URI),
                                   data=status_string,
                                   headers=self._make_header(generate_auth_token=True),
                                   verify=self.verify)
        return response.json()

    def get_validate(self) -> dict:
        """
        Call Randori endpoint to validate the connection to Randori from SOAR.
        """
        response = self.rc.execute("GET",
                                   self._get_uri(GET_VALIDATE_URI),
                                   headers=self._make_header(generate_auth_token=True),
                                   verify=self.verify)
        return response.json()

    def format_randori_comment(self, comment: dict) -> str:
        """ Format a comment from Randori to be displayed in IBM SOAR.

        Args:
            comment (str): Randori comment (json object)

        Returns:
            str: Randori comment formatted for IBM SOAR
        """
        comment_text = comment.get('comment',"")
        if comment_text:
            created_at = comment.get('created_at',"")
            name = comment.get('name',"")
            text = f"{comment_text}<br><br>Created at: {created_at}<br>By: {name}"
            return text

        return None

    def get_paths(self, target_id: str) -> dict:
        """
        Call Randori endpoint to get the paths data for target from Randori.
        """
        params = {
            'terminal': target_id
        }

        url = self._get_uri(GET_PATHS_URI.format(api_version=self.api_version))
        response = self.rc.execute("GET",
                                   url=url,
                                   params=params,
                                   headers=self._make_header(generate_auth_token=True),
                                   verify=self.verify)
        return response.json()

def _get_verify_ssl(app_configs: dict):
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
