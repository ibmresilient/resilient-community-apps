# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.

from resilient_lib import RequestsCommon

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
    url = "{}/{}/{}".format(options['url'], greynoise_type, greynoise_value)

    headers = HTTP_HEADERS.copy()
    headers['key'] = options['api_key']

    ## make request and check results
    rc = RequestsCommon(opts, options)

    response = rc.execute_call_v2("get", url, headers=headers, proxies=rc.get_proxies()) # added proxies
    return response.json()
