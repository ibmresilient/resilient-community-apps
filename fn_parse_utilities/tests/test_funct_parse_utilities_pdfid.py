# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from tests.mock_attachment import AttachmentMock
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_parse_utilities"
FUNCTION_NAME = "parse_utilities_pdfid"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = AttachmentMock

SAMPLE1_RESULTS = {
    "header": "%PDF-1.3",
    "filename": "sample1.pdf",
    "isPdf": "True",
    "obj": 20,
    "endobj": 20,
    "stream": 3,
    "endstream": 3,
    "xref": 1,
    "trailer": 1,
    "startxref": 1,
    "/Page": 1,
    "/Encrypt": 0,
    "/ObjStm": 0,
    "/JS": 0,
    "/JavaScript": 0,
    "/AA": 0,
    "/OpenAction": 0,
    "/AcroForm": 0,
    "/JBIG2Decode": 0,
    "/RichMedia": 0,
    "/Launch": 0,
    "/EmbeddedFile": 0,
    "/XFA": 0,
    "/Colors > 2^24": 0
}

def call_parse_utilities_pdfid_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("parse_utilities_pdfid", function_params)

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
        event = circuits.watcher.wait("parse_utilities_pdfid_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value


class TestParseUtilitiesPdfid:
    """ Tests for the parse_utilities_pdfid function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.parametrize("base64content, expected_results", [
        (AttachmentMock.test_data_b64("sample1.pdf"), SAMPLE1_RESULTS)
    ])
    def test_success(self, circuits_app, base64content, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = {
            "parse_utilities_base64content": base64content,
            "parse_utilities_filename": "sample1.pdf"
        }
        results = call_parse_utilities_pdfid_function(circuits_app, function_params)
        assert(expected_results == results)
