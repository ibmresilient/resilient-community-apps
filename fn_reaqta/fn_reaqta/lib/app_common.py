# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
import logging
import time
from datetime import datetime
from io import BytesIO
from urllib.parse import urljoin
from fn_reaqta.lib.soar_common import IBM_SOAR, eval_mapping, s_to_b
from resilient_lib import validate_fields, str_to_bool, readable_datetime, clean_html
from cachetools import cached, LRUCache
from retry import retry

LOG = logging.getLogger(__name__)

PACKAGE_NAME = "fn_reaqta"

HEADER = { 'Content-Type': 'application/json' }

ENDPOINT_URI = "endpoint/{}/"
ENDPOINT_FILE_URI = "endpoint-file/{}/"
ALERT_URI = "alert/{}/"
POLICY_URI = "policy/"
POLICIES_URI = "policies"
POLICY_DETAILS = "policies/details/{}"
ENDPOINT_GROUP_URI = "endpoint-groups"

LINKBACK_URL = "alerts/{}"   # url to generate back to the entity (case, alert, etc.)

DOWNLOAD_WAIT_SEC = 15  # number of seconds to wait between status checks for a file download

class AuthenticationError(Exception):
    """Trap authentication errors for reauthenticating"""
    pass

class AppCommon():
    def __init__(self, rc, options):
        validate_fields([
                            "reaqta_url",
                            "api_version",
                            "cafile",
                            "api_key",
                            "api_secret"
                        ],
                        options)
        self.api_key = options['api_key']
        self.api_secret = options['api_secret']
        self.reaqta_url = options['reaqta_url']
        self.api_version = options['api_version']
        self.rc = rc
        self.verify = str_to_bool(options.get('cafile', 'false'))

        # set any additional filters to include for alert query
        self.filters = eval_mapping(options.get('polling_filters', ''), wrapper='{{ {} }}')

        self.token = self.header = None

    def get_filters(self):
        return self.filters

    def authenticate(self):
        """authenticate to ReaQta

        Args:
            api_call (bool, optional): bypass if called from the api_call function. Defaults to False.

        Returns:
            str: err_msg or None
        """
        self.token = "pending" # needed to avoid infinite loop with api_call()

        params = {
            "secret": self.api_secret,
            "id": self.api_key
        }

        response, err_msg = self.api_call("POST", 'authenticate', params)
        if err_msg:
            return err_msg

        # determine if response is successful
        result = response.json()
        if not result.get('token'):
            return result.get('message') if result.get('message') else result

        self.token = result.get('token')
        self.header = self._make_header(self.token)
        return None

    def get_entities_since_ts(self, query_field_name, timestamp, optional_filters, refresh_authentication=False):
        """get changed entities since last poller run

        Args:
            query_field_name (str): field to use for ReaQta field to query on
            timestamp (datetime): datetime when the last poller ran
            optional_filters (dict): name/value pairs for query criteria

        Returns:
            list: changed entity list
        """
        query = { }

        if query_field_name:
            query[query_field_name] = readable_datetime(timestamp) # utc datetime format

        # add any additional query parameters
        groups_filter = []
        impact_filter = None
        if optional_filters:
            # groups and relevance are managed after the api call is made
            if "groups" in optional_filters:
                groups_filter = optional_filters.pop('groups')
            if "impact" in optional_filters:
                impact_filter = int(optional_filters.pop('impact'))

            for k,v in optional_filters.items():
                query[k] = v

        LOG.debug(query)
        response, err_msg = self.api_call("GET", 'alerts', query, refresh_authentication=refresh_authentication)

        results = response if isinstance(response, dict) else response.json()

        # trim results by optional filters
        if not err_msg and (groups_filter or impact_filter):
            filtered_results = []
            for alert in results['result']:
                accept_filtered = False
                # both groups_filter and impact_filter need to succeed if both are specified
                if groups_filter:
                    # get the endpoint groups and test if list and filters intersect
                    endpoint_groups = [group['name'] for group in alert.get("endpoint", {}).get("groups", [])]
                    if list(set(groups_filter) & set(endpoint_groups)):
                        accept_filtered = True

                if impact_filter:
                    accept_filtered = bool(alert.get("impact") >= impact_filter)

                if accept_filtered:
                    filtered_results.append(alert)

            LOG.info("Original List: %s. Filtered List: %s", len(results), len(filtered_results))
            results = { "result": filtered_results }

        return results, err_msg

    def get_next_page(self, next_url):
        """This endpoint pages result size. This method is used for subsequent calls

        Args:
            next_url (str): url provided by endpoint API call to get next paged list

        Returns:
            list: next entity paged result
        """
        response, err_msg = self.api_call("GET", next_url, None)

        return response.json()

    def isolate_machine(self, endpoint_id):
        url = urljoin(ENDPOINT_URI.format(endpoint_id), "isolate")

        response, err_msg = self.api_call("POST", url, None)
        return response.json(), err_msg

    def get_processes(self, endpoint_id):
        url = urljoin(ENDPOINT_URI.format(endpoint_id), "processes")

        response, err_msg = self.api_call("GET", url, None)
        return response.json()

    def get_endpoint_status(self, endpoint_id):
        url = ENDPOINT_URI.format(endpoint_id)

        response, err_msg = self.api_call("GET", url, None)
        return response.json(), err_msg

    def kill_process(self, endpoint_id, process_pid, start_time):
        url = urljoin(ENDPOINT_URI.format(endpoint_id), "processes/kill")
        payload = [
            {
                "pid": process_pid,
                "startTime": start_time
            }
        ]

        response, err_msg = self.api_call("POST", url, payload)
        return response.json()

    def get_program_file(self, endpoint_id, program_path):

        url = urljoin(ENDPOINT_URI.format(endpoint_id), "request-file")
        payload = {
            "path": program_path,
        }

        response, err_msg = self.api_call("POST", url, payload)

        # go into a spin loop waiting for the request to complete
        if response.status_code == 200 and response.json().get('uploadId'):
            results = response.json()
            upload_id = results['uploadId']
            download_id = None
            url = urljoin(ENDPOINT_FILE_URI.format(upload_id), "status")

            for _ in range(0, 3):
                time.sleep(DOWNLOAD_WAIT_SEC)
                response, err_msg = self.api_call("GET", url, None)
                if not response.status_code == 200:
                    break

                if response.json().get("downloadId"):
                    results = response.json()
                    download_id = results["downloadId"]
                    break
                if response.json().get("stage", {}).get("error"):
                    err_msg = response.json().get("stage", {}).get("error")
                    break

            if download_id:
                url = urljoin(ENDPOINT_FILE_URI.format(download_id), "download")
                response, err_msg = self.api_call("GET", url, None)

                return BytesIO(s_to_b(response.text)), None

        return {}, err_msg

    def close_alert(self, alert_id, is_malicious):
        params = {
            "alertId": alert_id,
            "closed": True,
            "malicious": is_malicious
            }

        url = urljoin(ALERT_URI.format(alert_id), "close")
        response, err_msg = self.api_call("POST", url, params)

        return (response.json(), err_msg) if not err_msg else ({}, err_msg)

    def get_alert(self, alert_id):
        url = ALERT_URI.format(alert_id)
        url = url[:-1] if url[-1] == '/' else url
        response, err_msg = self.api_call("GET", url, None)

        return (response.json(), err_msg) if not err_msg else ({}, err_msg)

    def create_note(self, alert_id, note, header=IBM_SOAR):
        # get the existing note so we can append the new content
        response, err_msg = self.get_alert(alert_id)
        if not err_msg:
            existing_note = response.get('notes')

            params = {
                "notes": make_comment(existing_note, note, header=header)
            }

            url = urljoin(ALERT_URI.format(alert_id), "notes")
            response, err_msg = self.api_call("PUT", url, params)

        return (response.text, err_msg) if not err_msg else ({}, err_msg)

    def create_policy(self, fn_inputs):
        """create a policy based on a file hash

        Args:
            fn_inputs (dict): inputs to API call
            -   fn_inputs.reaqta_policy_title
            -   fn_inputs.reaqta_policy_block
            -   fn_inputs.reaqta_policy_included_groups
            -   fn_inputs.reaqta_policy_excluded_groups
            -   fn_inputs.reaqta_sha256
            -   fn_inputs.reaqta_policy_description
            -   fn_inputs.reaqta_policy_enabled

        Returns:
            (dict, str): API call results and an err_msg, if an error occured
        """

        # determine if the policy is already in place
        response, err_msg = self._get_policy_by_sha256(fn_inputs.get('reaqta_sha256'))
        if err_msg:
            return {}, err_msg

        policy_info = response.json()
        if policy_info.get('result'):
            return {}, 'A policy already exists for this file hash: {0}. <a href="{1}" target="blank">{1}</a>'.format(
                fn_inputs.get('reaqta_sha256'),
                self.make_linkback_url(policy_info['result'][0]['id'], POLICY_DETAILS))

        params = {
            "sha256": fn_inputs.get('reaqta_sha256'),
            "title": fn_inputs.get('reaqta_policy_title', ''),
            "description": fn_inputs.get('reaqta_policy_description', ''),
            "disable": not fn_inputs.get('reaqta_policy_enabled', True),
            "block": fn_inputs.get('reaqta_policy_block', False),
            "enabledGroups": [],
            "disabledGroups": []
        }

        # collect all the group names and find the groupIds
        if fn_inputs.get('reaqta_policy_included_groups'):
            group_name_list = [ group.strip() for group in fn_inputs.get('reaqta_policy_included_groups', "").split(',') ]
            group_id_list = self.get_group_ids(group_name_list)
            if group_id_list:
                params['enabledGroups'] = group_id_list

        if fn_inputs.get('reaqta_policy_excluded_groups'):
            group_name_list = [ group.strip() for group in fn_inputs.get('reaqta_policy_excluded_groups', "").split(',') ]
            group_id_list = self.get_group_ids(group_name_list)
            if group_id_list:
                params['disabledGroups'] = group_id_list

        LOG.debug("create_policy: %s", params)
        url = urljoin(POLICY_URI, "trigger-on-process-hash")
        return self.api_call("POST", url, params)

    def _get_policy_by_sha256(self, sha256):
        """find a policy based on it's sha256 value

        Args:
            sha256 (str): file sh256 value to check if a policy already exists

        Returns:
            dict/None, str: return the policy, if found and an error msg
        """
        params = {
            "hash": [sha256],
            "alg": [1]
        }

        LOG.debug("_get_policy_by_sha256: %s", params)
        return self.api_call("GET", POLICIES_URI, params)

    def _get_uri(self, cmd):
        """build API url

        Args:
            cmd (str): portion of API: alerts, endpoints, policies

        Returns:
            str: complete URL
        """
        return urljoin(urljoin(self.reaqta_url, self.api_version), cmd)

    def _make_header(self, token):
        """Build API header using authorization token

        Args:
            token (str): authorization token

        Returns:
            dict: complete header
        """
        header = HEADER.copy()
        header['Authorization'] = "Bearer {}".format(token)

        return header

    def make_linkback_url(self, entity_id, linkback_url=LINKBACK_URL):
        """Create a url to link back to the endpoint alert, case, etc.

        Args:
            template (str): portion of url to join with base url
            entity_id (str/int): id representing the alert, case, etc.

        Returns:
            str: completed url for linkback
        """
        return urljoin(self.reaqta_url, linkback_url.format(entity_id))

    @retry(AuthenticationError, tries=2, delay=2)
    def api_call(self, method, url, payload, refresh_authentication=False):
        if not self.token or refresh_authentication:
            err_msg = self.authenticate()
            if err_msg:
                return {}, err_msg

        # save token. Normal operation will restore it
        #  if AuthenticationError, the token will be recreated
        token_sv = self.token
        self.token = None

        if method in ["PUT", "POST"]:
            response, err_msg = self.rc.execute(method,
                                   self._get_uri(url),
                                   json=payload,
                                   headers=self.header,
                                   verify=self.verify,
                                   callback=callback)
        elif payload:
            response, err_msg =  self.rc.execute(method,
                                   self._get_uri(url),
                                   params=payload,
                                   headers=self.header,
                                   verify=self.verify,
                                   callback=callback)

        else:
            response, err_msg = self.rc.execute(method,
                               self._get_uri(url),
                               headers=self.header,
                               verify=self.verify,
                               callback=callback)

        self.token = token_sv # restore value
        return response, err_msg

    def get_group_ids(self, group_name_list):
        group_id_list = []
        for group_name in group_name_list:
            response, err_msg = self._get_endpoint_group(group_name)
            if err_msg:
                LOG.error("_get_endpoint_group error: %s", err_msg)
            else:
                group_result = response.json()
                if group_result.get("result"):
                    group_id_list.append(group_result["result"][0]['id'])
                else:
                    LOG.warning("Unable to find group: %s", group_name)

        return group_id_list

    @cached(cache=LRUCache(maxsize=100))
    def _get_endpoint_group(self, group_name):
        """ cached API call to get group information """
        params = {
            "name": group_name
        }

        response, err_msg = self.api_call("GET", ENDPOINT_GROUP_URI, params)
        if not err_msg:
            result = response.json()
            if result.get("nextPage"):
                response_next = self.get_next_page(result.get("nextPage"))

        return response, err_msg

