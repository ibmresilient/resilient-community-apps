# -*- coding: utf-8 -*-
"""Tests APIs using both mocked endpoints and livetests"""

import json
import os
from sys import api_version
from unittest import mock
import logging

import pytest
from mock import patch, Mock
import requests_mock
from fn_wiz.lib.app_common import (AppCommon, PACKAGE_NAME, MAX_RESULTS, MAX_VULN_RESULTS)
from fn_wiz.lib.wiz_graphql_queries import GRAPHQL_PULL_ISSUES, GRAPHQL_UPDATE_ISSUE, GRAPHQL_PULL_VULNERABILITIES
from resilient_lib import RequestsCommon, readable_datetime, IntegrationError, clean_html
from requests.models import Response

MOCK_URI_AUTHORIZATION = "https://wizauth.io"
MOCK_URI_GRAPHQL = "https://wizapi.io/graphql"

APP_CONFIG = {
    "client_id": "abcd-efgh",
    "client_secret": "abcdefg-hijklmno",
    "endpoint_url": "https://fake.app.wiz.com",
    "api_url": MOCK_URI_GRAPHQL,
    "token_url": MOCK_URI_AUTHORIZATION,
    "polling_interval": 60,
    "polling_lookback": 120,
    "verify": "false"
}

BASE_MOCK_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "mock_data")
PATH_AUTH_MOCK = os.path.join(BASE_MOCK_PATH, "POST_authtoken.json")
PATH_ISSUE_MOCK_FIRST_PAGE = os.path.join(BASE_MOCK_PATH, "POST_issue_first_page.json")
PATH_ISSUE_MOCK_LAST_PAGE = os.path.join(BASE_MOCK_PATH, "POST_issue_last_page.json")
PATH_SINGLE_ISSUE_MOCK = os.path.join(BASE_MOCK_PATH, "POST_single_issue.json")
PATH_UPDATE_ISSUE_MOCK = os.path.join(BASE_MOCK_PATH, "POST_update_issue.json")
PATH_VULNERABILITIES_MOCK = os.path.join(BASE_MOCK_PATH, "POST_vulnerabilities.json")

def load_json(path_file):
    with open(path_file, "r") as json_file:
        json_data = json_file.read()
    
    return json.loads(json_data)

class MockedResponse:
    def __init__(self, json_data):
        self.json_data = json_data

    def json(self):
        return self.json_data

@pytest.fixture(scope="function")
def mock_api():
    # create a requests mock and intercept each of the endpoints that have been implemented
    # note that requests to endpoints outside the scope of these that have been implemented
    # will return 
    with requests_mock.Mocker() as mock_api:
        mock_api.register_uri("POST", url=MOCK_URI_AUTHORIZATION, 
                              json=load_json(PATH_AUTH_MOCK), status_code=200)
        # Use this for paginating results
        mock_api.register_uri("POST", MOCK_URI_GRAPHQL, 
                              [{'json': load_json(PATH_ISSUE_MOCK_FIRST_PAGE), 'status_code': 200},
                               {'json': load_json(PATH_ISSUE_MOCK_LAST_PAGE), 'status_code': 200}])
        yield mock_api

@pytest.fixture(scope="module")
def app_common():
    rc = RequestsCommon()
    yield AppCommon(rc, PACKAGE_NAME, APP_CONFIG)

@pytest.fixture
def fx_generate_auth_token():
    """
    Patch generate auth token because it has to be done with every API call and involves a live API endpoint request
    """
    with patch("fn_wiz.lib.app_common.AppCommon._generate_auth_token") as mock_token:
        mock_token.return_value = "abcdefg"

def test_make_headers(app_common: AppCommon):
    """
    Test setting API token in headers
    """
    headers = app_common._make_headers("api_token")
    assert headers == { 'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': "Bearer api_token" }

def test_generate_auth_token(mock_api: requests_mock.Mocker, app_common: AppCommon):
    resp_token = app_common._generate_auth_token()
    assert resp_token == "abcdefg123"

