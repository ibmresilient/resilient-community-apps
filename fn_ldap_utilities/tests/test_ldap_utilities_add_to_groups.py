# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from mock import patch
from fn_ldap_utilities.util.helper import PACKAGE_NAME
from resilient_circuits.util import get_function_definition
from helper import TestingHelper, get_mock_config_data
from resilient_circuits import SubmitTestFunction, FunctionResult

FUNCTION_NAME = "ldap_utilities_add_to_groups"

#Set mock config_data
config_data = get_mock_config_data()

# Provide a simulation of the SOAR REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"

def call_ldap_utilities_add_to_groups_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction(FUNCTION_NAME, function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait(FUNCTION_NAME+"_result", parent=evt, timeout=timeout)
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
        assert func

    inputs = {
      "ldap_multiple_user_dn": "['CN=Test User8,CN=Users,dc=example,DC=com', 'CN=Test User9,CN=Users,dc=example,DC=com']",
      "ldap_multiple_group_dn": "['CN=TestGroup5,CN=Users,dc=example,DC=com']"
    }

    outputs = {
        'success': True,
        "content": {
            'groups_dn': ['CN=TestGroup5,CN=Users,dc=example,DC=com'],
            'users_dn': ['CN=Test User8,CN=Users,dc=example,DC=com','CN=Test User9,CN=Users,dc=example,DC=com']
        }
    }

    @patch('fn_ldap_utilities.util.helper.Connection', helper.mocked_connection())
    @patch('fn_ldap_utilities.util.helper.Server', helper.mocked_server())
    @pytest.mark.parametrize("mock_inputs, expected_results", [(inputs, outputs)])
    def test_success(self, circuits_app, mock_inputs, expected_results):
        """ Test adding 2 users to a group """
        results = call_ldap_utilities_add_to_groups_function(circuits_app, mock_inputs)
        for expected in expected_results:
            assert expected in results
