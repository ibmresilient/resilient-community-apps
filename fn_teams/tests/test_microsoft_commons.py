# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""
import os
import pytest

from urllib import parse
from unittest.mock import patch
from resilient_lib import RequestsCommon

from tests import testcommons
from tests.testcommons import required_parameters
from fn_teams.lib import constants, microsoft_commons
from fn_teams.lib.microsoft_groups import GroupsInterface


@pytest.fixture(scope="function")
def patch_generate_members(required_parameters: dict) -> dict:
    rest_client = testcommons.MockRestClient()
    rest_client.add_post_request(constants.RES_USERS, {
        "data" : testcommons.json_read(testcommons.PATH_RESILIENT_USERS)})
    rest_client.add_get_request(constants.RES_GROUPS,
        testcommons.json_read(testcommons.PATH_RESILIENT_GROUP))
    rest_client.add_get_request(parse.urljoin(
        constants.RES_INCIDENT, "2098/members"),{
        "members" : [20,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44]})
    parameters = required_parameters.copy()
    parameters["resclient"] = rest_client
    parameters["incident_id"] = "2098"
    parameters["add_members_from"] = "incident"
    yield parameters, testcommons.json_read(testcommons.PATH_RESILIENT_USERS)


def test_generate_member_list(patch_generate_members: tuple):
    required_parameters = patch_generate_members[0]
    expected_users = patch_generate_members[1]
    response = microsoft_commons.generate_member_list(
        resclient=required_parameters.get("resclient"),
        logger=required_parameters.get("logger"),
        task_id=required_parameters.get("task_id"),
        incident_id = required_parameters.get("incident_id"),
        add_members_from = required_parameters.get("add_members_from"),
        additional_members = required_parameters.get("additional_members"))
    for user in map(lambda user_info: user_info.get('email'), expected_users):
        assert user in response


def test_is_direct_member(required_parameters):
    user_list = testcommons.json_read(testcommons.PATH_RESILIENT_USERS)
    assert microsoft_commons.is_direct_member(31, user_list)
    assert microsoft_commons.is_direct_member(32, user_list)
    assert microsoft_commons.is_direct_member(33, user_list)
    assert not microsoft_commons.is_direct_member(1, user_list)
    assert not microsoft_commons.is_direct_member(2, user_list)
    assert not microsoft_commons.is_direct_member(3, user_list)


def test_is_group_member(required_parameters):
    user_list = testcommons.json_read(testcommons.PATH_RESILIENT_USERS)
    group_list = testcommons.json_read(testcommons.PATH_RESILIENT_GROUP)
    users = microsoft_commons.is_group_member(46, user_list, group_list)
    expected_users = list(
        filter(
            lambda groups: groups.get("id") == 46, group_list))[0].get("output_group_membrs")
    assert len(users) == 6
    for user in users:
        assert user in expected_users


def patch_read_user_info(method, url, headers, callback) -> dict:
    testcommons.check_request_parameters(
        method=method,
        url=url,
        headers=headers,
        callback=callback)
    user_info = testcommons.json_read(testcommons.PATH_MS_USERS)
    user = list(
        filter(lambda user: user_info[user].get("id") == url.split("/")[-1].strip(),
        user_info))

    url_sections = url.split("/")

    assert "graph.microsoft.com" in url_sections
    assert "v1.0" in url_sections
    assert "users" in url_sections

    if len(user) > 0:
        return user_info[user[0]]
    else:
        return user_info["Resilient User"]


@patch('resilient_lib.RequestsCommon.execute', side_effect=patch_read_user_info)
def test_read_user_info(patch_rc, required_parameters: dict):
    user_info = testcommons.json_read(testcommons.PATH_MS_USERS)
    finder = microsoft_commons.MSFinder(
        rc=required_parameters.get("rc"),
        rh=microsoft_commons.ResponseHandler(),
        headers=required_parameters.get("header"))
    for user in user_info:
        finder.find_user(user_info[user].get("id"))
