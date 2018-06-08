"""Tests for Have I Been Pwned custom threat service"""
from __future__ import print_function
import requests
import json
import logging
import time

SERVICE_URL = "http://localhost:9000/cts/have_i_been_pwned_threat_service"


class TestHaveIBeenPwnedCustomThreatService(object):
    """ System tests """

    LOG=logging.getLogger(__name__)

    def test_server_up(self, circuits_app):
        """Verify the web service is responding at the root"""
        response = requests.get(SERVICE_URL + "/123")
        assert response.status_code == 200

    def test_options(self, circuits_app):
        """Verify the web service is responding to the OPTIONS method"""
        response = requests.options(SERVICE_URL)
        assert response.status_code == 200

    def test_check_for_hit(self, circuits_app):
        """Verify hit is returned on unsafe email"""
        artifact = json.dumps({"type": "email.header", "value": "test@example.com"})
        # put artifact hit data in cache so correct code is returned
        r = requests.post(SERVICE_URL, artifact)
        assert r.status_code == 303
        time.sleep(2)
        response = requests.post(SERVICE_URL, artifact)
        assert response.status_code == 200
        content = json.loads(response.text)
        props = content["hits"][0]["props"]
        p = 0
        while True:
            if props[p]["type"] == "uri":
                props = props[p]
                break
            p = p+1
        artifact = json.loads(artifact)
        #assert shows the correct Have I Been Pwned URI
        assert props["value"] == "https://haveibeenpwned.com/api/v2/unifiedsearch/" + artifact["value"]

    def test_check_no_hit(self, circuits_app):
        """Verify no hit is returned on safe email"""
        artifact = json.dumps({"type": "email.header.to", "value": "safe@email2.com"})
        #put artifact hit data in cache so correct code is returned
        r = requests.post(SERVICE_URL, artifact)
        assert r.status_code == 303
        time.sleep(2)
        response = requests.post(SERVICE_URL, artifact)
        assert response.status_code == 200
        content = json.loads(response.text)
        #assert no hit objects
        assert len(content["hits"]) == 0

    def test_check_hit_no_pastes(self, circuits_app):
        """Verify hit is returned if no pastes are found on email"""
        artifact = json.dumps({"type": "email.header.to", "value": "a1@example.com"})
        # put artifact hit data in cache so correct code is returned
        r = requests.post(SERVICE_URL, artifact)
        assert r.status_code == 303
        time.sleep(2)
        response = requests.post(SERVICE_URL, artifact)
        assert response.status_code == 200
        content = json.loads(response.text)
        # assert hit is returned
        assert len(content["hits"]) == 1
        props = content["hits"][0]["props"]
        p = 0
        while True:
            if props[p]["name"] == "Pastes":
                props = props[p]
                break
            p = p + 1
        assert props["value"] == "0"
