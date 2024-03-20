# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# -*- coding: utf-8 -*-

import shodan
from resilient_lib import IntegrationError

CONFIG_DATA_SECTION = "fn_shodan"
HANDLED_ERROR_MSGS = (
    "Invalid IP",
    "No information available for that IP."
)


def handle_error(reason):
    """
    Returns a dict containing err and reason

    :param reason: A string, why it failed
    :return: A dict containing err and reason
    :rtype: dict
    """
    return {
        "err": True,
        "reason": reason
    }


def make_api_call(call_type, rc, api_key, app_configs, qry=None):
    """
    Function that makes the api call to Shodan.io

    :param call_type: A string, either 'host', 'search' or 'info'
    :param rc: resilient_lib.RequestsCommon object
    :param api_key: The API Key to Shodan.io
    :param app_configs: The app_configs for fn_shodan. Used to get proxies
    :param qry: The query to search for. For 'host' it is an IP Address. For 'search' it is a search query identical syntax to the Shodan.io website
    :raise: shodan.exception.APIError if API Key is invalid
    :return: The response of the API call
    :rtype: dict
    """
    res = None

    api = shodan.Shodan(
        key=api_key,
        proxies=rc.get_proxies()
    )

    try:
        if call_type == "host":
            res = api.host(qry)

        elif call_type == "search":
            res = api.search(qry)

        elif call_type == "info":
            res = api.info()

        else:
            raise IntegrationError(u"API call type not supported: {0}".format(call_type))

    except shodan.exception.APIError as err:

        if err.value in HANDLED_ERROR_MSGS:
            res = handle_error(err.value)

        else:
            raise err

    return res


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
