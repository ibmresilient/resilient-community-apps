# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest, os, sys
from mock_attachment import AttachmentMock
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_utilities"
FUNCTION_NAME = "utilities_parse_ssl_certificate"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = AttachmentMock


def call_utilities_parse_ssl_certificate_function(circuits, function_params, timeout=30):
    # Fire a message to the function
    evt = SubmitTestFunction("utilities_parse_ssl_certificate", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("utilities_parse_ssl_certificate_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestUtilitiesParseSslCertificate:
    """ Tests for the utilities_parse_ssl_certificate function"""

    DATA_DIR = "data/ssl_certs"

    @pytest.mark.skipif(sys.version_info < (3, 6), reason="requires python3.6 or higher")
    @pytest.mark.livetest
    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.parametrize("artifact_id, utilities_certificate, incident_id, expected_results", [
        (1, "ssl_example.cert", 2095,  "Valid"),
        #(6, "text", 2095, {"expiration_status": "Expired"})
    ])
    @pytest.mark.livetest
    @pytest.mark.skipif(sys.version_info < (3, 6), reason="requires python3.6 or higher")
    def test_success(self, circuits_app, artifact_id, utilities_certificate, incident_id, expected_results):
        """ Test calling with sample values for the parameters """
        curr_dir = os.path.dirname(os.path.realpath(__file__))

        certificate = open(os.path.join(curr_dir, TestUtilitiesParseSslCertificate.DATA_DIR, utilities_certificate), mode="r").read()

        function_params = { 
            "artifact_id": artifact_id,
            "utilities_certificate": certificate,
            "incident_id": incident_id
        }

        results = call_utilities_parse_ssl_certificate_function(circuits_app, function_params)
        assert expected_results == results.get("expiration_status")