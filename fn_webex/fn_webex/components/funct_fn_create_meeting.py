# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
#
# """AppFunction implementation"""
from re import S
from fn_webex.lib.cisco_api import WebexAPI
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import IntegrationError, validate_fields, RequestsCommon, ResultPayload

PACKAGE_NAME = "fn_webex"
FN_NAME = "fn_create_meeting"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'fn_create_meeting'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)
        self.requiredParameters, self.meetingParameters = {}, {}
        self.opts = opts
        self.config_options = opts.get(PACKAGE_NAME, {})


    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))
        validate_fields(["webex_meeting_start_time", "webex_meeting_end_time"], fn_inputs)
        validate_fields([{"name" : "webex_site_url", 
                         "name" : "webex_bearerID", 
                         "name" : "webex_timezone"}], self.config_options)

        self.requiredParameters["start"] = fn_inputs.webex_meeting_start_time
        self.requiredParameters["end"] = fn_inputs.webex_meeting_end_time
        self.requiredParameters["timezone"] = self.config_options.get("webex_timezone")
        self.requiredParameters["clientID"] = self.config_options.get("client_id")
        self.requiredParameters["clientSecret"] = self.config_options.get("client_secret")
        self.requiredParameters["refreshToken"] = self.config_options.get("refresh_token")
        self.requiredParameters["scope"] = self.config_options.get("scope")

        self.meetingParameters["title"] = fn_inputs.webex_meeting_name
        self.meetingParameters["agenda"] = fn_inputs.webex_meeting_agenda
        self.meetingParameters["password"] = fn_inputs.webex_meeting_password
        self.meetingParameters["sendEmail"] = True

        self.requiredParameters["rc"] = self.rc
        self.requiredParameters["siteURL"]  = "https://webexapis.com/v1/meetings/"
        self.requiredParameters["tokenURL"] = "https://webexapis.com/v1/access_token"

        fn_msg = self.get_fn_msg()
        self.LOG.info("fn_msg: %s", fn_msg)

        webex = WebexAPI(self.requiredParameters, self.meetingParameters)
        webex.Authenticate()
        response = webex.create_meeting()
        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        yield FunctionResult(response)
