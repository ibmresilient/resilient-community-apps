# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, line-too-long
''' (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved. '''

import logging
import posixpath
from urllib import parse

import msal
from resilient_lib import IntegrationError, validate_fields

from fn_teams.lib import constants

LOG = logging.getLogger(__name__)

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

    def __init__(self, request_common, app_config):
        validate_fields(["application_id", "secret_value", "directory_id"], app_config)

        self.rc  = request_common
        self.required_parameters = {}

        self.required_parameters["scope"] = constants.DEFAULT_SCOPE
        self.required_parameters["application_id"] = app_config.get("application_id")
        self.required_parameters["secret_value"] = app_config.get("secret_value")
        self.required_parameters["oauth_consent_url"] = app_config.get("oauth_consent_url")

        self.required_parameters["directory_id"] = parse.urljoin(
            constants.AUTH_URL,
            app_config.get("directory_id"))
        self.required_parameters["redirect_uri"] = app_config.get(
            "redirect_uri",
            constants.DEFAULT_REDIRECT_URI)


    def _generate_application_bearer_id(self) -> str:
        '''
        This function performs MSAL authentication and retrieves the bearer_id which is necessary
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
            client_credential=self.required_parameters["secret_value"])

        response = app.acquire_token_for_client(scopes=[
            parse.urljoin(constants.BASE_URL, constants.DEFAULT_SCOPE)])

        if "access_token" in response:
            LOG.info(constants.INFO_RETRIEVED_BEARER_ID)
            return response['access_token']

        msg = constants.ERROR_UNABLE_TO_AUTHENTICATE.format(
            response.get('error'),
            response.get('error_description'))
        LOG.error(msg)
        raise IntegrationError(msg)


    def _generate_header(self, bearer_id:str) -> dict:
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
        LOG.debug(constants.DEBUG_BEARER_ID.format(bearer_id))

        return {
            "Authorization" : constants.BEARER.format(bearer_id),
            "Content-type"  : constants.CONTENT_TYPE_JSON}


    def authenticate_application_permissions(self) -> dict:
        '''
        Helper method that establishes a connection with the Client servers and performs an OAuth
        authentication. The server returns a bearerID for the session, which then is used to make
        requests. This bearer_id is incorporated with the header for every request henceforth

        Returns:
        --------
            header <dict> : Request header with access_token
        '''
        bearer_id = self._generate_application_bearer_id()
        header = self._generate_header(bearer_id)
        return header


    def _generate_delegation_tokens(self, grant_type:str, consent_code:str) -> dict:

        if grant_type == constants.DELEGATED_GRANT_REFRESH:
            code_type = constants.CODE_TYPE_REFRESH
        else:
            code_type = constants.CODE_TYPE_ACCESS

        url = posixpath.join(
            self.required_parameters["directory_id"],
            constants.OAUTH_TOKEN_URL)

        header = {
            "Content-type"  : constants.CONTENT_TYPE_URLENCODED}

        authorization_body = {
            code_type       : consent_code,
            "grant_type"    : grant_type,
            "client_id"     : self.required_parameters["application_id"],
            "redirect_uri"  : self.required_parameters["redirect_uri"],
            "client_secret" : self.required_parameters["secret_value"]}

        response = self.rc.execute(
            "post",
            url=url,
            headers=header,
            data=authorization_body)
        response = response.json()

        if "access_token" in response:
            return response

        msg = constants.ERROR_UNABLE_TO_AUTHENTICATE.format(
            response.get('error'),
            response.get('error_description'))
        LOG.error(msg)
        raise IntegrationError(msg)


    def authenticate_delegated_permissions(self, refresh_token:str = None):

        if refresh_token:
            LOG.info("Refreshing existing access token")
            tokens = self._generate_delegation_tokens(constants.DELEGATED_GRANT_REFRESH, refresh_token)
        else:
            raise IntegrationError(constants.ERROR_NO_REFRESH_TOKEN)

        header = self._generate_header(tokens.get("access_token"))
        return header
