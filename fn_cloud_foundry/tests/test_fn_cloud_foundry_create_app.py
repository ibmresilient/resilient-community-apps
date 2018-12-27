# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult, BaseFunctionError
from .mock_response import give_response, AuthenticationMock

try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

PACKAGE_NAME = "fn_cloud_foundry"
FUNCTION_NAME = "fn_cloud_foundry_create_app"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_fn_cloud_foundry_create_app_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("fn_cloud_foundry_create_app", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("fn_cloud_foundry_create_app_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value

class TestFnCloudFoundryCreateApp:
    """ Tests for the fn_cloud_foundry_create_app function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @patch("fn_cloud_foundry.components.fn_cloud_foundry_create_app.IBMCloudFoundryAuthenticator")
    @patch("fn_cloud_foundry.util.cloud_foundry_api.requests.post")
    @pytest.mark.parametrize("fn_cloud_foundry_applications, fn_cloud_foundry_space_guid, fn_cloud_foundry_additional_parameters_json", [
        ("text", "space", "{}")
    ])
    def test_success(self, post, auth, circuits_app, fn_cloud_foundry_applications, fn_cloud_foundry_space_guid,
                     fn_cloud_foundry_additional_parameters_json):
        """ Test calling with sample values for the parameters """
        auth.return_value = AuthenticationMock()
        post.return_value = give_response(201, {})

        function_params = { 
            "fn_cloud_foundry_applications": fn_cloud_foundry_applications,
            "fn_cloud_foundry_space_guid": fn_cloud_foundry_space_guid,
            "fn_cloud_foundry_additional_parameters_json": fn_cloud_foundry_additional_parameters_json
        }

        results = call_fn_cloud_foundry_create_app_function(circuits_app, function_params)
        assert(results["success"] == True)

    @patch("fn_cloud_foundry.components.fn_cloud_foundry_create_app.IBMCloudFoundryAuthenticator")
    @patch("fn_cloud_foundry.util.cloud_foundry_api.requests.post")
    @pytest.mark.parametrize(
        "fn_cloud_foundry_applications, fn_cloud_foundry_space_guid, fn_cloud_foundry_additional_parameters_json", [
            ("text", "space", "{}")
        ])
    def test_fail(self, post, auth, circuits_app, fn_cloud_foundry_applications, fn_cloud_foundry_space_guid,
                     fn_cloud_foundry_additional_parameters_json):
        """ Test calling with sample values for the parameters """
        auth.return_value = AuthenticationMock()
        post.return_value = give_response(404, {})

        function_params = {
            "fn_cloud_foundry_applications": fn_cloud_foundry_applications,
            "fn_cloud_foundry_space_guid": fn_cloud_foundry_space_guid,
            "fn_cloud_foundry_additional_parameters_json": fn_cloud_foundry_additional_parameters_json
        }

        results = call_fn_cloud_foundry_create_app_function(circuits_app, function_params)
        assert (results["success"] == False)

    @patch("fn_cloud_foundry.components.fn_cloud_foundry_create_app.IBMCloudFoundryAuthenticator")
    @patch("fn_cloud_foundry.util.cloud_foundry_api.requests.post")
    @pytest.mark.parametrize(
        "fn_cloud_foundry_applications, fn_cloud_foundry_space_guid, fn_cloud_foundry_additional_parameters_json", [
            (None, "space", "{}"),
            ("name", None, "{}"),
            ("name", "space", "fails json parse"),
        ])
    def test_fail_expected(self, post, auth, circuits_app, fn_cloud_foundry_applications, fn_cloud_foundry_space_guid,
                  fn_cloud_foundry_additional_parameters_json):
        """ Test calling with sample values for the parameters """
        auth.return_value = AuthenticationMock()
        post.return_value = give_response(404, {})

        function_params = {
            "fn_cloud_foundry_applications": fn_cloud_foundry_applications,
            "fn_cloud_foundry_space_guid": fn_cloud_foundry_space_guid,
            "fn_cloud_foundry_additional_parameters_json": fn_cloud_foundry_additional_parameters_json
        }

        with pytest.raises(AssertionError):
            # failed. In the end it's the calling function that fails, so can only catch Assert
            results = call_fn_cloud_foundry_create_app_function(circuits_app, function_params)
            assert True
