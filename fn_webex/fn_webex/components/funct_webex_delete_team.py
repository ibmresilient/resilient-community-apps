# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
#
# """AppFunction implementation"""
from resilient_lib import validate_fields, IntegrationError
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult

from fn_webex.lib.cisco_delete import WebexDelete
from fn_webex.lib import constants
from fn_webex.lib.cisco_authentication import WebexAuthentication

PACKAGE_NAME = "fn_webex"
FN_NAME = "webex_delete_team"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'webex_delete_teamsrooms'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)
        self.opts = opts
        self.required_parameters = {}
        self.config_options = opts.get(PACKAGE_NAME, {})


    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        This function creates a Webex team and adds a team to it.

        Fn Inputs:
        ----------
            teamId            (<str>) : ID of the Room or Team to be deleted
            teamName          (<str>) : Name of the Room or Team to be deleted

        Config Options:
        ---------------
            baseURL           (<str>) : The Webex site url

        Self Objects:
        -------------
            rc                 (<rc>) : A resilient wrapper for Requests object
            logger         (<logger>) : A resilient wrapper for logger obhect
            resclient (<rest_client>) : Rest client to interact with the SOAR instance

        Yields:
        -------
                   (<FunctionResult>) : States if the application was executed successfully or not.
                                        returns the response retrieved from the Webex endpoint in
                                        the form of a dictionary.
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))
        validate_fields(["webex_site_url", "webex_timezone", "client_id",
                         "client_secret", "refresh_token", "scope"], self.config_options)

        self.required_parameters["rc"] = self.rc
        self.required_parameters["logger"] = self.LOG
        self.required_parameters["resclient"] = self.rest_client()

        self.required_parameters["baseURL"] = self.config_options.get("webex_site_url")
        self.required_parameters["entityId"] = fn_inputs.webex_team_id if hasattr(fn_inputs, 'webex_team_id') else None
        self.required_parameters["entityName"] = fn_inputs.webex_team_name if hasattr(fn_inputs, 'webex_team_name') else None
        self.required_parameters["entityType"] = constants.TEAM
        
        try:
            yield self.status_message(constants.MSG_CREATE_SECURITY)
            self.LOG.info(constants.MSG_CREATE_SECURITY)
            authenticator = WebexAuthentication(self.required_parameters, self.config_options)
            self.required_parameters["header"] = authenticator.authenticate()
            authenticated = True
            self.LOG.info(constants.MSG_SUCCESS_AUTHENTICATED)
            yield self.status_message(constants.MSG_SUCCESS_AUTHENTICATED)

        except IntegrationError as err:
            self.LOG.error(constants.MSG_FAILED_AUTH)
            yield self.status_message(constants.MSG_FAILED_AUTH)
            authenticated = False
            yield self.status_message("Failed to run App Function : '{0}'".format(FN_NAME))
            yield FunctionResult(None, success=False, reason=str(err))

        if authenticated:
            webex = WebexDelete(self.required_parameters)
            yield webex.delete_team_room()
            yield self.status_message(constants.MSG_SUCCESS_EXECUTION.format(FN_NAME))
