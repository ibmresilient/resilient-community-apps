# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_service_now.util.helper import ServiceNowHelper
import json

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'sn_create_incident"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_service_now", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_service_now", {})

    @function("sn_create_incident")
    def _sn_create_incident_function(self, event, *args, **kwargs):
        """Function: A function that creates a new Incident on your connected ServiceNow Platform"""

        log = logging.getLogger(__name__)

        try:
          # Instansiate helper (which gets appconfigs from file)
          helper = ServiceNowHelper(self.options)
          yield StatusMessage("Appconfig Settings OK")

          # Get function inputs
          input_incident_id = helper.get_function_input(kwargs, "incident_id") # number (required) 
          yield StatusMessage("Function Inputs OK")

          # Instansiate new Resilient API object
          res_client = self.rest_client()

          res_incident = helper.get_res_incident(res_client, input_incident_id, want_attachments=True)
          
          res_incident_tasks = helper.get_res_incident_tasks(res_client, input_incident_id, want_notes=True, want_attachments=True)

          objsendtofile = {
            'incident': res_incident,
            'incident_tasks': res_incident_tasks
          }

          helper.write_file('all_data_object2.json', json.dumps(objsendtofile))
          # data = """<request>
          #             <entry>
          #               <short_description>Unable to connect to office wifi 3</short_description>
          #               <urgency>2</urgency>
          #               <impact>2</impact>
          #             </entry>
          #           </request>"""

          data = {
            "short_description": "Test incident",
            "urgency": 2,
            "impact": 3
          }

          yield StatusMessage("Appconfig Settings OK")

          response = helper.POST('/table/incident', json.dumps(data))

          success = False
          
          if response.status_code == 201: 
            success = True
          else:
            raise ValueError("Failed to create incident on ServiveNow")

          results = {
              "success": success
          }
          
          log.info("Completed")

          # Produce a FunctionResult with the results
          yield FunctionResult(results)
        except Exception:
            yield FunctionError()