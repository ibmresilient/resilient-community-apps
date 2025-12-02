# -*- coding: utf-8 -*-
# Generated with resilient-sdk v51.0.5.0.1475
"""Tests using pytest_resilient_circuits"""

import pytest
from resilient_circuits.util import get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from helper import PACKAGE_NAME, get_mock_config_data, create_event, create_event_return
from mock import patch

FUNCTION_NAME = "on_call_manager_create_event"

# Read the default configuration-data section from the package
config_data = get_mock_config_data()

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"

def call_on_call_manager_create_event_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("on_call_manager_create_event", function_params)

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
        event = circuits.watcher.wait("on_call_manager_create_event_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value

class TestOnCallManagerCreateEvent:
    """ Tests for the on_call_manager_create_event function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    mock_inputs_1 = {
        "ocm_resource_correlationkey": "sample text",
        "ocm_type_eventtype": "sample text",
        "ocm_type_statusorthreshold": "sample text",
        "ocm_resource_displayname": "sample text",
        "ocm_resource_interface": "sample text",
        "ocm_resource_accessscope": "sample text",
        "ocm_event_severity": "Critical",
        "ocm_event_expirytime": 123,
        "ocm_resource_location": "sample text",
        "ocm_resource_port": "sample text",
        "ocm_event_resolution": True,
        "ocm_resource_type": "Application",
        "ocm_event_summary": "sample text",
        "ocm_event_priority": "5",
        "ocm_resource_controller": "sample text",
        "ocm_resource_cluster": "sample text",
        "ocm_soar_inc_id": 123,
        "ocm_resource_service": "sample text",
        "ocm_resource_sourceid": "sample text",
        "ocm_resource_application": "sample text",
        "ocm_deduplicationkey": "sample text",
        "ocm_resource_ipaddress": "sample text",
        "ocm_resource_name": "sample text",
        "ocm_event_details": "sample text",
        "ocm_resource_hostname": "sample text",
        "ocm_resource_component": "sample text"
    }

    expected_results_1 = create_event_return()

    @patch('fn_ocm.util.helper.ocm_client.create_event', create_event)
    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (mock_inputs_1, expected_results_1)
    ])
    def test_success(self, circuits_app, mock_inputs, expected_results):
        """ Test calling with sample values for the parameters """

        results = call_on_call_manager_create_event_function(circuits_app, mock_inputs)
        assert(expected_results == results.get("content", {}))
