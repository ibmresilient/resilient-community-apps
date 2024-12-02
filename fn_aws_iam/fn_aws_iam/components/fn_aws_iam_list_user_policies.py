# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, FunctionResult, FunctionError
from resilient_lib import ResultPayload, validate_fields
from fn_aws_iam.lib.aws_iam_client import AwsIamClient
from fn_aws_iam.lib.helpers import CONFIG_DATA_SECTION, transform_kwargs, validate_opts

LOG = logging.getLogger(__name__)

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_aws_iam_list_user_policies"""

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

    @function("fn_aws_iam_list_user_policies")
    def _fn_aws_iam_list_user_policies_function(self, event, *args, **kwargs):
        """Function: Get all managed policies and in-line policies that are attached to the specified IAM user.

        param aws_iam_user_name: An IAM user name.
        """
        try:
            params = transform_kwargs(kwargs) if kwargs else {}
            # Instantiate result payload object
            rp = ResultPayload(CONFIG_DATA_SECTION, **kwargs)
            # Get the function parameters:
            aws_iam_user_name = kwargs.get("aws_iam_user_name")  # text

            LOG.info("aws_iam_user_name: %s", aws_iam_user_name)

            validate_fields(["aws_iam_user_name"], kwargs)

            iam_cli = AwsIamClient(self.options)
            # Get user managed policies.
            rtn = iam_cli.get("list_attached_user_policies", paginate=True, **params)
            # Add user in-line policies at beginning of result.
            for user_policy in iam_cli.get("list_user_policies", paginate=True, **params):
                rtn[:0] = [user_policy]

            results = rp.done(True, rtn)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)

        except Exception as aws_err:
            LOG.exception("ERROR with Exception '%s' in Resilient Function for AWS IAM.", aws_err.__repr__())
            yield FunctionError()
