# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from mock import patch
from fn_ldap_utilities.util.helper import PACKAGE_NAME
from resilient_circuits.util import get_function_definition
from tests.helper import TestingHelper, get_mock_config_data
from resilient_circuits import SubmitTestFunction, FunctionResult

FUNCTION_NAME = "ldap_utilities_toggle_access"

# Set mock config_data
config_data = get_mock_config_data()

# Provide a simulation of the SOAR REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"

def call_ldap_utilities_toggle_access_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("ldap_utilities_toggle_access", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait(
        "ldap_utilities_toggle_access_result", parent=evt, timeout=timeout)
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

    inputs2 = {
        "ldap_dn": "CN=Test User8,CN=Users,dc=example,DC=com",
        "ldap_toggle_access": {"name": "Disable"}
    }

    outputs2 = {
        "success": True,
        "user_dn": "CN=Test User8,CN=Users,dc=example,DC=com",
        "user_status": "Disabled"
    }

    @patch('fn_ldap_utilities.util.helper.Connection', helper.mocked_connection())
    @patch('fn_ldap_utilities.util.helper.Server', helper.mocked_server())
    @pytest.mark.parametrize("ldap_dn, ldap_toggle_access, expected_results", [
        (inputs2["ldap_dn"], inputs2["ldap_toggle_access"], outputs2)])
    def test_enable(self, circuits_app, ldap_dn, ldap_toggle_access, expected_results):
        """ Test enabling/disabling a user """
        function_params = {
            "ldap_dn": ldap_dn,
            "ldap_toggle_access": ldap_toggle_access
        }
        results = call_ldap_utilities_toggle_access_function(circuits_app, function_params)
        for expected_result in expected_results:
            assert expected_result in results
