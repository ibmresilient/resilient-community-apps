# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2018. All Rights Reserved.
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from mock import patch
import requests_mock
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from fn_gcp.util.helper import GCPHelper
PACKAGE_NAME = "fn_gcp"
FUNCTION_NAME = "gcp_utilities_screenshot_sandboxed_webpage"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"

# This method will be used by the mock to replace requests.get
def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    if kwargs.get('success') == True:
        return MockResponse(json_data={'contents': [{"test1":"test"},{"test2":"test"}]},status_code=200)
    else:
        return MockResponse(json_data={}, status_code=400)

def call_gcp_utilities_screenshot_sandboxed_webpage_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("gcp_utilities_screenshot_sandboxed_webpage", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("gcp_utilities_screenshot_sandboxed_webpage_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestGcpUtilitiesScreenshotSandboxedWebpage:
    """ Tests for the gcp_utilities_screenshot_sandboxed_webpage function"""

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

                
