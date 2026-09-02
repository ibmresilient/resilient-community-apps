# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
# Generated with resilient-sdk v50.1.262
import os
import logging
from urllib.parse import urljoin

from requests.exceptions import JSONDecodeError
from resilient_lib import readable_datetime, eval_mapping, IntegrationError

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
#   _api_call

LOG = logging.getLogger(__name__)

PACKAGE_NAME = "fn_rapid7_insight_idr"

ENDPOINT_URL = "https://{region}.api.insight.rapid7.com"
LINKBACK_URL = "https://{region}.idr.insight.rapid7.com/op/{org_token}/investigations/{entity_id}"

# E N D P O I N T S
GET_ALERTS_URI = "/idr/{api_version}/investigations{rrn}/alerts?index={index}"
GET_ALERT_EVIDENCE_URI = "/idr/at/alerts/{alert_rrn}/evidences"
GET_ALERT_EVIDENCE_RESTRICTED_URI = "/idr/{api_version}/restricted/investigations/{rrn}/evidence"
GET_ATTACHMENT_URI = "/idr/{api_version}/attachments/{rrn}"
GET_ATTACHMENTS_LIST_URI = "/idr/{api_version}/attachments?index={index}"
GET_COMMENTS_URI = "/idr/{api_version}/comments?index={index}"
# The default total number of investigations returned is 20.  
# Set the maximum possible number returned to 100 using the size parameter.
GET_INVESTIGATIONS_URI = "/idr/{api_version}/investigations?index={index}&size=100"
GET_INVESTIGATION_URI = "/idr/{api_version}/investigations{rrn}"
POST_COMMENT_URI = "/idr/{api_version}/comments"
PUT_PRIORITY_URI = "/idr/{api_version}/investigations/{rrn}/priority/{priority}"
PUT_STATUS_URI = "/idr/{api_version}/investigations/{rrn}/status/{status}"
PUT_DISPOSITION_URI = "/idr/{api_version}/investigations/{rrn}/disposition/{disposition}"

