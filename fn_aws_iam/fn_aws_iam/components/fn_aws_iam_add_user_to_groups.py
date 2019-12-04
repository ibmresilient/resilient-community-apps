# -*- coding: utf-8 -*-
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
    """Component that implements Resilient function 'fn_aws_iam_add_user_to_groups"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_aws_iam", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_aws_iam", {})

    @function("fn_aws_iam_add_user_to_groups")
    def _fn_aws_iam_add_user_to_groups_function(self, event, *args, **kwargs):
        """Function: None"""
        try:
            params = transform_kwargs(kwargs) if kwargs else {}
            # Instantiate result payload object
            rp = ResultPayload(CONFIG_DATA_SECTION, **kwargs)
            # Get the function parameters:
            aws_iam_user_name = kwargs.get("aws_iam_user_name")  # text
            aws_iam_group_names = kwargs.get("aws_iam_group_names")  # text

            log = logging.getLogger(__name__)
            log.info("aws_iam_user_name: %s", aws_iam_user_name)
            log.info("aws_iam_group_names: %s", aws_iam_group_names)

            validate_fields(["aws_iam_user_name", "aws_iam_group_names"], kwargs)

            iam_cli = AwsIamClient(self.opts, self.options)
            # Pop 'AccessKeys' parameter from params.
            if "GroupNames" in params:
                del params["GroupNames"]

            rtn = []
            for group_name in re.split('\s*,\s*', aws_iam_group_names):
                params.update({"GroupName": group_name})
                rtn.append({
                    "GroupName": group_name,
                    "Status": iam_cli.result_post(iam_cli.iam.add_user_to_group, **params)}
                )

            results = rp.done(True, rtn)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            LOG.exception("Exception in Resilient Function for AWS IAM.")
            yield FunctionError()