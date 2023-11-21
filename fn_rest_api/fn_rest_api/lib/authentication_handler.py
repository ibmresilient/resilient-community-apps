# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010 to 2023. All Rights Reserved.

import jwt
import logging, json
import shutil, os, time

from resilient_lib import IntegrationError
from resilient_lib import write_to_tmp_file
from fn_rest_api.lib.helper import validate_url

APP_NAME = "fn_rest_api"
HEADERS = "headers"
AUTHORIZATION_KEY = "Authorization"
DEFAULT_TOKEN_TYPE = "bearer"


LOG = logging.getLogger(__file__)


"""
    O A U T H  2. 0
    - - - - -  -  -
"""
OAUTH_REQUEST_METHOD = "post"
DEFAULT_AUTH_CONTENT_TYPE = "application/x-www-form-urlencoded"

AUTH_URL = "auth_url"
TOKEN_URL = "token_url"
CODE  = "code"
STATE = "state"
SCOPE = "scope"
AUTH_TYPE = "auth_type"
TOKEN_VALUE = "token_value"
CLIENT_ID  = "client_id"
TOKEN_TYPE = "token_type"
EXPIRES_IN = "expires_in"
ACCESS_TOKEN = "access_token"
CLIENT_SECRET = "client_secret"
REFRESH_TOKEN = "refresh_token"
RESPONSE_MODE = "response_mode"
RESPONSE_TYPE = "response_type"
REDIRECT_URI  = "redirect_uri"
CONTENT_TYPE  = "content_type"
ADDITIONAL_HEADERS = "additional_headers"
ADDITIONAL_ATTRIBUTES = "additional_attributes"

OAUTH_SUPPORTED    = "oauth_supported"
FLOW_ACCESS_TOKEN  = "access_token_flow"
FLOW_REFRESH_TOKEN = "refresh_token_flow"
FLOW_AUTHORIZATION = "authorization_flow"
FLOW_CLIENT_CREDENTIALS = "client_credentials_flow"

GRANT_TYPE = "grant_type"
REFRESH_GRANT_TYPE = "refresh_token"
ACCESS_GRANT_TYPE  = "authorization_code"
CLIENT_CREDENTIALS_GRANT_TYPE = "client_credentials"


