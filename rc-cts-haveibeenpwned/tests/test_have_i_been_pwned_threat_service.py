"""Tests for Have I Been Pwned custom threat service"""
from __future__ import print_function
import unittest
import requests
import json
import logging
import time

SERVICE_URL = "http://localhost:9000/cts/have_i_been_pwned_threat_service"


class TestHaveIBeenPwnedCustomThreatService(unittest.TestCase):
    """ System tests """

    LOG=logging.getLogger(__name__)

    def test_server_up(self):
        """Verify the web service is responding at the root"""
        response = requests.get(SERVICE_URL + "/123")
        self.assertEqual(200, response.status_code)

    def test_options(self):
        """Verify the web service is responding to the OPTIONS method"""
        response = requests.options(SERVICE_URL)
        self.assertEqual(200, response.status_code)

    def test_post(self):
        """Verify the web service is responding to the OPTIONS method"""
        artifact = {"type": "email.header", "value": "test@test.com"}
        response = requests.post(SERVICE_URL, json.dumps(artifact))
        self.assertEqual(303, response.status_code)

    def test_check_for_hit(self):
        """Verify hit is returned on unsafe email"""
        artifact = json.dumps({"type": "email.header", "value": "test@example.com"})
        # put artifact hit data in cache so correct code is returned
        requests.post(SERVICE_URL, artifact)
        time.sleep(1)
        response = requests.post(SERVICE_URL, artifact)
        self.assertEqual(response.status_code, 200)
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
        self.assertEqual("https://haveibeenpwned.com/api/v2/unifiedsearch/" + artifact["value"], props["value"])

    def test_check_no_hit(self):
        """Verify no hit is returned on safe email"""
        artifact = json.dumps({"type": "email.header.to", "value": "safe@email2.com"})
        #put artifact hit data in cache so correct code is returned
        requests.post(SERVICE_URL, artifact)
        time.sleep(1)
        response = requests.post(SERVICE_URL, artifact)
        self.assertEqual(response.status_code, 200)
        content = json.loads(response.text)
        #assert no hit objects
        self.assertEqual(0, len(content["hits"]))
