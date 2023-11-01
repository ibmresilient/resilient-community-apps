# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010 to 2023. All Rights Reserved.

import logging, json, requests

from urllib.error import URLError
from urllib.parse import urlparse
from resilient_lib import render, RequestsCommon

LOG = logging.getLogger()
CONTENT_TYPES = ["Content-type", "content-type", "CONTENT-TYPE", "Content-Type"]
CONTENT_TYPE_JSON = "application/json"


def validate_url(url):
    """
    Validate a string is a URL format.
    :param url: String to validate as a URL.
    :return: Boolean from result of validation.
    """
    if url:
        result = urlparse(url.strip())
        if all([result.scheme, result.netloc]):
            return url
        else:
            raise URLError(f"URL format is invalid: {url}")
    return None


def render_dict_components(input_properties, options):
    """
    Read newline-separated or json formatted 'headers', 'body' 'query_parameters', and 'cookies'
    into a dictionary, if None, skipped. The input values are not required to be returned
    as they are passed by reference.
    """
    for key in input_properties:
        kv_option = input_properties[key]
        if kv_option:
            if not isinstance(kv_option, dict):
                kv_option = render(kv_option, options)
                kv_option = build_dict(kv_option)
                input_properties[key] = kv_option
        else:
            input_properties[key] = kv_option
        LOG.info(f"{key} : {input_properties[key]}")


def build_dict(kv_string:str) -> dict:
    """
    Builds a dictionary from the key-value string provided. If the key-value string is
    in json format, then it is converted to dictionary. If the key-value string is not,
    then the sting is assumed to be new-line separated, converted to a simple dictionary.
    
    Note: New-line separated key-value string does not support nested dictionary or lists.
    
    :param rest_temp: any key-value string
    :return: Dictionary
    """
    _ret_value = {}
    if kv_string is not None:
        try:
            # if key-value is in json format, then convert it to dictionary
            LOG.info("Trying to decode key-value to json format")
            _ret_value = json.loads(kv_string)

        except json.decoder.JSONDecodeError as e:
            # Checking if the given value is a key-value pair at all
            if ":" in kv_string:
                # If the key-value is not in json format, then try to build a simple dictionary
                LOG.warn("Unable to decode in json format. Building a simple dictionary")
                for each_line in kv_string.split("\n"):
                    item = each_line.strip().split(":", 1)
                    if len(item) == 2:
                        _ret_value[item[0].strip()] = item[1].strip()
            else:
                _ret_value = kv_string
    return _ret_value


def make_rest_call(opts, options, rest_method : str,
    rest_url : str,  headers_dict : dict, cookies_dict : dict, body_dict  : dict,
    query_params : dict, retry_tries  : int, retry_delay: int, retry_backoff: int,
    rest_verify : bool, rest_timeout : int, rest_certificate : tuple=None,
    allowed_status_codes : list=[200]) -> requests.Response:
    '''
    A wrapper function that makes the rest call and returns the response object. The callback function
    allows the response to be returned if the status code is > 300 and in the allowed_status_codes list.

    Arguments:
    ---------
        opts          : Self.opts,
        options       : Self.options,
        rest_method   : Rest method, values: "GET", "HEAD", "POST", "PUT", "DELETE", "OPTIONS", "PATCH"
        rest_url      : Rest url
        headers_dict  : Dictionary of headers. Supports json and new-line separated key-value string
        cookies_dict  : Dictionary of cookies. Supports json and new-line separated key-value string
        body_dict     : Dictionary of body. Supports json and new-line separated key-value string
        query_params  : Dictionary of GET method url values. Supports json and new-line separated key-value string
        retry_tries   : Maximum number of request retry attempts. Default: 1 (no retry). Use -1 for unlimited retries.
        retry_delay   : Initial delay between attempts. Default: 0
        retry_backoff : Multiplier applied to delay between attempts. Default: 1 (no backoff)
        rest_verify   : Indicates whether to verify SSL certificates. Default is True
        rest_timeout  : Timeout in seconds. Default is 600 seconds
        rest_certificate : Tuple (.csr, .key), or a string .key. Required to perform client side authentication
        allowed_status_codes : List of allowed status codes. Default is [200]
    '''

    def callback(response: requests.Response):
        ''' 
        Callback function to check the response status code and return the response. if the status is < 300,
        or in the allowed_status_codes list, then return the response, else raise an exception.
        '''
        # return response if status code is < 300
        if response.status_code < 300:
            return response

        # return response if status codein allowed_status_codes list
        elif int(response.status_code) in allowed_status_codes:
            return response

        # raise exception for everything else
        else:
            response.raise_for_status()

    rc = RequestsCommon(opts, options)

    # If the content-type is json, then use the json parameter, else use the data parameter
    # Content-type is made case agnostic
    if headers_dict:
        for content_type in CONTENT_TYPES:
            if content_type in headers_dict and CONTENT_TYPE_JSON in headers_dict[content_type]:
                LOG.info(f"Found {content_type} : {CONTENT_TYPE_JSON} in request header. Payload will be json formatted")
                return rc.execute(
                    rest_method, rest_url,
                    headers=headers_dict,
                    cookies=cookies_dict,
                    json=body_dict,
                    params=query_params,
                    retry_tries=retry_tries,
                    retry_delay=retry_delay,
                    retry_backoff=retry_backoff,
                    verify=rest_verify,
                    timeout=rest_timeout,
                    clientauth=rest_certificate,
                    callback=callback)

    return rc.execute(
        rest_method, rest_url,
        headers=headers_dict,
        cookies=cookies_dict,
        data=body_dict,
        params=query_params,
        retry_tries=retry_tries,
        retry_delay=retry_delay,
        retry_backoff=retry_backoff,
        verify=rest_verify,
        timeout=rest_timeout,
        clientauth=rest_certificate,
        callback=callback)


def dedup_dict(item_list):
    """
    this is needed to ensure headers or cookies keys are not duplicated
    :param item_list:
    :return: dictionary representation
    """
    return {k: v for k, v in item_list.items()}