def make_comment(existing_note, note, header=IBM_SOAR):
    # add datestamp
    now = datetime.now()
    ts = now.strftime("%d/%m/%Y %H:%M:%S")

    return '\n'.join([existing_note if existing_note else "",
                      "{} {}".format(header, ts),
                      clean_html(note)])

def callback(response):
    """
    callback needed for certain REST API calls to return a formatted error message
    :param response:
    :return: response, error_msg
    """
    error_msg = None
    if response.status_code >= 300 and response.status_code < 500:
        resp = response.json()
        if response.status_code == 401 and resp.get("message") == "Authentication Error":
            raise AuthenticationError()

        msg = resp.get('messages') or resp.get('message')
        details = resp.get('details')
        error_msg  = u"ReaQta Error: \n    status code: {0}\n    message: {1}\n    details: {2}".format(
            response.status_code,
            msg,
            details)

    return response, error_msg

def get_hive_options(hive_label, opts):
    """Return app.config section parameters

    Args:
        hive_label (str): label used in app.config as: [fn_reaqta:hive_label]
        opts (dict): all app.config section information

    Returns:
        dict: section settings found or None
    """
    section_header = "{}:{}".format(PACKAGE_NAME, hive_label)
    if not opts.get(section_header):
        LOG.warning("Unable to find section header: %s", section_header)
        return None

    return opts.get(section_header)
