# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_service_now.util.resilient_helper import ResilientHelper, ExternalTicketStatusDatatable
import time

class FunctionPayload:
  """Class that contains the payload sent back to UI and available in the post-processing script"""
  def __init__(self, inputs):
    self.success = True
    self.inputs = {}
    self.res_id = None
    self.row_id = None

    for input in inputs:
      self.inputs[input] = inputs[input]
  
  def asDict(self):
    """Return this class as a Dictionary"""
    return self.__dict__

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'sn_utilities_update_datatable"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_service_now", {})

        # Get host as needed to create link to incident/task
        self.host = opts.get("host")

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_service_now", {})

    @function("sn_utilities_update_datatable")
    def _sn_utilities_update_datatable_function(self, event, *args, **kwargs):
        """Function: Function that updates the ServiceNow Datatable when an Incident/Task is added/updated"""
        
        log = logging.getLogger(__name__)

        try:
            # Instansiate helper (which gets appconfigs from file)
            res_helper = ResilientHelper(self.options)
            
            # Get the function inputs:
            inputs = {
              "incident_id": res_helper.get_function_input(kwargs, "incident_id"), # number (required)
              "task_id": res_helper.get_function_input(kwargs, "task_id", True), # number (optional)
              "sn_resilient_status": res_helper.get_function_input(kwargs, "sn_resilient_status"), # text (required)
            }

            # Create payload dict with inputs
            payload = FunctionPayload(inputs)

            yield StatusMessage("Function Inputs OK")

            # Instansiate new Resilient API object
            res_client = self.rest_client()

            # Instansiate a reference to the ServiceNow Datatable
            res_datatable = ExternalTicketStatusDatatable(res_client, payload.inputs["incident_id"])

            # Get the datatable data and rows
            res_datatable.get_data()
            
            # Generate the res_id
            payload.res_id = res_helper.generate_res_id(payload.inputs["incident_id"], payload.inputs["task_id"])

            # Search for a row that contains the res_id
            row_found = res_datatable.get_row("res_id", payload.res_id)

            # Get current time (*1000 as API does not accept int)
            now = int(time.time()*1000)

            if row_found:
              yield StatusMessage("Row found. Updating Datatable")

              resilient_status = None

              # A=Active Incident, O=Open Task
              if payload.inputs["sn_resilient_status"] == "A" or payload.inputs["sn_resilient_status"] == "O":
                resilient_status = res_helper.convert_text_to_richtext("Active", "green")

              # C=Closed Incident/Task
              elif payload.inputs["sn_resilient_status"] == "C":
                resilient_status = res_helper.convert_text_to_richtext("Closed", "red")

              else:
                raise ValueError("{0} is not a handled status option".format(payload.inputs["sn_resilient_status"]))

              cells_to_update = {
                "time": now,
                "resilient_status": resilient_status
              }

              # Update the row
              update_row_response = res_datatable.update_row(row_found, cells_to_update)
              payload.row_id = update_row_response["id"]

            else:
              yield StatusMessage("No related ServiceNow record. Not changing Datatable state")
              payload.success = False

            results = payload.asDict()

            log.info("Complete")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()