# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import re
from resilient_circuits import ResilientComponent, function, handler, FunctionResult, FunctionError
from resilient_lib import ResultPayload, validate_fields
from fn_aws_iam.lib.aws_iam_client import AwsIamClient
from fn_aws_iam.lib.helpers import CONFIG_DATA_SECTION, transform_kwargs

LOG = logging.getLogger(__name__)

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_aws_iam_delete_access_keys"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_aws_iam", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_aws_iam", {})

    @function("fn_aws_iam_delete_access_keys")
    def _fn_aws_iam_delete_access_keys_function(self, event, *args, **kwargs):
        """Function: None"""
        try:
            params = transform_kwargs(kwargs) if kwargs else {}
            # Instantiate result payload object
            rp = ResultPayload(CONFIG_DATA_SECTION, **kwargs)
            # Get the function parameters:
            aws_iam_user_name = kwargs.get("aws_iam_user_name")  # text
            aws_iam_access_keys = kwargs.get("aws_iam_access_keys")  # text

            LOG.info("aws_iam_user_name: %s", aws_iam_user_name)
            LOG.info("aws_iam_access_keys: %s", aws_iam_access_keys)

            validate_fields(["aws_iam_user_name", "aws_iam_access_keys"], kwargs)

            iam_cli = AwsIamClient(self.opts, self.options)
            # Pop 'AccessKeys' parameter from params.
            if "AccessKeys" in params:
                del params["AccessKeys"]

            rtn = []
            for ak_id in re.split('\s*,\s*', aws_iam_access_keys):
                params.update({"AccessKeyId": ak_id})
                rtn.append({
                    "AccessKeyId": ak_id,
                    "Status": iam_cli.result_post(iam_cli.iam.delete_access_key, **params)}
                )

            results = rp.done(True, rtn)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            LOG.exception("Exception in Resilient Function for AWS IAM.")
            yield FunctionError()
