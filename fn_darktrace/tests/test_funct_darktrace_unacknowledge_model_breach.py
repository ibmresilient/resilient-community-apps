# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from unittest.mock import patch

import pytest
from resilient_circuits import FunctionResult, SubmitTestFunction
from resilient_circuits.util import get_config_data, get_function_definition

PACKAGE_NAME = "fn_darktrace"
FUNCTION_NAME = "darktrace_unacknowledge_model_breach"

# Read the default configuration-data section from the package
config_data = """[fn_darktrace]
api_key=abcd-efgh
api_secret=1234-abcd-56789-efgh
darktrace_base_url=https://fake.cloud.darktrace.com
"""

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_darktrace_unacknowledge_model_breach_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("darktrace_unacknowledge_model_breach", function_params)

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
        event = circuits.watcher.wait("darktrace_unacknowledge_model_breach_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value


class TestDarktraceUnacknowledgeModelBreach:
    """ Tests for the darktrace_unacknowledge_model_breach function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    mock_inputs_1 = {
        "darktrace_model_breach_pbid": "1234abcd"
    }

    expected_results_1 = {"aianalyst": "SUCCESS"}

    mock_inputs_2 = {
        "darktrace_model_breach_pbid": "already_unacknowledged"
    }

    expected_results_2 = {"aianalyst": "ERROR"}

    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (mock_inputs_1, expected_results_1),
        (mock_inputs_2, expected_results_2)
    ])
    def test_success(self, circuits_app, mock_inputs, expected_results):
        """ Test calling with sample values for the parameters """

        with patch("fn_darktrace.components.funct_darktrace_unacknowledge_model_breach.AppCommon.unacknowledge_model_breach") as patch_nack:
            patch_nack.return_value = expected_results
            results = call_darktrace_unacknowledge_model_breach_function(circuits_app, mock_inputs)
            assert(expected_results == results.get("content"))
            patch_nack.assert_called
            patch_nack.assert_called_with(mock_inputs.get("darktrace_model_breach_pbid"))
