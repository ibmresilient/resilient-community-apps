# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
import json

from resilient_lib import IntegrationError, validate_fields
from fn_webex.lib import constants, cisco_commons

class WebexAuthentication:
    """
        This application refreshes the OAuth authetication >>RefreshToken<< to interface with 
        the Cisco Webex Endpoint using the Client ID and the Client Secret that was generated
        while an integration is created at developers.webex.com . Inputs are taken in the form
        of a dictionary: requiredParameters. The below mentioned inputs need to be available
        in the requiredParameters dictionary for the authenticator to work.

        Inputs:
        -------
            clientID     (<str>) : Client ID of the integration created on developer.webex.com
            elientSecret (<str>) : Client Secret of the same integration
            refreshToken (<str>) : Refresh token generated using the OAuth Utilities Tool
            scope        (<str>) : Scopes selected during integraiton creation is to be
                                    specified in a space seperated fashion

        Returns:
        --------
            RequestHeader (<dict>) : An authorization Bearer ID and Content-Type as 
                                     application/json
    """

    def __init__(self, required_parameters, app_config):
        validate_fields(["client_id", "scope", "client_secret", "refresh_token"], app_config)
        self.required_parameters = required_parameters
        self.required_parameters["clientID"] = app_config.get("client_id")
        self.required_parameters["clientSecret"] = app_config.get("client_secret")
        self.required_parameters["refreshToken"] = app_config.get("refresh_token")
        self.required_parameters["scope"] = app_config.get("scope")
        self.required_parameters["tokenURL"] = app_config.get("webex_site_url") + constants.TOKEN_URL
        self.rc  = required_parameters.get("rc")
        self.LOG = self.required_parameters.get("logger")
        self.response_handler = cisco_commons.ResponseHandler()


    def authenticate(self):
        '''
        Helper method that establishes a connection with the Client servers and performs an OAuth
        authentication. The server returns a beareID for the session, which then is used to make
        requests. This bearer_id is incorporated with the header for every request henceforth
        '''
        bearer_id = self.generate_bearerID()
        header = self.generate_header(bearer_id)
        return header


    def generate_bearerID(self):
        '''
        This function perfroms OAuth authentication and retrieves the bearer_id which is necessary
        to interact with the webex endpoint.

        Options:
        -------
        client_id : This ID is generated while creating an integration on the webex endpoint
        
        '''
        data = {
            "client_id": self.required_parameters["clientID"],
            "scope": self.required_parameters["scope"],
            "client_secret": self.required_parameters["clientSecret"],
            "refresh_token": self.required_parameters["refreshToken"],
            "grant_type": "refresh_token"
        }
        response = self.rc.execute("POST", self.required_parameters["tokenURL"], data=data, 
                                 callback=self.response_handler.check_response)
        self.LOG.debug("Webex Authentication : {}".format(json.dumps(response)))


        if "access_token" in response:
            bearer_id = response.get("access_token")
            self.LOG.debug("Webex: Bearer ID for current session: {}".format(bearer_id))
            return bearer_id

        msg = u"Unable to authenticate: Error: {}".format(response.get("message"))
        raise IntegrationError(msg)


    def generate_header(self, bearer_id):
        '''
        Checks for bearer_id and returns it in a json format for request header
        
        Arguments:
        ---------
        bearer_id : Integer
                   Session ID that is required for authentication
        '''
        if not bearer_id:
            raise IntegrationError("Bearer ID not specified")
        return {
            'Authorization' : "Bearer {}".format(bearer_id),
            'Content-Type'  : 'application/json'}
