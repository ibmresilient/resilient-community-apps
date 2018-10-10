# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import json
from bs4 import BeautifulSoup
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_service_now.util.resilient_helper import ResilientHelper, ExternalTicketStatusDatatable

class FunctionPayload:
  """Class that contains the payload sent back to UI and available in the post-processing script"""
  def __init__(self, inputs):
    self.success = True
    self.inputs = {}
    self.res_id = None
    self.sn_ref_id = None

    for input in inputs:
      self.inputs[input] = inputs[input]
  
  def asDict(self):
    """Return this class as a Dictionary"""
    return self.__dict__

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'sn_utilities_add_comment_to_servicenow_record"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_service_now", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_service_now", {})

    @function("sn_utilities_add_comment_to_servicenow_record")
    def _sn_utilities_add_comment_to_servicenow_record_function(self, event, *args, **kwargs):
        """Function: A function that adds a Resilient Note to a ServiceNow record as either a 'Work Note' or 'Additional Comment'"""

        log = logging.getLogger(__name__)

        try:
            # Instansiate helper (which gets appconfigs from file)
            res_helper = ResilientHelper(self.options)

           # Get the function inputs:
            inputs = {
              "sn_ref_id": res_helper.get_function_input(kwargs, "sn_ref_id", True), # text
              "task_id": res_helper.get_function_input(kwargs, "task_id", True), # number
              "note_id": res_helper.get_function_input(kwargs, "note_id"), # number (required)
              "incident_id": res_helper.get_function_input(kwargs, "incident_id"), # number (required)
              "sn_comment_text": res_helper.get_function_input(kwargs, "sn_comment_text"), # text (required)
              "sn_comment_type": res_helper.get_function_input(kwargs, "sn_comment_type")["name"] # select, text (required)
            }

            # Convert rich text comment to plain text
            soup = BeautifulSoup(inputs["sn_comment_text"], 'html.parser')
            soup = soup.get_text()
            inputs["sn_comment_text"] = soup.replace(u'\xa0', u' ')
            
            # Create payload dict with inputs
            payload = FunctionPayload(inputs)

            yield StatusMessage("Function Inputs OK")
            
            # Instansiate new Resilient API object
            res_client = self.rest_client()

            # Get the datatable and its data
            datatable = ExternalTicketStatusDatatable(res_client, payload.inputs["incident_id"])
            datatable.get_data()

            # Generate res_id using incident and task id
            res_id = res_helper.generate_res_id(payload.inputs["incident_id"], payload.inputs["task_id"])

            # Get sn_ref_id from input
            sn_ref_id = payload.inputs["sn_ref_id"]

            # If its None, check the datatable
            if sn_ref_id is None:

              yield StatusMessage("Searching Datatable for sn_ref_id")

              # Get all sn_ref_ids
              sn_ref_ids = datatable.get_sn_ref_ids(payload.inputs["incident_id"], payload.inputs["task_id"])

              # If task_id is defined, handle a Task Level Note
              if payload.inputs["task_id"] is not None:

                # Be sure only one relevant entry is in the datatable
                if(len(sn_ref_ids) == 1):
                  sn_ref_id = sn_ref_ids[0]

                # Else warn the user
                elif (len(sn_ref_ids) == 0):
                  payload.success = False
                  raise ValueError("This task has not been created in ServiceNow yet")

              # If an Incident Level Note and only one sn_ref_id, then use that id
              elif len(sn_ref_ids) == 1:
                sn_ref_id = sn_ref_ids[0]
              
              else:
                payload.success = False
                raise ValueError("This incident has not been created in ServiceNow yet")

            else:
              pass
              # Get id from activity field

            if sn_ref_id is not None:
              # Generate the request_data
              request_data = {
                "sn_ref_id": sn_ref_id,
                "type": "comment",
                "sn_comment_text": payload.inputs["sn_comment_text"],
                "sn_comment_type": payload.inputs["sn_comment_type"]
              }

              yield StatusMessage("Add Task Note to ServiceNow")
            
              # Call POST and get response
              add_in_sn_response = res_helper.sn_POST("/add", data=json.dumps(request_data))
              payload.res_id = res_id
              payload.sn_ref_id = sn_ref_id
          
            else:
              raise ValueError("No sn_ref_id defined")

            results = payload.asDict()

            yield StatusMessage("Complete")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()