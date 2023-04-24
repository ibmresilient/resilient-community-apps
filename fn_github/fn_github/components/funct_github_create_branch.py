# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# pragma pylint: disable=unused-argument, line-too-long, wrong-import-order

"""AppFunction implementation"""
from fn_github.lib.client_helper import GitHubHelper
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields

PACKAGE_NAME = "fn_github"
FN_NAME = "github_create_branch"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'github_create_branch'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: None
        Inputs:
            -   fn_inputs.github_owner
            -   fn_inputs.github_repo
            -   fn_inputs.github_branch
            -   fn_inputs.github_based_on_branch_or_sha
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        validate_fields(["github_owner", "github_repo", "github_based_on_branch_or_sha", "github_branch"], fn_inputs)

        gh = GitHubHelper(fn_inputs.github_owner, fn_inputs.github_repo, self.options)
        if gh.repo_err:
            yield FunctionResult(None, success=False, reason=gh.repo_err)
        else:
            results, err_msg = gh.create_branch(fn_inputs.github_branch,
                                                fn_inputs.github_based_on_branch_or_sha)

            if results:
                results = {"ref": results.ref}

            yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

            yield FunctionResult(results if results else {}, success=bool(results), reason=err_msg)
