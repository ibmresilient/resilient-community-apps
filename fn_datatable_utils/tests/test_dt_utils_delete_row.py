# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from fn_datatable_utils.util.helper import PACKAGE_NAME
from tests.test_helper import DTResilientMock
from resilient_circuits import SubmitTestFunction, FunctionResult
from resilient_circuits.util import get_config_data, get_function_definition

FUNCTION_NAME = "dt_utils_delete_row"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the SOAR REST API (uncomment to connect to a real appliance)
resilient_mock = DTResilientMock

def call_dt_utils_delete_row_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction(FUNCTION_NAME, function_params)

    # Fire a message to the function
    circuits.manager.fire(evt)

    # circuits will fire an "exception" event if an exception is raised in the FunctionComponent
    # return this exception if it is raised
    exception_event = circuits.watcher.wait("exception", parent=None, timeout=timeout)

    if exception_event:
        exception = exception_event.args[1]
        raise exception

    # else return the FunctionComponent's results
    else:
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
        assert func

    inputs = {
        "incident_id": 1001,
        "dt_utils_datatable_api_name": "mock_data_table",
        "dt_utils_row_id": 1
    }

    output = {
        'hints': [], 'message': None, 'success': True, 'title': None
    }

    @pytest.mark.parametrize("inputs, expected_results", [(inputs, output)])
    def test_success(self, circuits_app, inputs, expected_results):
        """ Test calling with sample values for the parameters """

        results = call_dt_utils_delete_row_function(circuits_app, inputs)
        assert(expected_results == results["content"]["row"])
