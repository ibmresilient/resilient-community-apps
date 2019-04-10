# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from sn_test_helper import *
from copy import deepcopy

PACKAGE_NAME = "fn_service_now"
FUNCTION_NAME = "fn_snow_close_record"

# Get mock config data
config_data = get_mock_config_data()

# Use custom resilient_mock
resilient_mock = SNResilientMock

def call_fn_snow_close_record_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("fn_snow_close_record", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("fn_snow_close_record_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value

class TestFnSnowCloseRecord:
    """ Tests for the fn_snow_close_record function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    inputs1 = {
      "incident_id": 1001,
      "task_id": 2002,
      "sn_res_id": None,
      "sn_record_state": 7,
      "sn_close_notes": "We have fixed this",
      "sn_close_code": "Solved (Permanently)",
      "sn_close_work_note": "This was fixed by IBM Resilient team"
    }

    output1 = {
      "inputs": deepcopy(inputs1),
      "success": True,
      "reason": None,
      "sn_ref_id": "INC123456",
      "sn_record_state": "Closed"
    }

    inputs2 = {
      "incident_id": 1001,
      "task_id": None,
      "sn_res_id": None,
      "sn_record_state": 7,
      "sn_close_notes": "We have fixed this",
      "sn_close_code": "Solved (Permanently)",
      "sn_close_work_note": "This was fixed by IBM Resilient team"
    }

    output2 = {
      "inputs": deepcopy(inputs2),
      "success": True,
      "reason": None,
      "sn_ref_id": "INC123457",
      "sn_record_state": "Closed"
    }

    inputs3 = {
      "incident_id": 1001,
      "task_id": None,
      "sn_res_id": "RES-1001-2002",
      "sn_record_state": 7,
      "sn_close_notes": "We have fixed this",
      "sn_close_code": "Solved (Permanently)",
      "sn_close_work_note": "This was fixed by IBM Resilient team"
    }

    output3 = {
      "inputs": deepcopy(inputs3),
      "success": True,
      "reason": None,
      "sn_ref_id": "INC123457",
      "sn_record_state": "Closed"
    }

    @pytest.mark.parametrize("inputs, expected_results", [(inputs1, output1), (inputs2, output2)])
    def test_success(self, circuits_app, inputs, expected_results):
        """ Test calling with sample values for the parameters """

        mock_response = {"sn_ref_id": "INC123456", "sn_state": "Closed"}

        ResilientHelper.sn_api_request = MagicMock(return_value=mock_response)

        results = call_fn_snow_close_record_function(circuits_app, inputs)
        assert(expected_results == results)