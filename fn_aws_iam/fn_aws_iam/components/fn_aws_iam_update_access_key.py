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
    """Component that implements Resilient function 'fn_aws_iam_update_access_key"""

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

    @function("fn_aws_iam_update_access_key")
    def _fn_aws_iam_update_access_key_function(self, event, *args, **kwargs):
        """Function: Update status of an IAM user access key.
        Change the status of an access key from Active to Inactive, or vice versa.

        param aws_iam_user_name: An IAM user name.
        param aws_iam_access_key_id: An IAM user access key id.
        param aws_iam_status: An IAM user access key taget status.
        """
        try:
            params = transform_kwargs(kwargs) if kwargs else {}
            # Instantiate result payload object
            rp = ResultPayload(CONFIG_DATA_SECTION, **kwargs)
            # Get the function parameters:
            aws_iam_user_name = kwargs.get("aws_iam_user_name")  # text
            aws_iam_access_key_id = kwargs.get("aws_iam_access_key_id")  # text
            aws_iam_status = \
                self.get_select_param(kwargs.get("aws_iam_status"))  # select, values: "Active", "Inactive"

            LOG.info("aws_iam_user_name: %s", aws_iam_user_name)
            LOG.info("aws_iam_access_key_id: %s", aws_iam_access_key_id)
            LOG.info("aws_iam_status: %s", aws_iam_status)

            validate_fields(["aws_iam_user_name", "aws_iam_access_key_id", "aws_iam_status"], kwargs)

            iam_cli = AwsIamClient(self.options)

            rtn = iam_cli.post("update_access_key", **params)
            results = rp.done(True, rtn)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)

        except Exception as aws_err:
            LOG.exception("ERROR with Exception '%s' in Resilient Function for AWS IAM.", aws_err.__repr__())
            yield FunctionError()
