# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn_secureworks_ctp
"""

import logging
from resilient_lib import RequestsCommon, validate_fields

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())

CONFIG_DATA_SECTION='fn_secureworks_ctp'

def selftest_function(opts):

    options = opts.get(CONFIG_DATA_SECTION, {})

    validate_fields(['base_url', 'username', 'password'], options)

    base_url = options.get('base_url')
    username = options.get('username')
    password = options.get('password')
    cafile = options.get('cafile')
    bundle = os.path.expanduser(cafile) if cafile else False
    api_key = u"APIKEY {0}:{1}".format(username, password)
    headers = {
                'Authorization': api_key,
                'content-type': "application/json"
                }
    payload = {'ticketType': 'INCIDENT'}

    url = u"{0}/tickets/count".format(base_url)
    try:
        rc = RequestsCommon(opts, options)
        response = rc.execute_call_v2("post", url, headers=headers, params=payload, verify=bundle,
                                      proxies=rc.get_proxies())

        if response.status_code == 200:
            return {'state': 'success'}

        reason = u"status code {0}".format(response.status_code)
        return {
               'state': 'failure',
               'reason': reason
                }

    except Exception as exc:
        return {
               'state': 'failure',
               'reason': exc
               }