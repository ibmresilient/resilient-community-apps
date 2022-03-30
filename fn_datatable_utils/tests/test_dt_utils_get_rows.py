# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from tests.test_helper import *

PACKAGE_NAME = "fn_datatable_utils"
FUNCTION_NAME = "dt_utils_get_rows"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the SOAR REST API (uncomment to connect to a real appliance)
resilient_mock = DTResilientMock

def call_dt_utils_get_rows_function(circuits, function_params, timeout=10):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("dt_utils_get_rows", function_params)

    # Fire a message to the function
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("dt_utils_get_rows_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value

class TestDtUtilsGetRows:
    """ Tests for the dt_utils_get_rows function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    inputs = {
        'incident_id': 1001,
        'dt_utils_datatable_api_name': 'mock_data_table',
        'dt_utils_sort_by': 'dt_col_status',
        'dt_utils_sort_direction': {'name': 'ASC'},
        'dt_utils_max_rows': 1,
        'dt_utils_search_column': 'dt_col_name',
        'dt_utils_search_value': 'Mary Blogs'
    }

    get_all_rows_inputs = {
        'incident_id': 1001,
        'dt_utils_datatable_api_name': 'mock_data_table',
        'dt_utils_sort_by': 'dt_col_status',
        'dt_utils_sort_direction': {'name': 'ASC'}
    }

    output = {
      'inputs': {
        'dt_utils_datatable_api_name': 'mock_data_table',
        'dt_utils_sort_by': 'dt_col_status',
        'dt_utils_search_column': 'dt_col_name',
        'dt_utils_sort_direction': 'ASC',
        'dt_utils_max_rows': 1,
        'incident_id': 1001,
        'dt_utils_search_value': 'Mary Blogs'
      },
      'success': True,
      'rows': [
        {
          u'id': 3,
          u'cells': {
            u'dt_col_name': {
              u'id': u'dt_col_name',
              u'value': u'Mary Blogs',
              u'row_id': 3
            },
            u'dt_col_email': {
              u'id': u'dt_col_email',
              u'value': u'mary@example.com',
              u'row_id': 3
            },
            u'dt_col_status': {
              u'id': u'dt_col_status',
              u'value': u'Active',
              u'row_id': 3
            },
            u'dt_col_id': {
              u'id': u'dt_col_id',
              u'value': 3003,
              u'row_id': 3
            }
          }
        }
      ]
    }

    get_all_rows_output = {
      'success': True,
      'inputs': {
        'incident_id': 1001,
        'dt_utils_datatable_api_name': 'mock_data_table',
        'dt_utils_sort_by': 'dt_col_status',
        'dt_utils_sort_direction': 'ASC',
        'dt_utils_max_rows': None,
        'dt_utils_search_column': None,
        'dt_utils_search_value': None
      },
      'rows': [
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
        },
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
        }
      ]
    }

    @pytest.mark.parametrize("mock_inputs, expected_results", [
      (inputs, output),
      (get_all_rows_inputs, get_all_rows_output)
    ])
    def test_success(self, circuits_app, mock_inputs, expected_results):
        """ Test calling with sample values for the parameters """

        results = call_dt_utils_get_rows_function(circuits_app, mock_inputs)
        assert (expected_results == results)
