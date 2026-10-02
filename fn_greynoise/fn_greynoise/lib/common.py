# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.

from urllib.parse import urlparse
from resilient_lib import RequestsCommon

V2_CONTEXT_IP = "v2/noise"
V3_COMMUNITY_IP = "v3/community"

SECTION_HEADER = "fn_greynoise"

HTTP_HEADERS = {
    "Accept": "application/json",
    "key": None
}

def call_greynoise(opts, options, greynoise_type, greynoise_value):
    """
    perform the request to greynoise
    :param opts - app.config containing [resilient] section
    :param options - section for greynoise params
    :param greynoise_type - 'context' or 'quick' for the url
    :return - json payload returned from the API call
    """
    # for backward compatibility rebuild the base URL which can be used for v2 and v3 api calls
    url_parse = urlparse(options['url'])
    url = f"{url_parse.scheme}://{url_parse.netloc}"
    if greynoise_type == "community":
        url = f"{url}/{V3_COMMUNITY_IP}/{greynoise_value}"
    else:
        url = f"{url}/{V2_CONTEXT_IP}/{greynoise_type}/{greynoise_value}"

    headers = HTTP_HEADERS.copy()
    headers['key'] = options['api_key']

    ## make request and check results
    result_code = RequestsCommon(opts, options)

    response, error_msg = result_code.execute("get",
                                              url,
                                              headers=headers,
                                              proxies=result_code.get_proxies(),
                                              callback=callback
                                              )
    return response.json(), error_msg

def callback(response):
    """
    callback needed for certain REST API calls to return a formatted error message
    :param response:
    :return: response, error_msg
    """
    error_msg = None
    if int(response.status_code/100) in [4]:
        resp = response.json()
        msg = resp.get("message")
        error_msg = f"Greynoise failure: \n  status code: {response.status_code}\n  message: {msg}"

    return response, error_msg
