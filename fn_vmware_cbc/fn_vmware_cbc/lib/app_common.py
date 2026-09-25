# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
# Generated with resilient-sdk v51.0.1.1.824

import logging
from time import time, sleep
from datetime import datetime
from json import loads

from requests.exceptions import JSONDecodeError
from resilient_lib import eval_mapping, readable_datetime, RequestsCommonWithoutSession

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

PACKAGE_NAME = "fn_vmware_cbc"

# E N D P O I N T S
# define the endpiont api calls your app will make to the endpoint solution. Below are examples
ALERTS_SEARCH       = "{cbc_hostname}/api/alerts/v7/orgs/{org_key}/alerts/_search"
ALERTS_URI          = "{cbc_hostname}/api/alerts/v7/orgs/{org_key}/alerts/{alert_id}"
ALERTS_HISTORY_URI  = "{cbc_hostname}/api/alerts/v7/orgs/{org_key}/alerts/{alert_id}/history"
ALERTS_NOTES_URI    = "{cbc_hostname}/api/alerts/v7/orgs/{org_key}/alerts/{alert_id}/notes"
ALERTS_WORKFLOW_URI = "{cbc_hostname}/api/alerts/v7/orgs/{org_key}/alerts/workflow"
THREATS_NOTES_URI   = "{cbc_hostname}/api/alerts/v7/orgs/{org_key}/threats/{threat_id}/notes"
TAGS_URI            = "{cbc_hostname}/api/alerts/v7/orgs/{org_key}/threats/{threat_id}/tags"
JOB_DETAILS_URI     = "{cbc_hostname}/jobs/v1/orgs/{org_key}/jobs/{job_id}"
DEVICES_URI         = "{cbc_hostname}/appservices/v6/orgs/{org_key}/devices/{device_id}"
DEVICE_ACTIONS_URI  = "{cbc_hostname}/appservices/v6/orgs/{org_key}/device_actions"
OBSERVATIONS_DETAIL_JOB_URI      = "{cbc_hostname}/api/investigate/v2/orgs/{org_key}/observations/detail_jobs"
OBSERVATIONS_RESULTS_URI         = "{cbc_hostname}/api/investigate/v2/orgs/{org_key}/observations/detail_jobs/{job_id}/results"
REPUTATION_OVERRIDES_URI         = "{cbc_hostname}/appservices/v6/orgs/{org_key}/reputations/overrides"
LIVERESPONSE_SESSIONS_POST_URI   = "{cbc_hostname}/appservices/v6/orgs/{org_key}/liveresponse/sessions"
LIVERESPONSE_SESSIONS_DELETE_URI = "{cbc_hostname}/appservices/v6/orgs/{org_key}/liveresponse/sessions/{session_id}"
LIVERESPONSE_COMMANDS_URI        = "{cbc_hostname}/appservices/v6/orgs/{org_key}/liveresponse/sessions/{session_id}/commands"
LIVERESPONSE_COMMANDS_STATUS_URI = "{cbc_hostname}/appservices/v6/orgs/{org_key}/liveresponse/sessions/{session_id}/commands/{command_id}"

QUERY_LIMIT = 9999
# CBC max timeout is 3 minutes
DEFAULT_JOB_TIMEOUT_SECONDS = 3*60
DEFAULT_JOB_SLEEP_INTERVAL_SECONDS = 1

