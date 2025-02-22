# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from mock_attachment import AttachmentMock
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_utilities"
FUNCTION_NAME = "utilities_attachment_to_base64"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the SOAR REST API (uncomment to connect to a real appliance)
resilient_mock = AttachmentMock

def call_attachment_to_base64_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction(FUNCTION_NAME, function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("{}_result".format(FUNCTION_NAME), parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value

class TestAttachmentToBase64:
    """ Tests for the attachment_to_base64 function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.parametrize("incident_id, task_id, attachment_id", [
        (123, None, 1),
        (123, None, 2)
    ])
    def test_success(self, circuits_app, incident_id, task_id, attachment_id):
        """ Test calling with sample values for the parameters """
        function_params = {
            "incident_id": incident_id,
            "task_id": task_id,
            "attachment_id": attachment_id
        }
        result = call_attachment_to_base64_function(circuits_app, function_params)
        assert(result['content'] == AttachmentMock.test_data_b64_by_id(attachment_id))
