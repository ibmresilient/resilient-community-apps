# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, line-too-long, wrong-import-order
# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.

"""AppFunction implementation"""
from resilient_lib import IntegrationError, validate_fields
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult

from fn_teams.lib import constants
from fn_teams.lib.microsoft_commons import ms_authenticate
from fn_teams.lib.microsoft_teams import TeamsInterface


PACKAGE_NAME = constants.PACKAGE_NAME
FN_NAME = "ms_teams_list_team_channels"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'ms_teams_enable_team'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        List available groups, using an optional filter to reduce the list returned:

            -> ms_channel_team_id
            -> teams_filter

        Returns:
        --------
            Response <dict> : A response with the details of the available groups
        """

        validate_fields(["ms_channel_team_id"], fn_inputs)

        yield self.status_message(constants.STATUS_STARTING_APP.format(FN_NAME))

        required_parameters = {}
        required_parameters["rc"] = self.rc
        required_parameters["logger"] = self.LOG
        required_parameters["resclient"] = self.rest_client()

        authenticator = ms_authenticate(self.rc, self.options)

        if authenticator:
            required_parameters["header"] = authenticator.authenticate_application_permissions()
            try:
                team_manager = TeamsInterface(required_parameters)

                response = team_manager.list_team_channels(fn_inputs.ms_channel_team_id, getattr(fn_inputs, 'teams_filter', None))
                yield FunctionResult(response["value"], success=True)

            except IntegrationError as err:
                yield FunctionResult({}, success=False, reason=str(err))
