# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
import json
import time
from fn_service_now.util.resilient_helper import ResilientHelper, ExternalTicketStatusDatatable

class FunctionPayload:
  """Class that contains the payload sent back to UI and available in the post-processing script"""
  def __init__(self, inputs):
    self.success = True
    self.inputs = {}
    self.row_id = None
    self.res_id = None
    self.sn_ref_id = None
    self.sn_status = None
    self.sn_action = None
    self.sn_record_link = None

    for input in inputs:
      self.inputs[input] = inputs[input]
  
  def asDict(self):
    """Return this class as a Dictionary"""
    return self.__dict__

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'sn_utilities_create_in_servicenow"""

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

    @function("sn_utilities_create_in_servicenow")
    def _sn_utilities_create_in_servicenow_function(self, event, *args, **kwargs):
        """Function: A function that sends Task or Incident information to a custom endpoint in ServiceNow in order to create an associated ServiceNow record"""

        log = logging.getLogger(__name__)

        def generate_request_data(res_client, res_helper, incident_id, task_id=None, init_note=None, track_changes=None, extra_info=None):
          """Function that generates the data that is sent in the request to the /create endpoint in ServiceNow"""
          request_data = None

          datatable = ExternalTicketStatusDatatable(res_client, payload.inputs["incident_id"])
          datatable.get_data()
          sn_ref_ids = datatable.get_sn_ref_ids(payload.inputs["incident_id"], payload.inputs["task_id"])

          if(len(sn_ref_ids) > 0):
            raise ValueError("This item is already in the datatable")

          if task_id is not None:
            # Get the task
            task = res_helper.get_task(res_client, task_id, incident_id)
          
            # Add task to the request_data
            request_data = task.asDict()
          
          else:
            incident = res_helper.get_incident(res_client, incident_id)

            # Add incident to the request_data
            request_data = incident.asDict()

          # Add resilient_id and link to the request_data
          request_data["id"] = res_helper.generate_res_id(incident_id, task_id)
          request_data["link"] = res_helper.generate_res_link(incident_id, self.host, task_id)

          # If there is a sn_init_work_note, add to the task
          request_data["sn_init_work_note"] = init_note

          # Indicate whether changes to the related record in ServiceNow should be reflected in Resilient
          request_data["track_changes_in_resilient"] = track_changes

          # Extend request_data if there is data in 'sn_extend_request'
          if extra_info is not None and len(extra_info) > 0:
            temp_dict = {}
            for d in extra_info:
              key = d
              value = extra_info[d]
              temp_dict[key] = value
            request_data["extra_info"] = temp_dict
          else:
            request_data["extra_info"] = None
          
          return request_data

        try:
            # Instansiate helper (which gets appconfigs from file)
            res_helper = ResilientHelper(self.options)
            
            # Get the function inputs:
            inputs = {
              "incident_id": res_helper.get_function_input(kwargs, "incident_id"), # number (required)
              "task_id": res_helper.get_function_input(kwargs, "task_id", True), # number
              "sn_init_work_note": res_helper.get_function_input(kwargs, "sn_init_work_note", True), # text
              "sn_track_changes": res_helper.get_function_input(kwargs, "sn_track_changes", True), # boolean
              "sn_extend_request": res_helper.get_function_input(kwargs, "sn_extend_request", True) # text, JSON String
            }

            # Convert 'sn_extend_request' JSON string to Dictionary
            try:
              inputs["sn_extend_request"] = json.loads(inputs["sn_extend_request"])
            except Exception as e:
              print e
              raise ValueError("sn_extend_request JSON String is invalid")
            
            # Create payload dict with inputs
            payload = FunctionPayload(inputs)

            yield StatusMessage("Function Inputs OK")

            # Instansiate new Resilient API object
            res_client = self.rest_client()

            # Generate the request_data
            request_data = generate_request_data(res_client, res_helper,
                                                payload.inputs["incident_id"],
                                                payload.inputs["task_id"],
                                                payload.inputs["sn_init_work_note"],
                                                payload.inputs["sn_track_changes"],
                                                payload.inputs["sn_extend_request"])

            yield StatusMessage("Send Request to ServiceNow")
            # Call POST and get response
            create_in_sn_response = res_helper.POST("/create", data=json.dumps(request_data))

            if create_in_sn_response is not None:

              yield StatusMessage("Request Successful")

              # Set datatable name
              data_table_api_name = "sn_external_ticket_status"
              
              # Get current time (*1000 as API does not accept int)
              now = int(time.time()*1000)

              # Generate Link to ServiceNow record
              link = res_helper.SN_HOST + "/" + create_in_sn_response["sn_record_link"]

              # Generate cells for the datatable
              cells = {
                "cells" : {
                  "time": {"value": now},
                  "res_id": {"value": create_in_sn_response["res_id"]},
                  "sn_ref_id": {"value": create_in_sn_response["sn_ref_id"]},
                  "status": {"value": create_in_sn_response["sn_status"]},
                  "action": {"value": create_in_sn_response["sn_action"]},
                  "link": {"value": """<a href="{0}">Link</a>""".format(link)}
                }
              }

              # Add values to payload
              payload.res_id = create_in_sn_response["res_id"]
              payload.sn_ref_id = create_in_sn_response["sn_ref_id"]
              payload.sn_status = create_in_sn_response["sn_status"]
              payload.sn_action = create_in_sn_response["sn_action"]
              payload.sn_record_link = link

              # Generate uri to POST datatable row
              uri = "/incidents/{0}/table_data/{1}/row_data?handle_format=names".format(payload.inputs["incident_id"], data_table_api_name)

              try:

                yield StatusMessage("Adding row to " + data_table_api_name + " datatable")

                # POST row
                add_row_response = res_client.post(uri, cells)

                # Add row_id to payload
                payload.row_id = add_row_response["id"]
              except:
                payload.success = False
                raise ValueError("Failed to add row to datatable")

            else:
              payload.success = False

            results = payload.asDict()

            yield StatusMessage("Complete")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()