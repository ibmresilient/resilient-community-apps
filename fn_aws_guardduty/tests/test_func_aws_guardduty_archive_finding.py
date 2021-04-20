# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
""" Test AWS GuardDuty archive finding function. """
import pytest
from mock import patch
from sys import version_info
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from .mock_artifacts import *

PACKAGE_NAME = "fn_aws_guardduty"
FUNCTION_NAME = "func_aws_guardduty_archive_finding"

# Read the mock configuration-data section from the package
config_data = get_mock_config()

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"

def assert_keys_in(json_obj, *keys):
    for key in keys:
        assert key in json_obj

def call_func_aws_guardduty_archive_finding_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("func_aws_guardduty_archive_finding", function_params)

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
        event = circuits.watcher.wait("func_aws_guardduty_archive_finding_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value


class TestFuncAwsGuarddutyArchiveFinding:
    """ Tests for the func_aws_guardduty_archive_finding function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    mock_inputs_1 = {
        "aws_gd_region": "us-east-2",
        "aws_gd_finding_id": "c2bb95a17b879bffc96c58f8a1689785",
        "aws_gd_detector_id": "32b7017d2019dfe922abc4e07c3fdded"
    }

    expected_results_1 = {'status': 'ok'}

    mock_inputs_2 = {
        "aws_gd_region": "us-east-2",
        "aws_gd_finding_id": "c2bb95a17b879bffc96c58f8a1689785",
        "aws_gd_detector_id": "32b7017d2019dfe922abc4e07c3fdfff"
    }

    expected_results_2 = {'status': 'error', 'msg': 'An error occurred (BadRequestException) when calling the '
                                                    'ArchiveFindings operation: The request is rejected because '
                                                    'the input detectorId is not owned by the current account.'}

    @patch('fn_aws_guardduty.components.func_aws_guardduty_archive_finding.AwsGdClient', side_effect=mocked_gd_client)
    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (mock_inputs_1, expected_results_1),
        (mock_inputs_2, expected_results_2)
    ])
    def test_success(self, mock_cli, circuits_app, mock_inputs, expected_results):
        """ Test calling with sample values for the parameters """

        keys = ["content", "inputs", "metrics", "raw", "reason", "success", "version"]

        results = call_func_aws_guardduty_archive_finding_function(circuits_app, mock_inputs)
        assert_keys_in(results, *keys)
        content = results["content"]
        assert content == expected_results