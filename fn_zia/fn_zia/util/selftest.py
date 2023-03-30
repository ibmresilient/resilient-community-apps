# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

import logging
from fn_zia.lib.zia_client import ZiaClient

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Simple test to verify Zia connectivity.
    """
    fn_opts = opts.get("fn_zia", {})
    try:
        ziacli = ZiaClient(opts, fn_opts)
        result = ziacli.get_blocklist_urls()
        if isinstance(result, dict):
            return {
                "state": "success",
                "reason": "Successful connection to Zia endpoint"
            }
        else:
            return {
                "state": "failure",
                "reason": "Failed to connect to Zia endpoint"
            }

    except Exception as e:
        return {
            "state": "failure",
            "status_code": e
        }