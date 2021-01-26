# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
""" Test AWS GuardDuty poller class. """
import sys
from threading import Thread

from mock import patch, MagicMock
import pytest
from fn_aws_guardduty.lib.aws_gd_poller import *
from fn_aws_guardduty.util import const
import fn_aws_guardduty.util.config as config
from .mock_artifacts import *
LOG = logging.getLogger(__name__)
"""
Suite of tests to test finding paylaod class
"""
time_stamp = "2021-01-22 15:45:26"
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

def assert_attribs_in(json_obj, *attribs):
    for attrib in attribs:
        assert hasattr(json_obj, attrib)

class TestParseFinding:
    """Test ParseFinding class"""

    mock_inputs_1 = {
        "finding": get_cli_raw_responses("get_findings")["Findings"][0],
        "region": "us-west-2",
        "refresh": False,
        "existing_artifacts": get_resilient_responses("find_resilient_artifacts_for_incident_with_artifacts"),
    }

    expected_results_1_1 = get_mocked_results("finding_payload_with_artifacts")
    expected_results_1_2 = get_mocked_results("finding_payload_data_tables")
    expected_attribs_1 = ["payload", "data_tables"]

    mock_inputs_2 = {
        "finding": get_cli_raw_responses("get_findings")["Findings"][0],
        "region": "us-west-2",
        "refresh": True,
        "existing_artifacts": get_resilient_responses("find_resilient_artifacts_for_incident_no_artifacts"),
    }

    expected_results_2_1 = get_mocked_results("finding_payload_with_artifacts_with_refresh")
    expected_results_2_2 = get_mocked_results("finding_payload_data_tables")
    expected_attribs_2 = ["payload", "finding", "data_tables"]

    mock_inputs_3 = {
        "finding": get_cli_raw_responses("get_findings")["Findings"][0],
        "region": "us-west-2",
        "refresh": False,
        "existing_artifacts": [],
    }

    expected_results_3_1 = get_mocked_results("finding_payload_no_artifacts")
    expected_results_3_2 = get_mocked_results("finding_payload_data_tables")
    expected_attribs_3 = ["payload", "data_tables"]

    @pytest.mark.parametrize("mock_inputs, expected_results_1, expected_results_2, expected_attribs", [
        (mock_inputs_1, expected_results_1_1, expected_results_1_2, expected_attribs_1),
        (mock_inputs_2, expected_results_2_1, expected_results_2_2, expected_attribs_2),
        (mock_inputs_3, expected_results_3_1, expected_results_3_2, expected_attribs_3),
    ])
    def test_make_create_object(self, mock_inputs, expected_results_1, expected_results_2, expected_attribs):
        result =  ParseFinding(**mock_inputs)
        assert_attribs_in(result, *expected_attribs)
        assert sorted(result.payload) == sorted(expected_results_1)
        for table_id in const.DATA_TABLE_IDS:
            assert "query_execution_date" in result.data_tables[table_id][0]["cells"]
            result.data_tables[table_id][0]["cells"]["query_execution_date"] = time_stamp
        assert result.data_tables == expected_results_2

    @pytest.mark.parametrize("finding, expected_results", [
        (get_cli_raw_responses("get_findings")["Findings"][0], get_mocked_results("replace_datetime"))
    ])
    def test_make_incident_fields(self, finding, expected_results):

        keys = ["name", "description", "discovered_date", "severity_code", "properties"]

        finding_payload = ParseFinding({"Severity": 7}, "us-west-2")

        finding_payload.payload = {}
        finding_payload.finding = finding_payload.replace_datetime(finding)
        assert finding_payload.payload == {}
        result = finding_payload.make_incident_fields()
        assert_keys_in(result, *keys)
        assert result == expected_results

    @pytest.mark.parametrize("finding, title, expected_results", [
        (get_cli_raw_responses("get_findings")["Findings"][0], True,
         "AWS GuardDuty: API GeneratedFindingAPIName was invoked from an IP address on a custom threat list."),
        (get_cli_raw_responses("get_findings")["Findings"][0], False,
         "AWS GuardDuty: No Title Provided."),
    ])
    def test_make_incident_name(self, finding, title, expected_results):

        finding_payload = ParseFinding({"Severity": 7, "Region": "us-west-2"}, "us-west-2")

        if not title:
            finding["Title"] = ''
        finding_payload.finding = finding_payload.replace_datetime(finding)
        result = finding_payload.make_incident_name()
        assert isinstance(result, str)
        assert result == expected_results
        if not title:
            del finding["Title"]
        finding_payload.finding = finding_payload.replace_datetime(finding)
        result = finding_payload.make_incident_name()
        assert isinstance(result, str)
        assert result == expected_results

    @pytest.mark.parametrize("finding, desc, expected_results", [
        (get_cli_raw_responses("get_findings")["Findings"][0], True,
         {'format': 'text', 'content': 'An API was used to access a bucket from an IP address on a custom threat list.'}),
        (get_cli_raw_responses("get_findings")["Findings"][0], False,
         {'content': 'AWS GuardDuty finding --', 'format': 'text'}),
    ])
    def test_make_incident_fields(self, finding, desc, expected_results):

        finding_payload = ParseFinding({"Severity": 7, "Region": "us-west-2"}, "us-west-2")

        if not desc:
            finding["Description"] = ''
        finding_payload.finding = finding_payload.replace_datetime(finding)
        result = finding_payload.make_incident_description()
        assert isinstance(result, dict)
        assert result == expected_results
        if not desc:
            del finding["Description"]
            finding_payload.finding = finding_payload.replace_datetime(finding)
            result = finding_payload.make_incident_description()
            assert isinstance(result, dict)
            assert result == expected_results


    @pytest.mark.parametrize("finding_severity, expected_results", [
        (1, "Low"),
        (2.0, "Low"),
        (3, "Low"),
        (4.0, "Medium"),
        (5, "Medium"),
        (6.0, "Medium"),
        (7, "High"),
        (8.0, "High"),
    ])
    def test_map_severity(self, finding_severity, expected_results):

        finding_payload = ParseFinding({"Severity": 7, "Region": "us-west-2"}, "us-west-2")

        result = finding_payload.map_severity(finding_severity)
        assert result == expected_results

    @pytest.mark.parametrize("finding_severity, expected_results", [
        (0, "Incorrect value '0' set for severity level."),
        (9, "Incorrect value '9' set for severity level."),
        (-1, "Incorrect value '-1' set for severity level."),
        ("string", "Incorrect value 'string' set for severity level."),
    ])
    def test_map_severity_invalid(self, finding_severity, expected_results):

        finding_payload = ParseFinding({"Severity": 7, "Region": "us-west-2"}, "us-west-2")

        with pytest.raises(ValueError) as e:
            result = finding_payload.map_severity(finding_severity)
        assert str(e.value) == expected_results

    @pytest.mark.parametrize("finding, expected_results", [
        (get_cli_raw_responses("get_findings")["Findings"][0], [7, 3])
    ])
    def test_get_artifact_data(self, finding, expected_results):

        keys = ["GeneratedFindingAccessKeyId", "GeneratedFindingUserName", "198.51.100.0", "10.0.0.1",
                "GeneratedFindingPublicDNSName", "GeneratedFindingPrivateDnsName", "GeneratedFindingPrivateName"]

        finding_payload = ParseFinding({"Severity": 7, "Region": "us-west-2"}, "us-west-2")
        finding_payload.finding = finding_payload.replace_datetime(finding)

        result = finding_payload.get_artifact_data()
        assert isinstance(result, dict)
        assert len(result) == expected_results[0]
        assert_keys_in(result, *keys)
        for value in result.values():
            assert isinstance(value, tuple)
            assert len(value) == expected_results[1]

    @pytest.mark.parametrize("finding, expected_results", [
        (get_cli_raw_responses("get_findings")["Findings"][0], 7)
    ])
    def test_add_artifacts_to_payload(self, finding, expected_results):

        keys = ["type", "description", "value"]

        finding_payload = ParseFinding({"Severity": 7,"Region": "us-west-2"}, "us-west-2")
        finding_payload.finding = finding_payload.replace_datetime(finding)
        finding_payload.existing_artifacts = []
        finding_payload.payload = {}

        finding_payload.add_artifacts_to_payload()
        assert "artifacts" in finding_payload.payload
        artifacts = finding_payload.payload.get("artifacts")
        assert isinstance(artifacts, list)
        assert len(artifacts) == expected_results
        for artifact in artifacts:
            assert_keys_in(artifact, *keys)

    @pytest.mark.parametrize("finding, refresh, expected_results", [
        (get_cli_raw_responses("get_findings")["Findings"][0], True, ["text","AWS GuardDuty finding Payload for refresh:"]),
        (get_cli_raw_responses("get_findings")["Findings"][0], False, ["text", "AWS GuardDuty finding Payload:"])

    ])
    def test_add_note_to_payload(self, finding, refresh, expected_results):

        finding_payload = ParseFinding({"Severity": 7, "Region": "us-west-2"}, "us-west-2")
        finding_payload.finding = finding_payload.replace_datetime(finding)
        finding_payload.payload = {}
        finding_payload.refresh = refresh

        finding_payload.add_note_to_payload()
        assert "comments" in finding_payload.payload
        comments = finding_payload.payload.get("comments")
        assert isinstance(comments, list)
        text = comments[0]["text"]
        assert expected_results[1] in text["content"]

    @pytest.mark.parametrize("finding, expected_results", [
        (get_cli_raw_responses("get_findings")["Findings"][0], None)
    ])
    def test_build_data_tables(self, finding, expected_results):

        keys_1 = ["gd_action_details", "gd_resource_affected"]

        finding_payload = ParseFinding({"Severity": 7, "Region": "us-west-2"}, "us-west-2")
        finding_payload.finding = finding_payload.replace_datetime(finding)
        finding_payload.data_tables = {}

        finding_payload.build_data_tables()
        assert_keys_in(finding_payload.data_tables, *keys_1)

    @pytest.mark.parametrize("finding, expected_results", [
        (get_mocked_finding_data("replace_datetime_finding"), None)
    ])
    def test_replace_datetime(self, finding, expected_results):

        finding_payload = ParseFinding({"Severity": 7, "Region": "us-west-2"}, "us-west-2")
        finding_payload.finding = finding

        assert isinstance(finding_payload.finding["CreatedAt"], datetime.datetime)
        assert isinstance(finding_payload.finding["Dates"][0]["TestDate"], datetime.datetime)
        assert isinstance(finding_payload.finding["OtherDates"]["TestDate2"], datetime.datetime)
        finding_payload.replace_datetime(finding)
        assert isinstance(finding_payload.finding["CreatedAt"], str)
        assert isinstance(finding_payload.finding["Dates"][0]["TestDate"], str)
        assert isinstance(finding_payload.finding["OtherDates"]["TestDate2"], str)


    mock_inputs_1 = {
        "finding": get_cli_raw_responses("get_findings")["Findings"][0],
        "region": "us-west-2",
        "refresh": True,
        "existing_artifacts": get_resilient_responses("find_resilient_artifacts_for_incident_with_artifacts")
    }

    expected_results_1 = get_mocked_results("finding_payload_no_artifacts")

    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (mock_inputs_1, expected_results_1),
    ])
    def test_to_json(self, mock_inputs, expected_results):

        keys = ["finding", "payload", "data_tables"]

        finding_payload = ParseFinding(**mock_inputs)
        result = finding_payload.to_json()
        assert isinstance(result, dict)
        assert_keys_in(result, *keys)
        for key in keys:
            assert isinstance(result[key], dict)

    @pytest.mark.skipif(sys.version_info.major != 2 , reason="requires python2")
    @pytest.mark.parametrize("finding, expected_results", [
        (get_mocked_finding_data("convert_unicode_finding"), None)
    ])
    def test_convert_unicode(self, finding, expected_results):

        finding_payload = ParseFinding({"Severity": 7, "Region": "us-west-2"}, "us-west-2")
        finding_payload.finding = finding

        assert isinstance(finding["CreatedAt"], unicode)
        assert isinstance(finding["Dates"][0]["TestDate"], unicode)
        assert isinstance(finding["OtherDates"]["TestDate2"], unicode)
        finding = finding_payload.convert_unicode(finding)
        assert isinstance(finding["CreatedAt"], str)
        assert isinstance(finding["Dates"][0]["TestDate"], str)
        assert isinstance(finding["OtherDates"]["TestDate2"], str)
