# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
"""Test fn_bigfix_remediation function"""
from __future__ import print_function
import pytest
from mock import patch
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from  mock_artifacts import mocked_bigfix_client

"""
Suite of tests to test fn_bigfix_remediation Resilient Function
"""

PACKAGE_NAME = "fn_bigfix"
FUNCTION_NAME = "fn_bigfix_remediation"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"

def assert_keys_in(json_obj, *keys):
    for key in keys:
        assert key in json_obj

def call_fn_bigfix_remediation_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("fn_bigfix_remediation", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("fn_bigfix_remediation_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value

class TestFnBigfixRemediation:
    """ Tests for the fn_bigfix_remediation function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @patch('fn_bigfix.components.fn_bigfix_remediation.BigFixClient', side_effect=mocked_bigfix_client)
    @pytest.mark.parametrize("bigfix_asset_id, bigfix_artifact_value, bigfix_artifact_type, bigfix_incident_id, expected_results", [
        (12315195, "/tmp/testfile.txt", "File Path", 2095, 127),
        (12315196, "besclient", "Process Name", 2095, 128),
        (12315197, "lfsvc", "Service", 2095, 129),
        (12315198, "HKLM\\SOFTWARE\\JP\\JP2\\com.jp.browsercore", "Registry Key", 2095, 130),
    ])
    def test_success(self, mock_get, circuits_app, bigfix_asset_id, bigfix_artifact_value, bigfix_artifact_type, bigfix_incident_id, expected_results):
        """ Tests for fn_bigfix_remediation using mocked data.  """

        keys = ["status", "remediation_date", "status_message", "action_id"]

        function_params = {
            "bigfix_asset_id": bigfix_asset_id,
            "bigfix_artifact_value": bigfix_artifact_value,
            "bigfix_artifact_type": bigfix_artifact_type,
            "bigfix_incident_id": bigfix_incident_id
        }
        results = call_fn_bigfix_remediation_function(circuits_app, function_params)
        assert_keys_in(results, *keys)
        assert(expected_results == results["action_id"])

