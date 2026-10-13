# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2025. All Rights Reserved.
# Generated with resilient-sdk v51.0.6.0.1543
"""Tests AWS GuardDuty delete threatintelset function."""

import pytest
from mock import patch
from resilient_circuits.util import get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from .mock_artifacts import *
from .test_helpers import assert_keys_in

FUNCTION_NAME = "aws_guardduty_delete_threatintelset"

# Read the default configuration-data section from the package
config_data = get_mock_config()

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"

def call_aws_guardduty_delete_threatintelset_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("aws_guardduty_delete_threatintelset", function_params)

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
        event = circuits.watcher.wait("aws_guardduty_delete_threatintelset_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value


class TestAwsGuarddutyDeleteThreatintelset:
    """ Tests for the aws_guardduty_delete_threatintelset function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    mock_inputs_1 = {
        "aws_gd_threat_intel_set_id": "4face156778d48a3a06663dd461187ce",
        "aws_gd_detector_id": "32b7017d2019dfe922abc4e07c3fdfff",
        "aws_gd_region": "us-east-1"
    }

    expected_results_1 = {"ResponseMetadata": {}, "status": "ok"}

    @pytest.mark.livetest
    @patch('fn_aws_guardduty.components.funct_aws_guardduty_delete_threatintelset.AwsGdClient', side_effect=mocked_gd_client)
    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (mock_inputs_1, expected_results_1)
    ])
    def test_success(self, circuits_app, mock_inputs, expected_results):
        """ Test calling with sample values for the parameters """

        keys = ["content", "inputs", "metrics", "raw", "reason", "success", "version"]
        results = call_aws_guardduty_delete_threatintelset_function(circuits_app, mock_inputs)
        assert_keys_in(results, *keys)
        content = results["content"]
        assert content == expected_results
