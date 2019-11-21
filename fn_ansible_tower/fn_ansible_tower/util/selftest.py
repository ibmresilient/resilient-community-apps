# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn_ansible_tower
"""

import logging
from resilient_lib import RequestsCommon, str_to_bool
from fn_ansible_tower.lib.common import SECTION_HDR, TOWER_API_BASE, get_common_request_items

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())

PING_URL = "ping/"

def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    options = opts.get(SECTION_HDR, {})

    rc = RequestsCommon(opts, options)

    # common
    basic_auth, cafile = get_common_request_items(options)

    # get summary information
    ping_url = "/".join((options['url'], TOWER_API_BASE, PING_URL))

    try:
        ping_result = rc.execute_call_v2("get", ping_url, proxies=rc.get_proxies(), auth=basic_auth,
                                         verify=cafile)

        return {"state": "success"}
    except Exception as err:
        return {"state": "failure", "reason": str(err)}
