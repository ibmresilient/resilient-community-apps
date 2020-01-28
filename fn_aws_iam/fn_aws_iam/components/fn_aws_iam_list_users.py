# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, FunctionResult, FunctionError
from resilient_lib import ResultPayload
from fn_aws_iam.lib.aws_iam_client import AwsIamClient
from fn_aws_iam.lib.helpers import CONFIG_DATA_SECTION, transform_kwargs, validate_opts, is_regex

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
        """Function: Get IAM user or users in the AWS account.  Users can be filtered by user name ,
        group and policy. If the user name is specified get only information for this user.

        param aws_iam_user_name: (optional) An IAM user name.
        param aws_iam_user_filter: (optional) User filter used to refined user data returned.
        param aws_aim_group_filter: (optional)Group filter used to refined user data returned.
        param aws_aim_policy_filter: (optional) Policy filter used to refined user data returned.
        """
        try:
            params = transform_kwargs(kwargs) if kwargs else {}
            # Instantiate result payload object
            rp = ResultPayload(CONFIG_DATA_SECTION, **kwargs)
            # Get the function parameters:
            aws_iam_user_name = kwargs.get("aws_iam_user_name")  # text
            aws_iam_user_filter = kwargs.get("aws_iam_user_filter")  # text
            aws_iam_group_filter = kwargs.get("aws_iam_group_filter")  # text
            aws_iam_policy_filter = kwargs.get("aws_iam_policy_filter")  # text
            aws_iam_access_key_filter = kwargs.get("aws_iam_access_key_filter")  # text
            aws_iam_query_type = \
                self.get_select_param(kwargs.get("aws_iam_query_type"))  # select, values: "users", "access_keys"

            LOG.info("aws_iam_user_name: %s", aws_iam_user_name)
            LOG.info("aws_iam_user_filter: %s", aws_iam_user_filter)
            LOG.info("aws_iam_group_filter: %s", aws_iam_group_filter)
            LOG.info("aws_iam_policy_filter: %s", aws_iam_policy_filter)
            LOG.info("aws_iam_access_key_filter: %s", aws_iam_access_key_filter)
            LOG.info("aws_iam_query_type: %s", aws_iam_query_type)

            # Get a list of all enabled filters.
            enabled_filters = [f for f in [aws_iam_user_filter, aws_iam_group_filter, aws_iam_policy_filter,
                                               aws_iam_access_key_filter] if f is not None]
            # Test any enabled filters to ensure they are valid regular expressions.
            for ef in (enabled_filters):
                if not is_regex(ef):
                    raise ValueError("The query filter '{}' is not a valid regular expression.".format(repr(ef)))

            iam_cli = AwsIamClient(self.options, sts_client=True)
            if aws_iam_user_name:
                # User specified.
                if aws_iam_query_type:
                    # If 'aws_iam_query_type' parameter is in function args remove "QueryType" from 'params'.
                    del params["QueryType"]
                # If a single user result will be add to a list to normalize result.
                rtn = iam_cli.get("get_user", **params)
            else:
                # All users
                # Initialize the filters.
                user_filter, group_filter, policy_filter, access_key_filter = ({} for _ in range(4))
                if aws_iam_user_filter:
                    user_filter["UserName"] = aws_iam_user_filter
                if aws_iam_group_filter:
                    group_filter["GroupName"] = aws_iam_group_filter
                if aws_iam_policy_filter:
                    policy_filter["PolicyName"] = aws_iam_policy_filter
                if aws_iam_access_key_filter:
                    access_key_filter["AccessKeyId"] = aws_iam_access_key_filter
                # Initialize result list.
                rtn_users = []
                rtn_users = iam_cli.get("list_users", paginate=True, results_filter=user_filter, return_filtered=True)
                # The user result will be returned as a tuple of filtered count and filtered user list if a filter
                # is specified . The count is not used.
                # The parameter return_filtered (Boolean) asks the request query to return the filtered result in the
                # result tuple.
                if isinstance(rtn_users, tuple):
                    (_, rtn_users) = rtn_users

                rtn = self.enhance_user_data(rtn_users, iam_cli, aws_iam_query_type, group_filter, policy_filter,
                                             access_key_filter)

            results = rp.done(True, rtn)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)

        except Exception as aws_err:
            LOG.exception("ERROR with Exception '%s' in Resilient Function for AWS IAM.", aws_err.__repr__())
            yield FunctionError()

    @staticmethod
    def enhance_user_data(rtn_users, iam_cli, query_type, group_filter=None, policy_filter=None,
                          access_key_filter=None):
        """ Add additional data for AWS IAM users.

        :param rtn_users: Basic user results list returned from AWS IAM lookup.
        :param iam_cli: The AWS IAM client instance.
        :param group_filter: The group filter applied by the integration.
        :param policy_filter: The group filter applied by the integration.
        :return: Enhanced user results.
        """
        # Boolean to ask the request query to return the filtered result in a result tuple.
        return_filtered = bool(query_type == "access_keys")
        rtn = []
        for i in range(len(rtn_users)):
            user = rtn_users[i]
            # When a filter is defined for groups or polices the 'group_count' or 'policy_count' will be returned in
            # the result as a tuple value. In either case if the count is 'True' i.e. > 0 the user and filtered
            # properties (group or policy) are included in the result, otherwise the user is dropped from the result.
            group_count = 0
            policy_count = 0
            access_key_count = 0
            # Only perform following queries if the list query type is for 'users'
            if query_type and query_type.lower() == "users":
                user_access_key_ids, user_policies, user_groups, user_tags = ([] for _ in range(4))
                # Add extra data for each user. Filtered count is also returned when a filter is defined for groups.
                user_groups = iam_cli.get("list_groups_for_user", paginate=True, UserName=user["UserName"],
                                          results_filter=group_filter)
                # The group result will be returned as a tuple of filtered count and filtered group list if a filter is
                # specified, otherwise it will be a list of groups.
                if isinstance(user_groups, tuple):
                    (group_count, user_groups) = user_groups
                if user_groups:
                    if group_filter and not group_count:
                        # If filter was specified and no filtered count returned drop user entry.
                        continue
                    user["Groups"] = user_groups
                elif group_filter:
                    # If we get no user access groups returned and filter was specified drop user entry.
                    continue
                # Add extra data for each user. Filtered count is also returned when a filter is defined for polices.
                user_policies = iam_cli.get("list_attached_user_policies", paginate=True, UserName=user["UserName"],
                                            results_filter=policy_filter, return_filtered=return_filtered)
                # The policy result will be returned as a tuple of filtered count and filtered policy list if
                # a filter is specified, otherwise it will be a list of policies.
                if isinstance(user_policies, tuple):
                    (policy_count, user_policies) = user_policies
                if user_policies:
                    if policy_filter and not policy_count:
                        # If filter was specified and no filtered count returned drop user entry.
                        continue
                    user["Policies"] = user_policies
                elif policy_filter:
                    # If we get no user policies returned and the filter was specified drop user entry.
                    continue
            # Add extra data for each user. Filtered count is also returned when a filter is defined for polices.
            user_access_key_ids = iam_cli.get("list_access_keys", paginate=True, UserName=user["UserName"],
                                              results_filter=access_key_filter, return_filtered=return_filtered)
            # The access key result will be returned as a tuple of filtered count and filtered access list if a filter
            # is specified, otherwise it will be a list of access keys.
            if isinstance(user_access_key_ids, tuple):
                (access_key_count, user_access_key_ids) = user_access_key_ids
            if user_access_key_ids:
                if access_key_filter and not access_key_count:
                    # If filter was specified and no filtered count returned drop user entry.
                    continue
                for j in range(len(user_access_key_ids)):
                    # Only perform following queries if the list query type is for 'access_keys'.
                    if not query_type or query_type.lower() == "access_keys":
                        user_access_key_ids[j]["key_last_used"] = \
                            iam_cli.get("get_access_key_last_used", AccessKeyId=user_access_key_ids[j]['AccessKeyId'])
                user["AccessKeyIds"] = user_access_key_ids
            elif access_key_filter:
                # If we get no user access keys returned and filter was specified drop user entry.
                continue

            # Only perform following queries if the list query type is for 'users;'.
            if query_type and query_type.lower() == "users":
                user_tags = iam_cli.get("list_user_tags", UserName=user["UserName"])
                if user_tags:
                    user["Tags"] = user_tags

            rtn.append(user)

        return rtn
