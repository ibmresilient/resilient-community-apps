# (c) Copyright IBM Corp. 2019. All Rights Reserved.
# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from test_helper import *

PACKAGE_NAME = "fn_datatable_utils"
FUNCTION_NAME = "dt_utils_delete_row"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = DTResilientMock


def call_dt_utils_delete_row_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("dt_utils_delete_row", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("dt_utils_delete_row_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestDtUtilsDeleteRow:
    """ Tests for the dt_utils_delete_row function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    inputs = {
        "incident_id": 1001,
        "dt_utils_datatable_api_name": "mock_data_table",
        "dt_utils_row_id": 1
    }

    output = {
        "success": True,
        "inputs": inputs,
        "row": {'hints': [], 'message': None, 'success': True, 'title': None}
    }

    @pytest.mark.parametrize("inputs, expected_results", [(inputs, output)])
    def test_success(self, circuits_app, inputs, expected_results):
        """ Test calling with sample values for the parameters """

        results = call_dt_utils_delete_row_function(circuits_app, inputs)
        assert(expected_results == results)
