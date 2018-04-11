# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
import logging
from mock_artifact import ArtifactMock
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from pytest_resilient_circuits import verify_subset

PACKAGE_NAME = "fn_utilities"
FUNCTION_NAME = "utilities_email_parse"
LOG = logging.getLogger(__name__)


# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = ArtifactMock


def call_email_parse_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction(FUNCTION_NAME, function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("{}_result".format(FUNCTION_NAME), parent=evt, timeout=timeout)
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

    @pytest.mark.parametrize("base64content, expected_result", [
        (ArtifactMock.test_data_b64("email_sample_1.eml"), {
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
        (ArtifactMock.test_data_b64("email_sample_2.eml"), {
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
        (ArtifactMock.test_data_b64("email_sample_3.eml"), {
            "body_html": "<div dir=\"ltr\">see this<div><br></div></div>\r\n",
            "attachments": [
                {
                    "content_type": "application/pdf",
                    "filename": "example.pdf"
                }
            ]
        }),
    ])
    def test_success(self, circuits_app, base64content, expected_result):
        """ Test calling with sample values for the parameters """
        function_params = { 
            "base64content": base64content
        }
        result = call_email_parse_function(circuits_app, function_params)
        verify_subset(expected_result, result)