class OAuth2Authorization():
    """
    Perform OAuth authentication. This supports 3 different flow:
    
    * Refresh-Token
    * Client-Credentials
    * Access-Token
    * Authorization
    
    ==================
    REFRESH-TOKEN FLOW
    ==================

            Using REFRESH_TOKENS usually generates new ACCESS_TOKEN. This also extends the
        life span of the same REFRESH_TOKEN. Therefore the same REFRESH_TOKEN can be used to
        generate new ACCESS_TOKEN

        ..note::
        On successfully completing a `refresh-token` flow, the existing client properties are
        updated with the newly fetched values. This means that this client can be used to fetch
        new tokens and values virtually indefinitely.

        ..code::
        REQUEST FORMAT:        Using REFRESH_TOKEN to refresh ACCESS_TOKEN and REFRESH_TOKEN
        ---------------
            Header:
                CONTENT_TYPE : "application/x-www-form-urlencoded"
            Body:
                GRANT_TYPE   : "refresh_token"
                CLIENT_ID
                CLIENT_SECRET
                REFRESH_TOKEN

        RESPONSE FORMAT:
        ----------------
            Body:
                ACCESS_TOKEN
                EXPIRES_IN
                REFRESH_TOKEN_EXPIRES_IN
                REFRESH_TOKEN                       (optional)
                SCOPE                               (optional)
    
    ==================
    AUTHORIZATION FLOW
    ==================

            Using CODE to get ACCESS_TOKEN and REFRESH_TOKEN. CODE is a one-off credential
        that can be exchanged for an ACCESS_TOKEN and REFRESH_TOKEN.

        ..note::
        if the endpoint returns a `refresh-token` on successively completing the above flow,
        the existing client properties are updated with the newly fetched values. This means
        the client goes from `Authorization Flow` to `Refresh-Token flow` moving forward.
        This means that this client can be used to fetch new tokens and values virtually
        indefinitely.

        REQUEST FORMAT:        Exchanging CODE for ACCESS_TOKEN and REFRESH_TOKEN
        ---------------
            Header:
                CONTENT_TYPE  : "application/x-www-form-urlencoded"

            Body:
                GRANT_TYPE    : "authorization_code"
                CLIENT_ID
                CLIENT_SECRET
                CODE
                REDIRECT_URI
                RESPONSE_TYPE : "code"              (optional)
                SCOPE                               (optional)
                STATE                               (optional)

        RESPONSE FORMAT:
        ----------------
            Body:
                ACCESS_TOKEN
                EXPIRES_IN
                REFRESH_TOKEN_EXPIRES_IN
                REFRESH_TOKEN                       (optional)
                SCOPE                               (optional)
    
    =======================
    CLIENT-CREDENTIALS FLOW
    =======================

            Client Credentials Flow doesn't involve user authentication, and it is suitable
        for scenarios where the client is a confidential client, meaning it can keep its client
        credentials (client ID and client secret) secure.

        ..note::
        if the endpoint returns a `refresh-token` on successively completing the above flow,
        the existing client properties are updated with the newly fetched values. This means
        the client goes from `Client-Credentials Flow` to `Refresh-Token flow` moving forward.
        This means that this client can be used to fetch new tokens and values virtually
        indefinitely.

        REQUEST FORMAT:        Exchanging CODE for ACCESS_TOKEN and REFRESH_TOKEN
        ---------------
            Header:
                CONTENT_TYPE  : "application/x-www-form-urlencoded"

            Body:
                GRANT_TYPE    : "client_credentials"
                CLIENT_ID
                CLIENT_SECRET

        RESPONSE FORMAT:
        ----------------
            Body:
                ACCESS_TOKEN
                EXPIRES_IN
                REFRESH_TOKEN_EXPIRES_IN
                REFRESH_TOKEN                       (optional)
                SCOPE                               (optional)
    """

    def __init__(self, rc, oauth_inputs, retry_options):
        """ Constructor for the OAuth2Authorization
        :param rc: request_common required for making REST requests
        :type rc: resilient_lib.request_common
        :param oauth_inputs: all oauth related inputs
        :type oauth_inputs: dict
        :param retry_options: enables the ability to retry failed requests
        :type retry_options: dict
        """
        self.rc = rc
        self._oauth_inputs  = oauth_inputs
        self._retry_options = retry_options


    def _compile_headers(self) -> dict:
        """
        Create headers needed for authentication/authorization, overriding the default ones if needed.

        :param headers: Dictionary containing the ``Authorization`` header
        :type headers: dict
        """
        return {AUTHORIZATION_KEY : f"{self._oauth_inputs.get(TOKEN_TYPE)} {self._oauth_inputs.get(ACCESS_TOKEN)}"}


    def _process_endpoint_response(self, response) -> bool:
        """
        Processes response received from the endpoint. The values received could vary from endpoint to endpoint. This allows
        the client to handle such varied responses.

        :param response: response received from endpoint
        :type response: requests.response
        :raises IntegrationError: Status code > 300. Invalid REFRESH_TOKEN supplied
        :raises ValueError: ACCESS_TOKEN not found in response
        :return: True when all required parameters are found in response
        :rtype: bool
        """

        if response.status_code >= 300:
            raise IntegrationError(f"Unable to refresh ACCESS_TOKEN. Please check or renew your REFRESH_TOKEN. {response.content}")

        response = response.json()

        # If REFRESH_TOKEN available in response, updates existing REFRESH_TOKEN to the current one.
        # Else retains existing TOKEN provided in the constructor.
        if REFRESH_TOKEN in response:
            self._oauth_inputs[REFRESH_TOKEN] = response.get(REFRESH_TOKEN)
            # Setting Grant-Type to `refresh_token` for re-authentication.
            self._oauth_inputs[GRANT_TYPE] = REFRESH_GRANT_TYPE

        # Extracting SCOPE if available in response
        if SCOPE in response:
            self._oauth_inputs[SCOPE] = response.get(SCOPE)

        # If TOKEN_TYPE not in response, using DEFAULT_TOKEN_TYPE specified while reading inputs in oauth_handler's constructor
        if TOKEN_TYPE in response:
            self._oauth_inputs[TOKEN_TYPE] = response.get(TOKEN_TYPE)
        else:
            LOG.warning(f"No {TOKEN_TYPE} detected in response. Using DEFAULT_TOKEN_TYPE : {DEFAULT_TOKEN_TYPE}")
            
        if EXPIRES_IN in response:
            self._oauth_inputs[EXPIRES_IN] = time.time() + int(response.get(EXPIRES_IN))

        if ACCESS_TOKEN in response:
            self._oauth_inputs[ACCESS_TOKEN] = response.get(ACCESS_TOKEN)
        else:
            raise ValueError(f"Did not receive ACCESS_TOKEN. Received response : {json.dumps(response, indent=2)}")

        return True


    def add_oauth_headers(self, rest_properties) -> dict:
        """
        This wrapper is for fn_rest_api. For the application to perform OAuth authentication,
        it requires certain parameters. This function checks to see if the required parameters
        are provided and performs OAuth authentication. If they aren't provided, it simply skips
        the process and directly performs the REST api call. To do so, it takes in the
        rest_headers and either adds oauth credentials/headers or skips and returns original
        headers untouched

        :param rest_properties: inputs for fn_rest_api
        :return: headers, with or without oauth generated credentials
        :rtype: dict
        """
        if self.check_oauth_ready()[OAUTH_SUPPORTED]:
            LOG.info("OAuth properties detected!")
            oauth_headers = self.authenticate()
            if rest_properties.get(HEADERS):
                rest_properties[HEADERS].update(oauth_headers)
            else:
                rest_properties[HEADERS] = oauth_headers
        return rest_properties


    def check_oauth_ready(self):
        """
        Responsible for determining if the application is OAuth ready. There are multiple authentication
        flows that can be performed, entirely depending upon the attributes provided.

            - TOKEN_URL
            - CLIENT_ID
            - CLIENT_SECRET (Optional: Client-credentials flow)
            - CODE          (Optional: Authorization flow)
            - ACCESS_TOKEN  (Optional: Access token flow)
            - REFRESH_TOKEN (Optional: Refresh token flow)

        This then returns a dictionary with a list of supported flows. This entirely depends on the input
        parameters provided.
        
        ..codeblock:: python
        {
            OAUTH_SUPPORTED    : False,
            FLOW_ACCESS_TOKEN  : False,
            FLOW_AUTHORIZATION : False,
            FLOW_REFRESH_TOKEN : False,
            FLOW_CLIENT_CREDENTIALS : False
        }
        
        :returns: True/False for each of the authentication flow
        :rtype: dict
        """
        supported_oauth_flow = {
            OAUTH_SUPPORTED    : False,
            FLOW_ACCESS_TOKEN  : False,
            FLOW_AUTHORIZATION : False,
            FLOW_REFRESH_TOKEN : False,
            FLOW_CLIENT_CREDENTIALS : False}
        
        if self._oauth_inputs.get(ACCESS_TOKEN):
            LOG.info(f"Application OAuth compliant. Detected: AccessToken Flow")
            supported_oauth_flow[FLOW_ACCESS_TOKEN] = supported_oauth_flow[OAUTH_SUPPORTED] = True

        # OAuth Client-Credentials Flow
        if  (
            self._oauth_inputs.get(TOKEN_URL) and
            self._oauth_inputs.get(CLIENT_ID) and
            self._oauth_inputs.get(CLIENT_SECRET) and
            self._oauth_inputs.get(GRANT_TYPE)) and (
            self._oauth_inputs.get(GRANT_TYPE).lower() == CLIENT_CREDENTIALS_GRANT_TYPE
        ):
            LOG.info(f"Application OAuth compliant. Detected: Client-Credentials Flow")
            supported_oauth_flow[FLOW_CLIENT_CREDENTIALS] = supported_oauth_flow[OAUTH_SUPPORTED] = True

        # OAuth Authorization Flow
        if  (
            self._oauth_inputs.get(CODE) and
            self._oauth_inputs.get(TOKEN_URL) and
            self._oauth_inputs.get(CLIENT_ID)
        ):
            LOG.info(f"Application OAuth compliant. Detected: Authorization Flow")
            supported_oauth_flow[FLOW_AUTHORIZATION] = supported_oauth_flow[OAUTH_SUPPORTED] = True

        # OAuth RefreshToken Flow
        if  (
            self._oauth_inputs.get(REFRESH_TOKEN) and
            self._oauth_inputs.get(TOKEN_URL) and
            self._oauth_inputs.get(CLIENT_ID)
        ):
            LOG.info(f"Application OAuth compliant. Detected: Refresh Token Flow")
            supported_oauth_flow[FLOW_REFRESH_TOKEN] = supported_oauth_flow[OAUTH_SUPPORTED] = True

        # Return False when provided parameters fall under none of the above mentioned categories
        return supported_oauth_flow


    def authenticate(self) -> dict:
        """
            This OAuth client support multiple authentication flows. The authentication flow to be performed
        is automatically chosen depending upon the input parameters provided to the OAuth client. However, certain
        authentication flows are alway prioritized over other flows, for instance, REFRESH_TOKEN flow is always
        prioritized over other flows. This is because REFRESH_TOKEN can always be used to fetch fresh ACCESS_TOKENS
        and on the even of a failed attempt, a REFRESH_TOKEN can always be used to renew the ACCESS_TOKEN.

        This is then followed by the AUTHORIZATION and the CLIENT_CREDENTIALS flow. It is worth noting that
        upon using AUTHORIZATION_FLOW or the REFRESH_TOKEN_FLOW the appropriate CODE and REFRESH_TOKEN is discarded
        and replaced with a REFRESH_TOKEN, if provided by the endpoint. This is to make sure that, if a request fails
        the new REFRESH_TOKEN can be used one other time to renew the ACCESS_TOKEN

        :retrun: compiled request header with an access_token
        :rtype: dict
        """
        supported_oauth_flows = self.check_oauth_ready()

        # Unsupported flow
        if not supported_oauth_flows[OAUTH_SUPPORTED]:
            err_msg = f"Application does not support OAuth authentication."
            LOG.error(err_msg)
            raise IntegrationError(err_msg)

        # Refresh_token flow
        if supported_oauth_flows[FLOW_REFRESH_TOKEN]:
            LOG.info(f"REFRESH_TOKEN detected. Fetching new ACCESS_TOKEN and possibly a REFRESH_TOKEN")
            # refresh-token is removed as this will be replaced later on successful authentication
            # this is to make sure that the existing refresh-toke is not used on retry
            _auth_specific_attributes = {
                AUTH_TYPE   : REFRESH_TOKEN,
                TOKEN_VALUE : self._oauth_inputs.pop(REFRESH_TOKEN),
                GRANT_TYPE  : REFRESH_GRANT_TYPE}

        # Authorization Flow
        elif supported_oauth_flows[FLOW_AUTHORIZATION]:
            # authorization-code is removed as this can not be reused. If the endpoint returns a
            # refresh-token, that is added back later, thereby changing the flow from `authorization`
            # to `refresh_token`. Which can later be used to renew access_token
            LOG.info(f"CODE detected. Fetching new ACCESS_TOKEN and possibly a REFRESH_TOKEN")
            _auth_specific_attributes = {
                AUTH_TYPE   : CODE,
                TOKEN_VALUE : self._oauth_inputs.pop(CODE),
                GRANT_TYPE  : ACCESS_GRANT_TYPE}

        # Client-Credentials Flow
        elif supported_oauth_flows[FLOW_CLIENT_CREDENTIALS]:
            # `Client-Credentials` flow does not alter the flow of authentication unless the endpoint returns
            # a `refresh-token` back. Therefore, once `Client-Credentials` flow is used, the application will
            # always follow the Client-Credentials flow.
            LOG.info(f"Client-Credentials detected. Fetching new ACCESS_TOKEN and possibly a REFRESH_TOKEN")
            _auth_specific_attributes = {GRANT_TYPE : CLIENT_CREDENTIALS_GRANT_TYPE}

        # Access_token flow
        elif supported_oauth_flows[FLOW_ACCESS_TOKEN]:
            LOG.info(f"ACCESS_TOKEN detected. Skipping token refresh mechanism.")
            if not self._oauth_inputs.get(TOKEN_TYPE):
                LOG.warning(f"{TOKEN_TYPE} not specified. ACCESS_TOKEN cannot be used without \
                    a {TOKEN_TYPE}. Using default token type : {DEFAULT_TOKEN_TYPE}")
                self._oauth_inputs[TOKEN_TYPE] = DEFAULT_TOKEN_TYPE
            return self._compile_headers()

        # Selecting and adding parameters only required for authentication from self._oauth_inputs
        _auth_specific_attributes.update({
            _each_key : self._oauth_inputs.get(_each_key) for _each_key in [
                TOKEN_URL, CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, SCOPE]})

        # Overriding GRANT_TYPE if specified by user
        if self._oauth_inputs.get(GRANT_TYPE):
            _auth_specific_attributes[GRANT_TYPE] = self._oauth_inputs[GRANT_TYPE]

        response = self.fetch_renew_tokens(**_auth_specific_attributes)

        if self._process_endpoint_response(response):
            return self._compile_headers()


    def fetch_renew_tokens(self, token_url:str, client_id:str, token_value:str=None, auth_type:str=None,
        client_secret:str=None, grant_type:str=None, redirect_uri:str=None, scope:str=None,
        content_type:dict=DEFAULT_AUTH_CONTENT_TYPE, additional_headers:dict={},
        additional_attributes:dict={}) -> dict:
        """
        Retrieves or extends access tokens through a POST request to the designated token_url. In addition
        to the mandatory parameters, supplementary ones are included if provided.

        :param token_url: The URL where the token request should be sent.
        :type token_url: str
        :param client_id: The client ID used for authentication.
        :type client_id: str
        :param token_value: (Optional) The token value (e.g., code or refresh token) if required by the
            authentication method.
        :type token_value: str
        :param auth_type: (Optional) The type of authentication (e.g., 'Bearer' for OAuth).
        :type auth_type: str
        :param client_secret: (Optional) The client secret used for authentication if required.
        :type client_secret: str
        :param grant_type: (Optional) The type of grant being requested if applicable.
        :type grant_type: str
        :param redirect_uri: (Optional) The redirect URI if applicable.
        :type redirect_uri: str
        :param scope: (Optional) The scope of the access request if applicable.
        :type scope: str
        :param content_type: (Optional) The content type of the request body (default is 
            DEFAULT_AUTH_CONTENT_TYPE).
        :type content_type: str
        :param additional_headers: (Optional) Additional headers to include in the request.
        :type additional_headers: dict
        :param additional_attributes: (Optional) Additional attributes to include in the request body.
        :type additional_attributes: dict
        :return: response from the token request.
        :rtype: dict
        """
        headers = {
            CONTENT_TYPE : content_type}

        data = {
            CLIENT_ID : client_id}

        # AUTH_TYPE (optional)
        if token_value:
            data.update({auth_type : token_value})

        # CLIENT_SECRET (optional)
        if client_secret:
            data.update({CLIENT_SECRET : client_secret})

        # GRANT_TYPE (optional)
        if grant_type:
            data.update({GRANT_TYPE : grant_type})

        # SCOPE (optional)
        if scope:
            data.update({SCOPE : scope})

        # REDIRECT_URI (optional)
        if redirect_uri:
            data.update({REDIRECT_URI : redirect_uri})

        # Adding any additional attributes to the request body, if required
        if additional_attributes:
            data.update(additional_attributes)

        # Adding any additional headers to the request body, if required
        if additional_headers:
            headers.update(additional_headers)

        response = self.rc.execute(
            OAUTH_REQUEST_METHOD,
            url=token_url,
            headers=headers,
            data=data,
            **self._retry_options)

        return response

    def show_tokens(self) -> dict:
        """
        :return: ACCESS_TOKEN, REFRESH_TOKEN, TOKEN_TYPE, EXPIRES_IN
        :rtype: dict
        """
        return {
            ACCESS_TOKEN  : self._oauth_inputs.get(ACCESS_TOKEN),
            REFRESH_TOKEN : self._oauth_inputs.get(REFRESH_TOKEN),
            TOKEN_TYPE    : self._oauth_inputs.get(TOKEN_TYPE),
            EXPIRES_IN    : self._oauth_inputs.get(EXPIRES_IN)}

