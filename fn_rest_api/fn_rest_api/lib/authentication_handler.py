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

DEFAULT_AUTH_CONTENT_TYPE = "application/x-www-form-urlencoded"
REFRESH_GRANT_TYPE = "refresh_token"
ACCESS_GRANT_TYPE  = "authorization_code"

AUTH_URL = "auth_url"
TOKEN_URL = "token_url"
CODE  = "code"
STATE = "state"
SCOPE = "scope"
CLIENT_ID  = "client_id"
GRANT_TYPE = "grant_type"
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

def add_oauth_headers(oauth_client, rest_properties) -> dict:
    """
    This application can function without OAuth authentication process. For the
    application to perform OAuth authentication, it requires certain parameters. This
    function checks to see if the required parameters are provided and performs OAuth 
    authentication. If they aren't provided, it simply skips the process and directly
    performs the REST api call. To do so, it takes in the rest_headers and either adds
    oauth credentials/headers or skips and returns original headers untouched

    Returns:
    --------
        <dict> : headers, with or without oauth generated credentials
    """
    if oauth_client.check_oauth_ready():
        LOG.info("OAuth properties detected!")
        oauth_headers = oauth_client.authenticate()
        if rest_properties.get(HEADERS):
            rest_properties[HEADERS].update(oauth_headers)
        else:
            rest_properties[HEADERS] = oauth_headers
    return rest_properties


