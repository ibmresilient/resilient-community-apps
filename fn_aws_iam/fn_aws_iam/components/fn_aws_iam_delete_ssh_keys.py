# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import re
from resilient_circuits import ResilientComponent, function, handler, FunctionResult, FunctionError
from resilient_lib import ResultPayload, validate_fields
from fn_aws_iam.lib.aws_iam_client import AwsIamClient
from fn_aws_iam.lib.helpers import CONFIG_DATA_SECTION, transform_kwargs, validate_opts

LOG = logging.getLogger(__name__)

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_aws_iam_delete_ssh_keys'"""

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

    @function("fn_aws_iam_delete_ssh_keys")
    def _fn_aws_iam_delete_ssh_keys_function(self, event, *args, **kwargs):
        """Function: Delete Secure Shell (SSH) public keys associated with the specified IAM user.

        param aws_iam_user_name: An IAM user name.
        aws_iam_ssh_key_ids: A comma separated list of SSH key ids credential ids.
        """
        try:
            params = transform_kwargs(kwargs) if kwargs else {}
            # Instantiate result payload object
            rp = ResultPayload(CONFIG_DATA_SECTION, **kwargs)

            aws_iam_user_name = kwargs.get("aws_iam_user_name")  # text
            aws_iam_ssh_key_ids = kwargs.get("aws_iam_ssh_key_ids")  # text

            LOG.info("aws_iam_user_name: %s", aws_iam_user_name)
            LOG.info("aws_iam_ssh_key_ids: %s", aws_iam_ssh_key_ids)

            validate_fields(["aws_iam_user_name", "aws_iam_ssh_key_ids"], kwargs)

            iam_cli = AwsIamClient(self.options)

            # Delete 'SshKeyIds' parameter from params.
            if "SshKeyIds" in params:
                del params["SshKeyIds"]

            rtn = []
            for ssh_key_id in re.split(r"\s*,\s*", aws_iam_ssh_key_ids):
                params.update({"SSHPublicKeyId": ssh_key_id})
                rtn.append({
                    "SSHPublicKeyId": ssh_key_id,
                    "Status": iam_cli.post("delete_ssh_public_key", **params)}
                )

            results = rp.done(True, rtn)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)

        except Exception as aws_err:
            LOG.exception("ERROR with Exception '%s' in Resilient Function for AWS IAM.", aws_err.__repr__())
            yield FunctionError()
