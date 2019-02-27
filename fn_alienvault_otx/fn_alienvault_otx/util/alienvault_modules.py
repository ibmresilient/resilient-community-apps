# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
# -*- coding: utf-8 -*-
""" Alien Vault OTX module to Access OTX threat Intelligence Data"""
import json
import datetime
import requests
from requests.packages.urllib3.util import Retry
from requests.adapters import HTTPAdapter

class InvalidAPIKey(Exception):
    def __init__(self, value=None):
        self.value = value or "Invalid API Key"

    def __str__(self):
        return repr(self.value)


class InvalidInputParam(Exception):
    def __init__(self, value=None):
        self.value = value or "Invalid Function Input Parameters"

    def __str__(self):
        return repr(self.value)


class BadRequest(Exception):
    def __init__(self, value=None):
        self.value = value or "Bad Request"

    def __str__(self):
        return repr(self.value)


class RetryError(Exception):
    def __init__(self, value=None):
        self.value = value or "Exceeded maximum number of retries"

    def __str__(self):
        return repr(self.value)


class ApiCallController(object):
    def __init__(self, req_session=None):
        self.request_session = req_session

    @classmethod
    def create_header(cls, api_key):
        header = {
            'X-OTX-API-KEY': api_key,
            'User-Agent': 'OTX Python Neetin Kandhare Integration/1.1',
            'Content-Type': 'application/json'
        }
        return header

    @classmethod
    def format_proxy_data(cls, proxy_data):
        proxies = {'http': proxy_data} if proxy_data else {}
        return proxies

    @classmethod
    def response_handle_errors(cls, response):
        def _response_json():
            try:
                return response.json()
            except Exception as e:
                return {'internal_error': 'Unable to decode response json: {}'.format(e)}

        if response.status_code == 403:
            raise InvalidAPIKey()
        elif response.status_code == 400:
            raise BadRequest(_response_json())
        elif str(response.status_code)[0] != "2":
            raise Exception("Unexpected http code: %r, response=%r", response.status_code, _response_json())

        return response

    @classmethod
    def create_alienvault_indicators_url(cls, base_url, search_value, search_type, search_section):
        _indicator_url = base_url+"/indicators/{}/{}/{}"
        _indicator_full_url = None
        if search_value is not None and search_type is not None and search_section is not None:
            if search_type.find('IP Address') != -1:
                if search_value.find(":") != -1:
                    _indicator_full_url = _indicator_url.format("IPv6", search_value, search_section)
                else:
                    _indicator_full_url = _indicator_url.format("IPv4", search_value, search_section)

            elif search_type.find('DNS Name') != -1:
                _indicator_full_url = _indicator_url.format("domain", search_value, search_section)
            elif search_type.find('System Name') != -1:
                _indicator_full_url = _indicator_url.format("hostname", search_value, search_section)
            elif search_type.find('Hash') != -1:
                _indicator_full_url = _indicator_url.format("file", search_value, search_section)
            elif search_type.find('URL') != -1:
                _indicator_full_url = _indicator_url.format("url", search_value, search_section)
            elif search_type.find('CVE') != -1:
                _indicator_full_url = _indicator_url.format("cve", search_value, search_section)
            else:
                raise InvalidInputParam("Invalid Function Input Type Parameter.")
        else:
            raise InvalidInputParam()

        return _indicator_full_url

    def session(self):
        if self.request_session is None:
            self.request_session = requests.Session()
            # This will allow 5 tries at a url, with an increasing backoff.  Only applies to a specific set of codes
            self.request_session.mount('https://', HTTPAdapter(
                    max_retries=Retry(
                        total=3,
                        status_forcelist=[429, 500, 502, 503],
                        backoff_factor=5,
                    )
            ))
        return self.request_session

