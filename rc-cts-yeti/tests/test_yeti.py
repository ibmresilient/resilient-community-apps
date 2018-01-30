"""Tests for custom threat service Yeti"""
from __future__ import print_function
import pytest
import requests
import json
import logging


SERVICE_URL = "http://localhost:9000/cts/yeti"

config_data = """
[yeti]
urlbase=http://resilient:5000/api
template_dir=../rc_cts_yeti/data/jinja
"""

print(config_data)

class TestCustomThreatService(object):
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

    def test_post(self, circuits_app):
        """Verify the web service is responding to the OPTIONS method"""
        artifact = {"type": "net.uri", "value": "http://example.org"}
        response = requests.post(SERVICE_URL, json.dumps(artifact))
        assert response.status_code == 303
