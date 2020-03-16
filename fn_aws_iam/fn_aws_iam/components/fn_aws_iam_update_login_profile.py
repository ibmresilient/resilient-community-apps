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
    """Component that implements Resilient function 'fn_aws_iam_update_login_profile"""

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

    @function("fn_aws_iam_update_login_profile")
    def _fn_aws_iam_update_login_profile_function(self, event, *args, **kwargs):
        """Function: Change the password for the specified IAM user.

        param aws_iam_user_name: An IAM user name.
        param aws_iam_password: A new password for an IAM user.
        param aws_iam_password_reset_required: A boolean value to determine whether a password reset should
        be required on change.
        """
        try:
            params = transform_kwargs(kwargs) if kwargs else {}
            # Instantiate result payload object
            rp = ResultPayload(CONFIG_DATA_SECTION, **kwargs)
            # Get the function parameters:
            aws_iam_user_name = kwargs.get("aws_iam_user_name")  # text
            aws_iam_password = kwargs.get("aws_iam_password")  # text
            aws_iam_password_reset_required = kwargs.get("aws_iam_password_reset_required")  # boolean

            LOG.info("aws_iam_user_name: %s", aws_iam_user_name)
            # Hide password fro logger.
            LOG.info("aws_iam_password: %s", "***")
            LOG.info("aws_iam_password_reset_required: %s", aws_iam_password_reset_required)

            validate_fields(["aws_iam_user_name", "aws_iam_password", "aws_iam_password_reset_required"], kwargs)


            iam_cli = AwsIamClient(self.options)

            rtn = iam_cli.post("update_login_profile", **params)

            results = rp.done(True, rtn)
            # Hide password in result.
            results["inputs"]["aws_iam_password"] = "***"
            # Produce a FunctionResult with the results
            yield FunctionResult(results)

        except Exception as aws_err:
            LOG.exception("ERROR with Exception '%s' in Resilient Function for AWS IAM.", aws_err.__repr__())
            yield FunctionError()
