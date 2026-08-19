# -*- coding: utf-8 -*-
# Generated with resilient-sdk v51.0.1.1.1.dev16+g03d1460d
"""Tests using pytest_resilient_circuits"""

import pytest
import json
import os
import uuid
from fn_low_code.lib.constants import INTEGRATION_ERROR
from fn_low_code.lib.helpers import encode_basic_auth, decode_basic_auth
from mocks.subscription_mocks import ConnectorResilientMock
from circuits import Event
from resilient_circuits import LowCodeMessage, LowCodeResult
from resilient_circuits.util import get_config_data

PACKAGE_NAME = "fn_low_code"
FUNCTION_NAME = "low_code"

BASIC_USER = "user@example.com"
BASIC_PWD = "secret"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
#resilient_mock = "pytest_resilient_circuits.BasicResilientMock"
resilient_mock = ConnectorResilientMock

HTTPBIN_JSON = json.loads(open(os.path.join(os.path.dirname(__file__), "data", "test_httpbin_template.json"), "r").read())

class SubmitTestLowCode(Event):
    """ Circuits event to insert a test Function Message """
    def __init__(self, lowcode_name, lowcode_params):
        if not lowcode_name or not isinstance(lowcode_params, dict):
            raise ValueError("lowcode_name and lowcode_params are required")
        msg_id = str(uuid.uuid4())
        super(SubmitTestLowCode, self).__init__(queue=lowcode_name, msg_id=msg_id, message=lowcode_params)

def call_low_code_function(circuits, lowcode_params, timeout=5):
    # Create the SubmitTestLowCode event
    evt = LowCodeMessage(queue_name="low_code",
                         headers=lowcode_params["headers"],
                         message=lowcode_params["message"],
                         frame=lowcode_params)

    # Fire a message to the function
    circuits.manager.fire(evt, "low_code")

    # circuits will fire an "exception" event if an exception is raised in the FunctionComponent
    # return this exception if it is raised
    exception_event = circuits.watcher.wait("exception", parent=None, timeout=timeout)

    if exception_event is not False:
        exception = exception_event.args[1]
        raise exception
    # else return the FunctionComponent's results
    else:
        event = circuits.watcher.wait("low_code_success", parent=evt, timeout=timeout)
        assert event
        lowcode_result = event.parent.value.getValue()[0]
        assert isinstance(lowcode_result, LowCodeResult)
        pytest.wait_for(event, "complete", True)
        return lowcode_result

class MockedResponse(LowCodeResult):
    def __init__(self):
        self.success = True
        self.status_code = 200
        self.text = '{"content": "mock data"}'

    def json(self):
        return {"content": "mock data"}

class TestLowCode:
    """ Tests for the low_code function"""

    @pytest.mark.livetest
    def test_put_success(self, circuits_app):
        msg = dict(HTTPBIN_JSON)
        payload = msg["message"]["request_payload"]
        payload["server_url"] = f"{payload['server_url']}/anything"
        payload["method"] = "PUT"
        payload["request_body"] = """{"x": "y"}"""
        payload["query_params"] = {"a": "b"}
        payload["headers"]["X-Anything"] = "anything"

        payload["security"]["scheme"] = "basic"
        payload["security"]["api_key"] = BASIC_USER
        payload["security"]["api_key_secret"] = BASIC_PWD

        """ Test calling with sample values for the parameters """
        results = call_low_code_function(circuits_app, msg)
        assert(results.success)
        assert(results.value.get("status_code") == 200)
        content = json.loads(results.value.get("content", {}))
        assert(content.get("args", {}).get("a") == "b")
        assert(content.get("json", {}).get("x") == "y")

        # test for basic auth and headers found
        found = 0
        headers = content.get("headers", [])
        for header in headers:
            if header == "Authorization":
                elements = headers[header].split(" ")
                assert len(elements) == 2
                assert elements[0] == "Basic"
                decode_usr, decode_pwd = decode_basic_auth(elements[1])
                assert decode_usr == BASIC_USER
                assert decode_pwd == BASIC_PWD
                found += 1
            elif header.lower() == "x-anything":
                assert headers[header] == "anything"
                found += 1

        if found != 2:
            raise AssertionError("Not all headers found")

    @pytest.mark.livetest
    def test_post_success(self, circuits_app):
        msg = dict(HTTPBIN_JSON)
        payload = msg["message"]["request_payload"]
        payload["server_url"] = f"{payload['server_url']}/anything"
        payload["method"] = "POST"
        payload["request_body"] = """{"x": "y"}"""
        payload["query_params"] = {"a": "b"}

        """ Test calling with sample values for the parameters """
        results = call_low_code_function(circuits_app, msg)
        assert(results.success)
        assert(results.value.get("status_code") == 200)
        content = json.loads(results.value.get("content", {}))
        assert(content.get("args", {}).get("a") == "b") # query_params
        assert(content.get("json", {}).get("x") == "y") # request body

    @pytest.mark.livetest
    def test_path_params_success(self, circuits_app):
        base64_encoded = encode_basic_auth(BASIC_USER, BASIC_PWD)
        msg = dict(HTTPBIN_JSON)
        payload = msg["message"]["request_payload"]
        payload["server_url"] = f"{payload['server_url']}/base64/{{base64_encoded}}"
        payload["method"] = "GET"
        payload["path_params"] = {"base64_encoded": f"{base64_encoded}"}

        """ Test calling with sample values for the parameters """
        results = call_low_code_function(circuits_app, msg)
        assert(results.success)
        assert(results.value.get("status_code") == 200)
        content = results.value.get("content")
        assert(content == f"{BASIC_USER}:{BASIC_PWD}")

    @pytest.mark.livetest
    def test_403_failure(self, circuits_app, caplog):
        TEST_403 = 403
        msg = dict(HTTPBIN_JSON)
        payload = msg["message"]["request_payload"]
        payload["server_url"] = f"{payload['server_url']}/status/{TEST_403}"
        payload["custom_params"]["num_retries"] = 2 # retry twice

        payload["method"] = "GET"

        """ Test calling with sample values for the parameters """
        results = call_low_code_function(circuits_app, msg)
        assert(not results.success)
        assert(results.value.get("status_code") == TEST_403)

        # check that we retried
        assert caplog.text.count("retrying in") == 1

    @pytest.mark.livetest
    def test_timeout_failure(self, circuits_app):
        msg = dict(HTTPBIN_JSON)
        payload = msg["message"]["request_payload"]
        payload["server_url"] = f"{payload['server_url']}/delay/10"
        payload["custom_params"]["request_timeout"] = 5
        payload["method"] = "GET"

        """ Test calling with sample values for the parameters """
        results = call_low_code_function(circuits_app, msg)
        assert(not results.success)
        assert(results.value.get("status_code") == INTEGRATION_ERROR)

    def test_app_failure(self, circuits_app):
        msg = dict(HTTPBIN_JSON)
        payload = msg["message"]["request_payload"]
        payload["server_url"] = f"{payload['server_url']}/status"
        payload["request_body"] = {"a": "b"} # should fail since this is not string encoded
        payload["method"] = "GET"

        """ Test calling with sample values for the parameters """
        results = call_low_code_function(circuits_app, msg)
        assert(not results.success)
        assert(results.value.get("status_code") == INTEGRATION_ERROR)
