# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2018. All Rights Reserved.
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from helper import TestingHelper, get_mock_config_data
from mock import patch

PACKAGE_NAME = "fn_ldap_utilities"
FUNCTION_NAME = "ldap_utilities_add_to_groups"

#Set mock config_data
config_data = get_mock_config_data()

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_ldap_utilities_add_to_groups_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("ldap_utilities_add_to_groups", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("ldap_utilities_add_to_groups_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestLdapUtilitiesAddToGroups:
    """ Tests for the ldap_utilities_add_to_groups function"""

    helper = TestingHelper()

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    inputs = {
      "ldap_multiple_user_dn": "['CN=Test User8,CN=Users,DC=dev,DC=co3sys,DC=com', 'CN=Test User9,CN=Users,DC=dev,DC=co3sys,DC=com']",
      "ldap_multiple_group_dn": "['CN=TestGroup5,CN=Users,DC=dev,DC=co3sys,DC=com']"
    }

    outputs = {
      'groups_dn': ['CN=TestGroup5,CN=Users,DC=dev,DC=co3sys,DC=com'],
      'success': True,
      'users_dn': ['CN=Test User8,CN=Users,DC=dev,DC=co3sys,DC=com','CN=Test User9,CN=Users,DC=dev,DC=co3sys,DC=com']
    }
    
    @patch('fn_ldap_utilities.util.helper.Connection', helper.mocked_connection())
    @patch('fn_ldap_utilities.util.helper.Server', helper.mocked_server())
    @pytest.mark.parametrize("ldap_multiple_user_dn, ldap_multiple_group_dn, expected_results", [
        (inputs["ldap_multiple_user_dn"], inputs["ldap_multiple_group_dn"], outputs)])
    def test_success(self, circuits_app, ldap_multiple_user_dn, ldap_multiple_group_dn, expected_results):
        """ Test adding 2 users to a group """
        function_params = { 
            "ldap_multiple_user_dn": ldap_multiple_user_dn,
            "ldap_multiple_group_dn": ldap_multiple_group_dn
        }
        results = call_ldap_utilities_add_to_groups_function(circuits_app, function_params)
        assert(expected_results == results)