# Some REST API calls need to be v1 and some need to be v2 at the time of app release
# as Rapid7 doe not all have v2 versions implemented. For those that are v1, 
# use this constant for now (not the value in the app.config).
API_VERSION = "v1"
IBM_SOAR = "IBM SOAR" # common label
SOAR_HEADER = "Created by {}".format(IBM_SOAR)
ENTITY_COMMENT_HEADER = "Created by Rapid7 InsightIDR"

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
        self.api_key = app_configs.get("api_key")
        self.api_version = app_configs.get("api_version")
        self.region = app_configs.get("region")
        self.endpoint_url = ENDPOINT_URL.format(region=self.region)
        self.org_token = app_configs.get("org_token", None)

        self.polling_filters = eval_mapping(app_configs.get('polling_filters', ''), wrapper='[{}]')
        self.rc = rc

    def _make_headers(self, token: str) -> dict:
        """Build API header using authorization token

        :param token: authorization token
        :type token: str
        :return: complete header
        :rtype: dict
        """
        return {"X-Api-Key": token,
                "Accept-Version": "strong-force-preview",
                "Content-type": 'application/json'}

    def make_linkback_url(self, entity_id: str) -> str:
        """
        Create a url to link back to the endpoint entity
        :param entity_id: id representing the entity
        :type entity_id: str
        :return: completed url for linkback
        :rtype: str
        """
        return LINKBACK_URL.format(region=self.region, org_token=self.org_token, entity_id=entity_id)

    def _api_call_paginated(self, uri_format, api_version, rrn=None, params=None):
        """ Make a REST API call to GET JSON data from the Rapid7 InsightIDR endpoint
        Args:
            uri_format (str): endpoint URI string to be formatted to call the endpoint
            api_version (str): REST API version (v1 or v2) 
            rrn (str): Rapid7 InsightIDR resource 
        Returns:
            list of dict: list of JSON object in Rapid7 InsightIDR "data" field
                     str: error message if the REST API call fails
        """
        # Initialize variables to collect multiple pages of investigations
        # index is the current page which starts at 0
        index = 0
        current_page = 0
        total_pages = 1
        page_size = 0
        data_list = []
        err_msg = None

        while not err_msg and current_page < total_pages:
            # Some paginated endpoints use rrn in the URL and some use API version v1 or v2.
            # index in the URL need updating each time through the loop, so formulate each time.
            if rrn:
                url = urljoin(self.endpoint_url, uri_format.format(api_version=api_version, rrn=rrn, index=index))
            else:
                # comments endpoint has no rrn and uses api version v1 (for now?)
                url = urljoin(self.endpoint_url, uri_format.format(api_version=api_version, index=index))

            response, err_msg = self.rc.execute("GET",
                               url,
                               params=params,
                               headers=self._make_headers(self.api_key),
                               callback=callback)
            if response.ok:
                response_json = response.json()
                data_list.extend(response_json.get("data", []))
                metadata = response_json.get("metadata", None)
                if metadata:
                    if metadata.get("index", 0) == 0:
                        # Get total_pages first time through the while loop
                        total_pages = metadata.get("total_pages", 1)
                        page_size = metadata.get("size")
                    # index is the current page so increment to get the next page
                    index = index + page_size
                    current_page = current_page + 1
                else:
                    LOG.error("Rapid7 InsightIDR API call failed - no metadata found: %s", url)
                    return None, err_msg
            if err_msg:
                LOG.error("Rapid7 InsightIDR API call failed: URL: %s  ERROR: %s", url, err_msg)
                return None, err_msg

        return data_list, None

    def query_entities_since_ts(self, timestamp, *args, **kwargs):
        """
        Get changed entities since last poller run

        :param timestamp: datetime when the last poller ran
        :type timestamp: datetime
        :param *args: additional positional parameters needed for endpoint queries
        :param **kwargs: additional key/value pairs needed for endpoint queries
        :return: changed entity list
        Returns:
            list of dict: list of JSON object in Rapid7 InsightIDR "data" field
                     str: error message if the REST API call fails
        """

        # Fill in filtering params
        params = {}
        params["start_time"] = readable_datetime(timestamp)
        if self.polling_filters:
            # Add any polling filters to the query
            for k,v in self.polling_filters:
                if isinstance(k, str) and isinstance(v, str) and k in ("statuses", "sources", "priorities", "tags"):
                    params[k] = v.upper()
                else:
                    LOG.error("Polling filter: (%s,%s) is not in correct tuple format (str, str)", k,v)

        return self._api_call_paginated(GET_INVESTIGATIONS_URI, api_version=self.api_version, params=params)
    
    def get_alerts(self, rapid7_insight_idr_rrn: str):
        """ Get the alert of a Rapid7 InsightIDR investigation

        Args:
            rapid7_insight_idr_rrn (str): investigation id (Rapid7 resource identifier)
        """
        return self._api_call_paginated(GET_ALERTS_URI, api_version=self.api_version, rrn=rapid7_insight_idr_rrn, params=None)

    def get_investigation(self, rapid7_insight_idr_rrn: str):
        """ Get the JSON format information on a Rapid7 InisghtIDR investigation

        Args:
            rapid7_insight_idr_rrn (str): investigation id (Rapid7 resource identifier)
        """
        url = urljoin(self.endpoint_url, GET_INVESTIGATION_URI.format(api_version=self.api_version, rrn=rapid7_insight_idr_rrn))

        LOG.debug("Querying endpoint with %s", url)

        response, err_msg = self.rc.execute("GET",
                                            url,
                                            headers=self._make_headers(self.api_key),
                                            callback=callback)

        if err_msg:
            LOG.error("%s API call failed: %s", self.package_name, err_msg)
            return None, err_msg

        response_json = response.json()
        return response_json, None 

    def get_alert_evidence(self, rapid7_insight_idr_rrn: str, rapid7_insight_idr_alert_rrn):

        if rapid7_insight_idr_alert_rrn:
            url = urljoin(self.endpoint_url, GET_ALERT_EVIDENCE_URI.format(alert_rrn=rapid7_insight_idr_alert_rrn))
        else:
            url = urljoin(self.endpoint_url, GET_ALERT_EVIDENCE_RESTRICTED_URI.format(api_version=API_VERSION, 
                                                                                      rrn=rapid7_insight_idr_rrn))

        LOG.debug("Querying endpoint with %s", url)

        response, err_msg = self.rc.execute("GET",
                                            url,
                                            headers=self._make_headers(self.api_key),
                                            callback=callback)

        if err_msg:
            LOG.error("%s API call failed: %s", self.package_name, err_msg)
            return None, err_msg

        response_json = response.json()
        return response_json, None 

    def get_comments(self, rapid7_insight_idr_rrn: str):
        """ Get the comments from a Rapid7 InsightsIDR investigation
            NOTE: This function is using a v1 REST API call as it is not implemented in v2 yet???

        Args:
            rapid7_insight_idr_rrn (str): investigation id (Rapid7 resource identifier)

        Returns:
            list of dict: list of JSON comment object in Rapid7 InsightIDR "data" field
                     str: error message if the REST API call fails
        """
        params = {
                "target": rapid7_insight_idr_rrn
                }
        return self._api_call_paginated(GET_COMMENTS_URI, api_version=API_VERSION, rrn=rapid7_insight_idr_rrn, params=params)
    
    def format_rapid7_insight_idr_comment(self, comment: dict) -> str:
        """ Format the Rapid7 InsightIDR comment into a string
            (Usually to be added as a note in SOAR, so HTML tags are ok to use for formatting)
            Comments from Rapid7 can include attachments.  Add the attachment file_name in the comment.
            Should we do the actual fetching of the attachment here?  For now that is a separate 
            playbook to get all of the attachments of an investigation as we don't include attachments in 
            notes.
        Args:
            comment (dict): Rapid7 InsightIDR investigation comment

        Returns:
            str: formatted string of the Rapid7 InsightIDR investigation comment 
        """
        body = comment.get("body","")
        attachments = comment.get("attachments")

        # Build the comment string with comment creator in Rapid7
        created_at = comment.get('created_time',"")
        creator = comment.get("creator", None)
        creator_type = None
        name = None
        if creator:
            creator_type = creator.get("type")
            name = creator.get("name")
        comment_text = f"<br><b>Created at:</b> {created_at}<br><b>By:</b> {creator_type}: {name}<br><br>"

        # Add the comment body
        comment_text = f"{comment_text}<b>Comment:</b><br>{body}"

        # Add the list of attachment file names to the comment string
        if attachments:
            comment_text = f"{comment_text}<br><b>Attachments:</b>"
            for attachment in attachments:
                file_name = attachment.get("file_name", "")
                comment_text = f"{comment_text}<br>{file_name}"

        comment_text = f"<b>{ENTITY_COMMENT_HEADER}:</b><br>{comment_text}"
        return comment_text

    def list_attachments(self, rapid7_insight_idr_rrn: str):
        """ List the attachments of a Rapid7 InsightIDR investigation
            Need the attachment rrn to get the actual attachment

        Args:
            rapid7_insight_idr_rrn (str): attachment rrn (Rapid7 resource identifier)
        """
        params = {
                "target": rapid7_insight_idr_rrn
                }
        return self._api_call_paginated(GET_ATTACHMENTS_LIST_URI, api_version=API_VERSION, params=params)
    
    def get_attachment(self, rapid7_insight_idr_rrn: str):
        """ Get a single attachment from a Rapid7 InsightsIDR investigation
            NOTE: This function is using a v1 REST API call as it is not implemented in v2 yet???

        Args:
            rapid7_insight_idr_rrn (str): attachment rrn (Rapid7 resource identifier)

        Returns:
            dict: JSON attachment of Rapid7 InsightIDR attachment
             str: error message if the REST API call fails
        """
       
        url = urljoin(self.endpoint_url, GET_ATTACHMENT_URI.format(api_version=API_VERSION, rrn=rapid7_insight_idr_rrn))

        LOG.debug("Querying endpoint with %s", url)

        response, err_msg = self.rc.execute("GET",
                                            url,
                                            headers=self._make_headers(self.api_key),
                                            callback=callback)

        if response.ok:
            return response.content, None
        else:
            LOG.error("%s API call failed: %s", self.package_name, err_msg)
            return None, err_msg
        
    def build_attachment_name(self, rapid7_insight_idr_attachment: dict) -> str:
        """Build the attachment name from the ContentVersion information 

        Args:
            rapid7_insight_idr_attachment (dict): Rapid7 InsightIDR attachment information

        Returns:
            str: Attachment name to be used to post Rapid7 InsightIDR attachment in SOAR
        """
        attachment_name = rapid7_insight_idr_attachment.get("file_name", None)

        if not attachment_name or attachment_name == "":
            attachment_name = "Rapid7-InsightIDR-attachment"

        return attachment_name

    def post_comment(self, rapid7_insight_idr_rrn: str, comment_text: str, comment_header: str):
        """ Post a comment to a Rapid7 InsightIDR investigation

        Args:
            rapid7_insight_idr_rrn (str): Rapid7 InsightIDR investigation resource name (RRN)
            comment_text (str): comment body text
            comment_header (str): comment header text to be pre-pended to comment body text.
                                  The header usually identifies the originating platform of the comment.
        """
        url = urljoin(self.endpoint_url, POST_COMMENT_URI.format(api_version=API_VERSION, rrn=rapid7_insight_idr_rrn))

        if comment_header:
            comment_text = "{}:  {}".format(comment_header, comment_text)
        data = {"attachments": [],
                "body": comment_text,
                "target": rapid7_insight_idr_rrn}

        LOG.debug("Querying endpoint with %s", url)
        response, err_msg = self.rc.execute("POST",
                                            url,
                                            json=data,
                                            headers=self._make_headers(self.api_key),
                                            callback=callback)

        if err_msg:
            LOG.error("%s API call failed: %s", self.package_name, err_msg)
            return None, err_msg

        response_json = response.json()
        return response_json, err_msg

    def set_priority(self, 
                     rapid7_insight_idr_rrn: str, 
                     priority: str):
        """ Set the priority field of a Rapid7 InsightIDR investigation in Rapid7 InsightIDR.

        Args:
            rapid7_insight_idr_rrn (str): Rapid7 InsightIDR investigation resource name (RRN)
            priority (str): Rapid7 InsigntIDR investigation priority:  
                Enum: "UNSPECIFIED" "LOW" "MEDIUM" "HIGH" "CRITICAL" 
        Returns:
            dict, str: JSON object of the investigation object after the status is updated, 
                       error message if the REST API call fails
        """
        # Rapid7 expects these strings to be upper case
        priority = priority.upper()

        url = urljoin(self.endpoint_url, PUT_PRIORITY_URI.format(api_version=self.api_version, rrn=rapid7_insight_idr_rrn, priority=priority))

        LOG.debug("Querying endpoint with %s", url)
        response, err_msg = self.rc.execute("PUT",
                                            url,
                                            headers=self._make_headers(self.api_key),
                                            callback=callback)

        if err_msg:
            LOG.error("%s API call failed: %s", self.package_name, err_msg)
            return None, err_msg

        response_json = response.json()
        return response_json, None 

    def set_disposition(self, 
                   rapid7_insight_idr_rrn: str, 
                   disposition : str):
        """ Set the disposition of a Rapid7 InsightIDR investigation

        Args:
            rapid7_insight_idr_rrn (str): Rapid7 InsightIDR investigation resource name (RRN)
            disposition (str): A disposition to set the investigation to. Only used if the new status is CLOSED.
                                          Enum: "BENIGN" "MALICIOUS" "NOT_APPLICABLE" 
        Returns:
            dict, str: JSON object of the investigation object after the status is updated, 
                       error message if the REST API call fails
        """
        # Rapid7 expects these strings to be upper case
        disposition = disposition.upper().replace(" ", "_")

        url = urljoin(self.endpoint_url, PUT_DISPOSITION_URI.format(api_version=self.api_version, 
                                                                    rrn=rapid7_insight_idr_rrn, 
                                                                    disposition=disposition))

        LOG.debug("Querying endpoint with %s", url)
        response, err_msg = self.rc.execute("PUT",
                                            url,
                                            headers=self._make_headers(self.api_key),
                                            callback=callback)

        if err_msg:
            LOG.error("%s API call failed: %s", self.package_name, err_msg)
            return None, err_msg

        response_json = response.json()
        return response_json, None 
    
    def set_status(self, 
                   rapid7_insight_idr_rrn: str, 
                   status: str):
        """ Set the status of a Rapid7 InsightIDR investigation
        Args:
            rapid7_insight_idr_rrn (str): Rapid7 InsightIDR investigation resource name (RRN)
            status (str): Rapid7 InsightIDR investigation status:  
                          Enum: "OPEN" "CLOSED" "INVESTIGATING" "WAITING" 

        Returns:
            dict, str: JSON object of the investigation object after the status is updated, 
                       error message if the REST API call fails
        """
        # Rapid7 expects these strings to be upper case
        status = status.upper()

        url = urljoin(self.endpoint_url, PUT_STATUS_URI.format(api_version=self.api_version, rrn=rapid7_insight_idr_rrn, status=status))

        LOG.debug("Querying endpoint with %s", url)
        response, err_msg = self.rc.execute("PUT",
                                            url,
                                            headers=self._make_headers(self.api_key),
                                            callback=callback)

        if err_msg:
            LOG.error("%s API call failed: %s", self.package_name, err_msg)
            return None, err_msg

        response_json = response.json()
        return response_json, None 
    
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
            response_json = response.json()
            msg = response_json.get("message", None)
            details = response_json.get("correlation_id", None)
        except JSONDecodeError as err:
            msg = str(err)
            details = response.text

        error_msg  = u"Error: \n    status code: {0}\n    message: {1}\n    reason: {2}".format(
                response.status_code,
                msg,
                details)

    return response, error_msg
