# -*- coding: utf-8 -*-

"""AppFunction implementation"""
from fn_github.lib.client_helper import GitHubHelper
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import IntegrationError, validate_fields

PACKAGE_NAME = "fn_github"
FN_NAME = "github_create_release"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'github_create_release'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: create_release(tag_name, target_commitish=None, name=None, body=None, draft=False, prerelease=False)
        Inputs:
            -   fn_inputs.github_owner
            -   fn_inputs.github_repo
            -   fn_inputs.github_release_name
            -   fn_inputs.github_release_tag
            -   fn_inputs.github_release_description
            -   fn_inputs.github_prerelease
            -   fn_inputs.github_release_draft
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        validate_fields([{"name": "base_url", "placeholder": "<https://base-url>"}],
            self.app_configs)

        validate_fields(["github_owner", "github_repo", "github_release_name",
                         "github_release_tag"], fn_inputs)

        gh = GitHubHelper(self.app_configs._asdict())
        results, err_msg = gh.create_release(fn_inputs._asdict())

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        yield FunctionResult(results, success=bool(results), reason=err_msg)
