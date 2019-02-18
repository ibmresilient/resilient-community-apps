# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_crowdstrike_falcon"
FUNCTION_NAME = "fn_cs_falcon_get_devices_ioc_ran_on"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_fn_cs_falcon_get_devices_ioc_ran_on_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("fn_cs_falcon_get_devices_ioc_ran_on", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("fn_cs_falcon_get_devices_ioc_ran_on_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestFnCsFalconGetDevicesIocRanOn:
    """ Tests for the fn_cs_falcon_get_devices_ioc_ran_on function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.parametrize("cs_ioc_type, cs_ioc_value, cs_return_limit, expected_results", [
        ("text", "text", 123, {"value": "xyz"}),
        ("text", "text", 123, {"value": "xyz"})
    ])
    def test_success(self, circuits_app, cs_ioc_type, cs_ioc_value, cs_return_limit, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = { 
            "cs_ioc_type": cs_ioc_type,
            "cs_ioc_value": cs_ioc_value,
            "cs_return_limit": cs_return_limit
        }
        results = call_fn_cs_falcon_get_devices_ioc_ran_on_function(circuits_app, function_params)
        assert(expected_results == results)