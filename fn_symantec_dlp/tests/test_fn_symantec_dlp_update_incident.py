# -*- coding: utf-8 -*-
# Copyright © IBM Corporation 2010, 2019

"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
import mock 
from fn_symantec_dlp.lib.dlp_soap_client import DLPSoapClient

PACKAGE_NAME = "fn_symantec_dlp"
FUNCTION_NAME = "fn_symantec_dlp_update_incident"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_fn_symantec_dlp_update_incident_function(circuits, function_params, timeout=3):
    # Fire a message to the function
    evt = SubmitTestFunction("fn_symantec_dlp_update_incident", function_params)
    circuits.manager.fire(evt)
    # circuits will fire an "exception" event if an exception is raised in the FunctionComponent
    # return this exception if it is raised
    exception_event = circuits.watcher.wait("exception", parent=None, timeout=1)

    if exception_event is not False:
        exception = exception_event.args[1].args[1]
        raise exception
    event = circuits.watcher.wait("fn_symantec_dlp_update_incident_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value

@pytest.fixture(scope="module")
@mock.patch('zeep.Client')
def setup_mocked_dlp_connection(MockedZeep):
        return DLPSoapClient(app_configs={
            "sdlp_wsdl": "https://localhost:8443/",
            "sdlp_host": "https://localhost:8443/",
            "sdlp_username": "admin",
            "sdlp_password": "admin",
            "sdlp_savedreportid": 111,
            "sdlp_incident_endpoint": "urls"
        })
class TestFnSymantecDlpUpdateIncident:
    """ Tests for the fn_symantec_dlp_update_incident function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None
   

    @pytest.mark.parametrize("sdlp_update_payload, expected_results", [
        ({"type": "text", "content": "{\"note\":\"lll\",\"incident_id\":191}"}, {"value": "xyz"}),
        ({"type": "text", "content": "{\"incident_id\":191,\"status\":\"Closed\"}"}, {"value": "xyz"})
    ])
    def test_success(self, circuits_app, sdlp_update_payload, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = { 
            "sdlp_update_payload": sdlp_update_payload
        } 
        from resilient_lib import ResultPayload

        res_payload = ResultPayload("fn_symantec_dlp_update", **function_params)      
        with mock.patch.object(DLPSoapClient, 'update_incident_raw', return_value="200"):
            with mock.patch.object(DLPSoapClient, 'incident_status', return_value=['Closed', 'New']):
                results = call_fn_symantec_dlp_update_incident_function(circuits_app, function_params)
        expected_results = res_payload.done(success=True, content={})
        
        assert expected_results['inputs'] == results['inputs']
        assert expected_results['content'] == results['content']
        assert results['success']

    @pytest.mark.parametrize("sdlp_update_payload, expected_results", [
        ({"type": "text", "content": "{\"status\":\"Triage team\",\"incident_id\":191}"}, {"value": "xyz"}),
        ({"type": "text", "content": "{\"incident_id\":191,\"status\":\"Notarealstatus\"}"}, {"value": "xyz"}),
        ({"type": "text", "content": ""}, {"value": "xyz"})
    ])
    def test_failure_bad_status(self, circuits_app, sdlp_update_payload, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = { 
            "sdlp_update_payload": sdlp_update_payload
        }
        with pytest.raises(ValueError):        
            with mock.patch.object(DLPSoapClient, 'update_incident_raw', return_value="200"):
                with mock.patch.object(DLPSoapClient, 'incident_status', return_value=['Closed', 'New']):
                    results = call_fn_symantec_dlp_update_incident_function(circuits_app, function_params)
        

    