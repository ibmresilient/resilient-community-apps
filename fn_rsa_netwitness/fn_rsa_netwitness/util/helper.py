# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# Copyright © IBM Corporation 2010, 2019

"""Helper functions for Resilient circuits Functions supporting NetWitness integration"""

import logging
import base64
import datetime


log = logging.getLogger(__name__)

def get_headers(username, password):
    """Formats the header to contain username and password variables """
    login_string = "{}:{}".format(username, password)

    # Python 2.7 and 3.6 support
    base64_login = base64.b64encode(str.encode(login_string))
    str_base64_login = base64_login.decode("utf-8")

    return {
        "Authorization": "Basic {}".format(str_base64_login),
        "Content-Type": "application/x-www-form-urlencoded",
        "Cache-Control": "no-cache"
    }

def convert_to_nw_time(resilient_time):
    """Converts Resilient epoch time to time format for NetWitness server"""
    time = resilient_time/1000

    return datetime.datetime.fromtimestamp(time).strftime('%Y-%b-%d %H:%M:%S')
