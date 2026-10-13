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
PATH_NEXT_PAGE_MOCK = os.path.join(BASE_MOCK_PATH, "GET_next_page.json")

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
        mock_api.register_uri("GET", "/services/data/v58.0/query/01gRO0000016PIAYA2-500", headers={"Authorization": "Bearer xyz"}, json=load_json(PATH_NEXT_PAGE_MOCK), status_code=200)
        rc = RequestsCommon()
        yield AppCommon(PACKAGE_NAME, APP_CONFIG), mock_api

def test_make_headers(fx_setup_mock_api):
    app_common = fx_setup_mock_api[0]
    mock_api = fx_setup_mock_api[1]
    headers = app_common._make_headers("mock_token")

    assert headers == { 'Content-Type': 'application/json',  'Authorization': "Bearer mock_token" }

def test_paginate_results(fx_setup_mock_api):
    app_common = fx_setup_mock_api[0]
    response_json = {"totalSize":2,
                     "done":True,
                     "records":[{"attributes":{"type":"Case",
                                               "url":"/services/data/v58.0/sobjects/Case/500Hr00001Wuk5zIAB"},
                                  "Id":"500Hr00001Wuk5zIAB",
                                  "CaseNumber":"00001196"}, 
                                {"attributes":{"type":"Case",
                                               "url":"/services/data/v58.0/sobjects/Case/500Hr00001WuTFoIAN"},
                                  "Id":"500Hr00001WuTFoIAN",
                                  "CaseNumber":"00001180"}
                                ]
                    }
    records_list = app_common.paginate_results(response_json)
    assert records_list == response_json.get("records")
    response_json_2 = {"totalSize":2,
                     "done":False,
                     "nextRecordsUrl": "/services/data/v58.0/query/01gRO0000016PIAYA2-500",
                     "records":[{"attributes":{"type":"Case",
                                               "url":"/services/data/v58.0/sobjects/Case/500Hr00001Wuk5zIAB"},
                                  "Id":"500Hr00001Wuk5zIAB",
                                  "CaseNumber":"00001196"}, 
                                {"attributes":{"type":"Case",
                                               "url":"/services/data/v58.0/sobjects/Case/500Hr00001WuTFoIAN"},
                                  "Id":"500Hr00001WuTFoIAN",
                                  "CaseNumber":"00001180"}
                                ]
                    }
    records_list = app_common.paginate_results(response_json_2)
    response_json_3 = load_json(PATH_NEXT_PAGE_MOCK)
    assert records_list == response_json.get("records") + response_json_3.get("records")