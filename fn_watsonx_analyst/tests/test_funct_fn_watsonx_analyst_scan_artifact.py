# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.
# Generated with resilient-sdk v51.0.2.2.1096
"""Tests using pytest_resilient_circuits"""

from unittest.mock import patch
import pytest
from tests import helper
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_watsonx_analyst"
FUNCTION_NAME = "fn_watsonx_analyst_scan_artifact"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_fn_watsonx_analyst_scan_artifact_function(
    circuits, function_params, timeout=5
):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("fn_watsonx_analyst_scan_artifact", function_params)

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
        event = circuits.watcher.wait(
            "fn_watsonx_analyst_scan_artifact_result", parent=evt, timeout=timeout
        )
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value


class TestFnWatsonxScanArtifact:
    """Tests for the fn_watsonx_analyst_scan_artifact function"""

    cold_mem_limit = "40 MB"

    def test_function_definition(self):
        """Test that the package provides customization_data that defines the function"""
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    mock_inputs_1 = {
        "fn_watsonx_analyst_incident_id": 123,
        "fn_watsonx_analyst_artifact_id": 123,
        "fn_watsonx_analyst_model_id": "ibm/granite-13b-chat-v2",
        "fn_watsonx_analyst_system_prompt": "sample text",
    }

    expected_results_1 = "Artifact name: runme2.sh\n\n<p>Lorem ipsum</p>"

    mock_inputs_2 = {
        "fn_watsonx_analyst_incident_id": 123,
        "fn_watsonx_analyst_artifact_id": 1412,
        "fn_watsonx_analyst_model_id": "ibm/granite-13b-chat-v2",
        "fn_watsonx_analyst_system_prompt": "sample text",
    }

    expected_results_2 = "Parsed content from the artifact 'image.png' is empty or could not be extracted."

    @patch("fn_watsonx_analyst.util.rest.RestHelper.do_request", helper.mock_do_request)
    @patch(
        "fn_watsonx_analyst.util.QueryHelper.QueryHelper.get_api_key",
        helper.mock_get_api_key,
    )
    @patch(
        "fn_watsonx_analyst.util.QueryHelper.QueryHelper.text_generation",
        helper.mock_text_generation,
    )
    @pytest.mark.parametrize(
        "mock_inputs, expected_results",
        [(mock_inputs_1, expected_results_1), (mock_inputs_2, expected_results_2)],
    )
    @pytest.mark.limit_memory(cold_mem_limit)
    def test_success(self, circuits_app, mock_inputs, expected_results):
        """Test calling with sample values for the parameters"""

        results = call_fn_watsonx_analyst_scan_artifact_function(
            circuits_app, mock_inputs
        )
        assert results["content"]["generated_text"] == expected_results
