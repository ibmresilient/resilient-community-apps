# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

from logging import getLogger
from json import loads
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_datatable_utils.util.helper import RESDatatable, PACKAGE_NAME
from resilient_lib import validate_fields, ResultPayload

LOG = getLogger(__name__)

class FunctionComponent(ResilientComponent):
    """Component that implements SOAR function 'dt_utils_update_row"""

    def __init__(self, opts):
        """Constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_datatable_utils", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_datatable_utils", {})

    @function("dt_utils_update_row")
    def _dt_utils_update_row_function(self, event, *args, **kwargs):
        """Function: Function that takes a JSON String of 'column name/cell value' pairs to update a Data Table row"""

        try:
            # Instansiate new SOAR API object
            res_client = self.rest_client()

            # Get the wf_instance_id of the workflow this Function was called in, if not found return a backup string
            wf_instance_id = event.message.get("workflow_instance", {}).get("workflow_instance_id", "no instance id found")
            yield StatusMessage("Starting 'dt_utils_update_row' that was running in workflow '{}'".format(wf_instance_id))

            validate_fields(["incident_id", "dt_utils_datatable_api_name", "dt_utils_row_id", "dt_utils_cells_to_update"], kwargs)

            incident_id = kwargs.get("incident_id"),  # number (required)
            dt_utils_datatable_api_name = kwargs.get("dt_utils_datatable_api_name"),  # text (required)
            dt_utils_row_id = kwargs.get("dt_utils_row_id"),  # number (required)
            dt_utils_cells_to_update = kwargs.get("dt_utils_cells_to_update")  # text (required)

            LOG.info("incident_id: %s", incident_id)
            LOG.info("dt_utils_datatable_api_name: %s", dt_utils_datatable_api_name)
            LOG.info("dt_utils_row_id: %s", dt_utils_row_id)
            LOG.info("dt_utils_cells_to_update: %s", dt_utils_cells_to_update)

            try:
                dt_utils_cells_to_update = loads(dt_utils_cells_to_update)
            except Exception:
                raise ValueError("Failed to parse JSON string: {}".format(dt_utils_cells_to_update))

            # Create payload dict with inputs
            rp = ResultPayload(PACKAGE_NAME, **kwargs)

            yield StatusMessage("Function Inputs OK")

            # Instantiate a new RESDatatable
            datatable = RESDatatable(res_client, incident_id, dt_utils_datatable_api_name)

            # Get the data table data
            datatable.get_data()

            # Use the current row_id if dt_utils_row_id = 0
            if not dt_utils_row_id or not int(dt_utils_row_id):
                row_id = datatable.get_row_id_from_workflow(wf_instance_id)
                if not row_id:
                    raise ValueError("Run the workflow from a datatable to get the current row_id.")

                LOG.info("Using current row_id: %s", row_id)
                dt_utils_row_id = row_id

            # Update the row
            updated_row = datatable.update_row(dt_utils_row_id, dt_utils_cells_to_update)

            if "error" in updated_row:
                yield StatusMessage("Row in {} NOT updated.".format(datatable.api_name))
                results = rp.done(False, None)
                raise ValueError(updated_row["error"])

            else:
                yield StatusMessage("Row {} in {} updated.".format(updated_row["id"], datatable.api_name))
                results = rp.done(True, None)
                results["row"] = updated_row

            LOG.info("Complete")
            yield StatusMessage("Finished 'dt_utils_update_row' that was running in workflow '{}'".format(wf_instance_id))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
