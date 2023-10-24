# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010 to 2023. All Rights Reserved.

import logging, json, requests

from urllib.error import URLError
from urllib.parse import urlparse
from resilient_lib import render, RequestsCommon

LOG = logging.getLogger()
CONTENT_TYPE = "content-type"
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
    Read newline-separated or json formatted 'headers', 'body' and 'cookies' into a 
    dictionary, if None, skipped. The input values are not required to be returned
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
    rest_url  : str, headers_dict : dict, cookies_dict : dict,
    body_dict : dict, rest_verify : bool, rest_timeout : int,
    rest_certificate : tuple=None, allowed_status_codes : list=[200]) -> requests.Response:
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
    :param rest_certificate: Tuple (.csr, .key), or a string .key. Required to perform client side authentication
    :param allowed_status_codes: list of allowed status codes. Default is [200]
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
    if headers_dict and CONTENT_TYPE in headers_dict and CONTENT_TYPE_JSON in headers_dict[CONTENT_TYPE]:
        return rc.execute(
            rest_method, rest_url,
            headers=headers_dict,
            cookies=cookies_dict,
            json=body_dict,
            verify=rest_verify,
            timeout=rest_timeout,
            clientauth=rest_certificate,
            callback=callback)

    return rc.execute(
        rest_method, rest_url,
        headers=headers_dict,
        cookies=cookies_dict,
        data=body_dict,
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