def test_check_error(app_common: AppCommon, caplog):
    response_1 = {
        "errors": [{
            "message": "this is an error"
        }]
    }

    with pytest.raises(IntegrationError) as interror1:
        app_common.check_error(response_1)
    
    assert "Received an error from Wiz API" in caplog.text
    assert interror1.value.value == "this is an error"

    response_2 = {
        "errors": [{
            "message": "this is an error"
            },
            {   
            "message2": "this is another error"
            }
        ]
    }
    with pytest.raises(IntegrationError) as interror2:
        app_common.check_error(response_2)
    assert interror2.value.value == "Unexpected number of errors returned 2"

    response_3 = {}
    assert app_common.check_error(response_3) is None

def test__api_call_paged_issues(fx_generate_auth_token, mock_api: requests_mock.Mocker, app_common: AppCommon):
    """
    Test first querying first page and then next page and getting the list of issues back. The second page is the "last" page.
    """
    variables = {
                "first": MAX_RESULTS,
                "filterBy": {
                    "createdAt": {
                        "after": readable_datetime(1710257531) # utc datetime format
                    }
                }
            }
    issues = app_common._api_call_paged_issues(variables)
    assert len(issues) == 5     # should be getting 5 issues back - 2 from first page, 3 from last page


def test_query_changed_entities_since_ts(fx_generate_auth_token, app_common: AppCommon):
    """
    Test first querying first page and then next page and getting the list of issues back. The second page is the "last" page.
    """
    with patch("fn_wiz.lib.app_common.AppCommon._api_call_paged_issues") as mock_paged_call:
        mock_paged_call.return_value = [1,2,3]
        issues = app_common.query_changed_entities_since_ts(1710257531)
        test_variables = {
                "first": MAX_RESULTS,
                "filterBy": {
                    "statusChangedAt": {
                        "after": readable_datetime(1710257531) # utc datetime format
                    }
                }
            }

        mock_paged_call.assert_called_with(test_variables)
        assert issues == [1,2,3]

def test_make_linkback_url(app_common: AppCommon):
    url = app_common.make_linkback_url(123, linkback_url = "issues#~(issue~'{})")
    assert url == "https://fake.app.wiz.com/issues#~(issue~'123)"

def test_get_issue(fx_generate_auth_token, app_common: AppCommon):
    """
    Test if the correct queries are made to _api_call when looking for an issue.
    Also test error handling - should not be returning more than 1 Wiz Issue from API
    """

    # Patch API call and response to read from test Single Issue Data
    test_response = load_json(PATH_SINGLE_ISSUE_MOCK)

    # look for fake wiz issue id
    wiz_issue_id = "fffc02c7"
    test_variables = {
        "first": 1,
        "filterBy": {
            "id": [
                wiz_issue_id
            ]
        }
    }
    query = {
            "query": GRAPHQL_PULL_ISSUES,
            "variables": test_variables
        }
    
    with patch("fn_wiz.lib.app_common.AppCommon._api_call") as mock_api_call:
        mock_api_call.return_value = test_response
        issue = app_common.get_issue(wiz_issue_id)
        # API call should have been made with the above query
        mock_api_call.assert_called_with("POST", app_common.graphql_api_url, query)
        assert issue.get("id") == wiz_issue_id
    
        # Test if an Integration Error was raised if the incorrect number of issues came back from API
        test_response = load_json(PATH_ISSUE_MOCK_FIRST_PAGE)
        mock_api_call.return_value = test_response
        with pytest.raises(IntegrationError) as interror:
            app_common.get_issue(wiz_issue_id)
        assert interror.value.value == f"Unexpected number of issues returned 2 for issue ID {wiz_issue_id}. Expected 1 issue."

@pytest.mark.parametrize("mock_projects, mock_num_results, expected_results_len", [
        (["83b76efe", "af52828c", "c"], 50, 3),     # should be 3 results in total from mocked response
        (["83b76efe", "af52828c", "c"], 2, 2),      # but we only *want* 2 results
        (["a", "b", "c"], 2, 0)                     # but there are *no matches*
    ])
