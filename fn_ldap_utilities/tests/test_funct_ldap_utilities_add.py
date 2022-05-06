# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from resilient_circuits.util import get_function_definition
from fn_ldap_utilities.util.helper import PACKAGE_NAME
from resilient_circuits import SubmitTestFunction, FunctionResult
from helper import TestingHelper, get_mock_config_data
from mock import patch

FUNCTION_NAME = "ldap_utilities_add"

# Read the default configuration-data section from the package
config_data = get_mock_config_data()

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"

def call_ldap_utilities_add_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction(FUNCTION_NAME, function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait(FUNCTION_NAME+"_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value

class TestLdapUtilitiesAdd:
    """ Tests for the ldap_utilities_add function"""

    helper = TestingHelper()

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func

    inputs = {
        "ldap_dn": "CN=Test User8X,CN=Users,DC=example,DC=com",
        "ldap_attribute_name_values": "'objectclass':'inetOrgPerson'",
        "ldap_multiple_group_dn": "['CN=TestGroup5,CN=Users,dc=example,DC=com']"
    }

    outputs = {
        'success': True,
        'reason': None,
        'content': {
            'result': 0,
            'description': 'success',
            'dn': '',
            'message': '',
            'referrals': None,
            'type': 'addResponse'
        },
        'inputs': {},
        'metrics': {}
    }

    @patch('fn_ldap_utilities.util.helper.Connection', helper.mocked_connection())
    @patch('fn_ldap_utilities.util.helper.Server', helper.mocked_server())
    @pytest.mark.parametrize("ldap_dn, ldap_attribute_name_values, ldap_multiple_group_dn, expected_results",
                             [(inputs["ldap_dn"], inputs["ldap_attribute_name_values"], inputs["ldap_multiple_group_dn"], outputs)])
    def test_success(self, circuits_app, ldap_dn, ldap_attribute_name_values, ldap_multiple_group_dn, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = {
            "ldap_dn": ldap_dn,
            "ldap_attribute_name_values": ldap_attribute_name_values,
            "ldap_multiple_group_dn": ldap_multiple_group_dn
        }
        results = call_ldap_utilities_add_function(
            circuits_app, function_params)
        assert(results['success'])
        assert(expected_results['content'] == results['content'])
