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
    """Component that implements Resilient function 'fn_aws_iam_remove_user_from_groups"""

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

    @function("fn_aws_iam_remove_user_from_groups")
    def _fn_aws_iam_remove_user_from_groups_function(self, event, *args, **kwargs):
        """Function: Removes the specified IAM user from the specified groups.
        Group names is be a comma separated string of group names.

        param aws_iam_user_name: An IAM user name.
        param aws_iam_group_names: A comma separated list of IAM group names.
        """
        try:
            params = transform_kwargs(kwargs) if kwargs else {}
            # Instantiate result payload object
            rp = ResultPayload(CONFIG_DATA_SECTION, **kwargs)
            # Get the function parameters:
            aws_iam_user_name = kwargs.get("aws_iam_user_name")  # text
            aws_iam_group_names = kwargs.get("aws_iam_group_names")  # text

            LOG.info("aws_iam_user_name: %s", aws_iam_user_name)
            LOG.info("aws_iam_group_names: %s", aws_iam_group_names)

            validate_fields(["aws_iam_user_name", "aws_iam_group_names"], kwargs)

            iam_cli = AwsIamClient(self.options)
            # Pop 'GroupNames' parameter from params.
            if "GroupNames" in params:
                del params["GroupNames"]
            # Get user groups
            user_groups = iam_cli.get("list_groups_for_user", paginate=True, UserName=aws_iam_user_name)
            rtn = []
            # Iterate over group names in the comma separated list in parameter 'aws_iam_group_names'. For each group,
            # if the group exists, add to the 'params' dict then attempt to remove the user in parameter
            # 'aws_iam_user_name' from the group. Include the status of each attempt in the returned result.
            for group_name in re.split(r"\s*,\s*", aws_iam_group_names):
                # Test that the user is a member of the group.
                if user_groups:
                    group = [group for group in user_groups if group["GroupName"] == group_name][0]

                if not user_groups or not group:
                    raise ValueError("User '{0}' is not a member of group '{1}'.".format(aws_iam_user_name, group_name))

                params.update({"GroupName": group_name})
                rtn.append({
                    "GroupName": group_name,
                    "Status": iam_cli.post("remove_user_from_group", **params)
                })

            results = rp.done(True, rtn)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)

        except Exception as aws_err:
            LOG.exception("ERROR with Exception '%s' in Resilient Function for AWS IAM.", aws_err.__repr__())
            yield FunctionError()
