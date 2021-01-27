# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Test helper functions"""
import pytest
from fn_aws_guardduty.lib.helpers import *
from .mock_artifacts import *
"""
Suites of tests to test the AWS GuardDuty Helper functions
"""

class TestIQuery:
    """Test IQuery class"""

    @pytest.mark.parametrize("finding, fields, region, expected_results, expected_results_2", [
        (get_cli_raw_responses("get_findings")["Findings"][0],
         ["Id", "DetectorId"], "us-west-2",
         ["60baffd3f9042e38640f2300d5c5a631", "f2baedb0ac74f8f42fc929e15f56da6a"], "us-west-2"),
        (get_cli_raw_responses("get_findings")["Findings"][0],
         ["Id"], "us-west-2", ["60baffd3f9042e38640f2300d5c5a631", ""], "us-west-2"),
        (get_cli_raw_responses("get_findings")["Findings"][0],
         ["DetectorId"], "us-west-2", ["", "f2baedb0ac74f8f42fc929e15f56da6a"], "us-west-2"),
    ])
    def test_iquery(self, finding, fields, region, expected_results_2, expected_results):
        result = IQuery(finding, fields)
        assert(issubclass(type(result), dict))
        assert "filters" in result
        assert "sorts" in result
        assert len(fields) + 1 == len(result["filters"][0]["conditions"])
        if "Id" in fields:
            assert result["filters"][0]["conditions"][1]["value"] == expected_results[0]
        if "DetectorId" in fields:
            inx = len(fields)
            assert result["filters"][0]["conditions"][inx]["value"] == expected_results[1]
        result.add_conditions(region, "Region")
        inx = len(fields) + 1
        assert result["filters"][0]["conditions"][inx]["value"] == expected_results_2

    @pytest.mark.parametrize("finding, fields, expected_results, expected_results_2", [
        (get_cli_raw_responses("get_findings")["Findings"][0],
         ["Id", "DetectorId"], ["properties.aws_guardduty_finding_id", "properties.aws_guardduty_detector_id"],
         "properties.aws_guardduty_region"),
        (get_cli_raw_responses("get_findings")["Findings"][0],
         ["Id"], ["properties.aws_guardduty_finding_id", ""], "properties.aws_guardduty_region"),
        (get_cli_raw_responses("get_findings")["Findings"][0],
         ["DetectorId"], ["", "properties.aws_guardduty_detector_id"], "properties.aws_guardduty_region"),
    ])
    def test_iquery_alt(self, finding, fields, expected_results, expected_results_2):
        result = IQuery(finding, fields, alt=True)
        assert(issubclass(type(result), dict))
        assert "filters" in result
        assert "sorts" not in result
        assert len(fields) + 1 == len(result["filters"][0]["conditions"])
        if "Id" in fields:
            assert result["filters"][0]["conditions"][1]["field_name"] == expected_results[0]
        if "DetectorId" in fields:
            inx = len(fields)
            assert result["filters"][0]["conditions"][inx]["field_name"] == expected_results[1]
        result.add_alt_conditions("Region")
        inx = len(fields) + 1
        assert result["filters"][0]["conditions"][inx]["field_name"] == expected_results_2

class TestFCrit:
    """Test FCrit class"""
    @pytest.mark.parametrize("severity_threshold, expected_results", [
        (1, 1),
        (7, 7),
        (9, 9)
    ])
    def test_fcrit_set_severity(self, severity_threshold, expected_results):
        now = dt.datetime.now()
        last_update = (time.mktime(now.timetuple()) + now.microsecond / 1e6) * 1000.0
        result = FCrit()
        result.set_severity(severity_threshold)
        result.set_update(last_update)
        assert (issubclass(type(result), dict))
        assert result["Criterion"]["severity"]["Gte"] == expected_results
        assert result["Criterion"]["updatedAt"]["Gte"] == int(last_update)

class TestIsRegex:
    """Test is_regex function"""

    @pytest.mark.parametrize("regex_pattern, expected_results", [
        ("^(us|eu).*", True),
        ("us-west-2", True),
        ("+++", False)
    ])
    def test_is_regex(self, regex_pattern, expected_results):

        assert is_regex(regex_pattern) == expected_results


class TestGetLastRunUnixEpoch:
    """Test lastrun_unix_epoch function"""

    @pytest.mark.parametrize("lookback_interval, expected_results", [
        (60,  ""),
        (dt.datetime.now(), ""),
    ])
    def test_get_lastrun_unix_epoch(self, lookback_interval,  expected_results):
        result = get_lastrun_unix_epoch(lookback_interval)
        assert isinstance(result, float)
        d = dt.datetime.fromtimestamp((result/1000.0), tz=None)
        assert isinstance(d, dt.datetime)

