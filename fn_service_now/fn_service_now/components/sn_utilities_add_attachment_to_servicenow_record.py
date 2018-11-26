# (c) Copyright IBM Corp. 2018. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_service_now.util.resilient_helper import ResilientHelper, ExternalTicketStatusDatatable
import json
import base64

def get_attachment(res_client, attachment_id, incident_id=None, task_id=None):
  """Function that gets incident/task attachment"""
  attachment = {"id": None, "name": None, "content_type": None, "contents": None}
  meta_data_uri, contents_uri = None, None

  if task_id:
    meta_data_uri = "/tasks/{0}/attachments/{1}".format(task_id, attachment_id)
    contents_uri = "/tasks/{0}/attachments/{1}/contents".format(task_id, attachment_id)
  elif incident_id:
    meta_data_uri = "/incidents/{0}/attachments/{1}".format(incident_id, attachment_id)
    contents_uri = "/incidents/{0}/attachments/{1}/contents".format(incident_id, attachment_id)
  else:
    raise FunctionError("task_id or incident_id must be specified with attachment")

  meta_data = res_client.get(meta_data_uri)

  attachment["content_type"] = meta_data["content_type"]
  attachment["id"] = attachment_id
  attachment["name"] = meta_data["name"]
  attachment["contents"] = base64.b64encode(res_client.get_content(contents_uri))

  return attachment

class FunctionPayload:
  """Class that contains the payload sent back to UI and available in the post-processing script"""
  def __init__(self, inputs):
    self.success = True
    self.inputs = {}
    self.res_id = None
    self.sn_ref_id = None
    self.attachment_name = None

    for input in inputs:
      self.inputs[input] = inputs[input]
  
  def asDict(self):
    """Return this class as a Dictionary"""
    return self.__dict__

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'sn_utilities_add_attachment_to_servicenow_record"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_service_now", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_service_now", {})

    @function("sn_utilities_add_attachment_to_servicenow_record")
    def _sn_utilities_add_attachment_to_servicenow_record_function(self, event, *args, **kwargs):
        """Function: A function that adds a Resilient Attachment to a ServiceNow Record."""
        try:
            # Instansiate helper (which gets appconfigs from file)
            res_helper = ResilientHelper(self.options)

            # Get the function inputs:
            inputs = {
              "sn_table_name": res_helper.get_function_input(kwargs, "sn_table_name"), # number (required)
              "attachment_id": res_helper.get_function_input(kwargs, "attachment_id"), # number (required)
              "incident_id": res_helper.get_function_input(kwargs, "incident_id"), # number (required)
              "task_id": res_helper.get_function_input(kwargs, "task_id", True) # number
            }

            # Create payload dict with inputs
            payload = FunctionPayload(inputs)

            yield StatusMessage("Function Inputs OK")

            # Instansiate new Resilient API object
            res_client = self.rest_client()
            
            # Get the attachment
            attachment = get_attachment(res_client, 
                                        payload.inputs["attachment_id"],
                                        payload.inputs["incident_id"],
                                        payload.inputs["task_id"])

            # Get the datatable
            datatable = ExternalTicketStatusDatatable(res_client, payload.inputs["incident_id"])

            # Generate res_id using incident and task id
            res_id = res_helper.generate_res_id(payload.inputs["incident_id"], payload.inputs["task_id"])

            # Get the sn_ref_id from the datatable
            sn_ref_id = datatable.get_sn_ref_id(res_id)

            if not sn_ref_id:
              payload.success = False
              raise FunctionError("This has not been created in ServiceNow yet. No sn_ref_id found in datatable.")

            else:
              # Generate the request_data
              request_data = {
                "sn_ref_id": sn_ref_id,
                "sn_table_name": payload.inputs["sn_table_name"],
                "type": "attachment",
                "attachment_base64": attachment["contents"],
                "attachment_name": attachment["name"],
                "attachment_content_type": attachment["content_type"]
              }
              
              yield StatusMessage("Add Attachment to ServiceNow")
            
              # Call POST and get response
              add_in_sn_response = res_helper.sn_POST("/add", data=json.dumps(request_data))
              payload.res_id = res_id
              payload.sn_ref_id = sn_ref_id
              payload.attachment_name = attachment["name"]

            results = payload.asDict()

            yield StatusMessage("Complete")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()