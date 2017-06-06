"""System Integration Tests for Resilient Circuits Webserver"""
from __future__ import print_function
import pytest
import requests


@pytest.mark.usefixtures("configure_resilient")
class TestWebserverTests:
    """ System tests for the Resilient Circuits webservice components """

    def test_server_up(self, circuits_app, new_incident):
        """ Verify Webserver is Up """
        response = requests.get("http://localhost:9000")
        assert response.status_code == 200
        assert response.text == "<HTML><BODY>Not Found</BODY></HTML>"
