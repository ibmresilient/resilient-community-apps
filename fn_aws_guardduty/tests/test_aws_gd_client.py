# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
""" Test AWS GuardDuty client class. """
from mock import patch
import pytest
from fn_aws_guardduty.lib.aws_gd_client import *
from .mock_artifacts import *

LOG = logging.getLogger(__name__)
"""
Suite of tests to test AWS GuardDuty client class
"""

def get_config():
    return dict({
        "aws_gd_access_key_id":    "AKAABBCCDDEEFFGGHH12",
        "aws_gd_secret_access_key": "pplXXEEK/aAbBcCdDeEfFgGhHiH1234567+sssss",
        "aws_gd_master_region":   "us-west-2"
    })

class TestAWSGdClient:

    """ Test AwsGdClient object setup using mocked data.  """

    @pytest.mark.parametrize("service, expected_result", [
        (None, "botocore.client.GuardDuty object at "),
        ("ec2", "botocore.client.EC2 object at "),
    ])
    def test_aws_gd_obj(self,  service, expected_result):
        options = {}
        aws_cli_obj = AwsGdClient(options, get_config(), service_name=service,
                                  region=get_config()["aws_gd_master_region"])
        assert(expected_result in repr(aws_cli_obj.gd))

    """ Test aws_gd_client._get_client"""

    @pytest.mark.parametrize("service, expected_result", [
        ("guardduty", "botocore.client.GuardDuty object at "),
        ("ec2", "botocore.client.EC2 object at "),
    ])
    def test_get_client(self,  service, expected_result):
        options = {}
        aws_cli = AwsGdClient(options, get_config(), region=get_config()["aws_gd_master_region"])
        response = aws_cli._get_client(service)
        assert(expected_result in repr(response))

    """ Test aws_gd_client.__get_type_from_response"""

    @pytest.mark.parametrize("op, type_list, expected_result", [
        ("get_findings", SUPPORTED_GET_TYPES, "Findings"),
        ("describe_regions", SUPPORTED_GET_TYPES, "Regions"),
        ("list_detectors", SUPPORTED_PAGINATE_TYPES, "DetectorIds"),
        ("list_findings", SUPPORTED_PAGINATE_TYPES, "FindingIds")
    ])
    def test_get_type_from_response(self, op, type_list, expected_result):
        options = {}

        gd_cli = AwsGdClient(options, get_config(), region=get_config()["aws_gd_master_region"])
        response = gd_cli._get_type_from_response(get_cli_raw_responses(op), type_list)
        assert(expected_result in repr(response))

    """ Test aws_gd_client.__get_type_from_response negative case"""

    @pytest.mark.parametrize("op, type_list, expected_result", [
        ("get_findings", SUPPORTED_PAGINATE_TYPES, "No supported type for integration found in AWS GuardDuty response")
    ])
    def test_get_type_from_response_err(self, op, type_list, expected_result):
        options = {}

        aws_cli = AwsGdClient(options, get_config(), region=get_config()["aws_gd_master_region"])
        with pytest.raises(ValueError) as e:
            response = aws_cli._get_type_from_response(get_cli_raw_responses(op), type_list)
        assert str(e.value) == expected_result

    """ Test aws_gd_client.paginate"""
    @patch('botocore.client.BaseClient.get_paginator', side_effect=mocked_client_paginator)
    @pytest.mark.parametrize("op, expected_result", [
        ("list_detectors", get_cli_raw_responses("list_detectors")["DetectorIds"])
    ])
    def test_paginate(self, mock_paginator, op, expected_result):
        options = {}

        gd_cli = AwsGdClient(options, get_config(), region=get_config()["aws_gd_master_region"])
        response = gd_cli.paginate(op)
        assert (expected_result == response)

    """ Test aws_gd_client.get"""
    @patch('fn_aws_guardduty.lib.aws_gd_client.AwsGdClient._get_client', side_effect=mocked_get_client)
    @pytest.mark.parametrize("op, expected_result", [
        ("get_findings", get_cli_raw_responses("get_findings")["Findings"])
    ])
    def test_get(self, mock_gd, op, expected_result):
        options = {}

        gd_cli = AwsGdClient(options, get_config(), region=get_config()["aws_gd_master_region"])
        response = gd_cli.get(op)
        assert (expected_result == response)
