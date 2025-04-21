# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# Generated with resilient-sdk v51.0.1.0.695

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import (validate_fields)
from fn_axonius.lib.axonius_client import (AxoniusClient)

PACKAGE_NAME = "fn_axonius"
FN_NAME = "axonius_run_enforcement_set"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'axonius_run_enforcement_set'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Run the Axonius enforcement set given an enforcement set name.
        Inputs:
            -   fn_inputs.axonius_enforcement_set_name
        """
        validate_fields(["axonius_enforcement_set_name"], fn_inputs)

        axonius_client = AxoniusClient(self.rc, PACKAGE_NAME, self.options)

        results, error_msg = axonius_client.get_enforcement_by_name(enforcement_name=fn_inputs.axonius_enforcement_set_name,
                                                                    limit=1)

        results_run = {}
        error_msg_run = ""
        if results and not error_msg:
            enforcements = results.get("enforcements", None)
            if not enforcements:
                error_msg_run = "{0}No Enforcement Set found with name: {1}<br>".format(error_msg_run, 
                                                                                      fn_inputs.axonius_enforcement_set_name)
            else:
                for enforcement in enforcements:
                    results_run, error_msg_run = axonius_client.run_enforcement(id=enforcement.get("uuid"))

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        yield FunctionResult(results_run, 
                             success=False if error_msg or error_msg_run else True, 
                             reason=error_msg_run if error_msg_run else error_msg)
