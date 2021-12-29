# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from helper import TestingHelper, get_mock_config_data
from mock import patch

PACKAGE_NAME = "fn_ldap_utilities"
FUNCTION_NAME = "ldap_utilities_add"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"

def call_ldap_utilities_add_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("ldap_utilities_add", function_params)

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
        event = circuits.watcher.wait("ldap_utilities_add_result", parent=evt, timeout=timeout)
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
        assert func is not None

    inputs = {
      "ldap_dn": "CN=Test User8X,CN=Users,DC=dev,DC=co3sys,DC=com",
      "ldap_attribute_name_values": "'objectclass':'inetOrgPerson'",
      "ldap_multiple_group_dn": "['CN=TestGroup5,CN=Users,DC=dev,DC=co3sys,DC=com']"
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
        results = call_ldap_utilities_add_function(circuits_app, function_params)
        assert(results['success'])
        assert(expected_results['content'] == results['content'])
