#
import pytest
import logging
import os
import json
from fn_siemplify.lib.jinja_common import JinjaEnvironment

SIEMPLIFY_CREATE_CASE = "../fn_siemplify/lib/templates/siemplify_create_case.jinja"

INCIDENT1 = {
    "name": "test incident",
    "description": None,
    "severity": 4,
    "confirmed": True,
    "discovered_date":  1638989883000,
    "siemplify_assigned_user": "a@example.com",
    "siemplify_environment": None,
    "comments": [],
    "artifacts": [
    ]
}

LOG = logging.getLogger(__name__)

class TestSiemplify:
    def test_create_case(self):
        jinja_env = JinjaEnvironment()

        template_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), SIEMPLIFY_CREATE_CASE)
        result = jinja_env.make_payload_from_template(None, template_path, INCIDENT1)
        LOG.info(result)
