"""Tests for custom threat service example"""
from __future__ import print_function
import pytest
import requests
import json
import logging


SERVICE_URL = "http://localhost:9000/cts/example"


class TestCustomThreatService(object):
    """ System tests """

    LOG=logging.getLogger(__name__)

    def test_server_up(self, circuits_app, new_incident):
        """Verify the web service is responding at the root"""
        #WebTest({}).register(circuits_app.app.component_loader)
        response = requests.get(SERVICE_URL + "/123")
        assert response.status_code == 200

    def test_options(self, circuits_app, new_incident):
        """Verify the web service is responding to the OPTIONS method"""
        #WebTest({}).register(circuits_app.app.component_loader)
        response = requests.options(SERVICE_URL)
        assert response.status_code == 200

    def test_post(self, circuits_app, new_incident):
        """Verify the web service is responding to the OPTIONS method"""
        #WebTest({}).register(circuits_app.app.component_loader)
        artifact = {"type": "net.uri", "value": "http://foo"}
        response = requests.post(SERVICE_URL, json.dumps(artifact))
        # assert response.status_code == 303
