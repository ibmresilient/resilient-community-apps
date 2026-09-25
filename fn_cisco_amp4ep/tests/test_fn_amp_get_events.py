# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from mock import patch
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from mock_artifacts import mocked_amp_client, get_mock_config

PACKAGE_NAME = "fn_cisco_amp4ep"
FUNCTION_NAME = "fn_amp_get_events"

# Read the default configuration-data section from the package
config_data = get_mock_config()

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"

def assert_keys_in(json_obj, *keys):
    for key in keys:
        assert key in json_obj

def call_fn_amp_get_events_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("fn_amp_get_events", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("fn_amp_get_events_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestFnAmpGetEvents:
    """ Tests for the fn_amp_get_events function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @patch('fn_cisco_amp4ep.components.fn_amp_get_events.Ampclient', side_effect=mocked_amp_client)
    @pytest.mark.parametrize("amp_detection_sha256, amp_application_sha256, amp_conn_guid, amp_group_guid, "
                             " amp_start_date, amp_event_type, amp_limit, amp_offset, amp_severity, expected_results_1, "
                             "expected_results_2, expected_results_3", [
        (None, None, None, None, None, None, None, None, None, "v1.2.0", 1, "WIN-S1AC1PI6L5L"),
        (None, None, None, None, None, None, None, None, "High", "v1.2.0", 1, "WIN-S1AC1PI6L5L"),
        (None, None, None, None, None, "1090519054,1090519084", None, None, "v1.2.0", 1, "WIN-S1AC1PI6L5L")
    ])
    def test_success(self, mock_get, circuits_app, amp_detection_sha256, amp_application_sha256, amp_conn_guid, amp_group_guid,
                     amp_start_date, amp_event_type, amp_limit, amp_offset, amp_severity, expected_results_1,
                     expected_results_2, expected_results_3):
        """ Test calling with sample values for the parameters """

        keys = ["response", "query_execution_time"]
        keys_e = ["data", "metadata"]
        keys_e_d_0 = ["computer", "date", "detection_id", "event_type", "event_type_id", "file",
                  "group_guids", "id", "timestamp", "timestamp_nanoseconds" ]

        function_params = {
            "amp_detection_sha256": amp_detection_sha256,
            "amp_application_sha256": amp_application_sha256,
            "amp_conn_guid": amp_conn_guid,
            "amp_group_guid": amp_group_guid,
            "amp_start_date": amp_start_date,
            "amp_event_type": amp_event_type,
            "amp_limit": amp_limit,
            "amp_offset": amp_offset
        }
        results = call_fn_amp_get_events_function(circuits_app, function_params)
        assert expected_results_1 == results["response"]["version"]
        assert_keys_in(results, *keys)
        assert(expected_results_2 == len(results["response"]["data"]))
        events = results["response"]
        assert_keys_in(events, *keys_e)
        data = results["response"]["data"]
        assert_keys_in(data[0], *keys_e_d_0)
        assert expected_results_3 == data[0]["computer"]["hostname"]

class TestFnAmpGetEvents:
    """ Tests for the fn_amp_get_events function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @patch('fn_cisco_amp4ep.components.fn_amp_get_events.Ampclient', side_effect=mocked_amp_client)
    @pytest.mark.parametrize("amp_detection_sha256, amp_application_sha256, amp_conn_guid, amp_group_guid, "
                             " amp_start_date, amp_event_type, amp_limit, amp_offset, expected_results_1, "
                             "expected_results_2, expected_results_3", [
        (None, None, None, None, None, None, None, None, "v1.2.0", 1, "WIN-S1AC1PI6L5L")
    ])
    def test_success(self, mock_get, circuits_app, amp_detection_sha256, amp_application_sha256, amp_conn_guid, amp_group_guid,
                     amp_start_date, amp_event_type, amp_limit, amp_offset, expected_results_1,
                     expected_results_2, expected_results_3):
        """ Test calling with sample values for the parameters """

        keys = ["response", "query_execution_time"]
        keys_e = ["data", "metadata"]
        keys_e_d_0 = ["computer", "date", "detection_id", "event_type", "event_type_id", "file",
                  "group_guids", "id", "timestamp", "timestamp_nanoseconds" ]

        function_params = {
            "amp_detection_sha256": amp_detection_sha256,
            "amp_application_sha256": amp_application_sha256,
            "amp_conn_guid": amp_conn_guid,
            "amp_group_guid": amp_group_guid,
            "amp_start_date": amp_start_date,
            "amp_event_type": amp_event_type,
            "amp_limit": amp_limit,
            "amp_offset": amp_offset
        }
        results = call_fn_amp_get_events_function(circuits_app, function_params)
        assert expected_results_1 == results["response"]["version"]
        assert_keys_in(results, *keys)
        assert(expected_results_2 == len(results["response"]["data"]))
        events = results["response"]
        assert_keys_in(events, *keys_e)
        data = results["response"]["data"]
        assert_keys_in(data[0], *keys_e_d_0)
        assert expected_results_3 == data[0]["computer"]["hostname"]