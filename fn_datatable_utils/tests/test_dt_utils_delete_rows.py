# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from fn_datatable_utils.util.helper import PACKAGE_NAME
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from tests.test_helper import DTResilientMock

FUNCTION_NAME = "dt_utils_delete_rows"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the SOAR REST API (uncomment to connect to a real appliance)
resilient_mock = DTResilientMock

def call_dt_utils_delete_rows_function(circuits, function_params, timeout=10):
    # Create the submitTestFunction event
    evt = SubmitTestFunction(FUNCTION_NAME, function_params)

    # Fire a message to the function
    circuits.manager.fire(evt)
    event = circuits.watcher.wait(
        "dt_utils_delete_rows_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value

class TestDtUtilsDeleteRows:
    """ Tests for the dt_utils_delete_rows function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func

    inputs = {
        'incident_id': 1001,
        'dt_utils_datatable_api_name': 'mock_data_table',
        'dt_utils_rows_ids': '[1,2]',
        'dt_utils_search_column': None,
        'dt_utils_search_value': None
    }

    delete_all_inputs = {
        'incident_id': 1001,
        'dt_utils_datatable_api_name': 'mock_data_table',
        'dt_utils_delete_all_rows': True
    }

    delete_all_output = [1, 2, 3]

    output = [1, 2]

    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (inputs, output),
        (delete_all_inputs, delete_all_output)
    ])
    def test_success(self, circuits_app, mock_inputs, expected_results):
        """ Test calling with sample values for the parameters """

        results = call_dt_utils_delete_rows_function(circuits_app, mock_inputs)
        assert (expected_results == results["content"]["rows_ids"])
