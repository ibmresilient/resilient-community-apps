# -*- coding: utf-8 -*-

import logging
import datetime

from fn_webex.lib.cisco_api import WebexAPI
from resilient_lib import validate_fields, RequestsCommon


log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    app_configs = opts.get("fn_webex", {})


    validate_fields([{"name" : "webex_site_url", 
                        "name" : "webex_bearerID", 
                        "name" : "webex_timezone"}], app_configs)

    requiredParameters, meetingParameters = {}, {}
    
    requiredParameters["start"] = round((datetime.datetime.now() + datetime.timedelta(minutes=10)).timestamp()) * 1000
    requiredParameters["end"] =  round((datetime.datetime.now() + datetime.timedelta(minutes=40)).timestamp()) * 1000
    requiredParameters["url"] = app_configs.get("webex_site_url")
    requiredParameters["bearerID"] = app_configs.get("webex_bearerid")
    requiredParameters["rc"] = RequestsCommon(opts, app_configs)
    requiredParameters["timezone"] = app_configs.get("webex_timezone", None)

    meetingParameters["siteURL"] = app_configs.get("webex_siteurl", "")
    meetingParameters["hostEmail"] = app_configs.get("hostEmail", "")
    meetingParameters["title"] = "Selftest Meeting"
    meetingParameters["agenda"] = ""
    meetingParameters["password"] = "Selftest123#"
    meetingParameters["sendEmail"] = True
    
    try :
        webex = WebexAPI(requiredParameters, meetingParameters)
        response = webex.create_meeting()
        return {
            "state": "success",
            "reason": "success"
        }
    except Exception as err:
        return {
                "state": "failure",
                "reason": err
            }
