# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, FunctionResult, FunctionError
from resilient_lib import ResultPayload, validate_fields
from fn_aws_iam.lib.aws_iam_client import AwsIamClient
from fn_aws_iam.lib.helpers import CONFIG_DATA_SECTION, transform_kwargs, validate_opts

LOG = logging.getLogger(__name__)

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_aws_iam_list_mfa_devices'"""

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

    @function("fn_aws_iam_list_mfa_devices")
    def _fn_aws_iam_list_mfa_devices_function(self, event, *args, **kwargs):
        """Function: List the MFA devices associated with an IAM user also determine which of the associated MFA
        devices is a virtual device.

        param aws_iam_user_name: An IAM user name.
        """
        try:
            params = transform_kwargs(kwargs) if kwargs else {}
            # Instantiate result payload object
            rp = ResultPayload(CONFIG_DATA_SECTION, **kwargs)

            aws_iam_user_name = kwargs.get("aws_iam_user_name")  # text

            LOG.info("aws_iam_user_name: %s", aws_iam_user_name)

            validate_fields(["aws_iam_user_name"], kwargs)

            iam_cli = AwsIamClient(self.options)

            # Get active mfa devices for user.
            rtn = iam_cli.get("list_mfa_devices", paginate=True, **params)
            if isinstance(rtn, list):
                # Get virtual mfa devices for the account.
                virt_mfas = iam_cli.get("list_virtual_mfa_devices", paginate=True)
                # Determine if active mfa is also a virtual MFA.
                for i in range(len(rtn)):
                    for virt_mfa in virt_mfas:
                        if rtn[i]["SerialNumber"] == virt_mfa["SerialNumber"]:
                            rtn[i]["is_virtual"] = True

            results = rp.done(True, rtn)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)

        except Exception as aws_err:
            LOG.exception("ERROR with Exception '%s' in Resilient Function for AWS IAM.", aws_err.__repr__())
            yield FunctionError()
