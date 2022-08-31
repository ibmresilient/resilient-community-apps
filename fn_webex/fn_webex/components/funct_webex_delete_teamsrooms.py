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

        Args:
        -----
            entityId           (<str>)  : ID of the Room or Team to be deleted
            entityName         (<str>)  : Specifies if a Room or Team is to be deleted
            rc                  (<rc>)  : A resilient wrapper for Requests object
            logger           (<logger>) : A resilient wrapper for logger obhect
            resclient   (<rest_client>) : Rest client to interact with the SOAR instance

        Yields:
        -------
            (<FunctionResult>): States if the application was executed successfully or not.
                                Returns the response retrieved from the Webex endpoint in 
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
            yield self.status_message("Authenticating Webex using OAuth Access Token: '{0}'".format(FN_NAME))
            self.LOG.info("Webex: Creating a Security context and establishing a connection with the Webex EndPoint")
            authenticator = WebexAuthentication(self.requiredParameters, self.config_options)
            self.requiredParameters["header"] = authenticator.Authenticate()
            yield self.status_message("Successfully Authenticated!")
            
        except Exception as err:
            self.LOG.error("Failed to create Security Context")
            yield self.status_message("Failed to Authenticate {}! Is the Refresh token Upto date?".format(FN_NAME))
            reason = err.__str__()
            yield FunctionResult(value=None, success=False, reason=reason)

        webex = WebexInterface(self.requiredParameters)
        response = webex.deleteEntity()
        
        if response.get("status_code") == 204:
            yield FunctionResult(response, success=True)
        elif response.get("status_code") == 404:
            yield FunctionResult(response, success=False, reason="The specified room/team ID could not be found!")
        elif response.get("status_code") == 405:
            yield FunctionResult(response, success=False, reason="This room cannot be deleted directly. Delete the team associated with it to clear this space.")

        yield self.status_message("Finished running App Function successfully: '{0}'".format(FN_NAME))
