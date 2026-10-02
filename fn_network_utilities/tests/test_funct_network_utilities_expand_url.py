# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_network_utilities"
FUNCTION_NAME = "network_utilities_expand_url"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_network_utilities_expand_url_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("network_utilities_expand_url", function_params)

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
        event = circuits.watcher.wait("network_utilities_expand_url_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value


class TestnetworkUtilitiesExpandUrl:
    """ Tests for the network_utilities_expand_url function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.livetest
    @pytest.mark.parametrize("resilient_url, expected_results", [
        ("https://tinyurl.com/y8u79w5g",
         {"urllist": ['https://developer.ibm.com/security/resilient/', 
                      'https://community.ibm.com/community/user/communities/community-home',
                      'https://login.ibm.com/oidc/endpoint/default/authorize', 
                      'https://login.ibm.com/oidc/sps/auth']}),
        ("tinyurl.com/y8u79w5g",
         {"urllist": ['https://developer.ibm.com/security/resilient/', 
                      'https://community.ibm.com/community/user/communities/community-home',
                      'https://login.ibm.com/oidc/endpoint/default/authorize', 
                      'https://login.ibm.com/oidc/sps/auth']}),
        ("https://tinyurl.com/means_nothing", {"urllist": []}),
        ("https://doesnt_exist.com", {"urllist": []})
    ])
    def test_success(self, circuits_app, resilient_url, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = {
            "network_utilities_resilient_url": resilient_url
        }
        results = call_network_utilities_expand_url_function(circuits_app, function_params)

        for i, url in enumerate(results["urllist"]):
            assert url.startswith(expected_results["urllist"][i])