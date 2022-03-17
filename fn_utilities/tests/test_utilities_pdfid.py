# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from mock_attachment import AttachmentMock
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_utilities"
FUNCTION_NAME = "utilities_pdfid"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the SOAR REST API (uncomment to connect to a real appliance)
resilient_mock = AttachmentMock

SAMPLE1_RESULTS = {
    "header": "%PDF-1.3",
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



def call_pdfid_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction(FUNCTION_NAME, function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("{}_result".format(FUNCTION_NAME), parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestPdfid:
    """ Tests for the pdfid function"""

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
            "base64content": base64content
        }
        results = call_pdfid_function(circuits_app, function_params)
        assert(expected_results == results)