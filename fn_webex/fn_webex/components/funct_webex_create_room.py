# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
#
# """AppFunction implementation"""
from urllib import parse
from fn_webex.lib import constants
from fn_webex.lib.cisco_interface import WebexInterface
from fn_webex.lib.cisco_authentication import WebexAuthentication
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields

PACKAGE_NAME = "fn_webex"
FN_NAME = "webex_create_room"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'webex_create_meeting'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)
        self.requiredParameters, self.meetingParameters = {}, {}
        self.opts = opts
        self.config_options = opts.get(PACKAGE_NAME, {})


    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        This function creates a Webex room and adds a team to it.

        Args:
        -----
            roomName           (<str>)  : Name of the room to be created
            teamId             (<str>)  : ID of the team to be added
            incidentId         (<str>)  : Incident ID
            addAllMembers      (<bool>) : Adds all members of the incident to the room
            additionalAttendee (<str>)  : Additonal attendees to be added
            entityId           (<str>)  : always >>roomId<<
            entityName         (<str>)  : always >>roomName<<
            entityURL          (<str>)  : Rooms API URL
            membershipURL      (<str>)  : Rooms Membership API URL
            rc                  (<rc>)  : A resilient wrapper for Requests object
            logger           (<logger>) : A resilient wrapper for logger obhect
            resclient   (<rest_client>) : Rest client to interact with the SOAR instance
 
        Yields:
        -------
            (<FunctionResult>): States if the application was executed successfully or not.
                                Returns the response retrieved from the Webex endpoint in 
                                the form of a dictionary.
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))
        validate_fields(["webex_room_name", "webex_add_all_members", "webex_incident_id"], fn_inputs)
        validate_fields([{"name" : "client_id",
                          "name" : "scope",
                          "name" : "client_secret",
                          "name" : "refresh_token"}], self.config_options)

        self.requiredParameters["roomName"] = fn_inputs.webex_room_name
        self.requiredParameters["teamId"] = fn_inputs.webex_team_id if hasattr(fn_inputs, 'webex_team_id') else None
        self.requiredParameters["incidentId"] = fn_inputs.webex_incident_id
        self.requiredParameters["addAllMembers"] = fn_inputs.webex_add_all_members
        self.requiredParameters["additionalAttendee"] = fn_inputs.webex_meeting_attendees if hasattr(fn_inputs, 'webex_meeting_attendees') else None

        self.requiredParameters["entityId"]   = "roomId"
        self.requiredParameters["entityName"] = "roomName"
        self.requiredParameters["entityURL"]  = parse.urljoin(self.config_options.get("webex_site_url"), constants.ROOMS_URL)
        self.requiredParameters["membershipUrl"] = parse.urljoin(self.config_options.get("webex_site_url"), constants.ROOMS_MEMBERSHIP_URL)

        self.requiredParameters["rc"] = self.rc
        self.requiredParameters["logger"] = self.LOG
        self.requiredParameters["resclient"] = self.rest_client()
        
        fn_msg = self.get_fn_msg()
        self.LOG.info("Webex: %s", fn_msg)

        try:
            yield self.status_message("Authenticating Webex using OAuth Access Token: '{0}'".format(FN_NAME))
            self.LOG.info("Webex: Creating a Security context and establishing a connection with the Webex EndPoint")
            authenticator = WebexAuthentication(self.requiredParameters, self.config_options)
            self.requiredParameters["header"] = authenticator.Authenticate()
            yield self.status_message("Successfully Authenticated!")
            
        except Exception as err:
            self.LOG.error("Failed to create Security Context")
            yield self.status_message("Failed to Authenticate {}! Is the Refresh token Upto date?".format(FN_NAME))
            reason = err.__str__()
            yield FunctionResult(value=None, success=False, reason=reason)

        try:
            webex = WebexInterface(self.requiredParameters)
            webex.generate_member_list()
            webex.createRetrieveEntity()
            yield self.status_message("Successfully created/retrieved a room")
            webex.addMembership()
            yield self.status_message("Successfully added membership to the room")
            response = webex.getEntityDetails()
            yield self.status_message("Finished running App Function successfully: '{0}'".format(FN_NAME))
            yield FunctionResult(response, success=True)

        except Exception as err:
            yield self.status_message("Failed to run App Function : '{0}'".format(FN_NAME))
            yield self.status_message("Does the integration have the appropriate scopes required to perform this action?")
            reason = err.__str__()
            yield FunctionResult(None, success=False, reason=reason)
            