class TestGetDataAtPath:
    """Test get_data_at_path function"""

    @pytest.mark.parametrize("finding, path, expected_results", [
        (get_cli_raw_responses("get_findings")["Findings"][0], ["Resource", "AccessKeyDetails"], True),
        (get_cli_raw_responses("get_findings")["Findings"][0], ["Resource", "NotExists"], False),
        (get_cli_raw_responses("get_findings")["Findings"][0], ["Resource", "S3BucketDetails"], True),
        (get_cli_raw_responses("get_findings")["Findings"][0], ["Resource", "S3BucketDetails", 0], True),
        (get_cli_raw_responses("get_findings")["Findings"][0], ["Resource", "S3BucketDetails", 1], False),
    ])
    def test_get_data_at_path(self, finding, path, expected_results):
        (ele_match, _) = get_data_at_path(finding, path)
        assert ele_match == expected_results


class TestSearchJson:
    """Test search_json function"""

    @pytest.mark.parametrize("finding, key, path, expected_length, expected_results", [
        (get_cli_raw_responses("get_findings")["Findings"][0], "AccessKeyId", None, 1,
         [("GeneratedFindingAccessKeyId", ["Resource", "AccessKeyDetails"])]),
        (get_cli_raw_responses("get_findings")["Findings"][0], "NotExists", None, 0,
         []),
        (get_cli_raw_responses("get_findings")["Findings"][0], "PrivateIpAddress", None, 2,
         [("10.0.0.1", ["Resource", "InstanceDetails", "NetworkInterfaces", 0]), ("10.0.0.1", ["Resource", "InstanceDetails", "NetworkInterfaces", 0, "PrivateIpAddresses", 0])]),
        (get_cli_raw_responses("get_findings")["Findings"][0], "AccessKeyId", ["Resource", "AccessKeyDetails"], 1,
         [("GeneratedFindingAccessKeyId", ["Resource", "AccessKeyDetails"])]),
        (get_cli_raw_responses("get_findings")["Findings"][0], "PrivateIpAddress",
         ["Resource", "InstanceDetails", "NetworkInterfaces", 0], 2,
         [("10.0.0.1", ["Resource", "InstanceDetails", "NetworkInterfaces", 0]),
          ("10.0.0.1", ["Resource", "InstanceDetails", "NetworkInterfaces", 0, "PrivateIpAddresses", 0])]),

    ])
    def test_search_json(self, finding, key, path, expected_length, expected_results):
        result = search_json(finding, key, path=path)
        assert isinstance(result, list)
        assert len(result) == expected_length
        assert sorted(result) == sorted(expected_results)
        if len(result) > 0:
            for r in result:
                assert isinstance(r, tuple)

    @pytest.mark.parametrize("finding, key, path, expected_results", [
        (get_cli_raw_responses("get_findings")["Findings"][0], "AccessKeyId", ["Resource", "NotExists"],
         {"msg": "Path not found", "path": "['Resource', 'NotExists']"}),
        (get_cli_raw_responses("get_findings")["Findings"][0], "AccessKeyId", ["Resource", "S3BucketDetails", 1],
         {"msg": "Path not found", "path": "['Resource', 'S3BucketDetails', 1]"}),

    ])
    def test_search_json_missing_path(self, finding, key, path, expected_results):
        result = search_json(finding, key, path=path)
        assert isinstance(result, dict)
        assert result == expected_results

    @pytest.mark.parametrize("finding, key, path, expected_results", [
        (get_cli_raw_responses("get_findings")["Findings"][0], "AccessKeyId", ["Resource", "NotExists"],
         {"msg": "Path not found", "path": "['Resource', 'NotExists']"}),
        (get_cli_raw_responses("get_findings")["Findings"][0], "AccessKeyId", ["Resource", "S3BucketDetails", 1],
         {"msg": "Path not found", "path": "['Resource', 'S3BucketDetails', 1]"}),

    ])
    def test_map_property(self, finding, key, path, expected_results):
        result = search_json(finding, key, path=path)
        assert isinstance(result, dict)
        assert result == expected_results

class TestMapProperty:
    @pytest.mark.parametrize("gd_prop, expected_results", [
        ("Id", ("aws_guardduty_finding_id", None)),
        ("Arn", ("aws_guardduty_finding_arn", None)),
        ("Type", ("aws_guardduty_finding_type", None)),
        ("UpdatedAt", ("aws_guardduty_finding_updated_at", None)),
        ("Region", ("aws_guardduty_region", None)),
        ("ResourceType", ("aws_guardduty_resource_type", "Resource")),
        ("DetectorId", ("aws_guardduty_detector_id", "Service")),
        ("Count", ("aws_guardduty_count", "Service"))
    ])
    def test_map_property(self, gd_prop, expected_results):
        result = map_property(gd_prop)
        assert result == expected_results

    @pytest.mark.parametrize("gd_prop, expected_results", [
        ("Unknown", "'Unsupported finding property: Unknown.'")
    ])
    def test_map_property_unsupported(self, gd_prop, expected_results):

        with pytest.raises(KeyError) as e:
            response = map_property(gd_prop)
        assert str(e.value) == expected_results