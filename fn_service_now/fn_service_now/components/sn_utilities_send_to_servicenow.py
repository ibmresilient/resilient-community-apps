# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError


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

        try:
            # Get the function parameters:
            incident_id = kwargs.get("incident_id")  # number
            task_id = kwargs.get("task_id")  # number
            attachment_id = kwargs.get("attachment_id")  # number
            note_id = kwargs.get("note_id")  # number
            artifact_id = kwargs.get("artifact_id")  # number
            sn_ref_id = kwargs.get("sn_ref_id")  # text
            sn_comment_type = kwargs.get("sn_comment_type")  # text
            sn_optional_fields = kwargs.get("sn_optional_fields")  # text
            sn_track_changes = kwargs.get("sn_track_changes")  # boolean

            log = logging.getLogger(__name__)
            log.info("incident_id: %s", incident_id)
            log.info("task_id: %s", task_id)
            log.info("attachment_id: %s", attachment_id)
            log.info("note_id: %s", note_id)
            log.info("artifact_id: %s", artifact_id)
            log.info("sn_ref_id: %s", sn_ref_id)
            log.info("sn_comment_type: %s", sn_comment_type)
            log.info("sn_optional_fields: %s", sn_optional_fields)
            log.info("sn_track_changes: %s", sn_track_changes)

            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE
            #  yield StatusMessage("starting...")
            #  yield StatusMessage("done...")

            results = {
                "value": "xyz"
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()