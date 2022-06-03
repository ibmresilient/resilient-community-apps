# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

import pytest
import time
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_playbook_maker"
FUNCTION_NAME = "make_playbook"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
#resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_make_playbook_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("make_playbook", function_params)

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
        event = circuits.watcher.wait("make_playbook_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value


class TestMakePlaybook:
    """ Tests for the make_playbook function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    mock_inputs_1 = {
        "pbm_app_name": "fn_scheduler",
        "pbm_function_names": None,
        "pdm_activation_fields": True,
        "pbm_playbook_type": "incident",
        "pbm_activation_type": "Manual",
        "pbm_playbook_name": "test app_"+str(int(time.time()))
    }

    expected_results_1 = {"value": "xyz"}

    mock_inputs_2 = {
        "pbm_app_name": None,
        "pbm_function_names": "create_a_scheduled_rule, list_scheduled_rules",
        "pdm_activation_fields": False,
        "pbm_playbook_type": "artifact",
        "pbm_activation_type": "Automatic",
        "pbm_playbook_name": "test function_"+str(int(time.time()))
    }

    expected_results_2 = {"value": "xyz"}

    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (mock_inputs_2, expected_results_2)
    ])
    def test_success(self, circuits_app, mock_inputs, expected_results):
        """ Test calling with sample values for the parameters """

        results = call_make_playbook_function(circuits_app, mock_inputs)
        assert(expected_results == results)
