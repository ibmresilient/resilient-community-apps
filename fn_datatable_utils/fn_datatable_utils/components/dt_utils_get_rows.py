# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

from logging import getLogger
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_datatable_utils.util.helper import validate_search_inputs, RESDatatable, PACKAGE_NAME
from resilient_lib import validate_fields, ResultPayload

LOG = getLogger(__name__)

class FunctionComponent(ResilientComponent):
    """Component that implements SOAR function 'dt_utils_get_rows''"""

    def __init__(self, opts):
        """Constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_datatable_utils", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_datatable_utils", {})

    @function("dt_utils_get_rows")
    def _dt_utils_get_rows_function(self, event, *args, **kwargs):
        """Function: Function that returns rows found based on searching/sorting criteria."""

        try:
            # Instansiate new SOAR API object
            res_client = self.rest_client()

            # Get the wf_instance_id of the workflow this Function was called in, if not found return a backup string
            wf_instance_id = event.message.get("workflow_instance", {}).get("workflow_instance_id", "no instance id found")
            yield StatusMessage("Starting 'dt_utils_get_rows' that was running in workflow '{}'".format(wf_instance_id))

            validate_fields(["incident_id", "dt_utils_datatable_api_name"], kwargs)

            incident_id = kwargs.get("incident_id"),  # number (required)
            dt_utils_datatable_api_name = kwargs.get("dt_utils_datatable_api_name"),  # text (required)
            dt_utils_sort_by = kwargs.get("dt_utils_sort_by"),  # text (optional)
            dt_utils_sort_direction = kwargs.get("dt_utils_sort_direction")["name"],  # select, values: "ASC", "DESC" (optional)
            dt_utils_max_rows = kwargs.get("dt_utils_max_rows"),  # number (optional)
            dt_utils_search_column = kwargs.get("dt_utils_search_column"),  # text (optional)
            dt_utils_search_value = kwargs.get("dt_utils_search_value"),  # text (optional)

            LOG.info("incident_id: %s", incident_id)
            LOG.info("dt_utils_datatable_api_name: %s", dt_utils_datatable_api_name)
            LOG.info("dt_utils_sort_by: %s", dt_utils_sort_by)
            LOG.info("dt_utils_sort_direction: %s", dt_utils_sort_direction)
            LOG.info("dt_utils_max_rows: %s", dt_utils_max_rows)
            LOG.info("dt_utils_search_column: %s", dt_utils_search_column)
            LOG.info("dt_utils_search_value: %s", dt_utils_search_value)

            # Ensure correct search inputs are defined correctly
            valid_search_inputs = validate_search_inputs(sort_by=dt_utils_sort_by,
                                                         sort_direction=dt_utils_sort_direction,
                                                         search_column=dt_utils_search_column,
                                                         search_value=dt_utils_search_value,
                                                         search_criteria_required=False)

            if not valid_search_inputs["valid"]:
                raise ValueError(valid_search_inputs["msg"])

            # Create payload dict with inputs
            rp = ResultPayload(PACKAGE_NAME, **kwargs)

            # Instantiate a new RESDatatable
            datatable = RESDatatable(res_client,incident_id,dt_utils_datatable_api_name)

            # Get the data table data
            datatable.get_data()

            # Get rows
            rows = datatable.get_rows(dt_utils_max_rows,dt_utils_sort_by,
                                     dt_utils_sort_direction,
                                     dt_utils_search_column,dt_utils_search_value)

            # If no rows found, create a log and set success to False
            if not rows:
                yield StatusMessage("No rows found")
                results = rp.done(False, None)

            # Else, set rows in the payload
            else:
                yield StatusMessage("{0} row/s found".format(len(rows)))
                results = rp.done(True, None)
                results["rows"] = rows

            LOG.info("Complete")
            yield StatusMessage("Finished 'dt_utils_get_rows' that was running in workflow '{}'".format(wf_instance_id))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
