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
            LOG.info("URL valid!")
            return url
        else:
            raise URLError(f"URL format is invalid! {url}")
    return None


def render_dict_components(input_properties, options):
    """
    Read newline-separated or json formatted 'headers', 'body' 'query_parameters', and 'cookies'
    into a dictionary, if None, skipped. The input values are not required to be returned
    as they are passed by reference.

    :param input_properties: Dictionary of json-type objects passed in as string
    :type input_properties: dict
    :return: No return as values are modified directly by reference
    :rtype: None
    """
    # Iterating through inputs and rendering each component. input_properties is a dictionary of
    # inputs which are of type string. These strings are to be converted into dictionaries with
    # appropriate secrets rendered.
    for key in input_properties:
        kv_option = input_properties[key]
        if kv_option and not isinstance(kv_option, dict):
                # skips input if already of type dict or None
                LOG.info(f"Detected string kv-pair for {key}, converting to dictionary")
                kv_option = render(kv_option, options)
                kv_option = build_dict(kv_option)
                input_properties[key] = kv_option
        else:
            # If value has None assigned to it. It is directly assigned here
            input_properties[key] = kv_option


def build_dict(kv_string:str) -> dict:
    """
    Builds a dictionary from the key-value string provided. If the key-value string is
    in json format, then it is converted to dictionary. If the key-value string is not,
    then the sting is assumed to be new-line separated, converted to a simple dictionary.

        .. note::
            New-line separated key-value string does not support nested dictionary or lists.

    :param kv_string: any key-value string
    :type kv_string: str
    :return: A dictionary equivalent of the provided string
    :rtype: dict
    """
    _ret_value = {}
    if kv_string is not None:
        try:
            # if key-value is in json format, then convert it to dictionary
            LOG.debug("Trying to decode key-value to json format")
            _ret_value = json.loads(kv_string)

        except json.decoder.JSONDecodeError as e:
            LOG.warning("Unable to json decode value. Checking to see if value is of dict format")
            # Checking if the given value is a key-value pair at all
            if ":" in kv_string:
                # If the key-value is not in json format, then try to build a simple dictionary
                LOG.debug("Assuming dict is in new-line separated format. Attempting to build dict)")
                for each_line in kv_string.split("\n"):
                    item = each_line.strip().split(":", 1)
                    if len(item) == 2:
                        _ret_value[item[0].strip()] = item[1].strip()
            else:
                LOG.debug("Detected value does not seem to be a dict. Directly assigning value")
                _ret_value = kv_string
    return _ret_value


def make_rest_call(opts, options, allowed_status_codes:list=[200], **kwargs) -> requests.Response:
    """
    A wrapper function that makes the rest call and returns the response object. The callback function
    allows the response to be returned if the status code is > 300 and in the allowed_status_codes list.

    :param opts:  All configurations found in the app.config file
    :type opts: dict
    :param function_opts: All configurations found in the ``[my_function]`` section of the app.config file
    :type function_opts: dict
    :param allowed_status_codes: (Optional) List of allowed status codes. Default: ``[200]``.
    :type allowed_status_code: list
    :return: Response returned by the endpoints
    :rtype: :class:`requests.Response <https://docs.python-requests.org/en/latest/api/#requests.Response>`_ object
        or ``callback`` function.
    """

    def callback(response:requests.Response):
        ''' 
        Callback function to check the response status code and return the response. if the status is < 300,
        or in the allowed_status_codes list, then return the response, else raise an exception.

        :return: Response returned by the endpoints
        :rtype: :class:`requests.Response <https://docs.python-requests.org/en/latest/api/#requests.Response>`_ object
            or ``callback`` function.
        
        '''
        LOG.info("Checking response status_code")
        
        # return response if status code is < 300
        if response.status_code < 300:
            LOG.info("Valid response code, returning request")
            return response

        # return response if status codein allowed_status_codes list
        elif int(response.status_code) in allowed_status_codes:
            LOG.info("Response status_code falls under exempted status_codes, returning request")
            return response

        # raise exception for everything else
        else:
            response.raise_for_status()

    rc = RequestsCommon(opts, options)

    # If the content-type is json, then use the json parameter, else use the data parameter
    # Content-type is made case agnostic
    _headers = kwargs.get("headers")

    # Request body is assumed to be data
    kwargs["data"]     = kwargs.pop("body", {})
    kwargs["callback"] = callback

    if _headers:
        for content_type in CONTENT_TYPES:
            # checking to see if header has content-type : application/json. If so, assigns body to data
            if content_type in _headers and CONTENT_TYPE_JSON in _headers[content_type]:
                LOG.info(f"Found {content_type} : {CONTENT_TYPE_JSON} in request header. Payload will be json formatted")
                kwargs["json"] = kwargs.pop("data")

    return rc.execute(**kwargs)


def dedup_dict(item_list):
    """
    this is needed to ensure headers or cookies keys are not duplicated
    :param item_list:
    :return: dictionary representation
    :returns: Dictionary of deduplicated values
    :rtype: dict
    """
    return {k: v for k, v in item_list.items()}
