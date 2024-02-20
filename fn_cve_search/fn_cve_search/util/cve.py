# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
""" A common library functions for CVE"""
import time
import calendar
from resilient_lib import RequestsCommon


def get_gm_epoch_time_stamp(date_string):
    """
    :param date_string:  date string like 2018-09-11
    :return: time stamp in milli seconds

    """
    string_format_date = date_string.split('T')[0]
    time_tuple = time.strptime(string_format_date, "%Y-%m-%d")
    time_miliseconds = calendar.timegm(time_tuple) * 1000
    return time_miliseconds


def make_rest_api_get_call(rest_url, app_config_ops, app_config_cve_search, api_call=None):
    """
    :param rest_url: Rest Api URL
    :param api_call: Just reference
    :return: JSON Object Returned from the Call
    """
    response_json_object = dict()
    try:
        rc = RequestsCommon(app_config_ops, app_config_cve_search)
        response = rc.execute_call_v2("GET", rest_url)

        response_json_object['content'] = response.json()
        response_json_object['api_call'] = api_call
        return response_json_object

    except Exception as call_err:
        raise ValueError("CVE API Call Failed : {}".format(call_err))
