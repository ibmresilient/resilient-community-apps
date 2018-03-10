# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from mock_attachment import AttachmentMock
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from pytest_resilient_circuits import verify_subset

PACKAGE_NAME = "fn_utilities"
FUNCTION_NAME = "spreadsheet_read"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = AttachmentMock


def call_spreadsheet_read_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("spreadsheet_read", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("spreadsheet_read_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestSpreadsheetRead:
    """ Tests for the spreadsheet_read function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    def test_success(self, circuits_app):
        """ Test calling with sample values for the parameters """
        base64content = AttachmentMock.test_data_b64("spreadsheet_sample_1.xlsx")
        function_params = { 
            "base64content": base64content
        }
        result = call_spreadsheet_read_function(circuits_app, function_params)

        s = result["worksheets"]["Sheet1"]
        assert s[0]["A"] == "ID"
        s = result["worksheets"][u"Secönd Sheet"]
        assert s[8]["E"] == u"\"τρία\""
