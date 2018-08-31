# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from mock import patch
from resilient_circuits.util import get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from test_helper import get_test_config, generate_response, string_test_config
from fn_mcafee_esm.components.mcafee_esm_get_list_of_cases import case_get_case_list
from fn_mcafee_esm.util.helper import check_config


PACKAGE_NAME = "fn_mcafee_esm"
FUNCTION_NAME = "mcafee_esm_get_list_of_cases"

# Read test configuration-data
t_config_data = get_test_config()
config_data = string_test_config()

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


class TestMcafeeEsmGetListOfCases:
    """ Tests for the mcafee_esm_get_list_of_cases function"""

    @patch("requests.post")
    def test_case_get_list_of_cases(self, mocked_requests_post):
        ops = check_config(t_config_data)
        content1 = {
            "status": "success"
        }
        content2 = [{
            "severity": 2,
            "summary": "test3",
            "openTime": "08/09/2018 21:07:29",
            "id": 2,
            "statusId": {
                "value": 1
            }
        },  {
            "severity": 1,
            "summary": "test3",
            "openTime": "08/10/2018 19:18:43",
            "id": 3,
            "statusId": {
                "value": 1
            }
        }]
        mocked_requests_post.side_effect = [generate_response(content1, 200),
                                            generate_response(content2, 200)]

        actual_response = case_get_case_list(ops)
        assert content2 == actual_response




    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.parametrize("expected_results", [
        ({'case_list': [{'id': 2, 'openTime': '08/09/2018 21:07:29', 'statusId': {'value': 1}, 'severity': 2, 'summary': 'test3'}, {'id': 3, 'openTime': '08/10/2018 19:18:43', 'statusId': {'value': 1}, 'severity': 1, 'summary': 'test3'}]})
    ])
    @patch("requests.post")
    def test_success(self, mocked_requests_post, circuits_app, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = {
        }
        content1 = {
            "status": "success"
        }
        content2 = [{
            "severity": 2,
            "summary": "test3",
            "openTime": "08/09/2018 21:07:29",
            "id": 2,
            "statusId": {
                "value": 1
            }
        }, {
            "severity": 1,
            "summary": "test3",
            "openTime": "08/10/2018 19:18:43",
            "id": 3,
            "statusId": {
                "value": 1
            }
        }]
        mocked_requests_post.side_effect = [generate_response(content1, 200),
                                            generate_response(content2, 200)]

        results = call_mcafee_esm_get_list_of_cases_function(circuits_app, function_params)
        del results["metrics"]
        assert(expected_results == results)
