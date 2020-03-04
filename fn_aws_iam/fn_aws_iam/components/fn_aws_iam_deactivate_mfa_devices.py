# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import re

from fn_aws_iam.lib.aws_iam_client import AwsIamClient
from fn_aws_iam.lib.helpers import CONFIG_DATA_SECTION, transform_kwargs, validate_opts
from resilient_circuits import ResilientComponent, function, handler, FunctionResult, FunctionError
from resilient_lib import ResultPayload, validate_fields

LOG = logging.getLogger(__name__)

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_aws_iam_deactivate_mfa_devices'"""

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

    @function("fn_aws_iam_deactivate_mfa_devices")
    def _fn_aws_iam_deactivate_mfa_devices_function(self, event, *args, **kwargs):
        """Function: Deactivate an MFA device and remove it from association with the user name for which it
        was originally enabled.

        param aws_iam_user_name: An IAM user name.
        param aws_iam_mfa_serial_numbers: A comma separated list of IAM MFA serial numbers or arns.
        """
        try:
            params = transform_kwargs(kwargs) if kwargs else {}
            # Instantiate result payload object
            rp = ResultPayload(CONFIG_DATA_SECTION, **kwargs)

            aws_iam_user_name = kwargs.get("aws_iam_user_name")  # text
            aws_iam_mfa_serial_nums = kwargs.get("aws_iam_mfa_serial_nums")  # text

            LOG.info("aws_iam_user_name: %s", aws_iam_user_name)
            LOG.info("aws_iam_mfa_serial_nums: %s", aws_iam_mfa_serial_nums)

            validate_fields(["aws_iam_user_name", "aws_iam_mfa_serial_nums"], kwargs)

            iam_cli = AwsIamClient(self.options)
            # Delete 'MfaSerialNums' parameter from params.
            if "MfaSerialNums" in params:
                del params["MfaSerialNums"]

            rtn = []
            for mfa_ser_num in re.split(r"\s*,\s*", aws_iam_mfa_serial_nums):
                params.update({"SerialNumber": mfa_ser_num})
                rtn.append({
                    "SerialNumber": mfa_ser_num,
                    "Status": iam_cli.post("deactivate_mfa_device", **params)}
                )

            results = rp.done(True, rtn)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)

        except Exception as aws_err:
            LOG.exception("ERROR with Exception '%s' in Resilient Function for AWS IAM.", aws_err.__repr__())
            yield FunctionError()
