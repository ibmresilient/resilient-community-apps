# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

from __future__ import print_function
import requests_mock
from pytest_resilient_circuits import BasicResilientMock, resilient_endpoint
import logging
LOG = logging.getLogger(__name__)


class IncidentMock(BasicResilientMock):
    incident_id = 123
    incident_1 = {
        "id": incident_id,
        "name": "some title",
        "description": "some description",
        "vers": 5,
        "discovered_date": 1664571300000,
        "create_date": 1664571301083,
        "owner_id": 68,
        "severity_code": None
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
        "vers": 5
    }

    mock_incident_attachments = {
        "attachments": [],
        "max_results_exceeded": False
    }

    @resilient_endpoint("GET", "/types/incident$")
    def incident_types_get(self, request):
        """ Callback for GET to /orgs/<org_id>/types/incident """
        LOG.info("incident_types_get")
        return requests_mock.create_response(request, status_code=200, json=IncidentMock.mock_incident_fields)

    @resilient_endpoint("GET", "/incidents/[0-9]+\?handle_format=names$")
    def incident_get(self, request):
        """ Callback for GET to /orgs/<org_id>/incidents/<inc_id> """
        LOG.info("incident_get")
        return requests_mock.create_response(request, status_code=200, json=IncidentMock.incident_1)

    @resilient_endpoint("POST", "/incidents/[0-9]+/attachments/query*")
    def incident_attachment_post(self, request):
        LOG.info("incident_attachment_post")
        return requests_mock.create_response(request, status_code=200, json=IncidentMock.mock_incident_attachments)
