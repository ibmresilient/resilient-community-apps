# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""
import pytest
from unittest.mock import patch
from resilient_lib import IntegrationError
from tests import testcommons
from fn_teams.lib.microsoft_teams import TeamsInterface
from tests.testcommons import required_parameters


def patch_archive_unarchive_team(method, url, headers, callback, data=None, proxies=None):
    ret = testcommons.json_read(testcommons.PATH_MS_GROUP)
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

    elif method == "put":
        print(url)
        url_sections = url.split("/")
        assert "team" in url_sections and "groups" in url_sections
        assert "graph.microsoft.com" in url_sections
        assert 'v1.0' in url_sections
        assert ret["value"][0]["id"] in url_sections
        return {"status_code" : 204}


@patch('resilient_lib.RequestsCommon.execute', side_effect=patch_archive_unarchive_team)
def test_delete_group(patch, required_parameters):
    ti = TeamsInterface(required_parameters)
    ti.enable_team_group({
        "group_mail_nickname" : "MailBoxs@5rf2xs.onmicrosoft.com"})

    ti.enable_team_group({
        "group_mail_nickname" : "MailBoxs"})

    ti.enable_team_group({
        "group_name" : "Unittest Group1"})

    ti.enable_team_group({
        "group_id": "40bd9442-ca0f-4c7c-ba64-5e0fa56f3fb9"})

    with pytest.raises(IntegrationError):
        ti.enable_team_group({
            "group_mail_nickname" : ""})

    with pytest.raises(IntegrationError):
        ti.enable_team_group({
            "group_name" : ""})

    with pytest.raises(IntegrationError):
        ti.enable_team_group({
            "group_id" : ""})

    with pytest.raises(IntegrationError):
        ti.enable_team_group({
            "id": ""})
