# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from mock import patch
import requests_mock
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from fn_google_cloud_functions.util.helper import GCPHelper
from requests.sessions import Session

PACKAGE_NAME = "fn_google_cloud_functions"
FUNCTION_NAME = "gcp_cloud_functions_sandbox_and_screenshot_webpage"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"

# This method will be used by the mock to replace requests.get
def mocked_requests_get(*args, **kwargs):

    class RawResp:
        """
        A mock class intended to mock the 'raw' attribute on a Response

        Contains a method Read() which is the most common way to access the raw attribute
        """
        def read(self):
            """
            Python 2 and 3 handle strings/bytes differently so we need a solution which works on both

            One solution is to make the return value 'bytes-like'
            But in doing so we must also decode this value to avoid errors on py3

            python 2 can -- return "Mock"
            python 3 can -- return b"Mock"

            but then you need to decode any byte-like stuff to make it JSON Serializable
            #.decode("utf-8")
            :return:
            """
            return b'Mock'

    class MockResponse:
        """
        A mock class intended to mock the entire Response attribute for a request.
        """
        def __init__(self, json_data, status_code,raw):
            self.json_data = json_data
            self.status_code = status_code
            self.raw = RawResp()

        def json(self):
            return self.json_data


    if kwargs.get('success') == True:
        return MockResponse(json_data={'contents': [{"test1":"test"},{"test2":"test"}]},status_code=200, raw="test")
    else:
        return MockResponse(json_data={}, status_code=400)
def call_gcp_cloud_functions_sandbox_and_screenshot_webpage_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("gcp_cloud_functions_sandbox_and_screenshot_webpage", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("gcp_cloud_functions_sandbox_and_screenshot_webpage_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestGcpCloudFunctionsSandboxAndScreenshotWebpage:
    """ Tests for the gcp_cloud_functions_sandbox_and_screenshot_webpage function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None


    def test_config_gather_failure(self):
        """Should raise an exception when trying to gather config options without patching.
        This is because config.py does not have usuable config values and that is where they are pulled from when not in a resilient-circuits enviroment."""
        helper = GCPHelper({})
        with pytest.raises(Exception):
            helper.setup_config()

    def test_config_gather_success(self):
        """When patching the gathering of config values to return Non-Null values,
        the function should not fail or raise any errors """
        helper = GCPHelper({})
        with patch.object(GCPHelper, "get_config_option", lambda x, y, z=None: "10", True):
            helper.setup_config()


    @pytest.mark.parametrize("gcp_url, expected_results", [
        ("text", {"success": True}),
        ("text2", {"success": True})
    ])
    def test_success(self, circuits_app, gcp_url, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = {
            "gcp_url": gcp_url
        }
        # Mock acquiring the config options, all config options are set to '10' or 10
        with patch.object(GCPHelper, "get_config_option", lambda x, y, z=None: "10", True):
            # Get a handle on the requests.Session class and patch its get function
            with patch.object(Session, 'get') as mock_session:
                # Replace the return value of our mock_session with a custom function
                mock_session.return_value = mocked_requests_get(success=True)
                # Fire the function with mocked functionality
                results = call_gcp_cloud_functions_sandbox_and_screenshot_webpage_function(circuits_app, function_params)
                assert (expected_results["success"] == results["success"])


