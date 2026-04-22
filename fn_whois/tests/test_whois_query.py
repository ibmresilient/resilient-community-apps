# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2019. All Rights Reserved.
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
import whois
import os
from mock import patch
PACKAGE_NAME = "fn_whois"
FUNCTION_NAME = "whois_query"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_whois_query_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("whois_query", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("whois_query_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value

class WhoisMock():
    """
    Mock out the WHOIS package so that the query function, doesnt contact an outside source

    We also patch the __dict__
    """

    def __init__(self):
        print("In the whois mock")


def mock_whois_payload(input):
    """

    We only need to mock the __dict__ keyword
    This is because __dict__ is how we access the results
    The return type of the whois package is a Domain class
    In the function code __dict__ is called on this class

    In the test itself, we patch this __dict__ with this function mock_whois_payload
    """

    if "ibm-website" in input:
        print("Matched input, to ibm test case")
        return {'name': 'ibm.com', 'registrar': 'CSC Corporate Domains, Inc.', 'creation_date': '1986-03-19 05:00:00', 'expiration_date': '2019-03-20 04:00:00', 'last_updated': '2018-09-18 20:31:50', 'name_servers': ['ns1-99.akam.net', 'asia3.akam.net', 'ns1-206.akam.net', 'usw2.akam.net', 'eur5.akam.net', 'eur2.akam.net', 'usc3.akam.net', 'usc2.akam.net']}

class TestWhoisQuery:
    """ Tests for the whois_query function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.mock_test
    @pytest.mark.parametrize("whois_query", [
        ("https://www.ibm.com")
    ],
    ids=['Test-with-ibm-website'])
    def test_success(self, circuits_app, whois_query):
        """ Test calling with sample values for the parameters """
        function_params = { 
            "whois_query": whois_query
        }
        with patch.object(whois, "whois") as mock_whois:
            mock_whois.return_value = mock_whois_payload(os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0])
            results = call_whois_query_function(circuits_app, function_params)
            assert (results["success"] == True)
            assert (isinstance(results["domain_details"], dict))
            assert (isinstance(results["domain_details_keys"], list))
            assert (isinstance(results["domain_details_values"], list))



    @pytest.mark.livetest
    @pytest.mark.parametrize("whois_query", [
        ("https://www.ibm.com"),
        ("www.ibm.com"),
        ("ibm.com"),
        ("https://www.google.com"),
        ("//www.google.com"),
        ("www.google.com"),
        ("www.reddit.com"),
        ("//www.google.com/")
    ],
    ids=[
        'Test-with-ibm-URL',
        'Test-with-ibm-WWW',
        'Test-with-ibm-hostname',
        'Test-with-google-URL',
        'Test-with-google-WWW-leading-//',
        'Test-with-google-WWW',
        'Test-with-reddit',
        'Test-with-google-WWW-ending-/',
    ])
    def test_live_success(self, circuits_app, whois_query):
        """ Test calling with sample values for the parameters """
        function_params = {
            "whois_query": whois_query
        }

        results = call_whois_query_function(circuits_app, function_params)
        assert (results["success"] == True)
        assert (isinstance(results["domain_details"], dict))
        assert (isinstance(results["domain_details_keys"], list))
        assert (isinstance(results["domain_details_values"], list))
