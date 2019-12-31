# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from mock import patch
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from . import helper

"""
pytest --resilient_app_config=/<path>/<to>/app.config tests/test_ansible_tower_list_job_templates.py
"""

PACKAGE_NAME = "fn-ansible-tower"
FUNCTION_NAME = "ansible_tower_list_job_templates"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_ansible_tower_list_job_templates_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("ansible_tower_list_job_templates", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("ansible_tower_list_job_templates_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestAnsibleTowerListJobTemplates:
    """ Tests for the ansible_tower_list_job_templates function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None


    @patch('fn_ansible_tower.lib.common.RequestsCommon.execute_call_v2')
    @pytest.mark.parametrize("tower_project, expected_results", [
        (None, 2),
        ("Demo Project", 1),
        ("2nd Project", 1),
        ("not found", 0)
    ])
    def test_filter(self, mock_get, circuits_app, tower_project, expected_results):
        """ Test calling with sample values for the parameters """
        mock_get.return_value = helper.MockedResponse(helper.mocked_get_job_template_by_project())

        function_params = {
            "tower_project": tower_project
        }
        results = call_ansible_tower_list_job_templates_function(circuits_app, function_params)
        assert(len(results['content']) == expected_results)
