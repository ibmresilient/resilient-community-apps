# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from resilient_circuits import FunctionResult, FunctionError

PACKAGE_NAME = "fn_docker"
FUNCTION_NAME = "docker_run_docker_container"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_docker_run_docker_container_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("docker_run_docker_container", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("docker_run_docker_container_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestDockerRunDockerContainer:
    """ Tests for the docker_run_docker_container function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None
