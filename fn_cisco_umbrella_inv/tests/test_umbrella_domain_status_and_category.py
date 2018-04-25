# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from mock import patch

from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from fn_cisco_umbrella_inv.components.umbrella_dns_rr_hist import *
from  mock_umbrella import  mocked_response


PACKAGE_NAME = "fn_cisco_umbrella_inv"
FUNCTION_NAME = "umbrella_domain_status_and_category"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"

def assert_keys_in(json_obj, *keys):
    for key in keys:
        assert key in json_obj

def call_umbrella_domain_status_and_category_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("umbrella_domain_status_and_category", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("umbrella_domain_status_and_category_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestUmbrellaDomainStatusAndCategory:
    """ Tests for the umbrella_domain_status_and_category function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @patch('investigate.Investigate.get', side_effect=mocked_response)
    @pytest.mark.parametrize("umbinv_domains, umbinv_showlabels, umbinv_status_endpoint", [
        (None, True, 'categories')
    ])
    def test_categories(self, mock_get, circuits_app, umbinv_domains, umbinv_showlabels, umbinv_status_endpoint):
        """ Test domain categories using mocked response. """

        keys = ["130", "131", "132", "133", "137", "141"]

        function_params = { 
            "umbinv_domains": umbinv_domains,
            "umbinv_showlabels": umbinv_showlabels,
            "umbinv_status_endpoint": umbinv_status_endpoint
        }
        results = call_umbrella_domain_status_and_category_function(circuits_app, function_params)
        domain_categories = results["categories"]
        assert_keys_in(domain_categories, *keys)

    @patch('investigate.Investigate.get', side_effect=mocked_response)
    @pytest.mark.parametrize("umbinv_domains, umbinv_showlabels, umbinv_status_endpoint", [
        ("amazon.com", True, 'categorization')
    ])
    def test_domain_statuses(self, mock_get, circuits_app, umbinv_domains, umbinv_showlabels, umbinv_status_endpoint):

        """ Test domain statues using mocked response. """

        keys = ["status", "content_categories", "security_categories"]
        function_params = {
            "umbinv_domains": umbinv_domains,
            "umbinv_showlabels": umbinv_showlabels,
            "umbinv_status_endpoint": umbinv_status_endpoint
        }
        results = call_umbrella_domain_status_and_category_function(circuits_app, function_params)
        domain_statuses = results["statuses"]
        domain_status = domain_statuses.pop("amazon.com")
        assert_keys_in(domain_status, *keys)