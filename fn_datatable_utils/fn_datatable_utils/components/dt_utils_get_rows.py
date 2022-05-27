# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from fn_datatable_utils.util.helper import RESDatatable, PACKAGE_NAME, validate_search_inputs
from resilient_lib import validate_fields, ResultPayload

FN_NAME = "dt_utils_get_rows"

class FunctionComponent(AppFunctionComponent):
    """Component that implements SOAR function 'dt_utils_get_rows''"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)
        self.options = opts.get(PACKAGE_NAME, {})

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """Function: Function that returns rows found based on searching/sorting criteria.
            -   fn_inputs.incident_id
            -   fn_inputs.dt_utils_datatable_api_name
            -   fn_inputs.dt_utils_sort_by
            -   fn_inputs.dt_utils_sort_direction
            -   fn_inputs.dt_utils_max_rows
            -   fn_inputs.dt_utils_search_column
            -   fn_inputs.dt_utils_search_value"""

        try:
            # Instansiate new SOAR API object
            res_client = self.rest_client()

            yield self.status_message("Starting App Function: '{}'".format(FN_NAME))

            validate_fields(["incident_id", "dt_utils_datatable_api_name"], fn_inputs)

            dt_utils_datatable_api_name = fn_inputs.dt_utils_datatable_api_name  # text (required)
            incident_id = fn_inputs.incident_id  # number (required)
            dt_utils_sort_by = fn_inputs.dt_utils_sort_by if hasattr(fn_inputs, "dt_utils_sort_by") else None  # text (optional)
            dt_utils_sort_direction = fn_inputs.dt_utils_sort_direction if hasattr(fn_inputs, "dt_utils_sort_direction")["name"] else None  # select, values: "ASC", "DESC" (optional)
            dt_utils_max_rows = fn_inputs.dt_utils_max_rows if hasattr(fn_inputs, "dt_utils_max_rows") else None  # number (optional)
            dt_utils_search_column = fn_inputs.dt_utils_search_column if hasattr(fn_inputs, "dt_utils_search_column") else None  # text (optional)
            dt_utils_search_value = fn_inputs.dt_utils_search_value if hasattr(fn_inputs, "dt_utils_search_value") else None  # text (optional)

            self.LOG.info("incident_id: %s", incident_id)
            self.LOG.info("dt_utils_datatable_api_name: %s", dt_utils_datatable_api_name)
            self.LOG.info("dt_utils_sort_by: %s", dt_utils_sort_by)
            self.LOG.info("dt_utils_sort_direction: %s", dt_utils_sort_direction)
            self.LOG.info("dt_utils_max_rows: %s", dt_utils_max_rows)
            self.LOG.info("dt_utils_search_column: %s", dt_utils_search_column)
            self.LOG.info("dt_utils_search_value: %s", dt_utils_search_value)

            # Ensure correct search inputs are defined correctly
            valid_search_inputs = validate_search_inputs(sort_by=dt_utils_sort_by,
                                                         sort_direction=dt_utils_sort_direction,
                                                         search_column=dt_utils_search_column,
                                                         search_value=dt_utils_search_value,
                                                         search_criteria_required=False)

            if not valid_search_inputs["valid"]:
                raise ValueError(valid_search_inputs["msg"])

            # Create payload dict with inputs
            inputs_dict = fn_inputs._asdict()
            rp = ResultPayload(PACKAGE_NAME, **inputs_dict)

            # Instantiate a new RESDatatable
            datatable = RESDatatable(res_client, incident_id, dt_utils_datatable_api_name)

            # Get the data table data
            datatable.get_data()

            # Get rows
            rows = datatable.get_rows(dt_utils_max_rows,dt_utils_sort_by,
                                     dt_utils_sort_direction,
                                     dt_utils_search_column,dt_utils_search_value)

            # If no rows found, create a log and set success to False
            if not rows:
                yield self.status_message("No rows found")
                results = rp.done(False, None)
                results["reason"] = "No rows found"

            # Else, set rows in the payload
            else:
                yield self.status_message("{0} row/s found".format(len(rows)))
                results = rp.done(True, None)
                results["rows"] = rows

            yield self.status_message("Finished running App Function: '{}'".format(FN_NAME))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as err:
            yield FunctionResult({}, success=False, reason=str(err))
