# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2023. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

"""AppFunction implementation"""
import json
import requests

from logging import getLogger
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import render, RequestsCommon, validate_fields

FN_NAME = "rest_api"
PACKAGE_NAME = "fn_rest_api"
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
        validate_fields([
            "rest_api_method",
            "rest_api_url",
            "rest_api_verify"
            ], fn_inputs)

        # Get the function parameters:
        rest_properties = {}
        rest_method  = self.get_select_param(getattr(fn_inputs, "rest_api_method")) # select, values: "GET", "HEAD", "POST", "PUT", "DELETE", "OPTIONS", "PATCH"
        rest_url     = getattr(fn_inputs, "rest_api_url") # text
        rest_verify  = getattr(fn_inputs, "rest_api_verify") # boolean
        rest_timeout = getattr(fn_inputs, "rest_api_timeout", 600) # Default timeout to 600 seconds
        rest_properties["headers"] = self.get_textarea_param(getattr(fn_inputs, "rest_api_headers", None)) # textarea
        rest_properties["cookies"] = self.get_textarea_param(getattr(fn_inputs, "rest_api_cookies", None)) # textarea
        rest_properties["body"]    = self.get_textarea_param(getattr(fn_inputs, "rest_api_body", None))  # textarea
        allowed_status_codes = getattr(fn_inputs, "rest_api_allowed_status_codes", None) # text

        LOG.info("rest_method: %s", rest_method)
        LOG.info("rest_url: %s", rest_url)
        LOG.info("rest_verify: %s", rest_verify)
        LOG.info("rest_timeout: %s", rest_timeout)
        LOG.info("rest_headers: %s", rest_properties.get("headers"))
        LOG.info("rest_cookies: %s", rest_properties.get("cookies"))
        LOG.info("rest_body: %s", rest_properties.get("body"))
        LOG.info("allowed_status_codes: %s", allowed_status_codes)

        # Rendering rest url
        rest_url = render(rest_url, self.options)

        LOG.info("Rendering rest properties")
        # Read newline-separated or json formatted 'headers', 'body' and 'cookies' into a dictionary, if None, skipped
        for key in rest_properties:
            kv_option = rest_properties[key]
            if kv_option and not isinstance(kv_option, dict):
                kv_option = render(kv_option, self.options)
                kv_option = build_dict(kv_option)
                rest_properties[key] = kv_option
            LOG.info(f"{key} : {kv_option}")

        # Converting allowed_status_codes to a list of integers
        allowed_status_codes = [int(x) for x in allowed_status_codes.split(",")] if allowed_status_codes else []

        response = make_rest_call(
            self.opts, self.options, rest_method, rest_url,
            rest_properties.get("headers"), rest_properties.get("cookies"),
            rest_properties.get("body"), rest_verify, rest_timeout, allowed_status_codes)

        try:
            response_json = response.json()
        except:
            response_json = None

        results = {
            "ok": response.ok,
            "url": response.url,
            "status_code": response.status_code,
            "reason": response.reason,
            "cookies": dedup_dict(response.cookies),
            "headers": dedup_dict(response.headers),
            "elapsed": int(response.elapsed.total_seconds() * 1000.0),
            "apparent_encoding": response.apparent_encoding,
            "text": response.text,
            "json": response_json,
            "links": response.links,
        }

        # Produce a FunctionResult with the results
        yield FunctionResult(results)


def build_dict(kv_string:str) -> dict:
    """
    Builds a dictionary from the key-value string provided. If the key-value string is
    in json format, then it is converted to dictionary. If the key-value string is not,
    then the sting is assumed to be new-line separated, converted to a simple dictionary.
    
    Note: New-line separated key-value string does not support nested dictionary or lists.
    
    :param rest_temp: any key-value string
    :return: Dictionary
    """
    _dict = {}
    if kv_string is not None:
        try:
            # if key-value is in json format, then convert it to dictionary
            LOG.info("Trying to decode key-value to json format")
            _dict = json.loads(kv_string)

        except json.decoder.JSONDecodeError as e:
            # If the key-value is not in json format, then try to build a simple dictionary
            LOG.warn("Unable to decode in json format. Building a simple dictionary")
            for each_line in kv_string.split("\n"):
                item = each_line.strip().split(":", 1)
                if len(item) == 2:
                    _dict[item[0].strip()] = item[1].strip()
    return _dict


def make_rest_call(opts, options, rest_method : str,
    rest_url  : str, headers_dict : dict, cookies_dict : dict,
    body_dict : dict, rest_verify : bool, rest_timeout : int,
    allowed_status_codes : list=[200]) -> requests.Response:
    '''
    A wrapper function that makes the rest call and returns the response object. The callback function
    allows the response to be returned if the status code is > 300 and in the allowed_status_codes list.
    
    :param opts: self.opts,
    :param options: self.options,
    :param rest_method: rest method, values: "GET", "HEAD", "POST", "PUT", "DELETE", "OPTIONS", "PATCH"
    :param rest_url: rest url
    :param headers_dict: dictionary of headers. Supports json and new-line separated key-value string
    :param cookies_dict: dictionary of cookies. Supports json and new-line separated key-value string
    :param body_dict: dictionary of body. Supports json and new-line separated key-value string
    :param rest_verify: indicates whether to verify SSL certificates. Default is True
    :param rest_timeout: timeout in seconds. Default is 600 seconds
    :param allowed_status_codes: list of allowed status codes. Default is [200]
    '''

    def callback(response: requests.Response):
        ''' 
        Callback function to check the response status code and return the response if the status code even
        if response status code is > 300.
        '''
        if response.status_code < 300:
            return response
        elif int(response.status_code) in allowed_status_codes:
            return response
        else:
            response.raise_for_status()

    rc = RequestsCommon(opts, options)

    # If the content-type is json, then use the json parameter, else use the data parameter
    if CONTENT_TYPE in headers_dict and CONTENT_TYPE_JSON in headers_dict[CONTENT_TYPE]:
        return rc.execute(
            rest_method, rest_url,
            headers=headers_dict,
            cookies=cookies_dict,
            json=body_dict,
            verify=rest_verify,
            timeout=rest_timeout,
            callback=callback)

    return rc.execute(
        rest_method, rest_url,
        headers=headers_dict,
        cookies=cookies_dict,
        data=body_dict,
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
