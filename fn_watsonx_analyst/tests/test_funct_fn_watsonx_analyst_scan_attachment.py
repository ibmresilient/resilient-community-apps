# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2026. All Rights Reserved.
# Generated with resilient-sdk v51.0.2.2.1096
"""Tests using pytest_resilient_circuits"""

from unittest.mock import patch
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

from fn_watsonx_analyst.util.rest import RestUrls
from tests import helper
from tests.utils import were_ai_fields_updated

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


@patch("fn_watsonx_analyst.util.rest.RestHelper.do_request", helper.mock_do_request)
class TestFnWatsonxAnalystScanAttachment:
    """ Tests for the fn_watsonx_analyst_scan_attachment function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    mock_inputs_1 = {
        "fn_watsonx_analyst_incident_id": 123,
        "fn_watsonx_analyst_attachment_id": 1411,
        "fn_watsonx_analyst_model_id": "mistralai/mistral-small-3-1-24b-instruct-2503",
        "fn_watsonx_analyst_task_id": None,
    }

    expected_results_1 = 'Attachment name: runme2.sh'

    mock_inputs_2 = {
        "fn_watsonx_analyst_incident_id": 123,
        "fn_watsonx_analyst_attachment_id": 321,
        "fn_watsonx_analyst_model_id": "mistralai/mistral-small-3-1-24b-instruct-2503",
        "fn_watsonx_analyst_task_id": 1,
    }

    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (mock_inputs_1, expected_results_1),
        (mock_inputs_2, expected_results_1)
    ])
    def test_success(self, circuits_app, mock_inputs, expected_results):
        """ Test calling with sample values for the parameters """
        results = call_fn_watsonx_analyst_scan_attachment_function(circuits_app, mock_inputs)
        assert expected_results in results["content"]["generated_text"].strip() 


    @pytest.mark.parametrize(
        "ai_fields_present",
        [True, False]
    )
    def test_ai_fields_updated(self, circuits_app, ai_fields_present):
        call_tracker = []

        def tracking_mock(self, uri, **kwargs):
            call_tracker.append((uri, kwargs))
            return helper.mock_do_request(self, uri, **kwargs)

        with patch("fn_watsonx_analyst.util.rest.RestHelper.do_request", tracking_mock):
            with patch("fn_watsonx_analyst.watsonx_app_function.WatsonxAppFunction.ai_fields_present", return_value=ai_fields_present):
                results = call_fn_watsonx_analyst_scan_attachment_function(circuits_app, self.mock_inputs_1)

                assert results["content"]["metadata"]["soar_insights_added"] == ai_fields_present

                obj = were_ai_fields_updated(
                    call_tracker, RestUrls.UPDATE_ATTACHMENT_AI_INSIGHTS, None, 
                    "incident_attachment_id", "attach_ai_insights"
                )

                if ai_fields_present:
                    assert obj is not None
                else:
                    assert obj is None
