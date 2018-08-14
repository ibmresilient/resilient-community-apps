# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import os
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_utilities"
FUNCTION_NAME = "utilities_html2pdf"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_utilities_html2pdf_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("utilities_html2pdf", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("utilities_html2pdf_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestUtilitiesHtml2Pdf:
    """ Tests for the utilities_html2pdf function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.parametrize("html2pdf_data, html2pdf_data_type, html2pdf_stylesheet, expected_results", [
        ("<table border=\"1\"><tr><th>key10</th><td><table border=\"1\"><tr><th>key20</th><td><table border=\"1\"><tr><th>a</th><td>a1</td></tr><tr><th>b</th><td>b1</td></tr><tr><th>key30</th><td><ul><li>1</li><li>2</li><li>3</li><li>4</li></ul></td></tr></table></td></tr></table></td></tr></table>",
         "string", None, "data/html2pdf/no_stylesheet.b64"),
        ("<table border=\"1\"><tr><th>key10</th><td><table border=\"1\"><tr><th>key20</th><td><table border=\"1\"><tr><th>a</th><td>a1</td></tr><tr><th>b</th><td>b1</td></tr><tr><th>key30</th><td><ul><li>1</li><li>2</li><li>3</li><li>4</li></ul></td></tr></table></td></tr></table></td></tr></table>",
         "string", "@page { size: landscape; }* { font-family: Arial; font-size: small; }table { border-collapse: collapse; }table, th, td { border: 1px solid black; }", "data/html2pdf/stylesheet.b64")
    ])
    def test_success(self, circuits_app, html2pdf_data, html2pdf_data_type, html2pdf_stylesheet, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = { 
            "html2pdf_data": html2pdf_data,
            "html2pdf_data_type": html2pdf_data_type,
            "html2pdf_stylesheet": html2pdf_stylesheet
        }
        results = call_utilities_html2pdf_function(circuits_app, function_params)
        # get the expected data
        res_path = os.path.join(os.path.dirname(__file__), expected_results)
        with open(res_path, 'r') as file:
            expected = file.read()

        print (results)
        assert expected == results.get('content')