# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
# Generated with resilient-sdk v51.0.2.2.1096
import base64
import logging
from datetime import datetime
from urllib.parse import urljoin
from requests.exceptions import JSONDecodeError
from resilient_lib import readable_datetime, str_to_bool, RequestsCommonWithoutSession

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

PACKAGE_NAME = "fn_sumo_logic"

LINKBACK_URL = "{console_url}/sec/insight/{entity_id}"

# E N D P O I N T S
# define the endpiont api calls your app will make to the endpoint solution. Below are examples
ENTITIES_URI          = "{api_endpoint_url}/sec/v1/entities"
INSIGHTS_ALL_URI      = "{api_endpoint_url}/sec/v1/insights/all"
INSIGHTS_URI          = "{api_endpoint_url}/sec/v1/insights"
INSIGHTS_BY_ID_URI    = "{api_endpoint_url}/sec/v1/insights/{id}"
INSIGHTS_COMMENTS_URI = "{api_endpoint_url}/sec/v1/insights/{id}/comments"
INSIGHTS_SEVERITY_URI = "{api_endpoint_url}/sec/v1/insights/{id}/severity"
INSIGHTS_STATUS_URI   = "{api_endpoint_url}/sec/v1/insights/{id}/status"
INSIGHTS_TAGS_URI     = "{api_endpoint_url}/sec/v1/insights/{id}/tags"
SIGNALS_BY_ID_URI     = "{api_endpoint_url}/sec/v1/signals/{id}"

# Sumo Logic max query limit
MAX_QUERY_LIMIT = 50

IBM_SOAR = "IBM SOAR" # common label
SOAR_HEADER = f"Created by {IBM_SOAR}"
ENTITY_COMMENT_HEADER = "Created by Sumo Logic"

