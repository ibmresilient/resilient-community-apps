# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
#
# """AppFunction implementation"""
from fn_webex.lib import constants
from fn_webex.lib.cisco_meetings import WebexMeetings
from fn_webex.lib.cisco_authentication import WebexAuthentication

from resilient_lib import validate_fields
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult

PACKAGE_NAME = "fn_webex"
FN_NAME = "webex_create_meeting"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'webex_create_meeting'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)
        self.opts = opts
        self.requiredParameters, self.meetingParameters = {}, {}
        self.config_options = opts.get(PACKAGE_NAME, {})


    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))
        validate_fields(["webex_meeting_name"], fn_inputs)
        validate_fields([{"name" : "webex_site_url",
                          "name" : "webex_timezone"}], self.config_options)

        self.requiredParameters["start"] = fn_inputs.webex_meeting_start_time if hasattr(fn_inputs, 'webex_meeting_start_time') else None
        self.requiredParameters["end"] = fn_inputs.webex_meeting_end_time if hasattr(fn_inputs, 'webex_meeting_end_time') else None
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
        self.requiredParameters["resclient"] = self.rest_client()
        self.requiredParameters["meetingsURL"]  = self.config_options.get("webex_site_url") + constants.MEETINGS_URL
        self.requiredParameters["tokenURL"] = self.config_options.get("webex_site_url") + constants.TOKEN_URL
        self.requiredParameters["logger"] = self.LOG

        fn_msg = self.get_fn_msg()
        self.LOG.info("Webex: %s", fn_msg)

        try:
            yield self.status_message("Authenticating Webex using OAuth Access Token: '{0}'".format(FN_NAME))
            self.LOG.info("Webex: Creating a Security context and establishing a connection with the Webex EndPoint")
            authenticator = WebexAuthentication(self.requiredParameters)
            self.requiredParameters["header"] = authenticator.Authenticate()
            yield self.status_message("Successfully Authenticated!")

        except Exception as err:
            self.LOG.error("Failed to create Security Context")
            yield self.status_message("Failed to Authenticate {}! Is the Refresh token Upto date?".format(FN_NAME))
            reason = err.__str__()
            yield FunctionResult(value=None, success=False, reason=reason)

        try:
            webex = WebexMeetings(self.requiredParameters, self.meetingParameters)
            response = webex.create_meeting()
            yield self.status_message("Successfully created a meeting")
            yield self.status_message("Finished running App Function successfully: '{0}'".format(FN_NAME))
            yield FunctionResult(value=response, success=True)

        except Exception as err:
            yield self.status_message("Failed to run App Function : '{0}'".format(FN_NAME))
            yield self.status_message("Does the integration have the appropriate scopes required to perform this action?")
            reason = err.__str__()
            yield FunctionResult(value=None, success=False, reason=reason)
