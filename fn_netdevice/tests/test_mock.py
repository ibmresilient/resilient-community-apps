# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""
# Copyright IBM Corp. - Confidential Information
from __future__ import print_function
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

"""
pytest --resilient_app_config=/<user>/<path>/resilient-community-apps/fn_netdevice/tests/data/app.config tests/test_mock.py
"""

PACKAGE_NAME = "fn_netdevice"
FUNCTION_NAME = "fn_netdevice_query"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_netdevice_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("fn_netdevice_query", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("fn_netdevice_query_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestNetMiko:
    """ Tests for the ioc_parser function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.parametrize("netdevice_ids, netdevice_send_cmd, netdevice_config_cmd,  netdevice_use_textfsm, expected_results", [
        ('', 'ls', None, False, {"value": "xyz"})
    ])
    def test_no_section(self, circuits_app,
                     netdevice_ids, netdevice_send_cmd, netdevice_config_cmd, netdevice_use_textfsm,
                     expected_results):
        """ Test calling with sample values for the parameters """
        function_params = {
            "netdevice_ids": netdevice_ids,
            "netdevice_send_cmd": netdevice_send_cmd,
            "netdevice_config_cmd": netdevice_config_cmd,
            "netdevice_use_textfsm": netdevice_use_textfsm
        }
        results = call_netdevice_function(circuits_app, function_params)
        assert(results['success'] == False)

    @pytest.mark.parametrize("netdevice_ids, netdevice_send_cmd, netdevice_config_cmd,  netdevice_use_textfsm, expected_results", [
        ('ansible-linux', None, None, False, {"value": "xyz"}),
        ('ansible-linux', None, None, True, {"value": "xyz"})
    ])
    def test_failure_exceptions(self, circuits_app,
                  netdevice_ids, netdevice_send_cmd, netdevice_config_cmd, netdevice_use_textfsm,
                  expected_results):
        """ Test calling with sample values for the parameters """
        function_params = {
            "netdevice_ids": netdevice_ids,
            "netdevice_send_cmd": netdevice_send_cmd,
            "netdevice_config_cmd": netdevice_config_cmd,
            "netdevice_use_textfsm": netdevice_use_textfsm
        }

        with pytest.raises(Exception) as e_info:
            results = call_netdevice_function(circuits_app, function_params)

    @pytest.mark.parametrize("netdevice_ids, netdevice_send_cmd, netdevice_config_cmd,  netdevice_use_textfsm, expected_results", [
        ('ansible-linux', 'df', None, False,
        'Filesystem              1K-blocks   Used Available Use% Mounted on\n/dev/mapper/centos-root   6486016 935832   5550184  15%/\n'
        )
    ])
    def test_failure_success(self, circuits_app,
                                netdevice_ids, netdevice_send_cmd, netdevice_config_cmd, netdevice_use_textfsm,
                                expected_results):
        """ Test calling with sample values for the parameters """
        function_params = {
            "netdevice_ids": netdevice_ids,
            "netdevice_send_cmd": netdevice_send_cmd,
            "netdevice_config_cmd": netdevice_config_cmd,
            "netdevice_use_textfsm": netdevice_use_textfsm
        }

        results = call_netdevice_function(circuits_app, function_params)
        assert (results['success'] == True)
        assert (results['content']['ansible-linux']['status'] == 'success')
        assert (results['content']['ansible-linux']['send_command'] == netdevice_send_cmd)
        assert (results['content']['ansible-linux']['send_result'][0:30] == expected_results[0:30])
