# -*- coding: utf-8 -*-
"""Tests APIs using both mocked endpoints and livetests"""

import json
import os
import datetime
from sys import api_version
from unittest import mock

import pytest
import requests_mock
from fn_randori.lib.app_common import (AppCommon, PACKAGE_NAME, 
                                       GET_VALIDATE_URI,
                                       GET_ALL_DETECTIONS_FOR_TARGET_URI)
from resilient_lib import RequestsCommon

APP_CONFIG = {
    "api_token": "abcd-efgh",
    "api_version": "v1",
    "endpoint_url": "https://fake.app.randori.io",
    "tenant_name": "my-randori-tenant",
    "polling_interval": 60,
    "polling_lookback": 120,
    "verify": "false"
}

BASE_MOCK_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "mock_data")
PATH_VALIDATE_MOCK = os.path.join(BASE_MOCK_PATH, "GET_validate.json")
PATH_DETECTIONS_MOCK = os.path.join(BASE_MOCK_PATH, "GET_detections.json")
URI_GET_VALIDATE="{}{}".format(APP_CONFIG.get("endpoint_url"),
                               GET_VALIDATE_URI.format(api_version="v1"))
URI_GET_DETECTIONS="{}{}{}".format(APP_CONFIG.get("endpoint_url"),
                                   GET_ALL_DETECTIONS_FOR_TARGET_URI.format(api_version="v1"), 
                                   "?q=eyJjb25kaXRpb24iOiAiQU5EIiwgInJ1bGVzIjogW119&limit=2000&offset=0")

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
        mock_api.register_uri("GET", url=URI_GET_VALIDATE, 
                              json=load_json(PATH_VALIDATE_MOCK), status_code=200)
        mock_api.register_uri("GET", url=URI_GET_DETECTIONS,
                              json=load_json(PATH_DETECTIONS_MOCK), status_code=200)
        yield mock_api


@pytest.fixture(scope="module")
def app_common():
    rc = RequestsCommon()
    yield AppCommon(rc, PACKAGE_NAME, APP_CONFIG)

def test_make_headers(app_common: AppCommon):
    headers = app_common._make_header("api_token")

    assert headers == { 'Content-Type': 'application/json',  'Authorization': "Bearer api_token" }

def test_get_validate(mock_api: requests_mock.Mocker, app_common: AppCommon):
    resp = app_common.get_validate()

    assert resp
    assert mock_api.called_once
    assert resp["username"] == "user@example.com"
    assert "authenticated" in resp["perms"]

def test_get_detections_for_target(mock_api: requests_mock.Mocker, app_common: AppCommon):
    query =  {
            'condition': "AND",
            'rules': []
    }
    resp = app_common.get_detections_for_target(query)
    assert resp
    assert mock_api.called_once
    assert resp[0]["priority_score"] == 146.4
    assert resp[0]["target_first_seen"] == "2022-07-07T07:19:09.157578+00:00"