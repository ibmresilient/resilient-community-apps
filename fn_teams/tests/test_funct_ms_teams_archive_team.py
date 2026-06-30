# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""
import os
import logging
import pytest
from unittest.mock import patch
from resilient_lib import RequestsCommon, IntegrationError
from tests import testcommons
from fn_teams.lib import constants
from fn_teams.lib.microsoft_teams import TeamsInterface


PACKAGE_NAME = constants.PACKAGE_NAME
FUNCTION_NAME = "ms_teams_archive_teams"

PATH_TEST_DATA = os.path.join(os.path.abspath(os.path.dirname(__file__)), "data")
PATH_MS_GROUP = os.path.join(PATH_TEST_DATA, "find_group.json")


@pytest.fixture(scope="function")
def required_parameters():
    log = logging.getLogger(__name__)
    log.setLevel(logging.INFO)
    log.addHandler(logging.StreamHandler())
    header = {
        'Authorization': 'Bearer ID123',
        'Content-type': 'application/json'}
    yield {
        "rc" : RequestsCommon(),
        "logger" : log,
        "header" : header,
        "resclient" : None}


def patch_archive_unarchive_team(method, url, headers, callback, proxies=None):
    ret = testcommons.json_read(PATH_MS_GROUP)
    testcommons.check_request_parameters(
        method=method,
        url=url,
        headers=headers,
        callback=callback)

    if method == "get":
        if "=" in url:
            base_url, query = url.split("=")
            assert base_url == "https://graph.microsoft.com/v1.0/groups?$filter"
            assert "mailNickname" in query or "displayName" in query
        else:
            query = "id"
            assert "https://graph.microsoft.com/v1.0/groups/" in url
            assert url.split("/")[-1].strip() == ret["value"][0]["id"]
            response = ret["value"][0]
            response["status_code"] = 200
            return response

        if "mailNickname" in query:
            assert "@" not in query
            assert query.split("eq")[-1].strip().replace("'", "") == ret["value"][0]["mailNickname"]
        elif "displayName" in query:
            assert query.split("eq")[-1].strip().replace("'", "") == ret["value"][0]["displayName"]
        return ret

    elif method == "post":
        print(url)
        url_sections = url.split("/")
        assert "archive" in url_sections or "unarchive" in url_sections
        assert "graph.microsoft.com" in url_sections
        assert 'v1.0' in url_sections
        assert "teams" in url_sections
        assert ret["value"][0]["id"] in url_sections
        return {"status_code" : 204}


@patch('resilient_lib.RequestsCommon.execute', side_effect=patch_archive_unarchive_team)
def test_delete_group(patch, required_parameters):
    ti = TeamsInterface(required_parameters)
    ti.archive_unarchive_team({
        "operation" : "archive",
        "group_mail_nickname" : "MailBoxs@5rf2xs.onmicrosoft.com"})

    ti.archive_unarchive_team({
        "operation" : "unarchive",
        "group_mail_nickname" : "MailBoxs"})

    ti.archive_unarchive_team({
        "operation" : "archive",
        "group_name" : "Unittest Group1"})

    ti.archive_unarchive_team({
        "operation" : "unarchive",
        "group_id": "40bd9442-ca0f-4c7c-ba64-5e0fa56f3fb9"})

    with pytest.raises(IntegrationError):
        ti.archive_unarchive_team({
        "operation" : "archive",
        "group_mail_nickname" : ""})

    with pytest.raises(IntegrationError):
        ti.archive_unarchive_team({
        "operation" : "unarchive",
        "group_name" : ""})

    with pytest.raises(IntegrationError):
        ti.archive_unarchive_team({
        "operation" : "archive",
        "group_id" : ""})

    with pytest.raises(IntegrationError):
        ti.archive_unarchive_team({
        "operation" : "unarchive",
        "id": ""})
