# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from mock import patch

from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from  mock_umbrella import  mocked_response

PACKAGE_NAME = "fn_cisco_umbrella_inv"
FUNCTION_NAME = "umbrella_threat_grid_sample"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"

def assert_keys_in(json_obj, *keys):
    for key in keys:
        assert key in json_obj

def call_umbrella_threat_grid_sample_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("umbrella_threat_grid_sample", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("umbrella_threat_grid_sample_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestUmbrellaThreatGridSample:
    """ Tests for the umbrella_threat_grid_sample function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @patch('investigate.Investigate.get', side_effect=mocked_response)
    @pytest.mark.parametrize("umbinv_hash, umbinv_sample_endpoint, umbinv_limit, umbinv_offset", [
        ("414e38ed0b5d507734361c2ba94f734252ca33b8259ca32334f32c4dba69b01c", "basic", 2, 0)
    ])
    def test_umbrella_sample_basic(self, mock_get, circuits_app, umbinv_hash, umbinv_sample_endpoint, umbinv_limit, umbinv_offset):
        """ Test umbrella_threat_grid_sample: basic using mocked response. """

        keys = ["magicType", "sha1", "md5", "size", "threatScore", "firstSeen", "lastSeen", "behaviors", "connections", "samples"]

        function_params = { 
            "umbinv_hash": umbinv_hash,
            "umbinv_sample_endpoint": umbinv_sample_endpoint,
            "umbinv_limit": umbinv_limit,
            "umbinv_offset": umbinv_offset
        }
        results = call_umbrella_threat_grid_sample_function(circuits_app, function_params)
        sample_basic = results["sample_basic"]
        assert_keys_in(sample_basic, *keys)

    @patch('investigate.Investigate.get', side_effect=mocked_response)
    @pytest.mark.parametrize("umbinv_hash, umbinv_sample_endpoint, umbinv_limit, umbinv_offset", [
        ("414e38ed0b5d507734361c2ba94f734252ca33b8259ca32334f32c4dba69b01c", "samples", 2, 0)
    ])
    def test_umbrella_sample_samples(self, mock_get, circuits_app, umbinv_hash, umbinv_sample_endpoint, umbinv_limit, umbinv_offset):
        """ Test umbrella_threat_grid_sample: samples using mocked response. """

        keys = ["totalResults", "limit", "moreDataAvailable", "samples", "offset"]
        keys_s = [ "magicType", "behaviors", "direction", "sha1", "size", "threatScore", "visible" , "firstSeen", "sha256",
                   "avresults", "lastSeen", "md5"]
        function_params = {
            "umbinv_hash": umbinv_hash,
            "umbinv_sample_endpoint": umbinv_sample_endpoint,
            "umbinv_limit": umbinv_limit,
            "umbinv_offset": umbinv_offset
        }
        results = call_umbrella_threat_grid_sample_function(circuits_app, function_params)
        sample_samples = results["sample_samples"]
        assert_keys_in(sample_samples, *keys)
        samples = sample_samples["samples"]
        for s in samples:
            assert_keys_in(s, *keys_s)

    @patch('investigate.Investigate.get', side_effect=mocked_response)
    @pytest.mark.parametrize("umbinv_hash, umbinv_sample_endpoint, umbinv_limit, umbinv_offset", [
        ("414e38ed0b5d507734361c2ba94f734252ca33b8259ca32334f32c4dba69b01c", "behaviors", 2, 0)
    ])
    def test_umbrella_sample_behaviors(self, mock_get, circuits_app, umbinv_hash, umbinv_sample_endpoint, umbinv_limit, umbinv_offset):
        """ Test umbrella_threat_grid_sample: behaviors using mocked response. """

        keys = ["category", "hits", "severity", "title", "tags", "confidence", "threat", "name"]

        function_params = {
            "umbinv_hash": umbinv_hash,
            "umbinv_sample_endpoint": umbinv_sample_endpoint,
            "umbinv_limit": umbinv_limit,
            "umbinv_offset": umbinv_offset
        }
        results = call_umbrella_threat_grid_sample_function(circuits_app, function_params)
        sample_behaviors = results["sample_behaviors"]
        for sb in sample_behaviors:
            assert_keys_in(sb, *keys)

    @patch('investigate.Investigate.get', side_effect=mocked_response)
    @pytest.mark.parametrize("umbinv_hash, umbinv_sample_endpoint, umbinv_limit, umbinv_offset", [
        ("414e38ed0b5d507734361c2ba94f734252ca33b8259ca32334f32c4dba69b01c", "connections", 2, 0)
    ])
    def test_umbrella_sample_connections(self, mock_get, circuits_app, umbinv_hash, umbinv_sample_endpoint, umbinv_limit, umbinv_offset):
        """ Test umbrella_threat_grid_sample: connections using mocked response. """

        keys = ["connections", "totalResults", "limit", "moreDataAvailable", "offset"]
        keys_c = ["popularity1Month", "name", "attacks", "popularity3Month", "popularity", "securityCategories",
                  "ips", "lastCommit", "urls", "type", "firstSeen", "lastSeen"]
        function_params = {
            "umbinv_hash": umbinv_hash,
            "umbinv_sample_endpoint": umbinv_sample_endpoint,
            "umbinv_limit": umbinv_limit,
            "umbinv_offset": umbinv_offset
        }
        results = call_umbrella_threat_grid_sample_function(circuits_app, function_params)
        sample_connections = results["sample_connections"]
        assert_keys_in(sample_connections, *keys)
        connections = sample_connections["connections"]
        for sc in connections:
            assert_keys_in(sc, *keys_c)
