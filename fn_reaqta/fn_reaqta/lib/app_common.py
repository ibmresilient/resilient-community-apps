# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
import logging
import ntpath
import time
from datetime import datetime
from io import BytesIO
from urllib.parse import urljoin
from fn_reaqta.lib.poller_common import IBM_SOAR
from resilient_lib import str_to_bool, readable_datetime, write_file_attachment, clean_html
from fn_reaqta.lib.poller_common import eval_mapping, s_to_b

LOG = logging.getLogger(__name__)

HEADER = { 'Content-Type': 'application/json' }

ENDPOINT_URI = "endpoint/{}/"
ENDPOINT_FILE_URI = "endpoint-file/{}/"
ALERT_URI = "alert/{}/"

DOWNLOAD_WAIT_SEC = 15  # number of seconds to wait between status checks for a file download

class AppCommon():
    def __init__(self, rc, options):
        self.api_key = options['api_key']
        self.api_secret = options['api_secret']
        self.reaqta_url = options['reaqta_url']
        self.api_version = options['api_version']
        self.rc = rc
        self.verify = str_to_bool(options.get("cafile", "false"))

        # set any additional filters to include for alert query
        self.filters = eval_mapping(options.get('poller_filters', ''), wrapper='{{ {} }}')

        self.token = self.header = None

    def get_filters(self):
        return self.filters

    def authenticate(self, refresh=False):
        if refresh or not self.token:
            params = {
                "secret": self.api_secret,
                "id": self.api_key
            }

            response, err_msg = self.api_call("POST", 'authenticate', params, refresh_authentication=None)
            if not err_msg:
                self.token = response.json()['token']
                self.header = self._make_header(self.token)

            return err_msg

    def get_entities_since_ts(self, query_field_name, timestamp, optional_filters):
        """get changed entities since last poller run

        Args:
            query_field_name (str): field to use for
            timestamp (datetime): datetime when the last poller ran
            optional_filters (dict): name/value pairs for query criteria

        Returns:
            list: changed entity list
        """
        query = {
            query_field_name: readable_datetime(timestamp) # utc datetime format
        }

        # add any additional query parameters
        if optional_filters:
            for k,v in optional_filters.items():
                query[k] = v

        LOG.debug(query)
        response, err_msg = self.api_call("GET", 'alerts', query, refresh_authentication=True)
        return response.json()

    def get_next_entities(self, next_url):
        """This endpoint pages result size. This method is used for subsequent calls

        Args:
            next_url (str): url provided by endpoint API call to get next paged list

        Returns:
            list: next entity paged result
        """
        response = self.rc.execute("GET", next_url, headers=self.header, verify=self.verify)
        return response.json()

    def isolate_machine(self, endpoint_id):
        url = urljoin(ENDPOINT_URI.format(endpoint_id), "isolate")

        response, err_msg = self.api_call("POST", url, None)
        return response.json()

    def get_processes(self, endpoint_id):
        url = urljoin(ENDPOINT_URI.format(endpoint_id), "processes")

        response, err_msg = self.api_call("GET", url, None)
        return response.json()

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

    def attach_file(self, rest_client, incident_id, endpoint_id, program_path):
        # collect the file name
        file_name = ntpath.basename(program_path)

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
                if response.status_code == 200 and response.json().get("downloadId"):
                    results = response.json()
                    download_id = results["downloadId"]
                    break

            if download_id:
                url = urljoin(ENDPOINT_FILE_URI.format(download_id), "download")
                response, err_msg = self.api_call("GET", url, None)

                attachment = BytesIO(s_to_b(response.text))
                results = write_file_attachment(rest_client, file_name, attachment, incident_id)

        return results

    def close_alert(self, alert_id, is_malicious):
        params = {
            "alertId": alert_id,
            "closed": True,
            "malicious": is_malicious
            }

        url = urljoin(ALERT_URI.format(alert_id), "close")
        response, err_msg = self.api_call("POST", url, params)

        return (response.json(), err_msg) if not err_msg else (None, err_msg)

    def get_alert(self, alert_id):
        url = ALERT_URI.format(alert_id)
        response, err_msg = self.api_call("GET", url, None)

        return (response.json(), err_msg) if not err_msg else (None, err_msg)

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

        return (response.json(), err_msg) if not err_msg else (None, err_msg)

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

    def make_linkback_url(self, template_uri, entity_id):
        """Create a url to link back to the endpoint alert, case, etc.

        Args:
            template (str): portion of url to join with base url
            entity_id (str/int): id representing the alert, case, etc.

        Returns:
            str: completed url for linkback
        """
        return urljoin(self.reaqta_url, template_uri.format(entity_id))

    def api_call(self, method, url, payload, refresh_authentication=False):
        if refresh_authentication is not None:
            self.authenticate(refresh=refresh_authentication)

        if method in ["PUT", "POST"]:
            return self.rc.execute(method,
                                   self._get_uri(url),
                                   json=payload,
                                   headers=self.header,
                                   verify=self.verify,
                                   callback=callback)
        elif payload:
            return self.rc.execute(method,
                                   self._get_uri(url),
                                   params=payload,
                                   headers=self.header,
                                   verify=self.verify,
                                   callback=callback)
        else:
            return self.rc.execute(method,
                                   self._get_uri(url),
                                   headers=self.header,
                                   verify=self.verify,
                                   callback=callback)

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
        msg = resp.get('messages')
        details = resp.get('details')
        error_msg  = u"ReaQta Error: \n    status code: {0}\n    message: {1}\n    details: {2}".format(
            response.status_code,
            msg,
            details)

    return response, error_msg