# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

from logging import getLogger
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_datatable_utils.util.helper import RESDatatable, validate_search_inputs
from resilient_lib import validate_fields

LOG = getLogger(__name__)

class FunctionPayload(object):
    """Class that contains the payload sent back to UI and available in the post-processing script"""
    def __init__(self, inputs):
        self.success = True
        self.inputs = inputs
        self.rows_ids = None

    def as_dict(self):
        """Return this class as a Dictionary"""
        return self.__dict__

class FunctionComponent(ResilientComponent):
    """Component that implements SOAR function 'dt_utils_delete_rows''"""

    def __init__(self, opts):
        """Constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_datatable_utils", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_datatable_utils", {})

    @function("dt_utils_delete_rows")
    def _dt_utils_delete_rows_function(self, event, *args, **kwargs):
        """Function: Function that deletes rows from a Data Table"""

        try:
            # Instansiate new SOAR API object
            res_client = self.rest_client()

            # Get the wf_instance_id of the workflow this Function was called in, if not found return a backup string
            wf_instance_id = event.message.get("workflow_instance", {}).get("workflow_instance_id", "no instance id found")
            yield StatusMessage("Starting 'dt_utils_delete_rows' that was running in workflow '{}'".format(wf_instance_id))

            validate_fields(["incident_id", "dt_utils_datatable_api_name"], kwargs)

            inputs = {
                "incident_id": kwargs.get("incident_id"),  # number (required)
                "dt_utils_datatable_api_name": kwargs.get("dt_utils_datatable_api_name"),  # text (required)
                "dt_utils_rows_ids": kwargs.get("dt_utils_rows_ids"),  # text (optional)
                "dt_utils_search_column": kwargs.get("dt_utils_search_column"),  # text (optional)
                "dt_utils_search_value": kwargs.get("dt_utils_search_value"), # text (optional)
                "dt_utils_delete_all_rows": bool(kwargs.get("dt_utils_delete_all_rows", False)), # bool (optional)
            }

            LOG.info("incident_id: {}".format(inputs["incident_id"]))
            LOG.info("dt_utils_datatable_api_name: {}".format(inputs["dt_utils_datatable_api_name"]))
            LOG.info("dt_utils_rows_ids: {}".format(inputs["dt_utils_rows_ids"]))
            LOG.info("dt_utils_search_column: {}".format(inputs["dt_utils_search_column"]))
            LOG.info(u"dt_utils_search_value: {}".format(inputs["dt_utils_search_value"]))
            LOG.info(u"dt_utils_delete_all_rows: {}".format(inputs["dt_utils_delete_all_rows"]))

            # Ensure correct search inputs are defined correctly
            valid_search_inputs = validate_search_inputs(rows_ids=inputs["dt_utils_rows_ids"],
                                                         search_column=inputs["dt_utils_search_column"],
                                                         search_value=inputs["dt_utils_search_value"],
                                                         search_criteria_required=False)

            if not valid_search_inputs["valid"]:
                raise ValueError(valid_search_inputs["msg"])

            # Create payload dict with inputs
            payload = FunctionPayload(inputs)

            # Instantiate a new RESDatatable
            datatable = RESDatatable(res_client, payload.inputs["incident_id"],
                                     payload.inputs["dt_utils_datatable_api_name"])

            # Get datatable row_id if function used on a datatable
            row_id = datatable.get_row_id_from_workflow(wf_instance_id)
            row_id and LOG.debug("Current row_id: %s", row_id)

            # Get the data table data
            datatable.get_data()

            deleted_rows = datatable.delete_rows(payload.inputs["dt_utils_rows_ids"],
                                                 payload.inputs["dt_utils_search_column"],
                                                 payload.inputs["dt_utils_search_value"],
                                                 payload.inputs["dt_utils_delete_all_rows"],
                                                 row_id,
                                                 wf_instance_id)

            payload.success = False
            if not deleted_rows:
                yield StatusMessage("No row(s) found.")

            elif "error" in deleted_rows:
                yield StatusMessage(u"Row(s) not deleted. Error: {}".format(deleted_rows.get("error")))
                raise FunctionError("Failed to delete a row.")

            else:
                yield StatusMessage("Row(s) {} in {} deleted.".format(deleted_rows, datatable.api_name))
                payload.rows_ids = deleted_rows
                payload.success = True

            results = payload.as_dict()

            LOG.info("Complete")
            yield StatusMessage("Finished 'dt_utils_delete_rows' that was running in workflow '{}'".format(wf_instance_id))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
