# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
# Generated with resilient-sdk v50.0.108
"""Tests using pytest_resilient_circuits"""
import unittest, time
import pytest

from fn_mandiant.lib.mandiant_client import *
from unittest.mock import MagicMock

PACKAGE_NAME = "fn_mandiant"
FUNCTION_NAME = "mandiant_threat_intelligence"

def mock_authentication_request(method, url, headers, data):

    class response:
        request_count = 0

        def __init__(self, value):
            self.value = value
        
        def json(self):
            return self.value

    assert method == "post"
    assert url == TOKEN_URL
    assert headers
    assert data
    assert "Authorization" in headers
    assert headers["Authorization"] == "Basic a2V5MTIzOnNlY3JldDEyMw=="
    assert "grant_type" in data
    assert data["grant_type"] == "client_credentials"
    return response({
        "access_token" : "accesstoken123",
        "token_type"   : "bearer",
        "expires_in"   : 100000})


def mock_search_artifact(method, url, headers):
    exp_url = 'https://api.intelligence.mandiant.com/v4/indicator/{}/data?explainer=true'
    assert method == "get"
    assert any([exp_url.format(artifact) == url  for artifact in ["ipv4", "url", "fqdn", "md5"]])
    assert headers
    assert "Authorization" in headers
    assert "bearer" in headers["Authorization"]
    ret = MagicMock()
    ret.json.return_value = {"success" : True}
    return ret


class TestMandiantClient(unittest.TestCase):

    def test_mandiant_client_constructor(self):
        rc = MagicMock()
        options = {
            AUTH_KEY : "key123",
            AUTH_SECRET : "secret123"}

        mc = MandiantClient(rc, options)
        self.assertDictEqual(mc._client_common, {
            'api_key': 'key123',
            'api_secret': 'secret123',
            'authenticated': False})


    def test_authenticate(self):
        rc = MagicMock()
        rc.execute = mock_authentication_request
        options = {
            AUTH_KEY : "key123",
            AUTH_SECRET : "secret123"}

        mc = MandiantClient(rc, options)
        mc.authenticate()
        self.assertDictEqual(mc._client_common["headers"], {
            'Accept'  : "application/json",
            'X-App-Name': 'ibm-app',
            'Authorization' : "bearer accesstoken123"})
        assert mc._client_common[AUTHENTICATED]
        assert mc._client_common["expires_in"] > int(time.time())


    def test_search_artifact(self):
        rc = MagicMock()
        rc.execute = mock_authentication_request
        options = {
            AUTH_KEY : "key123",
            AUTH_SECRET : "secret123"}

        mc = MandiantClient(rc, options)
        mc.authenticate()

        rc.execute = mock_search_artifact
        assert mc.search_artifact("ip address", "data")["success"]
        assert mc.search_artifact("url", "data")["success"]
        assert mc.search_artifact("dns name", "data")["success"]
        assert mc.search_artifact("malware md5 hash", "data")["success"]
        with pytest.raises(ValueError):
            mc.search_artifact("email", "data")
