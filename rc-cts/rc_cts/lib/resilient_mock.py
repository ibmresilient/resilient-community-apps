"""
A minimal mock for Resilient REST API

To run with this mock class, in [resilient] section of app.config, set:
    resilient_mock=rc_cts.lib.resilient_mock.MyResilientMock

"""

import logging
import requests
import requests_mock
from resilient.resilient_rest_mock import ResilientMock, resilient_endpoint


LOG = logging.getLogger(__name__)


class MyResilientMock(ResilientMock):

    def __init__(self, *args, **kwargs):
        super(MyResilientMock,self).__init__(*args, **kwargs)
        self.incident = {
            "create_date": 1485448269000,
            "name": "test",
            "id": 2314
        }

    @resilient_endpoint("POST", "/rest/session")
    def session_post(self, request):
        """ Callback for POST to /rest/session """
        LOG.debug("session_post")
        session_data = {
            "csrf_token": "79945884c2e6f2339cbffbbaba01f17b",
            "user_lname": "Doe",
            "user_id": 1,
            "orgs": [
                {
                    "enabled": True,
                    "id": 201,
                    "name": self.org_name
                }
            ],
            "session_ip": "192.168.56.1",
            "user_fname": "John",
            "user_email": self.email
        }
        cookies = {'JSESSIONID': 'FakeSessionId'}
        return requests_mock.create_response(request,
                                             status_code=200,
                                             cookies=requests.cookies.cookiejar_from_dict(cookies),
                                             json=session_data)

    @resilient_endpoint("GET", "/incidents/[0-9]+$")
    def incident_get(self, request):
        """ Callback for GET to /orgs/<org_id>/incidents/<inc_id> """
        LOG.debug("incident_get")
        return requests_mock.create_response(request,
                                             status_code=200,
                                             json=self.incident)

    @resilient_endpoint("PUT", "/incidents/[0-9]+")
    def incident_put(self, request):
        """ Callback for PUT to /orgs/<org_id>/incidents/<inc_id> """
        LOG.debug("incident_put")
        self.incident = request.json()
        return requests_mock.create_response(request,
                                             status_code=200,
                                             json=self.incident)

    @resilient_endpoint("POST", "/incidents/")
    def incident_post(self, request):
        """ Callback for POST to /orgs/<org_id>/incidents """
        LOG.debug("incident_post")
        self.incident = request.json()
        return requests_mock.create_response(request,
                                             status_code=200,
                                             json=self.incident)

    @resilient_endpoint("GET", "/orgs/[0-9]+$")
    def org_get(self, request):
        """ Callback for GET to /orgs/<org_id> """
        LOG.debug("org_get")
        return requests_mock.create_response(request,
                                             status_code=200,
                                             json={"actions_framework_enabled": True})

    @resilient_endpoint("GET", "/types/incident/fields")
    def incident_fields_get(self, request):
        """ Callback for GET to /orgs/<org_id>/types/incident/fields """
        LOG.debug("incident_fields_get")
        return requests_mock.create_response(request,
                                             status_code=200,
                                             json={})

    @resilient_endpoint("GET", "/types/actioninvocation/fields")
    def action_fields_get(self, request):
        """ Callback for GET to /orgs/<org_id>/types/actioninvocation/fields """
        LOG.debug("action_fields_get")
        return requests_mock.create_response(request,
                                             status_code=200,
                                             json={})

    @resilient_endpoint("GET", "/actions")
    def actions_get(self, request):
        """ Callback for GET to /orgs/<org_id>/actions """
        LOG.debug("actions_get")
        return requests_mock.create_response(request,
                                             status_code=200,
                                             json={"entities": []})
