# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from mock import patch
from fn_qradar_integration.util.qradar_constants import PACKAGE_NAME

FUNCTION_NAME = "qradar_reference_table_delete_item"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"

MOCK_DELETE_RESPONSE = {
  "time_to_live": "999 years 0 mons 0 days 0 hours 0 mins 0.00 secs",
  "timeout_type": "LAST_SEEN",
  "number_of_elements": 555,
  "creation_time": 1570221529014,
  "name": "demo_v3",
  "namespace": "SHARED",
  "element_type": "ALN",
  "collection_id": 86
}

MOCK_DELETE_RESPONSE_UNICODE = {
  "time_to_live": "999 years 0 mons 0 days 0 hours 0 mins 0.00 secs",
  "timeout_type": "LAST_SEEN",
  "number_of_elements": 555,
  "creation_time": 1570221529014,
  "name": "演示版vz",
  "namespace": "SHARED",
  "element_type": "ALN",
  "collection_id": 86
}

def call_qradar_reference_table_delete_item_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("qradar_reference_table_delete_item", function_params)

    # Fire a message to the function
    circuits.manager.fire(evt)

    # circuits will fire an "exception" event if an exception is raised in the FunctionComponent
    # return this exception if it is raised
    exception_event = circuits.watcher.wait("exception", parent=None, timeout=timeout)

    if exception_event is not False:
        exception = exception_event.args[1]
        raise exception

    # else return the FunctionComponent's results
    else:
        event = circuits.watcher.wait("qradar_reference_table_delete_item_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value

class TestQradarReferenceTableDeleteItem:
    """ Tests for the qradar_reference_table_delete_item function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    mock_inputs_1 = {
        "qradar_reference_table_name": "sample text",
        "qradar_reference_table_item_value": "sample text",
        "qradar_label": "SOAR_Plugin_Destination_Name1"
    }

    expected_results_1 = MOCK_DELETE_RESPONSE

    mock_inputs_2 = {
        "qradar_reference_table_name": "sample text",
        "qradar_reference_table_item_value": "sample text",
        "qradar_label": "SOAR_Plugin_Destination_Name2"
    }

    expected_results_2 = MOCK_DELETE_RESPONSE_UNICODE

    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (mock_inputs_1, expected_results_1),
        (mock_inputs_2, expected_results_2)
    ])
    def test_success(self, circuits_app, mock_inputs, expected_results):
        """ Test calling with sample values for the parameters """

        with patch('fn_qradar_integration.lib.reference_data.ReferenceTableFacade.ReferenceTableFacade.delete_ref_element') as patched_add_element:
            patched_add_element.return_value = expected_results
            results = call_qradar_reference_table_delete_item_function(circuits_app, mock_inputs)
            assert(expected_results == results['content'])
