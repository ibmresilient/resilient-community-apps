# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_codegen_test"
FUNCTION_NAME = "utilities_base64_to_artifact"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_utilities_base64_to_artifact_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("utilities_base64_to_artifact", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("utilities_base64_to_artifact_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestUtilitiesBase64ToArtifact:
    """ Tests for the utilities_base64_to_artifact function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.parametrize("base64content, incident_id, artifact_file_type, file_name, content_type, description, expected_results", [
        ("text", 123, 'Email Attachment', "text", "text", {"type": "text", "content": "line1\nline2"}, {"value": "xyz"}),
        ("text", 123, 'Malware Sample', "text", "text", {"type": "text", "content": "line1\nline2"}, {"value": "xyz"})
    ])
    def test_success(self, circuits_app, base64content, incident_id, artifact_file_type, file_name, content_type, description, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = { 
            "base64content": base64content,
            "incident_id": incident_id,
            "artifact_file_type": artifact_file_type,
            "file_name": file_name,
            "content_type": content_type,
            "description": description
        }
        results = call_utilities_base64_to_artifact_function(circuits_app, function_params)
        assert(expected_results == results)