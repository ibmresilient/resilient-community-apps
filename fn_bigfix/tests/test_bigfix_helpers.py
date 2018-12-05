# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
"""Test Bigfix helper functions"""
from __future__ import print_function
from mock import patch
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
import pytest
from fn_bigfix.lib.bigfix_helpers import *
from  mock_artifacts import mocked_bigfix_client
from  mock_artifacts import get_artifact_data_1, get_artifact_data_2

"""
Suite of tests to test BigFix Helper functions
"""

def assert_keys_in(json_obj, *keys):
    for key in keys:
        assert key in json_obj

class Func(object):
    def __init__(self, options={}):
        self.options = options

class TestBigFixHelpersGetHits:
    """ Test for get_hits using mocked data.  """
    @pytest.mark.parametrize("artifact_data, params, expected_results_1, expected_results_2", [
        (get_artifact_data_1(), {"incident_id": 12345,"artifact_id": 6789 }, 2, 1),
        (get_artifact_data_2(), {"incident_id": 23456, "artifact_id": 7891}, 5, 2)
    ])
    def test_get_hits(self, artifact_data, params, expected_results_1, expected_results_2):

        hits = get_hits(artifact_data, params)
        assert (len(artifact_data)) == expected_results_1
        assert(len(hits)) == expected_results_2

class TestBigFixHelperPollActionStatus:
    """ Test for poll_action_status using mocked data.  """

    @pytest.mark.parametrize("result_type, bigfix_action_id, retry_interval, response_interval, retry_timeout, expected_results_1, expected_results_2", [
        ("success", 12345, 3, 5, 12, "OK", "The action executed successfully."),
        ("not_relevant", 12345, 3, 7, 12, "OK", "The Fixlet which this action addresses is not relevant on this machine."),
        ("failed", 12345, 3, 9, 12, "Failed", "The action failed."),
        ("timedout", 12345, 3, 13, 12, "Timedout", None),
    ])
    def test_poll_action_status(self, result_type, bigfix_action_id, retry_interval, response_interval, retry_timeout, expected_results_1, expected_results_2):
        """ Test create_attachment using mocked data.  """
        end_time = time.time() + response_interval

        (status, status_message) = poll_action_status(mocked_bigfix_client("get_bf_action_status", result_type, end_time), bigfix_action_id,
                                                      retry_interval, retry_timeout)
        assert status == expected_results_1
        assert status_message == expected_results_2


