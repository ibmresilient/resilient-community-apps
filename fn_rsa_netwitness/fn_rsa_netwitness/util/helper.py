# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# Copyright © IBM Corporation 2010, 2019

import tempfile
import shutil
import logging
import base64


log = logging.getLogger(__name__)


def create_tmp_file(contents):
    temp_d = tempfile.mkdtemp("tmp")
    temp_f = tempfile.mkstemp(dir=temp_d)
    report_file = temp_f[1]

    with open(report_file, 'wb') as f:
        f.write(contents)
        log.info("Saved ATD report")

    return temp_d, report_file


def remove_dir(dir):
    shutil.rmtree(dir)
    log.debug("Tmp directory removed")


def get_headers(username, password):
    login_string = "{}:{}".format(username, password)
    base64_login = base64.b64encode(str.encode(login_string))

    headers = {
        "Authorization": "Basic {}".format(base64_login),
        "Content-Type": "application/x-www-form-urlencoded",
        "Cache-Control": "no-cache"
    }

    return headers
