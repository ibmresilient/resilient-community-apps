"""Tests for AbuseDBIP custom threat service"""
from __future__ import print_function
import requests
import json
import logging
import time
import rc_cts_abuseipdb.components.abuseipdb_threat_feed_searcher

SERVICE_URL = "http://localhost:9000/cts/abuseipdb_threat_feed"

config_data = """[abuseipdb_cts]
abuseipdb_url=https://www.abuseipdb.com/check
abuseipdb_key=$TEST_RESILIENT_ABUSE_IP_DB_KEY
ignore_white_listed=True
"""


class TestAbuseIPDBCustomThreatService(object):
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
        """Verify hit is returned """
        artifact = json.dumps({"type": "net.ip", "value": "91.200.12.212"})
        # put artifact hit data in cache so correct code is returned
        r = requests.post(SERVICE_URL, artifact)
        assert r.status_code == 303
        time.sleep(5)
        response = requests.post(SERVICE_URL, artifact)
        assert response.status_code == 200
        content = json.loads(response.text)

        # assert if hit where found
        assert len(content["hits"]) == 0

    def test_check_no_hit(self, circuits_app):
        """Verify no hit is returned"""
        artifact = json.dumps({"type": "net.ip", "value": "8.8.8.8"})
        r = requests.post(SERVICE_URL, artifact)
        assert r.status_code == 303
        time.sleep(2)
        response = requests.post(SERVICE_URL, artifact)
        assert response.status_code == 200
        content = json.loads(response.text)
        # assert no hit objects
        assert len(content["hits"]) == 0
