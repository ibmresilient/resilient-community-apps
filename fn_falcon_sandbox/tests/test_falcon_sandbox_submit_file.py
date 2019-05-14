# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_falcon_sandbox"
FUNCTION_NAME = "falcon_sandbox_submit_file"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_falcon_sandbox_submit_file_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("falcon_sandbox_submit_file", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("falcon_sandbox_submit_file_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestFalconSandboxSubmitFile:
    """ Tests for the falcon_sandbox_submit_file function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.parametrize("falcon_sandbox_environment, falcon_sandbox_action_script, falcon_sandbox_no_share_third_party, falcon_sandbox_allow_community_access, falcon_sandbox_comment, falcon_sandbox_priority, falcon_sandbox_environment_variable, falcon_sandbox_custom_run_time, falcon_sandbox_submit_name, falcon_sandbox_custom_date_time, falcon_sandbox_document_password, falcon_sandbox_tor_enabled_analysis, falcon_sandbox_incident_id, falcon_sandbox_task_id, falcon_sandbox_attachment_id, falcon_sandbox_artifact_id, expected_results", [
        ('Windows 7 32 bit', 'Open Internet Explorer', True, True, "text", 123, "text", "text", "text", "text", "text", True, 123, 123, 123, 123, {"value": "xyz"}),
        ('Linux (Ubuntu 16.04, 64 bit)', 'Random desktop files', True, True, "text", 123, "text", "text", "text", "text", "text", True, 123, 123, 123, 123, {"value": "xyz"})
    ])
    def test_success(self, circuits_app, falcon_sandbox_environment, falcon_sandbox_action_script, falcon_sandbox_no_share_third_party, falcon_sandbox_allow_community_access, falcon_sandbox_comment, falcon_sandbox_priority, falcon_sandbox_environment_variable, falcon_sandbox_custom_run_time, falcon_sandbox_submit_name, falcon_sandbox_custom_date_time, falcon_sandbox_document_password, falcon_sandbox_tor_enabled_analysis, falcon_sandbox_incident_id, falcon_sandbox_task_id, falcon_sandbox_attachment_id, falcon_sandbox_artifact_id, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = { 
            "falcon_sandbox_environment": falcon_sandbox_environment,
            "falcon_sandbox_action_script": falcon_sandbox_action_script,
            "falcon_sandbox_no_share_third_party": falcon_sandbox_no_share_third_party,
            "falcon_sandbox_allow_community_access": falcon_sandbox_allow_community_access,
            "falcon_sandbox_comment": falcon_sandbox_comment,
            "falcon_sandbox_priority": falcon_sandbox_priority,
            "falcon_sandbox_environment_variable": falcon_sandbox_environment_variable,
            "falcon_sandbox_custom_run_time": falcon_sandbox_custom_run_time,
            "falcon_sandbox_submit_name": falcon_sandbox_submit_name,
            "falcon_sandbox_custom_date_time": falcon_sandbox_custom_date_time,
            "falcon_sandbox_document_password": falcon_sandbox_document_password,
            "falcon_sandbox_tor_enabled_analysis": falcon_sandbox_tor_enabled_analysis,
            "falcon_sandbox_incident_id": falcon_sandbox_incident_id,
            "falcon_sandbox_task_id": falcon_sandbox_task_id,
            "falcon_sandbox_attachment_id": falcon_sandbox_attachment_id,
            "falcon_sandbox_artifact_id": falcon_sandbox_artifact_id
        }
        results = call_falcon_sandbox_submit_file_function(circuits_app, function_params)
        assert(expected_results == results)