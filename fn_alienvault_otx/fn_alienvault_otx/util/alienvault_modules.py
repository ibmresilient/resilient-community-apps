# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
# -*- coding: utf-8 -*-
""" Alien Vault OTX module to Access OTX threat Intelligence Data"""
import json
import re
import datetime
import requests
from requests.packages.urllib3.util import Retry
from requests.adapters import HTTPAdapter

"""
class InvalidAPIKey(Exception):
    def __init__(self, value=None):
        self.value = value or "Invalid API Key"

    def __str__(self):
        return repr(self.value)
"""

class InvalidInputParam(Exception):
    def __init__(self, value=None):
        self.value = value or "Invalid Function Input Parameters"

    def __str__(self):
        return repr(self.value)

"""
class BadRequest(Exception):
    def __init__(self, value=None):
        self.value = value or "Bad Request"

    def __str__(self):
        return repr(self.value)
"""

class RetryError(Exception):
    def __init__(self, value=None):
        self.value = value or "Exceeded maximum number of retries"

    def __str__(self):
        return repr(self.value)


class ApiCallController(object):
    def __init__(self, req_session=None):
        self.request_session = req_session

    @staticmethod
    def create_header(api_key):
        """

        :param api_key:
        :return:
        """
        header = {
            'X-OTX-API-KEY': api_key,
            'User-Agent': 'Resilient Integration Server/1.1',
            'Content-Type': 'application/json'
        }
        return header

    @staticmethod
    def format_proxy_data(proxy_data):
        """

        :param proxy_data:
        :return:
        """
        proxies = {'http': proxy_data, 'https': proxy_data,} if proxy_data not in ['None', 'none'] else {}
        print("Proxies", proxies)
        return proxies

    @classmethod
    def create_alienvault_indicators_url(cls, base_url, search_value, search_type, search_section):
        """

        :param base_url:
        :param search_value:
        :param search_type:
        :param search_section:
        :return:
        """
        _indicator_url = base_url + "/indicators/{}/{}/{}"
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

    @staticmethod
    def timestamp_to_ms_epoch(str_timestamp, timestamp_format="%Y-%m-%dT%H:%M:%S"):
        """Converts a String Timestamp to an int in milliseconds since 1970 epoch, a format that
        Resilient DateTime field type accepts"""

        epoch = datetime.datetime(1970, 1, 1)
        utc_time = datetime.datetime.strptime(str_timestamp, timestamp_format)
        return int((utc_time - epoch).total_seconds() * 1000.0)

    @staticmethod
    def convert_date_string_to_ms_epoch(response_data=""):
        """
        :param response_data: String Formatted API response data
        :return:  String Formatted API response data with converted all date strings to milli seconds epoch format.
        """
        date_time_list = re.findall(r'"\d+-\d+-\d+T\d+:\d+:\d+\.\d*"|"\d+-\d+-\d+T\d+:\d+:\d*"|"\d+-\d+-\d+"',
                                    response_data, re.IGNORECASE)
        date_string_epoch_dict = dict()
        for tmp_found_date_string in date_time_list:
            print("DATE IS GETTING CONVERTING : {}".format(tmp_found_date_string))
            found_date_string = tmp_found_date_string
            if tmp_found_date_string.find('T') == -1:
                tmp_found_date_string = re.sub('"', '', tmp_found_date_string)
                tmp_found_date_string = '"{}T00:00:00"'.format(tmp_found_date_string)

            # removing milli seconds from string date found
            date_time = re.sub(r'\.\d*', '', tmp_found_date_string, re.DOTALL)
            date_time = re.sub(r'"', '', date_time)

            # Converting string date to milli second epoch
            millisec_epoch = ApiCallController.timestamp_to_ms_epoch(str(date_time))

            # create a dict with string date as key and ms epoch as value
            date_string_epoch_dict[found_date_string] = millisec_epoch

        for date_string, epoch_value in date_string_epoch_dict.items():
            print("DATE STRING : {} AND EPOCH TIME STAMP : {}".format(date_string, epoch_value))
            response_data = re.sub(date_string, str(epoch_value), response_data)
        print(" FINAL RESPONSE OUT : {}".format(response_data))
        return response_data
    """
    def response_handle_errors(self, response):
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
    """

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

