# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
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

            iam_cli = AwsIamClient(self.opts, self.options, sts_client=True)
            if aws_iam_user_name:
                # User specified.
                rtn = iam_cli.get("get_user", **params)
                # If a single user add to a list to normalize result.
            else:
                # All users
                # Initialize the filters.
                user_filter, group_filter, policy_filter = ({} for _ in range(3))
                if aws_iam_user_filter:
                    user_filter["UserName"] = aws_iam_user_filter
                if aws_iam_group_filter:
                    group_filter["GroupName"] = aws_iam_group_filter
                if aws_iam_policy_filter:
                    policy_filter["PolicyName"] = aws_iam_policy_filter
                # Initialize result list.
                rtn_users = []
                rtn_users = iam_cli.get("list_users", paginate=True, results_filter=user_filter)
                # The user result will be returned as a tuple of filtered count and filtered user list if a filter
                # is specified . The count is not used.
                if isinstance(rtn_users, tuple):
                    (_, rtn_users) = rtn_users

                rtn = self.enhance_user_data(rtn_users, iam_cli, group_filter, policy_filter)

            results = rp.done(True, rtn)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)

        except Exception:
            LOG.exception("Exception in Resilient Function for AWS IAM.")
            yield FunctionError()

    @staticmethod
    def enhance_user_data(rtn_users, iam_cli, group_filter=None, policy_filter=None):
        """ Add additional data for AWS IAM users.

        :param rtn_users: Basic user results list returned from AWS IAM lookup.
        :param iam_cli: The AWS IAM client instance.
        :param group_filter: The group filter applied by the integration.
        :param policy_filter: The group filter applied by the integration.
        :return: Enhanced user results.
        """
        rtn = []
        for i in range(len(rtn_users)):
            user = rtn_users[i]
            group_count = 0
            policy_count = 0
            user_access_key_ids, user_policies, user_groups, user_tags = ([] for _ in range(4))
            # Add extra data for each user. Filtered count is also returned in certain instances.
            user_groups = iam_cli.get("list_groups_for_user", paginate=True, UserName=user["UserName"],
                                      results_filter=group_filter)
            # The group result will be returned as a tuple of filtered count and group list if a filter is
            # specified, otherwise it will be a list of groups.
            if isinstance(user_groups, tuple):
                (group_count, user_groups) = user_groups
            if user_groups:
                if group_filter and not group_count:
                    continue
                user["Groups"] = user_groups
            elif group_filter:
                continue
            user_policies = iam_cli.get("list_attached_user_policies", paginate=True,
                                        UserName=user["UserName"], results_filter=policy_filter)
            # The policy result will be returned as a tuple of filtered count and policy list if a filter is
            # specified, otherwise it will be a list of policies.
            if isinstance(user_policies, tuple):
                (policy_count, user_policies) = user_policies
            if user_policies:
                if policy_filter and not policy_count:
                    continue
                user["Policies"] = user_policies
            elif policy_filter:
                continue

            user_access_key_ids = iam_cli.get("list_access_keys", paginate=True, UserName=user["UserName"])
            if user_access_key_ids:
                user["AccessKeyIds"] = user_access_key_ids
            user_tags = iam_cli.get("list_user_tags", UserName=user["UserName"])
            if user_tags:
                user["Tags"] = user_tags

            rtn.append(user)

        return rtn
