# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from fn_datatable_utils.util.helper import PACKAGE_NAME
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from tests.test_helper import DTResilientMock

FUNCTION_NAME = "dt_utils_clear_datatable_content"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the SOAR REST API (uncomment to connect to a real appliance)
resilient_mock = DTResilientMock

def call_dt_utils_clear_datatable_content_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction(FUNCTION_NAME, function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait(
        "dt_utils_clear_datatable_content_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value

class TestDtUtilsClearDatatable:
    """ Tests for the dt_utils_clear_datatable_content function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func

    mock_inputs_1 = {
        "dt_utils_datatable_api_name": "mock_data_table",
        "incident_id": 1001
    }

    @pytest.mark.parametrize("mock_inputs", [(mock_inputs_1)])
    def test_success(self, circuits_app, mock_inputs):
        """ Test calling with sample values for the parameters """

        results = call_dt_utils_clear_datatable_content_function(circuits_app, mock_inputs)
        assert results['success']
