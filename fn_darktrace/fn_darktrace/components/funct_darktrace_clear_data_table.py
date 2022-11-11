# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

"""AppFunction implementation"""

from fn_darktrace.lib.app_common import PACKAGE_NAME
from resilient import SimpleHTTPException
from resilient_circuits import (AppFunctionComponent, FunctionResult,
                                app_function)
from resilient_lib import IntegrationError, validate_fields

FN_NAME = "darktrace_clear_data_table"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'darktrace_clear_data_table'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Clear a given data table so it can be updated
        Inputs:
            -   fn_inputs.darktrace_data_table_name
            -   fn_inputs.darktrace_soar_case_id
        """

        validate_fields(["darktrace_soar_case_id", "darktrace_data_table_name"], fn_inputs)

        # case ID and DT name are required to clear the datatable
        case_id = fn_inputs.darktrace_soar_case_id
        data_table_name = fn_inputs.darktrace_data_table_name

        self.LOG.debug(f"Attempting to clear datatable '{data_table_name}' in case {case_id}")

        try:
            self.rest_client().delete(f"/incidents/{case_id}/table_data/{data_table_name}/row_data?handle_format=names")
            self.LOG.debug(f"Data in table {data_table_name} in incident {case_id} has been cleared")

            yield self.status_message(f"Successfully cleared {data_table_name} in case {case_id}")
        except SimpleHTTPException as err_msg:
            self.LOG.error(f"Failed to clear table: {data_table_name} error: {err_msg}")
            raise IntegrationError(f"Error while clearing table: {data_table_name}")

        yield FunctionResult({})
