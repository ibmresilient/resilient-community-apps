# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
#
# """AppFunction implementation"""
import json
from urllib import parse

from resilient_lib import validate_fields, IntegrationError
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult

from fn_teams.lib import constants
from fn_teams.lib.teams_authentication import TeamsAuthentication

PACKAGE_NAME = "fn_teams"
FN_NAME = "ms_teams_create_group"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'webex_delete_teamsrooms'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)
        self.opts = opts
        self.required_parameters = {}
        self.config_options = opts.get(PACKAGE_NAME, {})


    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):

        yield self.status_message(constants.STATUS_STARTING_APP.format(FN_NAME))
        validate_fields(["base_url"], self.config_options)

        self.required_parameters["rc"] = self.rc
        self.required_parameters["logger"] = self.LOG
        self.required_parameters["resclient"] = self.rest_client()

        try:
            yield self.status_message(constants.STATUS_GENERATE_HEADER)
            authenticator = TeamsAuthentication(self.required_parameters, self.config_options)
            self.required_parameters["header"] = authenticator.authenticate()
            authenticated = True
            yield self.status_message(constants.STATUS_SUCCESSFULLY_AUTHENTICATED)

        except IntegrationError as err:
            self.LOG.error(constants.STATUS_SUCCESSFULLY_AUTHENTICATED)
            yield self.status_message(constants.STATUS_AUTHENTICATION_FAILED)
            authenticated = False
            yield self.status_message(constants.STATUS_FAILED_APP.format(FN_NAME))
            yield FunctionResult(None, success=False, reason=str(err))

        if authenticated:
            self.rc.execute(method="get",
                url=parse.urljoin(constants.BASE_URL, constants.LIST_USERS),
                headers=self.required_parameters.get("header"))
            yield FunctionResult(constants.STATUS_SUCCESSFULLY_AUTHENTICATED, success=True)
