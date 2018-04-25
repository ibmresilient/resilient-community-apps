# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from mock import patch

from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from  mock_umbrella import  mocked_response

PACKAGE_NAME = "fn_cisco_umbrella_inv"
FUNCTION_NAME = "umbrella_domain_co_occurrences"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"

def assert_keys_in(json_obj, *keys):
    for key in keys:
        assert key in json_obj

def call_umbrella_domain_co_occurrences_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("umbrella_domain_co_occurrences", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("umbrella_domain_co_occurrences_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestUmbrellaDomainCoOccurrences:
    """ Tests for the umbrella_domain_co_occurrences function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @patch('investigate.Investigate.get', side_effect=mocked_response)
    @pytest.mark.parametrize("umbinv_domain", [
        ("domain.com")
    ])
    def test_co_occurrences(self, mock_get, circuits_app, umbinv_domain):
        """ Test domain_co_occurrences using mocked response. """

        keys = ["domain_name", "found", "pfs2"]
        function_params = {
            "umbinv_domain": umbinv_domain
        }
        results = call_umbrella_domain_co_occurrences_function(circuits_app, function_params)
        domain_co_occurrences = results["cooccurrences"]
        assert_keys_in(domain_co_occurrences, *keys)