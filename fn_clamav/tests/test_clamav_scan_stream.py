# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from mock import patch
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from mock_artifacts import mocked_pyclamd_client, mocked_res_client

PACKAGE_NAME = "fn_clamav"
FUNCTION_NAME = "clamav_scan_stream"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_clamav_scan_stream_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("clamav_scan_stream", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("clamav_scan_stream_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestClamavScanStream:
    """ Tests for the clamav_scan_stream function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @patch('fn_clamav.components.clamav_scan_stream.pyclamd.ClamdNetworkSocket', side_effect=mocked_pyclamd_client)
    @patch('resilient_circuits.actions_component.ResilientComponent.rest_client', side_effect=mocked_res_client)
    @pytest.mark.parametrize("incident_id, artifact_id, attachment_id, task_id, expected_results_1, expected_results_2", [
        (2095, None, 25, None, "incident_eicar.txt", {u'stream': [u'FOUND', u'Eicar-Test-Signature']}),
        (2095, 10, None, None, "artifact_eicar.txt", {u'stream': [u'FOUND', u'Eicar-Test-Signature']}),
        (2095, None, 25, 2251251, "task_eicar.txt", {u'stream': [u'FOUND', u'Eicar-Test-Signature']})
    ])
    def test_success(self, mock_get_1, mock_get_2, circuits_app, incident_id, artifact_id, attachment_id, task_id,
                     expected_results_1, expected_results_2):
        """ Test calling with sample values for the parameters """
        function_params = { 
            "incident_id": incident_id,
            "artifact_id": artifact_id,
            "attachment_id": attachment_id,
            "task_id": task_id
        }
        results = call_clamav_scan_stream_function(circuits_app, function_params)
        assert (expected_results_1 == results["file_name"])
        assert(expected_results_2 == results["response"])
