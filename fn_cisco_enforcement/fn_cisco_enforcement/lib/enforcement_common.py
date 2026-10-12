# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.

HEADERS = {'content-type': 'application/json'}
SECTION_NAME = "fn_cisco_enforcement"

def callback(response):
    """
    callback needed for main code to handle statuscodes
    :param response:
    :return: json result or None, error_msg
    """
    error_msg = None
    if response.status_code >= 300:
        resp = response.json()
        msg = resp['message']
        if response.status_code == 404:
            error_msg  = u"Cisco Enforcement issue: {}: {}".format(response.status_code, msg)
        else:
            error_msg = u"Cisco Enforcement failure: {}: {}".format(response.status_code, msg)

    try:
        content = response.json()
    except:
        content = ""

    return content, error_msg
