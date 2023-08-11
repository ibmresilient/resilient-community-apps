# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
"""Tests APIs using both mocked endpoints and livetests"""

import json
import os
from unittest import mock

import pytest
import requests_mock
from fn_salesforce.lib.app_common import (AppCommon, PACKAGE_NAME, TOKEN_URL)
from resilient_lib import RequestsCommon

APP_CONFIG = {
    "my_domain_url": "company.develop.my.salesforce.com",
    "my_domain_name": "company.develop",
    "api_version": "v58.0",
    "consumer_key": "12345690XYZ",
    "consumer_secret": "0DF1234ABCDEFG",
    "polling_interval": 0,
    "polling_lookback": 0,
    "verify": "false"
}

BASE_MOCK_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "mock_data")
PATH_TOKEN_MOCK = os.path.join(BASE_MOCK_PATH, "POST_token.json")
TOKEN_URL_MOCK = TOKEN_URL.format(my_domain_url=APP_CONFIG.get("my_domain_url"))

def load_json(path_file):
    with open(path_file, "r") as json_file:
        json_data = json_file.read()
    
    return json.loads(json_data)

@pytest.fixture(scope="function")
def fx_setup_mock_api():
    # create a requests mock and intercept each of the endpoints that have been implemented
    # note that requests to endpoints outside the scope of these that have been implemented
    # will return 

    with requests_mock.Mocker() as mock_api:
        mock_api.register_uri("POST", "https://company.develop.my.salesforce.com/services/oauth2/token", json=load_json(PATH_TOKEN_MOCK), status_code=200)
        rc = RequestsCommon()
        yield AppCommon(PACKAGE_NAME, APP_CONFIG), mock_api

def test_make_headers(fx_setup_mock_api):
    app_common = fx_setup_mock_api[0]
    mock_api = fx_setup_mock_api[1]
    headers = app_common._make_headers("mock_token")

    assert headers == { 'Content-Type': 'application/json',  'Authorization': "Bearer mock_token" }
