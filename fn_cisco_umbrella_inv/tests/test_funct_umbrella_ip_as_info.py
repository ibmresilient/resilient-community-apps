# -*- coding: utf-8 -*-
# Generated with resilient-sdk v51.0.2.2.1096
"""Tests using pytest_resilient_circuits"""

import pytest, mock_umbrella
from unittest.mock import patch
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

FUNCTION_NAME = "umbrella_ip_as_info"

# Read the default configuration-data section from the package
config_data = get_config_data(mock_umbrella.PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_umbrella_ip_as_info_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("umbrella_ip_as_info", function_params)

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
        event = circuits.watcher.wait("umbrella_ip_as_info_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value


class TestUmbrellaIpAsInfo:
    """ Tests for the umbrella_ip_as_info function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(mock_umbrella.PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    mock_inputs_1 = {
        "umbinv_resource": "1.2.3.4"
    }

    expected_results_1 = mock_umbrella.bgp_routes_ip_return
    
    mock_inputs_2 = {
        "umbinv_resource": 1234
    }
    
    expected_results_2 = mock_umbrella.bgp_routes_asn_return

    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (mock_inputs_1, expected_results_1)
    ])
    def test_success(self, circuits_app, mock_inputs, expected_results):
        """ Test calling with sample values for the parameters """
        with patch("fn_cisco_umbrella_inv.components.umbrella_ip_as_info.investigateClient") as patch_client:
            patch_client.return_value = mock_umbrella.mock_client()
            results = call_umbrella_ip_as_info_function(circuits_app, mock_inputs)
            if results.get("content", {}).get("as_for_ip"):
                assert(expected_results == results.get("content", {}).get("as_for_ip"))
            else:
                assert(expected_results == results.get("content", {}).get("prefixes_for_asn"))