class AppCommon():
    def __init__(self, package_name, app_configs):
        """
        Initialize the parameters needed to communicate to the endpoint solution

        :param rc: object to resilient_lib.requests_common for making API calls
        :type rc: ``resilient_lib.RequestsCommon``
        :param package_name: name of the package to be created
        :type package_name: str
        :param app_configs: app.config parameters in order to authenticate and access the endpoint
        :type app_configs: dict
        """

        self.package_name = package_name
        self.access_id = app_configs.get("access_id")
        self.access_key = app_configs.get("access_key")
        self.api_endpoint_url = app_configs.get("api_endpoint_url")
        self.console_url = app_configs.get("console_url")
        self.rc = RequestsCommonWithoutSession(function_opts=app_configs)
        polling_filters = app_configs.get("polling_filters", None)
        self.polling_filters =  'status:in("inprogress","new","closed")' if not polling_filters or polling_filters == "" else polling_filters
        self.headers = self._make_headers()

    def _make_headers(self) -> dict:
        """Build API header using authorization token

        :param self : access_id and access_key contained in self
        :type self: object
        :return: complete header
        :rtype: dict
        """
        access_token  = f"{self.access_id}:{self.access_key}"

        string_encoded_url_key = base64.b64encode(str.encode(access_token))
        auth_token = string_encoded_url_key.decode("utf-8")

        # Create the headers
        headers = {"Authorization": f"Basic {auth_token}",
                   "Content-Type": "application/json"}
        return headers

    def _api_call(self, method: str, url: str, payload=None):
        """
        Make an API call to the endpoint solution and get back the response

        :param method: REST method to execute (GET, POST, PUT, ...)
        :type method: str
        :param url: URL to send request to
        :type url: str
        :param payload: JSON payload to send if a POST, defaults to None
        :type payload: dict|None
        :return: requests.Response object returned from the endpoint call
        :rtype: ``requests.Response``
        """

        kwargs = {  
            "headers": self.headers,  
            "callback": callback  
        }  

        if method in ["PUT", "POST"] and payload:  
            kwargs["json"] = payload
        elif payload:
            kwargs["params"] = payload

        response, error_msg = self.rc.execute(method, url, **kwargs)  

        if error_msg:
            LOG.error("%s API call failed: %s", self.package_name, error_msg)
            return response, error_msg

        return response, error_msg

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
        url = INSIGHTS_URI.format(api_endpoint_url=self.api_endpoint_url)

        # Create readable timestamps to use for querying detections.
        last_poll_time = readable_datetime(timestamp)

        offset = total = 0
        objects = []
        has_next_page = True

        # Get Insights that are created between the last poll time and now.
        # Only get those that are In Progress and New.
        q = f'created:>={last_poll_time} {self.polling_filters}'
        query = {
            "q": q,
            "offset": offset,
            "limit": MAX_QUERY_LIMIT
        }

        while has_next_page and offset <= total:
            LOG.debug("Querying endpoint url %s with %s", url, query)
            response, err_msg = self._api_call("GET", url=url, payload=query)

            if err_msg:
                LOG.error("%s API call failed: %s", self.package_name, err_msg)
                return [], err_msg
            response_json = response.json() if response else {}
            # Implement pagination here - data = {'hasNextPage': False, 'total': 0, 'objects': []}
            data = response_json.get("data", None)
            has_next_page = data.get("hasNextPage", False)
            total = total + data.get("total")
            offset = offset + len(data.get("objects", []))
            objects.extend(data.get("objects", []))
            # Update offset for next query call
            query["offset"] = offset

        # Reverse the order so that oldest insights are created first as a case
        objects.reverse()
        return objects, err_msg

    def get_entity(self, entity_type: str, entity_value: str):
        """ Get an Sumo Logic signal by ID

        Args:
            signal_id (str): sumo logic signal ID

        Return:
            dict, str tuple: JSON response from sumo logic, error message
        """
        url = ENTITIES_URI.format(api_endpoint_url=self.api_endpoint_url)

        query = {
            "q": f'type:in("{entity_type}") value:in("{entity_value}")'
        }

        LOG.debug("Querying endpoint url %s with %s", url, query)
        response, error_msg = self._api_call("GET", url=url, payload=query)

        if error_msg:
            LOG.error("%s API call failed: %s", self.package_name, error_msg)
            return {}, error_msg
        response_json = response.json()
        return response_json, error_msg
    
    def query_insights_list(self, insight_id_list: list):
        """ Get a list of Sumo Logic insights

        Args:
            insight_id (list): list of sumo logic insight IDs

        Return:
            list, str tuple: list of insight dict, error message
        """
        url = INSIGHTS_URI.format(api_endpoint_url=self.api_endpoint_url)
        insight_list_string =  ",".join([f'"{insight_id}"' for insight_id in insight_id_list])
        q = f'id:in({insight_list_string})'

        query = {
            "q": q,
            "limit": len(insight_id_list)
        }
        LOG.debug("Querying endpoint url %s with %s", url, query)
        response, error_msg = self._api_call("GET", url=url, payload=query)

        if error_msg:
            LOG.error("%s API call failed: %s", self.package_name, error_msg)
            return [], error_msg
        response_json = response.json()
        data = response_json.get("data", None)
        objects = data.get("objects", [])
        return objects, error_msg

    def get_insight_by_id(self, insight_id: str):
        """ Get an Sumo Logic insight by ID

        Args:
            insight_id (str): sumo logic insight ID

        Return:
            dict, str tuple: JSON response from sumo logic, error message
        """
        url = INSIGHTS_BY_ID_URI.format(api_endpoint_url=self.api_endpoint_url, id=insight_id)

        response, error_msg = self._api_call("GET", url)
        response_json = response.json()
        return response_json, error_msg

    def get_comments_from_insight(self, insight_id: str):
        """ Get an Insight's comments

        Args:
            insight_id (str): sumo logic insight ID

        Return:
            dict, str tuple: JSON response from sumo logic, error message
        """
        url = INSIGHTS_COMMENTS_URI.format(api_endpoint_url=self.api_endpoint_url, id=insight_id)

        response, error_msg = self._api_call("GET", url)
        response_json = response.json()
        data = response_json.get("data", None)
        comments = data.get("comments", []) if data else []
        return comments, error_msg

    def format_insight_note(self, comment: dict) -> str:
        """ Format the comment text into a note

        Args:
            comment (dict): sumo logic comment dict

        Returns:
            str: formatted comment
        """
        body = comment.get("body","")

        # Build the note string with comment information
        created_at = comment.get("timestamp","")
        author = comment.get("author", None)
        username = author.get("username", "") if author else ""

        comment_text = f"<br><b>Comment added by<br>{username}</b><br>{created_at}<br><br>{body}"

        # Prepend entity header
        comment_text = f"<b>{ENTITY_COMMENT_HEADER}:</b><br>{comment_text}"
        return comment_text

    def post_comment(self, insight_id: str, comment_body: str, comment_header: str):
        """ Add a comment to a sumo logic Insight

        Args:
            insight_id (str): sumo logic insight ID
            comment_body (str): comment body to add to the insight

        Return:
            dict, str tuple: JSON response from sumo logic, error message
        """
        url = INSIGHTS_COMMENTS_URI.format(api_endpoint_url=self.api_endpoint_url, id=insight_id)

        comment = f"{comment_header}:  {comment_body}" if comment_header else comment_body

        payload = {"body": comment}
        response, error_msg = self._api_call("POST", url, payload=payload)
        response_json = response.json()
        return response_json, error_msg

    def post_tag_name(self, insight_id: str, tag_name: str):
        """ Add a tag to an Insight

        Args:
            insight_id (str): sumo logic insight ID
            tag_name (str): tag name to add to the insight

        Return:
            dict, str tuple: JSON response from sumo logic, error message      
        """
        url = INSIGHTS_TAGS_URI.format(api_endpoint_url=self.api_endpoint_url, id=insight_id)
        payload = {"tagName": tag_name}
        response, error_msg = self._api_call("POST", url=url, payload=payload)
        response_json = response.json()
        return response_json, error_msg

    def update_insight_severity(self, insight_id: str, severity: str):
        """ Update the severity of an insight in sumo logic

        Args:
            insight_id (str): sumo logic insight ID
            severity (str): severity level to set the insight
                            severity values in sumo logic: "CRITICAL", "HIGH", "MEDIUM", "LOW"

        Return:
            dict, str tuple: JSON response from sumo logic, error message   
        """
        url = INSIGHTS_SEVERITY_URI.format(api_endpoint_url=self.api_endpoint_url, id=insight_id)
        payload = {"severity": severity}
        response, error_msg = self._api_call("PUT", url=url, payload=payload)
        response_json = response.json()
        return response_json, error_msg

    def update_insights_status(self, insight_id: str, status: str, resolution: str=None):
        """ Update the status of an insight in sumo logic

        Args:
            insight_id (str): sumo logic insight ID
            status (str): The status to update this Insight to. Default values are
                          "new", "inprogress", and "closed", but custom statuses can also be
                          created in the UI.
            resolution (str): The resolution reason for closing this Insight.

        Return:
            dict, str tuple: JSON response from sumo logic, error message
        """
        url = INSIGHTS_STATUS_URI.format(api_endpoint_url=self.api_endpoint_url, id=insight_id)
        payload = {"status": status}
        if resolution:
            payload["resolution"] = resolution

        response, error_msg = self._api_call("PUT", url=url, payload=payload)
        response_json = response.json()
        return response_json, error_msg


    def get_signal_by_id(self, signal_id: str):
        """ Get an Sumo Logic signal by ID

        Args:
            signal_id (str): sumo logic signal ID

        Return:
            dict, str tuple: JSON response from sumo logic, error message
        """
        url = SIGNALS_BY_ID_URI.format(api_endpoint_url=self.api_endpoint_url, id=signal_id)

        response, error_msg = self._api_call("GET", url)
        response_json = response.json()
        return response_json, error_msg
    
    def make_linkback_url(self, entity_id: str):
        """
        Create a url to link back to the endpoint entity

        :param entity_id: id representing the entity
        :type entity_id: str
        :return: completed url for linkback
        :rtype: str
        """
        return LINKBACK_URL.format(console_url=self.console_url, entity_id=entity_id)


def callback(response):
    """
    Callback needed for certain REST API calls to return a formatted error message

    :param response: the requests response object
    :type response: ``requests.Response``
    :return: response, error_msg
    :rtype: tuple(``requests.Response``, str)
    """
    error_msg = None
    if response.status_code >= 300 and response.status_code <= 500:
        try:
            resp = response.json()
            errors = resp.get('errors', [])
            msg = ""
            details = ""
            if errors:
                msg = errors[0].get("message", "")
                code = errors[0].get("code", "")
                error_id = errors[0].get("error_id", "")
                details = f"error code: {code}  error_id: {error_id}"
        except JSONDecodeError as err:
            msg = str(err)
            details = response.text

        error_msg  = f"Error: \n    status code: {response.status_code}\n    message: {msg}\n    details: {details}"

    return response, error_msg

