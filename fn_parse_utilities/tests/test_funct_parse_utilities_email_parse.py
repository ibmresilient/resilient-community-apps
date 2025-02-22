# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from tests.mock_artifact import ArtifactMock
from resilient_lib import b_to_s
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_parse_utilities"
FUNCTION_NAME = "parse_utilities_email_parse"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = ArtifactMock

def call_parse_utilities_email_parse_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("parse_utilities_email_parse", function_params)

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
        event = circuits.watcher.wait("parse_utilities_email_parse_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value


class TestParseUtilitiesEmailParse:
    """ Tests for the parse_utilities_email_parse function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.parametrize("base64content, expected_result", [
            (ArtifactMock.test_data_b64("email_sample_1.eml"), {
                "from": [["", "foo@example.com"]],
                "body": u"This is the first part.",
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
                "html_body": u'["<div dir=\\"ltr\\">see this<div><br></div></div>',
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
            "parse_utilities_base64content": b_to_s(base64content),
            "parse_utilities_incident_id": 1001
        }
        result = call_parse_utilities_email_parse_function(circuits_app, function_params)
        verify_subset(expected_result, result["content"])

def verify_subset(expected, actual):
    """Test that the values match, where expected can be a subset of actual"""
    if isinstance(expected, dict):
        assert isinstance(actual, dict)
        for (key, value) in expected.items():
            verify_subset(value, actual.get(key))
    elif isinstance(expected, list):
        assert isinstance(actual, list)
        for evalue, avalue in zip(expected, actual):
            verify_subset(evalue, avalue)
    else:
        assert actual.startswith(expected)