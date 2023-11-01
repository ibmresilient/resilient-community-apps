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

LOG = getLogger(__name__)

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'rest_api'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: This function calls a REST web service. It supports the standard REST methods: 
            GET, HEAD, POST, PUT, DELETE, OPTIONS, and PATCH.

        The function parameters determine the type of call, the URL, and optionally the headers 
        and body. The results include the text or structured (JSON) result from the web service,
        and additional information including the elapsed time.

        Inputs:
        -------
            -   fn_inputs.rest_api_body
            -   fn_inputs.rest_api_query_parameters
            -   fn_inputs.rest_api_url
            -   fn_inputs.rest_api_method
            -   fn_inputs.rest_api_timeout
            -   fn_inputs.rest_api_cookies
            -   fn_inputs.rest_api_allowed_status_codes
            -   fn_inputs.rest_api_verify
            -   fn_inputs.rest_api_headers

            -   fn_inputs.rest_retry_tries
            -   fn_inputs.rest_retry_delay
            -   fn_inputs.rest_retry_backoff

            -   fn_inputs.oauth_token_url
            -   fn_inputs.oauth_client_id
            -   fn_inputs.oauth_client_secret
            -   fn_inputs.oauth_redirect_uri
            -   fn_inputs.oauth_scope
            -   fn_inputs.oauth_code
            -   fn_inputs.oauth_access_token
            -   fn_inputs.oauth_refresh_token
            -   fn_inputs.oauth_token_type

            -   fn_inputs.client_auth_pem
            -   fn_inputs.client_auth_key
            -   fn_inputs.client_auth_cert
        """
        yield self.status_message(f"Starting App Function: '{FN_NAME}'")
        validate_fields([
            "rest_api_method",
            "rest_api_url",
            "rest_api_verify"
            ], fn_inputs)

        rest_properties = oauth_properties = certs_path = {}

        # Get the function parameters: 
        # Select, values: "GET", "HEAD", "POST", "PUT", "DELETE", "OPTIONS", "PATCH"
        rest_method  = self.get_select_param(getattr(fn_inputs, "rest_api_method")) 
        rest_url     = getattr(fn_inputs, "rest_api_url") # text
        rest_verify  = getattr(fn_inputs, "rest_api_verify") # boolean
        rest_timeout = getattr(fn_inputs, "rest_api_timeout", 600) # Default timeout to 600 seconds
        allowed_status_codes = getattr(fn_inputs, "rest_api_allowed_status_codes", None) # text

        rest_properties = {
            "headers" : self.get_textarea_param(getattr(fn_inputs, "rest_api_headers", None)), # textarea
            "cookies" : self.get_textarea_param(getattr(fn_inputs, "rest_api_cookies", None)), # textarea
            "body"    : self.get_textarea_param(getattr(fn_inputs, "rest_api_body", None)),    # textarea
            "query_params"  : self.get_textarea_param(getattr(fn_inputs, "rest_api_query_parameters", None))}  # textarea

        retry_properties = {
            "retry_tries"   : int(getattr(fn_inputs, "rest_retry_tries", 1)),      # integer
            "retry_delay"   : int(getattr(fn_inputs, "rest_retry_delay", 1)),      # integer
            "retry_backoff" : int(getattr(fn_inputs, "rest_retry_backoff", 1))}    # integer

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

        LOG.info(f"rest_method          : {rest_method}")
        LOG.info(f"rest_url             : {rest_url}")
        LOG.info(f"rest_verify          : {rest_verify}")
        LOG.info(f"rest_timeout         : {rest_timeout}")
        LOG.info(f"allowed_status_codes : {allowed_status_codes}")
        LOG.info(f"rest_properties      : {json.dumps(rest_properties, indent=2)}")

        # Rendering rest url with values from app.conf
        rest_url = render(rest_url, self.options)

        # Rendering any OAuth property that has values from app.conf
        LOG.info("Rendering OAuth properties")
        for key, value in oauth_properties.items():
            if value:
                oauth_properties[key] = render(value, self.options)

        LOG.info("Rendering rest properties. If values contain SECRETS, they are incorporated.")
        render_dict_components(rest_properties, self.options)

        LOG.info("Rendering JWT properties. If values contain SECRETS, they are incorporated.")
        render_dict_components(jwt_properties, self.options)

        # Converting allowed_status_codes to a list of integers
        allowed_status_codes = [int(x) for x in allowed_status_codes.split(",")] if allowed_status_codes else []

        # Initializing OAuth handler
        oauth_client     = authentication_handler.OAuth2Authorization(self.rc, oauth_properties)

        # Performing OAuth authentication if Oauth parameters are provided
        rest_properties  = authentication_handler.add_oauth_headers(oauth_client, rest_properties)
        
        # Initializing JWT handler
        jwt_client       = authentication_handler.JWTHandler(jwt_properties)

        # Generating jwt headers if jwt attributes are provided
        rest_properties  = jwt_client.add_jwt_headers(rest_properties)
        
        # Generating certificates for client side authentication, if certificates are provided
        rest_certificate = authentication_handler.check_certificate(cert_properties, certs_path)

        LOG.debug(f"Request Header : {json.dumps(rest_properties.get('headers'), indent=2)}")
        LOG.debug(f"Request Body   : {json.dumps(rest_properties.get('body'), indent=2)}")

        retry = False
        try:
            LOG.info("Attempting call")
            response = make_rest_call(
                self.opts, self.options,
                rest_method, rest_url,
                rest_properties.get("headers"),
                rest_properties.get("cookies"),
                rest_properties.get("body"),
                rest_properties.get("query_params"),
                retry_properties.get("retry_tries"),
                retry_properties.get("retry_delay"),
                retry_properties.get("retry_backoff"),
                rest_verify,
                rest_timeout,
                rest_certificate,
                allowed_status_codes)

        except (HTTPError, IntegrationError) as err:
            # If the error raised is either HTTPError else IntegrationError, sets retry to True
            LOG.warning(str(err))
            if oauth_client.check_oauth_ready():
                retry = True
            else:
                raise IntegrationError(str(err))

        if retry:
            # Retrying request by attempting to refresh_tokens
            oauth_client.force_refresh_tokens()
            rest_properties = authentication_handler.add_oauth_headers(oauth_client, rest_properties)
            response = make_rest_call(
                self.opts, self.options,
                rest_method, rest_url,
                rest_properties.get("headers"),
                rest_properties.get("cookies"),
                rest_properties.get("body"),
                rest_properties.get("query_params"),
                retry_properties.get("retry_tries"),
                retry_properties.get("retry_delay"),
                retry_properties.get("retry_backoff"),
                rest_verify,
                rest_timeout,
                rest_certificate,
                allowed_status_codes)

        try:
            response_json = response.json()
            LOG.debug(json.dumps(response_json, indent=2))
        except:
            response_json = None

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

        if len(certs_path) == 0:
            LOG.info("No client authentication certificates detected.")
        elif authentication_handler.delete_certificates(certs_path):
            LOG.info("Successfully deleted client side authentication certificates.")
        else:
            LOG.warning(f"Unable to clear all client side authentication certificates {certs_path.keys()}.")

        # Produce a FunctionResult with the results
        yield FunctionResult(results)
