# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from .mock_response import give_response, AuthenticationMock, GUIDS_MOCK

try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

PACKAGE_NAME = "fn_cloud_foundry"
FUNCTION_NAME = "fn_cloud_foundry_manage_applications"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_fn_cloud_foundry_manage_applications_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("fn_cloud_foundry_manage_applications", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("fn_cloud_foundry_manage_applications_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestFnCloudFoundryManageApplications:
    """ Tests for the fn_cloud_foundry_manage_applications function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @patch("fn_cloud_foundry.components.fn_cloud_foundry_manage_applications.IBMCloudFoundryAuthenticator")
    @patch("fn_cloud_foundry.util.cloud_foundry_api.requests.get")
    @patch("fn_cloud_foundry.util.cloud_foundry_api.requests.put")
    @pytest.mark.parametrize("fn_cloud_foundry_action, fn_cloud_foundry_applications", [
        ('start', "test1, test2"),
        ('stop', "test1")
    ])
    def test_success(self, put, get, auth, circuits_app, fn_cloud_foundry_action, fn_cloud_foundry_applications):
        """ Test calling with sample values for the parameters """
        auth.return_value = AuthenticationMock()
        put.return_value = give_response(201, GUIDS_MOCK["resources"][0])
        get.return_value = give_response(200, GUIDS_MOCK)

        function_params = { 
            "fn_cloud_foundry_action": fn_cloud_foundry_action,
            "fn_cloud_foundry_applications": fn_cloud_foundry_applications
        }
        results = call_fn_cloud_foundry_manage_applications_function(circuits_app, function_params)
        assert results["test1"]["success"] == True

    @patch("fn_cloud_foundry.components.fn_cloud_foundry_manage_applications.IBMCloudFoundryAuthenticator")
    @patch("fn_cloud_foundry.util.cloud_foundry_api.requests.get")
    @patch("fn_cloud_foundry.util.cloud_foundry_api.requests.put")
    @pytest.mark.parametrize("fn_cloud_foundry_action, fn_cloud_foundry_applications", [
        ('start', "test1")
    ])
    def test_success_start(self, put, get, auth, circuits_app, fn_cloud_foundry_action, fn_cloud_foundry_applications):
        """ Test calling with sample values for the parameters """
        auth.return_value = AuthenticationMock()
        put.return_value = give_response(201, GUIDS_MOCK["resources"][0])
        get.return_value = give_response(200, GUIDS_MOCK)

        function_params = {
            "fn_cloud_foundry_action": fn_cloud_foundry_action,
            "fn_cloud_foundry_applications": fn_cloud_foundry_applications
        }
        results = call_fn_cloud_foundry_manage_applications_function(circuits_app, function_params)
        assert results["test1"]["success"] == True
        assert results["test1"]["current_state"] == "STARTED"

    @patch("fn_cloud_foundry.components.fn_cloud_foundry_manage_applications.IBMCloudFoundryAuthenticator")
    @patch("fn_cloud_foundry.util.cloud_foundry_api.requests.get")
    @patch("fn_cloud_foundry.util.cloud_foundry_api.requests.put")
    @pytest.mark.parametrize("fn_cloud_foundry_action, fn_cloud_foundry_applications", [
        ('wut is this action', "test1")
    ])
    def test_incorrect_action(self, put, get, auth, circuits_app, fn_cloud_foundry_action, fn_cloud_foundry_applications):
        """ Test calling with sample values for the parameters """
        auth.return_value = AuthenticationMock()
        put.return_value = give_response(201, GUIDS_MOCK["resources"][0])
        get.return_value = give_response(200, GUIDS_MOCK)

        function_params = {
            "fn_cloud_foundry_action": fn_cloud_foundry_action,
            "fn_cloud_foundry_applications": fn_cloud_foundry_applications
        }
        results = call_fn_cloud_foundry_manage_applications_function(circuits_app, function_params)
        assert results["success"] == False

    @patch("fn_cloud_foundry.components.fn_cloud_foundry_manage_applications.IBMCloudFoundryAuthenticator")
    @patch("fn_cloud_foundry.util.cloud_foundry_api.requests.get")
    @patch("fn_cloud_foundry.util.cloud_foundry_api.requests.put")
    @pytest.mark.parametrize("fn_cloud_foundry_action, fn_cloud_foundry_applications", [
        ('wut is this action', None),
        (None, "test"),
        (None, None)
    ])
    def test_fails_parameters(self, put, get, auth, circuits_app, fn_cloud_foundry_action, fn_cloud_foundry_applications):
        """ Test calling with sample values for the parameters """
        auth.return_value = AuthenticationMock()
        put.return_value = give_response(201, GUIDS_MOCK["resources"][0])
        get.return_value = give_response(200, GUIDS_MOCK)

        function_params = {
            "fn_cloud_foundry_action": fn_cloud_foundry_action,
            "fn_cloud_foundry_applications": fn_cloud_foundry_applications
        }
        with pytest.raises(AssertionError):
            results = call_fn_cloud_foundry_manage_applications_function(circuits_app, function_params)

    @patch("fn_cloud_foundry.components.fn_cloud_foundry_manage_applications.IBMCloudFoundryAuthenticator")
    @patch("fn_cloud_foundry.util.cloud_foundry_api.requests.get")
    @patch("fn_cloud_foundry.util.cloud_foundry_api.requests.put")
    @pytest.mark.parametrize("fn_cloud_foundry_action, fn_cloud_foundry_applications", [
        ("restage", "rand name")
    ])
    def test_app_not_found(self, put, get, auth, circuits_app, fn_cloud_foundry_action, fn_cloud_foundry_applications):
        """ Test calling with sample values for the parameters """
        auth.return_value = AuthenticationMock()
        put.return_value = give_response(201, GUIDS_MOCK["resources"][0])
        get.return_value = give_response(200, GUIDS_MOCK)

        function_params = {
            "fn_cloud_foundry_action": fn_cloud_foundry_action,
            "fn_cloud_foundry_applications": fn_cloud_foundry_applications
        }
        results = call_fn_cloud_foundry_manage_applications_function(circuits_app, function_params)
        assert results[fn_cloud_foundry_applications]["success"] == False

    @patch("fn_cloud_foundry.components.fn_cloud_foundry_manage_applications.IBMCloudFoundryAuthenticator")
    @patch("fn_cloud_foundry.util.cloud_foundry_api.requests.get")
    @patch("fn_cloud_foundry.util.cloud_foundry_api.requests.put")
    @pytest.mark.parametrize("fn_cloud_foundry_action, fn_cloud_foundry_applications", [
        ('start', "test1")
    ])
    def test_fails_updating(self, put, get, auth, circuits_app, fn_cloud_foundry_action, fn_cloud_foundry_applications):
        """ Test calling with sample values for the parameters """
        auth.return_value = AuthenticationMock()
        put.return_value = give_response(404, {})
        get.return_value = give_response(200, GUIDS_MOCK)

        function_params = {
            "fn_cloud_foundry_action": fn_cloud_foundry_action,
            "fn_cloud_foundry_applications": fn_cloud_foundry_applications
        }
        results = call_fn_cloud_foundry_manage_applications_function(circuits_app, function_params)
        assert results["test1"]["success"] == False