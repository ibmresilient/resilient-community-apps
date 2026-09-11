"""Tests for Have I Been Pwned custom threat service"""
from __future__ import print_function
import requests
import json
import logging
import time

SERVICE_URL = "http://localhost:9000/cts/gsb"


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
        artifact = {"type": "net.uri", "value": "karow-burau.com"}
        # put artifact hit data in cache so correct code is returned
        response = requests.post(SERVICE_URL, json.dumps(artifact))
        if response.status_code == 303:
            time.sleep(2)
            response = requests.post(SERVICE_URL, json.dumps(artifact))
        assert response.status_code == 200
        content = json.loads(response.text)

        props = content["hits"][0]["props"]
        p = 0
        while True:
            if props[p]["type"] == "uri":
                hit = props[p]
                break
            p = p+1

        #assert shows the correct report link
        assert hit["value"] == "https://www.google.com/transparencyreport/safebrowsing/diagnostic/#url=" + artifact["value"]

    def test_check_no_hit(self, circuits_app):
        """Verify no hit is returned on safe email"""
        artifact = {"type": "net.uri", "value": "safe.com"}
        #put artifact hit data in cache so correct code is returned
        response = requests.post(SERVICE_URL, json.dumps(artifact))
        if response.status_code == 303:
            time.sleep(2)
            response = requests.post(SERVICE_URL, json.dumps(artifact))
        assert response.status_code == 200
        content = json.loads(response.text)
        #assert no hit objects
        assert len(content["hits"]) == 0

