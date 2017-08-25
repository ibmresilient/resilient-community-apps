"""System Integration Tests for Resilient Circuits Webserver"""
from __future__ import print_function
import pytest
import requests
from circuits.web import BaseController
from rc_webserver.web import exposeWeb


HTML = """
<html>
 <head>
  <title>A Test</title>
 </head>
 <body>Test</body>
</html>"""


class WebTest(BaseController):
    """ Test Web Component """

    def __init__(self, opts):
        super(WebTest, self).__init__(opts)
        self.channel = "/test"

    @exposeWeb("index")
    def _index(self, status=""):
        return HTML


@pytest.mark.usefixtures("configure_resilient")
class TestWebserverTests:
    """ System tests for the Resilient Circuits webservice components """

    def test_server_up(self, circuits_app, new_incident):
        """ Verify Webserver is Up """
        WebTest({}).register(circuits_app.app.component_loader)
        response = requests.get("http://localhost:9000/test")
        assert response.status_code == 200
        assert response.text == HTML
