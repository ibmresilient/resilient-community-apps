# -*- coding: utf-8 -*-
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
        """Function: None"""
        try:
            params = transform_kwargs(kwargs) if kwargs else {}
            # Instantiate result payload object
            rp = ResultPayload(CONFIG_DATA_SECTION, **kwargs)
            # Get the function parameters:
            aws_iam_user_name = kwargs.get("aws_iam_user_name")  # text
            aws_iam_policy_names = kwargs.get("aws_iam_policy_names")  # text
            aws_iam_arns = kwargs.get("aws_iam_arns")  # text

            log = logging.getLogger(__name__)
            log.info("aws_iam_user_name: %s", aws_iam_user_name)
            log.info("aws_iam_policy_names: %s", aws_iam_policy_names)
            log.info("aws_iam_arns: %s", aws_iam_arns)

            if not aws_iam_policy_names and not aws_iam_arns:
                raise ValueError("Expected either parameter '{0}' or '{1}' to be set."
                                 .format("aws_iam_policy_names", "aws_iam_arns"))
            if all([aws_iam_policy_names, aws_iam_arns]):
                raise ValueError("Expected only one of parameters '{0}' or '{1}' to be set."
                                 .format("aws_iam_policy_names", "aws_iam_arns"))
            iam_cli = AwsIamClient(self.opts, self.options)
            rtn = []
            if aws_iam_policy_names:
                # Delete 'PolicyNames' from params
                del params["PolicyNames"]
                # Get user policies
                user_policies = iam_cli.get("list_attached_user_policies", paginate=True, UserName=aws_iam_user_name)
                # Test if policy_names are attached for user name and get arn.
                for policy_name in re.split(r"\s*,\s*", aws_iam_policy_names):
                    if user_policies:
                        policy = [policy for policy in user_policies if policy["PolicyName"] == policy_name][0]

                    if not user_policies or not policy:
                        raise ValueError("Policy with name '{0}' not attached for user '{1}'."
                                         .format(policy_name, aws_iam_user_name))

                    params.update({"PolicyArn": policy["PolicyArn"]})
                    rtn.append({"PolicyName": policy_name,
                                "Status": iam_cli.post(iam_cli.iam.detach_user_policy, **params)})
            else:
                # Delete 'Arn' from params
                del params["Arns"]
                for arn in re.split(r"\s*,\s*", aws_iam_arns):
                    params.update({"PolicyArn": arn})
                    rtn.append({
                        "PolicyArn": arn,
                        "Status": iam_cli.post(iam_cli.iam.detach_user_policy, **params)}
                    )

            results = rp.done(True, rtn)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            LOG.exception("Exception in Resilient Function for AWS IAM.")
            yield FunctionError()
