# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import datetime
import pytest
import pytz
from resilient_circuits.util import get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from fn_rsa_netwitness.util.helper import get_headers, convert_to_nw_time


PACKAGE_NAME = "fn_rsa_netwitness"
FUNCTION_NAME = "netwitness_query"

# Read the default configuration-data section from the package
# config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_netwitness_query_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("netwitness_query", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("netwitness_query_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestNetwitnessQuery:
    """ Tests for the netwitness_query function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.livetest
    @pytest.mark.parametrize("nw_query, nw_results_size, expected_results", [
        ("select sessionid where time='2019-Feb-26 "\
            "08:00:00'-'2019-Feb-27 08:00:00'", 10, {"value": "xyz"})
        # expected_results doesn't matter in this case since this
        # is going to just check that a value exists
    ])
    def test_success(self, circuits_app, nw_query, nw_results_size, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = {
            "nw_query": nw_query,
            "nw_results_size": nw_results_size
        }
        results = call_netwitness_query_function(circuits_app, function_params)
        # Assert content is returned, TODO improve tests
        assert results.get("content") is not None

    def test_get_headers(self):
        expected_headers = {
            "Authorization": "Basic dXNlcm5hbWU6cGFzc3dvcmQ=",
            "Content-Type": "application/x-www-form-urlencoded",
            "Cache-Control": "no-cache"
        }
        headers = get_headers("username", "password")

        assert headers == expected_headers

    def test_convert_to_nw_time(self):
        expected_nw_time = "2018-Dec-18 13:28:45"
        nw_time = datetime.datetime.strptime(convert_to_nw_time(1545157725000),\
            '%Y-%b-%d %H:%M:%S')
        nw_time_timezone = nw_time.astimezone(pytz.timezone("America/New_York"))\
            .strftime('%Y-%b-%d %H:%M:%S')

        assert nw_time_timezone == expected_nw_time
