# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# Generated with resilient-sdk v49.0.4423
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
import datetime
import logging
from urllib.parse import urljoin
from base64 import b64encode
from urllib.parse import quote_plus, urljoin
import json

from requests.exceptions import JSONDecodeError
from resilient_lib import IntegrationError, readable_datetime, eval_mapping, str_to_bool

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

PACKAGE_NAME = "fn_salesforce"

# change the header as necessary
HEADER = { 'Content-Type': 'application/json' }

# E N D P O I N T S
TOKEN_URL = "https://{my_domain_url}/services/oauth2/token"
BASE_URL = "https://{my_domain_url}"
QUERY_URI = "/services/data/{api_version}/query/"
CASE_URI = "/services/data/{api_version}/sobjects/Case/{case_id}"
CASE_COMMENTS_URI = "/services/data/{api_version}/sobjects/Case/{case_id}/CaseComments"
ACCOUNT_URI = "/services/data/{api_version}/sobjects/Account/{account_id}"
OWNER_URI = "/services/data/{api_version}/sobjects/Owner/{owner_id}"
USER_URI = "/services/data/{api_version}/sobjects/User/{user_id}"
CONTACT_URI = "/services/data/{api_version}/sobjects/Contact/{contact_id}"

# C O N S T A N T S
SOQL_QUERY_LAST_MODIFIED_DATE = "SELECT FIELDS(ALL) FROM Case WHERE LastModifiedDate > {time}"
SOQL_QUERY_CASE_ID = "SELECT FIELDS(ALL) FROM Case WHERE Id = '{case_id}'"
LINKBACK_URL = "https://{my_domain_name}.lightning.force.com/lightning/r/Case/{entity_id}/view"
LIMIT = 200

