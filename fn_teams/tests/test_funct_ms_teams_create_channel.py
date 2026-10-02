# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""
import pytest
from unittest.mock import patch
from resilient_lib import IntegrationError
from tests import testcommons
from tests.testcommons import required_parameters
from fn_teams.lib.microsoft_channels import ChannelInterface


def patch_create_channel(method, url, headers, callback, data=None, proxies=None):
    ret = testcommons.json_read(testcommons.PATH_MS_GROUP)
    body = testcommons.check_request_parameters(
        method=method,
        url=url,
        body=data,
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
        print(body)
        print(url)
        url_sections = url.split("/")
        assert "graph.microsoft.com" in url_sections
        assert 'v1.0' in url_sections
        assert "teams" in url_sections
        assert "channels" in url_sections
        assert ret["value"][0]["id"] in url_sections
        assert "displayName" in body and body.get("displayName")
        assert "description" in body and body.get("description")
        return {"status_code" : 201}

@patch('resilient_lib.RequestsCommon.execute', side_effect=patch_create_channel)
def test_create_channel(patch, required_parameters):
    ci = ChannelInterface(required_parameters)
    ci.create_channel({
        "displayName" : "ChannelTest",
        "description" : "Test description",
        "group_mail_nickname" : "MailBoxs@5rf2xs.onmicrosoft.com"})

    with pytest.raises(AssertionError):
        ci.create_channel({
            "description" : "Test description",
            "group_mail_nickname" : "MailBoxs"})

    with pytest.raises(AssertionError):
        ci.create_channel({
            "displayName" : "ChannelTest",
            "group_mail_nickname" : "MailBoxs"})

    with pytest.raises(IntegrationError):
        ci.create_channel({
            "displayName" : "ChannelTest",
            "description" : "Test description"})
