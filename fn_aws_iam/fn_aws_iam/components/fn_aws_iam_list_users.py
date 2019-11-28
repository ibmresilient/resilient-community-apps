# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import copy

from resilient_circuits import ResilientComponent, function, handler, FunctionResult, FunctionError
from resilient_lib import ResultPayload
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
            aws_iam_user_filter = kwargs.get("aws_iam_user_filter")  # text
            aws_iam_group_filter = kwargs.get("aws_iam_group_filter")  # text
            aws_iam_policy_filter = kwargs.get("aws_iam_policy_filter")  # text

            LOG.info("aws_iam_user_name: %s", aws_iam_user_name)
            LOG.info("aws_iam_user_filter: %s", aws_iam_user_filter)
            LOG.info("aws_iam_group_filter: %s", aws_iam_group_filter)
            LOG.info("aws_iam_policy_filter: %s", aws_iam_policy_filter)

            iam = AwsIamClient(self.opts, self.options, sts_client=True)
            if aws_iam_user_name:
                # User specified.
                rtn = iam.get_user(**params)
                # If a single user add to a list to normalize result.
            else:
                filter = {}
                if aws_iam_user_filter:
                    filter["UserName"] = aws_iam_user_filter
                if aws_iam_group_filter:
                    filter["GroupName"] = aws_iam_group_filter
                if aws_iam_policy_filter:
                    filter["PolicyName"] = aws_iam_policy_filter

                # All users
                (filtered_count, rtn_users) = iam.result_paginator("list_users", filter=filter)
                rtn = []
                for i in range(len(rtn_users)):
                    user = rtn_users[i]
                    group_count = policy_count = 0
                    user_access_key_ids = user_policies = user_groups = user_tags = []
                    # Add extra data for each user. Filtered count is also returned in certain instances.
                    (group_count, user_groups) = iam.result_paginator("list_groups_for_user", UserName=user["UserName"], filter=filter)
                    if user_groups:
                        if aws_iam_group_filter and not group_count:
                            continue
                        else:
                            user["Groups"] = user_groups
                    elif aws_iam_group_filter:
                        continue

                    (policy_count, user_policies) = iam.result_paginator("list_attached_user_policies", UserName=user["UserName"], filter=filter)
                    if user_policies:
                        if aws_iam_policy_filter and not policy_count:
                            continue
                        else:
                            user["Policies"] = user_policies
                    elif aws_iam_policy_filter:
                        continue

                    (_, user_access_key_ids) = iam.result_paginator("list_access_keys", UserName=user["UserName"])
                    if user_access_key_ids:
                        user["AccessKeyIds"] = user_access_key_ids

                    user_tags = iam.list_user_tags(UserName=user["UserName"])
                    if user_tags:
                        user["Tags"] = user_tags
                    rtn.append(user)

            results = rp.done(True, rtn)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)

        except Exception:
            LOG.exception("Exception in Resilient Function for AWS IAM.")
            yield FunctionError()
