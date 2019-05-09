# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn_spamhaus_query
"""

import logging
from resilient_lib import RequestsCommon
from fn_spamhaus_query.util.spamhause_helper import *

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """

    # Getting the Config file parameters.
    options = opts.get("fn_spamhaus_query", {})
    wqs_url = options.get('spamhaus_wqs_url')
    dqs_key = options.get('spamhaus_dqs_key')

    # Header data
    header_data = {'Authorization': 'Bearer {}'.format(dqs_key)}

    requestcommon_object = RequestsCommon(function_opts=options)

    proxies_data = requestcommon_object.get_proxies()
    try:
        response_json = requestcommon_object.execute_call('GET', wqs_url.format('AUTHBL', '127.0.0.2'),
                                                          headers=header_data, proxies=proxies_data,
                                                          callback=spamhause_call_error)
        return {"state": "Success"}
    except Exception as err_msg:
        log.info(err_msg)
        return {"state": "Failed"}
