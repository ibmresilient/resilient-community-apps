# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

import msal
from urllib import parse

from resilient_lib import IntegrationError, validate_fields
from fn_teams.lib import constants

class MicrosoftAuthentication:
    """
        This application generates an access token using the the MSAL class to interface with 
        the Microsoft Endpoint using the directory_id, application_id and secret_value that was
        generated while an integration is created at portal.azure.com. Inputs are taken in the
        form of a dictionary: requiredParameters. The below mentioned inputs need to be available
        in the requiredParameters dictionary for the authenticator to work. All required credentials
        for an integration can be found at:
            portal.azure.com > App registrations > Integration Name
        Inputs:
        -------
            directory_id   <str> : Directory (tenant) ID found at azure portal
            application_id <str> : Application (client) ID found at azure portal
            secret_value   <str> : Secret Value found for the integration
            scope          <str> : Specifies required access permission for this
                                   application to function
        Returns:
        --------
            RequestHeader <dict> : An authorization Bearer ID and Content-Type as 
                                   application/json
    """

    def __init__(self, required_parameters, app_config):
        validate_fields(["directory_id", "application_id", "secret_value"], app_config)

        self.required_parameters = required_parameters
        self.rc  = required_parameters.get("rc")
        self.LOG = required_parameters.get("logger")

        self.required_parameters["scope"] = constants.DEFAULT_SCOPE
        self.required_parameters["application_id"] = app_config.get("application_id")
        self.required_parameters["secret_value"] = app_config.get("secret_value")
        self.required_parameters["directory_id"] = parse.urljoin(
            constants.AUTH_URL,
            app_config.get("directory_id"))


    def authenticate(self):
        '''
        Helper method that establishes a connection with the Client servers and performs an OAuth
        authentication. The server returns a beareID for the session, which then is used to make
        requests. This bearer_id is incorporated with the header for every request henceforth
        Returns:
        --------
            header <dict> : Request header with access_token
        '''
        bearer_id = self.generate_bearer_id()
        header = self.generate_header(bearer_id)
        return header


    def generate_bearer_id(self):
        '''
        This function perfroms MSAL authentication and retrieves the bearer_id which is necessary
        to interact with the Microsoft's endpoint.
        Raises:
        -------
            <IntegrationError> : Access_token not found in response
        Returns:
        --------
            bearer_id <str> : Access_token on successful authentication
        '''
        app = msal.ConfidentialClientApplication(
            self.required_parameters["application_id"],
            authority=self.required_parameters["directory_id"],
            client_credential=self.required_parameters["secret_value"]
        )
        response = app.acquire_token_for_client(scopes=[
            parse.urljoin(constants.BASE_URL, constants.DEFAULT_SCOPE)])

        if "access_token" in response:
            self.LOG.info(constants.INFO_RETRIEVED_BEARER_ID)
            return response['access_token']

        msg = f"Unable to authenticate: Error: {response.get('error')} {response.get('error_description')}"
        self.LOG.error(msg)
        raise IntegrationError(msg)


    def generate_header(self, bearer_id):
        '''
        Checks for bearer_id and returns it in a json format for request header
        
        Arguments:
        ---------
            bearer_id <int> : Session ID that is required for authentication
        
        Returns:
        --------
            header <dict> : Request header with access_token
        '''
        if not bearer_id:
            raise IntegrationError("Bearer ID not specified")
        self.LOG.debug(constants.DEBUG_BEARER_ID.format(bearer_id))

        return {
            'Authorization' : 'Bearer {}'.format(bearer_id),
            "Content-type"  : "application/json"}