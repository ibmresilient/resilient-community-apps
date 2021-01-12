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
    """Test get_data_at_path function"""

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

    @pytest.mark.parametrize("finding, expected_results", [
        (get_cli_raw_responses("get_findings")["Findings"][0],
         {'name': 'AWS GuardDuty: API GeneratedFindingAPIName was invoked from an IP address on a custom threat list.',
          'description': {'format': 'text', 'content': 'An API was used to access a bucket from an IP address on a custom threat list.'},
          'discovered_date': '2020-11-25T13:46:37.960Z', 'severity_code': 'Low',
          'properties': {'aws_guardduty_finding_id': '60baffd3f9042e38640f2300d5c5a631',
                         'aws_guardduty_finding_arn': 'arn:aws:guardduty:us-west-2:834299573936:detector/f2baedb0ac74f8f42fc929e15f56da6a/finding/60baffd3f9042e38640f2300d5c5a631',
                         'aws_guardduty_finding_type': 'UnauthorizedAccess:S3/MaliciousIPCaller.Custom',
                         'aws_guardduty_finding_updated_at': '2020-11-26T15:18:12.620Z',
                         'aws_guardduty_region': 'us-west-2',
                         'aws_guardduty_resource_type': 'S3Bucket',
                         'aws_guardduty_count': 4,
                         'aws_guardduty_detector_id': 'f2baedb0ac74f8f42fc929e15f56da6a'}
          }),

    ])
    def test_make_incident_fields(self, finding, expected_results):
        aws_gd_poller = AwsGdPoller({}, get_config(), 2)
        result = aws_gd_poller.make_incident_fields(finding)
        assert isinstance(result, dict)
        assert result == expected_results

    @pytest.mark.parametrize("finding, title, expected_results", [
        (get_cli_raw_responses("get_findings")["Findings"][0], True,
         "AWS GuardDuty: API GeneratedFindingAPIName was invoked from an IP address on a custom threat list."),
        (get_cli_raw_responses("get_findings")["Findings"][0], False,
         "AWS GuardDuty: No Title Provided."),
    ])
    def test_make_incident_fields(self, finding, title, expected_results):
        aws_gd_poller = AwsGdPoller({}, get_config(), 2)
        if not title:
            finding["Title"] = ''
        result = aws_gd_poller.make_incident_name(finding)
        assert isinstance(result, str)
        assert result == expected_results
        if not title:
            del finding["Title"]
        result = aws_gd_poller.make_incident_name(finding)
        assert isinstance(result, str)
        assert result == expected_results

    @pytest.mark.parametrize("finding, desc, expected_results", [
        (get_cli_raw_responses("get_findings")["Findings"][0], True,
         {'format': 'text', 'content': 'An API was used to access a bucket from an IP address on a custom threat list.'}),
        (get_cli_raw_responses("get_findings")["Findings"][0], False,
         {'content': 'AWS GuardDuty finding --', 'format': 'text'}),
    ])
    def test_make_incident_fields(self, finding, desc, expected_results):
        aws_gd_poller = AwsGdPoller({}, get_config(), 2)
        if not desc:
            finding["Description"] = ''
        result = aws_gd_poller.make_incident_description(finding)
        assert isinstance(result, dict)
        assert result == expected_results
        if not desc:
            del finding["Description"]
            result = aws_gd_poller.make_incident_description(finding)
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
        aws_gd_poller = AwsGdPoller({}, get_config(), 2)
        result = aws_gd_poller.map_severity(finding_severity)
        assert result == expected_results

    @pytest.mark.parametrize("finding_severity, expected_results", [
        (0, "Incorrect value '0' set for severity level."),
        (9, "Incorrect value '9' set for severity level."),
        (-1, "Incorrect value '-1' set for severity level."),
        ("string", "Incorrect value 'string' set for severity level."),
    ])
    def test_map_severity_invalid(self, finding_severity, expected_results):
        aws_gd_poller = AwsGdPoller({}, get_config(), 2)
        with pytest.raises(ValueError) as e:
            result = aws_gd_poller.map_severity(finding_severity)
        assert str(e.value) == expected_results

    @pytest.mark.parametrize("aws_gd_severity_threshold, aws_gd_lookback_interval, last_update, expected_results", [
        (None, None, None, {'Criterion': {}}),
        (7, None, None, {'Criterion': {'severity': {'Gte': 7}}}),
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

    @pytest.mark.parametrize("finding, expected_results", [
        (get_cli_raw_responses("get_findings")["Findings"][0], [7, 3])
    ])
    def test_get_artifact_data(self, finding, expected_results):

        keys = ["GeneratedFindingAccessKeyId", "GeneratedFindingUserName", "198.51.100.0", "10.0.0.1",
                "GeneratedFindingPublicDNSName", "GeneratedFindingPrivateDnsName", "GeneratedFindingPrivateName"]

        aws_gd_poller = AwsGdPoller({}, get_config(), 2)
        result = aws_gd_poller.get_artifact_data(finding)
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

        aws_gd_poller = AwsGdPoller({}, get_config(), 2)

        artifact_data = aws_gd_poller.get_artifact_data(finding)

        result = aws_gd_poller.add_artifacts_to_payload({}, artifact_data)
        assert isinstance(result, dict)
        assert "artifacts" in result
        artifacts = result.get("artifacts")
        assert isinstance(artifacts, list)
        assert len(artifacts) == expected_results
        for artifact in artifacts:
            assert_keys_in(artifact, *keys)

    @pytest.mark.parametrize("finding, expected_results", [
        (get_cli_raw_responses("get_findings")["Findings"][0], ["text","AWS GuardDuty finding Payload:"])
    ])
    def test_add_note_to_payload(self, finding, expected_results):

        aws_gd_poller = AwsGdPoller({}, get_config(), 2)

        result = aws_gd_poller.add_note_to_payload({}, finding)
        assert isinstance(result, dict)
        assert "comments" in result
        comments = result.get("comments")
        assert isinstance(comments, list)
        text = comments[0]["text"]
        assert expected_results[1] in text["content"]


    @pytest.mark.parametrize("finding, expected_results", [
        (get_cli_raw_responses("get_findings")["Findings"][0], None)
    ])
    def test_build_data_tables(self, finding, expected_results):

        keys_1 = ["gd_action_details", "gd_resource_affected"]

        aws_gd_poller = AwsGdPoller({}, get_config(), 2)

        result = aws_gd_poller.build_data_tables(finding)
        assert isinstance(result, dict)
        assert_keys_in(result, *keys_1)