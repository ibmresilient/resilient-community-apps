# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""
import os
import pytest
from unittest.mock import patch

from tests import testcommons
from fn_teams.lib import constants
from fn_teams.lib.microsoft_messages import MessageClient
from tests.testcommons import required_parameters

PACKAGE_NAME = constants.PACKAGE_NAME
FUNCTION_NAME = "ms_teams_read_message"

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
            assert "https://graph.microsoft.com/v1.0/groups" in url
        elif "channels":
            assert "teams" in url
            assert "graph.microsoft.com/v1.0" in url
        return ret


@patch('resilient_lib.RequestsCommon.execute', side_effect=patch_archive_unarchive_team)
def test_delete_group(patch, required_parameters):
    mi = MessageClient(required_parameters.get("rc"))

    dual_headers ={
        "application" : {'Authorization': 'Bearer id123', 'Content-type': 'application/json'},
        "delegated"   : {'Authorization': 'Bearer id123', 'Content-type': 'application/json'}}
    options = {"channel_name" : "Unittest Group1", "group_id" : "1234"}
    mi.read_messages(dual_headers, options)
