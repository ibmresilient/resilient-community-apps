# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# pragma pylint: disable=unused-argument, line-too-long, wrong-import-order

from fn_github.lib.client_helper import GitHubHelper
from resilient_lib import s_to_b, validate_fields
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult

"""AppFunction implementation"""
PACKAGE_NAME = "fn_github"
FN_NAME = "github_update_file"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'github_update_file'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: github_update_file
        Inputs:
            -   fn_inputs.github_owner
            -   fn_inputs.github_repo
            -   fn_inputs.github_file_path
            -   fn_inputs.github_file_contents
            -   fn_inputs.github_commit_message
            -   fn_inputs.github_committer
            -   fn_inputs.github_branch
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        gh = GitHubHelper(fn_inputs.github_owner, fn_inputs.github_repo, self.options)

        validate_fields([{"name": "base_url", "placeholder": "<https://base-url>"}],
            self.app_configs)

        validate_fields(["github_owner", "github_repo", "github_file_path",
                         "github_file_contents", "github_commit_message"], fn_inputs)

        committer = None
        if getattr(fn_inputs, 'github_committer', None):
            split_committer = fn_inputs.github_committer.split(':')
            committer = {
                "name": split_committer[0],
                "email": split_committer[1] if len(split_committer) > 1 else ""
            }

        results, err_msg = gh.update_file(fn_inputs.github_file_path,
                                          s_to_b(fn_inputs.github_file_contents),
                                          fn_inputs.github_commit_message,
                                          committer,
                                          branch=getattr(fn_inputs, 'github_branch', None))

        # clean up results so it can be returned
        if results and results.get('commit'):
            results['commit'] = results['commit'].sha

        if results and results.get('content'):
            results['content'] = results['content'].sha

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        yield FunctionResult(results, success=bool(results), reason=err_msg)
