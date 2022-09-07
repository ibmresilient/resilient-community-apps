# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
import json

from fn_webex.lib import constants, cisco_commons
from resilient_lib import IntegrationError, validate_fields

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

    def __init__(self, requiredParameters, app_config):
        validate_fields(["client_id", "scope", "client_secret", "refresh_token"], app_config)
        self.requiredParameters = requiredParameters
        self.requiredParameters["clientID"] = app_config.get("client_id")
        self.requiredParameters["clientSecret"] = app_config.get("client_secret")
        self.requiredParameters["refreshToken"] = app_config.get("refresh_token")
        self.requiredParameters["scope"] = app_config.get("scope")
        self.requiredParameters["tokenURL"] = app_config.get("webex_site_url") + constants.TOKEN_URL
        self.rc  = requiredParameters.get("rc")
        self.LOG = self.requiredParameters.get("logger")
        self.response_handler = cisco_commons.ResponseHandler()


    def Authenticate(self):
        '''
        Helper method that establishes a connection with the Client servers and performs an OAuth
        authentication. The server returns a beareID for the session, which then is used to make
        requests. This bearerID is incorporated with the header for every request henceforth
        '''
        bearerID = self.generate_bearerID()
        header = self.generate_header(bearerID)
        return header


    def generate_bearerID(self):
        '''
        This function perfroms OAuth authentication and retrieves the bearerID which is necessary
        to interact with the webex endpoint.

        Options:
        -------
        client_id : This ID is generated while creating an integration on the webex endpoint
        
        '''
        data = {
            "client_id": self.requiredParameters["clientID"],
            "scope": self.requiredParameters["scope"],
            "client_secret": self.requiredParameters["clientSecret"],
            "refresh_token": self.requiredParameters["refreshToken"],
            "grant_type": "refresh_token"
        }
        response = self.rc.execute("POST", self.requiredParameters["tokenURL"], data=data, 
                                 callback=self.response_handler.check_response)
        self.LOG.debug("Webex Authentication : {}".format(json.dumps(response)))


        if "access_token" in response:
            bearerID = response.get("access_token")
            self.LOG.debug("Webex: Bearer ID for current session: {}".format(bearerID))
            return bearerID

        msg = u"Unable to authenticate: Error: {}\nDescription: {}"\
            .format(response.get("error"), response.get("error_description"))
        raise IntegrationError(msg)


    def generate_header(self, bearerID):
        '''
        Checks for bearerID and returns it in a json format for request header
        
        Arguments:
        ---------
        bearerID : Integer
                   Session ID that is required for authentication
        '''
        if not bearerID:
            raise ValueError("Bearer ID not specified")
        return {
            'Authorization' : "Bearer {}".format(bearerID),
            'Content-Type'  : 'application/json'}
