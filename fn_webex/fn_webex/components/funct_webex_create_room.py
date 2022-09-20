# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
#
# """AppFunction implementation"""
from urllib import parse
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields, IntegrationError

from fn_webex.lib import constants
from fn_webex.lib.cisco_authentication import WebexAuthentication
from fn_webex.lib.cisco_interface import WebexInterface


PACKAGE_NAME = "fn_webex"
FN_NAME = "webex_create_room"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'webex_create_meeting'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)
        self.opts = opts
        self.required_parameters = {}
        self.config_options = opts.get(PACKAGE_NAME, {})


    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        This function creates a Webex room and adds a team to it.

        Fn Inputs:
        ----------
            roomName           (<str>)  : Name of the room to be created
            teamId             (<str>)  : ID of the team to be added
            incidentId         (<str>)  : Incident ID
            addAllMembers      (<bool>) : Adds all members of the incident to the room
            additionalAttendee (<str>)  : Additonal attendees to be added

        Self Objects:
        -------------
            rc                  (<rc>)  : A resilient wrapper for Requests object
            logger           (<logger>) : A resilient wrapper for logger obhect
            resclient   (<rest_client>) : Rest client to interact with the SOAR instance

        Constants:
        ----------
            entityName         (<str>)  : Room Name
            entityURL          (<str>)  : Rooms API URL
            membershipURL      (<str>)  : Rooms Membership API URL

        Yields:
        -------
            (<FunctionResult>): States if the application was executed successfully or not.
                                Returns the response retrieved from the Webex endpoint in
                                the form of a dictionary.
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))
        validate_fields(["webex_room_name", "webex_add_all_members", "webex_incident_id"], fn_inputs)
        validate_fields(["webex_site_url", "webex_timezone", "client_id",
                        "client_secret", "refresh_token", "scope"], self.config_options)

        self.required_parameters["taskId"] = fn_inputs.webex_task_id if hasattr(fn_inputs, 'webex_task_id') else None
        self.required_parameters["teamId"] = fn_inputs.webex_team_id if hasattr(fn_inputs, 'webex_team_id') else None
        self.required_parameters["incidentId"] = fn_inputs.webex_incident_id
        self.required_parameters["addAllMembers"] = fn_inputs.webex_add_all_members
        self.required_parameters["additionalAttendee"] = fn_inputs.webex_meeting_attendees if hasattr(fn_inputs, 'webex_meeting_attendees') else None

        self.required_parameters["entityName"] = fn_inputs.webex_room_name
        self.required_parameters["entityType"] = constants.ROOM
        self.required_parameters["entityURL" ] = parse.urljoin(self.config_options.get("webex_site_url"),constants.ROOMS_URL)
        self.required_parameters["membershipUrl"] = parse.urljoin(self.config_options.get("webex_site_url"),constants.ROOMS_MEMBERSHIP_URL)

        self.required_parameters["rc"] = self.rc
        self.required_parameters["logger"] = self.LOG
        self.required_parameters["resclient"] = self.rest_client()

        fn_msg = self.get_fn_msg()
        self.LOG.info("Webex: %s", fn_msg)

        try:
            yield self.status_message(constants.MSG_CREATE_SECURITY)
            self.LOG.info(constants.MSG_CREATE_SECURITY)
            authenticator = WebexAuthentication(self.required_parameters, self.config_options)
            self.required_parameters["header"] = authenticator.authenticate()
            authenticated = True
            self.LOG.info(constants.MSG_SUCCESS_AUTHENTICATED)
            yield self.status_message(constants.MSG_SUCCESS_AUTHENTICATED)

        except IntegrationError as err:
            self.LOG.error(constants.MSG_FAILED_AUTH)
            yield self.status_message(constants.MSG_FAILED_AUTH)
            authenticated = False
            yield self.status_message("Failed to run App Function : '{0}'".format(FN_NAME))
            yield FunctionResult(None, success=False, reason=str(err))

        if authenticated:
            webex = WebexInterface(self.required_parameters)
            yield webex.create_team_room()
            yield self.status_message(constants.MSG_SUCCESS_EXECUTION.format(FN_NAME))