"""
   C L I E N T   S I D E   A U T H E N T I C A T I O N
   - - - - - -   - - - -   - - - - - - - - - - - - - -
"""


FILE_TYPE_KEY = ".key"
FILE_TYPE_CSR = ".csr"
FILE_TYPE_PEM = ".pem"
CLIENT_AUTH_CERT = "client_auth_cert"
CLIENT_AUTH_KEY  = "client_auth_key"
CLIENT_AUTH_PEM  = "client_auth_pem"

def check_certificates(cert_properties:dict) -> None:
    """
    Checks to see if the application is Client-Side Authentication compliant. In other
    words, checks to see if any of the cert_properties have been populated.

    :param cert_properties: Contents of certificates
    :type cert_properties: dict
    :return: True if compliant else False
    :rtype: bool
    """
    # Creating .csr certificate and key using the values provided as text
    if cert_properties.get(CLIENT_AUTH_CERT) and cert_properties.get(CLIENT_AUTH_KEY):
        return True
    # Creating pem certificate and key using the values provided as text
    if cert_properties.get(CLIENT_AUTH_PEM):
        return True
    return False
    
    
def add_certificates(cert_properties:dict, certs_path:dict) -> tuple:
    """
    Checks if certificates have been provided as string values to the cert_properties argument. if yes, safely
    creates cert files in a temp directory and keeps a track of their location. If not, simply returns None.
    Two types of certificates can be created : CRT - KEY pair cert or a PEM cert. 

    Format:
    -------
        {"client_auth_crt" : "
                        -----BEGIN CERTIFICATE-----
                        MIIEezCCA2OgAwIBAgICG8AwDQY
                        bHftonwhOMIF+ik47Y2VqkqGOGF
                        10sAfVjlDqOz95HuMnMQ+gTGmok
                        -----END CERTIFICATE-----",

        "client_auth_pem" : "
                        -----BEGIN CERTIFICATE-----
                        MIIEezCCA2OgAwIBAgICG8AwDQY
                        bHftonwhOMIF+ik47Y2VqkqGOGF
                        10sAfVjlDqOz95HuMnMQ+gTGmok
                        -----END CERTIFICATE-----"}

    Args:
    -----
        cert_properties  <dict> : Can only have 3 possible keys -> client_auth_cert, client_auth_key and 
                                  client_auth_pem. Their respective values are teh certificates themselves,
                                  provided in a str format. 

        certs_path       <dict> : This placeholder is used to hold all certificate location during the life
                                  span of the application. This is later used to clear all created certificates.

    Returns:
    --------
        <tuple> : (.crt, .key) path to .crt and .key files in a tuple
           or
         <str>  : path to .pem file
           or 
          None  : No certificates created as none were provided
    
    """
    # Creating .csr certificate and key using the values provided as text
    if cert_properties.get(CLIENT_AUTH_CERT) and cert_properties.get(CLIENT_AUTH_KEY):
        prepare_certificates(cert_properties.get(CLIENT_AUTH_CERT), CLIENT_AUTH_CERT, FILE_TYPE_CSR, certs_path)
        prepare_certificates(cert_properties.get(CLIENT_AUTH_KEY) , CLIENT_AUTH_KEY , FILE_TYPE_KEY, certs_path)
        return (certs_path.get(CLIENT_AUTH_CERT).get("file"), certs_path.get(CLIENT_AUTH_KEY).get("file"))

    # Creating pem certificate and key using the values provided as text
    if cert_properties.get(CLIENT_AUTH_PEM):
        prepare_certificates(cert_properties.get(CLIENT_AUTH_PEM), CLIENT_AUTH_PEM, FILE_TYPE_PEM, certs_path)
        return certs_path.get(CLIENT_AUTH_PEM).get("file")
    return None



