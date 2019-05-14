# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
import logging

log = logging.getLogger(__name__)


PACKAGE_NAME = "fn_falcon_sandbox"
FUNCTION_NAME = "falcon_sandbox_submit_url"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_falcon_sandbox_submit_url_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("falcon_sandbox_submit_url", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("falcon_sandbox_submit_url_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value

INPUT_OUTPUT = (
    'Windows 7 64 bit', 'Default analysis', 2120, 341, 
    'http://malware.wicar.org/data/ms14_064_ole_xp.html',
    {
        "job_id": "5cd9dff1038838e10f0c7c8a", 
        "environment_id": 120, 
        "environment_description": "Windows 7 64 bit", 
        "state": "SUCCESS"
    }
)

class TestFalconSandboxSubmitUrl:
    """ Tests for the falcon_sandbox_submit_url function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.parametrize("falcon_sandbox_environment, falcon_sandbox_action_script, falcon_sandbox_incident_id, falcon_sandbox_artifact_id, falcon_sandbox_url, expected_results", [
        INPUT_OUTPUT
    ])
    def test_success(self, circuits_app, falcon_sandbox_environment, falcon_sandbox_action_script, falcon_sandbox_incident_id, falcon_sandbox_artifact_id, falcon_sandbox_url, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = { 
            "falcon_sandbox_environment": falcon_sandbox_environment,
            "falcon_sandbox_action_script": falcon_sandbox_action_script,
            "falcon_sandbox_incident_id": falcon_sandbox_incident_id,
            "falcon_sandbox_artifact_id": falcon_sandbox_artifact_id,
            "falcon_sandbox_url": falcon_sandbox_url
        }

        results = call_falcon_sandbox_submit_url_function(circuits_app, function_params)
        assert(expected_results['environment_id'] == results['environment_id'])
        assert(results['job_id'] is not None)
        assert(results['state'] in ["ERROR", "SUCCESS"])