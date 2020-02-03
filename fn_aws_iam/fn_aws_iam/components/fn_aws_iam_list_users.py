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
        param aws_iam_access_key_filter: (optional) Policy filter used to refined user data returned.
        param aws_iam_query_type: (optional) Policy filter used to determin type of query.
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
            for ef in enabled_filters:
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
                # is specified. The count is not used.
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
        :param query_type: The query type to be executed can be either "users" or "access_keys".
        :param group_filter: The group filter applied by the integration.
        :param policy_filter: The group filter applied by the integration.
        :param access_key_filter: The group filter applied by the integration.
        :return: Enhanced user results.
        """
        # Boolean to ask the request query to return the filtered result instead of full result in a result tuple.
        return_filtered = bool(query_type == "access_keys")
        rtn = []
        # Get a shortcut to this class.
        cls = FunctionComponent
        user_access_key_ids, user_policies, user_groups, user_tags = ([] for _ in range(4))
        # Property query lookup table.
        prop_params = [
            ["Groups", "list_groups_for_user", group_filter, user_groups],
            ["Policies", "list_attached_user_policies", policy_filter, user_policies],
            ["AccessKeyIds", "list_access_keys", access_key_filter, user_access_key_ids],
            ["Tags", "list_user_tags", None, user_tags]
        ]
        for i in range(len(rtn_users)):
            skip_prop = False
            user = rtn_users[i]
            user_name = user["UserName"]
            # When a filter is defined for groups, polices or access key ids the 'group_count', 'policy_count' or
            # 'access_key_filter' will be returned in the result as a tuple value. In all casees if the count is
            # 'True' i.e. > 0 the user and non-filtered properties (groups, policies, access key ids) are included in
            # the result, otherwise the user is dropped from the result.
            for prop_param in prop_params:
                # Don't perform property lookup if query_type = "access_keys" and the query is for groups, policies
                # or tags.
                if query_type and query_type.lower() == "access_keys" and prop_param[0] in ["Groups", "Policies",
                                                                                            "Tags"]:
                    pass
                else:
                    user_access_key_ids, user_policies, user_groups, user_tags = ([] for _ in range(4))
                    (skip_prop, prop_param[3]) = cls.process_user_property(iam_cli, prop_param[1], user_name,
                                                                            prop_param[2], return_filtered)
                    if skip_prop:
                        break
                    if prop_param[3]:
                        if prop_param[0] == "AccessKeyIds":
                            for j in range(len(prop_param[3])):
                                # Only perform following queries if the list query type is for 'access_keys'.
                                if not query_type or query_type.lower() == "access_keys":
                                    prop_param[3][j]["key_last_used"] = \
                                        iam_cli.get("get_access_key_last_used",
                                                    AccessKeyId=prop_param[3][j]['AccessKeyId'])
                        user[prop_param[0]] = prop_param[3]
            # Skip user if boolean is set to 'True' in inner loop.
            if skip_prop:
                continue

            rtn.append(user)

        return rtn


    @staticmethod
    def process_user_property(iam_cli, op, user_name, results_filter, return_filtered):
        """ Get properties data for AWS IAM users.
        Properties can be any of groups, policies, access key ids or tags.

        :param iam_cli: The AWS IAM client instance.
        :param op: The AWS IAM op to execute.
        :param user_name: The AWS IAM user name.
        :param results_filter: The user property filter for groups, policies or access key ids.
        :param return_filtered: Boolean to indicate where full or filtered result should be returned.
        :return: User properties for groups, policies or access key ids.
        """
        skip_prop = False
        prop_count = 0
        user_prop = iam_cli.get(op, paginate=True, UserName=user_name, results_filter=results_filter,
                                return_filtered=return_filtered)
        # Filtered count can also be returned when a filter is defined for the property query.
        # The result will be returned as a tuple of filtered count and filtered property list if a filter is
        # specified, otherwise it will be a list of properties of type specified by AWS IAM query op.
        if isinstance(user_prop, tuple):
            (prop_count, user_prop) = user_prop

        if user_prop:
            # A property list is returned for the query.
            if results_filter and not prop_count:
                # If we get here we get a property list and have no property count.
                # However a filter was specified so return 'True' to skip entry.
                skip_prop = True
        elif results_filter:
            # An empty list can be a legitimate result, however if we get here and we specified a filter but no property
            # list was returned return 'True' to skip entry.
            skip_prop = True

        return (skip_prop, user_prop)
