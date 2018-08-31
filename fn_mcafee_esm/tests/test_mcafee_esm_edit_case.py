# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from mock import patch
from resilient_circuits.util import get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from test_helper import get_test_config, get_default_test_config, generate_response, string_test_config
from fn_mcafee_esm.util.helper import check_config, check_status_code, get_authenticated_headers, merge_two_dicts
from fn_mcafee_esm.components.mcafee_esm_edit_case import case_edit_case_details

PACKAGE_NAME = "fn_mcafee_esm"
FUNCTION_NAME = "mcafee_esm_edit_case"

# Read test configuration-data
t_config_data = get_test_config()
default_config_data = get_default_test_config()
config_data = string_test_config()

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_mcafee_esm_edit_case_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("mcafee_esm_edit_case", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("mcafee_esm_edit_case_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestMcafeeEsmEditCase:
    """ Tests for the mcafee_esm_edit_case function"""

    def test_check_status_valid(self):
        try:
            check_status_code(200)
            assert True
        except ValueError:
            assert False

    def test_check_status_invalid(self):
        try:
            check_status_code(404)
            assert False
        except ValueError:
            assert True

    def test_merge_two_dicts(self):
        dict1 = {
            "a": "aa",
            "b": "bb"
        }
        dict2 = {
            "b": "zz",
            "c": "cc"
        }
        expected_dict = {
            "a": "aa",
            "b": "zz",
            "c": "cc"
        }

        actual_dict = merge_two_dicts(dict1, dict2)
        assert expected_dict == actual_dict

    def test_check_config_valid(self):
        expected_config_ops = t_config_data.copy()
        expected_config_ops["trust_cert"] = False
        actual_config_ops = check_config(t_config_data)

        assert expected_config_ops == actual_config_ops

    def test_check_config_valid_trust_cert(self):
        test_config_data = t_config_data.copy()
        test_config_data["trust_cert"] = "True"
        expected_config_ops = t_config_data.copy()
        expected_config_ops["trust_cert"] = True
        actual_config_ops = check_config(test_config_data)

        assert expected_config_ops == actual_config_ops

    def test_check_config_no_esm_section(self):
        try:
            check_config({})
            assert False
        except ValueError as e:
            assert e.args[0] == "[fn_mcafee_esm] section is not set in the config file"

    def test_check_config_no_url(self):
        test_config_ops = t_config_data.copy()
        try:
            del test_config_ops["esm_url"]
            check_config(test_config_ops)
            assert False
        except ValueError as e:
            assert e.args[0] == "esm_url is not set. You must set this value to run this function"

    def test_check_config_no_username(self):
        test_config_ops = t_config_data.copy()
        try:
            del test_config_ops["esm_username"]
            check_config(test_config_ops)
            assert False
        except ValueError as e:
            assert e.args[0] == "esm_username is not set. You must set this value to run this function"

    def test_check_config_no_password(self):
        test_config_ops = t_config_data.copy()
        try:
            del test_config_ops["esm_password"]
            check_config(test_config_ops)
            assert False
        except ValueError as e:
            assert e.args[0] == "esm_password is not set. You must set this value to run this function"

    def test_check_config_no_trust_cert(self):
        test_config_ops = t_config_data.copy()
        try:
            del test_config_ops["trust_cert"]
            check_config(test_config_ops)
            assert False
        except ValueError as e:
            assert e.args[0] == "trust_cert is not set. You must set this value to run this function"

    def test_check_config_default_url(self):
        test_config_ops = default_config_data.copy()
        try:
            check_config(test_config_ops)
            assert False
        except ValueError as e:
            assert e.args[0] == "esm_url is still the default value, this must be changed to run this function"

    def test_check_config_default_username(self):
        test_config_ops = default_config_data.copy()
        try:
            test_config_ops["esm_url"] = "somethingelse.com"
            check_config(test_config_ops)
            assert False
        except ValueError as e:
            assert e.args[0] == "esm_username is still the default value, this must be changed to run this function"

    def test_check_config_default_password(self):
        test_config_ops = default_config_data.copy()
        try:
            test_config_ops["esm_url"] = "somethingelse.com"
            test_config_ops["esm_username"] = "fake_username"
            check_config(test_config_ops)
            assert False
        except ValueError as e:
            assert e.args[0] == "esm_password is still the default value, this must be changed to run this function"

    def test_check_config_default_trust_cert(self):
        test_config_ops = default_config_data.copy()
        try:
            test_config_ops["esm_url"] = "somethingelse.com"
            test_config_ops["esm_username"] = "fake_username"
            test_config_ops["esm_password"] = "fake_password"
            check_config(test_config_ops)
            assert False
        except ValueError as e:
            assert e.args[0] == "trust_cert is still the default value, this must be changed to run this function"

    @patch("requests.post")
    def test_get_authenticated_headers(self, mocked_requests_post):
        ops = check_config(t_config_data)
        content = {
            "status": "success"
        }
        mocked_requests_post.return_value = generate_response(content, 200)

        expected_headers = {
            "content-type": "application/json",
            "cache-control": "no-cache",
            "Cookie": "JWTToken=mock_cookie_token",
            "X-Xsrf-Token": "mock_header_token"
        }
        actual_headers = get_authenticated_headers(ops.get("esm_url"), ops.get("esm_username"),
                                                   ops.get("esm_password"), ops.get("trust_cert"))

        assert expected_headers == actual_headers

    @patch("requests.post")
    def test_case_edit_case_details(self, mocked_requests_post):
        ops = check_config(t_config_data)
        content1 = {
            "status": "success"
        }
        content2 = {
            "dataSourceList": None,
            "assignedTo": 1,
            "orgId": 1,
            "closeTime": "08/22/2018 21:27:34",
            "eventList": [],
            "deviceList": None,
            "notes": [{
                "changes": [],
                "content": "",
                "username": "admin",
                "action": "Open",
                "timestamp": "08/22/2018 21:27:34(GMT)"
            }],
            "noteAdded": "",
            "history": [{
                "changes": [],
                "content": "",
                "username": "admin",
                "action": "Viewed",
                "timestamp": "08/22/2018 21:28:24(GMT)"
            }],
            "severity": 1,
            "summary": "test5",
            "openTime": "08/22/2018 21:27:34",
            "id": 8194,
            "statusId": {
                "value": 1
            }
        }
        mocked_requests_post.side_effect = [generate_response(content1, 200),
                                            generate_response(content2, 200),
                                            generate_response({}, 200)]

        payload = {"caseDetail": {
            "summary": "This is a new summary",
            "severity": "2"
        }}

        case_edit_case_details(ops, payload, 1)
        # Doesn't return anything, if it made it here it passed successfully
        assert True

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.parametrize(
        "mcafee_esm_edit_case_json, mcafee_esm_case_id, mcafee_esm_case_status, mcafee_esm_case_summary, mcafee_esm_case_severity, expected_results",
        [
            ({"type": "text", "content": '{"caseDetail": {"summary": "This is a new summary","severity": "2"}}'}, 1, None, None, None, {"inputs": {"mcafee_esm_case_id": 1, "mcafee_esm_case_severity": None, "mcafee_esm_case_status": None, "mcafee_esm_case_summary": None, "mcafee_esm_edit_case_json": '{"caseDetail": {"summary": "This is a new summary","severity": "2"}}'}})
        ])
    @patch("requests.post")
    def test_success(self, mocked_requests_post, circuits_app, mcafee_esm_edit_case_json, mcafee_esm_case_id, mcafee_esm_case_status,
                     mcafee_esm_case_summary, mcafee_esm_case_severity, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = {
            "mcafee_esm_edit_case_json": mcafee_esm_edit_case_json,
            "mcafee_esm_case_id": mcafee_esm_case_id,
            "mcafee_esm_case_status": mcafee_esm_case_status,
            "mcafee_esm_case_summary": mcafee_esm_case_summary,
            "mcafee_esm_case_severity": mcafee_esm_case_severity
        }

        content1 = {
            "status": "success"
        }
        content2 = {
            "dataSourceList": None,
            "assignedTo": 1,
            "orgId": 1,
            "closeTime": "08/22/2018 21:27:34",
            "eventList": [],
            "deviceList": None,
            "notes": [{
                "changes": [],
                "content": "",
                "username": "admin",
                "action": "Open",
                "timestamp": "08/22/2018 21:27:34(GMT)"
            }],
            "noteAdded": "",
            "history": [{
                "changes": [],
                "content": "",
                "username": "admin",
                "action": "Viewed",
                "timestamp": "08/22/2018 21:28:24(GMT)"
            }],
            "severity": 1,
            "summary": "test5",
            "openTime": "08/22/2018 21:27:34",
            "id": 8194,
            "statusId": {
                "value": 1
            }
        }
        mocked_requests_post.side_effect = [generate_response(content1, 200),
                                            generate_response(content2, 200),
                                            generate_response({}, 200)]

        results = call_mcafee_esm_edit_case_function(circuits_app, function_params)
        del results["metrics"]
        assert expected_results == results
