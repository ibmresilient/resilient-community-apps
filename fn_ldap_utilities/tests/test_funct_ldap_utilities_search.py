# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from mock import patch
from fn_ldap_utilities.util.helper import PACKAGE_NAME
from resilient_circuits.util import get_function_definition
from helper import TestingHelper, get_mock_config_data
from resilient_circuits import SubmitTestFunction, FunctionResult

FUNCTION_NAME = "ldap_utilities_search"

# Read the default configuration-data section from the package
config_data = get_mock_config_data()

# Provide a simulation of the SOAR REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"

def call_ldap_utilities_search_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction(FUNCTION_NAME, function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait(FUNCTION_NAME+"_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value

class TestLdapUtilitiesSearch:
    """ Tests for the ldap_utilities_search function"""

    helper = TestingHelper(isSearch=True)

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func

    inputs = {
        "ldap_search_base": "dc=example,dc=com",
        "ldap_search_filter": {"type": "text", "content": "(uid=)"},
        "ldap_search_attributes": "cn",
        "ldap_search_param": ""
    }

    outputs = {
        "success": False,
        "content": {
            "entries": []
        }
    }

    @patch('fn_ldap_utilities.util.helper.Server', helper.mocked_server())
    @patch('fn_ldap_utilities.util.helper.Connection', helper.mocked_connection())
    @pytest.mark.parametrize("mock_inputs, login_expected_result", [(inputs, outputs)])
    def test_ldap_basic_connection(self, circuits_app, mock_inputs, login_expected_result):
        """ Test LDAP connection
         Test LDAP connection with simple search options.
         Positive tests.
         """
        result = call_ldap_utilities_search_function(circuits_app, mock_inputs)
        assert result.get("success") == login_expected_result.get("success")

    inputs1 = {
        "ldap_search_base": "dc=example,dc=com",
        "ldap_search_filter": {"type": "text", "content": "(&(objectClass=person)(uid=einstein))"},
        "ldap_search_attributes": "uid,cn",
        "ldap_search_param": ""
    }

    outputs1 = {
        'success': True,
        "content":{
            'entries': [{'cn': ['Albert Einstein'], 'dn': 'uid=einstein,dc=example,dc=com', 'uid': ['einstein']}]
        }
    }

    inputs2 = {
        "ldap_search_base": "dc=example,dc=com",
        "ldap_search_filter": {"type": "text", "content": "(&(objectClass=person)(uid=%ldap_param%))"},
        "ldap_search_attributes": "uid,cn",
        "ldap_search_param": "einstein"
    }

    outputs2 = {
        'success': True,
        "content":{
            'entries': [{'cn': ['Albert Einstein'], 'dn': 'uid=einstein,dc=example,dc=com', 'uid': ['einstein']}]
        }
    }

    inputs3 = {
        "ldap_search_base": "dc=example,dc=com",
        "ldap_search_filter": {"type": "text", "content": "(&(objectClass=person)(|(uid=newton)(uid=%ldap_param%)))"},
        "ldap_search_attributes": "uid,cn",
        "ldap_search_param": "einstein"
    }

    outputs3 = {
        'success': True,
        "content":{
            'entries': [{'cn': ['Isaac Newton'], 'dn': 'uid=newton,dc=example,dc=com', 'uid': ['newton']}, {'cn': ['Albert Einstein'], 'dn': 'uid=einstein,dc=example,dc=com', 'uid': ['einstein']}]
        }
    }

    @patch('fn_ldap_utilities.util.helper.Connection', helper.mocked_connection())
    @patch('fn_ldap_utilities.util.helper.Server', helper.mocked_server())
    @pytest.mark.parametrize("mock_inputs, success_expected_result",
    [(inputs1, outputs1), (inputs2, outputs2), (inputs3, outputs3)])

    def test_utilities_ldap_search(self, circuits_app, mock_inputs, success_expected_result):
        """ Test LDAP searches
         Test LDAP search with various base, filter and attribute options.
         All positive tests.
         """
        result = call_ldap_utilities_search_function(circuits_app, mock_inputs)
        for expected in success_expected_result:
            assert expected in result
