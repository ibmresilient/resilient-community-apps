# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""
import datetime
import logging
from resilient_lib import validate_fields, RequestsCommon
from fn_create_webex_meeting.lib.cisco_api import WebexAPI

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())

PACKAGE_NAME = "fn_create_webex_meeting"

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    options = opts.get(PACKAGE_NAME, {})
    required_fields = ["webex_email", "webex_password", "webex_site_url", "webex_timezone"]
    validate_fields(required_fields, options)

    opts = dict()
    opts["rc"] = RequestsCommon(opts, options)
    opts["webex_site_url"] = options.get("webex_site_url")
    opts["email"] = options.get("webex_email")
    opts["password"] = options.get("webex_password")
    opts["sitename"] = options.get("webex_site")
    opts["timezone"] = options.get("webex_timezone")
    opts["meeting_password"] = "Selftest23#"
    opts["meeting_name"] = "SelfTest Meeting"
    opts["meeting_agenda"] = "Agenda"

    # compute meeting start/end time for 1 day in the future (in epoch)
    now = datetime.datetime.utcnow()
    meeting_start = now + datetime.timedelta(days=1)
    meeting_end = meeting_start + datetime.timedelta(minutes= 10)
    webex_meeting_start_time = int(meeting_start.timestamp()*1000)
    webex_meeting_end_time = int(meeting_end.timestamp()*1000)

    try:
        webex = WebexAPI(opts, webex_meeting_start_time, webex_meeting_end_time)

        response = webex.create_meeting()

        if response.get("status") == "SUCCESS":
            return {"state": "success",
                    "reason": "success"}
        else:
            return {"state": "failure",
                    "reason": response.get("fail_reason")}
    except Exception as err:
        return {"state": "failure",
                "reason": err}