def test_get_vulnerabilities_by_projects(fx_generate_auth_token, app_common: AppCommon, caplog, mock_projects, mock_num_results, expected_results_len):
    """
    Test getting vulnerabilities by project (filtering the cached vulnerabilities by the provided project IDs AND the number of requested results)
    """
    all_vuln = load_json(PATH_VULNERABILITIES_MOCK)
    with patch("fn_wiz.lib.app_common.AppCommon.get_vulnerabilities") as mock_api_call:
        mock_api_call.return_value = all_vuln.get('data', {}).get('vulnerabilityFindings', {}).get('nodes', [])
        response = app_common.get_vulnerabilities_by_project(mock_projects, mock_num_results)
        assert len(response) == expected_results_len

def test_get_vulnerabilities_by_projects_errors(fx_generate_auth_token, app_common: AppCommon, caplog):
    """
    Test getting vulnerabilities by project but requested # of results is more than we can return
    """
    all_vuln = load_json(PATH_VULNERABILITIES_MOCK)
    with patch("fn_wiz.lib.app_common.AppCommon.get_vulnerabilities") as mock_api_call:
        mock_api_call.return_value = all_vuln.get('data', {}).get('vulnerabilityFindings', {}).get('nodes', [])
        # Test project IDs -- too many results requested
        with pytest.raises(IntegrationError) as interror:
            response = app_common.get_vulnerabilities_by_project(["a", "b", "c"], 501)
        assert "Requested number of results exceeds maximum" in interror.value.value

def test_get_vulnerabilities_by_projects_cache(fx_generate_auth_token, app_common: AppCommon, caplog):
    """
    Test the cache for get_vulnerabilities_by_project
    """
    all_vuln = load_json(PATH_VULNERABILITIES_MOCK)
    with patch("fn_wiz.lib.app_common.AppCommon.get_vulnerabilities") as mock_api_call:
        # the first set of dummy data will yield no results
        mock_api_call.return_value = []     # this will also test if the there are no vulnerabilities returned
        response = app_common.get_vulnerabilities_by_project(["a", "c"], 50)
        assert len(response) == 0

        # Now mock the return value such that there would actually be vulnerabilities if we were not using the cache
        mock_api_call.return_value = all_vuln.get('data', {}).get('vulnerabilityFindings', {}).get('nodes', [])
        response = app_common.get_vulnerabilities_by_project(["a", "c"], 50)
        assert len(response) == 0       # should still be 0 from the cache, even though there *are* matches


def test_get_vulnerabilities_custom(fx_generate_auth_token, app_common: AppCommon, caplog):
    with patch("fn_wiz.lib.app_common.AppCommon._api_call") as mock_api_call:
        # Test if custom filter is passed in -- but without the "first" key
        with pytest.raises(IntegrationError) as interror:
            app_common.get_vulnerabilities_custom({"bad_test": "filter"})
        assert "Required 'first' parameter for Wiz" in interror.value.value

        # Test if custom filter is passed in, with the required key "first"
        test_filter = {"first": 10, "filterBy": {"status": ["RESOLVED"]}}
        app_common.get_vulnerabilities_custom(test_filter)
        query = {
                "query": GRAPHQL_PULL_VULNERABILITIES,
                "variables": test_filter
            }
        mock_api_call.assert_called_with("POST", app_common.graphql_api_url, query)

