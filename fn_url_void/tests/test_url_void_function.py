# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from mock import patch
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from fn_url_void.components.url_void_function import get_netloc, get_endpoint, call_url_void_api
from resilient_lib import RequestsCommon


PACKAGE_NAME = "fn_url_void"
FUNCTION_NAME = "url_void_function"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_url_void_function_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("url_void_function", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("url_void_function_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestUrlVoidFunction:
    """ Tests for the url_void_function function"""

    def _generateResponse(self, content, status):
        class simResponse:
            def __init__(self, content, status):
                self.status_code = status
                self.text = content

        return simResponse(content, status)

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    def test_get_netloc(self):
        url1 = "https://google.com"
        netloc1 = get_netloc(url1)
        assert netloc1 == "google.com"

        url2 = "https://google.com:443/something?parm1=\"sometext\""
        netloc2 = get_netloc(url2)
        assert netloc2 == "google.com:443"

    def test_get_endpoint(self):
        ep = get_endpoint("Retrieve")
        assert ep == ""

        ep = get_endpoint("Scan")
        assert ep == "scan"

        ep = get_endpoint("Rescan")
        assert ep == "rescan"

        try:
            get_endpoint("something_else")
        except ValueError as e:
            assert e.args[0] == "Unhandled url_api value: something_else. Supported values: retrieve, scan and rescan"

    @patch("requests.request")
    def test_call_url_void_api(self, mocked_requests_get):
        sim_content = """
        <response>
        <details>
            <host> google.com </host>
        </details>
        <detections>
            <engines>
                <engine> ZeroCERT </engine>
            </engines>
            <count> 1 </count>
        </detections>
        <page_load> 0.01 </page_load>
        </response>
        """
        mocked_requests_get.return_value = self._generateResponse(sim_content, 200)

        req_common = RequestsCommon({}, {})
        response = call_url_void_api(req_common, "https://google.com", "fake_identifier", "fake_api_key", "Retrieve")

        expected = {
            "response": {
                "details": {
                    "host": "google.com"
                },
                "detections": {
                    "engines": {
                        "engine": "ZeroCERT"
                    },
                    "count": "1"
                },
                "page_load": "0.01"
            }
        }

        assert response == expected
