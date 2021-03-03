# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""
Function implementation test.
Usage: resilient-circuits selftest -l fn_aws_guardduty
"""

import logging
from fn_aws_guardduty.lib.aws_gd_client import AwsGdClient

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Simple test to verify AWS GuardDuty connectivity.
    """
    options = opts.get("fn_aws_guardduty", {})
    try:
        aws_gd = AwsGdClient(opts, options, region=options.get("aws_gd_master_region"))
        # Get the DetectorId for the specified AWS Region.
        detector = aws_gd.get("list_detectors")
        if isinstance(detector, list):
            return {"state": "success"}
        else:
            return {"state": "failure"}

    except Exception as e:
        return {"state": "failure", "status_code": e}