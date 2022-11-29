# -*- coding: utf-8 -*-

"""AppFunction implementation"""

import base64
from fn_playbook_utils.lib.common import export_playbook
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import IntegrationError, validate_fields, b_to_s, s_to_b

PACKAGE_NAME = "fn_playbook_utils"
FN_NAME = "pb_export_playbook"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'pb_export_playbook'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: None
        Inputs:
            -   fn_inputs.pbm_id
            -   fn_inputs.pbm_name
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        if not (getattr(fn_inputs, 'pbm_id', None) or getattr(fn_inputs, 'pbm_name', None)):
            ValueError("Specify either playbook ID or Name")

        status, results = export_playbook(self.rest_client(),
                                          getattr(fn_inputs, 'pbm_id', None), 
                                          getattr(fn_inputs, 'pbm_name', None))

        if status:
            results = b_to_s(base64.b64encode(s_to_b(results)))

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        yield FunctionResult(results if results else {},
                             success=status,
                             reason=results if not status else None)
