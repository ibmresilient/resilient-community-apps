# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import sys
import pkg_resources
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

import ipaddress

from mock import patch
from test_helper import get_mock_config

PACKAGE_NAME = "fn_ipinfo"
FUNCTION_NAME = "fn_ipinfo_query_ip_address"

# Read the default configuration-data section from the package
#config_data = get_config_data(PACKAGE_NAME)
config_data = get_mock_config()
# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"

def mocked_ipinfo_call():
    """Mock the result of the IPInfo call.
    This call returns a custom class called Details
    Import it here and fill the class with mock data"""
    from ipinfo.details import Details

    raw_details = {'ip': u'8.8.8.8', 'hostname': 'google-public-dns-a.google.com', 'city': 'Mountain View', 'region': 'California', 'country': 'US', 'loc': '37.3860,-122.0840', 'postal': '94035', 'phone': '650', 'org': 'AS15169 Google LLC', 'country_name': 'United States', 'latitude': '37.3860', 'longitude': '-122.0840'}

    #if sys.version_info < (3, 0):
    raw_details['ip_address'] = ipaddress.ip_address(raw_details.get('ip'))
    return Details(raw_details)



def call_fn_ipinfo_query_ip_address_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("fn_ipinfo_query_ip_address", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("fn_ipinfo_query_ip_address_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestFnIpinfoQueryIpAddress:
    """ Tests for the fn_ipinfo_query_ip_address function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    """ At the time of development, the ipinfo package does not work on Py2 due to an import issue
    This is prevelant on version 1.0.3
    While a fix is developed, skip tests if
    -- the version number of ipinfo is not 1.0.4 or greater
    -- the version is less than py36
    
    """
    @pytest.mark.skipif((pkg_resources.get_distribution("ipinfo").version <= "1.0.3" and sys.version_info < (3, 6)),
                        reason="Tests currently fail on 2 with ipinfo==1.0.3")
    @pytest.mark.parametrize("ipinfo_query_ip, expected_results", [
        ("8.8.8.8", {"value": "xyz"})
    ],ids=['Google-DNS'])
    def test_success(self, circuits_app, ipinfo_query_ip, expected_results):
        """ Test calling with sample values for the parameters """
        # Import ipinfo here to avoid py2 failure on test setup
        from ipinfo.handler import Handler
        import ipinfo

        function_params = { 
            "ipinfo_query_ip": ipinfo_query_ip
        }
        # Patch the init of Handler class to prevent outside calls
        with patch.object(Handler, "__init__", lambda access_token: None) as mocked_handler:

            with patch.object(ipinfo, "getHandler",
                              lambda token: Handler()):
                # Patch getDetails with a mock of the return data
                with patch.object(Handler, "getDetails") as mock_get_details:
                    mock_get_details.return_value = mocked_ipinfo_call()
                    results = call_fn_ipinfo_query_ip_address_function(circuits_app, function_params)
                    assert(results["success"])

    @pytest.mark.skipif((pkg_resources.get_distribution("ipinfo").version <= "1.0.3" and sys.version_info < (3, 6)),
                        reason="Tests currently fail on 2 with ipinfo>=1.0.3")
    @pytest.mark.parametrize("ipinfo_query_ip, expected_results", [
        ("8.8.8.8", {"value": "xyz"})
    ],ids=['Google-DNS'])
    def test_ip_address_removal(self, circuits_app, ipinfo_query_ip, expected_results):
        """ Test calling with sample values for the parameters """
        # Import ipinfo here to avoid py2 failure on test setup
        from ipinfo.handler import Handler
        import ipinfo

        function_params = {
            "ipinfo_query_ip": ipinfo_query_ip
        }
        # Patch the init of Handler class to prevent outside calls
        with patch.object(Handler, "__init__", lambda access_token: None) as mocked_handler:
            with patch.object(ipinfo, "getHandler",
                              lambda token: Handler()):
                # Patch getDetails with a mock of the return data
                with patch.object(Handler, "getDetails") as mock_get_details:
                    mock_get_details.return_value = mocked_ipinfo_call()
                    results = call_fn_ipinfo_query_ip_address_function(circuits_app, function_params)
                    assert (results["success"])
                    # Assert the IPAddress object is removed
                    assert (results.get("ipaddress", True))

    @pytest.mark.skipif((pkg_resources.get_distribution("ipinfo").version <= "1.0.3" and sys.version_info < (3, 6)),
                        reason="Tests currently fail on 2 with ipinfo==1.0.3")
    @pytest.mark.parametrize("ipinfo_query_ip, expected_results", [
        (u"8.8.8.8", {"value": "xyz"})
    ], ids=['Google-DNS'])
    def test_json_serialize(self, circuits_app, ipinfo_query_ip, expected_results):
        """ Test calling with sample values for the parameters """
        # Import ipinfo here to avoid py2 failure on test setup
        from ipinfo.handler import Handler
        import ipinfo

        function_params = {
            "ipinfo_query_ip": ipinfo_query_ip
        }
        # Patch the init of Handler class to prevent outside calls
        with patch.object(Handler, "__init__", lambda access_token: None) as mocked_handler:
            with patch.object(ipinfo, "getHandler",
                              lambda token: Handler()):
                # Patch getDetails with a mock of the return data
                with patch.object(Handler, "getDetails") as mock_get_details:
                    mock_get_details.return_value = mocked_ipinfo_call()
                    results = call_fn_ipinfo_query_ip_address_function(circuits_app, function_params)
                    assert (results["success"])
                    import json
                    # Assert we can serialize the JSON result, this wont be possible if 'ip_address' wasn't removed
                    assert(json.dumps(results))