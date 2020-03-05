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
    """Component that implements Resilient function 'fn_aws_iam_delete_access_keys"""

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

    @function("fn_aws_iam_delete_access_keys")
    def _fn_aws_iam_delete_access_keys_function(self, event, *args, **kwargs):
        """Function: Delete the access key pairs associated with the specified IAM user.

        :param aws_iam_user_name: An IAM user name.
        :param aws_iam_access_keys: A comma separated list of IAM access key ids.
        """
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

            iam_cli = AwsIamClient(self.options)
            # Pop 'AccessKeys' parameter from params.
            if "AccessKeys" in params:
                del params["AccessKeys"]

            rtn = []
            # Iterate over access key ids in the comma separated list in parameter 'aws_iam_access_keys'. Add each in
            # turn to the 'params' dict then attempt to delete each access key for the user in parameter
            # 'aws_iam_user_name'. Include the status of each attempt in the returned result.
            for ak_id in re.split(r"\s*,\s*", aws_iam_access_keys):
                params.update({"AccessKeyId": ak_id})
                rtn.append({
                    "AccessKeyId": ak_id,
                    "Status": iam_cli.post("delete_access_key", **params)}
                )

            results = rp.done(True, rtn)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)

        except Exception as aws_err:
            LOG.exception("ERROR with Exception '%s' in Resilient Function for AWS IAM.", aws_err.__repr__())
            yield FunctionError()

