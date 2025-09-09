# -*- coding: utf-8 -*-
# Generated with resilient-sdk v51.0.2.2.1096
"""Tests using pytest_resilient_circuits"""

from unittest.mock import patch
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

from tests import helper

PACKAGE_NAME = "fn_watsonx_analyst"
FUNCTION_NAME = "fn_watsonx_analyst_scan_attachment"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_fn_watsonx_analyst_scan_attachment_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("fn_watsonx_analyst_scan_attachment", function_params)

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
        event = circuits.watcher.wait("fn_watsonx_analyst_scan_attachment_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value


class TestFnWatsonxAnalystScanAttachment:
    """ Tests for the fn_watsonx_analyst_scan_attachment function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    mock_inputs_1 = {
        "fn_watsonx_analyst_incident_id": 123,
        "fn_watsonx_analyst_attachment_id": 1411,
        "fn_watsonx_analyst_model_id": "ibm/granite-3-2b-instruct",
        "fn_watsonx_analyst_task_id": None,
    }

    expected_results_1 = 'Attachment name: runme2.sh\n\n<p style="display: inline">Lorem ipsum</p>'

    mock_inputs_2 = {
        "fn_watsonx_analyst_incident_id": 123,
        "fn_watsonx_analyst_attachment_id": 321,
        "fn_watsonx_analyst_model_id": "ibm/granite-3-2b-instruct",
        "fn_watsonx_analyst_task_id": 1,
    }

    @patch("fn_watsonx_analyst.util.rest.RestHelper.do_request", helper.mock_do_request)
    @patch("fn_watsonx_analyst.util.QueryHelper.QueryHelper.get_api_key", helper.mock_get_api_key)
    @patch("fn_watsonx_analyst.util.QueryHelper.QueryHelper.text_generation", helper.mock_text_generation)
    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (mock_inputs_1, expected_results_1),
        (mock_inputs_2, expected_results_1)
    ])
    def test_success(self, circuits_app, mock_inputs, expected_results):
        """ Test calling with sample values for the parameters """
        results = call_fn_watsonx_analyst_scan_attachment_function(circuits_app, mock_inputs)
        assert results["content"]["generated_text"].strip() == expected_results
