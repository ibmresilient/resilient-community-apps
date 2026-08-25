# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""
import pytest, random
from unittest.mock import patch
from resilient_lib import IntegrationError
from tests import testcommons
from fn_teams.lib.microsoft_teams import TeamsInterface
from tests.testcommons import required_parameters


def patch_build_member_format(method, url, headers, callback, proxies=None) -> dict:
    testcommons.check_request_parameters(
        method=method,
        url=url,
        headers=headers,
        callback=callback)
    user_info = testcommons.json_read(testcommons.PATH_MS_USERS)
    try:
        user = next(
            filter(lambda user: user_info[user].get("mail") == url.split("/")[-1].strip(),
            user_info))
        return user_info.get(user)
    except StopIteration:
        return {}


def expected_format(email, owner=False):
    user_info = testcommons.json_read(testcommons.PATH_MS_USERS)
    user = next(
        filter(lambda user: user_info[user].get("mail") == email,
        user_info))
    id_value = user_info.get(user).get("id")
    return {
        '@odata.type': '#microsoft.graph.aadUserConversationMember',
        'roles': ["owner"] if owner else [],
        'user@odata.bind': f"https://graph.microsoft.com/v1.0/users('{id_value}')"}


@patch('resilient_lib.RequestsCommon.execute', side_effect=patch_build_member_format)
def test_build_member_format(patch_rc, required_parameters):

    ti = TeamsInterface(required_parameters)

    user_email = "LeeG@5rf2xs.onmicrosoft.com"
    member_format = ti._build_member_format(user_email)
    assert expected_format(user_email) == member_format

    user_email = "LeeG@5rf2xs.onmicrosoft.com"
    member_format = ti._build_member_format(user_email, True)
    assert expected_format(user_email, True) == member_format

    with pytest.raises(IntegrationError):
        user_email = "admin@example.com"
        member_format = ti._build_member_format(user_email, True)


def patch_add_members(method, url, headers, callback, data=None, proxies=None) -> dict:
    body = testcommons.check_request_parameters(
        method=method,
        url=url,
        body=data,
        headers=headers,
        callback=callback)

    if method == "get":
        user_info = testcommons.json_read(testcommons.PATH_MS_USERS)
        try:
            user = next(
                filter(lambda user: user_info[user].get("mail") == url.split("/")[-1].strip(),
                user_info))
            return user_info.get(user)
        except StopIteration:
            return {}

    elif method == "post":
        print(body)
        assert body.get("values")
        assert len(body.get("values")) == 3

        for user in body.get("values"):
            assert "@odata.type" in user
            assert "roles" in user
            assert "user@odata.bind" in user
            assert user.get("@odata.type") == "#microsoft.graph.aadUserConversationMember"
            assert "https://graph.microsoft.com/v1.0/users" in user.get("user@odata.bind")


@patch('resilient_lib.RequestsCommon.execute', side_effect=patch_add_members)
def test_add_members(patch_rc, required_parameters):
    ti = TeamsInterface(required_parameters)
    users = [
        "LeeG@5rf2xs.onmicrosoft.com",
        "IsaiahL@5rf2xs.onmicrosoft.com",
        "JoniS@5rf2xs.onmicrosoft.com"]

    member_list = [ti._build_member_format(user, random.choice([True, False])) for user in users]
    ti._add_members("ID123123", member_list)