def prepare_certificates(cert_content:str, cert_name:str, cert_type:str, certs_path:dict) -> bool:

    """
    A wrapper function that checks if the provided certificate type is of the supported standard.
    If yes, creates the certificates and writes the location information to certs_path dictionary.
    
    Args:
    -----
        cert_content <str> : Certificate contents in string format
        cert_name    <str> : Certificate name
        cert_type    <str> : Certificate type. Supported types -> csr, key, pem
        certs_path  <dict> : This placeholder that holds all certificate location during the life
                             span of the application.

    Raises:
    -------
        ValueError: Raised when an invalid file type is provided.

    Returns:
    --------
        <bool> : True when a certificate is successfully created.
    """

    # Checks for valid file type
    if cert_type not in [FILE_TYPE_CSR, FILE_TYPE_KEY, FILE_TYPE_PEM]:
        raise ValueError(f"Invalid file type provided: {cert_type}")

    # The certificate content is unicode encoded before being written to the certificate
    _file_path, _file_dir = write_to_tmp_file(cert_content.encode("utf-8"), tmp_file_name=cert_name+cert_type)

    # updates certs_path to keep track of the file. Need not be returned as certs_path is passed by reference
    certs_path[cert_name] = {
        "file" : _file_path,
        "dir"  : _file_dir}

    return True


