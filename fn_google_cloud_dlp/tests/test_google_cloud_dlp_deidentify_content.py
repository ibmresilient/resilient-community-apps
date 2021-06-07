# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_google_cloud_dlp"
FUNCTION_NAME = "google_cloud_dlp_deidentify_content"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_google_cloud_dlp_deidentify_content_function(circuits, function_params, timeout=10):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("google_cloud_dlp_deidentify_content", function_params)

    # Add the workflow_instance_id
    evt.kwargs.get("message").update({
        "workflow_instance": {
            "workflow_instance_id": 123
        }
    })

    # Fire a message to the function
    circuits.manager.fire(evt)

    # circuits will fire an "exception" event if an exception is raised in the FunctionComponent
    # return this exception if it is raised
    exception_event = circuits.watcher.wait("exception", parent=None, timeout=timeout)

    if exception_event is not False:
        exception = exception_event.args[1].args[1]
        raise exception

    # else return the FunctionComponent's results
    else:

        # Fire a message to the function
        #evt = SubmitTestFunction("google_cloud_dlp_deidentify_content", function_params)
        circuits.manager.fire(evt)
        event = circuits.watcher.wait("google_cloud_dlp_deidentify_content_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value


class TestGoogleCloudDlpDeidentifyContent:
    """ Tests for the google_cloud_dlp_deidentify_content function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.livetest
    @pytest.mark.parametrize("artifact_id, attachment_id, incident_id, task_id, gcp_artifact_input, gcp_dlp_info_types, expected_results", [
        (123, 123, 123, 123, "My name is John", ['FIRST_NAME', 'PERSON_NAME', 'US_INDIVIDUAL_TAXPAYER_IDENTIFICATION_NUMBER'], {"value": "xyz"}),
        (123, 123, 123, 123, "My email is johnsmith@gmail.com", ['EMAIL_ADDRESS', 'US_BANK_ROUTING_MICR'], {"value": "xyz"})
    ])
    def test_success(self, circuits_app, artifact_id, attachment_id, incident_id, task_id, gcp_artifact_input, gcp_dlp_info_types, expected_results):
        """ Test calling with sample values for the parameters """


        function_params = { 
            "artifact_id": artifact_id,
            "attachment_id": attachment_id,
            "incident_id": incident_id,
            "task_id": task_id,
            "gcp_artifact_input": gcp_artifact_input,
            "gcp_dlp_info_types": gcp_dlp_info_types
        }
        results = call_google_cloud_dlp_deidentify_content_function(circuits_app, function_params)
        assert(not any(item in results["content"]["de_identified_text"] for item in ['John', 'johnsmith@gmail.com']))

    @pytest.mark.livetest
    @pytest.mark.parametrize(
        "artifact_id, attachment_id, incident_id, task_id, gcp_artifact_input, gcp_dlp_info_types, expected_results", [
            (123, 123, 123, 123, "My name is John",
             ['US_INDIVIDUAL_TAXPAYER_IDENTIFICATION_NUMBER'], {"value": "xyz"}),
            (123, 123, 123, 123, "My email is johnsmith@gmail.com", ['US_BANK_ROUTING_MICR'],
             {"value": "xyz"})
        ])
    def test_non_removal(self, circuits_app, artifact_id, attachment_id, incident_id, task_id, gcp_artifact_input,
                     gcp_dlp_info_types, expected_results):
        """ Test calling with sample values for the parameters
         In this test, we are ensuring, if we explicity do not specify an info type
         any instances of that info_type are not removed.
         This requires at least 1 info type specified"""

        function_params = {
            "artifact_id": artifact_id,
            "attachment_id": attachment_id,
            "incident_id": incident_id,
            "task_id": task_id,
            "gcp_artifact_input": gcp_artifact_input,
            "gcp_dlp_info_types": gcp_dlp_info_types
        }
        results = call_google_cloud_dlp_deidentify_content_function(circuits_app, function_params)
        assert (any(item in results["content"]["de_identified_text"] for item in ['John', 'johnsmith@gmail.com']))