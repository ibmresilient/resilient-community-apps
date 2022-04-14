# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
from os.path import dirname, join, realpath
import pytest
from fn_utilities.util.utils_common import b_to_s
from resilient_circuits.util import get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_utilities"
FUNCTION_NAME = "utilities_xml_transformation"

config_data = """[fn_utilities]
# directory of xml stylesheets to use for xml transformations
xml_stylesheet_dir={}
""".format(join(dirname(realpath(__file__)), "data/xmltransformation/"))

# Provide a simulation of the SOAR REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"

def call_utilities_xml_transformation_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("utilities_xml_transformation", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("utilities_xml_transformation_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value

class TestUtilitiesXmlTransformation:
    """ Tests for the utilities_xml_transformation function"""
    DATA_DIR = "data/xmltransformation"

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.parametrize("xml_source, xml_stylesheet, expected_results", [
        ("cdcatalog.xml", "cdcatalog.xslt", "cdcatalog.html")
    ])
    def test_success(self, circuits_app, xml_source, xml_stylesheet, expected_results):
        curr_dir = dirname(realpath(__file__))

        xml_data = open(join(curr_dir, TestUtilitiesXmlTransformation.DATA_DIR, xml_source), mode="rb").read()
        expected_results = open(join(curr_dir, TestUtilitiesXmlTransformation.DATA_DIR, expected_results), mode="r").read()

        """ Test calling with sample values for the parameters """
        function_params = {
            "xml_source": b_to_s(xml_data),
            "xml_stylesheet": xml_stylesheet
        }

        results = call_utilities_xml_transformation_function(circuits_app, function_params)

        assert expected_results == results['content']
