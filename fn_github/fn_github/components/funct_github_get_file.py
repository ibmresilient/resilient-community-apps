# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# pragma pylint: disable=unused-argument, line-too-long, wrong-import-order

import base64
from fn_github.lib.client_helper import GitHubHelper
from resilient_lib import b_to_s
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields

"""AppFunction implementation"""

PACKAGE_NAME = "fn_github"
FN_NAME = "github_get_file"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'github_get_file'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: github_get_file
        Inputs:
            -   fn_inputs.github_owner
            -   fn_inputs.github_repo
            -   fn_inputs.github_ref
            -   fn_inputs.github_file_path
            -   fn_inputs.github_return_base64
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        validate_fields([{"name": "base_url", "placeholder": "<https://base-url>"}],
            self.app_configs)

        validate_fields(["github_owner", "github_repo", "github_file_path"], fn_inputs)

        gh = GitHubHelper(self.app_configs._asdict())

        results, err_msg = gh.get_file_contents(fn_inputs.github_owner,
                                                fn_inputs.github_repo,
                                                fn_inputs.github_file_path,
                                                getattr(fn_inputs, 'github_ref', None)
                                               )

        if results and not getattr(fn_inputs, 'github_return_base64', True):
            try:
                results = b_to_s(base64.b64decode(results))
            except:
                pass # pass results asis

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        yield FunctionResult({"contents": results}, success=bool(results), reason=err_msg)
