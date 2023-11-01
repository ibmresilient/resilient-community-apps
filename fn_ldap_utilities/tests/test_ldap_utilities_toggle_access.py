# -*- coding: utf-8 -*-
# Generated with resilient-sdk v48.0.4034
"""Tests using pytest_resilient_circuits"""

import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from helper import TestingHelper, get_mock_config_data
from mock import patch
from fn_ldap_utilities.util.helper import PACKAGE_NAME

FUNCTION_NAME = "ldap_utilities_toggle_access"

# Set mock config_data
config_data = get_mock_config_data()

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"

def call_ldap_utilities_toggle_access_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction(FUNCTION_NAME, function_params)

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
        event = circuits.watcher.wait(FUNCTION_NAME+"_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value

class TestLdapUtilitiesToggleAccess:
    """ Tests for the ldap_utilities_toggle_access function"""

    helper = TestingHelper()

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    mock_inputs_1 = {
        "ldap_toggle_access": "Disable",
        "ldap_dn": "CN=Test User8,CN=Users,dc=example,DC=com"
    }

    expected_results_1 = {
        "success": True,
        "content": {
            "user_dn": "CN=Test User8,CN=Users,dc=example,DC=com",
            "user_status": "Disable"
        }
    }

    @patch('fn_ldap_utilities.util.helper.Connection', helper.mocked_connection())
    @patch('fn_ldap_utilities.util.helper.Server', helper.mocked_server())
    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (mock_inputs_1, expected_results_1)
    ])
    def test_success(self, circuits_app, mock_inputs, expected_results):
        """ Test calling with sample values for the parameters """

        results = call_ldap_utilities_toggle_access_function(circuits_app, mock_inputs)
        for expected in expected_results:
                assert expected in results
