# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.

"""VirusTotal REST API client"""

import base64
import logging 
from resilient_lib import RequestsCommon, IntegrationError, validate_fields, str_to_bool

LOG = logging.getLogger(__name__)

BASE_URL = "https://virustotal.com/api/v3"

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

    def get_headers(self, auth_token):
        """ Return the authorization header.
        """
        headers = {
            "accept": "application/json",
            "x-apikey": "{0}".format(auth_token),
            "content-type": "application/x-www-form-urlencoded"
        }
        return headers

    def scan_url(self, url):
        endpoint_url = "{0}{1}".format(self.base_url, SCAN_URI)
        response = self.rc.execute("POST",
                                   endpoint_url,
                                   data=url,
                                   headers=self.headers)
        return response.json()

    def get_url_report(self, url):
        url_id = base64.urlsafe_b64encode(url.encode()).decode().strip("=")

        endpoint_url = "{0}/urls/{id}".format(self.base_url, id=url_id)
        response = self.rc.execute("GET",
                                   endpoint_url,
                                   headers=self.headers)
        return response.json()

    def scan_file(self, file_to_scan, filename):
        endpoint_url = "{0}/files".format(self.base_url)
        # files = {"file": ("copy.txt", open("copy.txt", "rb"), "text/plain")}
        files = {"file": (filename, open(file_to_scan, "rb"), "text/plain")}
        headers_for_file = {
            "accept": "application/json",
            "x-apikey": self.headers["x-apikey"]
        }
#            "content-type": "multipart/form-data"
        response = self.rc.execute("POST",
                                   endpoint_url,
                                   files=files,
                                   headers=headers_for_file)
        response_json = response.json()
        data = response_json.get("data", None)
        if data is not None:
            links = data.get("links", None)
            if links is not None:
                endpoint_url = links.get("self", None)
                analysis_response = self.rc.execute("GET",
                                                endpoint_url,
                                                headers=self.headers)
                analysis_response_json = analysis_response.json()
                return analysis_response_json


    def get_file_report(self, id):
        endpoint_url = "{0}/files/{id}".format(self.base_url, id=id)
        response = self.rc.execute("GET",
                                   endpoint_url,
                                   headers=self.headers)
        return response.json()

    def get_ip_report(self, ip):
        endpoint_url = "{0}/ip_addresses/{ip}".format(self.base_url, ip=ip)
        response = self.rc.execute("GET",
                                   endpoint_url,
                                   headers=self.headers)
        return response.json()

    def get_domain_report(self, domain):
        endpoint_url = "{0}/domains/{domain}".format(self.base_url, domain= domain)
        response = self.rc.execute("GET",
                                   endpoint_url,
                                   headers=self.headers)
        return response.json()
