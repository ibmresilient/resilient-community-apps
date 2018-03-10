# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
import json
import ast
import base64
import openpyxl
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_utilities"
FUNCTION_NAME = "spreadsheet_write"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_spreadsheet_write_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("spreadsheet_write", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("spreadsheet_write_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


single_sheet_data_1 = [
    {
        "A": "one",
        "B": 1
    },
    {
        "A": u"twö",
        "B": 2
    }
]

single_sheet_data_2 = [
    {},
    {},
    {
        "D": u"one",
        "E": 1
    },
    {
        "D": "two",
        "F": 2
    }
]

multi_sheet_data = {
    "Sheet 1": single_sheet_data_1,
    "Sheet 2": single_sheet_data_2
}

class TestSpreadsheetWrite:
    """ Tests for the spreadsheet_write function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.parametrize("name, input_data, expected_result", [
        ("1json", json.dumps(single_sheet_data_1), {"content": "CgAKAIACAAAXEAAAAAA="}),
        ("2json", json.dumps(single_sheet_data_2), {"content": "AAoAgAIAABkQAAAAAA=="}),
        ("3json", json.dumps(multi_sheet_data), {"content": "AAsACwDGAgAAxBEAAAAA"}),
        ("1str", str(single_sheet_data_1), {"content": "CgAKAIACAAAXEAAAAAA="}),
        ("2str", str(single_sheet_data_2), {"content": "AAoAgAIAABkQAAAAAA=="}),
        ("3str", str(multi_sheet_data), {"content": "AAsACwDGAgAAxBEAAAAA"})
    ])
    def test_success(self, circuits_app, name, input_data, expected_result):
        """ Test calling with sample values for the parameters """

        function_params = {
            "input_data": input_data
        }
        results = call_spreadsheet_write_function(circuits_app, function_params)

        # write the file
        data = base64.b64decode(results["content"])
        filename = "/tmp/{}.xlsx".format(name)
        with open(filename, "wb") as xlsx:
            xlsx.write(data)

        try:
            input = json.loads(input_data)
        except ValueError:
            input = ast.literal_eval(input_data)

        # open it in openpyxl and spot check
        wb = openpyxl.load_workbook(filename, read_only=True)
        if isinstance(input, list):
            assert len(wb.worksheets) == 1
        else:
            assert len(wb.worksheets) == len(input.keys())
            for sheet in wb.worksheets:
                assert sheet.title in input

        # verify the raw content
        assert(results["content"].endswith(expected_result["content"]))

