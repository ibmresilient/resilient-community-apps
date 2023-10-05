# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""
from unittest.mock import patch
from tests import testcommons
from fn_teams.lib.microsoft_groups import GroupsInterface
from tests.testcommons import required_parameters


def patch_write_group(method, url, data, headers, callback):
    body = testcommons.check_request_parameters(
        method=method,
        url=url,
        body=data,
        headers=headers,
        callback=callback)
    response = testcommons.json_read(testcommons.PATH_WRITE_GROUPS_JSON).get("response")
    assert url == response.get("url")
    assert False not in [body.get(key) == response.get(key) for key in body]
    return response


@patch('resilient_lib.RequestsCommon.execute', side_effect=patch_write_group)
def test_write_group(patch_rc, required_parameters):
    gi = GroupsInterface(required_parameters)
    group_details = testcommons.json_read(testcommons.PATH_WRITE_GROUPS_JSON).get("request")
    response = gi._write_group(
        description=group_details.get("description"),
        displayName=group_details.get("displayName"),
        mailNickname=group_details.get("mailNickname"),
        owners=group_details.get("owners@odata.bind"),
        members=group_details.get("members@odata.bind"))
    assert response
