# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from sn_test_helper import *
from copy import deepcopy


PACKAGE_NAME = "fn_service_now"
FUNCTION_NAME = "fn_snow_helper_update_datatable"

# Read the default configuration-data section from the package
config_data = get_mock_config_data()

# Use custom resilient_mock
resilient_mock = SNResilientMock


def call_fn_snow_helper_update_datatable_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("fn_snow_helper_update_datatable", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("fn_snow_helper_update_datatable_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestFnSnowHelperUpdateDatatable:
    """ Tests for the fn_snow_helper_update_datatable function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    inputs1 = {
        "incident_id": 1001,
        "task_id": 2002,
        "sn_resilient_status": "A"
    }

    output1 = {
        'inputs': deepcopy(inputs1),
        'row_id': 1,
        'res_id': 'RES-1001-2002',
        'success': True
    }

    @pytest.mark.parametrize("inputs, expected_results", [(inputs1, output1)])
    def test_success(self, circuits_app, inputs, expected_results):
        """ Test calling with sample values for the parameters """

        results = call_fn_snow_helper_update_datatable_function(circuits_app, inputs)
        assert(expected_results == results)