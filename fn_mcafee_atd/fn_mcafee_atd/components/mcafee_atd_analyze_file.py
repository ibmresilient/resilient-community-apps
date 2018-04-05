# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'mcafee_atd_analyze_file"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_mcafee_atd", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_mcafee_atd", {})

    def getFile(self, incident_id, artifact_id, file_location, **kwargs):
        url_switcher = {
            "Artifact": "/incidents/{}/artifacts/{}/contents",
            "Attachment": "/incidents/{}/attachments/{}/contents",
            "Task": "/tasks/{}/attachments/{}/contents"
        }
        url = ""
        if file_location == "Artifact":
            url = "/incidents/{}/artifacts/{}/contents".format(kwargs["incident_id"], kwargs["artifact_id"])
        elif file_location == "Attachment":
            url = "/incidents/{}/attachments/{}/contents".format(kwargs["incident_id"], kwargs["attachment_id"])
        elif file_location == "Task":
            url = "/tasks/{}/attachments/{}/contents".format(kwargs["task_id"], kwargs["attachment_id"])

        # url_base = url_switcher[file_location]
        resilient_client = self.rest_client()

        # url = url_base.format(incident_id, artifact_id)
        response = resilient_client.get_content(url)
        return response

    @function("mcafee_atd_analyze_file")
    def _mcafee_atd_analyze_file_function(self, event, *args, **kwargs):
        """Function: """
        try:
            yield StatusMessage("starting...")

            # Get the function parameters:
            incident_id = kwargs.get("incident_id")  # number
            artifact_id = kwargs.get("artifact_id")  # number
            mcafee_atd_file_location = self.get_select_param(kwargs.get("mcafee_atd_file_location"))  # select

            log = logging.getLogger(__name__)
            log.info("incident_id: %s", incident_id)
            log.info("artifact_id: %s", artifact_id)
            self.get_select_param(kwargs.get("inputType"))

            file = self.getFile(incident_id, artifact_id, mcafee_atd_file_location)


            results = {
                "value": "xyz"
            }

            yield StatusMessage("done...")
            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()