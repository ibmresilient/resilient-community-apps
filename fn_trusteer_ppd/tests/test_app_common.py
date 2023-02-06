# -*- coding: utf-8 -*-
"""Tests APIs using both mocked endpoints and livetests"""

import json
import os
from unittest import mock

import pytest
import requests_mock
from fn_trusteer_ppd.lib.app_common import (AppCommon, PACKAGE_NAME, LINKBACK_URL)

APP_CONFIG = {
    "api_token": "abcd-efgh",
    "api_version": "v1",
    "endpoint_url": "https://fake.trusteer.com",
    "verify": "true"
}

BASE_MOCK_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "mock_data")

def load_json(path_file):
    with open(path_file, "r") as json_file:
        json_data = json_file.read()
    
    return json.loads(json_data)

@pytest.fixture(scope="function")
def mock_api():
    # create a requests mock and intercept each of the endpoints that have been implemented
    # note that requests to endpoints outside the scope of these that have been implemented
    # will return 
    with requests_mock.Mocker() as mock_api:
        yield mock_api


@pytest.fixture(scope="module")
def app_common():
    yield AppCommon(PACKAGE_NAME, APP_CONFIG)

def test_make_headers(app_common: AppCommon):
    headers = app_common._make_header("api_token")

    assert headers == { 'Content-Type': 'application/json',  'Authorization': "Bearer api_token" }

def test_make_linkback_url(app_common: AppCommon):
    pu_id = "aaaa-bbbb-cccc-dddd"
    device_id = "aaaa-bbbb-1111-2222"
    puid_url = app_common.make_linkback_url(id=pu_id, id_type='puid')
    device_id_url = app_common.make_linkback_url(id=device_id, id_type='device_id')

    assert puid_url == LINKBACK_URL.format(base_url=APP_CONFIG.get('endpoint_url'), id=pu_id, id_type='puid')
    assert device_id_url == LINKBACK_URL.format(base_url=APP_CONFIG.get('endpoint_url'), id=device_id, id_type='device_id')