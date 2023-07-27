# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.

"""AppFunction implementation"""
from resilient_lib import IntegrationError, validate_fields
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult

from fn_teams.lib import constants
from fn_teams.lib.microsoft_teams import TeamsInterface
from fn_teams.lib.microsoft_authentication import  MicrosoftAuthentication

PACKAGE_NAME = constants.PACKAGE_NAME
FN_NAME = "ms_teams_archive_team"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'ms_teams_delete_group'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        This application allows for archiving or unarchivig a Microsoft Team using the
        Microsoft Graph API. This provides SOAR with the ability to archive an existing
        MS Team or unarchive a previously archived MS Team within a SOAR incident or a 
        task. "archive_operation" specifies if the team is to be archived or unarchived.
        To locate this team for the archival/unarchival operation, one of the following
        inputs can be used:

            -> ms_groupteam_id
            -> ms_group_mail_nickname
            -> ms_groupteam_name

        Note: If multiple options are provided to locate the Graph Object then
        ms_group_mail_nickname supersedes ms_groupteam_name and ms_groupteam_id supersedes
        the other two options

        Inputs:
        -------
            archive_operation      <str> : Option that specifies the operation to be performed
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
        validate_fields(["archive_operation"], fn_inputs)

        required_parameters = {}
        required_parameters["rc"] = self.rc
        required_parameters["logger"] = self.LOG
        required_parameters["resclient"] = self.rest_client()

        try:
            yield self.status_message(constants.STATUS_GENERATE_HEADER)
            authenticator = MicrosoftAuthentication(self.rc, self.options)
            required_parameters["header"] = authenticator.authenticate_application_permissions()
            authenticated = True
            yield self.status_message(constants.STATUS_SUCCESSFULLY_AUTHENTICATED)

        except IntegrationError as err:
            self.LOG.error(constants.STATUS_SUCCESSFULLY_AUTHENTICATED)
            yield self.status_message(constants.STATUS_AUTHENTICATION_FAILED)
            authenticated = False
            yield FunctionResult({}, success=False, reason=str(err))

        if authenticated:
            team_manager = TeamsInterface(required_parameters)

            if getattr(fn_inputs, 'ms_groupteam_id', ""):
                response = team_manager.archive_unarchive_team(
                    {"group_id"  : fn_inputs.ms_groupteam_id,
                     "operation" : fn_inputs.archive_operation})

            elif getattr(fn_inputs, 'ms_group_mail_nickname', ""):
                response = team_manager.archive_unarchive_team(
                    {"group_mail_nickname" : fn_inputs.ms_group_mail_nickname,
                     "operation" : fn_inputs.archive_operation})

            elif getattr(fn_inputs, 'ms_groupteam_name', ""):
                response = team_manager.archive_unarchive_team(
                    {"group_name" : fn_inputs.ms_groupteam_name,
                     "operation"  : fn_inputs.archive_operation})

            else:
                raise IntegrationError(constants.ERROR_INVALID_OPTION_PASSED)
            try:
                yield FunctionResult(response, success=True)
            except IntegrationError as err:
                yield FunctionResult({}, success=False, reason=str(err))
