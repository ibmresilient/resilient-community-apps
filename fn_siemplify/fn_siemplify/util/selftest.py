# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

import logging
from resilient_lib import RequestsCommon
from fn_siemplify.lib.siemplify_common import SiemplifyCommon

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    app_configs = opts.get("fn_siemplify", {})

    rc = RequestsCommon(opts, app_configs)

    try:
        sc = SiemplifyCommon(rc, app_configs)
        _result, error_msg = sc.get_version()

        return {
            "state": "success" if not error_msg else "failure",
            "reason": error_msg
        }
    except Exception as err:
        return {
            "state": "failure",
            "reason": str(err)
        }
