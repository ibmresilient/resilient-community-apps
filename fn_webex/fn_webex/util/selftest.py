# -*- coding: utf-8 -*-

import logging

from fn_webex.lib import constants
from fn_webex.lib.cisco_authentication import WebexAuthentication
from resilient_lib import validate_fields, RequestsCommon


log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    app_configs = opts.get("fn_webex", {})


    validate_fields([{"name" : "webex_site_url", 
                      "name" : "webex_bearerID", 
                      "name" : "webex_timezone"}], app_configs)

    requiredParameters = {}
    requiredParameters["rc"] = RequestsCommon(opts, app_configs)
    requiredParameters["logger"] = log
    requiredParameters["tokenURL"] = app_configs.get("webex_site_url") + constants.TOKEN_URL
    
    try :
        authenticator = WebexAuthentication(requiredParameters, app_configs)
        _ = authenticator.Authenticate()
        return {
            "state": "success",
            "reason": "success"}

    except Exception as err:
        return {
                "state": "failure",
                "reason": err.__str__()}
