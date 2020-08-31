# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from mock_attachment import AttachmentMock
from fn_utilities.util.utils_common import b_to_s
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from pytest_resilient_circuits import verify_subset

PACKAGE_NAME = "fn_utilities"
FUNCTION_NAME = "utilities_string_to_attachment"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
# resilient_mock = "pytest_resilient_circuits.BasicResilientMock"
resilient_mock = AttachmentMock


def call_utilities_string_to_attachment_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction(FUNCTION_NAME, function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("{}_result".format(FUNCTION_NAME), parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestUtilitiesStringToAttachment:
    """ Tests for the utilities_string_to_attachment function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.livetest
    @pytest.mark.parametrize("string_to_convert_to_attachment, attachment_name, incident_id, expected_results", [
        ("test string", "test attachment name", 202, {"attachment_id" : 27})
    ])
    def test_success(self, circuits_app, string_to_convert_to_attachment, attachment_name, incident_id, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = { 
            "string_to_convert_to_attachment": b_to_s(string_to_convert_to_attachment),
            "attachment_name": attachment_name,
            "incident_id": incident_id
        }
        results = call_utilities_string_to_attachment_function(circuits_app, function_params)
        verify_subset(expected_results, results)
