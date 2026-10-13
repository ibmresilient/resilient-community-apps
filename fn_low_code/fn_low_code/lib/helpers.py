# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.
# pragma pylint: disable=line-too-long, wrong-import-order
""" Helpers for Low Code App """

import base64
import logging
from typing import Tuple
from urllib.parse import unquote
from resilient_lib import IntegrationError, RequestsCommon, str_to_bool
from fn_low_code.lib.constants import INTEGRATION_ERROR

LOG = logging.getLogger(__name__)


def set_security_data(security_data: dict, rc: RequestsCommon) -> Tuple[dict, dict]:
    """
    Update **headers** or **query parameters** based on security scheme with authorization info
    Supports authorization as Basic, APIKey (headers or query params), Bearer token

    :param security_data: SecurityDTO passed with message
    :type security_data: dict
    :param rc: common code for making API calls
    :type rc: RequestsCommon

    :returns: a tuple of the new headers and query_params
    :rtype: Tuple[dict, dict]
    """
    headers = {}
    query_params = {}

    # convert scheme to lower for comparison
    scheme = security_data.get("scheme").lower() if security_data.get("scheme") else ""

    LOG.debug("Setting security based on scheme %s", scheme)

    if not scheme:
        LOG.warning("Security scheme not provided")

    elif scheme == "basic":
        # Username and password stored in api_key and api_key_secret, respectively
        api_key = security_data.get("api_key")
        api_key_secret = security_data.get("api_key_secret")
        auth_header = encode_basic_auth(api_key, api_key_secret)
        # Basic scheme will always get passed in as a header
        headers["Authorization"] = f"Basic {auth_header}"

    elif scheme == "apikey":
        # API key may be passed via the header or query params
        api_key = security_data.get("api_key")                  # API key is passed in as "apikeyid:apikeysecret" already formed; do we have to decode it?
        api_key_in = security_data.get("api_key_in", "").lower()    # indicates how to pass API key
        if api_key_in == "header":
            api_key_param_name = security_data.get("api_key_param_name", "Authorization")
            headers[api_key_param_name] = api_key
        elif api_key_in == "query":
            # If the API key is passed as a query parameter, then we add the api key to query_params
            api_key_param_name = security_data.get("api_key_param_name")
            query_params[api_key_param_name] = api_key
        else:
            LOG.warning("Unknown 'api_key_in' value: %s", api_key_in)

    elif scheme == "bearer":
        # OAuth?
        if str_to_bool(security_data.get("generate_bearer_token", 'False')) == True:
            token = generate_oauth_token(security_data, rc)
        else:
            # Bearer passed via headers as `Bearer <token>`
            token = security_data.get("auth_token")
        headers["Authorization"] = f"Bearer {token}"
    else:
        raise IntegrationError(f"Scheme {scheme} not supported.")

    return (headers, query_params)

def generate_oauth_token(security_data: dict, rc: RequestsCommon) -> str:
    """generate the oauth token from the security data 

    :param security_data: parameters needed for client_credentials
    :type security_data: dict
    :param rc: common code for making API calls
    :type rc: RequestsCommon

    :return: OAuth token
    :rtype: str
    """
    url = security_data.get("auth_token_auth_url")
    payload = security_data.get("auth_token_payload")
    headers = {
        "Content-Type": security_data.get("auth_token_payload_content_type")
    }
    token_results = rc.execute("POST", url, data=payload, headers=headers, proxies=rc.get_proxies())

    return token_results.json().get(security_data.get("auth_token_property_name")) if token_results else None

def encode_basic_auth(api_key: str, api_key_secret: str) -> str:
    return base64.b64encode(f"{api_key}:{api_key_secret}".encode("utf-8")).decode("utf-8")

def decode_basic_auth(basic_auth: str) -> list[str, str]:
    decoded = base64.b64decode(basic_auth.encode("utf-8")).decode("utf-8")
    return decoded.split(":")[:2]

def clean_encoding(hex_encoded: str) -> str:
    """ remove any hex encoding: valueA%26valueB """
    return unquote(hex_encoded)
