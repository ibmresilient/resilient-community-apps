# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_service_now.util.resilient_helper import ResilientHelper
try:
    # for Python 2.x
    from StringIO import StringIO
except ImportError:
    # for Python 3.x
    from io import StringIO
import csv

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'sn_utilities_send_to_servicenow"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_service_now", {})

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
            input_incident_id = res_helper.get_function_input(kwargs, "incident_id")  # number (required)
            input_task_id = res_helper.get_function_input(kwargs, "task_id", True)  # number
            input_attachment_id = res_helper.get_function_input(kwargs, "attachment_id", True)  # number
            input_note_id = res_helper.get_function_input(kwargs, "note_id", True)  # number
            input_artifact_id = res_helper.get_function_input(kwargs, "artifact_id", True)  # number
            input_sn_ref_id = res_helper.get_function_input(kwargs, "sn_ref_id", True)  # text
            input_sn_comment_type = res_helper.get_function_input(kwargs, "sn_comment_type", True)  # text
            input_sn_optional_fields = res_helper.get_function_input(kwargs, "sn_optional_fields", True)  # text [csv]
            input_sn_init_work_note = res_helper.get_function_input(kwargs, "sn_init_work_note", True)  # text
            input_sn_track_changes = res_helper.get_function_input(kwargs, "sn_track_changes", True)  # boolean
            yield StatusMessage("Function Inputs OK")

            # Convert input_sn_optional_fields in CSV to Python list
            if input_sn_optional_fields is not None:
              optional_fields_as_list = []
              f = StringIO(input_sn_optional_fields)
              reader = csv.reader(f, delimiter=',')
              for value in reader:
                optional_fields_as_list.append(value)
              input_sn_optional_fields = optional_fields_as_list[0]

            # Instansiate new Resilient API object
            res_client = self.rest_client()

            if input_incident_id and input_task_id:
              task = res_helper.get_task(res_client, input_task_id, input_incident_id, input_sn_optional_fields)
              
              # TODO
              # Send task to ServiceNow

            log.info("incident_id: %s", input_incident_id)
            log.info("task_id: %s", input_task_id)
            log.info("attachment_id: %s", input_attachment_id)
            log.info("note_id: %s", input_note_id)
            log.info("artifact_id: %s", input_artifact_id)
            log.info("sn_ref_id: %s", input_sn_ref_id)
            log.info("sn_comment_type: %s", input_sn_comment_type)
            log.info("sn_optional_fields: %s", input_sn_optional_fields)
            log.info("sn_init_work_note: %s", input_sn_init_work_note)
            log.info("sn_track_changes: %s", input_sn_track_changes)

            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE
            #  yield StatusMessage("starting...")
            #  yield StatusMessage("done...")

            results = {
                "success": True
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()