# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_phish_ai"
FUNCTION_NAME = "phish_ai_get_report"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_phish_ai_get_report_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("phish_ai_get_report", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("phish_ai_get_report_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestPhishAiGetReport:
    """ Tests for the phish_ai_get_report function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.parametrize("phishai_scan_id, expected_results", [
        ("3QEQuLnFUNpfnJLgCmH8", {"status": "completed", "domain": "google.com", "target": "unknown", "title": "google", "url": "https://google.com", "plan": "free", "tld": "com", "verdict": "clean", "user_agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36", "time": "2018-12-07T02:14:29.105Z", "iso_code": "US", "first_seen": "2018-05-24T10:13:07.736Z", "ip_address": "209.85.147.113", "asn": 15169, "user_email": "api", "user": "free-api"}),
        ("gGBSaVvlN5qc5PcwvnuT", {"status": "completed", "domain": "startup417.gb.net", "user_agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36", "target": "Microsoft", "title": "sign_in_to_your_microsoft_account", "url": "https://startup417.gb.net/M3?mes1=asdf@asdf.com", "time": "2018-12-06T22:39:34.210Z", "verdict": "malicious", "plan": "free", "tld": "net", "iso_code": "US", "first_seen": "2018-12-06T19:16:20.825Z", "ip_address": "104.24.104.116", "asn": 13335, "user_email": "api", "user": "free-api"})
    ])
    def test_success(self, circuits_app, phishai_scan_id, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = { 
            "phishai_scan_id": phishai_scan_id
        }
        results = call_phish_ai_get_report_function(circuits_app, function_params)
        assert expected_results == results["content"]
