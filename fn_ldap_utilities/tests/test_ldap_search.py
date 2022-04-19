# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
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
    evt = SubmitTestFunction("ldap_utilities_search", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("ldap_utilities_search_result", parent=evt, timeout=timeout)
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
        assert func is not None

    @patch('fn_ldap_utilities.util.helper.Server', helper.mocked_server())
    @patch('fn_ldap_utilities.util.helper.Connection', helper.mocked_connection())
    @pytest.mark.parametrize("login_search_base, login_search_filter, login_search_attributes, login_param, login_expected_result", [
        ("dc=example,dc=com", {"type": "text", "content": "(uid=)"}, "cn", "", {'success': False, 'entries': []})
    ])
    def test_ldap_basic_connection(self, circuits_app, login_search_base, login_search_filter, login_search_attributes, login_param,
                             login_expected_result):
        """ Test LDAP connection
         Test LDAP connection with simple search options.
         Positive tests.
         """
        function_params = {
            "ldap_search_base": login_search_base,
            "ldap_search_filter": login_search_filter,
            "ldap_search_attributes": login_search_attributes,
            "ldap_search_param": login_param
        }
        result = call_ldap_utilities_search_function(circuits_app, function_params)
        for expected_result in login_expected_result:
            assert expected_result in result

    @patch('fn_ldap_utilities.util.helper.Connection', helper.mocked_connection())
    @patch('fn_ldap_utilities.util.helper.Server', helper.mocked_server())
    @pytest.mark.parametrize("success_search_base, success_search_filter, success_search_attributes, success_param, success_expected_result",
    [
        (
          "dc=example,dc=com",
          {"type": "text", "content": "(&(objectClass=person)(uid=einstein))"},
          "uid,cn",
          "",
          {'success': True,'entries': [{'cn': ['Albert Einstein'], 'dn': 'uid=einstein,dc=example,dc=com', 'uid': ['einstein']}]}
        ),
        (
          "dc=example,dc=com",
          {"type": "text", "content": "(&(objectClass=person)(uid=%ldap_param%))"},
          "uid,cn",
          "einstein",
          {'success': True, 'entries': [{'cn': ['Albert Einstein'], 'dn': 'uid=einstein,dc=example,dc=com', 'uid': ['einstein']}]}
        ),
        (
          "dc=example,dc=com",
          {"type": "text", "content": "(&(objectClass=person)(|(uid=newton)(uid=%ldap_param%)))"},
          "uid,cn",
          "einstein",
          {'success': True, 'entries': [{'cn': ['Isaac Newton'], 'dn': 'uid=newton,dc=example,dc=com', 'uid': ['newton']}, {'cn': ['Albert Einstein'], 'dn': 'uid=einstein,dc=example,dc=com', 'uid': ['einstein']}]}
        )
    ])

    def test_utilities_ldap_search(self, circuits_app, success_search_base, success_search_filter, success_search_attributes, success_param, success_expected_result):
        """ Test LDAP searches
         Test LDAP search with various base, filter and attribute options.
         All positive tests.
         """
        function_params = {
            "ldap_search_base": success_search_base,
            "ldap_search_filter": success_search_filter,
            "ldap_search_attributes": success_search_attributes,
            "ldap_search_param": success_param
        }
        result = call_ldap_utilities_search_function(circuits_app, function_params)
        for expected_result in success_expected_result:
            assert expected_result in result
