# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""
import os
import logging
import json
import pytest

from urllib import parse
from unittest.mock import patch
from resilient_lib import RequestsCommon

from tests import testcommons
from fn_teams.lib import constants
from fn_teams.lib.microsoft_groups import GroupsInterface


PACKAGE_NAME = constants.PACKAGE_NAME
FUNCTION_NAME = "ms_teams_delete_group"

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


def patch_delete_group(method, url, headers, callback):
    ret = testcommons.json_read(PATH_MS_GROUP)
    body = testcommons.check_request_parameters(
        method=method,
        url=url,
        headers=headers,
        callback=callback)
    
    if method == "get":
        base_url, query = url.split("=")
        assert base_url == "https://graph.microsoft.com/v1.0/groups?$filter"
        assert "mailNickname" in query or "displayName" in query
        if "mailNickname" in query:
            assert "@" not in query
            assert query.split("eq")[-1].strip().replace("'", "") == ret["value"][0]["mailNickname"]
        elif "displayName" in query:
            assert query.split("eq")[-1].strip().replace("'", "") == ret["value"][0]["displayName"]
        return ret
    
    elif method == "delete":
        url_sections = url.split("/")
        assert "graph.microsoft.com" in url_sections
        assert "groups" in url_sections
        assert ret["value"][0]["id"] in url_sections
        return {
            "status_code" : 204}


@patch('resilient_lib.RequestsCommon.execute', side_effect=patch_delete_group)
def test_delete_group(patch, required_parameters):
    gi = GroupsInterface(required_parameters)
    gi.delete_group({
        "group_mail_nickname" : "MailBoxs@5rf2xs.onmicrosoft.com"})

    gi.delete_group({
        "group_mail_nickname" : "MailBoxs"})

    with pytest.raises(AssertionError):
        gi.delete_group({"group_mail_nickname" : "----"})