# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

"""AppFunction implementation"""
from resilient_lib import IntegrationError
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult

from fn_teams.lib import constants
from fn_teams.lib.microsoft_teams import TeamsInterface
from fn_teams.lib.microsoft_authentication import  MicrosoftAuthentication

PACKAGE_NAME = constants.PACKAGE_NAME
FN_NAME = "ms_teams_enable_team"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'ms_teams_enable_team'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        This application allows for creating a Microsoft Group using the Microsoft Graph API. This
        provides SOAR with the ability to create Groups from within a SOAR incident or a task.

        Inputs:
        -------
            ms_group_id            <str> : The unique Id generated while creating a group
            ms_group_mail_nickname <str> : Mail nickname for the group (Must be unique)
            ms_group_name          <str> : Name of the Microsoft Group

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
            try:
                team_manager = TeamsInterface(required_parameters)

                if hasattr(fn_inputs, 'ms_group_id'):
                    response = team_manager.enable_team_group(
                        {"group_id" : fn_inputs.ms_group_id})

                elif hasattr(fn_inputs, 'ms_group_mail_nickname'):
                    response = team_manager.enable_team_group(
                        {"group_mail_nickname" : fn_inputs.ms_group_mail_nickname})

                elif hasattr(fn_inputs, 'ms_group_name'):
                    response = team_manager.enable_team_group(
                        {"group_name" : fn_inputs.ms_group_name})

                else:
                    raise IntegrationError(constants.ERROR_INVALID_OPTION_PASSED)
                yield FunctionResult(response, success=True)

            except IntegrationError as err:
                yield FunctionResult({}, success=False, reason=str(err))
