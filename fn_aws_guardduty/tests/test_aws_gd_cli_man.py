# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
""" Test AWS GuardDuty client manager. """
from mock import patch
import pytest
from fn_aws_guardduty.lib.aws_gd_cli_man import *
from .mock_artifacts import *

LOG = logging.getLogger(__name__)
"""
Suite of tests to test AWS GuardDuty client manager class
"""
def get_config(**settings):
    config = {
        "aws_gd_access_key_id":    "AKAABBCCDDEEFFGGHH12",
        "aws_gd_secret_access_key": "pplXXEEK/aAbBcCdDeEfFgGhHiH1234567+sssss",
        "aws_gd_master_region":   "us-west-2",
        "aws_gd_regions": ".*",
        "aws_gd_polling_interval": 2
    }
    for key, value in settings.items():
        config[key] = value
    return config

def assert_keys_in(json_obj, *keys):
    for key in keys:
        assert key in json_obj

def assert_attribs_in(json_obj, *attribs):
    for attrib in attribs:
        assert hasattr(json_obj, attrib)

class TestAwsGdCliMan:
    """Test get_data_at_path function"""

    @patch('fn_aws_guardduty.lib.aws_gd_cli_man.AwsGdClient', side_effect=mocked_gd_client)
    @pytest.mark.parametrize("aws_gd_regions, expected_results", [
        (".*", [16, ["f2baedb0ac74f8f42fc929e15f56da6a"]]),
        ("^(us|eu).*", [9, ["f2baedb0ac74f8f42fc929e15f56da6a"]]),
        ("eu", [5, ["f2baedb0ac74f8f42fc929e15f56da6a"]]),
        ("eu-west-2", [1, ["f2baedb0ac74f8f42fc929e15f56da6a"]]),
    ])
    def test_setup(self, mock_cli, aws_gd_regions, expected_results):
        attribs = ["aws_gd_master_region", "aws_gd_regions", "clients", "function_opts", "opts", "proxies", "timestamp"]
        result = AwsGdCliMan({}, get_config(aws_gd_regions=aws_gd_regions))
        assert_attribs_in(result, *attribs)
        assert len(result.clients) == expected_results[0]
        for region, cli in  result.clients.items():
            assert cli["detectors"] == expected_results[1]

    @patch('fn_aws_guardduty.lib.aws_gd_cli_man.AwsGdClient', side_effect=mocked_gd_client)
    @pytest.mark.parametrize("aws_gd_regions, expected_results", [
        (None, "'aws_gd_regions' is mandatory and is not set. You must set this value to run this function")
    ])
    def test_setup_missing_regions_setting(self, mock_cli, aws_gd_regions, expected_results):
        with pytest.raises(ValueError) as e:
            result = AwsGdCliMan({}, get_config(aws_gd_regions=aws_gd_regions))
        assert str(e.value) == expected_results

    @patch('fn_aws_guardduty.lib.aws_gd_cli_man.AwsGdClient', side_effect=mocked_gd_client)
    @pytest.mark.parametrize("aws_gd_regions, aws_gd_regions_new, expected_results", [
        ("NotExists", ".*", [0, 16])
    ])
    def test_get_clients(self, mock_cli, aws_gd_regions, aws_gd_regions_new, expected_results):
        aws_gd_man = AwsGdCliMan({}, get_config(aws_gd_regions=aws_gd_regions))
        assert len(aws_gd_man.clients) == expected_results[0]
        aws_gd_man.aws_gd_regions = aws_gd_regions_new
        aws_gd_man._get_clients()
        assert len(aws_gd_man.clients) == expected_results[1]

    @patch('fn_aws_guardduty.lib.aws_gd_cli_man.AwsGdClient', side_effect=mocked_gd_client)
    @pytest.mark.parametrize("aws_gd_regions, aws_gd_regions_new, expected_results", [
        ("NotExists", ".*", [0, 16])
    ])
    def test_refresh_clients(self, mock_cli, aws_gd_regions, aws_gd_regions_new, expected_results):
        aws_gd_man = AwsGdCliMan({}, get_config(aws_gd_regions=aws_gd_regions))
        assert len(aws_gd_man.clients) == expected_results[0]
        assert len(aws_gd_man.available_regions) == expected_results[0]
        aws_gd_man.aws_gd_regions = aws_gd_regions_new
        aws_gd_man.refresh_clients()
        assert len(aws_gd_man.clients) == expected_results[1]
        assert len(aws_gd_man.available_regions) == expected_results[1]
        for gd_region, gd_client_info in aws_gd_man.clients.items():
            assert gd_client_info.get("is_new", False) == True

    @patch('fn_aws_guardduty.lib.aws_gd_cli_man.AwsGdClient', side_effect=mocked_gd_client)
    @pytest.mark.parametrize("expected_results", [
        ((get_cli_raw_responses("describe_regions")["Regions"]))
    ])
    def test_get_regions(self, mock_cli, expected_results):
        expected_results = [region['RegionName'] for region in expected_results]
        aws_gd_man = AwsGdCliMan({}, get_config())
        result = aws_gd_man.get_regions()
        assert len(result) == len(expected_results)
        assert sorted(result) == sorted(expected_results)