def test_get_vulnerabilities(fx_generate_auth_token, app_common: AppCommon, caplog):
    """
    Test getting vulnerabilities queries and test that the cache is being used
    """
    caplog.set_level(logging.DEBUG)
    with patch("fn_wiz.lib.app_common.AppCommon._api_call") as mock_api_call:
        mock_api_call.return_value = {"data": {
                                        "vulnerabilityFindings": {
                                            "nodes": ["I", "am", "cached"]
                                            }
                                        }
                                    }
        results = app_common.get_vulnerabilities()
        test_variables = {
            "first": MAX_RESULTS,
            "filterBy": {
                "vendorSeverity": ["HIGH", "CRITICAL"],
                "status": ["OPEN"]
            },
            "orderBy": {
                "direction": "DESC"     # descending by firstDetectedAt value; most recent at the beginning
            }
        }
        query = {
                "query": GRAPHQL_PULL_VULNERABILITIES,
                "variables": test_variables
            }
        mock_api_call.assert_called_with("POST", app_common.graphql_api_url, query)
        assert results == ["I", "am", "cached"]
        assert "Found 3 vulnerabilities" in caplog.text

        # Test if the cache is accessed; even though our API call has a new return value, 
        # the older cached value should be what is returned by the `get_vulnerabilities` function
        mock_api_call.return_value = {"data": {
                                        "vulnerabilityFindings": {
                                            "nodes": ["I", "have", "been", "updated!"]
                                            }
                                        }
                                    }
        results = app_common.get_vulnerabilities()
        assert results == ["I", "am", "cached"]
        assert "Found 4 vulnerabilities" not in caplog.text

def test_update_issue(fx_generate_auth_token, app_common: AppCommon):
    """
    Test method to update an issue.
    """
    with patch("fn_wiz.lib.app_common.AppCommon._api_call") as mock_api_call:
        # Test if update is successful
        test_success = load_json(PATH_UPDATE_ISSUE_MOCK)
        mock_api_call.return_value = test_success
        resp = app_common.update_issue({}, "0")
        assert resp == load_json(PATH_UPDATE_ISSUE_MOCK).get('data').get('updateIssue').get('issue')


def test_add_note_to_issue(fx_generate_auth_token, app_common: AppCommon):
    """
    Test method to add note to an issue. This method mainly constructs a query and updates the issue
    """
    
    issue_id = "12345"
    test_variables = {
            "issueId": issue_id,
            "patch": {
                "note": f"Note from SOAR: {clean_html('new_note')}"
            }
        }
    query = {
        "query": GRAPHQL_UPDATE_ISSUE,
        "variables": test_variables
    }

    with patch("fn_wiz.lib.app_common.AppCommon.update_issue") as mock_update:
        app_common.add_note_to_issue(issue_id, "new_note")
        mock_update.assert_called_with(query, issue_id)

def test_sync_status_with_wiz(fx_generate_auth_token, app_common: AppCommon, caplog):
    """
    Test method to sync status with Wiz
    """
    issue_id = "12345"
    test_reason = "Duplicate"
    test_summary = "not needed"
    test_variables = {
            "issueId": issue_id,
            "patch": {
                "status": "REJECTED",
                "resolutionReason": "WONT_FIX",
                "note": f"Corresponding SOAR case has been closed with reason {test_reason} and resolution summary {test_summary}"
            }
        }

    query = {
            "query": GRAPHQL_UPDATE_ISSUE,
            "variables": test_variables
        }
    
    with patch("fn_wiz.lib.app_common.AppCommon.update_issue") as mock_update:
        # Test if a case is closed with "Resolved" in SOAR, the corresponding issue cannot be closed in Wiz due to API restrictions
        with caplog.at_level(logging.WARNING):
            with pytest.raises(IntegrationError) as interror:
                app_common.sync_status_with_wiz(issue_id, "Resolved")
        assert interror.value.value == "Cannot update Wiz issue to be 'Resolved'"
        assert "Cannot update Wiz issue to be 'Resolved'" in caplog.text
        
        mock_update.return_value = {"my": "test"}
        # Test if a case is closed with a reason like "Duplicate", where then the Wiz issue can be marked as "REJECTED"
        resp = app_common.sync_status_with_wiz(issue_id, test_reason, test_summary)
        mock_update.assert_called_with(query, issue_id)
        assert resp == {"my": "test"}
