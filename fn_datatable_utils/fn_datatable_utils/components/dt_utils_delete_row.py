# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# # -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

from logging import getLogger
from resilient_lib import validate_fields
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_datatable_utils.util.helper import RESDatatable

LOG = getLogger(__name__)

class FunctionPayload(object):
    """Class that contains the payload sent back to UI and available in the post-processing script"""
    def __init__(self, inputs):
        self.success = True
        self.inputs = inputs
        self.row = None

    def as_dict(self):
        """Return this class as a Dictionary"""
        return self.__dict__

class FunctionComponent(ResilientComponent):
    """Component that implements SOAR function 'dt_utils_delete_row"""

    def __init__(self, opts):
        """Constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_datatable_utils", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_datatable_utils", {})

    @function("dt_utils_delete_row")
    def _dt_utils_delete_row_function(self, event, *args, **kwargs):
        """Function: Function that deletes a row from a Data Table given the row's ID"""

        try:
            # Instansiate new SOAR API object
            res_client = self.rest_client()
            workflow_instance_id = event.message.get('workflow_instance', {}).get('workflow_instance_id')

            validate_fields(["dt_utils_datatable_api_name", "incident_id"], kwargs)

            dt_utils_row_id = kwargs.get("dt_utils_row_id") # number (optional)
            dt_utils_datatable_api_name = kwargs.get("dt_utils_datatable_api_name") # text (required)

            inputs = {
                "incident_id": kwargs.get("incident_id"), # number (required)
                "dt_utils_datatable_api_name": dt_utils_datatable_api_name,
                "dt_utils_row_id": dt_utils_row_id
            }
            LOG.debug(inputs)

            # Create payload dict with inputs
            payload = FunctionPayload(inputs)

            yield StatusMessage("Function Inputs OK")

            # Instantiate a new RESDatatable
            datatable = RESDatatable(res_client, payload.inputs["incident_id"], dt_utils_datatable_api_name)

            # Get datatable row_id if function used on a datatable
            row_id = datatable.get_row_id_from_workflow(workflow_instance_id)
            row_id and LOG.debug("Current row_id: %s", row_id)

            # If dt_utils_row_id == 0, use row_id
            if not dt_utils_row_id or not int(dt_utils_row_id):
                if not row_id:
                    raise ValueError("Run the workflow from a datatable to get the current row_id.")

                LOG.info("Using current row_id: %s", row_id)
                dt_utils_row_id = row_id

            if row_id == int(dt_utils_row_id):
                yield StatusMessage("Queuing row {0} for delete".format(dt_utils_row_id))
                deleted_row = datatable.queue_delete(workflow_instance_id, dt_utils_row_id)
            else:
                deleted_row = datatable.delete_row(dt_utils_row_id)

            if "error" in deleted_row:
                yield StatusMessage(u"Row {0} in {1} not deleted.".format(dt_utils_row_id, dt_utils_datatable_api_name))
                payload.success = False
                raise ValueError(deleted_row["error"])

            yield StatusMessage("Row {0} in {1} deleted.".format(dt_utils_row_id, dt_utils_datatable_api_name))
            payload.row = deleted_row
            payload.success = True

            results = payload.as_dict()

            LOG.info("Complete")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
