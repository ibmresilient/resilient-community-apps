# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# Copyright © IBM Corporation 2010, 2019

import tempfile
import shutil
import logging
import base64
import datetime


log = logging.getLogger(__name__)


def create_tmp_file(contents):
    temp_d = tempfile.mkdtemp("tmp")
    temp_f = tempfile.mkstemp(dir=temp_d)
    report_file = temp_f[1]

    with open(report_file, 'wb') as f:
        f.write(contents)
        log.info("Saved PCAP data locally.")

    return temp_d, report_file


def remove_dir(dir):
    shutil.rmtree(dir)
    log.debug("Tmp directory removed")


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
