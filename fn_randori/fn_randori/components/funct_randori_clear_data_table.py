# -*- coding: utf-8 -*-

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields

PACKAGE_NAME = "fn_randori"
FN_NAME = "randori_clear_data_table"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'randori_clear_data_table'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Clear the specified Randori data table
        Inputs:
            -   fn_inputs.randori_data_table_name
            -   fn_inputs.incident_id
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        validate_fields(["incident_id", "randori_data_table_name"], fn_inputs)

        results = self.rest_client().delete("/incidents/{}/table_data/{}/row_data?handle_format=names".format(fn_inputs.incident_id, 
                                                                                                              fn_inputs.randori_data_table_name))

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        yield FunctionResult(results)

