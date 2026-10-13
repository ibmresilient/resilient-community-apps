# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
"""Tests APIs using both mocked endpoints and livetests"""

import json
import os
from unittest import mock

import pytest
import requests_mock
from resilient_lib import (RequestsCommon)
from fn_trusteer_ppd.lib.trusteer_ppd_client import (TrusteerPPDClient, PACKAGE_NAME, 
                                                     ENDPOINT_URL, REST_API_BASE_URL, LINKBACK_URL)

BASE_MOCK_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
PATH_CERT_PEM = os.path.join(BASE_MOCK_PATH, "cert.pem")
PATH_KEY_PEM = os.path.join(BASE_MOCK_PATH, "key.pem")

APP_CONFIG = {
    "api_token": "abcd-efgh",
    "api_version": "v1",
    "customer_name": "trusteer_customer_name",
    "verify": "true",
    "client_auth_cert" : PATH_CERT_PEM,
    "client_auth_key" : PATH_KEY_PEM,
    "endpoint_url": ENDPOINT_URL.format(customer_name="trusteer_customer_name"),
    "rest_api_base_url": REST_API_BASE_URL.format(customer_name="trusteer_customer_name")
}


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
def trusteer_ppd_client():
    rc = RequestsCommon()
    yield TrusteerPPDClient(rc, PACKAGE_NAME, APP_CONFIG)

def test_make_linkback_url(trusteer_ppd_client: TrusteerPPDClient):
    pu_id = "aaaa-bbbb-cccc-dddd"
    device_id = "aaaa-bbbb-1111-2222"
    puid_url = trusteer_ppd_client.make_linkback_url(id=pu_id, id_type='puid')
    device_id_url = trusteer_ppd_client.make_linkback_url(id=device_id, id_type='device_id')

    assert puid_url == LINKBACK_URL.format(base_url=APP_CONFIG.get('endpoint_url'), id=pu_id, id_type='puid')
    assert device_id_url == LINKBACK_URL.format(base_url=APP_CONFIG.get('endpoint_url'), id=device_id, id_type='device_id')