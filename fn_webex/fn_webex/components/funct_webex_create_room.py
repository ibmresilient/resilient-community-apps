# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
#
# """AppFunction implementation"""

from fn_webex.lib.cisco_rooms import WebexRooms
from fn_webex.lib.cisco_authentication import WebexAuthentication
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields

PACKAGE_NAME = "fn_webex"
FN_NAME = "webex_create_room"
SITE_URL = "https://webexapis.com/v1/meetings/"
TOKEN_URL = "https://webexapis.com/v1/access_token"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'webex_create_meeting'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)
        self.requiredParameters, self.meetingParameters = {}, {}
        self.opts = opts
        self.config_options = opts.get(PACKAGE_NAME, {})


    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))
        validate_fields(["webex_room_name", "webex_add_all_members", "webex_incident_id"], fn_inputs)
        validate_fields([{"name" : "client_id",
                          "name" : "scope",
                          "name" : "client_secret",
                          "name" : "refresh_token"}], self.config_options)

        self.requiredParameters["clientID"] = self.config_options.get("client_id")
        self.requiredParameters["clientSecret"] = self.config_options.get("client_secret")
        self.requiredParameters["refreshToken"] = self.config_options.get("refresh_token")
        self.requiredParameters["scope"] = self.config_options.get("scope")
        self.requiredParameters["addAllMembers"] = fn_inputs.webex_add_all_members
        self.requiredParameters["additionalAttendee"] = fn_inputs.webex_meeting_attendees if hasattr(fn_inputs, 'webex_meeting_attendees') else None
        self.requiredParameters["teamID"] = fn_inputs.webex_team_id if hasattr(fn_inputs, 'webex_team_id') else None
        self.requiredParameters["roomName"] = fn_inputs.webex_room_name
        self.requiredParameters["incidentID"] = fn_inputs.webex_incident_id

        self.requiredParameters["rc"] = self.rc
        self.requiredParameters["logger"] = self.LOG
        self.requiredParameters["resclient"] = self.rest_client()
        self.requiredParameters["siteURL"]  = SITE_URL
        self.requiredParameters["tokenURL"] = TOKEN_URL

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
            webex = WebexRooms(self.requiredParameters)
            webex.generate_member_list()
            webex.createRetrieveRoom()
            yield self.status_message("Successfully created/retrieved a room")
            webex.addMembership()
            yield self.status_message("Successfully added membership to the room")
            response = webex.getRoomDetails()
            yield self.status_message("Finished running App Function successfully: '{0}'".format(FN_NAME))
            yield FunctionResult(response, success=True)

        except Exception as err:
            yield self.status_message("Failed to run App Function : '{0}'".format(FN_NAME))
            yield self.status_message("Does the integration have the appropriate scopes required to perform this action?")
            reason = err.__str__()
            yield FunctionResult(None, success=False, reason=reason)
            
