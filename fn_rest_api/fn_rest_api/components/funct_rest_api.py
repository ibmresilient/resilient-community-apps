# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2023. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

"""AppFunction implementation"""

from logging import getLogger
import requests
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields, render, RequestsCommon

PACKAGE_NAME = "fn_rest_api"
FN_NAME = "rest_api"
CONTENT_TYPE = "Content-type"
CONTENT_TYPE_JSON = "application/json"
LOG = getLogger(__name__)

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'rest_api'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: This function calls a REST web service. It supports the standard REST methods: GET, HEAD, POST, PUT, DELETE and OPTIONS.

        The function parameters determine the type of call, the URL, and optionally the headers and body. The results include the text or structured (JSON) result from the web service, and additional information including the elapsed time.
        Inputs:
            -   fn_inputs.rest_api_body
            -   fn_inputs.rest_api_url
            -   fn_inputs.rest_api_method
            -   fn_inputs.rest_api_timeout
            -   fn_inputs.rest_api_cookies
            -   fn_inputs.rest_api_allowed_status_codes
            -   fn_inputs.rest_api_verify
            -   fn_inputs.rest_api_headers
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        # Get the function parameters:
        rest_method = self.get_select_param(getattr(fn_inputs, "rest_api_method", None))  # select, values: "GET", "HEAD", "POST", "PUT", "DELETE", "OPTIONS", "PATCH"
        rest_url = getattr(fn_inputs, "rest_api_url", None)  # text
        rest_headers = self.get_textarea_param(getattr(fn_inputs,"rest_api_headers", None))  # textarea
        rest_cookies = self.get_textarea_param(getattr(fn_inputs,"rest_api_cookies", None))  # textarea
        rest_body = self.get_textarea_param(getattr(fn_inputs,"rest_api_body", None))  # textarea
        rest_verify = getattr(fn_inputs, "rest_api_verify")  # boolean
        rest_timeout = getattr(fn_inputs, "rest_api_timeout", 600) # Default timeout to 600 seconds
        allowed_status_codes = getattr(fn_inputs, "rest_api_allowed_status_codes", None) # text

        LOG.info("rest_method: %s", rest_method)
        LOG.info("rest_url: %s", rest_url)
        LOG.info("rest_headers: %s", rest_headers)
        LOG.info("rest_cookies: %s", rest_cookies)
        LOG.info("rest_body: %s", rest_body)
        LOG.info("rest_verify: %s", rest_verify)
        LOG.info("rest_timeout: %s", rest_timeout)
        LOG.info("allowed_status_codes: %s", allowed_status_codes)

        # Read newline-separated 'rest_headers' into a dictionary
        headers_dict = rest_headers
        if not isinstance(rest_headers, dict):
            rest_headers = render(rest_headers, self.options)
            headers_dict = build_dict(rest_headers)

        # Read newline-separated 'rest_cookies' into a dictionary
        cookies_dict = rest_cookies
        if not isinstance(rest_cookies, dict):
            cookies_dict = build_dict(rest_cookies)

        resp = make_rest_call(self.opts, self.options, rest_method, rest_url,
                                headers_dict, cookies_dict, rest_body, rest_verify, rest_timeout, allowed_status_codes)

        try:
            response_json = resp.json()
        except:
            response_json = None

        results = {
            "ok": resp.ok,
            "url": resp.url,
            "status_code": resp.status_code,
            "reason": resp.reason,
            "cookies": dedup_dict(resp.cookies),
            "headers": dedup_dict(resp.headers),
            "elapsed": int(resp.elapsed.total_seconds() * 1000.0),
            "apparent_encoding": resp.apparent_encoding,
            "text": resp.text,
            "json": response_json,
            "links": resp.links,
        }

        # Produce a FunctionResult with the results
        yield FunctionResult(results)

def build_dict(rest_temp):
    """
    Builds a dictionary from either the rest_headers or rest_cookies
    :param rest_temp: rest_headers or rest_cookies
    :return: Dictionary
    """
    temp_dict = {}
    if rest_temp is not None:
        lines = rest_temp.split("\n")
        for line in lines:
            keyval = line.strip().split(":", 1)
            if len(keyval) == 2:
                temp_dict[keyval[0].strip()] = keyval[1].strip()

    return temp_dict

def make_rest_call(opts, options, rest_method, rest_url, headers_dict, cookies_dict, rest_body, rest_verify, rest_timeout, allowed_status_codes=[200]):
    
    def callback(response: requests.Response):
        if response.status_code < 300:
            return response
        elif str(response.status_code) in allowed_status_codes:
            return response
        else:
            response.raise_for_status()
    
    rc = RequestsCommon(opts, options)

    if CONTENT_TYPE in headers_dict and CONTENT_TYPE_JSON in headers_dict[CONTENT_TYPE]:
        return rc.execute(rest_method, rest_url,
                                  headers=headers_dict,
                                  cookies=cookies_dict,
                                  json=rest_body,
                                  verify=rest_verify,
                                  timeout=rest_timeout,
                                  callback=callback)

    return rc.execute(rest_method, rest_url,
                              headers=headers_dict,
                              cookies=cookies_dict,
                              data=rest_body,
                              verify=rest_verify,
                              timeout=rest_timeout,
                              callback=callback)


def dedup_dict(item_list):
    """
    this is needed to ensure headers or cookies keys are not duplicated
    :param item_list:
    :return: dictionary representation
    """
    return {k: v for k, v in item_list.items()}