# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import re
from resilient_circuits import ResilientComponent, function, handler, FunctionResult, FunctionError
from resilient_lib import ResultPayload
from fn_aws_iam.lib.aws_iam_client import AwsIamClient
from fn_aws_iam.lib.helpers import CONFIG_DATA_SECTION, transform_kwargs, validate_opts

LOG = logging.getLogger(__name__)

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_aws_iam_detach_user_policies"""

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

    @function("fn_aws_iam_detach_user_policies")
    def _fn_aws_iam_detach_user_policies_function(self, event, *args, **kwargs):
        """Function: Remove the specified managed policy from the specified IAM user.

        Note: A user can also have inline policies embedded with it, this function will delete inline
        policies associated with the the user. Parameter aws_iam_user_name is an IAM user name.
        Note: one of parameters aws_iam_policy_names or aws_iam_arns required to be set.

        param aws_iam_policy_names: (optional) A comma separated  list of IAM policy names.
        param aws_iam_arns: (optional) A comma separated list of IAM policy arns.
        """
        try:
            params = transform_kwargs(kwargs) if kwargs else {}
            # Instantiate result payload object
            rp = ResultPayload(CONFIG_DATA_SECTION, **kwargs)
            # Get the function parameters:
            aws_iam_user_name = kwargs.get("aws_iam_user_name")  # text
            aws_iam_policy_names = kwargs.get("aws_iam_policy_names")  # text
            aws_iam_arns = kwargs.get("aws_iam_arns")  # text

            LOG.info("aws_iam_user_name: %s", aws_iam_user_name)
            LOG.info("aws_iam_policy_names: %s", aws_iam_policy_names)
            LOG.info("aws_iam_arns: %s", aws_iam_arns)

            if not aws_iam_policy_names and not aws_iam_arns:
                raise ValueError("Expected either parameter '{0}' or '{1}' to be set."
                                 .format("aws_iam_policy_names", "aws_iam_arns"))
            if all([aws_iam_policy_names, aws_iam_arns]):
                raise ValueError("Expected only one of parameters '{0}' or '{1}' to be set."
                                 .format("aws_iam_policy_names", "aws_iam_arns"))
            iam_cli = AwsIamClient(self.options)
            rtn = []
            if aws_iam_policy_names:
                # Delete 'PolicyNames' from params
                del params["PolicyNames"]
                # Get user policies
                user_policies = iam_cli.get("list_attached_user_policies", paginate=True, UserName=aws_iam_user_name)
                inline_policies = iam_cli.get("list_user_policies", paginate=True, UserName=aws_iam_user_name)
                # Iterate over policy names in the comma separated list in parameter 'aws_iam_policy_names'. Add each
                # in turn to the 'params' dict then attempt to detach each policy from the user in parameter
                # 'aws_iam_user_name'. Include the status of each attempt in the returned result.
                for policy_name in re.split(r"\s*,\s*", aws_iam_policy_names):
                    # Test if policy_name is attached for user name and get arn.
                    if inline_policies and policy_name in [ip["PolicyName"] for ip in inline_policies]:
                        if "PolicyArn" in params:
                            # Delete 'PolicyArn' from 'params' if in-line policy.
                            del params["PolicyArn"]
                        # Policy is an in-line policy delete instead.
                        params.update({"PolicyName": policy_name})
                        rtn.append({"PolicyName": policy_name, "Status": iam_cli.post("delete_user_policy", **params)})
                    elif user_policies:
                        if "PolicyName" in params:
                            # Delete 'PolicyName' from 'params' if managed policy.
                            del params["PolicyName"]
                        # Detach managed policies instead of deleting.
                        policy_list = [policy for policy in user_policies if policy["PolicyName"] == policy_name]

                        if not user_policies or not policy_list:
                            raise ValueError("Policy with name '{0}' not attached for user '{1}'."
                                             .format(policy_name, aws_iam_user_name))
                        policy = policy_list[0]
                        params.update({"PolicyArn": policy["PolicyArn"]})
                        rtn.append({"PolicyName": policy_name, "Status": iam_cli.post("detach_user_policy", **params)})
            else:
                # Delete 'Arn' from params
                del params["Arns"]
                # Iterate over policy arns in the comma separated list in parameter 'aws_iam_arns'. Add each in turn
                # to the 'params' dict then attempt to detach each policy to the user in parameter
                # 'aws_iam_user_name'. Include the status of each attempt in the returned result.
                for arn in re.split(r"\s*,\s*", aws_iam_arns):
                    params.update({"PolicyArn": arn})
                    rtn.append({
                        "PolicyArn": arn,
                        "Status": iam_cli.post("detach_user_policy", **params)}
                    )

            results = rp.done(True, rtn)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)

        except Exception as aws_err:
            LOG.exception("ERROR with Exception '%s' in Resilient Function for AWS IAM.", aws_err.__repr__())
            yield FunctionError()
