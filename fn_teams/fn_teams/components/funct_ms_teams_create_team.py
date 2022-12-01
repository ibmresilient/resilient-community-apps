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

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        This application allows for creating a Microsoft Team using the Microsoft Graph API. This
        provides SOAR with the ability to create a MS Team from within a SOAR incident or a task. This
        ms_teams_create_team function has the ability to create an MS Team with a Name and description
        from an Incident or a task. It also has the ability to add multiple owners by specifying
        their email addresses in a comma-separated manner. At least one owner must be mentioned for group
        creation. The function is developed to automatically add all members of an incident or a task
        to the MS Team. If the function is executed from within a task, in addition to task members,
        all incident members can also be automatically added if that option is selected. Apart from
        automatic member addition, individual members can be added by directly specifying their email
        addresses.

        Inputs:
        -------
            task_id             <str> : If called from task then Task ID
            incident_id         <str> : Incident ID
            ms_team_name        <str> : Name of the Microsoft Team to be created
            ms_owners_list      <str> : List of owners email addresses
            add_members_from    <str> : Specifies if members to be added form incident or task
            ms_description      <str> : Description for the group to be created
            additional_members  <str> : List of email addresses of additional members to be added

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
        required_parameters["description"] = fn_inputs.ms_description if hasattr(
            fn_inputs, 'ms_description') else ""
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
            response = team_manager.create_team(required_parameters)
            try:
                yield FunctionResult(response, success=True)
            except IntegrationError as err:
                yield FunctionResult({}, success=False, reason=str(err))
