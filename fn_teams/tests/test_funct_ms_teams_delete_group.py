# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""
import pytest
from unittest.mock import patch
from resilient_lib import IntegrationError
from tests import testcommons
from fn_teams.lib.microsoft_groups import GroupsInterface
from tests.testcommons import required_parameters


def patch_delete_group(method, url, headers, callback, proxies=None):
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

    elif method == "delete":
        print(url)
        url_sections = url.split("/")
        assert "graph.microsoft.com" in url_sections
        assert 'v1.0' in url_sections
        assert "groups" in url_sections
        assert ret["value"][0]["id"] in url_sections
        return {"status_code" : 204}


@patch('resilient_lib.RequestsCommon.execute', side_effect=patch_delete_group)
def test_delete_group(patch, required_parameters):
    gi = GroupsInterface(required_parameters)
    gi.delete_group({
        "group_mail_nickname" : "MailBoxs@5rf2xs.onmicrosoft.com"})

    gi.delete_group({
        "group_mail_nickname" : "MailBoxs"})

    gi.delete_group({
        "group_name" : "Unittest Group1"})

    gi.delete_group({
        "group_id": "40bd9442-ca0f-4c7c-ba64-5e0fa56f3fb9"})

    with pytest.raises(IntegrationError):
        gi.delete_group({"group_mail_nickname" : ""})

    with pytest.raises(IntegrationError):
        gi.delete_group({"group_name" : ""})

    with pytest.raises(IntegrationError):
        gi.delete_group({"group_id" : ""})

    with pytest.raises(IntegrationError):
        gi.delete_group({"id": ""})
