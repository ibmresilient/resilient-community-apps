# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

import logging
import sys
if sys.version_info.major >= 3:
    from urllib.parse import quote as url_encode
else:
    from urllib import quote as url_encode

SUB_URL = "v1/pay-as-you-go/"
LOG = logging.getLogger(__name__)


def build_request_url(base_url, sub_url, query_type, api_key, value):
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
        "Domain Reputation": {
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
                "email": value
            }
        },
        "ThreatLog": {
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
                "url": url_encode(value.encode('utf8')) if isinstance(value, str) else value
            }
        },
        "selftest": {
            "url": "sitetrust",
            "params": {
                "stats": value
            }
        },
    }

    try:
        request_type = url_map.get(query_type)
        request_url = request_type.get("url")
        request_params = request_type.get("params")

    except KeyError:
        raise ValueError("%s is an Invalid IP Void request type or it's not supported", query_type)

    # Join the base url, the request type and the sub url
    the_url = "/".join((base_url, request_url, sub_url))

    # Append the api key
    the_url = u"{0}?key={1}".format(the_url, api_key)

    # Append the params
    for (k, v) in request_params.items():
        the_url = u"{0}&{1}={2}".format(the_url, k, v)

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

    # Get url and params and build the request URL.
    request_url = build_request_url(base_url, sub_url, query_type, api_key, value)

    # Execute api call and return response
    return rc.execute_call_v2(method="get", url=request_url)
