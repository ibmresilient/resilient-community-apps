# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

"""AppFunction implementation"""
from resilient_lib import validate_fields, IntegrationError
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult

from fn_teams.lib import constants
from fn_teams.lib.microsoft_teams import TeamsInterface
from fn_teams.lib.microsoft_authentication import  MicrosoftAuthentication

PACKAGE_NAME = constants.PACKAGE_NAME
FN_NAME = "ms_teams_create_team"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'ms_teams_create_team'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)
        self._app_function("")

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        This application allows for creating a Microsoft Group using the Microsoft Graph API. This
        provides SOAR with the ability to create Groups from within a SOAR incident or a task.

        Inputs:
        -------
            task_id                <str> : If called from task then Task ID
            incident_id            <str> : Incident ID
            ms_team_name           <str> : Name of the Microsoft Team to be created
            ms_owners_list         <str> : List of owners email addresses
            add_members_from       <str> : Specifies if members to be added form incident or task
            additional_mambers     <str> : List of email addresses of additional members to be added
            ms_team_description    <str> : Description for the group to be created

        Returns:
        --------
            Response <dict> : A response with the room/team options and details
                              or the error message if the meeting creation
         """

        yield self.status_message(constants.STATUS_STARTING_APP.format(FN_NAME))

        required_parameters = {}
        required_parameters["rc"] = self.rc
        required_parameters["logger"] = self.LOG
        required_parameters["resclient"] = self.rest_client()

        if hasattr(fn_inputs, 'ms_group_id'):
            # Creates a Team using an existing MS Group setting
            required_parameters["group_id"] = fn_inputs.ms_group_id

        else:
            # Creates a Team from scratch
            validate_fields([
                "incident_id",
                "ms_team_name",
                "ms_owners_list",
                "add_members_from"], fn_inputs)

            required_parameters["incident_id"] = fn_inputs.incident_id
            required_parameters["displayName"] = fn_inputs.ms_team_name
            required_parameters["owners_list"] = fn_inputs.ms_owners_list
            required_parameters["add_members_from"] = fn_inputs.add_members_from

            required_parameters["task_id"] = fn_inputs.task_id if hasattr(
                fn_inputs, 'task_id') else None
            required_parameters["description"] = fn_inputs.ms_team_description if hasattr(
                fn_inputs, 'ms_team_description') else ""
            required_parameters["additional_members"] = fn_inputs.additional_members if hasattr(
                fn_inputs, 'additional_members') else None

        try:
            yield self.status_message(constants.STATUS_GENERATE_HEADER)
            authenticator = MicrosoftAuthentication(required_parameters, self.options)
            required_parameters["header"] = authenticator.authenticate()
            authenticated = True
            yield self.status_message(constants.STATUS_SUCCESSFULLY_AUTHENTICATED)

        except IntegrationError as err:
            self.LOG.error(constants.STATUS_SUCCESSFULLY_AUTHENTICATED)
            yield self.status_message(constants.STATUS_AUTHENTICATION_FAILED)
            authenticated = False
            yield FunctionResult({}, success=False, reason=str(err))

        if authenticated:
            team_manager = TeamsInterface(required_parameters)
            if "group_id" in required_parameters:
                response = team_manager.create_team_from_group(required_parameters.get("group_id"))
            else:
                response = team_manager.create_team(required_parameters)
            try:
                yield FunctionResult(response, success=True)
            except IntegrationError as err:
                yield FunctionResult({}, success=False, reason=str(err))
