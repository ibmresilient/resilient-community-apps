# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from mock import patch

from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from  mock_umbrella import  mocked_response

PACKAGE_NAME = "fn_cisco_umbrella_inv"
FUNCTION_NAME = "umbrella_domain_whois_info"

def assert_keys_in(json_obj, *keys):
    for key in keys:
        assert key in json_obj

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_umbrella_domain_whois_info_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("umbrella_domain_whois_info", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("umbrella_domain_whois_info_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestUmbrellaDomainWhoisInfo:
    """ Tests for the umbrella_domain_whois_info function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @patch('investigate.Investigate.get', side_effect=mocked_response)
    @pytest.mark.parametrize("umbinv_emails, umbinv_nameservers, umbinv_domain, umbinv_limit, umbinv_sort, umbinv_offset", [
        (None, None, "cisco.com", 2, "created", 0)
    ])
    def test_umbrella_domain(self, mock_get, circuits_app, umbinv_emails, umbinv_nameservers, umbinv_domain, umbinv_limit, umbinv_sort, umbinv_offset):
        """ Test domain using mocked response. """

        keys = ["administrativeContactName", "administrativeContactEmail", "technicalContactEmail",
                "administrativeContactCity", "administrativeContactOrganization", "addresses", "nameServers"]

        function_params = { 
            "umbinv_emails": umbinv_emails,
            "umbinv_nameservers": umbinv_nameservers,
            "umbinv_domain": umbinv_domain,
            "umbinv_limit": umbinv_limit,
            "umbinv_sort": umbinv_sort,
            "umbinv_offset": umbinv_offset
        }
        results = call_umbrella_domain_whois_info_function(circuits_app, function_params)
        domain_whois = results["domain_whois"]
        assert_keys_in(domain_whois, *keys)

    @patch('investigate.Investigate.get', side_effect=mocked_response)
    @pytest.mark.parametrize("umbinv_emails, umbinv_nameservers, umbinv_domain, umbinv_limit, umbinv_sort, umbinv_offset", [
        (None, "ns1.google.com", None, 2, "created", 0)
    ])

    def test_umbrella_nameservers(self, mock_get, circuits_app, umbinv_emails, umbinv_nameservers, umbinv_domain, umbinv_limit, umbinv_sort, umbinv_offset):
        """ Test nameservers using mocked response. """

        keys = ["sortField", "limit", "moreDataAvailable", "offset", "totalResults"]

        function_params = {
            "umbinv_emails": umbinv_emails,
            "umbinv_nameservers": umbinv_nameservers,
            "umbinv_domain": umbinv_domain,
            "umbinv_limit": umbinv_limit,
            "umbinv_sort": umbinv_sort,
            "umbinv_offset": umbinv_offset
        }
        results = call_umbrella_domain_whois_info_function(circuits_app, function_params)
        ns_whois = results["ns_whois"]
        assert_keys_in(ns_whois["ns1.google.com"], *keys)

    @patch('investigate.Investigate.get', side_effect=mocked_response)
    @pytest.mark.parametrize("umbinv_emails, umbinv_nameservers, umbinv_domain, umbinv_limit, umbinv_sort, umbinv_offset", [
        ("test@example.com", None, None, 2, "created", 0)
    ])

    def test_umbrella_emails(self, mock_get, circuits_app, umbinv_emails, umbinv_nameservers, umbinv_domain, umbinv_limit, umbinv_sort, umbinv_offset):
        """ Test emails using mocked response. """

        keys = ["sortField", "limit", "moreDataAvailable", "offset", "totalResults"]

        function_params = {
            "umbinv_emails": umbinv_emails,
            "umbinv_nameservers": umbinv_nameservers,
            "umbinv_domain": umbinv_domain,
            "umbinv_limit": umbinv_limit,
            "umbinv_sort": umbinv_sort,
            "umbinv_offset": umbinv_offset
        }
        results = call_umbrella_domain_whois_info_function(circuits_app, function_params)
        email_whois = results["email_whois"]
        assert_keys_in(email_whois["test@example.com"], *keys)