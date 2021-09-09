# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

import pytest
from mock import patch
from resilient_circuits import FunctionResult, SubmitTestFunction
from resilient_circuits.util import get_function_definition

PACKAGE_NAME = "fn_grpc_interface"
FUNCTION_NAME = "function_grpc"

# Read the default configuration-data section from the package
config_data = """[fn_grpc_interface]
interface_dir=fn_grpc_interface/tests/data/
grpc_channel=localhost:50051
grpc_function=helloworld:SayHello(HelloRequest)
helloworld=unary,None,None
"""

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_function_grpc_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("function_grpc", function_params)

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
        event = circuits.watcher.wait("function_grpc_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value


class TestFunctionGrpc:
    """ Tests for the function_grpc function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    mock_inputs_1 = {
        "grpc_function_data": "{\"name\": \"tester\"}"
    }
    expected_results_1 = {
        "content": {"message": "Hello, tester!"}, 
        "channel": "localhost:50051"
    }

    mock_inputs_2 = {
        "grpc_channel": "localhost:50051",
        "grpc_function": "helloworld:SayHello(HelloRequest)",
        "grpc_function_data": "{\"name\": \"Jon Snow\"}"
    }
    expected_results_2 = {
        "content": {"message": "Hello, Jon Snow!"}, 
        "channel": "localhost:50051"
    }

    @pytest.mark.livetest
    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (mock_inputs_1, expected_results_1),
        (mock_inputs_2, expected_results_2)
    ])
    def test_success(self, circuits_app, mock_inputs, expected_results):
        """ Test calling with sample values for the parameters """

        results = call_function_grpc_function(circuits_app, mock_inputs)
        assert(expected_results == results)
