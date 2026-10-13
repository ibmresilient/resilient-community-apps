# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
"""Tests APIs using both mocked endpoints and livetests"""

import json
import os
from unittest import mock

import pytest
import requests_mock
from fn_rapid7_insight_idr.lib.app_common import (AppCommon, PACKAGE_NAME)
from resilient_lib import RequestsCommon

API_TOKEN = "12345690XYZ"
APP_CONFIG = {
    "region": "us",
    "api_version": "v2",
    "api_token": API_TOKEN,
    "org_token": "EXEXEXEX",
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
    rc = RequestsCommon()
    yield AppCommon(rc, PACKAGE_NAME, APP_CONFIG)

def test_make_headers(app_common: AppCommon):
    headers = app_common._make_headers(APP_CONFIG.get("api_token"))

    assert headers == { "X-Api-Key": API_TOKEN,
                        "Accept-Version": "strong-force-preview",
                        "Content-type": "application/json"
                      }


def test_rapid7_insight_idr_comment(app_common: AppCommon):
    comment = {
        "attachments": [],
        "body": "Here is my comment.",
        "target": "rrn:investigation:us:01234567-89ab-cdef-0000-123123123123:investigation:ABCDEF543210"
    }
    expected_comment_text = "<b>Created by Rapid7 InsightIDR:</b><br><br><b>Created at:</b> <br><b>By:</b> None: None<br><br><b>Comment:</b><br>Here is my comment."
    comment_text = app_common.format_rapid7_insight_idr_comment(comment)

    assert comment_text == expected_comment_text

    comment = {
        "attachments": [],
        "body": "Here is my comment.",
        "created_time": "2018-06-06T16:56:42Z",
        "creator":{
            "name": "John Doe",
            "type": "USER"
        },
        "target": "rrn:investigation:us:01234567-89ab-cdef-0000-123123123123:investigation:ABCDEF543210"
    }
    expected_comment_text = "<b>Created by Rapid7 InsightIDR:</b><br><br><b>Created at:</b> 2018-06-06T16:56:42Z<br><b>By:</b> USER: John Doe<br><br><b>Comment:</b><br>Here is my comment."
    comment_text = app_common.format_rapid7_insight_idr_comment(comment)

    assert comment_text == expected_comment_text

    comment = {
        "attachments": [{
            "created_time": "2018-06-06T16:56:42Z",
            "creator": {},
            "file_name": "screenshot.png",
            "mime_type": "image/png",
            "rrn": "rrn:collaboration::orgId_123:attachment:d7812988-f171-4164-9309-65c32d5da28f",
            "scan_status": "CLEAN",
            "size": 12345
        }],
        "body": "Here is my comment.",
        "created_time": "2018-06-06T16:56:42Z",
        "creator":{
            "name": "John Doe",
            "type": "USER"
        },
        "target": "rrn:investigation:us:01234567-89ab-cdef-0000-123123123123:investigation:ABCDEF543210"
    }
    expected_comment_text = "<b>Created by Rapid7 InsightIDR:</b><br><br><b>Created at:</b> 2018-06-06T16:56:42Z<br><b>By:</b> USER: John Doe<br><br><b>Comment:</b><br>Here is my comment.<br><b>Attachments:</b><br>screenshot.png"
    comment_text = app_common.format_rapid7_insight_idr_comment(comment)

    assert comment_text == expected_comment_text
