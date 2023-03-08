# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_rest_api"
FUNCTION_NAME = "rest_api"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"

def call_rest_api_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("rest_api", function_params)

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
        event = circuits.watcher.wait("rest_api_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value


class TestInternetUtilitiesCallRestApi:
    """ Tests for the rest_api function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.livetest
    @pytest.mark.parametrize("rest_method, rest_url, rest_headers, rest_body, rest_verify", [
        ('POST', "https://httpbin.org/post", 'Content-type: application/json; charset=UTF-8',
         "title: foo, body: ƱƲ, userId: 1", True)
    ])
    def test_success(self, circuits_app, rest_method, rest_url, rest_headers, rest_body, rest_verify):
        """ Test calling with sample values for the parameters """
        function_params = {
            "rest_api_method": rest_method,
            "rest_api_url": rest_url,
            "rest_api_headers": {'content': rest_headers},
            "rest_api_body": {'content': rest_body },
            "rest_api_verify": rest_verify
        }
        results = call_rest_api_function(circuits_app, function_params)
        def build_dict(rest_temp):
            temp_dict = {}
            if rest_temp is not None:
                lines = rest_temp.split(",")
                for line in lines:
                    keyval = line.strip().split(":", 1)
                    if len(keyval) == 2:
                        temp_dict[keyval[0].strip()] = keyval[1].strip()
            return temp_dict
        rest_body = build_dict(rest_body)
        results = build_dict(results['content']['json']['json'])
        assert(rest_body['title'] == results['title'])
        assert(rest_body['body'] == results['body'])
        assert(rest_body['userId'] == results['userId'])