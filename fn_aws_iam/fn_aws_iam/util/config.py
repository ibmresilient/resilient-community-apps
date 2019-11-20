# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Generate a default configuration-file section for fn_aws_iam"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_aws_iam]
aws_iam_access_key_id=<AWS_IAM_ACCESS_KEY_ID>
aws_iam_secret_access_key=<AWS_IAM_SECRET_ACCESS_KEY>
# Optional configuration setting to set an AWS IAM region.
#aws_iam_region=None
"""
    return config_data