# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
# # -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from fn_datatable_utils.util.helper import RESDatatable, PACKAGE_NAME
from resilient_lib import validate_fields

FN_NAME = "dt_utils_get_all_data_table_rows"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'dt_utils_get_all_data_table_rows'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)
        self.options = opts.get(PACKAGE_NAME, {})

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """Function: Return all of the rows from a data table in SOAR
            -   fn_inputs.incident_id
            -   fn_inputs.dt_utils_datatable_api_name"""

        # Instansiate new SOAR API object
        res_client = self.rest_client()

        yield self.status_message("Starting App Function: '{}'".format(FN_NAME))

        validate_fields(['incident_id', 'dt_utils_datatable_api_name'], fn_inputs)

        incident_id = fn_inputs.incident_id  # text (required)
        dt_api_name = fn_inputs.dt_utils_datatable_api_name # text (required)

        self.LOG.info("incident_id: %s", incident_id)
        self.LOG.info("dt_utils_datatable_api_name: %s", dt_api_name)

        # Instantiate a new RESDatatable
        datatable = RESDatatable(res_client, incident_id, dt_api_name)

        # Get the data table data
        datatable.get_data()

        rows = datatable.get_rows()

        # If no rows found, create a log
        if not rows:
            yield self.status_message("No rows found")

        # Else, set rows in the payload
        else:
            yield self.status_message("{} row/s found".format(len(rows)))

        yield self.status_message("Finished running App Function: '{}'".format(FN_NAME))

        yield FunctionResult({"rows": rows})
