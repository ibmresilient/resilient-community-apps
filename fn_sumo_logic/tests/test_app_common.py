# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
"""Tests APIs using both mocked endpoints and livetests"""

import json
import os
import pytest
from fn_sumo_logic.lib.app_common import (AppCommon, PACKAGE_NAME)
from resilient_lib import RequestsCommon

API_TOKEN = "12345690XYZ"
APP_CONFIG = {
    "access_id": "aaa-bbb-ccc",
    "access_key": "abcdefghijk",
    "api_endpoint_url": "https://api.sumologic.com/api/",
    "console_url": "https://service.sumologic.com",
    "polling_interval": 60,
    "polling_lookback": 120
}

BASE_MOCK_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "mock_data")

def load_json(path_file):
    with open(path_file, "r") as json_file:
        json_data = json_file.read()
    
    return json.loads(json_data)

@pytest.fixture(scope="module")
def app_common():
    yield AppCommon(PACKAGE_NAME, APP_CONFIG)

def test_make_headers(app_common: AppCommon):
    headers = app_common._make_headers()

    assert headers
    assert len(headers) == 2
    assert headers["Authorization"] == "Basic YWFhLWJiYi1jY2M6YWJjZGVmZ2hpams="
    assert headers["Content-Type"] == "application/json"

