# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from fn_qradar_integration.util.qradar_constants import PACKAGE_NAME
from mock import patch

FUNCTION_NAME = "qradar_get_all_reference_tables"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"

MOCK_GET_TABLE_RESPONSE = [
  {
    "timeout_type": "LAST_SEEN",
    "number_of_elements": 0,
    "creation_time": 1464119414213,
    "name": "Mock URLs Data",
    "namespace": "SHARED",
    "key_name_types": {
      "Brand": "ALNIC",
      "First Seen Date": "DATE",
      "Identifier": "NUM",
      "Confidence": "NUM",
      "Last Seen Date": "DATE",
      "Report URL": "ALNIC",
      "Malware Family": "ALNIC",
      "Portal URL": "ALNIC",
      "Infrastructure Type": "ALNIC",
      "Provider": "ALN"
    },
    "element_type": "ALNIC",
    "collection_id": 181
  },
  {
    "timeout_type": "LAST_SEEN",
    "number_of_elements": 100,
    "creation_time": 1464119421471,
    "name": "Les faux logiciels malveillants hachent les données SHA",
    "namespace": "SHARED",
    "key_name_types": {
      "Brand": "ALNIC",
      "First Seen Date": "DATE",
      "Identifier": "NUM",
      "Confidence": "NUM",
      "Last Seen Date": "DATE",
      "Portal URL": "ALNIC",
      "Malware Family": "ALNIC",
      "Report URL": "ALNIC",
      "Infrastructure Type": "ALNIC",
      "Provider": "ALN"
    },
    "element_type": "ALNIC",
    "collection_id": 190
  }]

def call_qradar_get_all_reference_tables_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("qradar_get_all_reference_tables", function_params)

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
        event = circuits.watcher.wait("qradar_get_all_reference_tables_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value

class TestQradarGetAllReferenceTables:
    """ Tests for the qradar_get_all_reference_tables function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    mock_inputs_1 = {"qradar_label": "SOAR_Plugin_Destination_Name1"
    }

    expected_results_1 = MOCK_GET_TABLE_RESPONSE

    mock_inputs_2 = {"qradar_label": "SOAR_Plugin_Destination_Name2"
    }

    expected_results_2 = MOCK_GET_TABLE_RESPONSE

    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (mock_inputs_1, expected_results_1),
        (mock_inputs_2, expected_results_2)
    ])
    @pytest.mark.livetest
    def test_live_success(self, circuits_app, mock_inputs, expected_results):
        """ Test calling with sample values for the parameters """

        results = call_qradar_get_all_reference_tables_function(circuits_app, mock_inputs)
        assert results
        assert results['content'] # Ensure we have some results
        for entry in results['content']:
            assert entry.get('collection_id', False)
            assert entry.get('name', False)
            assert isinstance(entry.get('number_of_elements', False), int)
    
    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (mock_inputs_1, expected_results_1),
        (mock_inputs_2, expected_results_2)
    ])
    def test_mocked_success(self, circuits_app, mock_inputs, expected_results):
        """ Test calling with sample values for the parameters """

        with patch('fn_qradar_integration.lib.reference_data.ReferenceTableFacade.ReferenceTableFacade.get_all_reference_tables') as patched_add_element:
            patched_add_element.return_value = expected_results
            results = call_qradar_get_all_reference_tables_function(circuits_app, mock_inputs)
            assert results
            assert results['content'] # Ensure we have some results
            for entry in results['content']:
                assert entry.get('collection_id', False)
                assert entry.get('name', False)
                assert isinstance(entry.get('number_of_elements', False), int)