IBM_SOAR = "IBM SOAR" # common label
SOAR_HEADER = "Created by {}".format(IBM_SOAR)
ENTITY_COMMENT_HEADER = "Created by Salesforce"

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

        self.package_name = package_name
        self.my_domain_name = app_configs.get("my_domain_name")
        self.my_domain_url = app_configs.get("my_domain_url")
        self.api_version = app_configs.get("api_version")
        self.client_id = app_configs.get("consumer_key")
        self.client_secret = app_configs.get("consumer_secret")
        self.base_url = BASE_URL.format(my_domain_url=self.my_domain_url, api_version=self.api_version)
        self.token_url = TOKEN_URL.format(my_domain_url=self.my_domain_url)
        self.rc = rc
        self.verify = _get_verify_ssl(app_configs)
        self.access_token = self.get_token()
        self.polling_filters = eval_mapping(app_configs.get('polling_filters', ''), wrapper='[{}]')
        if not self.polling_filters:
            self.polling_filters = []

        # Setup access token in the header for making Salesforce REST API calls 
        if self.access_token:
            self.headers = self._make_headers(self.access_token)
        else:
            raise IntegrationError("Unable to get access token from Salesforce!")

    def get_token(self) -> str:
        """
        Get an API access token for Salesforce authentication.

        :return: API Access token (string)
        """
        uri = self.token_url

        auth_str = f"{self.client_id}:{self.client_secret}"
        auth_bytes = b64encode(auth_str.encode("utf-8"))
        encoded_auth = str(auth_bytes, "utf-8")

        headers = {
            "Authorization": "Basic {}".format(encoded_auth),
            "Content-Type": "application/x-www-form-urlencoded",
        }

        response = self.rc.execute("POST", uri, headers=headers, data="grant_type=client_credentials")

        response_json = response.json()

        return response_json.get("access_token", None)
    
    def _get_uri(self, cmd: str) -> str:
        """
        Build API url
        :param cmd: portion of API: 
        :type cmd: str
        :return: complete URL
        :rtype: str
        """
        return urljoin(self.base_url, cmd)
    
    def _add_query_filters(self, base_query: str, filters: list, limit: int) -> str:
        """ Create an SOQL query string which is sent to Salesforce /query endpoint to 
        perform a search on Case objects

        Args:
            base_query (str): Base query string (In our case is a SELECT statement that 
                            the poller uses to get most recent Cases from Salesforce 
                            since the last poll time)
            filters (list): List of tuples (Salesforce Case field, operator, value) that are 
                            converted to AND statements in the WHERE clause to filter cases 
                            when querying Salesforce for cases.
            limit (int): Salesforce has a 2000 limit on the number of query results returned.

        Returns:
            str: The SOQL SELECT command used to query Cases in Salesforce
        """
        soql_query = base_query

        # Loop through the filters defined by the user to limit the cases returned from the query
        # Append them to the base query for polling cases based on the last poll time.
        for filter_tuple in filters:
            if not isinstance(filter_tuple, tuple) or len(filter_tuple) != 3:
                LOG.error("polling filter tuple %s : invalid format or does not contain 3 elements - skipping this filter", filter_tuple)
                continue
            if isinstance(filter_tuple[2], list):
                # list of values - loop and add them in between enclosed parentheses.
                polling_filter_query = " AND {0} {1} (".format(filter_tuple[0], filter_tuple[1])
                for filter_value in filter_tuple[2]:
                    polling_filter_query = polling_filter_query + filter_value + ","
                # Replace last comma with close parentheses
                if polling_filter_query[-1:] == ",":
                    polling_filter_query = polling_filter_query[:-1] + ")"
            else:
                polling_filter_query = " AND {0} {1} {2}".format(filter_tuple[0], filter_tuple[1], filter_tuple[2])
            soql_query = soql_query + polling_filter_query

        if limit:
            soql_query = soql_query + " LIMIT {0}".format(limit)
        return soql_query
 
    def _make_headers(self, token: str) -> dict :
        """Build API header using authorization token

        :param token: authorization token
        :type token: str
        :return: complete header
        :rtype: dict
        """
        header = HEADER.copy()
        # modify to represent how to build the header
        header['Authorization'] = f"Bearer {token}"
        header['Content-Type'] = 'application/json'

        return header  

    def query_entities_since_ts(self, timestamp: datetime, *args, **kwargs) -> list:
        """
        Get changed entities since last poller run

        :param timestamp: datetime when the last poller ran
        :type timestamp: datetime
        :param *args: additional positional parameters needed for endpoint queries
        :param **kwargs: additional key/value pairs needed for endpoint queries
        :return: changed entity list
        :rtype: list
        """
        # Get the first batch of query results based

        readable_time = readable_datetime(timestamp)

        # Form the query endpoint
        query_url = self.base_url + QUERY_URI.format(api_version=self.api_version)

        # Build the SOQL query based on the polling time and the user input polling_filters
        soql_query_with_filters = self._add_query_filters(SOQL_QUERY_LAST_MODIFIED_DATE.format(time=readable_time), self.polling_filters, LIMIT)
        params = {'q': soql_query_with_filters}
        LOG.debug("Querying endpoint with URL %s", soql_query_with_filters)

        response = self.rc.execute("GET", url=query_url, headers=self.headers, params=params)
        response_json = response.json()
        records = response_json.get("records", [])
        query_results = []
        query_results.extend(records)
            
        done = response_json.get("done", True)
        while not done:
            if response_json.get("nextRecordsUrl", None) == None:
                IntegrationError("No nextRecordsUrl key returned from Salesforce REST API case query!")

            # Get URL for next batch of results using the link sent back from Salesforce 
            next_query_url = self._get_uri(response_json.get("nextRecordsUrl"))
            LOG.debug("Querying next records endpoint with URL %s", next_query_url)

            # Get the next batch of cases 
            response = self.rc.execute("GET", url=next_query_url, headers=self.headers)
            response_json = response.json()
            records = response_json.get("records", [])

            query_results.extend(records)

            # Check if we are done
            done = response_json.get("done", True)
        return query_results

    def make_linkback_url(self, entity_id: str) -> str:
        """
        Create a url to link back to the endpoint entity
        :param entity_id: id representing the entity
        :type entity_id: str
        :return: completed url for linkback
        :rtype: str
        """
        return LINKBACK_URL.format(my_domain_name=self.my_domain_name, entity_id=entity_id)

    def get_case(self, case_id: str) -> dict:
        """Get the Salesforce case data for the specified Salesforce case_id

        Args:
            case_id (str): Salesforce case Id

        Returns:
            dict: json case data from Salesforce
        """
        url = self.base_url + CASE_URI.format(api_version=self.api_version, case_id=case_id)
        LOG.debug("Querying endpoint with URL %s", url)

        response = self.rc.execute("GET", url=url, headers=self.headers)
        return response.json()
    
    def get_case_comments(self, case_id: str) -> list:
        """Get the comments associated with the specified Salesforce case

        Args:
            case_id (str): Salesforce case Id (from Salesforce)

        Returns:
            dict: comments from Salesforce
        """
        url = self.base_url + CASE_COMMENTS_URI.format(api_version=self.api_version, case_id=case_id)
        LOG.debug("Querying /CaseComments endpoint with URL %s", url)

        response = self.rc.execute("GET", url=url, headers=self.headers)

        response_json = response.json()

        records = response_json.get("records", [])
        comments = []
        comments.extend(records)
            
        done = response_json.get("done", True)
        while not done:
            if response_json.get("nextRecordsUrl", None) == None:
                IntegrationError("No nextRecordsUrl key returned from Salesforce REST API /CaseComments")

            # Get URL for next batch of results using the link sent back from Salesforce 
            next_records_url = self._get_uri(response_json.get("nextRecordsUrl"))
            LOG.debug("Querying next records /CaseComments endpoint with URL %s", next_records_url)

            # Get the next batch of cases 
            response = self.rc.execute("GET", url=next_records_url, headers=self.headers)
            response_json = response.json()
            records = response_json.get("records", [])

            comments.extend(records)

            # Check if we are done
            done = response_json.get("done", True)
        return comments


    def format_salesforce_comment(self, comment: dict) -> str:
        """Format a Salesforce comment 

        Args:
            comment (_type_): Salesforce comment (json object)

        Returns:
            str : formatted string
        """
        comment_body = comment.get('CommentBody',"")
        if comment_body:
            created_at = comment.get('CreatedDate',"")
            created_by_id = comment.get('CreatedById',"")
            if created_by_id:
                user = self.get_user(created_by_id)
                created_by = user.get('Name', created_by_id)
            else:
                created_by = "Not available"

            text = f"{comment_body}<br><br>Created at: {created_at}<br>By: {created_by}"
            return text
        else:
            return None
        
    def get_account(self, account_id: str) -> dict:
        """Get the Salesforce account data for the specified Salesforce AccountId

        Args:
            account_id (str): Salesforce AccountId

        Returns:
            dict: json account data from Salesforce
        """
        url = self.base_url + ACCOUNT_URI.format(api_version=self.api_version, account_id=account_id)
        LOG.debug("Querying /Account endpoint with URL %s", url)

        response = self.rc.execute("GET", url=url, headers=self.headers)
        return response.json()
    
    def get_contact(self, contact_id: str) -> dict:
        """Get the Salesforce case data for the specified Salesforce case_id

        Args:
            case_id (str): Salesforce case Id

        Returns:
            dict: json case data from Salesforce
        """
        url = self.base_url + CONTACT_URI.format(api_version=self.api_version, contact_id=contact_id)
        LOG.debug("Querying /Contact endpoint with %s", url)

        response = self.rc.execute("GET", url=url, headers=self.headers)
        return response.json()
    
    def get_user(self, user_id: str) -> dict:
        """Get the Salesforce case data for the specified Salesforce case_id

        Args:
            case_id (str): Salesforce case Id

        Returns:
            dict: json case data from Salesforce
        """
        url = self.base_url + USER_URI.format(api_version=self.api_version, user_id=user_id)
        LOG.debug("Querying /User endpoint with %s", url)

        response = self.rc.execute("GET", url=url, headers=self.headers)
        return response.json()

    def add_comment_to_case(self, case_id: str, comment: str) -> dict:
        """Post a comment to the Salesforce case

        Args:
            case_id (str): Salesforce case Id

        Returns:
            dict: json case data from Salesforce
        """
        url = self.base_url + CASE_URI.format(api_version=self.api_version, case_id=case_id)
        LOG.debug("Querying /User endpoint with %s", url)

        data = {"Comments": comment}
        data_string = json.dumps(data)
        response = self.rc.execute("PATCH", url=url, headers=self.headers, data=data_string)
        return True
    
    def update_case_status(self, salesforce_case_id, status):
        """Update the Status field in the Salesforce case

        Args:
            salesforce_case_id (str): Salesforce CaseId
            status (str): Salesforce Case Status
        """
        url = self.base_url + CASE_URI.format(api_version=self.api_version, case_id=salesforce_case_id)
        data = {"Status": status}
        data_string = json.dumps(data)

        response = self.rc.execute("PATCH", url=url, headers=self.headers, data=data_string)
        return True

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

def _get_verify_ssl(app_configs: dict) -> bool:
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