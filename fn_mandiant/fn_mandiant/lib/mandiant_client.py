# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.

import time
import logging

from retry import retry
from base64 import b64encode
from resilient_lib import IntegrationError
from resilient_lib import validate_fields

TOKEN_TYPE = "token_type"
ACCESS_TOKEN = "access_token"
ERROR_RESPONSE = "error"
CONTENT_TYPE = "application/json"

AUTH_KEY = "api_key"
AUTH_SECRET = "api_secret"
AUTHENTICATED = "authenticated"

TOKEN_URL = "https://api.intelligence.fireeye.com/token"
HOST_URL  = "https://api.intelligence.mandiant.com"
QUERY_URL = "{host}/v4/indicator/{type}/{value}?explainer=true"


LOG = logging.getLogger(__file__)

class MandiantClient:
    """
    Client that allows for connecting to Mandiant endpoint and searching information on IOC.
    """
    def __init__(self, rc, options):

        # Checking if AUTH_KEY and SECRET is available in app.conf
        validate_fields([AUTH_KEY, AUTH_SECRET], options)

        self.rc = rc
        self._client_common = {
            AUTH_KEY : options.get(AUTH_KEY),
            AUTH_SECRET : options.get(AUTH_SECRET),
            AUTHENTICATED : False}


    @retry(IntegrationError, delay=2, tries=3, backoff=2)
    def authenticate(self):
        """
        Initiates the authentication process by obtaining an access token using client credentials. A retry
        logic is built in to make sure that any connection drops or rejected requests does not result in a
        failed execution.

        This function performs the following steps:
            1. Logs the initiation of the authentication process.
            2. Retrieves the API key and secret from the client common configuration.
            3. Generates a basic authentication token by base64 encoding the key and secret.
            4. Constructs the HTTP headers with the generated authorization token.
            5. Constructs the request body with the 'grant_type' for client credentials.
            6. Sends a POST request to the token URL with the constructed headers and body.
            7. Parses the response and checks for the presence of an access token.
            8. If successful, updates the client common configuration with the received access
               token and expiration time.
            9. If unsuccessful, raises an IntegrationError with a description of the failure.

        Raises:
        ------
            IntegrationError:
                If the authentication process fails, raising this error with a description.
            IndentationError:
                If no ACCESS_TOKEN is found in the response.

        Returns:
        -------
            None
        """
        LOG.info("Initiating Authentication process")

        _key, _secret = self._client_common.get(AUTH_KEY), self._client_common.get(AUTH_SECRET)
        _cur_time = int(time.time())

        # base64Encoding the key and secret to generate the required token for a basic 
        # authentication.
        auth_token = b64encode(
            f"{_key}:{_secret}".encode('utf-8')
        ).decode('utf-8')

        header = {
            'Authorization' : f'Basic {auth_token}'}
        body = {
            'grant_type': 'client_credentials'}

        try:
            res = self.rc.execute(
                "post",
                TOKEN_URL,
                headers=header,
                data=body
            ).json()
        except Exception as e:
            # Failed request raises an Integration error, to be caught by the
            # retry logic preventing failed executions.
            raise IntegrationError(f"Authentication failed. {str(e)}")

        if res.get(ACCESS_TOKEN):
            # When ACCESS_TOKEN is found, the request header required for performing
            # all app related actions is formulated. The expiry time is also tracked
            # in order to 
            LOG.info("ACCESS_TOKEN received. Compiling request headers.")
            self._client_common["headers"] = {
                'Accept'        : CONTENT_TYPE,
                'Authorization' : f"{res.get(TOKEN_TYPE)} {res.get(ACCESS_TOKEN)}"}
            self._client_common['expires_in']  = _cur_time + res.get('expires_in')
            self._client_common[AUTHENTICATED] = True

        else:
            err_msg = f"Authentication failed. Did not receive ACCESS_TOKEN. Response : {res}"
            LOG.error(err_msg)
            raise IntegrationError(err_msg)


    def check_authenticated(self):
        """
        Checks whether the application has successfully established a connection with the endpoint.

        This function performs the following checks:
            1. Checks if the 'expires_in' value in the client common configuration is missing,
               or if the current time has exceeded the expiration time, or if 'AUTHENTICATED' flag
               is not set.
            2. If any of the above conditions are met, it logs that the application is not
               authenticated and returns False.
            3. If none of the conditions are met, it logs that the application has been successfully
               authenticated and returns True.
            
        Returns:
            bool: True if the application is authenticated, False otherwise.
        """
        LOG.info("Checking to see if the application has successfully established a connection with the endpoint")
        if (
            not self._client_common.get("expires_in")
            or int(time.time()) > self._client_common.get("expires_in")
            or not self._client_common.get(AUTHENTICATED)):
            LOG.info("App not authenticated.")
            return False
        LOG.info("App has been successfully authenticated.")
        return True


    @retry(IntegrationError, delay=2, tries=3, backoff=2)
    def search_artifact(self, artifact_type, artifact_data):
        """
        Searches for information related to a given artifact based on its type and data. A retry logic
        is built in to make sure that any connection drops or rejected requests does not result in a
        failed execution.
        
        This function performs the following steps:
            1. Constructs a query URL based on the provided artifact type and data.
            2. Sends a GET request to the constructed URL with the stored client headers.
            3. Attempts to parse the response JSON.
            4. In case of success, returns the response data.
            5. In case of an exception during the request or parsing, returns an error message.

        Args:
        ----
            artifact_type (str):
                    The type of the artifact, e.g., 'ip address', 'url', 'domain', 'malware md5 hash'.
    
            artifact_data (str):
                    The data associated with the artifact, e.g., an IP address, URL, domain, or MD5 hash.

        Returns:
        -------
            dict: 
                - A dictionary containing the response data, or an error message in case of failure.
                - If the provided artifact_type is not one of the supported types, it returns an error
                  dictionary.

        """
        if artifact_type == 'ip address':
            url = QUERY_URL.format(host=HOST_URL, type="ipv4", value=str(artifact_data))
        elif artifact_type == 'url':
            url  = QUERY_URL.format(host=HOST_URL, type="url", value=str(artifact_data))
        elif artifact_type == 'dns name':
            url  = QUERY_URL.format(host=HOST_URL, type="fqdn", value=str(artifact_data))
        elif artifact_type == 'malware md5 hash':
            url  = QUERY_URL.format(host=HOST_URL, type="md5", value=str(artifact_data))
        else:
            return {"error": "IoC Type not supported"}
        try:
            response = self.rc.execute("get", url, headers=self._client_common["headers"]).json()
        except Exception as e:
            # Reauthenticates to eliminate the possibility of an expired ACCESS_TOKEN and raises
            # an Integration error to be caught by the retry logic.
            self.authenticate()
            raise IntegrationError(str(e))
        return response
