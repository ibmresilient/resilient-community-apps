# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits
test as: pytest --resilient_app_config /path/to/.resilient/app.config -s
"""

from __future__ import print_function
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_virustotal"
FUNCTION_NAME = "virustotal"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_virustotal_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("virustotal", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("virustotal_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestVirustotal:
    """ Tests for the virustotal function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.parametrize("incident_id, artifact_id, attachment_id, vt_type, vt_data, expected_results", [
        (123, 123, 123, "ip", "8.8.8.8", 'detected_urls'),
        (123, 123, 123, "hash", "85be64025453711c9c7396efe3965b79f0115fd6647c68d186edf88d6398c21f", "permalink")
    ])
    def test_success(self, circuits_app, incident_id, artifact_id, attachment_id, vt_type, vt_data, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = { 
            "incident_id": incident_id,
            "artifact_id": artifact_id,
            "attachment_id": attachment_id,
            "vt_type": vt_type,
            "vt_data": vt_data
        }
        results = call_virustotal_function(circuits_app, function_params)
        assert results['scan'][expected_results]