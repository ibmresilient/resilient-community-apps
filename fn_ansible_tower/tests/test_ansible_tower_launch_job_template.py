# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from mock import patch
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from . import helper

"""
pytest --resilient_app_config=/<path>/<to>/app.config tests/test_ansible_tower_launch_job_template.py
"""

PACKAGE_NAME = "fn-ansible-tower"
FUNCTION_NAME = "ansible_tower_launch_job_template"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_ansible_tower_launch_job_template_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("ansible_tower_launch_job_template", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("ansible_tower_launch_job_template_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestAnsibleTowerLaunchJobTemplate:
    """ Tests for the ansible_tower_launch_job_template function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @patch('fn_ansible_tower.components.ansible_tower_launch_job_template.RequestsCommon.execute_call_v2')
    @pytest.mark.parametrize("tower_template_id, tower_hosts, tower_template_name, tower_arguments, tower_run_tags, tower_skip_tags, expected_results", [
        (123, "text", "text", None, None, None, 'pending')
    ])
    def test_success(self, mock_post, circuits_app, tower_template_id, tower_hosts, tower_template_name, tower_arguments, tower_run_tags, tower_skip_tags, expected_results):
        """ Test calling with sample values for the parameters """
        mock_post.return_value = helper.MockedResponse(helper.mocked_launch_job_template())

        function_params = { 
            "tower_template_id": tower_template_id,
            "tower_hosts": tower_hosts,
            "tower_template_name": tower_template_name,
            "tower_arguments": tower_arguments,
            "tower_run_tags": tower_run_tags,
            "tower_skip_tags": tower_skip_tags
        }
        results = call_ansible_tower_launch_job_template_function(circuits_app, function_params)
        assert(expected_results == results['content']['status'])

    @pytest.mark.parametrize("tower_template_id, tower_hosts, tower_template_name, tower_arguments, tower_run_tags, tower_skip_tags, expected_results", [
        (None, "all", None, None, None, None, 'Specify either tower_template_id or tower_template_name')
    ])
    def test_failure(self, circuits_app, tower_template_id, tower_hosts, tower_template_name, tower_arguments, tower_run_tags, tower_skip_tags, expected_results):
        """ Test calling with sample values for the parameters """

        function_params = {
            "tower_template_id": tower_template_id,
            "tower_hosts": tower_hosts,
            "tower_template_name": tower_template_name,
            "tower_arguments": tower_arguments,
            "tower_run_tags": tower_run_tags,
            "tower_skip_tags": tower_skip_tags
        }
        with pytest.raises(Exception) as e:
            results = call_ansible_tower_launch_job_template_function(circuits_app, function_params)
