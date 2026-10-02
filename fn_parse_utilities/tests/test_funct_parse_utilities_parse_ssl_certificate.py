# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from tests.mock_artifact import ArtifactMock
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from pytest_resilient_circuits import verify_subset

PACKAGE_NAME = "fn_parse_utilities"
FUNCTION_NAME = "parse_utilities_parse_ssl_certificate"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = ArtifactMock

def call_parse_utilities_parse_ssl_certificate_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("parse_utilities_parse_ssl_certificate", function_params)

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
        event = circuits.watcher.wait("parse_utilities_parse_ssl_certificate_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value


class TestParseUtilitiesParseSslCertificate:
    """ Tests for the parse_utilities_parse_ssl_certificate function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.parametrize("artifact_id, certificate, incident_id, expected_results", [
        (6, "text", 2095, {"expiration_status": "Valid"}),
        (7, "text", 2095, {"expiration_status": "Expired"})
    ])
    def test_success(self, circuits_app, artifact_id, certificate, incident_id, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = {
            "parse_utilities_artifact_id": artifact_id,
            "parse_utilities_certificate": certificate,
            "parse_utilities_incident_id": incident_id
        }
        results = call_parse_utilities_parse_ssl_certificate_function(circuits_app, function_params)
        verify_subset(expected_results, results)
