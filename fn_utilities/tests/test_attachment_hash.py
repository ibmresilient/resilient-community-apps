# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import os
import io
import pytest
import requests_mock
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from pytest_resilient_circuits import BasicResilientMock, resilient_endpoint

PACKAGE_NAME = "fn_utilities"
FUNCTION_NAME = "attachment_hash"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)


class AttachmentMock(BasicResilientMock):

    def test_data(self, filename):
        """Read a test data file"""
        template_file_path = os.path.join(os.path.dirname(__file__), "data", filename)
        with io.open(template_file_path, 'rb') as template_file:
            return template_file.read()

    attachments = {
        "1": {
            "description": "mail",
            "value": "email_sample_1.eml",
            "type": "RFC 822 Email Message File",
            "id": 1
        },
        "2": {
            "description": "mail",
            "value": "email_sample_2.eml",
            "type": "RFC 822 Email Message File",
            "id": 2
        },
        "3": {
            "description": "mail",
            "value": "email_sample_3.eml",
            "type": "RFC 822 Email Message File",
            "id": 3
        }
    }

    @resilient_endpoint("GET", "/incidents/[0-9]+/attachments/[0-9]+$")
    def artifacts_get(self, request):
        """ GET an artifact """
        attachment_id = request.url.split("/")[-1]
        data = self.attachments[attachment_id]
        return requests_mock.create_response(request,
                                             status_code=200,
                                             json=data)

    @resilient_endpoint("GET", "/incidents/[0-9]+/attachments/[0-9]+/contents$")
    def artifacts_contents_get(self, request):
        """ GET the file contents of an artifact """
        attachment_id = request.url.split("/")[-2]
        data = self.test_data(self.attachments[attachment_id]["value"])
        return requests_mock.create_response(request,
                                             status_code=200,
                                             content=data)


# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = AttachmentMock


def call_attachment_hash_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    circuits.manager.fire(SubmitTestFunction("attachment_hash", function_params))
    event = circuits.watcher.wait("attachment_hash_result", timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestAttachmentHash:
    """ Tests for the attachment_hash function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.parametrize("incident_id, attachment_id, expected_result", [
        (123, 123, {"value": "xyz"}),
        (123, 123, {"value": "xyz"})
    ])
    def test_success(self, circuits_app, incident_id, attachment_id, expected_result):
        """ Test calling with sample values for the parameters """
        function_params = { 
            "incident_id": incident_id,
            "attachment_id": attachment_id
        }
        result = call_attachment_hash_function(circuits_app, function_params)
        assert(result == expected_result)