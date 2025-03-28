# -*- coding: utf-8 -*-
# Generated with resilient-sdk v50.1.262
"""Tests using pytest_resilient_circuits"""

from unittest.mock import patch
import pytest, helper
from resilient_circuits.util import get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

FUNCTION_NAME = "splunk_update_notable"

# Read the default configuration-data section from the package
config_data = helper.config_data

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_splunk_update_notable_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("splunk_update_notable", function_params)

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
        event = circuits.watcher.wait("splunk_update_notable_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value


class TestSplunkUpdateNotable:
    """ Tests for the splunk_update_notable function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(helper.PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    mock_inputs_1 = {
        "comment": "SOAR incident is active",
        "splunk_label": None,
        "event_id": "0DE6791A-6F7D-42DC-BAF0-26D58032AE40@@notable@@b98308abb5851cacd0589ec3177389d6",
        "notable_event_status": 2
    }

    expected_results_1 = helper.update_notable_results()

    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (mock_inputs_1, expected_results_1)
    ])
    def test_success(self, circuits_app, mock_inputs, expected_results):
        """ Test calling with sample values for the parameters """
        with patch("fn_splunk_integration.components.splunk_update_notable.function_basics") as patch_ack:
            patch_ack.return_value = helper.mock_init()
            results = call_splunk_update_notable_function(circuits_app, mock_inputs)
            assert(expected_results == results.get("content"))
