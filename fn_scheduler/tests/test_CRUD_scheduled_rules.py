# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import datetime
import logging
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from common import setup_mock_incident, setup_mock_actions, setup_evt
import sys
if sys.version_info.major == 3:
    from unittest.mock import Mock, patch
else:
    from mock import Mock, patch

PACKAGE_NAME = "fn_scheduler"
FUNCTION_NAME = "list_scheduled_rules"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"

def call_create_a_scheduled_rule_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("create_a_scheduled_rule", function_params)
    setup_evt(evt)

    circuits.manager.fire(evt)
    event = circuits.watcher.wait("create_a_scheduled_rule_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value

def call_list_scheduled_rules_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("list_scheduled_rules", function_params)
    setup_evt(evt)

    circuits.manager.fire(evt)
    event = circuits.watcher.wait("list_scheduled_rules_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value

def call_remove_a_scheduled_rule_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("remove_a_scheduled_rule", function_params)
    setup_evt(evt)

    circuits.manager.fire(evt)
    event = circuits.watcher.wait("remove_a_scheduled_rule_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value

def call_scheduled_rule_pause_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("scheduled_rule_pause", function_params)
    setup_evt(evt)

    circuits.manager.fire(evt)
    event = circuits.watcher.wait("scheduled_rule_pause_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value

def call_scheduled_rule_resume_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("scheduled_rule_resume", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("scheduled_rule_resume_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value

class TestListScheduledRules:
    """ Tests for the list_scheduled_rules function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    #@pytest.mark.skip
    @pytest.mark.parametrize("scheduler_type, scheduler_type_value, scheduler_rule_name, scheduler_rule_parameters, "
                             "scheduler_label_prefix, incident_id, object_id, row_id, expected_results", [
                                 ('cron', "* 2 * * *", "Test Rule", None, "CRUD", 123, None, None, {"value": "xyz"})
                             ])
    @patch('fn_scheduler.lib.resilient_helper.get_rules')
    @patch('fn_scheduler.components.create_a_scheduled_rule.get_incident')
    def test_success(self, mock_get_incident, mock_get_rules,
                     circuits_app, scheduler_type, scheduler_type_value,
                     scheduler_rule_name, scheduler_rule_parameters,
                     scheduler_label_prefix, incident_id, object_id, row_id, expected_results):
        """ Test calling with sample values for the parameters """
        setup_mock_incident(mock_get_incident)
        setup_mock_actions(mock_get_rules)

        now = datetime.datetime.now()
        yyyymmdd = now.strftime('%s')

        rule_label = "{}_{}".format(scheduler_label_prefix, yyyymmdd)

        function_params = {
            "scheduler_type": scheduler_type,
            "scheduler_type_value": scheduler_type_value,
            "scheduler_rule_name": scheduler_rule_name,
            "scheduler_rule_parameters": scheduler_rule_parameters,
            "scheduler_label_prefix": rule_label,
            "incident_id": incident_id,
            "object_id": object_id,
            "row_id": row_id
        }
        results = call_create_a_scheduled_rule_function(circuits_app, function_params)
        assert results['success']
        job_id = results['content']['id']

        # list
        job = self.check_job(circuits_app, incident_id, job_id)
        if not job:
            raise LookupError("missing scheduled rule")

        # pause
        function_params = {
            "scheduler_label_prefix": job_id
        }
        results = call_scheduled_rule_pause_function(circuits_app, function_params)
        assert results['success']

        job = self.check_job(circuits_app, incident_id, job_id, is_enabled=False)
        if not job:
            raise LookupError("missing scheduled rule")

        # resume
        results = call_scheduled_rule_resume_function(circuits_app, function_params)
        assert results['success']

        job = self.check_job(circuits_app, incident_id, job_id)
        if not job:
            raise LookupError("missing scheduled rule")

        # remove
        results = call_remove_a_scheduled_rule_function(circuits_app, function_params)
        assert results['success']

        job = self.check_job(circuits_app, incident_id, job_id)
        if job:
            raise LookupError("scheduled rule not removed")


    def check_job(self, circuits_app, incident_id, job_label, is_enabled=True):
        """
        get a list of jobs and ensure the job meets the is_enabled criteria
        :param circuits_app:
        :param job_label:
        :param is_enabled: True if active
        :return: job object or None
        """
        function_params = {
            "incident_id": incident_id
        }

        results = call_list_scheduled_rules_function(circuits_app, function_params)
        for job in results['content']:
            if job['id'].startswith(job_label):
                if is_enabled:
                    assert job['next_run_time']
                else:
                    assert not job['next_run_time']

                return job

        return None
