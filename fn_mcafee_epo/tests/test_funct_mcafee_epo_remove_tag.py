# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

import pytest
from resilient_lib.components.integration_errors import IntegrationError
from resilient_circuits.action_message import FunctionException_
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_mcafee_epo"
FUNCTION_NAME = "mcafee_epo_remove_tag"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_mcafee_epo_remove_tag_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("mcafee_epo_remove_tag", function_params)

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
        event = circuits.watcher.wait("mcafee_epo_remove_tag_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value

def call_mcafee_tag_an_epo_asset_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("mcafee_tag_an_epo_asset", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("mcafee_tag_an_epo_asset_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestMcafeeEpoRemoveTag:
    """ Tests for the mcafee_epo_remove_tag function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.livetest
    @pytest.mark.parametrize("mcafee_epo_systems, mcafee_epo_tag", [
        ("test_server", "Server")
    ])
    def test_success(self, circuits_app, mcafee_epo_systems, mcafee_epo_tag):
        """ Test calling with sample values for the parameters """
        function_params = { 
            "mcafee_epo_systems": mcafee_epo_systems,
            "mcafee_epo_tag": mcafee_epo_tag
        }

        # first add tag
        results = call_mcafee_tag_an_epo_asset_function(circuits_app, function_params)
        assert(results['content'])
        results = call_mcafee_epo_remove_tag_function(circuits_app, function_params)
        assert(results['content'])

        # delete again which should fail
        results = call_mcafee_epo_remove_tag_function(circuits_app, function_params)
        assert(not results['content'])

    @pytest.mark.livetest
    @pytest.mark.parametrize("mcafee_epo_systems, mcafee_epo_tag, expected_results", [
        ("test_server", "Server", {"content": 0}),
        ("not_found", "Server", {"content": 0})
    ])
    def test_not_found(self, circuits_app, mcafee_epo_systems, mcafee_epo_tag, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = { 
            "mcafee_epo_systems": mcafee_epo_systems,
            "mcafee_epo_tag": mcafee_epo_tag
        }

        results = call_mcafee_epo_remove_tag_function(circuits_app, function_params)
        assert (results['content'] == expected_results['content'])

    # This live test requires an existing system as "test_server" and a tag "Resilient"
    @pytest.mark.livetest
    @pytest.mark.parametrize("mcafee_epo_systems, mcafee_epo_tag, expected_results", [
        (None, "Resilient", None),
        ("test_server", None, None)
    ])
    def test_failure(self, circuits_app, mcafee_epo_systems, mcafee_epo_tag, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = { 
            "mcafee_epo_systems": mcafee_epo_systems,
            "mcafee_epo_tag": mcafee_epo_tag
        }

        with pytest.raises(Exception): # should be ValueError
            call_mcafee_epo_remove_tag_function(circuits_app, function_params)


    @pytest.mark.livetest
    @pytest.mark.parametrize("mcafee_epo_systems, mcafee_epo_tag, expected_results", [
        ("test_server", "no_tag", None)
    ])
    def test_failure(self, circuits_app, mcafee_epo_systems, mcafee_epo_tag, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = { 
            "mcafee_epo_systems": mcafee_epo_systems,
            "mcafee_epo_tag": mcafee_epo_tag
        }

        with pytest.raises(Exception): # should be IntegrationError
            call_mcafee_epo_remove_tag_function(circuits_app, function_params)

