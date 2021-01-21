# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
""" Test AWS GuardDuty refresh finding function. """
import pytest
from mock import patch, MagicMock
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from pytest_resilient_circuits.mocks import BasicResilientMock
from .mock_artifacts import *

PACKAGE_NAME = "fn_aws_guardduty"
FUNCTION_NAME = "func_aws_guardduty_refresh_finding"

# Read the default configuration-data section from the package
config_data = get_mock_config()

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"

def assert_keys_in(json_obj, *keys):
    for key in keys:
        assert key in json_obj

def call_func_aws_guardduty_refresh_finding_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("func_aws_guardduty_refresh_finding", function_params)

    # Add mock workflow_instance_id
    evt.kwargs.get("message").update({
        "workflow_instance": {
            "workflow_instance_id": 100
        }
    })

    # Fire a message to the function
    circuits.manager.fire(evt)

    # circuits will fire an "exception" event if an exception is raised in the FunctionComponent
    # return this exception if it is raised
    exception_event = circuits.watcher.wait("exception", parent=None, timeout=timeout)

    if exception_event is not False:
        exception = exception_event.args[1]
        raise exception

    # else return the FunctionComponent's results
    else:
        event = circuits.watcher.wait("func_aws_guardduty_refresh_finding_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value


class TestFuncAwsGuarddutyRefreshFinding:
    """ Tests for the func_aws_guardduty_refresh_finding function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    mock_inputs_1 = {
        "aws_gd_finding_id": "60baffd3f9042e38640f2300d5c5a630",
        "aws_gd_detector_id": "f2baedb0ac74f8f42fc929e15f56da6a",
        "aws_gd_region": "us-west-2",
        "incident_id":  1
    }

    expected_results_1_1 = {}
    expected_results_1_2 = get_mocked_results("refresh_finding_with_artifacts")

    mock_inputs_2 = {
        "aws_gd_finding_id": "60baffd3f9042e38640f2300d5c5a631",
        "aws_gd_detector_id": "f2baedb0ac74f8f42fc929e15f56da6a",
        "aws_gd_region": "us-west-2",
        "incident_id": 2
    }

    expected_results_2_1 = get_mocked_results("refresh_finding_to_json")
    expected_results_2_2 = get_mocked_results("refresh_finding_no_artifacts")

    @patch('fn_aws_guardduty.components.func_aws_guardduty_refresh_finding.ResSvc', side_effect=mocked_ResSvc)
    @patch('fn_aws_guardduty.components.func_aws_guardduty_refresh_finding.AwsGdClient', side_effect=mocked_gd_client)
    @pytest.mark.parametrize("mock_inputs, expected_results_1, expected_results_2", [
        (mock_inputs_1, expected_results_1_1, expected_results_1_2),
        (mock_inputs_2, expected_results_2_1, expected_results_2_2)
    ])
    def test_success(self, mock_cli, mock_res, circuits_app, mock_inputs, expected_results_1, expected_results_2):
        """ Test calling with sample values for the parameters """
        keys = ["content", "inputs", "metrics", "raw", "reason", "success", "version"]
        keys_content = ["finding", "payload", "data_tables"]
        keys_payload = ["name", "description", "discovered_date", "severity_code", "properties",
                        "artifacts", "comments"]

        results = call_func_aws_guardduty_refresh_finding_function(circuits_app, mock_inputs)
        assert_keys_in(results, *keys)
        assert results["content"] == expected_results_1
        content = results["content"]
        if content:
            assert_keys_in(content, *keys_content)
            assert_keys_in(content["payload"], *keys_payload)
            assert content["payload"]["artifacts"] ==  expected_results_2
