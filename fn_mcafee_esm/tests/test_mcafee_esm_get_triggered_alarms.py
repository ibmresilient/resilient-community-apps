# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from mock import patch
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from test_helper import get_test_config, generate_response
from fn_mcafee_esm.components.mcafee_esm_get_triggered_alarms import alarm_get_triggered_alarms
from fn_mcafee_esm.util.helper import check_config


PACKAGE_NAME = "fn_mcafee_esm"
FUNCTION_NAME = "mcafee_esm_get_list_of_cases"

# Read the default configuration-data section from the package
config_data = get_test_config()

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_mcafee_esm_get_list_of_cases_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("mcafee_esm_get_list_of_cases", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("mcafee_esm_get_list_of_cases_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestMcafeeEsmGetTriggeredAlarms:
    """ Tests for the mcafee_esm_get_list_of_cases function"""

    @patch("requests.post")
    def test_case_get_list_of_cases(self, mocked_requests_post):
        ops = check_config(config_data)
        content1 = {
            "status": "success"
        }
        content2 = [{
            "severity": 50,
            "summary": "Signature ID 'Failed User Logon' (306-31) match found",
            "assignee": "admin",
            "triggeredDate": "08/27/2018 18:47:14",
            "acknowledgedDate": "",
            "acknowledgedUsername": "",
            "alarmName": "Failed User Logon",
            "conditionType": 22,
            "id": 8195
        }]
        mocked_requests_post.side_effect = [generate_response(content1, 200),
                                            generate_response(content2, 200)]
        params = {
            "triggeredTimeRange": "CURRENT_DAY"
        }

        actual_response = alarm_get_triggered_alarms(ops, params)
        assert content2 == actual_response




    # def test_function_definition(self):
    #     """ Test that the package provides customization_data that defines the function """
    #     func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
    #     assert func is not None
    #
    # @pytest.mark.parametrize("expected_results", [
    #     ({"value": "xyz"}),
    #     ({"value": "xyz"})
    # ])
    # def test_success(self, circuits_app, expected_results):
    #     """ Test calling with sample values for the parameters """
    #     function_params = {
    #     }
    #     results = call_mcafee_esm_get_list_of_cases_function(circuits_app, function_params)
    #     assert(expected_results == results)
