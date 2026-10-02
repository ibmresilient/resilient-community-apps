# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
"""Tests APIs using both mocked endpoints and livetests"""

import json
import os
from unittest import mock

import pytest
import requests_mock
from fn_vmware_cbc.lib.app_common import (AppCommon, PACKAGE_NAME, ENTITY_COMMENT_HEADER)
from resilient_lib import RequestsCommon

API_TOKEN = "12345690XYZ/ABCDEFGH"
APP_CONFIG = {
    "api_id": "ABCDEFGH",
    "api_secret": "12345690XYZ",
    "org_key": "ABCDEFG",
    "endpoint_url": "https://defense.conferdeploy.net",
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
    token = "{0}/{1}".format(APP_CONFIG.get("api_secret"),APP_CONFIG.get("api_id"))
    headers = app_common._make_headers(token)

    assert headers == {'X-AUTH-TOKEN': API_TOKEN,
                       'Content-Type': 'application/json'}
    
def test_format_cbc_note(app_common: AppCommon):

    note_text = "Test note text"
    note = {
            "author":"user@example.com",
            "create_timestamp":"2024-04-23T20:38:19.436Z",
            "last_update_timestamp":"2024-04-23T20:38:19.436Z",
            "id":"12345612-0c0c-4c4c-b0b0-1234abcd",
            "source":"CUSTOMER",
            "note": note_text,
            "note_json_format": None
    }
    formatted_note = app_common.format_cbc_note(note)
    author = note.get("author")
    created_at = note.get("create_timestamp")
    standard_note = f"<b>{ENTITY_COMMENT_HEADER}:</b><br><br><b>Note added by<br>{author}</b><br>{created_at}<br><br>{note_text}"
    # assert
    assert formatted_note == standard_note