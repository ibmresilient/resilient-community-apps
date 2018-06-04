# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from fn_utilities.components.utilities_excel_query import WorksheetData
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_utilities"
FUNCTION_NAME = "utilities_excel_query"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_utilities_excel_query_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("utilities_excel_query", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("utilities_excel_query_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestUtilitiesExcelQuery:
    """ Tests for the utilities_excel_query function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.parametrize("attachment_id, excel_ranges, excel_defined_names, incident_id, task_id, expected_results", [
        (123, "text", "text", 123, 123, {"value": "xyz"}),
        (123, "text", "text", 123, 123, {"value": "xyz"})
    ])
    def test_success(self, circuits_app, attachment_id, excel_ranges, excel_defined_names, incident_id, task_id, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = {
            "attachment_id": attachment_id,
            "excel_ranges": excel_ranges,
            "excel_defined_names": excel_defined_names,
            "incident_id": incident_id,
            "task_id": task_id
        }
        results = call_utilities_excel_query_function(circuits_app, function_params)
        assert(expected_results == results)

    @pytest.mark.parametrize("ranges, expected_result", [
        ("\"Sheet1\"!A1:B2, 'Sheet2'!A3", [{"name": "Sheet1", "top_left":"A1", "bottom_right": "B2"},
                                            {"name":"Sheet2", "top_left": "A3", "bottom_right": "A3"}]),
        ("Nothing captured", []),
        ("", []),
        ("'Sheet1'!a1:B2", [{"name":"Sheet1", "top_left":"a1", "bottom_right": "B2"}]),
        ("Somethign! a1:b2, 'Correct.,; '!A1", [{"name":"Correct.,; ", "top_left": "A1", "bottom_right": "A1"}])
    ])
    def test_excel_range_parser(self, ranges, expected_result):
        result = WorksheetData.parse_excel_notation(ranges)
        assert len(expected_result) == len(result)
        for match in range(len(expected_result)):
            for param in expected_result[match]:
                assert param in result[match] and result[match][param] == expected_result[match][param]


    @pytest.mark.parametrize("path, ranges, defined_names, expected_results",[
        ("data/spreadsheet_sample_1.xlsx", "", "", {}),
        ("data/spreadsheet_sample_1.xlsx", "", "", {})
    ])
    def test_worksheet_data(self, path, ranges, defined_names, expected_results):
        import os
        path = os.path.join(os.path.dirname(__file__), path)
        wb = WorksheetData(path, {})