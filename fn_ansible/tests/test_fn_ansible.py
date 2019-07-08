# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_ansible"
FUNCTION_NAME = "fn_ansible"

# The default configuration-data section from the package
config_data = """[fn_ansible]
runner_dir=/Users/markscherfling/ansible/
artifact_dir=/tmp/artifacts
"""

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)

resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_fn_ansible_function(circuits, function_params, timeout=20):
    # Fire a message to the function
    evt = SubmitTestFunction("fn_ansible", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("fn_ansible_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value



class TestFnAnsible:
    """ Tests for the function_ansible function"""

    TARGET_HOST = "192.168.1.3"

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    inputs = { 
            "ansible_playbook_name": "playbook1",
            "ansible_parameters": "host_names={}".format(TARGET_HOST)
        }

    output = {TARGET_HOST: {'ok': 1, 'failures': 0, 'unreachable': 0, 'changed': 0, 'skipped': 0}}

    @pytest.mark.parametrize("inputs, expected_results", [(inputs, output)])
    def test_success(self, circuits_app, inputs, expected_results):
        """ Test calling with sample values for the parameters """
        results = call_fn_ansible_function(circuits_app, inputs)
        assert(expected_results == results)