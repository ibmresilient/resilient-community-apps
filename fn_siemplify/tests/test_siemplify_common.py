#
import pytest
import logging
import os
import json
from fn_siemplify.lib.jinja_common import JinjaEnvironment

SIEMPLIFY_CREATE_CASE = "../fn_siemplify/lib/templates/siemplify_create_case.jinja"

INCIDENT1 = {
    "id": 2009,
    "name": "test incident",
    "description": "my description",
    "severity": 4,
    "confirmed": True,
    "discovered_date":  1638989883000,
    "siemplify_assigned_user": "a@example.com",
    "siemplify_environment": "Default Environment",
    "siemplify_tags": "tag1, tag2",
    "comments": [],
    "artifacts": [
    ]
}

RESULT1 = {
  "title": "IBM SOAR - test incident",
  "assignedUser": "a@example.com",
  "reason": "IBM SOAR Incident 2009",
  "priority": 25,
  "environment": "Default Environment",
  "isImportant": True,
  "alertName": "IBM SOAR Alert 2009",
  "occurenceTime": "2021-12-08T18:58:03Z",
  "slaExpirationDateTime": None,
  "tags": [
    "tag1",
    "tag2"
  ]
}

LOG = logging.getLogger(__name__)

class TestSiemplify:
    def test_create_case(self):
        jinja_env = JinjaEnvironment()

        template_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), SIEMPLIFY_CREATE_CASE)
        result = jinja_env.make_payload_from_template(None, template_path, INCIDENT1)
        assert(RESULT1 == result)
