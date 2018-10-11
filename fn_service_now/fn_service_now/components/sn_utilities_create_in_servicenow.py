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
    self.sn_time_created = None

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
        
        # Convert unicode dict to str dict
        def _byteify(data):
          if isinstance(data, unicode):
            return data.encode("utf-8")
          
          if isinstance(data, dict):
            return { _byteify(key): _byteify(value) for key, value in data.items() }

        def generate_sn_request_data(res_client, res_helper, res_datatable, incident_id, sn_table_name, task_id=None, init_note=None, sn_optional_fields=None):
          """Function that generates the data that is sent in the request to the /create endpoint in ServiceNow"""
          request_data = None

          # Get the datatable data and rows
          res_datatable.get_data()
          sn_ref_ids = res_datatable.get_sn_ref_ids(payload.inputs["incident_id"], payload.inputs["task_id"])

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

          # Add sn_table_name, resilient_id, link and init_note to the request_data
          request_data["sn_table_name"] = sn_table_name
          request_data["id"] = res_helper.generate_res_id(incident_id, task_id)
          request_data["link"] = res_helper.generate_res_link(incident_id, self.host, task_id)
          request_data["sn_init_work_note"] = init_note

          # Extend request_data if there is data in 'sn_optional_fields'
          if sn_optional_fields is not None and len(sn_optional_fields) > 0:
            fields = []
            for field in sn_optional_fields:
              fields.append({"name": field, "value": sn_optional_fields[field]})
            request_data["sn_optional_fields"] = fields
          else:
            request_data["sn_optional_fields"] = None
          
          return request_data

        try:
            # Instansiate helper (which gets appconfigs from file)
            res_helper = ResilientHelper(self.options)
            
            # Get the function inputs:
            inputs = {
              "incident_id": res_helper.get_function_input(kwargs, "incident_id"), # number (required)
              "task_id": res_helper.get_function_input(kwargs, "task_id", True), # number
              "sn_table_name": res_helper.get_function_input(kwargs, "sn_table_name"), # text (required)
              "sn_init_work_note": res_helper.get_function_input(kwargs, "sn_init_work_note", True), # text
              "sn_optional_fields": res_helper.get_function_input(kwargs, "sn_optional_fields", True) # text, JSON String
            }

            # Convert 'sn_optional_fields' JSON string to Dictionary
            try:
              inputs["sn_optional_fields"] = json.loads(inputs["sn_optional_fields"], object_hook=_byteify)
            except Exception as e:
              print e
              raise ValueError("sn_optional_fields JSON String is invalid")
            
            # Create payload dict with inputs
            payload = FunctionPayload(inputs)

            yield StatusMessage("Function Inputs OK")

            # Instansiate new Resilient API object
            res_client = self.rest_client()
            
            # Instansiate a reference to the ServiceNow Datatable
            datatable = ExternalTicketStatusDatatable(res_client, payload.inputs["incident_id"])

            # Generate the request_data
            request_data = generate_sn_request_data(res_client, res_helper, datatable,
                                                payload.inputs["incident_id"],
                                                payload.inputs["sn_table_name"],
                                                payload.inputs["task_id"],
                                                payload.inputs["sn_init_work_note"],
                                                payload.inputs["sn_optional_fields"])

            yield StatusMessage("Creating a new record in ServiceNow")
            # Call POST and get response
            create_in_sn_response = res_helper.sn_POST("/create", data=json.dumps(request_data))

            if create_in_sn_response is not None:

              yield StatusMessage("Record Created")
              
              # Get current time (*1000 as API does not accept int)
              now = int(time.time()*1000)

              # Generate Link to ServiceNow record
              link = res_helper.SN_HOST + "/" + create_in_sn_response["sn_record_link"]

              # Add values to payload
              payload.res_id = create_in_sn_response["res_id"]
              payload.sn_ref_id = create_in_sn_response["sn_ref_id"]
              payload.sn_status = create_in_sn_response["sn_status"]
              payload.sn_action = create_in_sn_response["sn_action"]
              payload.sn_record_link = link
              payload.sn_time_created = now

              # Generate cells for the datatable
              cells = [
                ("time", payload.sn_time_created),
                ("res_id", payload.res_id),
                ("sn_ref_id", payload.sn_ref_id),
                ("status", payload.sn_status),
                ("action", payload.sn_action),
                ("link", """<a href="{0}">Link</a>""".format(link))
              ]

              try:
                # Add row to the datatable
                add_row_response = datatable.add_row(cells)
                payload.row_id = add_row_response["id"]

              except Exception as e:
                payload.success = False
                raise ValueError("Failed to add row to datatable {0}".format(e))

            else:
              payload.success = False

            results = payload.asDict()

            log.info("Complete")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()