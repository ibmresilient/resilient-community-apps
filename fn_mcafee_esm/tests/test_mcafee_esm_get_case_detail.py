# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from mock import patch
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from test_helper import get_test_config, generate_response
from fn_mcafee_esm.components.mcafee_esm_get_case_detail import case_get_case_detail
from fn_mcafee_esm.util.helper import check_config

PACKAGE_NAME = "fn_mcafee_esm"
FUNCTION_NAME = "mcafee_esm_get_case_detail"

# Read the default configuration-data section from the package
config_data = get_test_config()

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_mcafee_esm_get_case_detail_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("mcafee_esm_get_case_detail", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("mcafee_esm_get_case_detail_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestMcafeeEsmGetCaseDetail:
    """ Tests for the mcafee_esm_get_case_detail function"""

    @patch("requests.post")
    def test_case_edit_case_details(self, mocked_requests_post):
        ops = check_config(config_data)
        content = {
            "dataSourceList": None,
            "assignedTo": 1,
            "orgId": 1,
            "closeTime": "08/22/2018 21:27:34",
            "eventList": [],
            "deviceList": None,
            "notes": [{
                "changes": [],
                "content": "",
                "username": "admin",
                "action": "Open",
                "timestamp": "08/22/2018 21:27:34(GMT)"
            }],
            "noteAdded": "",
            "history": [{
                "changes": [],
                "content": "",
                "username": "admin",
                "action": "Viewed",
                "timestamp": "08/22/2018 21:28:24(GMT)"
            }],
            "severity": 1,
            "summary": "test5",
            "openTime": "08/22/2018 21:27:34",
            "id": 8194,
            "statusId": {
                "value": 1
            }
        }
        mocked_requests_post.return_value = generate_response(content, 200)
        case = case_get_case_detail(ops, {}, 1)

        assert content == case


    # def test_function_definition(self):
    #     """ Test that the package provides customization_data that defines the function """
    #     func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
    #     assert func is not None
    #
    # @pytest.mark.parametrize("mcafee_case_id, expected_results", [
    #     (123, {"value": "xyz"}),
    #     (123, {"value": "xyz"})
    # ])
    # def test_success(self, circuits_app, mcafee_case_id, expected_results):
    #     """ Test calling with sample values for the parameters """
    #     function_params = {
    #         "mcafee_case_id": mcafee_case_id
    #     }
    #     results = call_mcafee_esm_get_case_detail_function(circuits_app, function_params)
    #     assert(expected_results == results)
