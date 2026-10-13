# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from mock import patch

from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from mock_artifacts import mocked_pptr_client, get_mock_config

PACKAGE_NAME = "fn_proofpoint_trap"
FUNCTION_NAME = "fn_proofpoint_trap_get_list_members"

# Read the mocked configuration-data section.
config_data = get_mock_config()

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"

def assert_keys_in(json_obj, *keys):
    for key in keys:
        assert key in json_obj

def assert_value_not_none(json_obj, *keys):
    for key in keys:
        assert json_obj[key] is not None

def call_fn_proofpoint_trap_get_list_members_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("fn_proofpoint_trap_get_list_members", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("fn_proofpoint_trap_get_list_members_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestFnProofpointTrapGetListMembers:
    """ Tests for the fn_proofpoint_trap_get_list_members function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @patch('fn_proofpoint_trap.components.fn_proofpoint_trap_get_list_members.PPTRClient', side_effect=mocked_pptr_client)
    @pytest.mark.parametrize("trap_list_id, trap_members_type, trap_member_id, expected_results", [
        (1, 'members.json', None, None)
    ])
    def test_success(self, mock_get, circuits_app, trap_list_id, trap_members_type, trap_member_id, expected_results):
        """ Test calling with sample values for the parameters """

        keys = ["content", "inputs", "metrics", "raw", "reason", "success", "version"]
        keys_host_1 = ["created_at", "deleted", "description", "enabled", "expiration", "host",
                     "host_id", "id", "list_id", "updated_at"]
        keys_host_2 = ["hash_reputation_id", "response_id", "reverse_user_id", "user_id"]
        function_params = { 
            "trap_list_id": trap_list_id,
            "trap_members_type": trap_members_type,
            "trap_member_id": trap_member_id
        }
        results = call_fn_proofpoint_trap_get_list_members_function(circuits_app, function_params)
        assert_keys_in(results, *keys)
        content = results["content"]
        for host in content:
            assert_keys_in(host, *keys_host_1)
            assert_keys_in(host, *keys_host_2)
            assert_value_not_none(host, *keys_host_1)
