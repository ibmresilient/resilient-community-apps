# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import functools
import pytest
from mock import patch, Mock
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from ldap3 import Server, Connection, ALL, ALL_ATTRIBUTES, MOCK_SYNC
import logging

LOG = logging.getLogger(__name__)
PACKAGE_NAME = "fn_ldap_search"
FUNCTION_NAME = "ldap_search"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"
# Create a fake LDAP server from the info and schema json files
fake_server = Server.from_definition('my_fake_server', 'mock_server_info.json', 'mock_server_schema.json')


def mocked_server():
    """Mock ldap3 server.
    :return: Return mocked server object
    """
    server = Mock(return_value=fake_server)
    return server

def mocked_connection():
    """Mock ldap3 connection.
    :return: Return mocked connection object
    """
    # Create a MockSyncStrategy connection to the fake server
    mocked_connection = Connection(fake_server, user='cn=my_user,ou=test,o=lab', password='my_password',
                                     client_strategy=MOCK_SYNC)
    # Populate the DIT of the fake server with mock entries
    mocked_connection.strategy.entries_from_json('mock_server_entries.json')

    connection = Mock(return_value=mocked_connection)
    return connection

def call_ldap_search_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("ldap_search", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("ldap_search_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestLdapSearch:
    """ Tests for the ldap_search function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @patch('fn_ldap_search.components.ldap_search.Connection', mocked_connection())
    @patch('fn_ldap_search.components.ldap_search.Server', mocked_server())
    @pytest.mark.parametrize("login_search_base, login_search_filter, login_search_attributes, login_param, login_expected_result", [
        ("dc=example,dc=com", {"type": "text", "content": "(uid=)"}, "cn", "", {'entries': []})
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
            "ldap_param": login_param
        }
        result = call_ldap_search_function(circuits_app, function_params)
        assert (login_expected_result == result)

    @patch('fn_ldap_search.components.ldap_search.Connection', mocked_connection())
    @patch('fn_ldap_search.components.ldap_search.Server', mocked_server())
    @pytest.mark.parametrize("success_search_base, success_search_filter, success_search_attributes, success_param, success_expected_result", [
        ("dc=example,dc=com", {"type": "text", "content": "(&(objectClass=person)(uid=einstein))"}, "uid,cn", "",
         {'entries': [{'cn': ['Albert Einstein'], 'dn': 'uid=einstein,dc=example,dc=com', 'uid': ['einstein']}]}),
        ("dc=example,dc=com", {"type": "text", "content": "(&(objectClass=person)(uid=%ldap_param%))"},
         "uid,cn", "einstein", {'entries': [{'cn': ['Albert Einstein'], 'dn': 'uid=einstein,dc=example,dc=com', 'uid': ['einstein']}]}),
        ("dc=example,dc=com", {"type": "text", "content": "(&(objectClass=person)(|(uid=newton)(uid=%ldap_param%)))"}, "uid,cn", "einstein",
         {'entries': [{'cn': ['Isaac Newton'], 'dn': 'uid=newton,dc=example,dc=com', 'uid': ['newton']},
                      {'cn': ['Albert Einstein'], 'dn': 'uid=einstein,dc=example,dc=com', 'uid': ['einstein']}]})
    ])
    def test_ldap_search(self, circuits_app, success_search_base, success_search_filter, success_search_attributes, success_param, success_expected_result):
        """ Test LDAP searches

         Test LDAP search with various base, filter and attribute options.
         All positive tests.

         """
        function_params = {
            "ldap_search_base": success_search_base,
            "ldap_search_filter": success_search_filter,
            "ldap_search_attributes": success_search_attributes,
            "ldap_param": success_param
        }
        result = call_ldap_search_function(circuits_app, function_params)
        assert(success_expected_result == result)





