# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload, validate_fields
from fn_aws_iam.lib.aws_iam_client import AwsIamClient
from fn_aws_iam.lib.helpers import CONFIG_DATA_SECTION, transform_kwargs, validate_opts

LOG = logging.getLogger(__name__)

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_aws_iam_list_users"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_aws_iam", {})
        validate_opts(self)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_aws_iam", {})
        validate_opts(self)

    @function("fn_aws_iam_list_users")
    def _fn_aws_iam_list_users_function(self, event, *args, **kwargs):
        """Function: None"""
        try:
            params = transform_kwargs(kwargs) if kwargs else {}
            # Instantiate result payload object
            rp = ResultPayload(CONFIG_DATA_SECTION, **kwargs)
            # Get the function parameters:
            aws_iam_user_name = kwargs.get("aws_iam_user_name")  # text

            LOG.info("aws_iam_user_name: %s", aws_iam_user_name)

            iam = AwsIamClient(self.opts, self.options, sts_client=True)
            if aws_iam_user_name:
                # User specified.
                rtn = iam.get_user(**params)
                # If a single user add to a list to normalize result.
            else:
                # All users
                rtn = iam.result_paginator("list_users")
                for i in range(len(rtn)):
                    # Add tags and groups for each user.
                    user_tags = iam.list_user_tags(UserName=rtn[i]["UserName"])
                    user_groups = iam.result_paginator("list_groups_for_user", UserName=rtn[i]["UserName"])
                    if len(user_tags) > 0:
                        rtn[i]["Tags"] = user_tags
                    if len(user_groups) > 0:
                        rtn[i]["Groups"] = user_groups

            results = rp.done(True, rtn)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)

        except Exception:
            LOG.exception("Exception in Resilient Function for AWS IAM.")
            yield FunctionError()

