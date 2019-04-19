# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# -*- coding: utf-8 -*-

import requests
from requests.packages.urllib3.util import Retry
from requests.adapters import HTTPAdapter
import calendar
from dateutil import parser

TOTAL_RETRIES = 3
BACK_OFF_FACTOR = 5


class phish_tank_helper(object):
    def __init__(self, req_session=None):
        self.request_session = req_session

    @staticmethod
    def create_post_data(url, api_key=None):
        """
        :param url : a url needs to checked for phishing status
        :param api_key:  PhishTank API Key
        :return:  REST API Get Call Header
        """

        post_data = {
            'url': url,
            'format': 'json'
        }

        # if api key is given then adding it to post data dictionary.
        if api_key:
            post_data['app_key'] = api_key
        return post_data

    @staticmethod
    def format_proxy_data(proxy_data):
        """
        :param proxy_data: Proxy Server Address, None if no proxy is defined.
        :return: Dictionary Containing http and https proxy settings
        """
        proxies = {'http': proxy_data, 'https': proxy_data, } if proxy_data not in ['None', 'none'] else {}
        return proxies

    @staticmethod
    def timestamp_to_ms_epoch(str_timestamp):
        """Converts a String Timestamp to an int in milliseconds since 1970 epoch, a format that
        Resilient DateTime field type accepts"""
        epoch = int(calendar.timegm(parser.parse(str_timestamp).timetuple()) * 1000.0)
        return epoch

    def session(self):
        """
        :return: Request Session object with maximum 3 retries and 5 as back off factor.
        """
        if self.request_session is None:
            self.request_session = requests.Session()
            # This will allow 5 tries at a url, with an increasing backoff.  Only applies to a specific set of codes
            self.request_session.mount('https://', HTTPAdapter(
                max_retries=Retry(
                    total=TOTAL_RETRIES,
                    status_forcelist=[429, 500, 502, 503],
                    backoff_factor=BACK_OFF_FACTOR,
                )
            ))
        return self.request_session
