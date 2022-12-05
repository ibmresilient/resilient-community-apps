# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# pragma pylint: disable=unused-argument, line-too-long, wrong-import-order

"""AppFunction implementation"""
from fn_github.lib.client_helper import GitHubHelper
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields

PACKAGE_NAME = "fn_github"
FN_NAME = "github_get_release"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'github_get_release'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: None
        Inputs:
            -   fn_inputs.github_owner
            -   fn_inputs.github_repo
            -   fn_inputs.github_release_tag
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        validate_fields([{"name": "base_url", "placeholder": "<https://base-url>"}],
            self.app_configs)

        validate_fields(["github_owner", "github_repo", "github_release_tag"], fn_inputs)

        gh = GitHubHelper(self.app_configs._asdict())

        results, err_msg = gh.get_release(fn_inputs)

        if results:
            results = results.as_dict()

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        yield FunctionResult(results, success=bool(results), reason=err_msg)
