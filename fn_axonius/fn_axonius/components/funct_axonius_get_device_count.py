# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# Generated with resilient-sdk v51.0.1.0.695

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import (IntegrationError)
from fn_axonius.lib.axonius_client import (AxoniusClient)
from fn_axonius.lib.configure_tab import (init_axonius_tab)

PACKAGE_NAME = "fn_axonius"
FN_NAME = "axonius_get_device_count"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'axonius_get_device_count'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)
        init_axonius_tab()

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Get the number of devices that match the Axonius query.
        Inputs:
            -   fn_inputs.axonius_saved_query_name
            -   fn_inputs.axonius_query_string
        """
        if not fn_inputs.axonius_query_string and not fn_inputs.axonius_saved_query_name:
            raise IntegrationError("Get Device Count requires a query string OR an saved query name as a parameter.")

        axonius_client = AxoniusClient(self.rc, PACKAGE_NAME, self.options)

        results, error_msg = axonius_client.get_device_count(query=fn_inputs.axonius_query_string,
                                                             saved_query_name=fn_inputs.axonius_saved_query_name)
        
        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        yield FunctionResult(results, success=False if error_msg else True, reason=error_msg)
