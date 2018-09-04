# (c) Copyright IBM Corp. 2018. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import json
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_service_now.util.resilient_helper import ResilientHelper

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'sn_utilities_send_to_servicenow"""

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

    @function("sn_utilities_send_to_servicenow")
    def _sn_utilities_send_to_servicenow_function(self, event, *args, **kwargs):
        """Function: A function that has the ability to send an Incident, Task, Attachment, Note or Artifact to ServiceNow"""

        log = logging.getLogger(__name__)

        try:
            # Instansiate helper (which gets appconfigs from file)
            res_helper = ResilientHelper(self.options)

            # Get the function inputs:
            inputs = {
              "incident_id": res_helper.get_function_input(kwargs, "incident_id"), # number (required)
              "task_id": res_helper.get_function_input(kwargs, "task_id", True), # number
              "attachment_id": res_helper.get_function_input(kwargs, "attachment_id", True), # number
              "note_id": res_helper.get_function_input(kwargs, "note_id", True), # number
              "artifact_id": res_helper.get_function_input(kwargs, "artifact_id", True), # number
              "sn_ref_id": res_helper.get_function_input(kwargs, "sn_ref_id", True), # text
              "sn_comment_type": res_helper.get_function_input(kwargs, "sn_comment_type", True), # text
              "sn_optional_fields": res_helper.get_function_input(kwargs, "sn_optional_fields", True), # text [csv]
              "sn_init_work_note": res_helper.get_function_input(kwargs, "sn_init_work_note", True), # text
              "sn_track_changes": res_helper.get_function_input(kwargs, "sn_track_changes", True) # boolean
            }
            yield StatusMessage("Function Inputs OK")

            # Create function_payload dict with inputs
            function_payload = res_helper.FunctionPayload(inputs)

            # Convert sn_optional_fields in CSV to Python list
            if function_payload.inputs["sn_optional_fields"] is not None:
              function_payload.inputs["sn_optional_fields"] = res_helper.csv_to_list(function_payload.inputs["sn_optional_fields"])

            # Instansiate new Resilient API object
            res_client = self.rest_client()

            # If its a Task
            if function_payload.inputs["task_id"] is not None:
              
              if function_payload.inputs["attachment_id"] is not None:
                # TODO: If its a Task attachment
                pass
              
              elif function_payload.inputs["note_id"] is not None:
                # TODO: If its a Task note
                pass

              else:
                # Get the task
                task = res_helper.get_task(res_client, function_payload.inputs["task_id"], 
                function_payload.inputs["incident_id"], function_payload.inputs["sn_optional_fields"])
                
                # If there is a sn_init_work_note, add to the task
                if(function_payload.inputs["sn_init_work_note"]):
                  task.add_work_note(function_payload.inputs["sn_init_work_note"])

                # Add task to the request_data
                request_data = task.asDict()
                
                # Add resilient_id and link to this task to the request_data
                request_data["id"] = res_helper.generate_res_id(function_payload.inputs["incident_id"], function_payload.inputs["task_id"])
                request_data["link"] = res_helper.generate_res_link(function_payload.inputs["incident_id"], self.host, function_payload.inputs["task_id"])

                # Call POST and get response
                response = res_helper.POST("/create", data=json.dumps(request_data))

                if response is not None:
                  print response["sn_sys_id"], response["sn_id"]
                else:
                  function_payload.success = False

            # Else it must be an incident
            else:
              
              if function_payload.inputs["artifact_id"] is not None:
                # TODO: If its an incident artifact
                pass

              elif function_payload.inputs["attachment_id"] is not None:
                # TODO: If its an incident attachment
                pass
              
              elif function_payload.inputs["note_id"] is not None:
                # TODO: If its an incident note
                pass
              
              else:
                # Get the incident
                incident = res_helper.get_incident(res_client, function_payload.inputs["incident_id"])
                
                # If there is a sn_init_work_note, add to the incident
                if(function_payload.inputs["sn_init_work_note"]):
                  incident.add_work_note(function_payload.inputs["sn_init_work_note"])

                # Add incident to the request_data
                request_data = incident.asDict()
                
                # Add resilient_id and link to this incident to the request_data
                request_data["id"] = res_helper.generate_res_id(function_payload.inputs["incident_id"])
                request_data["link"] = res_helper.generate_res_link(function_payload.inputs["incident_id"], self.host)

                # Call POST and get response
                response = res_helper.POST("/create", data=json.dumps(request_data))

                if response is not None:
                  print response["sn_sys_id"], response["sn_id"]
                else:
                  function_payload.success = False

            results = function_payload.asDict()

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()