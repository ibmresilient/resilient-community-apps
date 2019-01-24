# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
import json
import requests_mock
from mock import patch
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from fn_microsoft_security_graph.util.helper import MicrosoftGraphHelper
from fn_microsoft_security_graph.components.microsoft_security_graph_alerts_integrations import alert_search, \
    update_alert, create_query, get_alert_details, ds_to_millis, build_incident_dto, get_alerts, escape_illegal_chars
from resilient_circuits.template_functions import environment

PACKAGE_NAME = "fn_microsoft_security_graph"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def generate_response(content, status):
    class simResponse:
        def __init__(self, content, status):
            self.status_code = status
            self.content = content
            self.text = json.dumps(content)

        def json(self):
            return self.content

    return simResponse(content, status)


def call_microsoft_security_graph_update_alert_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("microsoft_security_graph_update_alert", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("microsoft_security_graph_update_alert_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


def call_microsoft_security_graph_get_alert_details_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("microsoft_security_graph_get_alert_details", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("microsoft_security_graph_get_alert_details_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


def call_microsoft_security_graph_alert_search_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("microsoft_security_graph_alert_search", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("microsoft_security_graph_alert_search_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestMicrosoftSecurityGraphfunctions:
    """ Tests for the microsoft security graph functions"""

    def test_functions_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, "microsoft_security_graph_update_alert")
        assert func is not None

        func = get_function_definition(PACKAGE_NAME, "microsoft_security_graph_get_alert_details")
        assert func is not None

        func = get_function_definition(PACKAGE_NAME, "microsoft_security_graph_alert_search")
        assert func is not None

    @patch("requests.post")
    def test_get_access_token(self, mocked_requests_post):
        content = {
            "access_token": "fake_access_token"
        }
        mocked_requests_post.return_value = generate_response(content, 200)

        ms_helper = MicrosoftGraphHelper("tenant_id1234", "client_id1234", "client_secret1234")
        token = ms_helper.get_access_token()
        assert token == "fake_access_token"

    @patch("requests.post")
    def test_get_access_token_refresh(self, mocked_requests_post):
        content1 = {
            "access_token": ""
        }
        content2 = {
            "access_token": "fake_refreshed_access_token"
        }
        mocked_requests_post.side_effect = [generate_response(content1, 200),
                                            generate_response(content2, 200)]

        ms_helper = MicrosoftGraphHelper("tenant_id1234", "client_id1234", "client_secret1234")
        ms_helper.clear_cache()
        token = ms_helper.get_access_token()
        assert token == "fake_refreshed_access_token"

    @patch("requests.post")
    def test_check_stats_code_good(self, mocked_requests_post):
        content = {
            "access_token": "fake_access_token"
        }
        mocked_requests_post.return_value = generate_response(content, 200)
        ms_helper = MicrosoftGraphHelper("tenant_id1234", "client_id1234", "client_secret1234")
        r = requests_mock.response
        r.status_code = 200

        assert ms_helper.check_status_code(r)

    @patch("requests.post")
    def test_check_stats_code_invalid(self, mocked_requests_post):
        content1 = {
            "access_token": "fake_access_token"
        }
        content2 = {
            "access_token": "new_fake_access_token"
        }
        mocked_requests_post.side_effect = [generate_response(content1, 200),
                                            generate_response(content2, 200)]
        ms_helper = MicrosoftGraphHelper("tenant_id1234", "client_id1234", "client_secret1234")
        r = requests_mock.response
        r.status_code = 401
        r.content = "Fake content"

        assert not ms_helper.check_status_code(r)

        token = ms_helper.get_access_token()
        assert token == "new_fake_access_token"

    @patch("requests.post")
    def test_check_stats_code_bad(self, mocked_requests_post):
        content = {
            "access_token": "fake_access_token"
        }
        mocked_requests_post.return_value = generate_response(content, 200)
        ms_helper = MicrosoftGraphHelper("tenant_id1234", "client_id1234", "client_secret1234")
        r = requests_mock.response
        r.status_code = 500

        try:
            ms_helper.check_status_code(r)
        except ValueError as e:
            assert e.args[0] == "Invalid response from Microsoft Security Graph"

    @patch("requests.get")
    @patch("requests.post")
    def test_search_alert(self, mocked_requests_post, mocked_requests_get):
        content = {
            "access_token": "fake_access_token"
        }
        content2 = {
            "alerts": [
                {"alert1": 1},
                {"alert2": 2}
            ]
        }
        mocked_requests_post.return_value = generate_response(content, 200)
        mocked_requests_get.return_value = generate_response(content2, 200)
        ms_helper = MicrosoftGraphHelper("tenant_id1234", "client_id1234", "client_secret1234")
        ms_helper.clear_cache()
        r = alert_search("ms_graph_url", ms_helper, "filter")

        assert r.json() == content2

    @patch("requests.get")
    @patch("requests.post")
    def test_get_alert_details(self, mocked_requests_post, mocked_requests_get):
        content = {
            "access_token": "fake_access_token"
        }
        content2 = {
            "alert_details": {
                "details": 1234
            }
        }
        mocked_requests_post.return_value = generate_response(content, 200)
        mocked_requests_get.return_value = generate_response(content2, 200)
        ms_helper = MicrosoftGraphHelper("tenant_id1234", "client_id1234", "client_secret1234")
        ms_helper.clear_cache()
        r = get_alert_details("ms_graph_url", ms_helper, "1223456788")

        assert r.json() == content2

    @patch("requests.patch")
    @patch("requests.post")
    def test_update_alert(self, mocked_requests_post, mocked_requests_patch):
        content = {
            "access_token": "fake_access_token"
        }
        content2 = {
            "alert_details": {
                "details": "updated"
            }
        }
        mocked_requests_post.return_value = generate_response(content, 200)
        mocked_requests_patch.return_value = generate_response(content2, 200)
        ms_helper = MicrosoftGraphHelper("tenant_id1234", "client_id1234", "client_secret1234")
        ms_helper.clear_cache()
        r = update_alert("ms_graph_url", ms_helper, "21354657678", '{"update_data": "data"}')

        assert r.json() == content2

    def test_create_filter_alert(self):
        f = create_query("filter=severity%20eq%20'high'", "")
        assert f == "?$filter=severity%20eq%20'high'"

    def test_create_filter_alert_date(self):
        f = create_query("filter=severity%20eq%20'high'", "createdDateTime%20ge%202018-11-28T19:42:42.225471Z")

        assert f == "?$filter=severity%20eq%20'high'%20and%20createdDateTime%20ge%202018-11-28T19:42:42.225471Z"

    def test_create_query(self):
        q = create_query("filter=userStates/any(user:%20user/accountName%20eq%20'brianwal_ibm')&$top=5&$sort=decn", "createdDateTime%20ge%202018-11-28T19:42:42.225471Z")

        assert q == "?$filter=userStates/any(user:%20user/accountName%20eq%20'brianwal_ibm')%20and%20createdDateTime%20ge%202018-11-28T19:42:42.225471Z&$top=5&$sort=decn"

    def test_ds_to_millis(self):
        epoch = ds_to_millis("2017-05-17T17:07:59.114Z")
        assert epoch == 1495040879000

    def test_build_incident_dto(self):
        ds_filter = {"ds_to_millis": ds_to_millis}
        env = environment()
        env.globals.update(ds_filter)

        alert_data = {"eventDateTime": "2018-11-01T19:48:16.3432936Z", "lastModifiedDateTime": "2018-11-01T19:51:19.0619566Z", "malwareStates": [], "networkConnections": [], "fileStates": [], "registryKeyStates": [], "description": "Sign-in from an anonymous IP address (e.g. Tor browser, anonymizer VPNs)", "createdDateTime": "2018-11-01T19:48:16.3432936Z", "title": "Anonymous IP address", "assignedTo": "", "cloudAppStates": [], "recommendedActions": [], "id": "ea1921b334a655056acfa2b7f4f5d5679dc0976a29e55882edf8e58f9e390c55", "riskScore": "", "severity": "medium", "processes": [], "comments": [], "hostStates": [], "confidence": 0, "vendorInformation": {"providerVersion": "3.0", "provider": "IPC", "vendor": "Microsoft"}, "azureTenantId": "07218a5e-c310-4a41-8eaf-f6b542f1ef5c", "triggers": [], "tags": [], "azureSubscriptionId": "", "vulnerabilityStates": [], "userStates": [{"logonIp": "51.15.43.205", "logonLocation": "Santpoort-Zuid, Noord-Holland, NL", "accountName": "brian_admin", "emailRole": "unknown", "riskScore": "0", "userPrincipalName": "brian_admin@brianwalibmoutlook.onmicrosoft.com"}], "detectionIds": [], "category": "AnonymousLogin", "sourceMaterials": [], "status": "newAlert"}
        inc_dto = build_incident_dto(alert_data)
        expected = {
            "description": {
                "format": "html",
                "content": "Sign-in from an anonymous IP address (e.g. Tor browser, anonymizer VPNs)"
            },
            "discovered_date": 1541101696000,
            "name": "Microsoft Security Graph Alert: 2018-11-01T19:48:16.3432936Z",
            "properties": {
                "microsoft_security_graph_alert_id": "ea1921b334a655056acfa2b7f4f5d5679dc0976a29e55882edf8e58f9e390c55"
            }
        }
        assert json.loads(inc_dto) == expected

    @patch("requests.get")
    @patch("requests.post")
    def test_get_alerts(self, mocked_requests_post, mocked_requests_get):
        opts = {
            "alert_time_range_sec": "100",
            "microsoft_graph_url": "fake_url",
            "alert_filter": "severity%20eq%20'high'"
        }
        content = {
            "access_token": "fake_access_token"
        }
        content2 = {
            "value": {
                "alert_details": {
                    "details": 1234
                }
            }
        }
        mocked_requests_post.return_value = generate_response(content, 200)
        mocked_requests_get.return_value = generate_response(content2, 200)

        ms_helper = MicrosoftGraphHelper("tenant_id1234", "client_id1234", "client_secret1234")
        alerts = get_alerts(opts, ms_helper)

        assert alerts == {"alert_details": {"details": 1234}}

    def test_escape_illegal_chars(self):
        test_string = "userStates/any(user: user/accountName eq 'brianwal_ibm') & filter(top)"
        actual_string = escape_illegal_chars(test_string)
        assert actual_string == "userStates%2Fany(user:%20user%2FaccountName%20eq%20'brianwal_ibm')%20%26%20filter(top)"

        test_string = "%+/?#& "
        actual_string = escape_illegal_chars(test_string)
        assert actual_string == "%25%2B%2F%3F%23%26%20"
