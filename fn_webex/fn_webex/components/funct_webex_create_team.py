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
FN_NAME = "webex_create_team"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'webex_create_meeting'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)
        self.opts = opts
        self.requiredParameters = {}
        self.config_options = opts.get(PACKAGE_NAME, {})


    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):

        """
        This function creates a Webex team and adds a team to it.

        Args:
        -----
            teamName           (<str>)  : Name of the team to be created
            incidentId         (<str>)  : Incident ID
            addAllMembers      (<bool>) : Adds all members of the incident to the team
            additionalAttendee (<str>)  : Additonal attendees to be added
            entityId           (<str>)  : always >>teamId<<
            entityName         (<str>)  : always >>teamName<<
            entityURL          (<str>)  : Teams API URL
            membershipURL      (<str>)  : Teams Membership API URL
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
        validate_fields(["webex_team_name", "webex_add_all_members", "webex_incident_id"], fn_inputs)

        self.requiredParameters["teamName"] = fn_inputs.webex_team_name
        self.requiredParameters["incidentId"] = fn_inputs.webex_incident_id
        self.requiredParameters["addAllMembers"] = fn_inputs.webex_add_all_members
        self.requiredParameters["additionalAttendee"] = fn_inputs.webex_meeting_attendees if hasattr(fn_inputs, 'webex_meeting_attendees') else None

        self.requiredParameters["rc"] = self.rc
        self.requiredParameters["logger"] = self.LOG
        self.requiredParameters["resclient"] = self.rest_client()

        self.requiredParameters["entityId"]   = "teamId"
        self.requiredParameters["entityName"] = "teamName"
        self.requiredParameters["tokenURL"] = parse.urljoin(self.config_options.get("webex_site_url"), constants.TOKEN_URL)
        self.requiredParameters["entityURL"]  = parse.urljoin(self.config_options.get("webex_site_url"), constants.TEAMS_URL)
        self.requiredParameters["membershipUrl"] = parse.urljoin(self.config_options.get("webex_site_url"), constants.TEAMS_MEMBERSHIP_URL)

        try:
            yield self.status_message(constants.MSG_CREATE_SECURITY)
            self.LOG.info(constants.MSG_CREATE_SECURITY)
            authenticator = WebexAuthentication(self.requiredParameters, self.config_options)
            self.requiredParameters["header"] = authenticator.Authenticate()
            authenticated = True
            yield self.status_message("Successfully Authenticated!")

        except Exception as err:
            self.LOG.error(constants.MSG_FAILED_AUTH)
            yield self.status_message(constants.MSG_FAILED_AUTH)
            reason = str(err)
            authenticated = False

        if authenticated:
            webex = WebexInterface(self.requiredParameters)
            response = webex.create_team_room()
            yield self.status_message("Finished running App Function successfully: '{0}'".format(FN_NAME))
            yield FunctionResult(response, success=True)

        else:
            yield self.status_message("Failed to run App Function : '{0}'".format(FN_NAME))
            yield FunctionResult(None, success=False, reason=reason)
