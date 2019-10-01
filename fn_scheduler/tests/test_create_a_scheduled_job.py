# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_scheduler"
FUNCTION_NAME = "create_a_scheduled_job"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_create_a_scheduled_job_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("create_a_scheduled_job", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("create_a_scheduled_job_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestCreateAScheduledJob:
    """ Tests for the create_a_scheduled_job function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.parametrize("scheduler_type, scheduler_type_value, scheduler_rule_name, scheduler_rule_parameters, scheduler_label, incident_id, object_id, row_id, expected_results", [
        ('interval', "text", "text", "text", "text", 123, 123, 123, {"value": "xyz"}),
        ('interval', "text", "text", "text", "text", 123, 123, 123, {"value": "xyz"})
    ])
    def test_success(self, circuits_app, scheduler_type, scheduler_type_value, scheduler_rule_name, scheduler_rule_parameters, scheduler_label, incident_id, object_id, row_id, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = { 
            "scheduler_type": scheduler_type,
            "scheduler_type_value": scheduler_type_value,
            "scheduler_rule_name": scheduler_rule_name,
            "scheduler_rule_parameters": scheduler_rule_parameters,
            "scheduler_label": scheduler_label,
            "incident_id": incident_id,
            "object_id": object_id,
            "row_id": row_id
        }
        results = call_create_a_scheduled_job_function(circuits_app, function_params)
        assert(expected_results == results)