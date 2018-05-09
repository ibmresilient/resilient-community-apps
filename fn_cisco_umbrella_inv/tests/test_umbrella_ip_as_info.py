# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from mock import patch

from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from  mock_umbrella import  mocked_response

PACKAGE_NAME = "fn_cisco_umbrella_inv"
FUNCTION_NAME = "umbrella_ip_as_info"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"

def assert_keys_in(json_obj, *keys):
    for key in keys:
        assert key in json_obj

def call_umbrella_ip_as_info_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("umbrella_ip_as_info", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("umbrella_ip_as_info_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestUmbrellaIpAsInfo:
    """ Tests for the umbrella_ip_as_info function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @patch('investigate.Investigate.get', side_effect=mocked_response)
    @pytest.mark.parametrize("umbinv_ipaddr, umbinv_asn", [
        ("93.184.216.119", None)
    ])
    def test_umbrella_ip_as_info_ip(self, mock_get, circuits_app, umbinv_ipaddr, umbinv_asn):
        """ Test ip using mocked response. """
        keys = ["description", "cidr", "ir", "asn", "creation_date"]

        function_params = { 
            "umbinv_ipaddr": umbinv_ipaddr,
            "umbinv_asn": umbinv_asn
        }
        results = call_umbrella_ip_as_info_function(circuits_app, function_params)
        as_for_ip = results["as_for_ip"]
        for as_ip in as_for_ip:
            assert_keys_in(as_ip, *keys)

    @patch('investigate.Investigate.get', side_effect=mocked_response)
    @pytest.mark.parametrize("umbinv_ipaddr, umbinv_asn", [
        (None, 12345)
    ])

    def test_umbrella_ip_as_info(self, mock_get, circuits_app, umbinv_ipaddr, umbinv_asn):
        """ Test asn using mocked response. """
        keys = ["cidr", "geo"]

        function_params = {
            "umbinv_ipaddr": umbinv_ipaddr,
            "umbinv_asn": umbinv_asn
        }
        results = call_umbrella_ip_as_info_function(circuits_app, function_params)
        prefixes_for_asn = results["prefixes_for_asn"]
        for as_asn in prefixes_for_asn:
            assert_keys_in(as_asn, *keys)