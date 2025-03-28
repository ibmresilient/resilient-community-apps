# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from sn_test_helper import PACKAGE_NAME

FUNCTION_NAME = "fn_snow_update_record"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_fn_snow_update_record_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("fn_snow_update_record", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("fn_snow_update_record_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestFnSnowUpdateRecord:
    """ Tests for the fn_snow_update_record function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.parametrize("incident_id, task_id, sn_res_id, sn_update_fields, expected_results", [
        (123, 123, "text", "text", {"value": "xyz"}),
        (123, 123, "text", "text", {"value": "xyz"})
    ])
    def test_success(self, circuits_app, incident_id, task_id, sn_res_id, sn_update_fields, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = { 
            "incident_id": incident_id,
            "task_id": task_id,
            "sn_res_id": sn_res_id,
            "sn_update_fields": sn_update_fields
        }
        results = call_fn_snow_update_record_function(circuits_app, function_params)
        assert(expected_results == results)