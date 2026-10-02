# -*- coding: utf-8 -*-
# Generated with resilient-sdk v51.0.2.2.1096
"""Tests using pytest_resilient_circuits"""

import pytest, mock_umbrella
from unittest.mock import patch
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

FUNCTION_NAME = "umbrella_threat_grid_sample"

# Read the default configuration-data section from the package
config_data = get_config_data(mock_umbrella.PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_umbrella_threat_grid_sample_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("umbrella_threat_grid_sample", function_params)

    # Fire a message to the function
    circuits.manager.fire(evt)

    # circuits will fire an "exception" event if an exception is raised in the FunctionComponent
    # return this exception if it is raised
    exception_event = circuits.watcher.wait("exception", parent=None, timeout=timeout)

    if exception_event is not False:
        exception = exception_event.args[1]
        raise exception

    # else return the FunctionComponent's results
    else:
        event = circuits.watcher.wait("umbrella_threat_grid_sample_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value


class TestUmbrellaThreatGridSample:
    """ Tests for the umbrella_threat_grid_sample function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(mock_umbrella.PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    mock_inputs_1 = {
        "umbinv_offset": 0,
        "umbinv_sample_endpoint": "basic",
        "umbinv_hash": "414e38ed0b5d507734361c2ba94f734252ca33b8259ca32334f32c4dba69b01c",
        "umbinv_limit": 30
    }

    expected_results_1 = mock_umbrella.sample_return

    mock_inputs_2 = {
        "umbinv_offset": 0,
        "umbinv_sample_endpoint": "artifacts",
        "umbinv_hash": "414e38ed0b5d507734361c2ba94f734252ca33b8259ca32334f32c4dba69b01c",
        "umbinv_limit": 30
    }

    expected_results_2 = mock_umbrella.sample_artifact_return
    
    mock_inputs_3 = {
        "umbinv_offset": 0,
        "umbinv_sample_endpoint": "connections",
        "umbinv_hash": "414e38ed0b5d507734361c2ba94f734252ca33b8259ca32334f32c4dba69b01c",
        "umbinv_limit": 30
    }

    expected_results_3 = mock_umbrella.sample_connections_return

    mock_inputs_4 = {
        "umbinv_offset": 0,
        "umbinv_sample_endpoint": "behaviors",
        "umbinv_hash": "414e38ed0b5d507734361c2ba94f734252ca33b8259ca32334f32c4dba69b01c",
        "umbinv_limit": 30
    }

    expected_results_4 = mock_umbrella.sample_behaviors_return

    mock_inputs_5 = {
        "umbinv_offset": 0,
        "umbinv_sample_endpoint": "samples",
        "umbinv_hash": "414e38ed0b5d507734361c2ba94f734252ca33b8259ca32334f32c4dba69b01c",
        "umbinv_limit": 30
    }

    expected_results_5 = mock_umbrella.samples_return

    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (mock_inputs_1, expected_results_1),
        (mock_inputs_2, expected_results_2),
        (mock_inputs_3, expected_results_3),
        (mock_inputs_4, expected_results_4),
        (mock_inputs_5, expected_results_5)
    ])
    def test_success(self, circuits_app, mock_inputs, expected_results):
        """ Test calling with sample values for the parameters """
        with patch("fn_cisco_umbrella_inv.components.umbrella_threat_grid_sample.investigateClient") as patch_client:
            patch_client.return_value = mock_umbrella.mock_client()
            results = call_umbrella_threat_grid_sample_function(circuits_app, mock_inputs)
            if results.get("content", {}).get("sample_basic"):
                assert(expected_results == results.get("content", {}).get("sample_basic"))
            elif results.get("content", {}).get("sample_artifacts"):
                assert(expected_results == results.get("content", {}).get("sample_artifacts"))
            elif results.get("content", {}).get("sample_connections"):
                assert(expected_results == results.get("content", {}).get("sample_connections"))
            elif results.get("content", {}).get("sample_samples"):
                assert(expected_results == results.get("content", {}).get("sample_samples"))
            elif results.get("content", {}).get("sample_behaviors"):
                assert(expected_results == results.get("content", {}).get("sample_behaviors"))
