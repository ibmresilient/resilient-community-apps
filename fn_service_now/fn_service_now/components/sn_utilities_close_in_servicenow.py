# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_service_now.util.resilient_helper import ResilientHelper, ExternalTicketStatusDatatable
import json
import time

class FunctionPayload:
  """Class that contains the payload sent back to UI and available in the post-processing script"""
  def __init__(self, inputs):
    self.success = True
    self.inputs = {}

    for input in inputs:
      self.inputs[input] = inputs[input]
  
  def asDict(self):
    """Return this class as a Dictionary"""
    return self.__dict__
  
class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'sn_utilities_close_in_servicenow"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_service_now", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_service_now", {})

    @function("sn_utilities_close_in_servicenow")
    def _sn_utilities_close_in_servicenow_function(self, event, *args, **kwargs):
        """Function: A Function that closes a record in ServiceNow while also supplying the reason for resolving"""

        log = logging.getLogger(__name__)

        try:

            # Instansiate helper (which gets appconfigs from file)
            res_helper = ResilientHelper(self.options)
            
            # Get the function inputs:
            inputs = {
              "incident_id": res_helper.get_function_input(kwargs, "incident_id"), # number (required)
              "task_id": res_helper.get_function_input(kwargs, "task_id", True), # number (optional)
              "sn_ref_id": res_helper.get_function_input(kwargs, "sn_ref_id", True), # text (optional)
              "sn_table_name": res_helper.get_function_input(kwargs, "sn_table_name"), # text (required)
              "sn_record_state": res_helper.get_function_input(kwargs, "sn_record_state"), # number (required)
              "sn_close_notes": res_helper.get_function_input(kwargs, "sn_close_notes", True), # text (optional)
              "sn_close_code": res_helper.get_function_input(kwargs, "sn_close_code", True), # text (required)
            }

            # Create payload dict with inputs
            payload = FunctionPayload(inputs)

            yield StatusMessage("Function Inputs OK")

            # Instansiate new Resilient API object
            res_client = self.rest_client()

            # Get the datatable and its data
            datatable = ExternalTicketStatusDatatable(res_client, payload.inputs["incident_id"])
            datatable.get_data()

            # Get sn_ref_id from input
            sn_ref_id = payload.inputs["sn_ref_id"]

            # If its None, check the datatable
            if sn_ref_id is None:

              yield StatusMessage("Searching Datatable for sn_ref_id")

              # Get all sn_ref_ids
              sn_ref_ids = datatable.get_sn_ref_ids(payload.inputs["incident_id"], payload.inputs["task_id"])

              # If task_id is defined, handle closing Task in ServiceNow
              if payload.inputs["task_id"] is not None:

                # Be sure only one relevant entry is in the datatable
                if(len(sn_ref_ids) == 1):
                  sn_ref_id = sn_ref_ids[0]

                # Else warn the user
                elif (len(sn_ref_ids) == 0):
                  payload.success = False
                  raise ValueError("This task has not been created in ServiceNow yet")

              # If an Incident and only one sn_ref_id, then use that id
              elif len(sn_ref_ids) == 1:
                sn_ref_id = sn_ref_ids[0]
              
              else:
                payload.success = False
                raise ValueError("This incident has not been created in ServiceNow yet")

            if sn_ref_id is not None:
              # Generate the request_data
              request_data = {
                "sn_ref_id": sn_ref_id,
                "sn_table_name": payload.inputs["sn_table_name"],
                "sn_close_code": payload.inputs["sn_close_code"],
                "sn_close_notes": payload.inputs["sn_close_notes"],
                "sn_record_state": payload.inputs["sn_record_state"]
              }

              try:
                yield StatusMessage("Closing in ServiceNow {0}".format(sn_ref_id))
                close_in_sn_response = res_helper.sn_POST("/close_record", data=json.dumps(request_data))
                payload.sn_ref_id = sn_ref_id
              
              except Exception as err:
                payload.success = False
                raise ValueError("Failed to close in ServiceNow: {0}".format(err))
              
              try:
                yield StatusMessage("Updating ServiceNow Status to {0}".format(close_in_sn_response["sn_state"]))

                row_id_to_update = datatable.get_row("sn_ref_id", sn_ref_id)

                cells_to_update = {
                  "time": int(time.time()*1000),
                  "servicenow_status": res_helper.convert_text_to_richtext(close_in_sn_response["sn_state"], "red")
                  }
                
                # Update the row
                datatable.update_row(row_id_to_update, cells_to_update)
              
              except Exception as err:
                payload.success = False
                raise ValueError("Failed to update ServiceNow Status in Datatable: {0}".format(err))

            else:
              raise ValueError("No sn_ref_id defined")

            results = payload.asDict()

            log.info("Complete")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()