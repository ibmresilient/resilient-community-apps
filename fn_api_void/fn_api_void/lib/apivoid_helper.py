# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

import logging
import urllib

SUB_URL = "v1/pay-as-you-go/"
LOG = logging.getLogger(__name__)


def get_request_url(base_url, sub_url, query_type, api_key, value):
    """
    Function that creates the url and parameters

    :param base_url: The base URL from the app.config
    :param sub_url: The sub URL from the app.config file. If not defined it will be: "v1/pay-as-you-go/"
    :param query_type: The query type of the request
    :param apikey: The api key from the app.config
    :param value: The artifact value

    :return: Tuple. A string of the URL and a dict of the params
    :rtype: tuple
    """
    # If no sub url defined in app.config file use the default one
    if not sub_url:
        sub_url = SUB_URL

    url_map = {
        "IP Reputation": {
            "url": "iprep",
            "params": {
                "ip": value
            }
        },
        "Domain Blacklist": {
            "url": "domainbl",
            "params": {
                "host": value
            }
        },
        "DNS Lookup": {
            "url": "dnslookup",
            "params": {
                "action": "dns-a",
                "host": value
            }
        },
        "Email Verify": {
            "url": "emailverify",
            "params": {
                "host": value
            }
        },
        "Threat Log": {
            "url": "threatlog",
            "params": {
                "host": value
            }
        },
        "SSL Info": {
            "url": "sslinfo",
            "params": {
                "host": value
            }
        },
        "URL Reputation": {
            "url": "urlrep",
            "params": {
                "url": urllib.parse.quote_plus(value)
            }
        },
        "selftest": {
            "url": "iprep",
            "params": {
                "stats": value
            }
        },
    }

    try:
        name = query_type.get("name")
        request_type_name = url_map.get(name)
        request_url = request_type_name.get("url")
        request_params = request_type_name.get("params")
        #request_url = url_map.get(query_type).get("url")

    except KeyError:
        raise ValueError("%s is an Invalid IP Void request type or it's not supported", query_type)

    # Join the base url, the request type and the sub url
    the_url = "/".join((base_url, request_url, sub_url))

    # Append the api key
    the_url = u"{0}/?key={1}".format(the_url, api_key)

    params_list = list(request_params.keys())
    # Append the params
    for k in params_list:
        params_value = request_params.get(k)
        the_url = u"{0}&{1}={2}".format(the_url, k, params_value)
    LOG.info("Using URL: %s", the_url)

    return the_url


def make_apivoid_api_call(base_url, sub_url, query_type, value, api_key, rc):
    """
    Function that makes the api call to APIVoid

    :param base_url: The base URL from the app.config
    :param sub_url: The sub URL from the app.config file. If not defined it will be: "v1/pay-as-you-go/"
    :param query_type: The query type of the request
    :param value: The artifact value
    :param api_key: The API Key to APIVoid read from the app.config file
    :param rc: RequestsCommon object

    :return: The response of the API call
    :rtype: response
    """

    # Get url and params
    request_url = get_request_url(base_url, sub_url, query_type, api_key, value)

    # Combine params
    #params = {"key": api_key}
    #params.update(request_info[1])

    # Execute api call and return response
    return rc.execute_call_v2(method="get", url=request_url)


def format_dict(dict_to_format):
    """
    Function that formats the passed dictionary
    and returns a string

    :param dict_to_format: A dict you want to format

    :return: String of the keys and values in the dict formatted
    :rtype: str
    """
    str_to_rtn = "\n-----------------\n"

    if not dict_to_format:
        str_to_rtn += "NONE\n"

    for (k, v) in dict_to_format.items():

        str_to_rtn += "{0}: {1}\n".format(k, v)

    str_to_rtn += "-----------------\n"

    return str_to_rtn
