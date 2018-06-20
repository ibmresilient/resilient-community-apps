# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function

from resilient_circuits.action_message import FunctionException_, FunctionError_

try:
    from unittest.mock import patch
except ImportError:
    from mock import patch
import pytest

from fn_utilities.components.utilities_excel_query import WorksheetData
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult, FunctionError
from tests.mock_attachment import AttachmentMock
import json
import os

PACKAGE_NAME = "fn_utilities"
FUNCTION_NAME = "utilities_excel_query"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = AttachmentMock


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

    @pytest.mark.parametrize("attachment_id, incident_id, task_id, excel_ranges, excel_defined_names, expected_results",
                             [
                                 (42, None, None, "'JAN 2015'!A3,", None, "data/excel_query/test_cell_empty.dat"),
                                 (None, 1123, 33, None, None, "data/excel_query/test_cell_empty.dat"),
                                 (None, None, 33, None, None, "data/excel_query/test_cell_empty.dat")
                             ])
    def test_bad_attachment_input(self, attachment_id, incident_id, task_id, excel_ranges,
                     excel_defined_names, expected_results, circuits_app):
        function_params = {
            "attachment_id": attachment_id,
            "excel_ranges": excel_ranges,
            "excel_defined_names": excel_defined_names,
            "incident_id": incident_id,
            "task_id": task_id
        }
        # When Function Error Gets called in testing, the runner fails
        with pytest.raises(AssertionError):
            result = call_utilities_excel_query_function(circuits_app, function_params)

    @patch("fn_utilities.components.utilities_excel_query.WorksheetData")
    @pytest.mark.parametrize("attachment_id, incident_id, task_id, excel_ranges, excel_defined_names, expected_results",
    [
        (42, 1123, None, "'JAN 2015'!B5:B5,", "", "data/excel_query/test_cell_string.dat"),
        (42, None, 33, "'JAN 2015'!B5,", "", "data/excel_query/test_cell_string.dat"),
        (42, 1123, 33, "", "test1", "data/excel_query/test_named_ranges.dat")
    ])
    def test_success(self, worksheet, circuits_app, attachment_id, incident_id, task_id, excel_ranges,
                     excel_defined_names, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = {
            "attachment_id": attachment_id,
            "excel_ranges": excel_ranges,
            "excel_defined_names": excel_defined_names,
            "incident_id": incident_id,
            "task_id": task_id
        }
        # get the expected data
        res_path = os.path.join(os.path.dirname(__file__), expected_results)
        with open(res_path, 'r') as file:
            expected = file.read()
        # mock the worksheet processing data
        worksheet = worksheet.return_value
        worksheet.parse.return_value = None
        worksheet.result = expected
        results = call_utilities_excel_query_function(circuits_app, function_params)

        assert expected == results


class TestWorksheetData:
    @pytest.mark.parametrize("ranges, expected_result", [
        (None, []),
        ("Nothing captured", []),
        ("", []),
        ("'Sheet1'!A1:B2", [{"name": "Sheet1", "top_left": "A1", "bottom_right": "B2"}]),
        ("'Sheet1'!a10:B20", [{"name": "Sheet1", "top_left": "a10", "bottom_right": "B20"}]),
        ("'Sheet1'!a1:B20", [{"name": "Sheet1", "top_left": "a1", "bottom_right": "B20"}]),
        ("'Sheet1'!a10:B2", [{"name": "Sheet1", "top_left": "a10", "bottom_right": "B2"}]),
        ("\"Sheet1\"!A1:B2, 'Sheet2'!A3", [{"name": "Sheet1", "top_left": "A1", "bottom_right": "B2"},
                                            {"name": "Sheet2", "top_left": "A3", "bottom_right": "A3"}]),
        ("Somethign! a1:b2, 'Correct.,; '!A1", [{"name":"Correct.,; ", "top_left": "A1", "bottom_right": "A1"}])
    ])
    def test_excel_range_parser(self, ranges, expected_result):
        result = WorksheetData.parse_excel_notation(ranges)
        assert len(expected_result) == len(result)
        for match in range(len(expected_result)):
            for param in expected_result[match]:
                assert param in result[match] and result[match][param] == expected_result[match][param]

    @pytest.mark.parametrize("path, ranges, defined_names, expected_result_path", [
        ("data/excel_query/budget.xlsx", "", "test1", "data/excel_query/test_named_ranges.dat"),
        ("data/excel_query/budget.xlsx", "", ["test1"], "data/excel_query/test_named_ranges.dat"),
        ("data/excel_query/budget.xlsx", "", True, "data/excel_query/test_named_ranges.dat"),
        ("data/excel_query/budget.xlsx", "'JAN 2015'!A3,", False, "data/excel_query/test_cell_empty.dat"),
    ])
    def test_defined_ranges_different_inputs(self, path, ranges, defined_names, expected_result_path):
        wb_path = os.path.join(os.path.dirname(__file__), path)
        wb = WorksheetData(wb_path, {
            "ranges": WorksheetData.parse_excel_notation(ranges),
            "named_ranges": defined_names
        })
        wb.parse()
        res_path = os.path.join(os.path.dirname(__file__), expected_result_path)
        with open(res_path, 'r') as file:
            expected = file.read()

        assert json.loads(expected.strip()) == json.loads(json.dumps(wb.result, default=WorksheetData.serializer))

    @pytest.mark.parametrize("path, ranges, defined_names, expected_result_path", [
        ("data/excel_query/budget.xlsx", {}, "test2", "data/excel_query/test_named_ranges.dat"),
        ("data/excel_query/budget.xlsx", [{"name": "JAN 2015", "top_left": "A03", "bottom_right": "00A"}],
            False, "data/excel_query/test_named_ranges.dat"),
        ("data/excel_query/budget.xlsx", {}, ["test2"], "data/excel_query/test_named_ranges.dat")
    ])
    def test_defined_ranges_different_wrong_inputs(self, path, ranges, defined_names, expected_result_path):
        wb_path = os.path.join(os.path.dirname(__file__), path)
        wb = WorksheetData(wb_path, {
            "ranges": ranges,
            "named_ranges": defined_names
        })
        with pytest.raises((FunctionError_, FunctionException_)):
            wb.parse_sheet_ranges(ranges)
            wb.parse_named_ranges(defined_names)

    @pytest.mark.parametrize("path, ranges, defined_names, expected_result_path",[
        ("data/excel_query/budget.xlsx", "'JAN 2015'!A3,", None, "data/excel_query/test_cell_empty.dat"),
        ("data/excel_query/budget.xlsx", "'JAN 2015'!A3,", "", "data/excel_query/test_cell_empty.dat"),
        ("data/excel_query/budget.xlsx", "'JAN 2015'!B5,", "", "data/excel_query/test_cell_string.dat"),
        ("data/excel_query/budget.xlsx", "'Sheet1'!A1:A1,", "", "data/excel_query/test_cell_symbols.dat"),
    ])
    def test_worksheet_data_single_cell(self, path, ranges, defined_names, expected_result_path):
        wb_path = os.path.join(os.path.dirname(__file__), path)
        wb = WorksheetData(wb_path, {
            "ranges": WorksheetData.parse_excel_notation(ranges),
            "named_ranges": WorksheetData.parse_defined_names_notation(defined_names)
        })
        wb.parse()
        res_path = os.path.join(os.path.dirname(__file__), expected_result_path)
        with open(res_path, 'r') as file:
            expected = file.read()
        # comparing objects is a work around for the difference in iteration through dictionaries in Python 2 and 3
        # which creates different json dumps
        assert json.loads(expected.strip()) == json.loads(json.dumps(wb.result, default=WorksheetData.serializer))

    @pytest.mark.parametrize("path, ranges, defined_names, expected_result_path", [
        ("data/excel_query/budget.xlsx", "'JAN 2015'!A3:A3,", "", "data/excel_query/test_cell_empty.dat"),
        ("data/excel_query/budget.xlsx", "'JAN 2015'!B5:B5,", "", "data/excel_query/test_cell_string.dat"),
        ("data/excel_query/budget.xlsx", "'Sheet1'!D1:D12", "", "data/excel_query/test_all_types.dat"),
        ("data/excel_query/Google Spreadsheet.xlsx", "'Sheet1'!A1:A10", "", "data/excel_query/test_google_sp.dat"),
        ("data/excel_query/budget.xlsx", "'JAN 2015'!A3, 'JAN 2015'!A1:D10",
            "", "data/excel_query/test_multiple_ranges.dat")
    ])
    def test_worksheet_data_range(self, path, ranges, defined_names, expected_result_path):
        wb_path = os.path.join(os.path.dirname(__file__), path)
        wb = WorksheetData(wb_path, {
            "ranges": WorksheetData.parse_excel_notation(ranges),
            "named_ranges": WorksheetData.parse_defined_names_notation(defined_names)
        })
        wb.parse()
        res_path = os.path.join(os.path.dirname(__file__), expected_result_path)
        with open(res_path, 'r') as file:
            expected = file.read()

        assert json.loads(expected.strip()) == json.loads(json.dumps(wb.result, default=WorksheetData.serializer))

    @pytest.mark.parametrize("path, ranges, defined_names, expected_result_path", [
        ("data/excel_query/budget.xlsx", "'JAN 2015'!A3:A3,", "", "data/excel_query/test_cell_empty.dat"),
        ("data/excel_query/budget.xlsm", "'JAN 2015'!A3:A3,", "", "data/excel_query/test_cell_empty.dat"),
        ("data/excel_query/Google Spreadsheet.xlsx", "'Sheet1'!A1:A10", "", "data/excel_query/test_google_sp.dat"),
    ])
    def test_worksheet_extensions(self, path, ranges, defined_names, expected_result_path):
        wb_path = os.path.join(os.path.dirname(__file__), path)
        wb = WorksheetData(wb_path, {
            "ranges": WorksheetData.parse_excel_notation(ranges),
            "named_ranges": WorksheetData.parse_defined_names_notation(defined_names)
        })
        wb.parse()
        res_path = os.path.join(os.path.dirname(__file__), expected_result_path)
        with open(res_path, 'r') as file:
            expected = file.read()

        assert json.loads(expected.strip()) == json.loads(json.dumps(wb.result, default=WorksheetData.serializer))

    @pytest.mark.parametrize("path, ranges, defined_names, expected_result_path", [
        ("data/excel_query/budget.xlsx", "'JAN 2015'!A3, 'Sheet1'!A1:A1",
         "", "data/excel_query/test_multiple_sheets.dat")
    ])
    def test_worksheet_data_multiple_sheets(self, path, ranges, defined_names, expected_result_path):
        wb_path = os.path.join(os.path.dirname(__file__), path)
        wb = WorksheetData(wb_path, {
            "ranges": WorksheetData.parse_excel_notation(ranges),
            "named_ranges": WorksheetData.parse_defined_names_notation(defined_names)
        })
        wb.parse()
        res_path = os.path.join(os.path.dirname(__file__), expected_result_path)
        with open(res_path, 'r') as file:
            expected = file.read()
        expected = json.loads(expected.strip())
        actual = json.loads(json.dumps(wb.result, default=WorksheetData.serializer))
        # Python 3.6 and 2.7 have different dictionary iteration order, so the _keys
        # are the same, but in different order
        expected["sheets"]["_keys"].sort()
        actual["sheets"]["_keys"].sort()
        assert expected == actual

    @pytest.mark.parametrize("path, ranges, defined_names, expected_result_path", [
        ("data/excel_query/budget.xlsx", "", "test1", "data/excel_query/test_named_ranges.dat"),
        ("data/excel_query/budget.xlsx", "'JAN 2015'!A3, 'JAN 2015'!A1:D10", "test1",
            "data/excel_query/test_ranges_and_named.dat")
    ])
    def test_defined_names(self, path, ranges, defined_names, expected_result_path):
        wb_path = os.path.join(os.path.dirname(__file__), path)
        wb = WorksheetData(wb_path, {
            "ranges": WorksheetData.parse_excel_notation(ranges),
            "named_ranges": WorksheetData.parse_defined_names_notation(defined_names)
        })
        wb.parse()
        res_path = os.path.join(os.path.dirname(__file__), expected_result_path)
        with open(res_path, 'r') as file:
            expected = file.read()

        assert json.loads(expected.strip()) == json.loads(json.dumps(wb.result, default=WorksheetData.serializer))

    @pytest.mark.parametrize("path, ranges, defined_names, expected_result_path", [
        ("data/excel_query/budget.xlsx", "'JANUA 2015'!A3:A3,", "", "data/excel_query/test_cell_empty.dat"),
        ("data/excel_query/budget.xlsx", "", "test2", "data/excel_query/test_cell_empty.dat"),
        ("data/excel_query/wrong_name.file", "", "test2", "data/excel_query/test_cell_empty.dat"),
        ("data/excel_query", "", "test2", "data/excel_query/test_cell_empty.dat")
    ])
    def test_no_arguments_fails(self, path, ranges, defined_names, expected_result_path):
        # Test that wrong input raises a FunctionError
        with pytest.raises((FunctionException_, FunctionError_)):
            wb_path = os.path.join(os.path.dirname(__file__), path)
            wb = WorksheetData(wb_path, {
                "ranges": WorksheetData.parse_excel_notation(ranges),
                "named_ranges": WorksheetData.parse_defined_names_notation(defined_names)
            })
            wb.parse()
