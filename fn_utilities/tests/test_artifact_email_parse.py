# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import io
import os
import pytest
import requests_mock
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from pytest_resilient_circuits import BasicResilientMock, resilient_endpoint, verify_subset

PACKAGE_NAME = "fn_utilities"
FUNCTION_NAME = "artifact_email_parse"


import logging
LOG = logging.getLogger(__name__)


class ArtifactMock(BasicResilientMock):

    def test_data(self, filename):
        """Read a test data file"""
        template_file_path = os.path.join(os.path.dirname(__file__), "data", filename)
        with io.open(template_file_path, 'rb') as template_file:
            return template_file.read()

    email_artifacts = {
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

    @resilient_endpoint("GET", "/incidents/[0-9]+/artifacts/[0-9]+$")
    def artifacts_get(self, request):
        """ GET an artifact """
        artifact_id = request.url.split("/")[-1]
        data = self.email_artifacts[artifact_id]
        return requests_mock.create_response(request,
                                             status_code=200,
                                             json=data)

    @resilient_endpoint("GET", "/incidents/[0-9]+/artifacts/[0-9]+/contents$")
    def artifacts_contents_get(self, request):
        """ GET the file contents of an artifact """
        artifact_id = request.url.split("/")[-2]
        data = self.test_data(self.email_artifacts[artifact_id]["value"])
        return requests_mock.create_response(request,
                                             status_code=200,
                                             content=data)


# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = ArtifactMock


def call_artifact_email_parse_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("artifact_email_parse", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("artifact_email_parse_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(evt, "complete", True)
    return event.kwargs["result"].value


class TestArtifactEmailParse:
    """ Tests for the artifact_email_parse function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.parametrize("incident_id, artifact_id, expected_result", [
        (1234, 1, {
            "from": [
                {
                    "name": "",
                    "email": "foo@example.com"
                }
            ],
            "body_text": "This is the first part.\r\n",
            "timestamp": 1118089282000,
            "subject": "testing"
        }),
        (1234, 2, {
            "headers": {
                "received": [
                    "from xxx.xxxx.xxx by xxx.xxxx.xxx with ESMTP id C1B953B4CB6 for <xxxxx@Exxx.xxxx.xxx>; Tue, 10 May 2005 15:27:05 -0500",
                    "from SMS-GTYxxx.xxxx.xxx by xxx.xxxx.xxx with ESMTP id ca for <xxxxx@Exxx.xxxx.xxx>; Tue, 10 May 2005 15:27:04 -0500",
                    "from xxx.xxxx.xxx by SMS-GTYxxx.xxxx.xxx with ESMTP id j4AKR3r23323 for <xxxxx@Exxx.xxxx.xxx>; Tue, 10 May 2005 15:27:03 -0500"
                ],
                "from": "xxx@xxxx.xxx",
                "to": "xxxxxxxxxxx@xxxx.xxxx.xxx",
            }
        }),
        (1234, 3, {
            "body_html": "<div dir=\"ltr\">see this<div><br></div></div>\r\n",
            "attachments": [
                {
                    "content_type": "application/pdf",
                    "filename": "example.pdf"
                }
            ]
        }),
    ])
    def test_success(self, circuits_app, incident_id, artifact_id, expected_result):
        """ Test calling with sample values for the parameters """
        function_params = { 
            "incident_id": incident_id,
            "artifact_id": artifact_id
        }
        result = call_artifact_email_parse_function(circuits_app, function_params)
        verify_subset(expected_result, result)
