# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

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
        self.required_parameters = {}


    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):

        yield self.status_message(constants.STATUS_STARTING_APP.format(FN_NAME))
        validate_fields(["archive_operation"], fn_inputs)

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
            team_manager = TeamsInterface(required_parameters)

            if hasattr(fn_inputs, 'ms_group_id'):
                response = team_manager.archive_unarchive_team(
                    {"group_id"  : fn_inputs.ms_group_id,
                     "operation" : fn_inputs.archive_operation})

            elif hasattr(fn_inputs, 'ms_group_mail_nickname'):
                response = team_manager.archive_unarchive_team(
                    {"group_mail_nickname" : fn_inputs.ms_group_mail_nickname,
                     "operation" : fn_inputs.archive_operation})

            elif hasattr(fn_inputs, 'ms_team_name'):
                response = team_manager.archive_unarchive_team(
                    {"group_name" : fn_inputs.ms_team_name,
                     "operation"  : fn_inputs.archive_operation})

            else:
                raise IntegrationError(constants.ERROR_INVALID_OPTION_PASSED)
            try:
                yield FunctionResult(response, success=True)
            except IntegrationError as err:
                yield FunctionResult({}, success=False, reason=str(err))
