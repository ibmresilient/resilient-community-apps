# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.

"""Function implementation
   test with: resilient-circuits selftest -l fn_qradar_advisor
"""

import logging
from fn_qradar_advisor.lib.qradar_advisor_client import QRadarAdvisorClient

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    qradar_verify_cert = True
    options = opts.get("fn_qradar_advisor", {})
    if "verify_cert" in options and options["verify_cert"] == "false":
        qradar_verify_cert = False

    try:
        qraw_client = QRadarAdvisorClient(qradar_host=options["qradar_host"],
                                          qradar_token=options["qradar_advisor_token"],
                                          advisor_app_id=options["qradar_advisor_app_id"],
                                          cafile=qradar_verify_cert, log=log,
                                          opts=opts, function_opts=options)
        r = qraw_client.test_connectivity()
        if r.status_code == 200:
            return {"state": "success", "status_code": r.status_code}
        else:
            return {"state": "failure", "status_code": r.status_code}

    except Exception as e:
        return {"state": "failure", "status_code": str(e)}