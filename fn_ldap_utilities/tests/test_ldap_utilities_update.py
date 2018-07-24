# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2018. All Rights Reserved.
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from helper import TestingHelper
from mock import patch

PACKAGE_NAME = "fn_ldap_utilities"
FUNCTION_NAME = "ldap_utilities_update"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"

def call_ldap_utilities_update_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("ldap_utilities_update", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("ldap_utilities_update_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestLdapUtilitiesUpdate:
    """ Tests for the ldap_utilities_update function"""

    helper = TestingHelper()

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None
    
    inputs = {
      "ldap_dn": "CN=Test User8,CN=Users,DC=dev,DC=co3sys,DC=com",
      "ldap_attribute_name": "givenName",
      "ldap_attribute_values": "['Lord Farquaad']"
    }

    outputs = {
      'attribute_name': 'givenName',
      'attribute_values': ['Lord Farquaad'],
      'success': True,
      'user_dn': 'CN=Test User8,CN=Users,DC=dev,DC=co3sys,DC=com'
    }

    @patch('fn_ldap_utilities.util.helper.Connection', helper.mocked_connection())
    @patch('fn_ldap_utilities.util.helper.Server', helper.mocked_server())
    @pytest.mark.parametrize("ldap_dn, ldap_attribute_name, ldap_attribute_values, expected_results", 
    [(inputs["ldap_dn"], inputs["ldap_attribute_name"], inputs["ldap_attribute_values"], outputs)])
    def test_success(self, circuits_app, ldap_dn, ldap_attribute_name, ldap_attribute_values, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = { 
            "ldap_dn": ldap_dn,
            "ldap_attribute_name": ldap_attribute_name,
            "ldap_attribute_values": ldap_attribute_values
        }
        results = call_ldap_utilities_update_function(circuits_app, function_params)
        assert(expected_results == results)