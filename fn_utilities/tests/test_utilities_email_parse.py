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
            "from": [["", "foo@example.com"]],
            "body": u"This is the first part.\n--- mail_boundary ---\n*H\r\x01\x07\x020\u069a+1\x0b0\t\x06\x05+\x0e\x03\x02\x1a\x05\x000\x06\t*J6\x07\x01\x00\x00\x05J0\x05F0\x04.\x02\x02\x04?D0\r\x06\t*\u069a+\r\x01\x01\x05\x05\x00011\x0b0\t\x06\x03U\x04\x06\x13\x02F6\n\x06\x03U\x04\n\x13\x03TDC1\x140\x12\x06\x13\x0bTDC OCES CH\u069a+\r040229115901Z\x17\r060262901Z01\x0b0\t\x06\x03U\x04K1)0'\x06\x03U\x04\n\x13 H\u069a+. organisatorisk tin6nin",
            "subject": "testing"
        }),
        (ArtifactMock.test_data_b64("email_sample_2.eml"), {
            "from": [["", "xxx@xxxx.xxx"]],
            "to": [["", "xxxxxxxxxxx@xxxx.xxxx.xxx"]],
            "received": [
                {"from": u'xxx.xxxx.xxx', "by": u'SMS-GTYxxx.xxxx.xxx', "id": u'j4AKR3r23323', "for": u'<xxxxx@Exxx.xxxx.xxx>', "date": u'Tue, 10 May 2005 15:27:03 -0500'},
                {"from": u'SMS-GTYxxx.xxxx.xxx', "by": u'xxx.xxxx.xxx', "id": u'ca', "for": u'<xxxxx@Exxx.xxxx.xxx>', "date": u'Tue, 10 May 2005 15:27:04 -0500'},
                {"from": u'xxx.xxxx.xxx', "by": u'xxx.xxxx.xxx', "id": u'C1B953B4CB6', "for": u'<xxxxx@Exxx.xxxx.xxx>', "date": u'Tue, 10 May 2005 15:27:05 -0500'}

            ]
        }),
        (ArtifactMock.test_data_b64("email_sample_3.eml"), {
            "html_body": u'["<div dir=\\"ltr\\">see this<div><br></div></div>"]',
            "attachments": [
                {
                    "mail_content_type": "application/pdf",
                    "filename": "example.pdf"
                }
            ]
        }),
    ])
    def test_success(self, circuits_app, base64content, expected_result):
        """ Test calling with sample values for the parameters """
        function_params = { 
            "base64content": base64content,
            "incident_id": 1001
        }
        result = call_email_parse_function(circuits_app, function_params)
        verify_subset(expected_result, result["content"])
