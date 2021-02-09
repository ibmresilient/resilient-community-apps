# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
""" Test AWS GuardDuty poller class. """
from threading import Thread

from mock import patch, MagicMock
import pytest
from pytest_resilient_circuits.mocks import BasicResilientMock
from fn_aws_guardduty.lib.aws_gd_poller import *
import fn_aws_guardduty.util.config as config
from .mock_artifacts import *

LOG = logging.getLogger(__name__)
"""
Suite of tests to test AWS GuardDuty client class
"""
def get_config(**settings):
    config = {
        "aws_gd_access_key_id":    "AKAABBCCDDEEFFGGHH12",
        "aws_gd_secret_access_key": "pplXXEEK/aAbBcCdDeEfFgGhHiH1234567+sssss",
        "aws_gd_master_region":   "us-west-2",
        "aws_gd_polling_interval": 2,
        "aws_gd_regions": ".*",
    }
    for key, value in settings.items():
        if value:
            config[key] = value
    return config

def assert_keys_in(json_obj, *keys):
    for key in keys:
        assert key in json_obj

class TestAwsGdPoller:
    """Test AwsGdPoller"""

    @patch('fn_aws_guardduty.lib.aws_gd_cli_man.AwsGdClient', side_effect=mocked_gd_client)
    @patch('fn_aws_guardduty.lib.aws_gd_poller.ResSvc', side_effect=mocked_ResSvc)
    @pytest.mark.parametrize("aws_gd_regions_interval, aws_gd_polling_interval, expected_results", [
        (.1, .1, None),

    ])
    def test_run(self, mock_res, mock_cli, aws_gd_regions_interval, aws_gd_polling_interval, expected_results):
        aws_gd_poller = AwsGdPoller({}, get_config(aws_gd_regions_interval=aws_gd_regions_interval),
                                    aws_gd_polling_interval)
        thread = Thread(target=aws_gd_poller.run)
        thread.start()
        config.STOP_THREAD = False
        time.sleep(1)
        assert thread.isAlive()
        config.STOP_THREAD = True
        time.sleep(1)
        assert not thread.isAlive()

    @pytest.mark.parametrize("aws_gd_severity_threshold, aws_gd_lookback_interval, last_update, expected_results", [
        (None, None, None, {'Criterion': {'service.archived': {'Eq': ['false']}}}),
        (7, None, None, {'Criterion': {'service.archived': {'Eq': ['false']}, 'severity': {'Gte': 7}}}),
        (None, 2, None, None),
        (7, 2, None, 7),
        (None, None, dt.datetime.now(), None),
        (7, None, dt.datetime.now(), 7),
    ])
    def test_set_criteria(self, aws_gd_severity_threshold, aws_gd_lookback_interval, last_update, expected_results):

        aws_gd_poller = AwsGdPoller({}, get_config(aws_gd_severity_threshold=aws_gd_severity_threshold,
                                                   aws_gd_lookback_interval=aws_gd_lookback_interval), 2)
        if last_update:
            aws_gd_poller.last_update = last_update
        result = aws_gd_poller.set_criteria()
        if not aws_gd_lookback_interval and not last_update:
            assert result == expected_results
        else:
            assert isinstance(result["Criterion"]["updatedAt"]["Gte"], int)
            if aws_gd_severity_threshold:
                assert result["Criterion"]["severity"]["Gte"] == expected_results
