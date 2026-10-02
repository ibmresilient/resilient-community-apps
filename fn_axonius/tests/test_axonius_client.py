# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
"""Tests APIs using both mocked endpoints and livetests"""

import json
import os
from unittest import mock

import pytest
import requests_mock
from fn_axonius.lib.axonius_client import (AxoniusClient, PACKAGE_NAME)
from resilient_lib import RequestsCommon

API_KEY = "12345690XYZ"
API_SECRET = "ABCDEFGXYZ"

APP_CONFIG = {
"endpoint_url": "https://myaccount.on.axonius.com",
"api_key": API_KEY,
"api_secret": API_SECRET,
"api_version": "v2"
}

BASE_MOCK_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "mock_data")

def load_json(path_file):
    with open(path_file, "r") as json_file:
        json_data = json_file.read()
    
    return json.loads(json_data)

@pytest.fixture(scope="module")
def axonius_client():
    rc = RequestsCommon()
    yield AxoniusClient(rc, PACKAGE_NAME, APP_CONFIG)

def test_make_headers(axonius_client: AxoniusClient):
    headers = axonius_client._make_headers(APP_CONFIG.get("api_key"), APP_CONFIG.get("api_secret"))

    assert headers == { "api-key": API_KEY,
                        "api-secret": API_SECRET,
                        "accept": "application/json",
                        "content-type": "application/json"
                      }
