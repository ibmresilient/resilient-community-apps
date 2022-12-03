# -*- coding: utf-8 -*-

"""AppFunction implementation"""

from fn_github.lib.client_helper import GitHubHelper
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import IntegrationError, validate_fields

PACKAGE_NAME = "fn_github"
FN_NAME = "github_delete_file"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'github_delete_file'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Delete a GitHub from a specific branch
        Inputs:
            -   fn_inputs.github_committer
            -   fn_inputs.github_owner
            -   fn_inputs.github_branch
            -   fn_inputs.github_repo
            -   fn_inputs.github_file_path
            -   fn_inputs.github_commit_message
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        gh = GitHubHelper(self.app_configs._asdict())

        validate_fields([{"name": "base_url", "placeholder": "<https://base-url>"}],
            self.app_configs)

        validate_fields(["github_owner", "github_repo", "github_file_path", 
                         "github_commit_message", "github_branch"], fn_inputs)

        committer = None
        if getattr(fn_inputs, 'github_committer', None):
            split_committer = fn_inputs.github_committer.split(':')
            committer = {
                "name": split_committer[0],
                "email": split_committer[1] if len(split_committer) > 1 else ""
            }

        results, err_msg = gh.delete_file(fn_inputs.github_owner,
                                          fn_inputs.github_repo,
                                          fn_inputs.github_file_path,
                                          fn_inputs.github_commit_message,
                                          committer,
                                          branch=fn_inputs.github_branch
                                        )

        # clean up results so it can be returned
        if results and results.get('commit'):
            results['commit'] = results['commit'].sha

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        yield FunctionResult(results, success=bool(results), reason=err_msg)
