# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

from __future__ import print_function
import requests_mock
from pytest_resilient_circuits import BasicResilientMock, resilient_endpoint


class IncidentMock(BasicResilientMock):
    incident_id = 123
    incident_1 = {
        "id": incident_id,
        "resolution_summary": "<div class=\"rte\"><div>unresolved</div></div>",
        "vers": 5
    }
    incident_2 = {
        "id": incident_id,
        "resolution_summary": "<div class=\"rte\"><div>resolved</div></div>",
        "resolution_id": 9,
        "plan_status": "C",
        "vers": 5
    }
    mock_incident_fields = {
        "id": incident_id,
        "type_id": 0,
        "type_name": "incident",
        "fields": {
            "country": {"name": "country", "input_type": "select"},
            "resolution_id": {"name": "resolution_id", "input_type": "select", "required": "close"},
            "resolution_summary": {"name": "resolution_summary", "input_type": "textarea", "required": "close"},
            "workspace": {"name": "resolution_id", "input_type": "select", "required": "always"}
        },
        "resolution_summary": "<div class=\"rte\"><div>unresolved</div></div>",
        "vers": 5
    }

    @resilient_endpoint("GET", "/types/incident")
    def incident_types_get(self, request):
        """ Callback for GET to /orgs/<org_id>/types/incident """
        return requests_mock.create_response(request, status_code=200, json=self.mock_incident_fields)

    @resilient_endpoint("GET", "/incidents/[0-9]+$")
    def incident_get(self, request):
        """ Callback for GET to /orgs/<org_id>/incidents/<inc_id> """
        return requests_mock.create_response(request, status_code=200, json=self.incident_1)

    @resilient_endpoint("PATCH", "/incidents/[0-9]+")
    def incident_patch(self, request):
        """ Callback for PATCH to /orgs/<org_id>/incidents/<inc_id> """
        return requests_mock.create_response(request, status_code=200, json=self.incident_2)
