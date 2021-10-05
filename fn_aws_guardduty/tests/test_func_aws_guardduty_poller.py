# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
""" Test AWS GuardDuty poller. """

from __future__ import print_function
import pytest
from mock import patch, MagicMock
from resilient_circuits.util import get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from fn_aws_guardduty.components.func_aws_guardduty_poller import *
import fn_aws_guardduty.util.config as config
from .mock_artifacts import *

def get_opt(**settings):
    opt = {
        "fn_aws_guardduty": {
            "aws_gd_access_key_id":    "AKAABBCCDDEEFFGGHH12",
            "aws_gd_secret_access_key": "pplXXEEK/aAbBcCdDeEfFgGhHiH1234567+sssss",
            "aws_gd_master_region":   "us-west-2",
            "aws_gd_regions_interval": 1,
            "aws_gd_polling_interval": 1,
            "aws_gd_regions": ".*",
        },
        "email": "a@b.com",
        "password": "password",
        "pytest_poller": True,
    }
    for key, value in settings.items():
        if value:
            opt[key] = value
    return opt

class TestFuncAwsGuarddutyPoller:
    """Test get_data_at_path function"""

    @patch('fn_aws_guardduty.components.func_aws_guardduty_poller.ResilientComponent.rest_client', side_effect=MagicMock)
    @patch('fn_aws_guardduty.lib.aws_gd_cli_man.AwsGdClient', side_effect=mocked_gd_client)
    @patch('fn_aws_guardduty.lib.aws_gd_poller.ResSvc', side_effect=mocked_ResSvc)
    def test_run(self, mock_svc, mock_cli, mock_res):
        mock_res.names = ("MagicMock",)
        aws_gd_poller = FuncAwsGuarddutyPoller(get_opt())
        time.sleep(1)
        threads = [t for t in aws_gd_poller.threads if t.is_alive()]
        assert threads
        config.STOP_THREAD = True
        time.sleep(1)
        threads = [t for t in aws_gd_poller.threads if t.is_alive()]
        assert threads