# -*- coding: utf-8 -*-
"""Tests APIs using both mocked endpoints and livetests"""

import json
import os
from datetime import datetime
from unittest import mock

import pytest
import requests_mock
from fn_darktrace.lib.app_common import (AI_ANALYST_EVENT_COMMENTS_URI,
                                         AI_ANALYST_EVENTS_URI,
                                         AI_ANALYST_INCIDENT_GROUPS_URI,
                                         DEVICES_URI, DT_TIME_FORMATTER,
                                         MODEL_BREACHES_URI, SYSTEM_STATUS_URI,
                                         AppCommon)
from resilient_lib import RequestsCommon

APP_CONFIG = {
    "api_key": "abcd-efgh",
    "api_secret": "1234-abcd-56789-efgh",
    "instance_url": "https://fake.cloud.darktrace.com/"
}

BASE_MOCK_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "mock_data")
PATH_STATUS_MOCK = os.path.join(BASE_MOCK_PATH, "GET_status.json")
PATH_AIANALYST_GROUPS_MOCK = os.path.join(BASE_MOCK_PATH, "GET_aianalyst_groups.json")
PATH_AIANALYST_INCIDENT_COMMENTS_MOCK = os.path.join(BASE_MOCK_PATH, "GET_aianalyst_incident_comments.json")
PATH_AIANALYST_INCIDENTEVENTS_MOCK = os.path.join(BASE_MOCK_PATH, "GET_aianalyst_incidentevents.json")
PATH_DEVICES_MOCK = os.path.join(BASE_MOCK_PATH, "GET_devices.json")
PATH_MODELBREACHES_MOCK = os.path.join(BASE_MOCK_PATH, "GET_modelbreaches.json")

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
        mock_api.register_uri("GET", SYSTEM_STATUS_URI, json=load_json(PATH_STATUS_MOCK), status_code=200)
        mock_api.register_uri("GET", AI_ANALYST_INCIDENT_GROUPS_URI, json=load_json(PATH_AIANALYST_GROUPS_MOCK), status_code=200)
        mock_api.register_uri("GET", AI_ANALYST_EVENT_COMMENTS_URI, json=load_json(PATH_AIANALYST_INCIDENT_COMMENTS_MOCK), status_code=200)
        mock_api.register_uri("GET", AI_ANALYST_EVENTS_URI, json=load_json(PATH_AIANALYST_INCIDENTEVENTS_MOCK), status_code=200)
        mock_api.register_uri("GET", DEVICES_URI, json=load_json(PATH_DEVICES_MOCK), status_code=200)
        mock_api.register_uri("GET", MODEL_BREACHES_URI, json=load_json(PATH_MODELBREACHES_MOCK), status_code=200)

        yield mock_api

@pytest.fixture(scope="module")
def app_common():
    rc = RequestsCommon()
    yield AppCommon(rc, APP_CONFIG)

#########################
## TEST QUERY SINCE TS ##
#########################
def test_query_entities_since_ts(mock_api: requests_mock.Mocker, app_common: AppCommon):
    resp = app_common.query_entities_since_ts(datetime.now())

    assert resp
    assert len(resp) == 1
    assert "incidentEvents" in resp[0]
    assert "devices" in resp[0]
    assert mock_api.called

def test_query_entities_since_ts_no_candidate_events(mock_api: requests_mock.Mocker, app_common: AppCommon):
    # overwrite the default mocked behavior
    mock_api.register_uri("GET", AI_ANALYST_EVENTS_URI, json=[], status_code=200)

    resp = app_common.query_entities_since_ts(datetime.now())
    assert not resp
    assert mock_api.called_once

###########################
## BASIC ENDPOINT CHECKS ##
###########################
# NOTE: all of these tests below rely on the mock data found in the 
# mock_data folder of the tests directory

def test_get_system_status(mock_api: requests_mock.Mocker, app_common: AppCommon):
    resp = app_common.get_system_status()

    assert resp
    assert mock_api.called_once
    assert resp["version"] == "0.0.0"

def test_get_model_breaches(mock_api: requests_mock.Mocker, app_common: AppCommon):
    resp = app_common.get_model_breaches()

    assert resp
    assert mock_api.called_once
    assert resp["pbid"] == 123

def test_get_incident_groups(mock_api: requests_mock.Mocker, app_common: AppCommon):
    resp = app_common.get_incident_groups()

    assert resp
    assert mock_api.called_once
    assert resp[0]["id"] == "g04a3f36e-4u8w-v9dh-x6lb-894778cf9633"

def test_get_incident_events(mock_api: requests_mock.Mocker, app_common: AppCommon):
    resp = app_common.get_incident_events()

    assert resp
    assert mock_api.called_once
    assert resp[0]["id"] == "04a3f36e-4u8w-v9dh-x6lb-894778cf9633"

def test_get_incident_event_comments(mock_api: requests_mock.Mocker, app_common: AppCommon):
    resp = app_common.get_incident_event_comments()

    assert resp
    assert mock_api.called_once
    assert len(resp["comments"]) == 1
    assert resp["comments"][0]["incident_id"] == "04a3f36e-4u8w-v9dh-x6lb-894778cf9633"

def test_get_devices(mock_api: requests_mock.Mocker, app_common: AppCommon):
    resp = app_common.get_devices()

    assert resp
    assert mock_api.called_once
    assert resp["id"] == 212

####################################
## STATIC AND HELPER METHOD TESTS ##
####################################
def test_generate_query_from_params():
    query1 = AppCommon._generate_query_from_params("/system_status", {"fast": "true"})
    query2 = AppCommon._generate_query_from_params("/aianalyst/groups", {"includegroupurl": "true", "groupid": "1,2,3,4"})

    assert query1 == "/system_status?fast=true"
    assert query2 == "/aianalyst/groups?includegroupurl=true&groupid=1,2,3,4"

def test_get_headers(app_common: AppCommon):
    time = datetime.utcnow().strftime(DT_TIME_FORMATTER)
    headers = app_common._get_headers(time, "signature")

    assert headers == {"DTAPI-Token": "abcd-efgh", "DTAPI-Date": time, "DTAPI-Signature": "signature"}

def test_generate_signature(app_common: AppCommon):
    time = datetime.utcfromtimestamp(100000).strftime(DT_TIME_FORMATTER)
    request = "/aianalyst/groups?includegroupurl=true&groupid=1,2,3,4"
    signature = app_common._generate_signature(request, time)

    assert signature == "3e30ac6b365018e15954cc2d4f262efa248c1bef"

def test_execute_dt_request(mock_api: requests_mock.Mocker, app_common: AppCommon):
    method = "GET"
    time = datetime.utcfromtimestamp(100000).strftime(DT_TIME_FORMATTER)
    request = "/aianalyst/groups"
    params = {"includegroupurl": "true", "groupid": "1,2,3,4"}

    resp = app_common._execute_dt_request(method, request, params=params, time=time)

    assert resp
    assert isinstance(resp, list)
    assert isinstance(resp[0], dict)
    assert mock_api.called_once
