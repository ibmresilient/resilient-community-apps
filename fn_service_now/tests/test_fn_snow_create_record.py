# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from sn_test_helper import *
from copy import deepcopy

PACKAGE_NAME = "fn_service_now"
FUNCTION_NAME = "fn_snow_create_record"

# Get mock config data
config_data = get_mock_config_data()

# Use custom resilient_mock
resilient_mock = SNResilientMock

def call_fn_snow_create_record_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("fn_snow_create_record", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("fn_snow_create_record_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestFnSnowCreateRecord:
    """ Tests for the fn_snow_create_record function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        print (FUNCTION_NAME)
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    inputs1 = {
      "incident_id": 3003,
      "task_id": 4004,
      "sn_init_work_note": "We have fixed this",
      "sn_optional_fields": mock_pre_scrip_dict_to_json_str({
        "assignment_group": "IT Security"
      })
    }

    output1 = {
      "success": True,
      "reason": None,
      "inputs": deepcopy(inputs1),
      "row_id": 3,
      "res_id": "RES-3003-4004",
      "res_link": "https://example.com/#incidents/3003?task_id=4004",
      "sn_ref_id": "INC123459",
      "sn_sys_id": "12558dfsasd43a5sdf32df",
      "sn_record_state": "New",
      "sn_record_link": "https://test.service-now.com/nav_to.do?uri=incident.do?sysparm_query=number=INC123459"
    }
    output1["inputs"]["sn_optional_fields"] = json.loads(output1["inputs"]["sn_optional_fields"], object_hook=mock_byteify)

    @pytest.mark.parametrize("inputs, expected_results", [(inputs1, output1)])
    def test_success(self, circuits_app, inputs, expected_results, request):
        """ Test calling with sample values for the parameters """

        mock_post_response = {
          "res_id": expected_results["res_id"],
          "sn_ref_id": expected_results["sn_ref_id"],
          "sn_sys_id": "12558dfsasd43a5sdf32df",
          "sn_state": "New"
        }

        ResilientHelper.sn_api_request = MagicMock(return_value=mock_post_response)

        mock_add_row_response = {
          "id": 3
        }

        ServiceNowRecordsDataTable.add_row = MagicMock(return_value=mock_add_row_response)

        mock_rename_task = None

        ResilientHelper.rename_task = MagicMock(return_value=mock_rename_task)

        results = call_fn_snow_create_record_function(circuits_app, inputs)

        del results["sn_time_created"]
        results['res_link'] = 'https://example.com/#incidents/3003?task_id=4004'
        results["sn_record_link"] = "https://test.service-now.com/nav_to.do?uri=incident.do?sysparm_query=number=INC123459"
        for key in expected_results:
          assert(expected_results[key] == results[key])