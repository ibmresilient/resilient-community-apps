# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# pragma pylint: disable=unused-argument, line-too-long, wrong-import-order

"""AppFunction implementation"""
from datetime import datetime
from fn_github.lib.client_helper import GitHubHelper
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields

PACKAGE_NAME = "fn_github"
FN_NAME = "github_get_commits"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'github_get_commits'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Get commit history for a repository or a specific file
        Inputs:
            -   fn_inputs.github_owner
            -   fn_inputs.github_repo
            -   fn_inputs.github_optional_file_path
            -   fn_inputs.github_until_date
            -   fn_inputs.github_since_date
            -   fn_inputs.github_branch
            -   fn_inputs.github_limit
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        validate_fields([{"name": "base_url", "placeholder": "<https://base-url>"}],
            self.app_configs)

        validate_fields(["github_owner", "github_repo"], fn_inputs)

        gh = GitHubHelper(self.app_configs._asdict())

        inputs = fn_inputs._asdict()
        # convert dates
        for date_ms in ["github_until_date", "github_since_date"]:
            if inputs.get(date_ms):
                inputs[date_ms] = datetime.fromtimestamp(inputs[date_ms]/1000).isoformat()

        commits, err_msg = gh.get_commits(inputs)

        results = []
        if commits:
            results = [commit.sha for commit in commits]

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        yield FunctionResult(results, success=bool(results), reason=err_msg)
