# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from sn_test_helper import *
from copy import deepcopy

PACKAGE_NAME = "fn_service_now"
FUNCTION_NAME = "sn_utilities_close_in_servicenow"

# Get mock config data
config_data = get_mock_config_data()

# Use custom resilient_mock
resilient_mock = SNResilientMock

def call_sn_utilities_close_in_servicenow_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("sn_utilities_close_in_servicenow", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("sn_utilities_close_in_servicenow_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value

class TestSnUtilitiesCloseInServicenow:
    """ Tests for the sn_utilities_close_in_servicenow function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    inputs1 = {
      "incident_id": 1001,
      "task_id": 2002,
      "sn_record_state": 7,
      "sn_close_notes": "We have fixed this",
      "sn_close_code": "Solved (Permanently)"
    }

    output1 = {
      "inputs": deepcopy(inputs1),
      "success": True,
      "sn_ref_id": "INC123456"
    }

    inputs2 = {
      "incident_id": 1001,
      "task_id": None,
      "sn_record_state": 7,
      "sn_close_notes": "We have fixed this",
      "sn_close_code": "Solved (Permanently)"
    }

    output2 = {
      "inputs": deepcopy(inputs2),
      "success": True,
      "sn_ref_id": "INC123457"
    }

    @pytest.mark.parametrize("inputs, expected_results", [(inputs1, output1), (inputs2, output2)])
    def test_success(self, circuits_app, inputs, expected_results):
        """ Test calling with sample values for the parameters """

        mock_response = {"sn_ref_id": "INC123456", "sn_state": "Closed"}

        ResilientHelper.sn_POST = MagicMock(return_value=mock_response)

        results = call_sn_utilities_close_in_servicenow_function(circuits_app, inputs)
        assert(expected_results == results)