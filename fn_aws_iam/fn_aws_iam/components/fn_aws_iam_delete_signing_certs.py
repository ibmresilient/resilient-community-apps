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
    """Component that implements Resilient function 'fn_aws_iam_delete_signing_certs'"""

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

    @function("fn_aws_iam_delete_signing_certs")
    def _fn_aws_iam_delete_signing_certs_function(self, event, *args, **kwargs):
        """Function: Delete signing certificates associated with the specified IAM user.

        param aws_iam_user_name: An IAM user name.
        param aws_iam_sign_cert_ids: A comma separated list of signing certificate ids
        """
        try:
            params = transform_kwargs(kwargs) if kwargs else {}
            # Instantiate result payload object
            rp = ResultPayload(CONFIG_DATA_SECTION, **kwargs)

            aws_iam_user_name = kwargs.get("aws_iam_user_name")  # text
            aws_iam_sign_cert_ids = kwargs.get("aws_iam_sign_cert_ids")  # text

            LOG.info("aws_iam_user_name: %s", aws_iam_user_name)
            LOG.info("aws_iam_sign_cert_ids: %s", aws_iam_sign_cert_ids)

            validate_fields(["aws_iam_user_name", "aws_iam_sign_cert_ids"], kwargs)

            iam_cli = AwsIamClient(self.options)
            # Delete 'SignCertIds' parameter from params.
            if "SignCertIds" in params:
                del params["SignCertIds"]

            rtn = []
            for scert_id in re.split(r"\s*,\s*", aws_iam_sign_cert_ids):
                params.update({"CertificateId": scert_id})
                rtn.append({
                    "CertificateId": scert_id,
                    "Status": iam_cli.post("delete_signing_certificate", **params)}
                )

            results = rp.done(True, rtn)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)

        except Exception as aws_err:
            LOG.exception("ERROR with Exception '%s' in Resilient Function for AWS IAM.", aws_err.__repr__())
            yield FunctionError()
