# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from fn_datatable_utils.util.helper import PACKAGE_NAME
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from tests.test_helper import DTResilientMock

FUNCTION_NAME = "dt_utils_get_all_data_table_rows"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the SOAR REST API (uncomment to connect to a real appliance)
resilient_mock = DTResilientMock

def call_dt_utils_get_all_data_table_rows_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction(FUNCTION_NAME, function_params)

    # Fire a message to the function
    circuits.manager.fire(evt)

    # circuits will fire an "exception" event if an exception is raised in the FunctionComponent
    # return this exception if it is raised
    exception_event = circuits.watcher.wait(
        "exception", parent=None, timeout=timeout)

    if exception_event:
        exception = exception_event.args[1]
        raise exception

    # else return the FunctionComponent's results
    else:
        event = circuits.watcher.wait(
            "dt_utils_get_all_data_table_rows_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value


class TestDtUtilsGetAllDataTableRows:
    """ Tests for the dt_utils_get_all_data_table_rows function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func

    mock_inputs_1 = {
        "dt_utils_datatable_api_name": "mock_data_table",
        "incident_id": 1001
    }

    expected_results_1 = [
            {
                'id': 1,
                'cells': {
                    'dt_col_id': {
                        'row_id': 1,
                        'id': 'dt_col_id',
                        'value': 3001
                    },
                    'dt_col_name': {
                        'row_id': 1,
                        'id': 'dt_col_name',
                        'value': 'Joe Blogs'
                    },
                    'dt_col_email': {
                        'row_id': 1,
                        'id': 'dt_col_email',
                        'value': 'joe@example.com'
                    },
                    'dt_col_status': {
                        'row_id': 1,
                        'id': 'dt_col_status',
                        'value': 'In Progress'
                    }
                }
            },
            {
                'id': 2,
                'cells': {
                    'dt_col_id': {
                        'row_id': 2,
                        'id': 'dt_col_id',
                        'value': 3002
                    },
                    'dt_col_name': {
                        'row_id': 2,
                        'id': 'dt_col_name',
                        'value': 'Mary Blogs'
                    },
                    'dt_col_email': {
                        'row_id': 2,
                        'id': 'dt_col_email',
                        'value': 'mary@example.com'
                    },
                    'dt_col_status': {
                        'row_id': 2,
                        'id': 'dt_col_status',
                        'value': 'In Progress'
                    }
                }
            },
            {
                'id': 3,
                'cells': {
                    'dt_col_id': {
                        'row_id': 3,
                        'id': 'dt_col_id',
                        'value': 3003
                    },
                    'dt_col_name': {
                        'row_id': 3,
                        'id': 'dt_col_name',
                        'value': 'Mary Blogs'
                    },
                    'dt_col_email': {
                        'row_id': 3,
                        'id': 'dt_col_email',
                        'value': 'mary@example.com'
                    },
                    'dt_col_status': {
                        'row_id': 3,
                        'id': 'dt_col_status',
                        'value': 'Active'
                    }
                }
            }
        ]

    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (mock_inputs_1, expected_results_1)
    ])
    def test_success(self, circuits_app, mock_inputs, expected_results):
        """ Test calling with sample values for the parameters """

        results = call_dt_utils_get_all_data_table_rows_function(
            circuits_app, mock_inputs)
        assert(expected_results == results["content"]["rows"])
