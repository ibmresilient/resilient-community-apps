# -*- coding: utf-8 -*-
# Generated with resilient-sdk v49.1.51
"""Tests using pytest_resilient_circuits"""

from unittest.mock import patch
import pytest, helper
from resilient_circuits.util import get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

FUNCTION_NAME = "azure_get_runbook"

# Read the default configuration-data section from the package
config_data = helper.config_data

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_azure_get_runbook_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("azure_get_runbook", function_params)

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
        event = circuits.watcher.wait("azure_get_runbook_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value


class TestAzureGetRunbook:
    """ Tests for the azure_get_runbook function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(helper.PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    mock_inputs_1 = {
        "account_name": "automation1",
        "runbook_name": "demoassets",
        "resource_group_name": "Hello_world"
    }

    expected_results_1 = helper.get_runbook_results()

    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (mock_inputs_1, expected_results_1)
    ])
    def test_success(self, circuits_app, mock_inputs, expected_results):
        """ Test calling with sample values for the parameters """
        with patch("fn_azure_automation_utilities.components.funct_azure_get_runbook.get_azure_client") as patch_ack:
            patch_ack.return_value = helper.mock_init()
            results = call_azure_get_runbook_function(circuits_app, mock_inputs)
            assert(expected_results == results.get("content", {}))
