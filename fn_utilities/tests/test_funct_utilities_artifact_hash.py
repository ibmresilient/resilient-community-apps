# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from mock_artifact import ArtifactMock
from pytest_resilient_circuits import verify_subset
from resilient_circuits import SubmitTestFunction, FunctionResult
from resilient_circuits.util import get_config_data, get_function_definition

PACKAGE_NAME = "fn_utilities"
FUNCTION_NAME = "utilities_artifact_hash"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the SOAR REST API (uncomment to connect to a real appliance)
resilient_mock = ArtifactMock

def call_utilities_artifact_hash_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction(FUNCTION_NAME, function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("{}_result".format(FUNCTION_NAME), parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value

class TestUtilitiesArtifactHash:
    """ Tests for the utilities_artifact_hash function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.parametrize("incident_id, artifact_id, expected_results", [
        (1, 8, {"sha1": "ef3207dd8c9caf3d4f8d3c8d6ccb3e2fcd2abf75"})
    ])
    def test_success(self, circuits_app, incident_id, artifact_id, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = {
            "incident_id": incident_id,
            "artifact_id": artifact_id
        }
        results = call_utilities_artifact_hash_function(circuits_app, function_params)
        verify_subset(expected_results, results)
