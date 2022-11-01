# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
#
# """AppFunction implementation"""
from urllib import parse

from resilient_lib import validate_fields, IntegrationError
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult

from fn_teams.lib import constants
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

        yield self.status_message(constants.STATUS_STARTING_APP.format(FN_NAME))

        self.required_parameters["rc"] = self.rc
        self.required_parameters["logger"] = self.LOG
        self.required_parameters["resclient"] = self.rest_client()

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
            yield FunctionResult(None, success=False, reason=str(err))

        if authenticated:
            self.rc.execute(method="get",
                url=parse.urljoin(constants.BASE_URL, constants.LIST_USERS),
                headers=self.required_parameters.get("header"))
            yield FunctionResult(constants.STATUS_SUCCESSFULLY_AUTHENTICATED, success=True)
