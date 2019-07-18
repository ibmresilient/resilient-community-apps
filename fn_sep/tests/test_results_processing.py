# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

"""Test results processing functionality."""
from __future__ import print_function
import pytest
from fn_sep.lib.results_processing import *
from  mock_artifacts import get_command_status, get_command_status_remediation, get_command_status_prefilter
"""
Suites of tests to test the Symantec SEP results_processing functions
"""

def assert_keys_in(json_obj, *keys):
    for key in keys:
        assert key in json_obj

def get_config():
    return dict({
        "sep_base_path":    "/sepm/api/v1",
        "sep_auth_path":    "/sepm/api/v1/identity/authenticate",
        "sep_host":         "192.168.1.2",
        "sep_port":         "8446",
        "sep_username":     "admin",
        "sep_password":     "password",
        "sep_domain":       "Default",
        "sep_results_limit": 200,
        "sep_scan_timeout": 1800
    })

class TestGetOverallProgress:

    """Test get_overall_progress function"""
    @pytest.mark.parametrize("rtn, expected_results", [
        (get_command_status(), "In progress"),
        (get_command_status_remediation(), "Completed"),
    ])
    def test_get_overall_progress(self, rtn, expected_results):

        results = get_overall_progress(rtn)
        assert expected_results == results

class TestParseScanResults:


    """Test parse_scan_results scan function"""
    @pytest.mark.parametrize("rtn, expected_results", [
        (get_command_status(), {'match_count': 0, 'remediation_count': 0, 'PARTIAL_MATCHES': [], 'HASH_MATCHES': [], 'artifact_type': '',
     'FULL_MATCHES': [], 'artifact_value': '', 'fail_remediation_count': 0, 'MATCH': False})
    ])
    def test_parse_scan_results_scan(self, rtn, expected_results):
        for c in rtn["content"]:
            if c["resultInXML"] is not None:
                xml = c["resultInXML"]
                results = parse_scan_results(xml)
                assert expected_results == results

    """Test parse_scan_results remediation function"""
    @pytest.mark.parametrize("rtn, expected_results", [
        (get_command_status_remediation(), {'match_count': 10, 'remediation_count': 0,  'fail_remediation_count': 9, 'MATCH': True}),
    ])
    def test_parse_scan_results_remediation(self, rtn, expected_results):
        for c in rtn["content"]:
            if c["resultInXML"] is not None:
                xml = c["resultInXML"]
                results = parse_scan_results(xml)
                assert expected_results["MATCH"] == results["MATCH"]
                assert expected_results["match_count"] == results["match_count"]
                assert expected_results["remediation_count"] == results["remediation_count"]
                assert expected_results["fail_remediation_count"] == results["fail_remediation_count"]

class TestFilterHits:

    """Test filter_hits function"""
    @pytest.mark.parametrize("rtn, status_type, expected_results", [
        (get_command_status_prefilter("match"), "remediation", 1),
        (get_command_status_prefilter("no_match"), "scan", 0)
    ])
    def test_filter_hits(self, rtn, status_type, expected_results):

        filter_hits(rtn, status_type)
        assert expected_results == len(rtn["content"])
        assert expected_results == rtn["totalElements"]


class TestProcessResults:

    """Test process_results function"""
    @pytest.mark.parametrize("rtn, status_type, expected_results", [
        (get_command_status(), "scan", "In progress"),
        (get_command_status_remediation(), "remediation", "Completed"),
    ])
    def test_process_results(self, rtn, status_type, expected_results):

        keys = ["content", "firstPage", "lastPage", "number", "numberOfElements", "size", "sort", "totalElements",
                  "totalPages"]

        keys_2 = ["overall_command_state", "total_ep_count", "total_match_count", "total_match_ep_count",
                  "total_not_completed", "total_remediation_count", "total_remediation_ep_count"]

        results = process_results(rtn, get_config(), status_type, None)
        assert_keys_in(results, *keys)
        assert_keys_in(results, *keys_2)
        assert expected_results == results["overall_command_state"]