def delete_certificates(certs_path : dict) -> bool:
    """
    Clears all certificates available in certs_path variable. Returns True when successfully clears
    all certs_path contents, i.e. deletes all values in certificate directory. Else returns False.
    The function will also return True if there are no contents in certs_path.

    Args:
    -----
        certs_path <dict> : This placeholder that holds all certificate location during the life
                            span of the application.

    Raises:
    -------
        ValueError: Raised when file path provided is invalid.

    Returns:
    --------
        <bool> : True if all the contents are cleared.
    """
    LOG.info("Deleting all Client-side Authentication Certificates")
    if len(certs_path) == 0:
        LOG.info("Certificate path is empty")
        return True

    deleted_files = []
    for _file in certs_path:
        _file_dir = certs_path[_file].get("dir")
        # Deleting all contents in directory
        if _file_dir and os.path.isdir(_file_dir):
            shutil.rmtree(_file_dir)
            deleted_files.append(_file)
        else:
            raise ValueError(f"Invalid file path provided: {_file_dir}")

    for _file in deleted_files:
        del certs_path[_file]

    if len(certs_path) == 0:
        return True
    return False


"""
    J S O N   W E B   T O K E N   A U T H E N T I C A T I O N   (JWT)
    - - - -   - - -   - - - - -   - - - - - - - - - - - - - -    ---
"""


