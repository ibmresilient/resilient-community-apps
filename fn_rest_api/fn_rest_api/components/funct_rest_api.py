# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010 to 2023. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

"""AppFunction implementation """
import json
from logging import getLogger

from requests.exceptions import HTTPError
from resilient_lib import render, validate_fields, IntegrationError
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult

from fn_rest_api.lib.helper import make_rest_call, dedup_dict, render_dict_components
from fn_rest_api.lib import authentication_handler

FN_NAME = "rest_api"
PACKAGE_NAME = "fn_rest_api"

RETRY_TRIES_DEFAULT = 1
RETRY_DELAY_DEFAULT = 1
RETRY_BKOFF_DEFAULT = 1

LOG = getLogger(__name__)

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'rest_api'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    def _status_and_log_message(self, msg):
        """
        Logs a message and returns a status message.

        :param msg: The message to be logged and used for the status message.
        :type msg: str
        :return: A status message based on the input message.
        :rtype: status_message
        """
        LOG.info(msg)
        return self.status_message(msg)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        The function parameters determine the type of call, the URL, and optionally the headers
        and body. Users can also specify request headers, parameters, and body content for
        different types of requests. It also supports various authentication methods, including
        basic authentication, OAuth, API keys, and client side authentication. The results include
        the text or structured (JSON) result from the web service, and additional information
        including the elapsed time.
        
        Function: This function calls a REST web service. It supports the standard REST methods:
            GET, HEAD, POST, PUT, DELETE, OPTIONS, and PATCH.

        :param fn_inputs.rest_api_method: The HTTP method (e.g., GET, POST, PUT) to use for the API call.
        :type fn_inputs.rest_api_method: str
        :param fn_inputs.rest_api_url: URL/Endpoint to execute request against
        :type fn_inputs.rest_api_url: str
        :param fn_inputs.rest_api_verify: Either a boolean, in which case it controls whether
            requests verifies  the server's TLS certificate, or a string, in which case it must be a path
            to a CA bundle to use. Matches ``verify`` parameter of `resilient-lib.request_common.execute
            <https://github.com/ibmresilient/resilient-python-api/blob/main/resilient-lib/resilient_lib/components/requests_common.py>`_.

            Example:

            .. code-block::

                ... # some other input params
                verify=<path/to/CA/bundle/to/use> or True

            .. note::
                The value held in the app's config will be overwritten if a value is passed in by the call
                to ``execute``.
        :type fn_inputs.rest_api_verify: bool or str.
        :param fn_inputs.rest_api_timeout: (Optional) Number of seconds to wait for the server to send data
            before sending a float or a timeout tuple (connect timeout, read timeout)
        :type fn_inputs.rest_api_timeout: float or tuple
        :param fn_inputs.rest_api_allowed_status_codes: (Optional) A list of HTTP status codes that are
            considered successful. A list of allowed status codes can be passed in as string. The parameter
            defaults to None and in that case, all status codes < 300 is considered as acceptable response.

            Example:

            .. code-block::

                ... # some other input params
                inputs.allowed_status_codes = "200, 201, 202"
                #                     (or)
                inputs.allowed_status_codes = None
        :type fn_inputs.rest_api_allowed_status_codes: str. Default:  ``None``.
        :param fn_inputs.rest_api_body: (Optional) The request body data for the REST API call. The body is to be
        :type fn_inputs.rest_api_body: json-string format.

            Example:

            .. code-block::

                ... # some other input params
                inputs.rest_api_body = "" {
                   "name"     : "user1",
                   "password" : "p@ssword1",
                   "role"     : "admin",
                   "content"  : { 
                      "site_url" : "www.example.com",
                      "users"    : ["user1", "user2"]
                      }
                  } ""
        :param fn_inputs.rest_api_query_parameters: The query parameters to include in the REST API call. Input
            format matches ``fn_inputs.rest_api_body``
        :type fn_inputs.rest_api_query_parameters: json-string format.
        :param fn_inputs.rest_api_cookies: (Optional) The cookies to include in the API request. Input
            format matches ``fn_inputs.rest_api_body``
        :type fn_inputs.rest_api_cookies: str
        :param fn_inputs.rest_api_headers: The HTTP headers to include in the API request. Input
            format matches ``fn_inputs.rest_api_body``
        :type fn_inputs.rest_api_headers: str
        :param fn_inputs.oauth_token_url: (Optional) The URL to obtain OAuth tokens. Default: ``None``
        :type fn_inputs.oauth_token_url: str
        :param fn_inputs.oauth_client_id: (Optional) The OAuth client ID for authentication. Default: ``None``
        :type fn_inputs.oauth_client_id: str
        :param fn_inputs.oauth_client_secret: (Optional) The OAuth client secret for authentication. Default: ``None``
        :type fn_inputs.oauth_client_secret: str
        :param fn_inputs.oauth_redirect_uri: (Optional) The OAuth redirect URI for the authentication flow. Default: ``None``
        :type fn_inputs.oauth_redirect_uri: str
        :param fn_inputs.oauth_scope: (Optional) The scope of access requested during OAuth authentication. Default: ``None``
        :type fn_inputs.oauth_scope: str
        :param fn_inputs.oauth_code: (Optional) The OAuth authorization code. Default: ``None``
        :type fn_inputs.oauth_code: str
        :param fn_inputs.oauth_access_token: (Optional) The OAuth access token. Default: ``None``
        :type fn_inputs.oauth_access_token: str
        :param fn_inputs.oauth_refresh_token: (Optional) The OAuth refresh token for token renewal. Default: ``None``
        :type fn_inputs.oauth_refresh_token: str
        :param fn_inputs.oauth_token_type: (Optional) The type of OAuth token (e.g., Bearer) for API authentication. Default: ``None``
        :type fn_inputs.oauth_token_type: str
        :param fn_inputs.client_auth_pem: (Optional) The contents of PEM file for client authentication. Default: ``None``
        :type fn_inputs.client_auth_pem: str
            Example:

            .. code-block::

            ... # some other input params
            inputs.client_auth_cert = ""
               Bag Attributes
                   friendlyName: Authentication certificate
                   localKeyID: 78 94 0E 86 8D 30 EC D3 90 C8 6A 69 0F XX XX XX XX
               Key Attributes: <No Attributes>
               -----BEGIN CERTIFICATE-----
               MIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDFo8xuU+xgNo7G
               9t6hyCRYC0imfYGlH8Huh6OrQ0qO6PnmV8GCGw4ZDHnhUqmS3xWhn5c3MWSXGS5E
               FEgCxB3Rdkim5Dfog6SCCFWIa4YAyv0rdgNLeRbQNTKyT14+inqWE+CLKvZ/T+56
               OEdDSh0RPCg+UxjyCnkSiMce+/8RT+FXK41q1iQZAREJGEpZJIizVYB+aW2caCdq
               PteGybdmFFeRIP/qbo0u17zc+Urj+MbuqYcEtx5YriF39+xRrReDbteSTnigQQP4
               7zQHgQkU+U6MOuFTICtqVBuH9LX8qCJAG+92FLseh6I4qg0gd1ilyTG8PnhKuBRi
               vkuz+SOtAgMBAAECggEAFkbnNQxamWGs6DpNT9j6V7412yZMZatVtaguR5CXJ9KU
               0GTV1+9qwGIKnt4tZPOmQYh2h+8WUn2xHFVY5I7seX6mo8EXmCq2cT21PmI4QYCf
               cNOKjYkEgwKBgAktKQorCoDvo5oiI89zpUhRHbJIlGWHuZFCCmEIQb4z+dUr72LL
               uhZP0s22aRkqXMzDblFYrS0H3p7clhqEsoD9DO9WsiQK/2G85nR+IZd9U0bQ7z/t
               7FOMkDbMPHkmkwAHlFC/UbS4XWJCZzrOoi6Zl/Cx4nFwvWyn7OtJfI/xAoGAdgat
               PtFt97+wPDuSdVIbXjArSSq9F22J/cpG+wOMIGdgtNfPbNJFRG7Q/Lc/eDMPB5Nw
               9O9YOnDFpqb8S+aE+4/Yfcxg4gGrKazXu+flYNhzpCTx3SpVawQCrUF3dE/2hbV+
               FbGVFPaJziRDeH3UA1+1q0/bRg1trxqkZtGSGukCgYAA7SWvZ3lGJ42tiFzoH4F5
               SfTZXQytCwyxXF6BIWTIXQBcCep5TrfOnYz4iEDwMdp4Qb/QhyjaUsIlo+JldquZ
               k76eXjwrXCwuR0dnwBEsgktWEL8tgCFL1KOACU6dLN2PvE1BOzz8gp1CySn0cpSQ
               Y20A9hExGKyHns4hW5KgvA==
               -----END CERTIFICATE-----
               ""
        :param fn_inputs.client_auth_key: (Optional) The contents of  private key for client authentication. Default: ``None``.
            Input format matches ``inputs.client_auth_pem``.
        :type fn_inputs.client_auth_key: str
        :param fn_inputs.client_auth_cert: (Optional) The contents of client certificate for authentication. Default: ``None``
            Input format matches ``inputs.client_auth_pem``.
        :type fn_inputs.client_auth_cert: str
        :param fn_inputs.jwt_token: (Optional) The JWT (JSON Web Token) for authentication. Default: ``None``
        :type fn_inputs.jwt_token: str
        :param fn_inputs.jwt_key: (Optional) The key used to sign or verify the JWT. Default: ``None``
        :type fn_inputs.jwt_key: str
        :param fn_inputs.jwt_headers: (Optional) The headers of the JWT. Default: ``None``
        :type fn_inputs.jwt_headers: str
        :param fn_inputs.jwt_payload: (Optional) The payload or claims of the JWT. Default: ``None``
        :type fn_inputs.jwt_payload: str
        :param fn_inputs.jwt_algorithm: (Optional) The encryption algorithm used for the JWT. Default: ``None``
        :type fn_inputs.jwt_algorithm: str

        """
        yield self.status_message(f"Starting App Function: '{FN_NAME}'")
        validate_fields([
            "rest_api_method",
            "rest_api_url",
            "rest_api_verify"
            ], fn_inputs)

        rest_options = rest_properties = oauth_properties = certs_path = {}

        # Exceptions are not raised for the following codes
        allowed_status_codes = getattr(fn_inputs, "rest_api_allowed_status_codes", None) # text

        # Get the function parameters:
        # Select, values: "GET", "HEAD", "POST", "PUT", "DELETE", "OPTIONS", "PATCH"
        rest_options = {
            "method"  : self.get_select_param(getattr(fn_inputs, "rest_api_method")),
            "url"     : getattr(fn_inputs, "rest_api_url"), # text
            "verify"  : getattr(fn_inputs, "rest_api_verify"), # boolean
            "timeout" : getattr(fn_inputs, "rest_api_timeout", 60)} # Default timeout to 60 seconds

        rest_properties = {
            "body"    : self.get_textarea_param(getattr(fn_inputs, "rest_api_body", None)), # textarea
            "headers" : self.get_textarea_param(getattr(fn_inputs, "rest_api_headers", None)), # textarea
            "cookies" : self.get_textarea_param(getattr(fn_inputs, "rest_api_cookies", None)), # textarea
            "params"  : self.get_textarea_param(getattr(fn_inputs, "rest_api_query_parameters", None))} # textarea

        # Properties required for OAuth Authentication
        oauth_properties = {
            authentication_handler.TOKEN_URL     : getattr(fn_inputs, "oauth_token_url", None),
            authentication_handler.CLIENT_ID     : getattr(fn_inputs, "oauth_client_id", None),
            authentication_handler.CLIENT_SECRET : getattr(fn_inputs, "oauth_client_secret", None),
            authentication_handler.REDIRECT_URI  : getattr(fn_inputs, "oauth_redirect_uri", None),
            authentication_handler.SCOPE         : getattr(fn_inputs, "oauth_scope", None),
            authentication_handler.CODE          : getattr(fn_inputs, "oauth_code", None),
            authentication_handler.ACCESS_TOKEN  : getattr(fn_inputs, "oauth_access_token", None),
            authentication_handler.REFRESH_TOKEN : getattr(fn_inputs, "oauth_refresh_token", None),
            authentication_handler.TOKEN_TYPE    : getattr(fn_inputs, "oauth_token_type", None)}

        # Properties required for JWT Authentication
        jwt_properties = {
            authentication_handler.JWT_TOKEN     : getattr(fn_inputs, "jwt_token", None),
            authentication_handler.JWT_KEY       : getattr(fn_inputs, "jwt_key", None),
            authentication_handler.JWT_HEADERS   : getattr(fn_inputs, "jwt_headers", None),
            authentication_handler.JWT_PAYLOAD   : getattr(fn_inputs, "jwt_payload", None),
            authentication_handler.JWT_ALGORITHM : getattr(fn_inputs, "jwt_algorithm", None) }

        # Properties required for Client-Side Authentication
        cert_properties = {
            authentication_handler.CLIENT_AUTH_CERT : getattr(fn_inputs, authentication_handler.CLIENT_AUTH_CERT, None),
            authentication_handler.CLIENT_AUTH_KEY  : getattr(fn_inputs, authentication_handler.CLIENT_AUTH_KEY, None),
            authentication_handler.CLIENT_AUTH_PEM  : getattr(fn_inputs, authentication_handler.CLIENT_AUTH_PEM, None)}

        LOG.info(f"REST Options : {json.dumps(rest_options, indent=2)}")

        # Rendering rest url with values from app.conf
        rest_options["url"] = render(rest_options["url"], self.options)

        # Rendering any OAuth property that has values from app.conf
        LOG.info("Rendering OAuth properties")
        for key, value in oauth_properties.items():
            if value:
                oauth_properties[key] = render(value, self.options)

        LOG.info("Rendering REST properties. If values contain SECRETS, they are incorporated.")
        yield self.status_message("Rendering REST properties")
        render_dict_components(rest_properties, self.options)

        LOG.info("Rendering JWT properties. If values contain SECRETS, they are incorporated.")
        yield self.status_message("Rendering JWT properties")
        render_dict_components(jwt_properties, self.options)

        # Converting allowed_status_codes to a list of integers
        allowed_status_codes = [int(x) for x in allowed_status_codes.split(",")] if allowed_status_codes else []

        # Initializing OAuth handler
        LOG.info("Initializing OAuth Client to handle Authentication")
        oauth_client     = authentication_handler.OAuth2Authorization(self.rc, oauth_properties)

        # Performing OAuth authentication if Oauth parameters are provided

        yield self._status_and_log_message("Checking if request is OAuth ready...")
        if oauth_client.check_oauth_ready():
            yield self.status_message("OAuth parameters detected, initializing authentication process..")
            rest_properties  = authentication_handler.add_oauth_headers(oauth_client, rest_properties)
            yield self.status_message("Successfully authenticated! ACCESS_TOKEN added to header")
        else:
            yield self._status_and_log_message("No Oauth parameters were detected. Skipping OAuth authentication")

        # Initializing JWT handler
        LOG.info("Initializing OAuth Client to handle Authentication")
        jwt_client       = authentication_handler.JWTHandler(jwt_properties)

        # Generating jwt headers if jwt attributes are provided
        yield self._status_and_log_message("Checking if request is JWT ready...")
        if jwt_client.check_jwt_ready():
            yield self.status_message("JWT parameters detected, initiating authentication process")
            rest_properties  = jwt_client.add_jwt_headers(rest_properties)
            yield self.status_message("Successfully authenticated! ACCESS_TOKEN added to header")
        else:
           yield self._status_and_log_message("No JWT parameters were detected. Skipping JWT authentication")


        # Generating certificates for client side authentication, if certificates are provided
        yield self._status_and_log_message("Checking if Client-Side Certificates have been provided ...")
        if authentication_handler.check_certificates(cert_properties):
            rest_properties["clientauth"] = authentication_handler.add_certificates(cert_properties, certs_path)
        else:
            yield self._status_and_log_message("No certificates were detected. Skipping Client-Side authentication")

        LOG.debug(f"Request Body : {json.dumps(rest_properties.get('body'), indent=2)}")

        try:
            yield self._status_and_log_message("Attempting call...")
            response = make_rest_call(
                self.opts, self.options, allowed_status_codes,
                **rest_options, **rest_properties)

        except (HTTPError, IntegrationError) as err:
            # If the error raised is either HTTPError or IntegrationError, checks to see if the request is
            # OAuth ready. If so, it is assumed that the ACCESS_TOKEN has expired, and so it attempts to
            # renew this by forcing the OAuth client to refresh its credentials, thereby generating new
            # headers.
            yield self._status_and_log_message(str(err))
            if oauth_client.check_oauth_ready():
                LOG.info("Request seems to be OAuth ready, attempting to refresh token")
                oauth_client.force_refresh_tokens()
                rest_properties = authentication_handler.add_oauth_headers(oauth_client, rest_properties)
                yield self._status_and_log_message("Retrying request with new header")
                response = make_rest_call(
                    self.opts, self.options, allowed_status_codes,
                    **rest_options, **rest_properties, **retry_properties)
            else:
                LOG.warning("Request is not OAuth ready. Raising exception")
                raise IntegrationError(str(err))

        yield self._status_and_log_message("Attempt Successful!")

        try:
            yield self._status_and_log_message("Attempting to JSON decode response")
            response_json = response.json()
            LOG.debug(json.dumps(response_json, indent=2))
        except:
            response_json = None

        # Formatting response
        results = {
            "ok"                : response.ok,
            "url"               : response.url,
            "status_code"       : response.status_code,
            "reason"            : response.reason,
            "cookies"           : dedup_dict(response.cookies),
            "headers"           : dedup_dict(response.headers),
            "elapsed"           : int(response.elapsed.total_seconds() * 1000.0),
            "apparent_encoding" : response.apparent_encoding,
            "text"              : response.text,
            "json"              : response_json,
            "links"             : response.links}

        # Cleaning up certificates, if any.
        if len(certs_path) == 0:
            LOG.info("No client authentication certificates detected.")
        elif authentication_handler.delete_certificates(certs_path):
            LOG.info("Successfully deleted client side authentication certificates.")
        else:
            LOG.warning(f"Unable to clear all client side authentication certificates {certs_path.keys()}.")

        # Produce a FunctionResult with the results
        yield self._status_and_log_message("Application Execution completed")
        yield FunctionResult(results)
