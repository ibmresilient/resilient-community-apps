# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
from os.path import dirname, join, realpath
import pytest
from fn_parse_utilities.util.utils_common import b_to_s
from resilient_circuits.util import get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_parse_utilities"
FUNCTION_NAME = "parse_utilities_xml_transformation"

# Read the default configuration-data section from the package
config_data = """[fn_parse_utilities]
# directory of xml stylesheets to use for xml transformations
xml_stylesheet_dir={}
""".format(join(dirname(realpath(__file__)), "data/xmltransformation/"))

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_parse_utilities_xml_transformation_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("parse_utilities_xml_transformation", function_params)

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
        event = circuits.watcher.wait("parse_utilities_xml_transformation_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value


class TestParseUtilitiesXmlTransformation:
    """ Tests for the parse_utilities_xml_transformation function"""

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

        xml_data = open(join(curr_dir, TestParseUtilitiesXmlTransformation.DATA_DIR, xml_source), mode="rb").read()
        expected_results = open(join(curr_dir, TestParseUtilitiesXmlTransformation.DATA_DIR, expected_results), mode="r").read()

        """ Test calling with sample values for the parameters """
        function_params = {
            "parse_utilities_xml_source": b_to_s(xml_data),
            "parse_utilities_xml_stylesheet": xml_stylesheet
        }

        results = call_parse_utilities_xml_transformation_function(circuits_app, function_params)

        assert expected_results == results['content']
