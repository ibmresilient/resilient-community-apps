# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# pragma pylint: disable=unused-argument, line-too-long, wrong-import-order

"""AppFunction implementation"""
from fn_github.lib.client_helper import GitHubHelper
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields

PACKAGE_NAME = "fn_github"
FN_NAME = "github_list_directory"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'github_list_directory'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: List the files within a folder patch and optionally within a branch
        Inputs:
            -   fn_inputs.github_owner
            -   fn_inputs.github_repo
            -   fn_inputs.github_branch
            -   fn_inputs.github_file_path
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        validate_fields([{"name": "base_url", "placeholder": "<https://base-url>"}],
                        self.app_configs)

        validate_fields(["github_owner", "github_repo", "github_file_path"],
                         fn_inputs)

        gh = GitHubHelper(fn_inputs.github_owner, fn_inputs.github_repo, self.options)

        results, err_msg = gh.get_directory(fn_inputs.github_file_path,
                                            getattr(fn_inputs, 'github_branch', None))

        if results:
            new_results = {}
            for file, contents in results.items():
                new_dict = {}
                for item in ['git_url', 'html_url', 'path', 'size', 'encoding']:
                    new_dict[item] = getattr(contents, item, None)
                new_results[file] = new_dict

            results = new_results

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        yield FunctionResult(results if results else None,
                             success=bool(results),
                             reason=err_msg)
