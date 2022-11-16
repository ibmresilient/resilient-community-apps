# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
"""Test Bigfix helper functions"""

from __future__ import print_function
import pytest
from time import time
from fn_bigfix.lib.bigfix_helpers import poll_action_status
from mock_artifacts import mocked_bigfix_client

"""Suite of tests to test BigFix Helper functions"""

class TestBigFixHelperPollActionStatus:
    """ Test for poll_action_status using mocked data. """

    @pytest.mark.parametrize("result_type, bigfix_action_id, retry_interval, response_interval, retry_timeout, expected_results_1, expected_results_2", [
        ("success", 12345, 3, 5, 12, "OK", "The action executed successfully."),
        ("not_relevant", 12345, 3, 7, 12, "OK",
         "The Fixlet which this action addresses is not relevant on this machine."),
        ("failed", 12345, 3, 9, 12, "Failed", "The action failed."),
        ("timedout", 12345, 3, 13, 12, "Timedout", None),
    ])
    def test_poll_action_status(self, result_type, bigfix_action_id, retry_interval, response_interval, retry_timeout, expected_results_1, expected_results_2):
        """ Test create_attachment using mocked data. """

        (status, status_message) = poll_action_status(mocked_bigfix_client(
            "get_bf_action_status", result_type, time() + response_interval), bigfix_action_id, retry_interval, retry_timeout)
        assert status == expected_results_1
        assert status_message == expected_results_2
