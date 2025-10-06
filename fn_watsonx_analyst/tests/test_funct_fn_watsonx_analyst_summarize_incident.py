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
FUNCTION_NAME = "fn_watsonx_analyst_summarize_incident"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_fn_watsonx_analyst_summarize_incident_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("fn_watsonx_analyst_summarize_incident", function_params)

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
            "fn_watsonx_analyst_summarize_incident_result", parent=evt, timeout=timeout
        )
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value


class TestFnWatsonxSummarizeIncident:
    """Tests for the fn_watsonx_analyst_summarize_incident function"""

    cold_mem_limit = "40 MB"

    """Test that the package provides customization_data that defines the function"""
    func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
    assert func is not None

    mock_inputs_1 = {
        "fn_watsonx_analyst_summary_type": "executive",
        "fn_watsonx_analyst_model_id": "ibm/granite-3-2b-instruct",
        "fn_watsonx_analyst_incident_id": 123,
        "fn_watsonx_analyst_data_config": "default",
    }

    expected_results_1 = "Lorem ipsum"

    mock_inputs_2 = {
        "fn_watsonx_analyst_summary_type": "technical",
        "fn_watsonx_analyst_model_id": "ibm/granite-3-2b-instruct",
        "fn_watsonx_analyst_incident_id": 456,
        "fn_watsonx_analyst_data_config": "default",
    }

    expected_results_2 = "**Incomplete tasks**"

    @pytest.mark.limit_memory(cold_mem_limit)
    @patch("fn_watsonx_analyst.util.rest.RestHelper.do_request", helper.mock_do_request)
    @patch(
        "fn_watsonx_analyst.util.QueryHelper.QueryHelper.get_api_key",
        helper.mock_get_api_key,
    )
    @patch(
        "fn_watsonx_analyst.util.QueryHelper.QueryHelper.text_generation",
        helper.mock_text_generation,
    )
    def test_success_executive(self, circuits_app):
        """Test calling with sample values for the parameters"""

        results = call_fn_watsonx_analyst_summarize_incident_function(
            circuits_app, self.mock_inputs_1
        )
        
        assert self.expected_results_1 in results["content"]["raw_output"]

        for check in ['<strong>Executive Summary</strong>', '<strong>Incident Type(s)</strong>', '<strong>Incident Severity</strong>']:
            assert check in results["content"]["generated_text"]
    @patch("fn_watsonx_analyst.util.rest.RestHelper.do_request", helper.mock_do_request)
    @patch(
        "fn_watsonx_analyst.util.QueryHelper.QueryHelper.get_api_key",
        helper.mock_get_api_key,
    )
    @patch(
        "fn_watsonx_analyst.util.QueryHelper.QueryHelper.text_generation",
        helper.mock_text_generation,
    )
    def test_success_technical(self, circuits_app):
        """Test calling with sample values for the parameters"""

        results = call_fn_watsonx_analyst_summarize_incident_function(
            circuits_app, self.mock_inputs_2
        )
        
        assert self.expected_results_2 in results["content"]["raw_output"]

        for check in ['<strong>Technical Summary</strong>', '<strong>Incident Type(s)</strong>', '<strong>Incident Severity</strong>']:
            assert check in results["content"]["generated_text"]