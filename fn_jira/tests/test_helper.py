#!/usr/bin/env python
# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
import mock
from fn_jira.util.helper import validate_app_configs, validate_task_id_for_jira_issue_id

def test_validate_app_configs():
    mock_app_configs = {
        "url": "www.example.com",
        "auth_method": "BASIC",
        "user": "exampleuser",
        "password": "examplepassword",
        "verify_cert": "true"
    }

    valid_app_configs = validate_app_configs(mock_app_configs)

    assert valid_app_configs.get("url") == "www.example.com"
    assert valid_app_configs.get("user") == "exampleuser"
    assert valid_app_configs.get("auth_method") == "BASIC"
    assert valid_app_configs.get("password") == "examplepassword"
    assert valid_app_configs.get("verify_cert") is True

def test_validate_task_id_for_jira_issue_id():
    mock_fn_inputs = {"jira_issue_id": "INT-9"}
    mock_app_config = {"jira_dt_name": "jira_task_references"}
    with mock.patch("fn_jira.util.helper._get_jira_issue_id") as mock_dt_call:
        mock_dt_call.return_value = ("INT-10", "https://jira.test/INT-10")
        valid = validate_task_id_for_jira_issue_id(None, mock_app_config, "100", "101", mock_fn_inputs)
        assert valid
        assert mock_fn_inputs["jira_issue_id"] == "INT-10"

def test_invalid_validate_task_id_for_jira_issue_id():
    mock_fn_inputs = {"jira_issue_id": "INT-9"}
    mock_app_config = {"jira_dt_name": "jira_task_references"}
    with mock.patch("fn_jira.util.helper._get_jira_issue_id") as mock_dt_call:
        mock_dt_call.return_value = (None, None)
        valid = validate_task_id_for_jira_issue_id(None, mock_app_config, "100", "101", mock_fn_inputs)
        assert not valid
