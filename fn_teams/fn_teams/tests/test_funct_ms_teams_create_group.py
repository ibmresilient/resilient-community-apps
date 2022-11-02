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
from fn_teams.lib.microsoft_authentication import MicrosoftAuthentication


PACKAGE_NAME = constants.FN_NAME
FUNCTION_NAME = "ms_teams_create_group"
APP_CONFIG = {
    "directory_id"   : "1d8a5928-8678-408e-ab06-50ca7e01766a",
    "application_id" : "18d10049-72e3-4652-ac9f-d9b13f24303c",
    "secret_value"   : "oCN8Q~1I0dFCI_x1kI6EseRxeTmNazVJboA0ZaMF"}

PATH_TEST_DATA = os.path.join(os.path.abspath(os.path.dirname(__file__)), "data")
PATH_MS_USERS = os.path.join(PATH_TEST_DATA, "find_all_users.json")
PATH_WRITE_GROUPS_JSON = os.path.join(PATH_TEST_DATA, "write_group.json")
PATH_RESILIENT_USERS = os.path.join(PATH_TEST_DATA, "resilient_users.json")
PATH_RESILIENT_GROUP = os.path.join(PATH_TEST_DATA, "resilient_groups.json")


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


@pytest.fixture(scope="function")
def patch_generate_members(required_parameters: dict) -> dict:
    rest_client = testcommons.MockRestClient()
    rest_client.add_post_request(constants.RES_USERS, {
        "data" : testcommons.json_read(PATH_RESILIENT_USERS)})
    rest_client.add_get_request(constants.RES_GROUPS,
        testcommons.json_read(PATH_RESILIENT_GROUP))
    rest_client.add_get_request(parse.urljoin(
        constants.RES_INCIDENT, "2098/members"),{
        "members" : [20,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44]})
    parameters = required_parameters.copy()
    parameters["resclient"] = rest_client
    parameters["incident_id"] = "2098"
    parameters["add_members_from"] = "incident"
    yield parameters, testcommons.json_read(PATH_RESILIENT_USERS)


def patch_write_group(method, url, data, headers, callback):
    body = testcommons.check_request_parameters(
        method=method,
        url=url,
        body=data,
        headers=headers,
        callback=callback)
    response = testcommons.json_read(PATH_WRITE_GROUPS_JSON).get("response")
    assert url == response.get("url")
    assert False not in [body.get(key) == response.get(key) for key in body]
    return response


def patch_read_user_info(method, url, headers, callback) -> dict:
    testcommons.check_request_parameters(
        method=method,
        url=url,
        headers=headers,
        callback=callback)
    user_info = testcommons.json_read(PATH_MS_USERS)
    user = list(
        filter(lambda user: user_info[user].get("id") == url.split("/")[-1].strip(),
        user_info))
    if len(user) > 0:
        return user_info[user[0]]
    else:
        return user_info["Resilient User"]


@patch('resilient_lib.RequestsCommon.execute', side_effect=patch_write_group)
def test_write_group(patch_rc, required_parameters):
    gi = GroupsInterface(required_parameters)
    group_details = testcommons.json_read(PATH_WRITE_GROUPS_JSON).get("request")
    response = gi._write_group(
        description=group_details.get("description"),
        displayName=group_details.get("displayName"),
        mailNickname=group_details.get("mailNickname"),
        owners=group_details.get("owners@odata.bind"),
        members=group_details.get("members@odata.bind"))
    assert response


def test_generate_member_list(patch_generate_members: tuple):
    expected_users = patch_generate_members[1]
    gi = GroupsInterface(patch_generate_members[0])
    gi._generate_member_list()
    for user in map(lambda user_info: user_info.get('email'), expected_users):
        assert user in gi.members_email_ids


def test_is_direct_member(required_parameters):
    user_list = testcommons.json_read(PATH_RESILIENT_USERS)
    gi = GroupsInterface(required_parameters)
    assert gi._is_direct_member(31, user_list)
    assert gi._is_direct_member(32, user_list)
    assert gi._is_direct_member(33, user_list)
    assert not gi._is_direct_member(1, user_list)
    assert not gi._is_direct_member(2, user_list)
    assert not gi._is_direct_member(3, user_list)


def test_is_group_member(required_parameters):
    user_list = testcommons.json_read(PATH_RESILIENT_USERS)
    group_list = testcommons.json_read(PATH_RESILIENT_GROUP)
    gi = GroupsInterface(required_parameters)
    users = gi._is_group_member(46, user_list, group_list)
    expected_users = list(
        filter(
            lambda groups: groups.get("id") == 46, group_list))[0].get("output_group_membrs")
    assert len(users) == 6
    for user in users:
        assert user in expected_users


@patch('resilient_lib.RequestsCommon.execute', side_effect=patch_read_user_info)
def test_read_user_info(patch_rc, required_parameters: dict):
    gi = GroupsInterface(required_parameters)
    user_info = testcommons.json_read(PATH_MS_USERS)
    for user in user_info:
        print(gi._read_user_info(user_info[user].get("id")))