# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
""" Test AWS GuardDuty Resilient service. """
import types
from mock import patch, MagicMock, Mock
import pytest
from pytest_resilient_circuits.mocks import BasicResilientMock
from fn_aws_guardduty.lib.resilient_service import *
from .mock_artifacts import *
"""
Suite of tests to test AWS GuardDuty Resilient service class
"""
def get_config(**settings):
    config = {
        "aws_gd_access_key_id":    "AKAABBCCDDEEFFGGHH12",
        "aws_gd_secret_access_key": "pplXXEEK/aAbBcCdDeEfFgGhHiH1234567+sssss",
    }
    for key, value in settings.items():
        config[key] = value
    return config

def get_opt(**settings):
    opt = {
        "email":    "email=a@a.com",
        "password": "password"
    }
    for key, value in settings.items():
        opt[key] = value
    return opt

class TestResilientService:
    """Test get_data_at_path function"""

    @patch('fn_aws_guardduty.lib.resilient_service.ResilientComponent.rest_client', side_effect=MagicMock)
    @pytest.mark.parametrize("expected_results", [
        None
    ])
    def test_setup(self, mock_res, expected_results):
        mock_res.names = ("MagicMock",)
        res_svc =  ResSvc(get_opt(), get_config())
        assert isinstance(res_svc, (ResSvc, ResilientComponent))

    @patch('fn_aws_guardduty.lib.resilient_service.ResilientComponent.rest_client', side_effect=MagicMock)
    @pytest.mark.parametrize("finding, region, f_fields, expected_results", [
        (get_cli_raw_responses("get_findings")["Findings"][0], "us-west-2", ["Id", "DetectorId"], None),
        (get_cli_raw_responses("get_findings")["Findings"][0], "us-west-1", ["Id", "DetectorId"], None),
    ])
    def test_find_resilient_incident_for_req(self, mock_res, finding, region, f_fields, expected_results):
        mock_res.names = ("MagicMock",)
        res_svc = ResSvc(get_opt(), get_config())
        assert isinstance(res_svc, (ResSvc, ResilientComponent))
        result = res_svc.find_resilient_incident_for_req(finding, region, f_fields)
        assert isinstance(result, MagicMock)
        assert "mock.post()" in str(result)

    @patch('fn_aws_guardduty.lib.resilient_service.ResilientComponent.rest_client', side_effect=MagicMock)
    @pytest.mark.parametrize("data, expected_results", [
        (get_function_params("data"), None)
    ])
    def test_create_incident(self, mock_res, data, expected_results):
        mock_res.names = ("MagicMock",)
        res_svc = ResSvc(get_opt(), get_config())
        assert isinstance(res_svc, (ResSvc, ResilientComponent))
        result = res_svc.create_incident(data)
        assert isinstance(result, MagicMock)
        assert "mock.post()" in str(result)

    @patch('fn_aws_guardduty.lib.resilient_service.ResilientComponent.rest_client', side_effect=MagicMock)
    @pytest.mark.parametrize("incident_id, tables, expected_results", [
        (2000, get_function_params("tables"), None)
    ])
    def test_add_datatables(self, mock_res, incident_id, tables, expected_results):
        mock_res.names = ("MagicMock",)
        res_svc = ResSvc(get_opt(), get_config())
        assert isinstance(res_svc, (ResSvc, ResilientComponent))
        result = res_svc.add_datatables(incident_id, tables)
        assert result is None

    @patch('fn_aws_guardduty.lib.resilient_service.ResilientComponent.rest_client', side_effect=MagicMock)
    @pytest.mark.parametrize("incident_id, tables, expected_results", [
        (2000, get_function_params("tables"), None)
    ])
    def test_add_datatables(self, mock_res, incident_id, tables, expected_results):
        mock_res.names = ("MagicMock",)
        res_svc = ResSvc(get_opt(), get_config())
        assert isinstance(res_svc, (ResSvc, ResilientComponent))
        result = res_svc.find_resilient_artifacts_for_incident(incident_id)
        assert isinstance(result, dict)
        assert not result

    @patch('fn_aws_guardduty.lib.resilient_service.ResilientComponent.rest_client', side_effect=MagicMock)
    @pytest.mark.parametrize("incident_id, note, tables, expected_results", [
        (2000, get_function_params("tables"), None,  None)
    ])
    def test_add_comment(self, mock_res, incident_id, note, tables, expected_results):
        mock_res.names = ("MagicMock",)
        res_svc = ResSvc(get_opt(), get_config())
        assert isinstance(res_svc, (ResSvc, ResilientComponent))
        result = res_svc.add_comment(incident_id, note)
        assert isinstance(result, MagicMock)


    @patch('fn_aws_guardduty.lib.resilient_service.ResilientComponent.rest_client', side_effect=MagicMock)
    @pytest.mark.parametrize("region, f_fields, expected_results", [
        ("us-west-2", ["Id", "DetectorId"], None)
    ])
    def test_page_incidents(self, mock_res, region, f_fields, expected_results):
        mock_res.names = ("MagicMock",)
        res_svc = ResSvc(get_opt(), get_config())
        assert isinstance(res_svc, (ResSvc, ResilientComponent))
        result = res_svc.page_incidents(region=region, f_fields=f_fields)
        assert isinstance(result, types.GeneratorType)