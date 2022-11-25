# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""
import os
import logging
import json
import pytest

from urllib import parse
from unittest.mock import patch
from resilient_lib import RequestsCommon, IntegrationError

from tests import testcommons
from fn_teams.lib import constants
from tests.testcommons import required_parameters
from fn_teams.lib.microsoft_channels import ChannelInterface

PACKAGE_NAME = constants.PACKAGE_NAME
FUNCTION_NAME = "ms_teams_archive_teams"

PATH_TEST_DATA = os.path.join(os.path.abspath(os.path.dirname(__file__)), "data")
PATH_MS_GROUP = os.path.join(PATH_TEST_DATA, "find_group.json")


def patch_archive_unarchive_team(method, url, headers, callback):
    ret = testcommons.json_read(PATH_MS_GROUP)
    testcommons.check_request_parameters(
        method=method,
        url=url,
        headers=headers,
        callback=callback)
    
    if method == "get":
        if "groups" in url:
            base_url, query = url.split("=")
            assert base_url == "https://graph.microsoft.com/v1.0/groups?$filter"
            assert "mailNickname" in query or "displayName" in query
        else:
            query = "id"
            assert "https://graph.microsoft.com/v1.0/" in url
            assert url.split("/")[-1] == "channels"
            assert url.split("/")[-2].strip() == ret["value"][0]["id"]
            ret["status_code"] = 204
            return ret

        if "mailNickname" in query:
            assert "@" not in query
            assert query.split("eq")[-1].strip().replace("'", "") == ret["value"][0]["mailNickname"]
        elif "displayName" in query:
            assert query.split("eq")[-1].strip().replace("'", "") == ret["value"][0]["displayName"]
        return ret

    elif method == "delete":
        url_sections = url.split("/")
        assert "channels" in url_sections
        assert "graph.microsoft.com" in url_sections
        assert 'v1.0' in url_sections
        assert "teams" in url_sections
        assert ret["value"][0]["id"] in url_sections
        return {"status_code" : 204}


@patch('resilient_lib.RequestsCommon.execute', side_effect=patch_archive_unarchive_team)
def test_delete_group(patch, required_parameters):
    ci = ChannelInterface(required_parameters)
    ci.delete_channel({
        "channel_name" : "Unittest Group1",
        "group_mail_nickname" : "MailBoxs@5rf2xs.onmicrosoft.com"})

    ci.delete_channel({
        "channel_name" : "Unittest Group1",
        "group_mail_nickname" : "MailBoxs"})

    ci.delete_channel({
        "channel_name" : "Unittest Group1",
        "group_name" : "Unittest Group1"})

    with pytest.raises(AssertionError):
        ci.delete_channel({
            "channel_name" : "Unittest Group1",
            "group_mail_nickname" : ""})

    with pytest.raises(AssertionError):
        ci.delete_channel({
            "channel_name" : "Unittest Group1",
            "group_name" : ""})

    with pytest.raises(IntegrationError):
        ci.delete_channel({
            "channel_name" : "Unittest Group1",
            "id": ""})
