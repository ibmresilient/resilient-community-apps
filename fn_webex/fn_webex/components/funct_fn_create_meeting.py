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

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))
        validate_fields(["webex_meeting_name", "webex_incident_id", "webex_add_all_members", "webex_meeting_attendee"], fn_inputs)
        validate_fields([{"name" : "webex_site_url", 
                         "name" : "webex_bearerID", 
                         "name" : "webex_timezone"}], self.config_options)

        self.requiredParameters["start"] = fn_inputs.webex_meeting_start_time if hasattr(fn_inputs, 'webex_meeting_start_time') else None
        self.requiredParameters["end"] = fn_inputs.webex_meeting_end_time if hasattr(fn_inputs, 'webex_meeting_end_time') else None
        self.requiredParameters["timezone"] = self.config_options.get("webex_timezone")
        self.requiredParameters["clientID"] = self.config_options.get("client_id")
        self.requiredParameters["clientSecret"] = self.config_options.get("client_secret")
        self.requiredParameters["refreshToken"] = self.config_options.get("refresh_token")
        self.requiredParameters["scope"] = self.config_options.get("scope")
        self.requiredParameters["incidentID"] = fn_inputs.webex_incident_id
        self.requiredParameters["addAllMembers"] = fn_inputs.webex_add_all_members
        self.requiredParameters["additionalAttendee"] = fn_inputs.webex_meeting_attendee

        self.meetingParameters["title"] = fn_inputs.webex_meeting_name
        self.meetingParameters["agenda"] = fn_inputs.webex_meeting_agenda if hasattr(fn_inputs, 'webex_meeting_agenda') else None
        self.meetingParameters["password"] = fn_inputs.webex_meeting_password if hasattr(fn_inputs, 'webex_meeting_password') else None
        self.meetingParameters["sendEmail"] = True

        self.requiredParameters["rc"] = self.rc
        self.requiredParameters["resclient"] = self.rest_client()
        self.requiredParameters["siteURL"]  = SITE_URL
        self.requiredParameters["tokenURL"] = TOKEN_URL

        
        print("\n\n\n\n\n\n",fn_inputs.webex_add_all_members)

        fn_msg = self.get_fn_msg()
        self.LOG.info("fn_msg: %s", fn_msg)

        webex = WebexAPI(self.requiredParameters, self.meetingParameters)
        webex.generate_attendee_list()
        webex.Authenticate()
        webex.createRetrieveRoom()
        # try:
        #     response = webex.create_meeting()
        #     yield self.status_message("Finished running App Function successfully: '{0}'".format(FN_NAME))
        #     yield FunctionResult(value=response, success=True)

        # except Exception as err:
        #     yield self.status_message("Failed to run App Function : '{0}'".format(FN_NAME))
        #     reason = err.__str__()
        #     yield FunctionResult(value=None, success=False, reason=reason)
