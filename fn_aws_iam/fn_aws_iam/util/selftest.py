# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn_aws_iam
"""

import logging
from fn_aws_iam.lib.aws_iam_client import AwsIamClient

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Simple test to verify AWS IAM connectivity.
    """
    options = opts.get("fn_aws_iam", {})
    try:
        iam = AwsIamClient(opts, options, sts_client=True)
        default_identity = iam.sts.get_caller_identity()

        if isinstance(default_identity , dict) and "Arn" in default_identity:
            user_name = default_identity["Arn"].split('/')[1]
            user_properties = iam.iam.get_user(UserName=user_name)
            if isinstance(user_properties, dict) and "User" in user_properties:
                return {"state": "success"}
            else:
                return {"state": "failure"}
        else:
            return {"state": "failure"}

    except Exception as e:
        return {"state": "failure", "status_code": e}