# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

"""AppFunction implementation"""
from resilient_lib import IntegrationError
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult

from fn_teams.lib import constants
from fn_teams.lib.microsoft_groups import GroupsInterface
from fn_teams.lib.microsoft_authentication import  MicrosoftAuthentication

PACKAGE_NAME = constants.PACKAGE_NAME
FN_NAME = "ms_teams_delete_group"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'ms_teams_delete_group'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)
        self.required_parameters = {}


    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        This application allows for deleting a Microsoft Group using the Microsoft Graph API. This
        provides SOAR with the ability to delete Groups from within a SOAR incident or a task.
        ms_group_mail_nickname is a unique value and so using this attribute to delete a group
        is highly recommended. If the ms_group_name attribute is used for deletion, there could
        exist two groups with the same name, in that case, the program would return an error.

        Inputs:
        -------
            ms_group_name          <str> : Name of the Microsoft Group to be deleted
            ms_group_mail_nickname <str> : Mail nickname for the group (Must be unique)

        Returns:
        --------
            Response <dict> : A response with the room/team options and details
                              or the error message if the meeting creation
        """

        yield self.status_message(constants.STATUS_STARTING_APP.format(FN_NAME))

        self.required_parameters["rc"] = self.rc
        self.required_parameters["logger"] = self.LOG
        self.required_parameters["resclient"] = self.rest_client()

        self.required_parameters["group_name"] = fn_inputs.ms_group_name if hasattr(
            fn_inputs, 'ms_group_name') else None
        self.required_parameters["group_mail_nickname"] = fn_inputs.ms_group_mail_nickname if hasattr(
            fn_inputs, 'ms_group_mail_nickname') else None

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
                response = group_manager.delete_group()
                yield FunctionResult(response, success=True)
            except IntegrationError as err:
                yield FunctionResult({}, success=False, reason=str(err))
