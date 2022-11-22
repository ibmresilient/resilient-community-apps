# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

"""AppFunction implementation"""

from resilient import SimpleHTTPException
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import (validate_fields, IntegrationError)
from fn_randori.lib.app_common import (PACKAGE_NAME)

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
        data_table_name = fn_inputs.randori_data_table_name
        case_id = fn_inputs.incident_id

        self.LOG.debug(f"Attempting to clear datatable '{data_table_name}' in case {case_id}")

        try:
            self.rest_client().delete(f"/incidents/{case_id}/table_data/{data_table_name}/row_data?handle_format=names")
            self.LOG.debug(f"Data in table {data_table_name} in incident {case_id} has been cleared")

            yield self.status_message(f"Successfully cleared {data_table_name} in case {case_id}")
        except SimpleHTTPException as err_msg:
            self.LOG.error(f"Failed to clear table: {data_table_name} error: {err_msg}")
            raise IntegrationError(f"Error while clearing table: {data_table_name}")

        yield FunctionResult({})