class OAuth2Authorization():

    def __init__(self, rc, oauth_options):

        self.rc = rc
        LOG.debug("Configuration values")
        LOG.debug(json.dumps(oauth_options, indent=2))

        self._oauth_properties = {
            TOKEN_URL     : validate_url(oauth_options.get(TOKEN_URL)),
            CLIENT_ID     : oauth_options.get(CLIENT_ID),
            CLIENT_SECRET : oauth_options.get(CLIENT_SECRET),
            REDIRECT_URI  : oauth_options.get(REDIRECT_URI),
            SCOPE         : oauth_options.get(SCOPE),
            CODE          : oauth_options.get(CODE),
            ACCESS_TOKEN  : oauth_options.get(ACCESS_TOKEN),
            REFRESH_TOKEN : oauth_options.get(REFRESH_TOKEN),
            TOKEN_TYPE    : oauth_options.get(TOKEN_TYPE, DEFAULT_TOKEN_TYPE),
            EXPIRES_IN    : oauth_options.get(EXPIRES_IN),
            ADDITIONAL_HEADERS    : oauth_options.get(ADDITIONAL_HEADERS, {}),
            ADDITIONAL_ATTRIBUTES : oauth_options.get(ADDITIONAL_ATTRIBUTES, {})}


    def _compile_headers(self) -> dict:
        """
        Create headers needed for authentication/authorization, overriding the default ones if needed.

        :param headers: Dictionary containing the ``Authorization`` header
        :type headers: dict
        """
        return {AUTHORIZATION_KEY : f"{self._oauth_properties.get(TOKEN_TYPE)} {self._oauth_properties.get(ACCESS_TOKEN)}"}


    def _process_endpoint_response(self, response) -> bool:
        """
        Processes response received from the endpoint. The values received could vary from endpoint to endpoint. This allows
        the client to handle such varied responses.

        Args:
        -----
            response <requests.response> : response received from endpoint

        Raises:
        -------
            __IntegrationError__ : Status code > 300. Invalid REFRESH_TOKEN supplied.
               __ValueError__    : ACCESS_TOKEN not found in response.
        
        Returns:
        --------
            <bool> : True when all required parameters are found in response

        """
        if response.status_code >= 300:
            raise IntegrationError(f"Unable to refresh ACCESS_TOKEN. Please check or renew your REFRESH_TOKEN. {response.content}")
        
        response = response.json()

        # If REFRESH_TOKEN available in response, updates existing REFRESH_TOKEN to the current one.
        # Else retains existing TOKEN provided in the constructor.
        if REFRESH_TOKEN in response:
            self._oauth_properties[REFRESH_TOKEN] = response.get(REFRESH_TOKEN)
        
        # If TOKEN_TYPE not in response, using DEFAULT_TOKEN_TYPE specified while reading inputs in oauth_handler's constructor
        if TOKEN_TYPE in response:
            self._oauth_properties[TOKEN_TYPE] = response.get(TOKEN_TYPE)
        else:
            LOG.warning(f"No {TOKEN_TYPE} detected in response. Using DEFAULT_TOKEN_TYPE : {DEFAULT_TOKEN_TYPE}")
            
        if EXPIRES_IN in response:
            self._oauth_properties[EXPIRES_IN] = time.time() + int(response.get(EXPIRES_IN))

        if ACCESS_TOKEN in response:
            self._oauth_properties[ACCESS_TOKEN] = response.get(ACCESS_TOKEN)
        else:
            raise ValueError(f"Did not receive ACCESS_TOKEN. Received response : {json.dumps(response, indent=2)}")

        return True


    def _update_tokens(self) -> bool:
        """
        Institutes a request for a new access token using REFRESH_TOKEN.
        """
        LOG.info(f"Refreshing ACCESS_TOKEN using REFRESH_TOKEN")

        if not self._oauth_properties.get(REFRESH_TOKEN):
            raise ValueError("In order to refresh tokens, REFRESH_TOKEN is required and cannot be None")

        response = self.fetch_renew_tokens(
            token_url=self._oauth_properties.get(TOKEN_URL),
            auth_type=REFRESH_TOKEN,
            code_or_refresh_token=self._oauth_properties.get(REFRESH_TOKEN),
            client_id=self._oauth_properties.get(CLIENT_ID),
            client_secret=self._oauth_properties.get(CLIENT_SECRET),
            grant_type=REFRESH_GRANT_TYPE,
            redirect_uri=self._oauth_properties.get(REDIRECT_URI),
            scope=self._oauth_properties.get(SCOPE),
            additional_headers=self._oauth_properties.get(ADDITIONAL_HEADERS, {}),
            additional_attributes=self._oauth_properties.get(ADDITIONAL_ATTRIBUTES, {}))

        return self._process_endpoint_response(response)


    def _get_tokens(self) -> bool:
        """
        Institutes a request for a new access token by exchanging CODE for the tokens
        """
        LOG.info(f"Exchanging CODE for ACCESS_TOKEN and REFRESH_TOKEN")
        
        if not self._oauth_properties.get(CODE):
            raise ValueError(f"In order to fetch tokens, CODE is required and cannot be None")

        response = self.fetch_renew_tokens(
            token_url=self._oauth_properties.get(TOKEN_URL),
            auth_type=CODE,
            code_or_refresh_token=self._oauth_properties.get(CODE),
            client_id=self._oauth_properties.get(CLIENT_ID),
            client_secret=self._oauth_properties.get(CLIENT_SECRET),
            grant_type=ACCESS_GRANT_TYPE,
            redirect_uri=self._oauth_properties.get(REDIRECT_URI),
            scope=self._oauth_properties.get(SCOPE),
            additional_headers=self._oauth_properties.get(ADDITIONAL_HEADERS, {}),
            additional_attributes=self._oauth_properties.get(ADDITIONAL_ATTRIBUTES, {}))

        return self._process_endpoint_response(response)


    def check_oauth_ready(self):
        """
        Responsible for determining if the application is OAuth ready. An application needs the following
        parameters to perform OAuth authentication. Failing to provide these would simply return False
        stating that the application is not OAuth ready.
        
            - TOKEN_URL
            - CLIENT_ID
            - CODE (or) ACCESS_TOKEN (or) REFRESH_TOKEN

        Returns:
        --------
            <bool> : True/False depending on the application being OAuth ready.
        """
        if self._oauth_properties.get(ACCESS_TOKEN):
            return True

        if (    (self._oauth_properties.get(CODE) or self._oauth_properties.get(REFRESH_TOKEN))
             and
                (self._oauth_properties.get(TOKEN_URL) and self._oauth_properties.get(CLIENT_ID))
           ):
            return True

        return False


    def force_refresh_tokens(self):
        """
        Forces the client to fetch fresh ACCESS_TOKEN and REFRESH_TOKEN.
        
        RAISES:
        -------
            __IntegrationError__ : REFRESH_TOKEN is either unavailable or invalid

        RETURNS:
        --------
            <bool> : _description_
        """
        LOG.info(f"Forcing ACCESS_TOKEN to be refreshed using REFRESH_TOKEN")
        if not self._oauth_properties.get(REFRESH_TOKEN):
            msg = f"Cannot refresh ACCESS_TOKEN. REFRESH_TOKEN is invalid: {self._oauth_properties.get(REFRESH_TOKEN)}"
            LOG.error(msg)
            raise IntegrationError(msg)

        if not self._update_tokens():
            raise IntegrationError(f"Unable to refresh tokens. Please check REFRESH_TOKEN {self._oauth_properties.get(REFRESH_TOKEN)}")
        return True


    def show_tokens(self) -> dict:
        """
        Returns:
            dict: ACCESS_TOKEN, REFRESH_TOKEN, TOKEN_TYPE, EXPIRES_IN
        """
        return {
            ACCESS_TOKEN  : self._oauth_properties.get(ACCESS_TOKEN),
            REFRESH_TOKEN : self._oauth_properties.get(REFRESH_TOKEN),
            TOKEN_TYPE    : self._oauth_properties.get(TOKEN_TYPE),
            EXPIRES_IN    : self._oauth_properties.get(EXPIRES_IN)}


    def authenticate(self) -> dict:
        """
            If ACCESS_TOKEN is directly provided, the oauth_handler should automatically use the token without having to refresh it.
        This is particularly used when an application is provided direct access without having to perform the entire OAuth
        authorization and authentication process. When an ACCESS_TOKEN is directly provided, its TOKEN_TYPE must also be specified.
        """
        if self._oauth_properties.get(ACCESS_TOKEN):
            LOG.info(f"ACCESS_TOKEN detected. Skipping token refresh mechanism.")
            if not self._oauth_properties.get(TOKEN_TYPE):
                LOG.warning(f"{TOKEN_TYPE} not specified. ACCESS_TOKEN cannot be used without a {TOKEN_TYPE}. Using default token type : {DEFAULT_TOKEN_TYPE}")
                self._oauth_properties[TOKEN_TYPE] = DEFAULT_TOKEN_TYPE

            elif self._oauth_properties.get(EXPIRES_IN):
                if self._oauth_properties.get(EXPIRES_IN) <= time.time():
                    # Validity of REFRESH_TOKEN has ended before current time.
                    LOG.info(f"Updating expired ACCESS_TOKEN")
                    if not self._update_tokens():
                        raise IntegrationError("Unable to refresh tokens")
                else:
                    # Expiry time of REFRESH_TOKEN is greater than current time. Hence valid.
                    LOG.info(f"ACCESS_TOKEN seem valid and well within expiration date {self._oauth_properties.get(EXPIRES_IN)}")
            else:
                # No expiration time was specified. ACCESS_TOKEN is used without checking validity.
                LOG.warning(f"ACCESS_TOKEN validity unverified. No {EXPIRES_IN} property available to check validity")

        # If REFRESH_TOKEN is specified without ACCESS_TOKEN, handler automatically fetches all required information for authentication
        elif self._oauth_properties.get(REFRESH_TOKEN):
            self.force_refresh_tokens()

        # If CODE is specified. ACCESS_TOKEN and REFRESH_TOKEN is fetched in exchange for CODE
        elif self._oauth_properties.get(CODE):
            LOG.info(f"CODE detected. No REFRESH_TOKEN OR ACCESS_TOKEN present.")
            if not self._get_tokens():
                raise IntegrationError(f"Unable to exchange CODE for REFRESH_TOKEN and ACCESS_TOKEN")

        # Failing execution as none of the required parameters are specified.
        else:
            err_msg = f"No ACCESS_TOKEN, REFRESH_TOKEN or CODE specified."
            LOG.error(err_msg)
            raise KeyError(err_msg)

        return self._compile_headers()


    def fetch_renew_tokens(self, token_url:str, auth_type:str, code_or_refresh_token:str, client_id:str,
            client_secret:str=None, grant_type:str=None, redirect_uri:str=None, scope:str=None,
            content_type:dict=DEFAULT_AUTH_CONTENT_TYPE, additional_headers:dict={},
            additional_attributes:dict={}) -> dict:
        """
        Refresh ACCESS_TOKEN using REFRESH_TOKEN. Both ACCESS_TOKEN and REFRESH_TOKEN are
        time-bound. ACCESS_TOKENS usually have a significantly shorter lifespan than REFRESH_TOKEN.
        When an ACCESS_TOKEN expires, it can be renewed using a REFRESH_TOKEN, doing so would also
        usually extend the lifespan of the REFRESH_TOKEN itself.
        
        Note: Using REFRESH_TOKENS usually generates new ACCESS_TOKEN. But the life span of the
              same REFRESH_TOKEN is extended. Therefore the same REFRESH_TOKEN can be used to
              generate new ACCESS_TOKEN

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
                REFRESH_TOKEN
                EXPIRES_IN
                REFRESH_TOKEN_EXPIRES_IN

        Using CODE to get ACCESS_TOKEN and REFRESH_TOKEN. CODE is a one off credential that
        can be exchanged for an ACCESS_TOKEN and REFRESH_TOKEN.

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
                REFRESH_TOKEN
                EXPIRES_IN
                REFRESH_TOKEN_EXPIRES_IN

        RAISES:
        -------
            __ValueError__ : Invalid authentication type provided.

        RETURNS:
        --------
            <response.response> : client endpoint response.
        """
        headers = {
            "Content-Type" : content_type}

        # Adding any additional headers to the request body, if required
        if additional_headers:
            headers.update(additional_headers)

        body = {
            CLIENT_ID : client_id}

        # AUTH_TYPE (required)
        if auth_type == CODE:
            body.update({CODE : code_or_refresh_token})
        elif auth_type == REFRESH_TOKEN:
            body.update({REFRESH_TOKEN : code_or_refresh_token})
        else:
            raise ValueError(f"Authentication Type has to be either {CODE} or {REFRESH_TOKEN}. {auth_type} is not a valid authentication type")

        # CLIENT_SECRET (optional)
        if client_secret:
            body.update({CLIENT_SECRET : client_secret})

        # GRANT_TYPE (optional)
        if grant_type:
            body.update({GRANT_TYPE : grant_type})
        elif auth_type == CODE:
            body.update({GRANT_TYPE : ACCESS_GRANT_TYPE})
        elif auth_type == REFRESH_TOKEN:
            body.update({GRANT_TYPE : REFRESH_GRANT_TYPE})
        # else: 
        #   Skipping GRANT_TYPE all-together

        # SCOPE (optional)
        if scope:
            body.update({SCOPE : scope})

        # REDIRECT_URI (optional)
        if redirect_uri:
            body.update({REDIRECT_URI : redirect_uri})

        # Adding any additional attributes to the request body, if required
        if additional_attributes:
            body.update(additional_attributes)
        
        LOG.debug(f"Response Header : {json.dumps(headers, indent=2)}")
        LOG.debug(f"Response Body : {json.dumps(body, indent=2)}")

        response = self.rc.execute(
            "post",
            url=token_url,
            headers=headers,
            data=body,
            callback=lambda resp: resp)

        return response


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
