# -*- coding: utf-8 -*-
# Generated with resilient-sdk v51.0.2.2.1096
"""Tests using pytest_resilient_circuits"""

import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from tests import test_helper
from unittest.mock import patch

PACKAGE_NAME = "fn_algosec"
FUNCTION_NAME = "algosec_traffic_simulation_query"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_algosec_traffic_simulation_query_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("algosec_traffic_simulation_query", function_params)

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
        event = circuits.watcher.wait("algosec_traffic_simulation_query_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value


class TestAlgosecTrafficSimulationQuery:
    """ Tests for the algosec_traffic_simulation_query function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    mock_inputs_1 = {
        "algosec_service": "any",
        "algosec_destination": "8.8.8.8",
        "algosec_source": "1.2.3.5"
    }

    expected_results_1 = {
        "queryUIResult": "https://aglosec/fa/query/results/#/work/ALL_FIREWALLS_query-1722608134438/",
        "queryResult": [
            {
                "queryDescription": "1.2.3.5=>8.8.8.8:any:any:any",
                "fipResult": "Unreachable",
                "finalResult": "Not routed",
                "queryHTMLPath": "https://local.algosec.com/fa/query/results/#/work/ALL_FIREWALLS_query-1722608134438/"
            }
        ]
    }

    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (mock_inputs_1, expected_results_1)
    ])
    def test_success(self, circuits_app, mock_inputs, expected_results):
        """ Test calling with sample values for the parameters """
        with patch("fn_algosec.components.funct_algosec_traffic_simulation_query.algosec_client") as patch_client:
            with patch("fn_algosec.components.funct_algosec_traffic_simulation_query.firewall_analyzer") as patch_firewall:
                patch_client.return_value = test_helper.mock_init_client()
                patch_firewall.return_value = test_helper.mock_firewall_analyzer()
                results = call_algosec_traffic_simulation_query_function(circuits_app, mock_inputs)
                assert(expected_results == results.get("content", {}))
