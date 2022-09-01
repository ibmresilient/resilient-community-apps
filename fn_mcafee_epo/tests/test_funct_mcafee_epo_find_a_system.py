# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_mcafee_epo"
FUNCTION_NAME = "mcafee_epo_find_a_system"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_mcafee_epo_find_a_system_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("mcafee_epo_find_a_system", function_params)

    # Fire a message to the function
    circuits.manager.fire(evt)

    # circuits will fire an "exception" event if an exception is raised in the FunctionComponent
    # return this exception if it is raised
    exception_event = circuits.watcher.wait("exception", parent=None, timeout=timeout)

    if exception_event is not False:
        exception = exception_event.args[1].args[1]
        raise exception

    # else return the FunctionComponent's results
    else:
        event = circuits.watcher.wait("mcafee_epo_find_a_system_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value


class TestMcafeeEpoFindASystem:
    """ Tests for the mcafee_epo_find_a_system function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    # this live test relies on the server "test_server" existing in your EPO system
    @pytest.mark.livetest
    @pytest.mark.parametrize("mock_inputs", [
        ({"mcafee_epo_systems": "test_server"})
    ])
    def test_success(self, circuits_app, mock_inputs):
        """ Test calling with sample values for the parameters """

        results = call_mcafee_epo_find_a_system_function(circuits_app, mock_inputs)
        assert(results['content'])


    @pytest.mark.livetest
    @pytest.mark.parametrize("mock_inputs", [
        ({"mcafee_epo_systems": "not_found"})
    ])
    def test_failure(self, circuits_app, mock_inputs):
        """ Test calling with sample values for the parameters """

        results = call_mcafee_epo_find_a_system_function(circuits_app, mock_inputs)
        assert(not results['content'])
