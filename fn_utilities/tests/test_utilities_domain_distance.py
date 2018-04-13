# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from pytest_resilient_circuits import verify_subset

PACKAGE_NAME = "fn_utilities"
FUNCTION_NAME = "utilities_domain_distance"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_domain_distance_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction(FUNCTION_NAME, function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("{}_result".format(FUNCTION_NAME), parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestDomainDistance:
    """ Tests for the domain_distance function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

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
        ("xn--ple-5cd5f.com", "apple.com", {"closest": {"name": "apple.com", "distance": 0}})
    ])
    def test_success(self, circuits_app, domain_name, domain_list, expected_result):
        """ Test calling with sample values for the parameters """
        function_params = { 
            "domain_name": domain_name,
            "domain_list": domain_list
        }
        result = call_domain_distance_function(circuits_app, function_params)

        import logging
        logging.getLogger(__name__).info(expected_result)
        logging.getLogger(__name__).info(result)

        verify_subset(expected_result, result)
        # assert(expected_result == result)