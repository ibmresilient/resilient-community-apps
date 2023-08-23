# -*- coding: utf-8 -*-
#(c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
#pragma pylint: disable=unused-argument, line-too-long

"""AppFunction implementation"""
import base64
from fn_playbook_utils.lib.common import import_playbook
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields

PACKAGE_NAME = "fn_playbook_utils"
FN_NAME = "pb_import_playbook"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'pb_import_playbook'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Import a playbook
        Inputs:
            -   fn_inputs.pbm_body
            -   fn_inputs.pbm_base64_content
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        validate_fields(["pbm_body"], fn_inputs)

        content = fn_inputs.pbm_body
        if getattr(fn_inputs, "pbm_base64_content", False):
            content = base64.b64decode(content)

        results = import_playbook(self.rest_client(), content)

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        yield FunctionResult(results)
