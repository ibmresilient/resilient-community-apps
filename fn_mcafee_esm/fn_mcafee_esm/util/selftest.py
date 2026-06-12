# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn-mcafee-esm
"""

import logging
from resilient_lib import RequestsCommon
from fn_mcafee_esm.util.helper import check_config, get_authenticated_headers

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Simple test to verify McAfee ESM connectivity.
    """
    options = opts.get("fn_mcafee_esm", {})
    try:
        # Instantiate RequestsCommon object
        rc = RequestsCommon(opts=opts, function_opts=options)
        # Check config file and change trust_cert to Boolean
        options = check_config(options)

        url = options["esm_url"] + "/rs/esm/v2/caseGetCaseList"

        headers = get_authenticated_headers(rc, options["esm_url"], options["esm_username"],
                                            options["esm_password"], options["trust_cert"])

        r = rc.execute_call_v2('post', url, headers=headers, verify=options["trust_cert"], proxies=rc.get_proxies())
        if r.status_code == 200:
            return {"state": "success", "status_code": r.status_code }
        else:
            return {"state": "failure", "status_code": r.status_code }

    except Exception as e:
        return {"state": "failure", "status_code": e}