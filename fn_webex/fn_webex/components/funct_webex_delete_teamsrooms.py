# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
#
# """AppFunction implementation"""
from urllib import parse
from fn_webex.lib import constants
from fn_webex.lib.cisco_interface import WebexInterface
from fn_webex.lib.cisco_authentication import WebexAuthentication
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields

PACKAGE_NAME = "fn_webex"
FN_NAME = "webex_delete_teamsrooms"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'webex_delete_teamsrooms'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)
        self.opts = opts
        self.requiredParameters = {}
        self.config_options = opts.get(PACKAGE_NAME, {})


    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        This function creates a Webex team and adds a team to it.

        Fn Inputs:
        ----------
            entityId          (<str>) : ID of the Room or Team to be deleted
            entityName        (<str>) : Specifies if a Room or a Team is to be deleted
        
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
        validate_fields(["webex_entity_id", "webex_roomteam_selector"], fn_inputs)

        self.requiredParameters["rc"] = self.rc
        self.requiredParameters["logger"] = self.LOG
        self.requiredParameters["resclient"] = self.rest_client()

        self.requiredParameters["baseURL"] = self.config_options.get("webex_site_url")
        self.requiredParameters["entityId"]   = fn_inputs.webex_entity_id
        self.requiredParameters["entityName"] = fn_inputs.webex_roomteam_selector
        
        try:
            yield self.status_message(constants.MSG_CREATE_SECURITY)
            self.LOG.info(constants.MSG_CREATE_SECURITY)
            authenticator = WebexAuthentication(self.requiredParameters, self.config_options)
            self.requiredParameters["header"] = authenticator.Authenticate()
            authenticated = True
            self.LOG.info(constants.MSG_SUCCESS_AUTHENTICATED)
            yield self.status_message(constants.MSG_SUCCESS_AUTHENTICATED)

        except Exception as err:
            self.LOG.error(constants.MSG_FAILED_AUTH)
            yield self.status_message(constants.MSG_FAILED_AUTH)
            authenticated = False
            yield self.status_message("Failed to run App Function : '{0}'".format(FN_NAME))
            yield FunctionResult(None, success=False, reason=str(err))

        if authenticated:
            webex = WebexInterface(self.requiredParameters)
            yield webex.delete_entity()
            yield self.status_message("Finished running App Function successfully: '{0}'".format(FN_NAME))
