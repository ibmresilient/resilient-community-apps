# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# Copyright © IBM Corporation 2010, 2019

import logging
import base64
import datetime
import sys
if sys.version_info.major < 3:
    from StringIO import StringIO
    from io import BytesIO
else:
    from io import StringIO, BytesIO


log = logging.getLogger(__name__)


def create_tmp_file(contents):
    if isinstance(contents, bytes):
        return BytesIO(contents)

    return StringIO(contents)

def get_headers(username, password):
    login_string = "{}:{}".format(username, password)

    # Python 2.7 and 3.6 support
    base64_login = base64.b64encode(str.encode(login_string))
    str_base64_login = base64_login.decode("utf-8")

    headers = {
        "Authorization": "Basic {}".format(str_base64_login),
        "Content-Type": "application/x-www-form-urlencoded",
        "Cache-Control": "no-cache"
    }

    return headers


# Converts Resilient epoch time to time format for NetWitness server
def convert_to_nw_time(resilient_time):
    time = resilient_time/1000

    return datetime.datetime.fromtimestamp(time).strftime('%Y-%b-%d %H:%M:%S')
