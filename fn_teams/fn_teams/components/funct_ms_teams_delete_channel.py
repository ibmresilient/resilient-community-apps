# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

"""AppFunction implementation"""
from resilient_lib import IntegrationError, validate_fields
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult

from fn_teams.lib import constants
from fn_teams.lib.microsoft_channels import ChannelInterface
from fn_teams.lib.microsoft_authentication import  MicrosoftAuthentication

PACKAGE_NAME = constants.PACKAGE_NAME
FN_NAME = "ms_teams_delete_channel"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'ms_teams_enable_team'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        This application allows for deleting a MS Channel using the Microsoft Graph API.
        This provides SOAR with the ability to delete an existing MS Channel of a Team.
        A MS Team can have multiple channels, but each MS Group can have only one Team.
        Inorder to delete an MS Channel, its MS Team/Group needs to be identified. To
        locate this team for this operation, one of the following inputs can be used:

            -> ms_groupteam_id
            -> ms_group_mail_nickname
            -> ms_groupteam_name

        Note: If multiple options are provided to locate the Graph Object then
        ms_group_mail_nickname supersedes ms_groupteam_name and ms_groupteam_id supersedes
        the other two options

        Inputs:
        -------
            ms_channel_name        <str> : Name of the channel to be deleted
            ms_groupteam_id        <str> : The unique Id generated while creating a group
            ms_group_mail_nickname <str> : Mail nickname for the group (Must be unique)
            ms_groupteam_name      <str> : Name of the Microsoft Group

        Returns:
        --------
            Response <dict> : A response with the details of the team that was archived or
                              unarchived, or an error message from the MS Graph api if the
                              operation fails
         """

        yield self.status_message(constants.STATUS_STARTING_APP.format(FN_NAME))

        validate_fields([
            "ms_channel_name"], fn_inputs)

        required_parameters, options = {}, {}
        required_parameters["rc"] = self.rc
        required_parameters["logger"] = self.LOG
        required_parameters["resclient"] = self.rest_client()

        options["channel_name"] = fn_inputs.ms_channel_name

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
                team_manager = ChannelInterface(required_parameters)

                if hasattr(fn_inputs, 'ms_groupteam_id'):
                        options.update(
                            {"group_id" : fn_inputs.ms_groupteam_id})

                elif hasattr(fn_inputs, 'ms_group_mail_nickname'):
                        options.update(
                            {"group_mail_nickname" : fn_inputs.ms_group_mail_nickname})

                elif hasattr(fn_inputs, 'ms_groupteam_name'):
                        options.update(
                            {"group_name" : fn_inputs.ms_groupteam_name})
                else:
                    raise IntegrationError(constants.ERROR_INVALID_OPTION_PASSED)

                response = team_manager.delete_channel(options)
                yield FunctionResult(response, success=True)

            except IntegrationError as err:
                yield FunctionResult({}, success=False, reason=str(err))
