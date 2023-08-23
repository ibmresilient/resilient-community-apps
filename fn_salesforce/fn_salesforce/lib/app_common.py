# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# Generated with resilient-sdk v49.0.4423
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
import datetime
import logging
from urllib.parse import urljoin
from base64 import b64encode
import json

from requests.exceptions import JSONDecodeError
from resilient_lib import IntegrationError, readable_datetime, eval_mapping, clean_html, RequestsCommonWithoutSession

#----------------------------------------------------------------------------------------
# This module is an open template for you to develop the methods necessary to interact
# with your endpoint solution. The only required method is:
#  query_entities_since_ts: get your entities (alerts, events, etc.) based on a timestamp
#       since the last time the poller ran
# Helper functions:
#  _make_headers: create the necessary API header for your endpoint communication
#  make_linkback_url: create a url for your alert, event, etc. to navigate back to your 
#                     endpoint console
#  _get_uri: assemble the parts of your URL (base address, version information, command
#            and arguments)
#  _api_call: perform the API call, passing parameters and check the returned status 
#             code before returning the response object

LOG = logging.getLogger(__name__)

PACKAGE_NAME = "fn_salesforce"

# change the header as necessary
HEADER = { 'Content-Type': 'application/json' }

# E N D P O I N T S
TOKEN_URL = "https://{my_domain_url}/services/oauth2/token"
BASE_URL = "https://{my_domain_url}"
QUERY_URI = "/services/data/{api_version}/query/"
ATTACHMENT_URI = "/services/data/{api_version}/sobjects/Attachment"
CONTENT_DOCUMENT_LINK = "/services/data/{api_version}/sobjects/ContentDocumentLink"
CONTENT_VERSION_GET = "/services/data/{api_version}/sobjects/ContentVersion/{content_version_id}"
CONTENT_VERSION_POST = "/services/data/{api_version}/sobjects/ContentVersion"
CASE_URI = "/services/data/{api_version}/sobjects/Case/{case_id}"
CASE_POST_URI = "/services/data/{api_version}/sobjects/Case"
CASE_COMMENTS_URI = "/services/data/{api_version}/sobjects/Case/{case_id}/CaseComments"
ACCOUNT_URI = "/services/data/{api_version}/sobjects/Account/{account_id}"
USER_URI = "/services/data/{api_version}/sobjects/User/{user_id}"
CONTACT_URI = "/services/data/{api_version}/sobjects/Contact/{contact_id}"
TASK_POST_URI = "/services/data/{api_version}/sobjects/Task"

# C O N S T A N T S
SOQL_QUERY_LAST_MODIFIED_DATE = "SELECT FIELDS(ALL) FROM Case WHERE LastModifiedDate > {time}"
SOQL_QUERY_BY_RECORD_TYPE_ID = " AND RecordTypeId IN ({record_type_id_list})"
SOQL_QUERY_RECORD_TYPE = "SELECT Id,Name from RecordType WHERE sObjectType=\'Case\'"
SOQL_QUERY_CASE_TASK = "SELECT FIELDS(ALL) FROM Task WHERE WhatId='{case_id}' LIMIT 200"
SOQL_QUERY_CONTENT_DOCUMENT = "SELECT id, ContentDocumentId, ContentDocument.LatestPublishedVersionId from ContentDocumentLink where LinkedEntityId='{case_id}'"
LINKBACK_URL = "https://{my_domain_name}.lightning.force.com/lightning/r/{entity_type}/{entity_id}/view"
LIMIT = 200

