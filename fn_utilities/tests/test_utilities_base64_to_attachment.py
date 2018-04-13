# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from mock_attachment import AttachmentMock
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_utilities"
FUNCTION_NAME = "utilities_base64_to_attachment"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = AttachmentMock


def call_base64_to_attachment_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction(FUNCTION_NAME, function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("{}_result".format(FUNCTION_NAME), parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestBase64ToAttachment:
    """ Tests for the base64_to_attachment function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.parametrize("base64content, incident_id, task_id, file_name, content_type, expected_result", [
        (AttachmentMock.test_data_b64("sample1.pdf"), 1234, None, "file.txt", "text/plain", {"value": "xyz"})
    ])
    def test_success(self, circuits_app, base64content, incident_id, task_id, file_name, content_type, expected_result):
        """ Test calling with sample values for the parameters """
        function_params = { 
            "base64content": base64content,
            "incident_id": incident_id,
            "task_id": task_id,
            "file_name": file_name,
            "content_type": content_type
        }
        #result = call_base64_to_attachment_function(circuits_app, function_params)
        #assert(result == expected_result)