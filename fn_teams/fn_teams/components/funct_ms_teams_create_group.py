# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

"""AppFunction implementation"""
from resilient_lib import validate_fields, IntegrationError
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult

from fn_teams.lib import constants
from fn_teams.lib.microsoft_groups import GroupsInterface
from fn_teams.lib.microsoft_authentication import  MicrosoftAuthentication

PACKAGE_NAME = constants.FN_NAME
FN_NAME = "ms_teams_create_group"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'webex_delete_teamsrooms'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)
        self.required_parameters = {}


    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        This application allows for creating a Microsoft Group using the Microsoft Graph API. This
        provides SOAR with the ability to create Groups from within a SOAR incident or a task.

        Inputs:
        -------
            task_id                <str> : If called from task then Task ID
            incident_id            <str> : Incident ID
            ms_group_name          <str> : Name of the Microsoft Group to be created
            ms_owners_list         <str> : List of owners email addresses
            add_members_from       <str> : Specifies if members to be added form incident or task
            additional_mambers     <str> : List of email addresses of additional members to be added
            ms_group_description   <str> : Description for the group to be created
            ms_group_mail_nickname <str> : Mail nickname for the group (Must be unique)

        Returns:
        --------
            Response <dict> : A response with the room/team options and details
                              or the error message if the meeting creation
         """

        yield self.status_message(constants.STATUS_STARTING_APP.format(FN_NAME))

        validate_fields([
            "incident_id",
            "ms_group_name",
            "add_members_from",
            "ms_group_description",
            "ms_group_mail_nickname"], fn_inputs)

        self.required_parameters["rc"] = self.rc
        self.required_parameters["logger"] = self.LOG
        self.required_parameters["resclient"] = self.rest_client()

        self.required_parameters["incident_id"] = fn_inputs.incident_id
        self.required_parameters["group_name"] = fn_inputs.ms_group_name
        self.required_parameters["add_members_from"] = fn_inputs.add_members_from
        self.required_parameters["group_description"] = fn_inputs.ms_group_description
        self.required_parameters["group_mail_nickname"] = fn_inputs.ms_group_mail_nickname

        self.required_parameters["task_id"] = fn_inputs.task_id if hasattr(
            fn_inputs, 'task_id') else None
        self.required_parameters["owners_list"] = fn_inputs.ms_owners_list if hasattr(
            fn_inputs, 'ms_owners_list') else None
        self.required_parameters["additional_members"] = fn_inputs.additional_members if hasattr(
            fn_inputs, 'additional_members') else None

        try:
            yield self.status_message(constants.STATUS_GENERATE_HEADER)
            authenticator = MicrosoftAuthentication(self.required_parameters, self.options)
            self.required_parameters["header"] = authenticator.authenticate()
            authenticated = True
            yield self.status_message(constants.STATUS_SUCCESSFULLY_AUTHENTICATED)

        except IntegrationError as err:
            self.LOG.error(constants.STATUS_SUCCESSFULLY_AUTHENTICATED)
            yield self.status_message(constants.STATUS_AUTHENTICATION_FAILED)
            authenticated = False
            yield FunctionResult({}, success=False, reason=str(err))

        if authenticated:
            try:
                group_manager = GroupsInterface(self.required_parameters)
                response = group_manager.create_group()
                yield FunctionResult(response, success=True)
            except IntegrationError as err:
                yield FunctionResult({}, success=False, reason=str(err))
