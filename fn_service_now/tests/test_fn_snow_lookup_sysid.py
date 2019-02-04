# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from sn_test_helper import *

PACKAGE_NAME = "fn_service_now"
FUNCTION_NAME = "fn_snow_lookup_sysid"

# Get mock config data
config_data = get_mock_config_data()

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"

def call_fn_snow_lookup_sysid_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("fn_snow_lookup_sysid", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("fn_snow_lookup_sysid_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value

class TestFnSnowLookupSysid:
    """ Tests for the fn_snow_lookup_sysid function"""

    inputs = {
      "sn_table_name": "sys_user_group",
      "sn_query_field": "sys_user_group",
      "sn_query_value": "My Group"
    }

    output = {
      "inputs": inputs,
      "success": True,
      "sys_id": "19JHGF7686GFDf6789"
    }

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.parametrize("inputs, expected_results", [(inputs, output)])
    def test_success(self, circuits_app, inputs, expected_results):
        """ Test calling with sample values for the parameters """

        mock_response = MockedResponse(200, json.dumps({"result": {"sys_id": "19JHGF7686GFDf6789"}})) 

        ResilientHelper.sn_GET = MagicMock(return_value=mock_response)

        results = call_fn_snow_lookup_sysid_function(circuits_app, inputs)
        assert(expected_results == results)