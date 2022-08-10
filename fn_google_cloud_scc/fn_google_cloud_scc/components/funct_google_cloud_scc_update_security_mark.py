# -*- coding: utf-8 -*-

"""AppFunction implementation"""

from fn_google_cloud_scc.lib.scc_common import PACKAGE_NAME, GoogleSCCCommon
from resilient_circuits import (AppFunctionComponent, FunctionResult,
                                app_function)
from resilient_lib import validate_fields

FN_NAME = "google_cloud_scc_update_security_mark"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'google_cloud_scc_update_security_mark'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Update/add a security mark of/to a given SCC finding.
        Inputs:
            -   fn_inputs.google_scc_finding_name
            -   fn_inputs.google_scc_update_value
            -   fn_inputs.google_scc_update_key
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        self.app_common = GoogleSCCCommon(self.options)

        validate_fields(["google_scc_finding_name", "google_scc_update_key"], fn_inputs)
        finding_name = fn_inputs.google_scc_finding_name
        update_key = fn_inputs.google_scc_update_key
        update_value = getattr(fn_inputs, "google_scc_update_value", None) # this allows for deletion

        # make the call to update the marks
        updated_marks, _ = self.app_common.update_security_mark(finding_name, update_key, update_value)

        results = {
            "updated_key": update_key,
            "updated_value": update_value,
            "updated_marks": updated_marks
        }

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        yield FunctionResult(results)