IBM_SOAR = "IBM SOAR" # common label
SOAR_HEADER = "Created by {}".format(IBM_SOAR)
ENTITY_COMMENT_HEADER = "Created by Salesforce"

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
        self.my_domain_name = app_configs.get("my_domain_name")
        self.my_domain_url = app_configs.get("my_domain_url")
        self.api_version = app_configs.get("api_version")
        self.client_id = app_configs.get("consumer_key")
        self.client_secret = app_configs.get("consumer_secret")
        self.base_url = BASE_URL.format(my_domain_url=self.my_domain_url, api_version=self.api_version)
        self.token_url = TOKEN_URL.format(my_domain_url=self.my_domain_url)
        self.rc = RequestsCommonWithoutSession(function_opts=app_configs)
        self.access_token = self.get_token()
        self.polling_filters = eval_mapping(app_configs.get('polling_filters', ''), wrapper='[{}]')
        if not self.polling_filters:
            self.polling_filters = []
        self.polling_record_type_names = eval_mapping(app_configs.get('polling_record_type_names', ''), wrapper='[{}]')
        if not self.polling_record_type_names:
            self.polling_record_type_names = []
        self.record_type_id_list = ""
        self.soql_limit = app_configs.get("soql_limit", LIMIT)

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
            "Authorization": "Basic {0}".format(encoded_auth),
            "Content-Type": "application/x-www-form-urlencoded",
        }

        response = self.rc.execute("POST", uri, headers=headers, 
                                   data="grant_type=client_credentials")

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
    
    def _add_query_filters(self, base_query: str, record_type_id_list, filters: list, limit: int) -> str:
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

        # Add record type ID filter list if any are defined
        if record_type_id_list:
            soql_query = soql_query + SOQL_QUERY_BY_RECORD_TYPE_ID.format(record_type_id_list=record_type_id_list)

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
 
    def _make_headers(self, token: str) -> dict:
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
        soql_query = self._add_query_filters(SOQL_QUERY_LAST_MODIFIED_DATE.format(time=readable_time), 
                                             self.record_type_id_list,
                                             self.polling_filters, self.soql_limit)
        params = {'q': soql_query}
        LOG.debug("Querying endpoint with URL %s", soql_query)

        response = self.rc.execute("GET", url=query_url, headers=self.headers, params=params)
        response_json = response.json()

        query_results = self.paginate_results(response_json)

        return query_results

    def make_linkback_url(self, entity_type: str, entity_id: str) -> str:
        """
        Create a url to link back to the endpoint entity
        :param entity_id: id representing the entity
        :type entity_id: str
        :return: completed url for linkback
        :rtype: str
        """
        return LINKBACK_URL.format(my_domain_name=self.my_domain_name, entity_type=entity_type, entity_id=entity_id)

    def get_case(self, case_id: str) -> dict:
        """Get the Salesforce case data for the specified Salesforce case_id

        Args:
            case_id (str): Salesforce case Id

        Returns:
            dict: json case data from Salesforce
        """
        url = self.base_url + CASE_URI.format(api_version=self.api_version, case_id=case_id)
        LOG.debug("Querying /Case endpoint with URL %s", url)

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

        comments = self.paginate_results(response_json)
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

            # Add entity comment header
            note = "<b>{}:</b><br>{}".format(ENTITY_COMMENT_HEADER, text)
            return note
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

    def add_comment_to_case(self, case_id: str, comment: str, comment_header: str) -> bool:
        """Post a comment to the Salesforce case

        Args:
            case_id (str): Salesforce case Id

        Returns:
            dict: json case data from Salesforce
        """
        url = self.base_url + CASE_URI.format(api_version=self.api_version, case_id=case_id)
        LOG.debug("PATCHing /Case endpoint with URL%s", url)

        if comment_header:
            comment = "{}:  {}".format(comment_header, comment)
        data = {"Comments": comment}
        data_string = json.dumps(data)

        response = self.rc.execute("PATCH", url=url, headers=self.headers, data=data_string)
        return True
    
    def create_salesforce_case(self, case_payload: dict) -> dict:
        """ Create a case in Salesforce with the specified case data in JSON format

        Args:
            case_payload (dict): _description_

            case_payload = {
                "Type": "System Intrusion",
                "Status": "New",
                "Origin": "Web",
                "Subject": "Break-in detected",
                "Priority": "Medium",
                "Description": "Test create case in Salesforce",
                "Comments": "Created by IBM SOAR: This case was created in SOAR"
            }

        Returns:
            dict: JSON from Salesforce is returned.
            Fields included in the JSON are: "id" (caseId), "success" (bool) and "errors" (list)
        """
        url = self.base_url + CASE_POST_URI.format(api_version=self.api_version)
        LOG.debug("POST /Case endpoint with URL%s", url)

        response = self.rc.execute("POST", url=url, headers=self.headers, json=case_payload)
        response_json = response.json()
        return response_json

    def create_task(self, task_payload: dict) -> dict:
        """ Create a task in Salesforce with the specified task data in JSON format

        Args:
            task_payload (dict): Salesforce task data in JSON format

            task_payload = {
                "WhatId": "500Hr00001Wthb4IAB", 
                "Description": "Task from IBM SOAR case", 
                "Subject": "Investigate Exposure of Personal Information/Data", 
                "Priority": "Normal", 
                "Status": "In Progress"
            }

        Returns:
            dict: JSON from Salesforce is returned.  
            Fields included in the JSON are: "id" (TaskId), "success" (bool) and "errors" (list)
        """
        url = self.base_url + TASK_POST_URI.format(api_version=self.api_version)
        LOG.debug("POST /Task endpoint with URL%s", url)

        # Remove html tags as Salesforce does not process them
        if task_payload['Description']:
            task_payload['Description'] = clean_html(task_payload['Description'])
        response = self.rc.execute("POST", url=url, headers=self.headers, json=task_payload)
        response_json = response.json()
        return response_json

    def get_case_tasks(self, case_id: str) -> list:
        """ Get the tasks associated with a case

        Args:
            case_id (str): Salesforce CaseId
        Returns:
            list : returns a list of tasks 
        """
        query_url = self.base_url + QUERY_URI.format(api_version=self.api_version)
        soql_query = SOQL_QUERY_CASE_TASK.format(case_id=case_id)    
        params = {'q': soql_query}
        LOG.debug("Querying endpoint with URL %s", query_url)

        response = self.rc.execute("GET", url=query_url, headers=self.headers, params=params)
        response_json = response.json()

        return self.paginate_results(response_json)
    
    def update_case_status(self, salesforce_case_id: str, status: str) -> bool:
        """Update the Status field in the Salesforce case

        Args:
            salesforce_case_id (str): Salesforce CaseId
            status (str): Salesforce Case Status
        """
        url = self.base_url + CASE_URI.format(api_version=self.api_version, case_id=salesforce_case_id)
        LOG.debug("PATCHing /Case endpoint with URL%s", url)

        data = {"Status": status}
        data_string = json.dumps(data)

        response = self.rc.execute("PATCH", url=url, headers=self.headers, data=data_string)
        return True

    def build_record_type_id_query_string(self) -> bool:
        """ Build a string of RecordTypeId in SOQL format.  Get the list of Record Type Names
        that is dedfined by the user in the app.config and convert the Record Type Names into
        RecordTypeIds. Each Id must be enclosed in escaped single quotes and separated by 
        a comma.

        Returns:
            bool: True if successful.
            AppCommon record_type_id_list string field is implicitly returned so that the string 
            can be stored and used for each poller call.
        """
        record_id_str = ""
        for record_type in self.polling_record_type_names:
            record_type_id = self.get_record_type_id(record_type)
            record_id_str = record_id_str + "\'" + record_type_id + "\',"
        if record_id_str[-1:] == ",":
            record_id_str = record_id_str[:-1]

        self.record_type_id_list = record_id_str
        return True

    def get_record_type_id(self, record_type_name: str) -> str:
        """Get the records types of all cases in Salesforce and look for the RecordTypeID of 
        the one that matches SOAR Case Record Type.  The poller uses the RecordTypeId to
        only search for SOAR Cases in Salesforce.

        Args: record_type_name (str) : Name of the RecordTypeId we are looking for

        Returns:
            bool: return True if the SOAR Case record type Id was found, else return False
        """
        query_url = self.base_url + QUERY_URI.format(api_version=self.api_version)

        params = {'q': SOQL_QUERY_RECORD_TYPE}
        LOG.debug("Querying endpoint with URL %s", SOQL_QUERY_RECORD_TYPE)

        response = self.rc.execute("GET", url=query_url, headers=self.headers, params=params)

        response_json = response.json()

        all_records = self.paginate_results(response_json)

        for record in all_records:
            if record.get("Name") == record_type_name:
                return record.get("Id")
        return None
    
    def get_content_version_ids(self, salesforce_case_id: str) -> list:
        """ Get the LatestPublishedVersionIds of a case.  
        (This is really the latest version of each attachment know as a 
         ContentVersion is Salesforce)

        Args:
            salesforce_case_id (str): Salesforce CaseId

        Returns:
            list of str: List of ContentVersion Ids associated with a Salesforce Case
        """
        # Define the query to get the ContentDocuments (attachments) associated with the Salesforce case
        query = SOQL_QUERY_CONTENT_DOCUMENT.format(case_id=salesforce_case_id)
        url = self.base_url + QUERY_URI.format(api_version=self.api_version)
        params = {'q': query}
        LOG.debug("GET /query endpoint with URL%s", url)

        response = self.rc.execute("GET", url=url, headers=self.headers, params=params)
        response_json = response.json()
        records = response_json.get("records")
        content_version_ids = []
        for record in records:
            # Get the LatestPublishedVersionId of the document (attachment) and return in the list
            content_doc = record.get("ContentDocument")
            content_version_id = content_doc.get("LatestPublishedVersionId")
            content_version_ids.append(content_version_id)
        return content_version_ids

    def get_content_version(self, content_version_id: str) -> dict:
        """Get the ContentVersion information of an attachment in Salesforce

        Args:
            content_version_id (str): ContentVersion Id

        Returns:
            dict : JSON format info of the ContentVersion (attachment)
        """
        url = self.base_url + CONTENT_VERSION_GET.format(api_version=self.api_version, 
                                                         content_version_id=content_version_id)
        response = self.rc.execute("GET", url=url, headers=self.headers)
        response_json = response.json()
        return response_json

    def get_content_version_data(self, content_version_data_uri: str) -> bytes:
        """Return the ContentVersion data (actual attachment data)

        Args:
            content_version_data_uri (str): URI from Salesforce used to get 
            the ContentVersion data

        Returns:
            byte stream attachment data 
        """
        content_version_data_url = self.base_url + content_version_data_uri
        content_header = {}
        content_header["Authorization"] = self.headers["Authorization"]
        content_header["Content-Type"] = "application/octet-stream"
        response_version_data = self.rc.execute("GET", url=content_version_data_url, headers=content_header)
        if response_version_data.ok:
            return(response_version_data.content)
        else:
            LOG.debug(f"Get Content Version Data couldn't download %s" % content_version_data_url)
        return None

    def build_attachment_name(self, content_version: dict) -> str:
        """Build the attachment name from the ContentVersion information 

        Args:
            content_version (dict): ContentVersion (attachment) information

        Returns:
            str: Attachment name to be used to post Salesforce attachment in SOAR
        """
        attachment_name = content_version.get("Title", None)
        extension = content_version.get("FileExtension", None)
        if not attachment_name or attachment_name == "":
            attachment_name = "salesforce-attachment"

        if extension and extension != "" and extension not in attachment_name:
            attachment_name =F"{attachment_name}.{extension}"
        return attachment_name

    def post_attachment_to_salesforce_case(self, attachment_name: str, 
                                           encoded_string: bytes,
                                           salesforce_case_id: str)-> dict:
        """ Post SOAR attachment data to a Salesforce case.

        Args:
            attachment_name (str): attachment name in SOAR
            encoded_string (bytes): attachment data
            salesforce_case_id (str): Salesforce CaseId

        Returns:
            dict : JSON returned from /ContentDocumentLink endpoint associating the case with the 
            document (attachment).
        """
        # Create a ContentVersion
        content_version_url = self.base_url + CONTENT_VERSION_POST.format(api_version=self.api_version)
        b64_encoded_string = b64encode(encoded_string).decode("utf-8")
        param = {'Title': attachment_name,
                 'PathOnClient': attachment_name,
                 'VersionData': b64_encoded_string}
        response = self.rc.execute("POST", url=content_version_url, headers=self.headers, json=param)
        response_json = response.json()

        content_version_id = response_json.get('id')

        content_version_get_url = self.base_url + CONTENT_VERSION_GET.format(api_version=self.api_version, 
                                                                             content_version_id=content_version_id)
        # Get the ContentDocument id
        response_get = self.rc.execute("GET", url=content_version_get_url, headers=self.headers)
        response_get_json = response_get.json()
        content_document_id = response_get_json.get('ContentDocumentId')


        # Create a ContentDocumentLink to link the document to the case
        data = {'ContentDocumentId': content_document_id,
                'LinkedEntityId': salesforce_case_id,
                'ShareType': 'V'}
        content_document_link_url = self.base_url + CONTENT_DOCUMENT_LINK.format(api_version=self.api_version)
        content_document_link = self.rc.execute("POST", url=content_document_link_url, headers=self.headers, json=data)
        content_document_link_json = content_document_link.json()
        return content_document_link_json
    
    def paginate_results(self, response_json: dict) -> list:
        """Use this function to return paginated results from Salesforce REST API.
        When calling some REST API endpoints, some results may be large and not 
        returned in one call.  Subsequent calls to get the results have a 
        "nextRecordsUrl" that contains a URL to get the next results.  There is also
        a "done" field returned that is set to True when there are no more results.

        Args:
            response_json (dict): The first response from REST API call 

        Returns:
            list: the whole list of results from a call to REST API
        """
        all_records = response_json.get("records", [])
            
        done = response_json.get("done", True)
        while not done:
            if response_json.get("nextRecordsUrl", None) is None:
                IntegrationError("No nextRecordsUrl key returned from Salesforce REST API case query!")

            # Get URL for next batch of results using the link sent back from Salesforce 
            next_query_url = self._get_uri(response_json.get("nextRecordsUrl"))
            LOG.debug("Querying next records endpoint with URL %s", next_query_url)

            # Get the next batch of cases 
            response = self.rc.execute("GET", url=next_query_url, headers=self.headers)
            response_json = response.json()
            records = response_json.get("records", [])

            all_records.extend(records)

            # Check if we are done
            done = response_json.get("done", True)
        return all_records
    
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
