# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from pytest_resilient_circuits import verify_subset

PACKAGE_NAME = "fn_network_utilities"
FUNCTION_NAME = "network_utilities_domain_distance"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_network_utilities_domain_distance_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("network_utilities_domain_distance", function_params)

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
        event = circuits.watcher.wait("network_utilities_domain_distance_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value


class TestNetworkUtilitiesDomainDistance:
    """ Tests for the network_utilities_domain_distance function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.livetest
    @pytest.mark.parametrize("domain_name, domain_list, expected_result", [
        ("monday", "mOnday, mand0y, mondäy, xn--mondy-dra, tuesday", {
            "domain_name": "monday",
            "distances": {
                "mOnday": 1,
                "mand0y": 2,
                "mondäy": 1,
                "xn--mondy-dra": 1,
                "tuesday": 4
            },
            "closest": {
                "name": "mOnday",
                "distance": 1
            }
        }),
        (u"wikipedi\u0430.com", "wikipedia.com, wikipedia.org", {"closest": {"name": "wikipedia.com", "distance": 0}}),
        ("xn--e1awd7f.com", "epic.com", {"closest": {"name": "epic.com", "distance": 0}}),
        ("xn--ple-5cd5f.com", "apple.com", {"closest": {"name": "apple.com", "distance": 0}}),
        ("http://1bm.com", "ibm.com", {"closest": {"name": "ibm.com", "distance": 1}})
    ])
    def test_success(self, circuits_app, domain_name, domain_list, expected_result):
        """ Test calling with sample values for the parameters """
        function_params = {
            "network_utilities_domain_name": domain_name,
            "network_utilities_domain_list": domain_list
        }
        result = call_network_utilities_domain_distance_function(circuits_app, function_params)

        import logging
        logging.getLogger(__name__).info(expected_result)
        logging.getLogger(__name__).info(result)

        verify_subset(expected_result, result)
        assert(expected_result['closest']['name'] == result['closest']['name'])
        assert(expected_result['closest']['distance'] == result['closest']['distance'])