JWT_KEY = "key"
JWT_TOKEN = "token"
JWT_HEADERS = HEADERS
JWT_PAYLOAD = "payload"
JWT_ALGORITHM = "algorithm"
JWT_TOKEN_TYPE = "token_type"
DEFAULT_JWT_ENCRYPTION_ALGORITHM = "HS256"

class JWTHandler:
    def __init__(self, jwt_properties):
        """
        JWTHandler is responsible for handling JSON Web Tokens (JWTs). It provides methods and
        functionality related to the creation, compilation, and manipulation of JWTs. It takes
        several optional parameters to customize the behavior of the JWT handling. 

        JWT based authentication can be performed in 2 ways:

        1. This application can function with a predefined jwt token. A fully generated JWT 
        token can be directly provided, and the application will automatically form the REST
        headers required for a request.
        
        2. This application can generate a jwt token. For it to do so, it requires certain 
        parameters which can be provided as json string or line separated format (similar to
        REST body/header/cookies). The function checks to see if the required parameters are
        provided and compiles a JWT token using said parameters.

        The constructor initializes the instance variable _jwt_properties as a dictionary that holds
        the JWT properties. The JWTHandler class provides various methods and functionalities for
        working with JWTs. Overall, the JWTHandler class encapsulates the logic and properties
        required to handle JWTs, allowing for easy manipulation, compilation, and customization
        of JWTs in a convenient manner.

        Args:
        ----
        JWT_TOKEN      (optional,  <str>): Represents an existing JWT token. If provided, it can be used for further processing.
        JWT_HEADERS    (optional, <dict>): headers of the JWT, contains metadata about the token.
        JWT_PAYLOAD    (optional, <dict>): payload of the JWT, contains the data to be included in the token.
        JWT_KEY        (optional,  <str>): key used for signing the JWT.
        JWT_token_type (optional,  <str>): type of the JWT token. It has a default value of DEFAULT_TOKEN_TYPE.
        JWT_algorithm  (optional,  <str>): encryption algorithm used for encoding the JWT. It has a default value of
                                       DEFAULT_JWT_ENCRYPTION_ALGORITHM.
        """

        self._jwt_properties = {
            JWT_KEY        : jwt_properties[JWT_KEY] if jwt_properties.get(JWT_KEY) else None,
            JWT_TOKEN      : jwt_properties[JWT_TOKEN] if jwt_properties.get(JWT_TOKEN) else None,
            JWT_HEADERS    : jwt_properties[JWT_HEADERS] if jwt_properties.get(JWT_HEADERS) else {},
            JWT_PAYLOAD    : jwt_properties[JWT_PAYLOAD] if jwt_properties.get(JWT_PAYLOAD) else {},
            JWT_TOKEN_TYPE : jwt_properties[JWT_TOKEN_TYPE] if jwt_properties.get(JWT_TOKEN_TYPE) else DEFAULT_TOKEN_TYPE,
            JWT_ALGORITHM  : jwt_properties[JWT_ALGORITHM] if jwt_properties.get(JWT_ALGORITHM) else DEFAULT_JWT_ENCRYPTION_ALGORITHM}


    def _compile_jwt_token(self) -> dict:
        """
        The function is a private method that compiles a JSON Web Token (JWT).
        It takes no arguments and returns a boolean value. Upon invocation, the function logs an
        informational message stating that the JWT token is being compiled. It then proceeds to
        encode the JWT using the specified properties. The function accesses the _jwt_properties
        dictionary, which is an instance variable of the class containing this method. 

        Returns:
        -------
            <dict> : REST request headers with jwt tokens baked into it
        """
        LOG.info("Compiling a JWT token using the provided parameters")
        self._jwt_properties[JWT_TOKEN] = jwt.encode(
            self._jwt_properties.get(JWT_PAYLOAD),
            key=self._jwt_properties.get(JWT_KEY),
            headers=self._jwt_properties.get(JWT_HEADERS),
            algorithm=self._jwt_properties.get(JWT_ALGORITHM))
        return self._compile_headers()


    def _compile_headers(self) -> dict:
        """
        This is a private method that compiles the headers for a JSON Web Token (JWT). It takes no arguments
        and returns a dictionary containing the compiled headers. Upon invocation, the function logs an
        informational message stating that the JWT headers are being compiled. The function retrieves the JWT
        token type and token from the `_jwt_properties` dictionary, using the keys `JWT_TOKEN_TYPE` and
        `JWT_TOKEN` respectively. It then creates a dictionary with a single key-value pair, where the key is
        `AUTHORIZATION_KEY` (presumably representing the authorization header) and the value is a string
        concatenation of the token type and token obtained from the `_jwt_properties` dictionary. The resulting
        dictionary represents the compiled headers for the JWT.

        Returns:
        -------
            <dict> : REST request headers with JWT tokens baked into it

        Note: The function assumes the presence of the necessary keys (`JWT_TOKEN_TYPE` and `JWT_TOKEN`) in the
        `_jwt_properties` dictionary for successful header compilation. The values for these keys are expected
        to be strings.
        """
        LOG.info("Adding JWT access_token by means of `Authorization` parameter to request header")
        return {AUTHORIZATION_KEY : f"{self._jwt_properties.get(JWT_TOKEN_TYPE)} {self._jwt_properties.get(JWT_TOKEN)}"}


    def check_jwt_ready(self) -> bool:
        """
        Responsible for determining if the application is JWT ready. An application needs the following
        parameters to compile a valid JWT token. Failing to provide these would simply return False
        stating that the application does not have a valid JWT token, nor can it compile one.
        
        Returns:
        -------
            <bool> : True if JWT authentication ready, False if not.
        """
        LOG.info("Checking to see if a valid JWT token was provided \
            or appropriate JWT attributes required for token generation is provided")
        if self._jwt_properties.get(JWT_TOKEN) or self._jwt_properties.get(JWT_KEY):
            return True
        return False


    def add_jwt_headers(self, rest_properties:dict) -> dict:
        """
        JWT based authentication can be performed in 2 ways:
        
        1. This application can function with a predefined jwt token. A fully generated JWT 
        token can be directly provided, and the application will automatically form the REST
        headers required for a request.
        
        2. This application can generate a jwt token. For it to do so, it requires certain 
        parameters which can be provided as json string or line separated format (similar to
        REST body/header/cookies). The function checks to see if the required parameters are
        provided and compiles a JWT token using said parameters.
        
        Note: If neither of these are provided the application simply skips the process and
        directly performs the REST api call. To do so, it takes in the rest_headers and returns
        original headers untouched.
        
        Args:
        ----
            rest_properties <dict> : Rest request properties that contains request header

        Returns:
        --------
            <dict> : headers, with or without oauth generated credentials
        """
        jwt_headers = {}

        # Checking if application is JWT ready
        if self.check_jwt_ready():

            # Precompiled JWT TOKEN detected! compiling headers with this token
            if self._jwt_properties.get(JWT_TOKEN):
                LOG.info("A precompiled JWT TOKEN detected! Directly creating request header using this token")
                jwt_headers = self._compile_headers()

            # Compiling JWT tokens using provided JWT attributes
            elif self._jwt_properties.get(JWT_KEY):
                LOG.info("JWT token attributes detected. Creating a new JWT token")
                jwt_headers = self._compile_jwt_token()

        # If request_properties has no header section, creating a new header section and adding the compiled header
        if not rest_properties.get(HEADERS):
            LOG.info("No header section was detected. Creating new header section for the request and the compiled header")
            rest_properties[HEADERS] = jwt_headers

        # Checking if header already has ACCESS_TOKEN present
        elif self.check_jwt_ready() and AUTHORIZATION_KEY in rest_properties.get(HEADERS) and rest_properties[HEADERS][AUTHORIZATION_KEY]:
            raise IntegrationError(f"""Conflict detected!! Request header already has an `Authorization` parameter. Please resolve conflict
                                   by opting out of other authentication mechanisms or opt out of this process by not providing any values for
                                   JWT parameters""")
        # Updating headers with JWT token
        else:
            rest_properties[HEADERS].update(jwt_headers)

        return rest_properties
