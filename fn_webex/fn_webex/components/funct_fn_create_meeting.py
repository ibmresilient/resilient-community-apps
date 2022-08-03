# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
#
# """AppFunction implementation"""

from fn_webex.lib.cisco_api import WebexAPI
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields

PACKAGE_NAME = "fn_webex"
FN_NAME = "fn_create_meeting"
SITE_URL = "https://webexapis.com/v1/meetings/"
TOKEN_URL = "https://webexapis.com/v1/access_token"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'fn_create_meeting'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)
        self.requiredParameters, self.meetingParameters = {}, {}
        self.opts = opts
        self.config_options = opts.get(PACKAGE_NAME, {})


    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):

        resclient = self.rest_client()
        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))
        validate_fields(["webex_meeting_start_time", "webex_meeting_end_time", 
                         "webex_meeting_name"], fn_inputs)
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
        self.meetingParameters["agenda"] = fn_inputs.webex_meeting_agenda if hasattr(fn_inputs, 'webex_meeting_agenda') else None
        self.meetingParameters["password"] = fn_inputs.webex_meeting_password if hasattr(fn_inputs, 'webex_meeting_password') else None
        self.meetingParameters["sendEmail"] = True

        self.requiredParameters["rc"] = self.rc
        self.requiredParameters["siteURL"]  = SITE_URL
        self.requiredParameters["tokenURL"] = TOKEN_URL

        print("\n\n\n\n")
        print(fn_inputs.webex_add_all_members)
        print(fn_inputs.webex_meeting_attendee)

        fn_msg = self.get_fn_msg()
        self.LOG.info("fn_msg: %s", fn_msg)

        try:
            webex = WebexAPI(self.requiredParameters, self.meetingParameters)
            webex.Authenticate()
            response = webex.create_meeting()
            yield self.status_message("Finished running App Function successfully: '{0}'".format(FN_NAME))
            yield FunctionResult(value=response, success=True)

        except Exception as err:
            yield self.status_message("Failed to run App Function : '{0}'".format(FN_NAME))
            yield FunctionResult(value=response, success=False, reason=err)
            
