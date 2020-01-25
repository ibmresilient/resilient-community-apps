# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from mock import patch
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from fn_ansible_tower.components.ansible_tower_list_jobs import convert_job_search_time
from . import helper

"""
pytest --resilient_app_config=/<path>/<to>/app.config tests/test_ansible_tower_list_jobs.py
"""

PACKAGE_NAME = "fn_ansible_tower"
FUNCTION_NAME = "ansible_tower_list_jobs"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_ansible_tower_list_jobs_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("ansible_tower_list_jobs", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("ansible_tower_list_jobs_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestAnsibleTowerListJobs:
    """ Tests for the ansible_tower_list_jobs function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @patch('fn_ansible_tower.components.ansible_tower_list_jobs.RequestsCommon.execute_call_v2')
    @pytest.mark.parametrize("tower_job_status, tower_last_updated, expected_results", [
        (None, None, 3),
        ('successful', None, 2),
        ('pending', None, 1),
        ('failed', None, 0),
        (None, "1000 weeks", 3)
    ])
    def test_success(self, mock_get, circuits_app, tower_job_status, tower_last_updated, expected_results):
        """ Test calling with sample values for the parameters """
        mock_get.return_value = helper.MockedResponse(helper.mocked_get_paged_jobs())

        function_params = { 
            "tower_job_status": tower_job_status,
            "tower_last_updated": tower_last_updated
        }
        results = call_ansible_tower_list_jobs_function(circuits_app, function_params)
        assert(len(results['content']) == expected_results)

    @pytest.mark.parametrize("tower_last_updated", [
        ('today'),
        ('Today'),
        ('10 minute'),
        (' 10  minute '),
        ('100 hours'),
        ('1 day'),
        ('2 days'),
        ('1 weeks')
    ])
    def test_convert_job_search_time_success(self, tower_last_updated):
        result = convert_job_search_time(tower_last_updated)

    @pytest.mark.parametrize("tower_last_updated", [
        ('10 today'),
        ('0 minute'),
        ('-2 hours'),
        ('1day'),
        ('2 unknown'),
        ('x weeks')
    ])
    def test_convert_job_search_time_failure(self, tower_last_updated):
        with pytest.raises(ValueError):
            result = convert_job_search_time(tower_last_updated)
