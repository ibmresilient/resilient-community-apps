# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
"""Test fn_bigfix_artifact function"""
from __future__ import print_function
import pytest
from mock import patch
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from mock_artifacts import mocked_bigfix_client

"""
Suite of tests to test fn_bigfix_artifact Resilient Function
"""

PACKAGE_NAME = "fn_bigfix"
FUNCTION_NAME = "fn_bigfix_artifact"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"

def assert_keys_in(json_obj, *keys):
    for key in keys:
        assert key in json_obj

def call_fn_bigfix_artifact_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("fn_bigfix_artifact", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("fn_bigfix_artifact_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestFnBigfixArtifact:
    """ Tests for the fn_bigfix_artifact function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @patch('fn_bigfix.components.fn_bigfix_artifact.BigFixClient', side_effect=mocked_bigfix_client)
    @pytest.mark.parametrize("bigfix_artifact_id, bigfix_artifact_value, bigfix_artifact_type, bigfix_incident_id, "
                             "bigfix_incident_plan_status, bigfix_artifact_properties_name, "
                             "bigfix_artifact_properties_value, expected_results", [
        (2, "10.0.2.15", "IP Address", 2095, "A", None, None, 2),
        (2, "/tmp/testfile.txt", "File Path", 2095, "A", None, None, 2),
        (2, "HKLM\\SOFTWARE\\JP\\JP2\\com.jp.browsercore", "Registry Key", 2095, "A", "MYKEY", "MYValue", 2),
        (2, "besclient", "Process Name", 2095, "A", None, None, 2),
        (2, "lfsvc", "Service", 2095, "A", None, None, 2),
    ])
    def test_success(self, mock_get, circuits_app, bigfix_artifact_id, bigfix_artifact_value, bigfix_artifact_type,
                     bigfix_incident_id, bigfix_incident_plan_status, bigfix_artifact_properties_name,
                     bigfix_artifact_properties_value, expected_results):
        """ Tests for fn_bigfix_artifact using mocked data.  """

        keys = ["hits_count", "endpoint_hits", "query_execution_date"]

        function_params = { 
            "bigfix_artifact_id": bigfix_artifact_id,
            "bigfix_artifact_value": bigfix_artifact_value,
            "bigfix_artifact_type": bigfix_artifact_type,
            "bigfix_incident_id": bigfix_incident_id,
            "bigfix_incident_plan_status": bigfix_incident_plan_status,
            "bigfix_artifact_properties_name": bigfix_artifact_properties_name,
            "bigfix_artifact_properties_value": bigfix_artifact_properties_value
        }
        results = call_fn_bigfix_artifact_function(circuits_app, function_params)
        assert_keys_in(results, *keys)
        assert(expected_results == len(results["endpoint_hits"]))