# -*- coding: utf-8 -*-
# Generated with resilient-sdk v51.0.1.0.695
"""Tests using pytest_resilient_circuits"""

import pytest, helper
from unittest.mock import patch
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

FUNCTION_NAME = "fn_ansible"

# Read the default configuration-data section from the package
config_data = get_config_data(helper.PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_fn_ansible_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("fn_ansible", function_params)

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
        event = circuits.watcher.wait("fn_ansible_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value


class TestFnAnsible:
    """ Tests for the fn_ansible function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(helper.PACKAGE_NAME, FUNCTION_NAME)
        assert func

    mock_inputs_1 = {
        "ansible_parameters": "command=echo Hello",
        "ansible_playbook_name": "playbook2"
    }

    expected_results_1 = {"summary": "successful", "stdout": "Hello"}

    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (mock_inputs_1, expected_results_1)
    ])
    def test_success(self, circuits_app, mock_inputs, expected_results):
        """ Test calling with sample values for the parameters """
        with patch("fn_ansible.components.funct_fn_ansible.run_playbook") as patch_ack:
            patch_ack.return_value = helper.run_ansible_playbook_results()
            results = call_fn_ansible_function(circuits_app, mock_inputs)
            assert(expected_results.get("summary") == results.get("content", {}).get("127.0.0.1", {}).get("summary"))
            assert(expected_results.get("stdout") == results.get("content", {}).get("127.0.0.1", {}).get("detail", {}).get("stdout"))
