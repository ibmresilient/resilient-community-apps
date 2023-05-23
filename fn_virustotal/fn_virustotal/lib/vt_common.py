# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.

"""VirusTotal REST API client"""
import os
import base64
import time
import json
from urllib.parse import urlencode
import logging 
from resilient_lib import RequestsCommon, IntegrationError, validate_fields, str_to_bool

LOG = logging.getLogger(__name__)

BASE_URL = "https://virustotal.com/api/v3"
VT_MAX_FILE_UPLOAD_SIZE_MB = 650
VT_MAX_FILE_SIZE_MB = 32

class VirusTotalClient(object):
    def __init__(self, opts, options):
        # Read the configuration options
        required_fields = ["api_token", "polling_interval_sec", "max_polling_wait_sec"]
        validate_fields(required_fields, options)
        self.rc = RequestsCommon(opts, options)
        self.api_token = options.get("api_token")
        self.polling_interval_sec = options.get("polling_interval_sec")
        self.max_polling_wait_sec = options.get("max_polling_wait_sec")
        self.base_url = BASE_URL

        self.verify = str_to_bool(options.get("verify", "true"))
        self.headers = self.get_headers(self.api_token)

    def get_headers(self, auth_token: str) -> dict:
        """ Return the authorization header with the auth token filled in.
        """
        headers = {
            "accept": "application/json",
            "x-apikey": "{0}".format(auth_token),
            "content-type": "application/x-www-form-urlencoded"
        }
        return headers

    def scan_url(self, url: str) -> dict:
        """ Perform a VirusTotal scan on a URL.

        Args:
            url (str): URL to be scanned

        Returns:
            dict: Return the VT scan results in json format.
            str: code returned from the VT REST API 
        """
        endpoint_url = "{0}/urls".format(self.base_url)
        payload = urlencode({"url":url})
        response, code = self.rc.execute("POST",
                                   endpoint_url,
                                   data=payload,
                                   headers=self.headers,
                                   callback=callback)
        response_json = response.json()
        return response_json, code

    def wait_for_scan_to_complete(self, response_json: dict) -> tuple[dict, str]:
        """Given a VirusTotal JSON scan analysis object returned from VirusTotal scan submission, 
        use the time parameters in the app.config to poll for the analysis to complete.

        Args:
            response_json (dict): JSON object that is returned from a call to the VirusTotal endpoint
                                  to scan a file or URL.  The JSON contains information on how to poll
                                  to get the analysis information when and determine when it is complete.

        Raises:
            IntegrationError: No "data" in VirusTotal scan JSON object.
            IntegrationError: No links in VirusTotal scan JSON object.
            IntegrationError: No self link in VirusTotal scan JSON object.
            IntegrationError: Invalid analysis status.
            IntegrationError: VirusTotal scan analysis is not complete - MAX poll time exceeded!

        Returns:
            dict: JSON object of the analysis scan
            str: status of the analysis (completed, in_progress, queued)
        """
        data = response_json.get("data", None)
        if not data or data.get("type", None) != "analysis":
            raise IntegrationError("No data in VirusTotal scan JSON object.")

        links = data.get("links", None)
        if not links:
            raise IntegrationError("No links in VirusTotal scan JSON object.")
 
        endpoint_url = links.get("self", None)
        if not endpoint_url:
            raise IntegrationError("No self link in VirusTotal scan JSON object.") 

        start_time = curr_time = time.time()
        # Loop until analysis status is complete of the max poll time is exceeded.
        while int(curr_time - start_time)/1000 <= int(self.max_polling_wait_sec):
            # Check the end point to see if the analysis is complete.
            analysis_response = self.rc.execute("GET",
                                                endpoint_url,
                                                headers=self.headers)
            analysis_response_json = analysis_response.json()
            LOG.info("analysis_response_json = {}".format(analysis_response_json))
            analysis_data = analysis_response_json.get("data", {})
            if analysis_data:
                attributes = analysis_data.get("attributes", {})
                if attributes:
                    status = attributes.get("status", None)
                    if status == "completed":
                        # Exit the loop when the analysis is complete.
                        return analysis_response_json, status
                    elif status in ["in-progress", "queued"]:
                        # resubmit
                        curr_time = time.time()
                        if int(curr_time - start_time)/1000 >= int(self.max_polling_wait_sec):
                            raise IntegrationError("exceeded max wait time: {}".format(self.max_polling_wait_sec))

                        time.sleep(int(self.polling_interval_sec))
                        # start again to review results
                    else:
                        raise IntegrationError("Invalid analysis status: {}.".format(status))

        raise IntegrationError("VirusTotal scan analysis is not complete - MAX poll time exceeded!")

    def get_url_report(self, url: str) -> tuple[dict, str]:
        """ Get the URL report from VirusTotal on the URL (if there is one).

        Args:
            url (str): URL to get VT information on.

        Returns:
            dict: Return VT scan report in JSON format.
            str: code returned from the VT REST API.
        """
        # urlencode the URL with command from VirusTotal REST API doc.
        url_id = base64.urlsafe_b64encode(url.encode()).decode().strip("=")

        endpoint_url = "{0}/urls/{id}".format(self.base_url, id=url_id)
        response, code = self.rc.execute("GET",
                                   endpoint_url,
                                   headers=self.headers,
                                   callback=callback)
        return response.json(), code

    def scan_file(self, file_to_scan: str, filename: str) -> tuple[dict, str]:
        """ Scan a file using VirusTotal.

        Args:
            file_to_scan (str): file path of file to be scanned
            filename (str): filename of file to be scanned

        Raises:
            IntegrationError: Raise error if the file to be scanned is larger than what VT will accept
            IntegrationError: Raise error if unable to get URL from VT on where to post the (large > 32MB) file

        Returns:
            dict: Return VT status on file analyses in JSON format.
            str: code returned from the VT REST API 
        """
        start_time = time.time()
        # files = {"file": ("copy.txt", open("copy.txt", "rb"), "text/plain")}
        files = {"file": (filename, open(file_to_scan, "rb"), "application/octet-stream")}
        headers_for_file = {
            "accept": "application/json",
            "x-apikey": self.headers["x-apikey"]
        }
        # If the file to be scanned is greater than 32MB, we need to call VT endpoint
        # to get a URL to load the file to. 
        # First compute filesize in MBs.
        files_size_MB = round(os.path.getsize(file_to_scan) / 1024**2, 3)
        if files_size_MB > VT_MAX_FILE_UPLOAD_SIZE_MB:
            raise IntegrationError("Cannot upload a file larger than {0} to VirusTotal: file size is {1} MB!".format(VT_MAX_FILE_UPLOAD_SIZE_MB, files_size_MB))

        if files_size_MB >= VT_MAX_FILE_SIZE_MB:
            response = self.get_upload_url()
            vt_upload_url = response.get("data", None)
        else:
            vt_upload_url = "{0}/files".format(self.base_url)
        if vt_upload_url is None:
            raise IntegrationError("Error getting file upload URL from VirusTotal")

        response, code = self.rc.execute("POST",
                                   vt_upload_url,
                                   files=files,
                                   headers=headers_for_file,
                                   callback=callback)
        return response.json(), code


    def get_file_report(self, id: str)  -> tuple[dict, str]:
        """ Get a file report from VirusTotal if one is available.

        Args:
            id (str): SHA-256, SHA-1 or MD5 identifying the file

        Returns:
            dict: Return information on the file from VT in JSON format
            str: code returned from the VT REST API 
        """
        endpoint_url = "{0}/files/{id}".format(self.base_url, id=id)
        response, code = self.rc.execute("GET",
                                   endpoint_url,
                                   callback=callback,
                                   headers=self.headers)
        return response.json(), code

    def get_ip_report(self, ip: str)  -> tuple[dict, str]:
        """ Get a VirusTotal IP address report

        Args:
            ip (str): IP address to get report on

        Returns:
            dict: Returns a report in JSON format from VT
            str: code returned from the VT REST API 
        """
        endpoint_url = "{0}/ip_addresses/{ip}".format(self.base_url, ip=ip)
        response, code = self.rc.execute("GET",
                                   endpoint_url,
                                   callback=callback,
                                   headers=self.headers)
        return response.json(), code

    def get_domain_report(self, domain: str) -> tuple[dict, str]:
        """ Get a VirusTotal Domain report
        Args:
            domain (str): Domain to get report on

        Returns:
            dict: Returns a report in JSON format from VT
            str: code returned from the VT REST API 
        """
        endpoint_url = "{0}/domains/{domain}".format(self.base_url, domain=domain)
        response, code = self.rc.execute("GET",
                                   endpoint_url,
                                   callback=callback,
                                   headers=self.headers)
        return response.json(), code

    def get_upload_url(self) -> dict:
        """ Get a VT URL where a large file (greater than 32 MB and less than 650 MB)
            (Smaller files can be post directly to the /files endpoint) 

        Returns:
            dict: JSON object contains URL where a file can be uploaded to for analyses.
            (URL is returned in the "data" field.)
        """
        endpoint_url = "{0}/files/upload_url".format(self.base_url)
        response = self.rc.execute("GET",
                                   endpoint_url,
                                   headers=self.headers)
        return response.json()

    def get_sha256_from_file_result(self, file_result: dict) -> str:
        """ Return the sha 256 hash from the results of a VT file scan.

        Args:
            file_result (dict): JSON object from VT scan

        Returns:
            str : SHA-256 hash 
        """
        sha256 = None
        meta = file_result.get("meta", None)
        if meta and meta.get("file_info", None):
            file_info = meta.get("file_info", None)
            if file_info and file_info.get("sha256", None):
                return file_info.get("sha256", None)
        return sha256

def callback(response: dict) -> tuple[dict, str]:
    """
    callback needed for certain REST API calls to return a formatted code (string).
    :param response:
    :return: response, code
    """
    if response.status_code < 300:
        code = "success"
    elif response.status_code in [400,404]:
        content = json.loads(response.text)
        error = content.get("error", None)
        code = error.get("code", None) if error else None
    else:
        response.raise_for_status()

    return response, code
