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
from mock_umbrella import mocked_response

PACKAGE_NAME = "fn_cisco_umbrella_inv"
FUNCTION_NAME = "umbrella_dns_rr_hist"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"

def assert_keys_in(json_obj, *keys):
    for key in keys:
        assert key in json_obj

def call_umbrella_dns_rr_hist_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("umbrella_dns_rr_hist", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("umbrella_dns_rr_hist_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestUmbrellaDnsRrHist:
    """ Tests for the umbrella_dns_rr_hist function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @patch('investigate.Investigate.get', side_effect=mocked_response)
    @pytest.mark.parametrize("umbinv_resource, umbinv_resource_type, umbinv_dns_type", [
        ("93.184.216.119", 'ip_address', 'A')
    ])
    def test_dns_rr_history_ip(self, mock_get, circuits_app, umbinv_resource, umbinv_resource_type, umbinv_dns_type):
        """ Test for ip rr history using mocked data. """

        keys_outer = ["features", "rrs"]
        keys_feature = ["rr_count","ld2_count","ld3_count","ld2_1_count","ld2_2_count","div_ld2","div_ld3","div_ld2_1","div_ld2_2"]
        keys_rrs = ["ttl","type","class","rr", "name"]

        function_params = { 
            "umbinv_resource": umbinv_resource,
            "umbinv_resource_type": umbinv_resource_type,
            "umbinv_dns_type": umbinv_dns_type
        }
        results = call_umbrella_dns_rr_hist_function(circuits_app, function_params)
        dns_rr_history_ip = results["dns_rr_history"]
        assert_keys_in(dns_rr_history_ip, *keys_outer)
        features = dns_rr_history_ip["features"]
        assert_keys_in(features, *keys_feature)
        for rrs in dns_rr_history_ip["rrs"]:
            assert_keys_in(rrs, *keys_rrs)

    @patch('investigate.Investigate.get', side_effect=mocked_response)
    @pytest.mark.parametrize("umbinv_resource, umbinv_resource_type, umbinv_dns_type", [
        ("domain.com", 'domain_name', 'A')
    ])
    def test_dns_rr_history_domain(self, mock_get, circuits_app, umbinv_resource, umbinv_resource_type, umbinv_dns_type):
        """ Test for domain rr history using mocked data. """

        keys_outer = ["features", "rrs_tf"]
        keys_feature = ["age","country_codes","is_subdomain","base_domain","rips","rips_stability","cname","prefixes","mail_exchanger"]
        keys_rrs_tf = ["first_seen","last_seen","rrs"]

        function_params = {
            "umbinv_resource": umbinv_resource,
            "umbinv_resource_type": umbinv_resource_type,
            "umbinv_dns_type": umbinv_dns_type
        }
        results = call_umbrella_dns_rr_hist_function(circuits_app, function_params)
        dns_rr_history_domain = results["dns_rr_history"]
        assert_keys_in(dns_rr_history_domain, *keys_outer)
        features = dns_rr_history_domain["features"]
        assert_keys_in(features, *keys_feature)
        for rrs_tf in dns_rr_history_domain["rrs_tf"]:
            assert_keys_in(rrs_tf, *keys_rrs_tf)