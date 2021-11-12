# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

import pytest
from mock import patch, MagicMock
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from .mock_artifacts import *

PACKAGE_NAME = "fn_extrahop"
FUNCTION_NAME = "funct_extrahop_rx_search_packets"

# Read the mock configuration-data section from the package
config_data = get_mock_config()

def assert_keys_in(json_obj, *keys):
    for key in keys:
        assert key in json_obj

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_funct_extrahop_rx_search_packets_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("funct_extrahop_rx_search_packets", function_params)

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
        event = circuits.watcher.wait("funct_extrahop_rx_search_packets_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value


class TestFunctExtrahopRxSearchPackets:
    """ Tests for the funct_extrahop_rx_search_packets function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    mock_inputs_1 = {
        "extrahop_bpf": "sample text",
        "extrahop_output": "zip",
        "extrahop_limit_bytes": "sample text",
        "extrahop_limit_search_duration": "sample text",
        "extrahop_active_until": 123,
        "extrahop_always_return_body": True,
        "extrahop_port1": "sample text",
        "extrahop_active_from": 123,
        "extrahop_port2": "sample text",
        "extrahop_ip1": "sample text",
        "extrahop_ip2": "sample text",
        "incident_id": 123
    }

    expected_results_1 = {"result": {"status": "No search matches found."}}

    mock_inputs_2 = {
        "extrahop_bpf": "sample text",
        "extrahop_output": "pcap",
        "extrahop_limit_bytes": "sample text",
        "extrahop_limit_search_duration": "sample text",
        "extrahop_active_until": 123,
        "extrahop_always_return_body": True,
        "extrahop_port1": "sample text",
        "extrahop_active_from": 123,
        "extrahop_port2": "sample text",
        "extrahop_ip1": "sample text",
        "extrahop_ip2": "sample text",
        "incident_id": 123
    }

    expected_results_2 = {"result": {"attachment": "example.pcap"}}

    mock_inputs_3 = {
        "extrahop_bpf": "sample text",
        "extrahop_output": "keylog_txt",
        "extrahop_limit_bytes": "sample text",
        "extrahop_limit_search_duration": "sample text",
        "extrahop_active_until": 123,
        "extrahop_always_return_body": True,
        "extrahop_port1": "sample text",
        "extrahop_active_from": 123,
        "extrahop_port2": "sample text",
        "extrahop_ip1": "sample text",
        "extrahop_ip2": "sample text",
        "incident_id": 123
    }

    expected_results_3 = {"result": {"error": "Missing response header"}}

    @patch('fn_extrahop.components.funct_extrahop_rx_search_packets.RxClient', side_effect=mocked_rx_client)
    @patch('fn_extrahop.components.funct_extrahop_rx_search_packets.write_file_attachment', side_effect=MagicMock)
    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (mock_inputs_1, expected_results_1),
        (mock_inputs_2, expected_results_2),
        (mock_inputs_3, expected_results_3)
    ])
    def test_success(self, mock_cli, mock_wfa, circuits_app, mock_inputs, expected_results):
        """ Test calling with sample values for the parameters """
        keys = ["content", "inputs", "metrics", "raw", "reason", "success", "version"]
        results = call_funct_extrahop_rx_search_packets_function(circuits_app, mock_inputs)
        assert_keys_in(results, *keys)
        assert(expected_results == results["content"])

