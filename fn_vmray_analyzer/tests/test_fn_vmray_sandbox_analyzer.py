# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_vmray_analyzer"
FUNCTION_NAME = "fn_vmray_sandbox_analyzer"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_fn_vmray_sandbox_analyzer_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("fn_vmray_sandbox_analyzer", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("fn_vmray_sandbox_analyzer_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestFnVmraySandboxAnalyzer:
    """ Tests for the fn_vmray_sandbox_analyzer function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.parametrize("incident_id, artifact_id, attachment_id, analysis_report_status, expected_results", [
        (123, 123, 123, True, {"value": "xyz"}),
        (123, 123, 123, True, {"value": "xyz"})
    ])
    def test_success(self, circuits_app, incident_id, artifact_id, attachment_id, analysis_report_status, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = { 
            "incident_id": incident_id,
            "artifact_id": artifact_id,
            "attachment_id": attachment_id,
            "analysis_report_status": analysis_report_status
        }
        results = call_fn_vmray_sandbox_analyzer_function(circuits_app, function_params)
        assert(expected_results == results)