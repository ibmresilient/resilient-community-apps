# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.
# Generated with resilient-sdk v51.0.2.0.974
"""Tests using pytest_resilient_circuits"""
from unittest.mock import patch
import concurrent
import pytest
from tests import helper
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_watsonx_analyst"
FUNCTION_NAME = "fn_watsonx_analyst_converse_via_notes"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_fn_watsonx_analyst_converse_via_notes_function(
    circuits, function_params, timeout=5
):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("fn_watsonx_analyst_converse_via_notes", function_params)

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
            "fn_watsonx_analyst_converse_via_notes_result", parent=evt, timeout=timeout
        )
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value


@patch("fn_watsonx_analyst.util.rest.RestHelper.do_request", helper.mock_do_request)
@patch(
    "fn_watsonx_analyst.util.QueryHelper.QueryHelper.get_api_key",
    helper.mock_get_api_key,
)
@patch(
    "fn_watsonx_analyst.util.QueryHelper.QueryHelper.text_generation",
    helper.mock_text_generation,
)
@patch(
    "fn_watsonx_analyst.util.QueryHelper.QueryHelper.generate_embeddings",
    helper.mock_generate_embeddings,
)
class TestFnWatsonxConverseViaNotes:
    """Tests for the fn_watsonx_analyst_converse_via_notes function"""

    cold_mem_limit = "120 MB"
    hot_mem_limit = "50 MB"
    parallel_mem_limit = "1000 MB"

    def test_function_definition(self):
        """Test that the package provides customization_data that defines the function"""
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    mock_inputs_1 = {
        "fn_watsonx_analyst_note_id": 1,
        "fn_watsonx_analyst_system_prompt": "sample text",
        "fn_watsonx_analyst_prompt": "sample text",
        "fn_watsonx_analyst_model_id": "mistralai/mistral-small-3-1-24b-instruct-2503",
        "fn_watsonx_analyst_incident_id": 123,
        "fn_watsonx_analyst_data_config": "default",
    }
    expected_results_1 = "Lorem ipsum"

    mock_inputs_2 = {
        "fn_watsonx_analyst_note_id": 2,
        "fn_watsonx_analyst_system_prompt": "sample text",
        "fn_watsonx_analyst_prompt": "sample text",
        "fn_watsonx_analyst_model_id": "mistralai/mistral-small-3-1-24b-instruct-2503",
        "fn_watsonx_analyst_incident_id": 123,
        "fn_watsonx_analyst_data_config": "default",
    }

    mock_inputs_3 = {
        "fn_watsonx_analyst_note_id": 3,
        "fn_watsonx_analyst_model_id": "mistralai/mistral-small-3-1-24b-instruct-2503",
        "fn_watsonx_analyst_incident_id": 123,
        "fn_watsonx_analyst_data_config": "default",
    }

    mock_inputs_4 = {
        "fn_watsonx_analyst_note_id": 4,
        # "fn_watsonx_analyst_prompt": "[runme3.sh]",
        "fn_watsonx_analyst_model_id": "mistralai/mistral-small-3-1-24b-instruct-2503",
        "fn_watsonx_analyst_incident_id": 123,
        "fn_watsonx_analyst_data_config": "default",
    }

    artifact_expected_results_4 = "Parsed content is empty or could not be extracted."
    artifact_expected_results = "Artifact conversation"
    artifact_expected_results_5 = "Lorem ipsum"

    mock_inputs_5 = {
        "fn_watsonx_analyst_note_id": 5,
        "fn_watsonx_analyst_model_id": "mistralai/mistral-small-3-1-24b-instruct-2503",
        "fn_watsonx_analyst_incident_id": 123,
        "fn_watsonx_analyst_data_config": "default",
    }

    @pytest.mark.parametrize(
        "mock_inputs, expected_results",
        [
            (mock_inputs_1, expected_results_1),
            (mock_inputs_5, artifact_expected_results_5),
        ],
    )
    @pytest.mark.limit_memory(cold_mem_limit)
    def test_success(self, circuits_app, mock_inputs, expected_results):
        """Test calling with sample values for the parameters"""
        results = call_fn_watsonx_analyst_converse_via_notes_function(
            circuits_app, mock_inputs
        )
        assert results["content"]["raw_output"] == expected_results

    def test_bad_html_artifact_name(self, circuits_app):
        """test to test html artifact"""
        results = call_fn_watsonx_analyst_converse_via_notes_function(
            circuits_app, self.mock_inputs_3
        )
        assert results["content"]["raw_output"] == self.artifact_expected_results

    def test_empty_artifact_content(self, circuits_app):
        """test to test empty artifact"""
        results = call_fn_watsonx_analyst_converse_via_notes_function(
            circuits_app, self.mock_inputs_4
        )
        assert results["content"]["generated_text"] == self.artifact_expected_results_4

    @pytest.mark.parametrize(
        "mock_inputs, expected_results", [(mock_inputs_2, artifact_expected_results)]
    )
    @pytest.mark.limit_memory(hot_mem_limit)
    def test_mem_pressure(self, circuits_app, mock_inputs, expected_results):
        """Test calling with sample values for the parameters"""
        results = call_fn_watsonx_analyst_converse_via_notes_function(
            circuits_app, mock_inputs
        )
        assert results["content"]["raw_output"] == expected_results

    @pytest.mark.limit_memory(parallel_mem_limit)
    def test_mem_pressure_parallel(self, circuits_app):
        """Testing memory pressure during parallel execution"""
        # run 12 instances of converse_via_notes_function in concurrent futures
        with concurrent.futures.ThreadPoolExecutor(max_workers=12) as executor:
            futures = [
                executor.submit(
                    call_fn_watsonx_analyst_converse_via_notes_function,
                    circuits_app,
                    self.mock_inputs_2,
                )
                for _ in range(12)
            ]
            for future in concurrent.futures.as_completed(futures):
                assert (
                    future.result().get("content", {}).get("raw_output")
                    == self.artifact_expected_results
                )
