# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from mock import patch

from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from  mock_umbrella import  mocked_response

PACKAGE_NAME = "fn_cisco_umbrella_inv"
FUNCTION_NAME = "umbrella_threat_grid_samples"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"

def assert_keys_in(json_obj, *keys):
    for key in keys:
        assert key in json_obj

def call_umbrella_threat_grid_samples_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("umbrella_threat_grid_samples", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("umbrella_threat_grid_samples_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestUmbrellaThreatGridSamples:
    """ Tests for the umbrella_threat_grid_samples function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @patch('investigate.Investigate.get', side_effect=mocked_response)
    @pytest.mark.parametrize("umbinv_resource, umbinv_resource_type, umbinv_limit, umbinv_offset, umbinv_sortby", [
        ("cisco.com", "domain_name", 5, 0, "score")
    ])
    def test_umbrella_samples(self, mock_get, circuits_app, umbinv_resource, umbinv_resource_type, umbinv_limit, umbinv_offset, umbinv_sortby):
        """ Test umbrella_threat_grid_samples using mocked response. """

        keys = ["moreDataAvailable", "samples", "offset", "query" ]
        keys_s  = ["magicType", "sha1" , "size", "visible", "sha256", "avresults", "firstSeen"]

        function_params = {
            "umbinv_resource": umbinv_resource,
            "umbinv_resource_type": umbinv_resource_type,
            "umbinv_limit": umbinv_limit,
            "umbinv_offset": umbinv_offset,
            "umbinv_sortby": umbinv_sortby
        }
        results = call_umbrella_threat_grid_samples_function(circuits_app, function_params)
        thread_grid_samples = results["thread_grid_samples"]
        assert_keys_in(thread_grid_samples, *keys)
        samples = thread_grid_samples["samples"]
        for s in samples:
            assert_keys_in(s, *keys_s)