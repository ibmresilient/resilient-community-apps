# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
""" Test AWS GuardDuty refresh finding function. """
import pytest
from mock import patch
from sys import version_info
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from .mock_artifacts import *

PACKAGE_NAME = "fn_aws_guardduty"
FUNCTION_NAME = "func_aws_guardduty_refresh_finding"

# Read the mockconfiguration-data section from the package
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

    time_stamp = "2021-01-22 15:35:48"
    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    # Test Case where finding id not found.
    mock_inputs_1 = {
        "aws_gd_finding_id": "60baffd3f9042e38640f2300d5c5a630",
        "aws_gd_detector_id": "f2baedb0ac74f8f42fc929e15f56da6a",
        "aws_gd_region": "us-west-2",
        "incident_id":  1
    }

    expected_results_1_1 = {}
    expected_results_1_2 = get_mocked_results("refresh_finding_with_artifacts")

    # Test Case where finding id exists.
    mock_inputs_2 = {
        "aws_gd_finding_id": "60baffd3f9042e38640f2300d5c5a631",
        "aws_gd_detector_id": "f2baedb0ac74f8f42fc929e15f56da6a",
        "aws_gd_region": "us-west-2",
        "incident_id": 2
    }

    expected_results_2_1 = get_mocked_results("refresh_finding_to_json")
    if version_info.major == 2:
        expected_results_2_2 = get_mocked_results("refresh_finding_no_artifacts_py2")
    else:
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
        keys_content = ["finding", "payload", "data_tables", "timestamp", "region"]
        keys_incident_properties = ["name", "description", "discovered_date", "severity_code"]
        keys_payload = keys_incident_properties + ["artifacts", "comments"]
        keys_data_tables = ["gd_finding_overview", "gd_s3_bucket_details", "gd_access_key_details",
                           "gd_instance_details", "gd_resource_affected", "gd_action_details"]

        results = call_func_aws_guardduty_refresh_finding_function(circuits_app, mock_inputs)
        assert_keys_in(results, *keys)
        assert sorted(results["content"]) == sorted(expected_results_1)
        content = results["content"]
        if content:
            assert_keys_in(content, *keys_content)
            payload = content["payload"]
            data_tables = content["data_tables"]
            for k in keys_incident_properties:
                assert payload[k] == expected_results_2[k]
            assert_keys_in(payload, *keys_payload)
            assert_keys_in(data_tables, *keys_data_tables )
            assert sorted(payload) == sorted(expected_results_2)
            assert payload["properties"] == expected_results_2["properties"]
            assert len(payload["artifacts"]) == len(expected_results_2["artifacts"])