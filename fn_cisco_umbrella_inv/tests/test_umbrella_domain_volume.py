# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from mock import patch

from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from  mock_umbrella import  mocked_response

PACKAGE_NAME = "fn_cisco_umbrella_inv"
FUNCTION_NAME = "umbrella_domain_volume"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"

def assert_keys_in(json_obj, *keys):
    for key in keys:
        assert key in json_obj

def call_umbrella_domain_volume_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("umbrella_domain_volume", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("umbrella_domain_volume_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestUmbrellaDomainVolume:
    """ Tests for the umbrella_domain_volume function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @patch('investigate.Investigate.get', side_effect=mocked_response)
    @pytest.mark.parametrize("umbinv_domain, umbinv_match, umbinv_start_epoch, umbinv_start_relative, umbinv_stop_epoch, umbinv_stop_relative", [
        ("cisco.com", 'all', None, "-1days", None, "now")
    ])
    def test_success(self, mock_get, circuits_app, umbinv_domain, umbinv_match, umbinv_start_epoch, umbinv_start_relative, umbinv_stop_epoch, umbinv_stop_relative):
        """ Test for umbrella_domain_volume using mocked data.  """

        keys = ["dates", "queries"]

        function_params = {
            "umbinv_domain": umbinv_domain,
            "umbinv_match": umbinv_match,
            "umbinv_start_epoch": umbinv_start_epoch,
            "umbinv_start_relative": umbinv_start_relative,
            "umbinv_stop_epoch": umbinv_stop_epoch,
            "umbinv_stop_relative": umbinv_stop_relative
        }
        results = call_umbrella_domain_volume_function(circuits_app, function_params)
        domain_volume = results["domain_volume"]
        assert_keys_in(domain_volume, *keys)