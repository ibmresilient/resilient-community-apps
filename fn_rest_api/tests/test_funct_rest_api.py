# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

import pytest, unittest, logging

from fn_rest_api.components import funct_rest_api
from fn_rest_api.lib.helper import build_dict
from resilient_lib import IntegrationError
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_rest_api"
FUNCTION_NAME = "rest_api"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"

def call_rest_api_function(circuits, function_params, timeout=5):
    # Fire a message to the function
    evt = SubmitTestFunction(FUNCTION_NAME, function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("rest_api_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestInternetUtilitiesCallRestApi:
    """ Tests for the rest_api function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.livetest
    @pytest.mark.parametrize(
        "method, url, rest_headers, rest_body, rest_verify",
        [
            (
                'POST',
                "https://httpbin.org/post",
                'Content-type: application/json;charset=UTF-8',
                "title: foo\n body : ƱƲ\n  userId:1\n",
                True
            ),
            (
                'POST',
                "https://httpbin.org/post",
                """Content-type: application/json; charset=UTF-8""",
                """{"title": "foo", "body" : "ƱƲ",  "userId":"1"}""",
                True
            )
        ]
    )
    def test_standard_request(self, circuits_app, method, url, rest_headers, rest_body, rest_verify):
        """ Test calling with sample values for the parameters """
        function_params = {
            "rest_api_method": method,
            "rest_api_url": url,
            "rest_api_headers": rest_headers,
            "rest_api_body"   : rest_body,
            "rest_api_verify" : rest_verify}

        results = call_rest_api_function(circuits_app, function_params)
        content = results.get('content')
        rest_body = build_dict(rest_body)
        tc = unittest.TestCase()
        tc.assertDictEqual(rest_body, content.get("json").get("json"))
    
    @pytest.fixture(autouse=True)
    def init_caplog_fixture(self, caplog):
        self.caplog = caplog

    @pytest.mark.livetest
    def test_retry_request(self, circuits_app):
        """ Test calling with sample values for the parameters """
        RETRY_TRIES_COUNT   = 4
        RETRY_DELAY_COUNT   = 2
        RETRY_BACKOFF_COUNT = 3
        ENDPOINT = "https://postman-echo.com/status/404"

        self.caplog.clear() # clear caplog
        # Capturing log messages that are only warning
        self.caplog.set_level(logging.WARNING)
        function_params = {
            "rest_api_method": "GET",
            "rest_api_url"  : ENDPOINT,
            "rest_api_verify" : True,
            "rest_retry_tries" : RETRY_TRIES_COUNT,
            "rest_retry_delay" : RETRY_DELAY_COUNT,
            "rest_retry_backoff" : RETRY_BACKOFF_COUNT}

        evt = SubmitTestFunction(FUNCTION_NAME, function_params)
        circuits_app.manager.fire(evt)
        event = circuits_app.watcher.wait("rest_api_result", parent=evt, timeout=30)
        # filtering out logs generated only by resilient_lib
        records = list(filter(lambda x:  x.name == 'resilient_lib.components.requests_common', self.caplog.records))

        # For these values: RETRY_TRIES_COUNT = 4   RETRY_DELAY_COUNT = 2   RETRY_BACKOFF_COUNT = 3
        # requests must be executed in the following order:
        # failed request 1, retrying in 2 seconds...
        # failed request 2, retrying in 6 seconds...
        # failed request 3, retrying in 18 seconds...
        # request 4
        assert len(records) == RETRY_TRIES_COUNT
        assert f"retrying in {RETRY_DELAY_COUNT} seconds..." in records[0].message
        assert f"retrying in {RETRY_DELAY_COUNT * RETRY_BACKOFF_COUNT} seconds..." in records[1].message
        assert f"retrying in {RETRY_DELAY_COUNT * RETRY_BACKOFF_COUNT * RETRY_BACKOFF_COUNT} seconds..." in records[2].message
        assert f"404 Client Error:" in records[3].message
        self.caplog.clear() # clear caplog

