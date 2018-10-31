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
    self.action = None #'add'/'update'/None
    self.res_id = None
    self.res_link = None
    self.sn_link = None
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
              "task_id": res_helper.get_function_input(kwargs, "task_id", True), # number
              "sn_ref_id": res_helper.get_function_input(kwargs, "sn_ref_id"), # text (required)
              "incident_status": res_helper.get_function_input(kwargs, "incident_status"), # text (required)
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
            
            # Search for a row that contains the same sn_ref_id
            row_found = res_datatable.get_row("sn_ref_id", payload.inputs["sn_ref_id"])

            # Get current time (*1000 as API does not accept int)
            now = int(time.time()*1000)

            if row_found:
              yield StatusMessage("Row found. Updating Datatable")

              cells_to_update = {
                "time": now,
                "status": res_helper.get_status_rich_text(payload.inputs["incident_status"]),
                "action": "Status Updated"
              }

              # Update the row
              update_row_response = res_datatable.update_row(row_found, cells_to_update)
              payload.row_id = update_row_response["id"]
            
            else:
              yield StatusMessage("No row found. Add row to Datatable")

              # Generate the res_id
              payload.res_id = res_helper.generate_res_id(payload.inputs["incident_id"], payload.inputs["task_id"])

              # Generate the res_link and sn_link
              payload.res_link = res_helper.generate_res_link(payload.inputs["incident_id"], self.host, payload.inputs["task_id"])
              payload.sn_link = res_helper.generate_sn_link("number={0}".format(payload.inputs["sn_ref_id"]))

              # Specify the action
              payload.action = "Task Created" if payload.inputs["task_id"] else "Incident Created"

              # Add the row
              add_row_response = res_datatable.add_row(
                  now,
                  payload.res_id,
                  payload.inputs["sn_ref_id"],
                  res_helper.get_status_rich_text(payload.inputs["incident_status"]),
                  payload.action,
                  """<a href="{0}">RES</a> <a href="{1}">SN</a>""".format(payload.res_link, payload.sn_link)
              )
              payload.row_id = add_row_response["id"]

            results = payload.asDict()

            log.info("Complete")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()