IBM_SOAR = "IBM SOAR" # common label
SOAR_HEADER = "Created by {}".format(IBM_SOAR)
ENTITY_COMMENT_HEADER = "Created by VMware CBC"

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
        self.api_id = app_configs.get("api_id")
        self.api_secret = app_configs.get("api_secret")
        self.org_key = app_configs.get("org_key")
        self.hostname = app_configs.get("hostname")
        self.token = f"{self.api_secret}/{self.api_id}"
        self.headers = self._make_headers(self.token)

        # Get polling criteria and exclusion tuples from app.config
        self.polling_filters_criteria_1   = eval_mapping(app_configs.get('polling_filters_criteria_1', ''), wrapper='[{}]')
        self.polling_filters_exclusions_1 = eval_mapping(app_configs.get('polling_filters_exclusions_1', ''), wrapper='[{}]')
        self.polling_filters_criteria_2   = eval_mapping(app_configs.get('polling_filters_criteria_2', ''), wrapper='[{}]')
        self.polling_filters_exclusions_2 = eval_mapping(app_configs.get('polling_filters_exclusions_2', ''), wrapper='[{}]')
        self.polling_filters_criteria_3   = eval_mapping(app_configs.get('polling_filters_criteria_3', ''), wrapper='[{}]')
        self.polling_filters_exclusions_3 = eval_mapping(app_configs.get('polling_filters_exclusions_3', ''), wrapper='[{}]')

        self.job_timeout = int(app_configs.get("job_timeout", DEFAULT_JOB_TIMEOUT_SECONDS))
        self.job_sleep_interval = int(app_configs.get("job_sleep_interval", DEFAULT_JOB_SLEEP_INTERVAL_SECONDS))
        self.rc = RequestsCommonWithoutSession(function_opts=app_configs)

    def _make_headers(self, token):
        """Build API header using authorization token

        :param token: authorization token
        :type token: str
        :return: complete header
        :rtype: dict
        """
        return {
            'X-AUTH-TOKEN': f'{token}',
            'Content-Type': 'application/json'
        }

    def create_filter_dict(self, filter_list: list) -> dict:
        """ Create a dictionary from the list of polling filters

        Args:
            polling_filter (list): List of tuples to convert to a dictionary

        Returns:
            dict: dictionary of polling filters
        """
        filter_dict = {}
        for k,v in filter_list:
            if isinstance(v, (int, bool, str, list)):
                filter_dict[k] = v
            else:
                LOG.error(f"Unknown criteria filter type for key: {k}, {v}")
        return filter_dict
    
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
        # Setup query criteria and exclusions based on app.config settings
        # Allow 3 sets of search criteria/exclusions


        # Create readable timestamps to use for querying alerts.
        last_poll_time = readable_datetime(timestamp)
        now_time = readable_datetime(int(datetime.now().timestamp()*1000))

        # Create list of criteria and exclusions dictionaries (from tuples) to be added to query when polling CBC for alerts
        criteria_list = list()
        criteria_list.append(self.create_filter_dict(self.polling_filters_criteria_1) if self.polling_filters_criteria_1 else {})
        criteria_list.append(self.create_filter_dict(self.polling_filters_criteria_2) if self.polling_filters_criteria_2 else {})
        criteria_list.append(self.create_filter_dict(self.polling_filters_criteria_3) if self.polling_filters_criteria_3 else {})
        exclusions_list = list()
        exclusions_list.append(self.create_filter_dict(self.polling_filters_exclusions_1) if self.polling_filters_exclusions_1 else {})
        exclusions_list.append(self.create_filter_dict(self.polling_filters_exclusions_2) if self.polling_filters_exclusions_2 else {})
        exclusions_list.append(self.create_filter_dict(self.polling_filters_exclusions_3) if self.polling_filters_exclusions_3 else {})

        # The backend_timestamp is the time that the alert becomes searchable in CBC (in other words the CREATED time that 
        # appears in the CBC alert console).  The user_update_timestamp is timestamp of the last property of an alert changed 
        # by a user, such as the alert workflow (status, closure_reason) or determination.  The query_string searches for
        # alerts between last poll time and now for new or updated alerts.  The criteria and exclusions fields further
        # filter the alerts returned from CBC.
        # NOTE (from CBC doc): Only the first 10,000 results of any search are accessible. That means start + rows must be less than 10,000. 
        # To access rows beyond the first 10,000, apply additional filters to reduce the result count.
        query_string = f"backend_timestamp:[{last_poll_time} TO {now_time}] OR user_update_timestamp:[{last_poll_time} TO {now_time}]"
        query = {
            "query": query_string,
            "start": "1",
            "rows": QUERY_LIMIT,
            "sort": [
                {
                "field": "user_update_timestamp",
                "order": "ASC"
                }
            ]
        }
        results = []
        index = 0
        # Loop through the list of polling criteria specified in app.config and append all to results list
        for criteria in criteria_list:
            # Execute at least first criteria even if it is empty json. 
            # After the first time through the loop, skip if there is no criteria specified.
            if index > 0 and not criteria:
                continue
            query["criteria"] = criteria
            query["exclusions"] = exclusions_list[index]
            index += 1

            url = ALERTS_SEARCH.format(cbc_hostname=self.hostname, org_key=self.org_key)
            LOG.debug("Querying endpoint %s with query: %s", url, query)

            response, err_msg = self.rc.execute("POST",
                                                url=url,
                                                headers=self.headers,
                                                json=query,
                                                callback=callback)

            if err_msg:
                LOG.error("%s API call failed: %s", self.package_name, err_msg)
                return None, err_msg

            response_json = response.json()
            results.extend(response_json.get("results", []))

        # If multiple polling filters are specified, then de-dup the list so each alert 
        # only appears in the list once. Reverse to descending order by update timestamp
        # so the latest timestamp ends up in the results.
        if index > 1 and len(results) > 1:
            results.sort(key=lambda item:item["backend_update_timestamp"], reverse=True)
            done = set()
            results_dedupd = []
            for alert in results:
                if alert['id'] not in done:
                    done.add(alert['id'])
                    results_dedupd.append(alert)
            # Order so that the results are ascending so they are created in that order.
            results_dedupd.sort(key=lambda item:item["backend_update_timestamp"], reverse=False)
            return results_dedupd, err_msg

        return results, err_msg
    
    def get_alert_by_id(self, vmware_cbc_alert_id: str):
        """Get the JSON alert data from VMware Carbon Black Cloud given the alert ID.

        Args:
            vmware_cbc_alert_id (str): Carbon Black Cloud alert ID.
        """

        url = ALERTS_URI.format(cbc_hostname=self.hostname, org_key=self.org_key, alert_id=vmware_cbc_alert_id)

        LOG.debug("Querying endpoint with %s", url)

        response, err_msg = self.rc.execute("GET",
                                            url,
                                            headers=self._make_headers(self.token),
                                            callback=callback)

        if err_msg:
            LOG.error("%s API call failed: %s", self.package_name, err_msg)
            return None, err_msg

        response_json = response.json()
        return response_json, None 

    def get_alert_history(self, vmware_cbc_alert_id: str):
        """Get the alert history data from VMware Carbon Black Cloud given the alert ID.

        Args:
            vmware_cbc_alert_id (str): Carbon Black Cloud alert ID.
        """

        url = ALERTS_HISTORY_URI.format(cbc_hostname=self.hostname, org_key=self.org_key, alert_id=vmware_cbc_alert_id)

        LOG.debug("Querying endpoint with %s", url)

        response, err_msg = self.rc.execute("GET",
                                            url,
                                            headers=self._make_headers(self.token),
                                            callback=callback)

        if err_msg:
            LOG.error("%s API call failed: %s", self.package_name, err_msg)
            return None, err_msg

        response_json = response.json()
        return response_json.get("results", []), None
    
    def get_alert_notes(self, vmware_cbc_alert_id: str):
        """Get the alert notes data from VMware Carbon Black Cloud given the alert ID.

        Args:
            vmware_cbc_alert_id (str): Carbon Black Cloud alert ID.
        """

        url = ALERTS_NOTES_URI.format(cbc_hostname=self.hostname, org_key=self.org_key, alert_id=vmware_cbc_alert_id)

        LOG.debug("Querying endpoint with %s", url)

        response, err_msg = self.rc.execute("GET",
                                            url,
                                            headers=self._make_headers(self.token),
                                            callback=callback)

        if err_msg:
            LOG.error("%s API call failed: %s", self.package_name, err_msg)
            return None, err_msg

        response_json = response.json()
        return response_json.get("results", []), None

    def get_threat_notes(self, vmware_cbc_threat_id: str):
        """Get the threat notes data from VMware Carbon Black Cloud given the threat ID.

        Args:
            vmware_cbc_threat_id (str): Carbon Black Cloud threat ID.
        """

        url = THREATS_NOTES_URI.format(cbc_hostname=self.hostname, org_key=self.org_key, threat_id=vmware_cbc_threat_id)

        LOG.debug("Querying endpoint with %s", url)

        response, err_msg = self.rc.execute("GET",
                                            url,
                                            headers=self._make_headers(self.token),
                                            callback=callback)

        if err_msg:
            LOG.error("%s API call failed: %s", self.package_name, err_msg)
            return None, err_msg

        response_json = response.json()
        return response_json.get("results", []), None
    
    def get_cbc_notes(self, id: str, note_type):
        if note_type == "alert":
            return self.get_alert_notes(id)
        else:
            return self.get_threat_notes(id)
        
    def format_cbc_note(self, note: dict) -> str:
        """ Format a CBC note with HTML tags to be post as a SOAR note. 

        Args:
            note (dict): CBC note in JSON format

        Returns:
            str: HTML formatted string with entity comment header
        """
        body = note.get("note","")

        # Build the note string with comment creator in 
        created_at = note.get('create_timestamp',"")
        author = note.get("author", None)

        comment_text = f"<br><b>Note added by<br>{author}</b><br>{created_at}<br><br>{body}"

        # Prepend entity header
        comment_text = f"<b>{ENTITY_COMMENT_HEADER}:</b><br>{comment_text}"
        return comment_text

    def post_alert_note(self, vmware_cbc_alert_id: str, note_text: str, comment_header: str):
        """ Post a note to a CBC alert

        Args:
            vmware_cbc_alert_id (str): CBC alert ID
            note_text (str): Text of the note to add to the CBC alert in CBC
            comment_header (str): comment header text to be pre-pended to comment body text.
                                  The header usually identifies the originating platform of the comment.
        Returns:
            dict, str tuple: JSON response from CBC, error message
        """
        url = ALERTS_NOTES_URI.format(cbc_hostname=self.hostname, org_key=self.org_key, alert_id=vmware_cbc_alert_id)

        if comment_header:
            note_text = "{}:  {}".format(comment_header, note_text)

        body = {"note": note_text}

        LOG.debug("Posting to %s endpoint with %s", url, body)

        response, err_msg = self.rc.execute("POST",
                                            url=url,
                                            headers=self.headers,
                                            json=body,
                                            callback=callback)

        if err_msg:
            LOG.error("%s API call failed: %s", self.package_name, err_msg)
            return None, err_msg

        response_json = response.json()
        return response_json, err_msg
    
    def post_alert_workflow_data(self, alert_id: str, determination: str=None, closure_reason: str=None, 
                                  status: str=None, note_text: str=None, comment_header: str=None):
        """ Update the workflow information in Carbon Black Cloud

        Args:
            alert_id (str): CBC alert ID
            determination (str): CBC determination of the alert (TRUE_POSITIVE, FALSE_POSITIVE, NONE)
            closure_reason (str): CBC reason alert is closed (NO_REASON, RESOLVED, RESOLVED_BENIGN_KNOWN_GOOD, DUPLICATE_CLEANUP, OTHER)
            status (str): CBC alert status (OPEN, IN_PROGRESS, CLOSED)
            note_text (str): text to add as a note to the alert
        """
        url = ALERTS_WORKFLOW_URI.format(cbc_hostname=self.hostname, org_key=self.org_key, alert_id=alert_id)

        if note_text and comment_header:
            note_text = "{}:  {}".format(comment_header, note_text)

        workflow = { "criteria": {
                        "id": [alert_id]
                        },
                    "determination": determination,
                    "closure_reason": closure_reason,
                    "status": status,
                    "note": note_text
                    }
        LOG.debug("Posting to %s endpoint with %s", url, workflow)

        response, err_msg = self.rc.execute("POST",
                                            url=url,
                                            headers=self.headers,
                                            json=workflow,
                                            callback=callback)

        if err_msg:
            LOG.error("%s API call failed: %s", self.package_name, err_msg)
            return None, err_msg

        response_json = response.json()
        request_id = response_json.get("request_id", None)
        
        if request_id:
            job_result, job_err_msg = self.wait_for_job(request_id)
            return job_result, job_err_msg
        
        return response_json, "No request_id returned from call to set workflow information in CBC."
    
    def wait_for_job(self, job_id):
        """ Wait for job request to complete

        Args:
            job_id (str): CBC job ID

        Returns:
            dict, str tuple: JSON response from CBC, error message
        """
        url = JOB_DETAILS_URI.format(cbc_hostname=self.hostname, org_key=self.org_key, job_id=job_id)
        LOG.debug("Querying endpoint with %s", url)

        # Initialize before the while loop.  
        # status returned from CBC will be CREATED, FAILED, COMPLETED
        response_json = {}
        status = None
        start_time = time()
        timed_out = False
        while status not in ["COMPLETED","FAILED"] and not timed_out:
            response, err_msg = self.rc.execute("GET",
                                                url,
                                                headers=self._make_headers(self.token),
                                                callback=callback)

            if err_msg:
                LOG.error("%s API call failed: %s", self.package_name, err_msg)
                status = "FAILED"
            else:
                response_json = response.json()
                status = response_json.get("status", None)
            if status in ["CREATED", None]:
                sleep(self.job_sleep_interval)
                if self.job_timeout != 0 and time() - start_time > self.job_timeout:
                    timed_out = True
        if timed_out and status not in ["COMPLETED","FAILED"]:
            err_msg = f"Job ID {job_id} timed out in {self.job_timeout} seconds."

        return response_json, err_msg

    def post_tags(self, threat_id: str, tags_string: str):
        """ Post a list of tags to the VMware Carbon Black Cloud Threat

        Args:
            threat_id (str): CBC threat ID
            tags (str): Comma separated list of strings (tags)

        Returns:
            dict, str tuple: JSON response from CBC, error message
        """
        url = TAGS_URI.format(cbc_hostname=self.hostname, org_key=self.org_key, threat_id=threat_id)

        LOG.debug("Posting to %s endpoint with tags %s", url, tags_string)

        body = {
            "tags": [tag.strip() for tag in tags_string.split(",")]
        }
        response, err_msg = self.rc.execute("POST",
                                            url=url,
                                            headers=self.headers,
                                            json=body,
                                            callback=callback)

        if err_msg:
            LOG.error("%s API call failed: %s", self.package_name, err_msg)
            return None, err_msg

        response_json = response.json()
        return response_json, err_msg
    
    def get_device_by_id(self, vmware_cbc_device_id: str):
        """Get the JSON device data from VMware Carbon Black Cloud given the device ID.

        Args:
            vmware_cbc_device_id (str): Carbon Black Cloud device ID.
        """

        url = DEVICES_URI.format(cbc_hostname=self.hostname, org_key=self.org_key, device_id=vmware_cbc_device_id)

        LOG.debug("Querying endpoint with %s", url)

        response, err_msg = self.rc.execute("GET",
                                            url,
                                            headers=self.headers,
                                            callback=callback)

        if err_msg:
            LOG.error("%s API call failed: %s", self.package_name, err_msg)
            return None, err_msg

        response_json = response.json()
        return response_json, None

    def post_device_action(self, vmware_cbc_device_id: str, device_action: str, toggle: str):
        """ Post a device action to a CBC device

        Args:
            vmware_cbc__id (str): CBC alert ID
            device_action (str): Device action: QUARANTINE, BYPASS, or BACKGROUND_SCAN
            toggle (str): Determines whether to enable or disable the action: ON, OFF

        Returns:
            dict, str tuple: JSON response from CBC, error message
        """
        url = DEVICE_ACTIONS_URI.format(cbc_hostname=self.hostname, org_key=self.org_key)

        body = {"action_type": device_action,
                "device_id": [vmware_cbc_device_id],
                "options": {"toggle": toggle}
                }

        LOG.debug("Posting to %s endpoint with %s", url, body)

        response, err_msg = self.rc.execute("POST",
                                            url=url,
                                            headers=self.headers,
                                            json=body,
                                            callback=callback)

        if err_msg:
            LOG.error("%s API call failed: %s", self.package_name, err_msg)
            return None, err_msg

        return {"device_status": "success"}, err_msg


    def post_observation_details(self, observations_string: str):
        """ Creates an Observations details job. The details will include information
        about the given event that’s not normally accessible during a search.

        Args:
            observations_string (str): string containing JSON request body to post to the
            investigate /observations/detail_jobs endpoint.

        Returns:
            dict, str tuple: JSON response from CBC, error message
        """
        url = OBSERVATIONS_DETAIL_JOB_URI.format(cbc_hostname=self.hostname, org_key=self.org_key)

        LOG.debug("Posting to %s endpoint with json body: %s", url, observations_string)

        body = loads(observations_string)

        response, err_msg = self.rc.execute("POST",
                                            url=url,
                                            headers=self.headers,
                                            json=body,
                                            callback=callback)

        if err_msg:
            LOG.error("%s API call failed: %s", self.package_name, err_msg)
            return None, err_msg

        response_json = response.json()
        job_id = response_json.get("job_id")

        if not job_id:
            LOG.error("%s API call failed: no job_id found.", self.package_name)
            return None, err_msg
        
        response_results_json, err_msg_results = self.wait_for_observations_job(job_id=job_id)

        if err_msg_results:
            LOG.error("%s API call failed: %s", self.package_name, err_msg_results)
            return None, err_msg_results
        
        return response_results_json, err_msg_results

    def wait_for_observations_job(self, job_id):
        """ Wait for observations job request to complete

        Args:
            job_id (str): CBC job ID

        Returns:
            dict, str tuple: JSON response from CBC, error message
        """
        url = OBSERVATIONS_RESULTS_URI.format(cbc_hostname=self.hostname, org_key=self.org_key, job_id=job_id)
        LOG.debug("Querying endpoint with %s", url)

        # Initialize before the while loop.
        # Job results are complete when "contacted" value equals "completed" value from
        # the observation detail_jobs endpoint.
        response_json = {}
        contacted = -1
        completed = -2
        start_time = time()
        timed_out = False
        while contacted != completed and not timed_out:
            response, err_msg = self.rc.execute("GET",
                                                url,
                                                headers=self.headers,
                                                callback=callback)

            if err_msg:
                LOG.error("%s API call failed: %s", self.package_name, err_msg)
            else:
                response_json = response.json()
                completed = response_json.get("completed", None)
                contacted = response_json.get("contacted", None)
            if contacted != completed:
                sleep(self.job_sleep_interval)
                if self.job_timeout != 0 and time() - start_time > self.job_timeout:
                    timed_out = True
        if timed_out and (contacted != completed):
            err_msg = f"Observations Job ID {job_id} timed out in {self.job_timeout} seconds."

        return response_json, err_msg

    def post_reputations_overrides(self, override_string: str):
        """ Override the reputation of an application by adding a SHA-256 hash, 
        a certificate signer or a path to a known IT tool application or directory 
        of IT tools to an Approved or Banned list.

        Args:
            override_string (str): string containing JSON request body to post to the 
            /reputations/overrides endpoint.

        Returns:
            dict, str tuple: JSON response from CBC, error message
        """
        url = REPUTATION_OVERRIDES_URI.format(cbc_hostname=self.hostname, org_key=self.org_key)

        LOG.debug("Posting to %s endpoint with json body: %s", url, override_string)

        body = loads(override_string)

        response, err_msg = self.rc.execute("POST",
                                            url=url,
                                            headers=self.headers,
                                            json=body,
                                            callback=callback)

        if err_msg:
            LOG.error("%s API call failed: %s", self.package_name, err_msg)
            return None, err_msg

        response_json = response.json()
        return response_json, err_msg

    def create_device_session(self, vmware_cbc_device_id: str):
        """Create a liveresponse session to a device

        Args:
            vmware_cbc_device_id (str): Carbon Black Cloud device ID.

        Returns:
            dict, str tuple: session JSON response from CBC, error message
        """

        url = LIVERESPONSE_SESSIONS_POST_URI.format(cbc_hostname=self.hostname, org_key=self.org_key)

        body = {"device_id": int(vmware_cbc_device_id) }

        LOG.debug("Posting to %s endpoint with json body: %s", url, body)

        response, err_msg = self.rc.execute("POST",
                                            url,
                                            headers=self.headers,
                                            json=body,
                                            callback=callback)

        if err_msg:
            LOG.error("%s API call failed: %s", self.package_name, err_msg)
            return None, err_msg

        response_json = response.json()
        return response_json, None

    def close_device_session(self, vmware_cbc_session_id: str):
        """Delete a liveresponse session to a device.

        Args:
            vmware_cbc_session_id (int): Carbon Black Cloud session ID.
        """

        url = LIVERESPONSE_SESSIONS_DELETE_URI.format(cbc_hostname=self.hostname, org_key=self.org_key, session_id=vmware_cbc_session_id)

        LOG.debug("Posting to %s endpoint.", url)

        response, err_msg = self.rc.execute("DELETE",
                                            url,
                                            headers=self.headers,
                                            callback=callback)

        if err_msg:
            LOG.error("%s API call failed: %s", self.package_name, err_msg)
            return False, err_msg

        return True, None

    def list_processes(self, sessions_id: str):
        """ Use liveresponse endpoint to get the list of processes running on a device.

        Args:
            sessions_id (str): session ID to the device

        Returns:
            list, str: list of processes returned from liveresponse command endpoint, error message if any
        """
        url = LIVERESPONSE_COMMANDS_URI.format(cbc_hostname=self.hostname, org_key=self.org_key, session_id=sessions_id)

        body = {
                "name": "process list"
                }

        LOG.debug("Posting to %s endpoint with json body: %s", url, body)

        response, err_msg = self.rc.execute("POST",
                                            url,
                                            headers=self.headers,
                                            json=body,
                                            callback=callback)

        if err_msg:
            LOG.error("%s API call failed: %s", self.package_name, err_msg)
            return [], err_msg

        response_json = response.json()

        # Get the id of the command that was submit to liveresponse endpoint
        command_id = response_json.get("id", None)
        if command_id >= 0:
            response_json_command, err_msg_command = self.get_command_status(sessions_id, command_id)
            processes = response_json_command.get("processes", [])

            return processes, err_msg_command

        return [], "ERROR: No ID returned from get command status"

    def kill_process(self, device_id: str, process_id: str):
        """ Send liveresponse to the device to kill a process.

        Args:
            device_id (str): Device ID of the device
            process_id (str): PID of the process to terminate

        Returns:
            dict, str: JSON returned from livereponse command endpoint to kill the process, error message if any
        """
        # Open a session to the device
        session_response, err_msg = self.create_device_session(device_id)
        if err_msg:
            LOG.error("%s API call to create session failed: %s", self.package_name, err_msg)
            return None, err_msg

        session_status = session_response.get("status", None)
        session_id = session_response.get("id", None)
        if session_status != "ACTIVE":
            LOG.error("%s session status is not ACTIVE: %s", self.package_name, session_status)
            return session_response, "No ACTIVE session found - try again later"

        # Check if process is running before trying to kill it.
        pid = int(process_id)

        processes, err_msg_processes = self.list_processes(session_id)

        if err_msg_processes:
            LOG.error("%s API call to list process failed: %s", self.package_name, err_msg)
            return session_response, err_msg_processes

        pid_running = False
        for proc in processes:
            if proc.get("process_pid", None) == pid:
                pid_running = True
                break

        if not pid_running:
            return session_response, f"Process ID {pid} is not running on the sensor"

        # Setup call to kill the process
        url = LIVERESPONSE_COMMANDS_URI.format(cbc_hostname=self.hostname, org_key=self.org_key, session_id=session_id)

        body = {
                "name": "kill",
                "pid": pid
                }

        LOG.debug("Posting to %s endpoint with json body: %s", url, body)

        response, err_msg = self.rc.execute("POST",
                                            url,
                                            headers=self.headers,
                                            json=body,
                                            callback=callback)

        if err_msg:
            LOG.error("%s API call to kill process failed: %s", self.package_name, err_msg)
            return None, err_msg

        response_json = response.json()

        # Get the id of the command that was submit to liveresponse endpoint so we can check the status
        command_id = response_json.get("id", None)
        if command_id is not None and command_id >= 0:
            response_json_command, err_msg_command = self.get_command_status(session_id, command_id)
            if err_msg_command:
                LOG.error("%s API call to get command status failed: %s", self.package_name, err_msg)
                return None, err_msg

            return response_json_command, err_msg_command
        else:
            return response_json, "ERROR: No ID returned from get command status in kill process function"

    def get_command_status(self, session_id: str, command_id: int):
        """ Get the status of a command sent to the liveresponse endpoint.
            Documentation says "status" is one of the following: “in progress”, “complete”, “cancel”, “error”

        Args:
            command_id (int): ID of the liveresponse command.  
                              command_id is returned from liveresponse /commands endpoint 

        Returns:
            dict, error_msg: JSON returned from CBC liveresponse get command status endpoint, error message if any
        """
        url = LIVERESPONSE_COMMANDS_STATUS_URI.format(cbc_hostname=self.hostname, org_key=self.org_key, session_id=session_id, command_id=command_id)
        LOG.debug("Querying endpoint with %s", url)

        status = "in progress"
        while status.lower() in ["in progress", "in_progress", "pending"]:
            response_status, err_msg_status = self.rc.execute("GET",
                                                              url,
                                                              headers=self.headers,
                                                              callback=callback)
            if err_msg_status:
                LOG.error("%s API call failed: %s", self.package_name, err_msg_status)
                return None, err_msg_status

            response_json_status = response_status.json()
            # Get status of the command. 
            # Doc says "status" is one of the following: “in progress”, “complete”, “cancel”, “error”
            # But status seems to be capitalized, so compare in lower case.
            status = response_json_status.get("status", None)

            # command_timeout should force an "error" status
            if status.lower() in ["complete", "error", "cancel"]:
                return response_json_status, err_msg_status

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
            msg = resp.get('error', None) or resp.get('error_code', None)
            details = resp.get('path', None) or resp.get('message', None)
        except JSONDecodeError as err:
            msg = str(err)
            details = response.text

        error_msg  = "Error: \n    status code: {0}\n    message: {1}\n    details: {2}".format(
            response.status_code,
            msg,
            details)

    return response, error_msg
