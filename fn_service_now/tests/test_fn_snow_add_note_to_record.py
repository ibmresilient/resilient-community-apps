# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from sn_test_helper import *
from copy import deepcopy

PACKAGE_NAME = "fn_service_now"
FUNCTION_NAME = "fn_snow_add_note_to_record"

# Get mock config data
config_data = get_mock_config_data()

# Use custom resilient_mock
resilient_mock = SNResilientMock

def call_fn_snow_add_note_to_record_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("fn_snow_add_note_to_record", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("fn_snow_add_note_to_record_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value

class TestFnSnowAddNoteToRecord:
    """ Tests for the fn_snow_add_note_to_record function"""

    inputs1 = {
      "incident_id": 1001,
      "task_id": 2002,
      "sn_note_text": "This is a test note",
      "sn_note_type": {"name": "work_note"}
    }

    output1 = {
      "inputs": deepcopy(inputs1),
      "success": True,
      "res_id": "RES-1001-2002",
      "sn_ref_id": "INC0010459"
    }
    output1["inputs"]["sn_note_type"] = output1["inputs"]["sn_note_type"]["name"]

    inputs2 = {
      "incident_id": 1001,
      "task_id": None,
      "sn_note_text": "This is a test note",
      "sn_note_type": {"name": "additional_comment"}
    }

    output2 = {
      "inputs": deepcopy(inputs2),
      "success": True,
      "res_id": "RES-1001",
      "sn_ref_id": "INC0010459"
    }
    output2["inputs"]["sn_note_type"] = output2["inputs"]["sn_note_type"]["name"]

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.parametrize("inputs, expected_results", [(inputs1, output1), (inputs2, output2)])
    def test_success(self, circuits_app, inputs, expected_results):
        """ Test calling with sample values for the parameters """

        mock_response = {"sn_ref_id": "INC0010459"}

        ResilientHelper.sn_POST = MagicMock(return_value=mock_response)

        results = call_fn_snow_add_note_to_record_function(circuits_app, inputs)
        assert(expected_results == results)