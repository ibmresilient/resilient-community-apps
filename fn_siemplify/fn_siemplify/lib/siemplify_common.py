# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.

import logging
import json
from urllib.parse import urljoin
from .jinja_common import JinjaEnvironment

LOG = logging.getLogger(__name__)

DEFAULT_CREATE_CASE = "templates/siemplify_create_case.jinja"

BASE_URL = "/api/external/v1/"
CREATE_CASE_URL = urljoin(BASE_URL, "cases/CreateManualCase")
GET_CASE_URL = urljoin(BASE_URL, "cases/GetCaseFullDetails/{}")

class SiemplifyCommon():
    def __init__(self, rc, options):
        self.options = options
        self.base_url = options.base_url
        self.api_key = options.api_key
        LOG.info(self.api_key)
        self.headers = _make_headers(self.api_key)
        self.jina_env = JinjaEnvironment()
        self.rc = rc
        self.verify = False if options.cafile.lower() == "false" else options.cafile

    def sync_case(self, incident_info):
        # perform an update to an existing incident
        if incident_info.get('siemplify_case_id'):
            return self.update_case(incident_info)

        return self.create_case(incident_info)

    def create_case(self, incident_info):
        incident_payload = self.jina_env.make_payload_from_template(
            self.options.siemplify_create_case_template,
            DEFAULT_CREATE_CASE,
            incident_info)

        url = urljoin(self.base_url, CREATE_CASE_URL)
        return self._make_call("POST", url, incident_payload)

    def update_case(self, incident_info):
        # get the existing case to start reviewing changes
        self._diff_case_info(incident_info)

        #_diff_comments(incident_info)

        #_diff_attachments(incident_info)
        return None

    def _diff_case_info(self, incident_info):
        # get the existing case
        url = urljoin(self.base_url, GET_CASE_URL.format(incident_info["siemplify_case_id"]))
        case_info = self._make_call("GET", url)
        LOG.info(case_info)

    def _make_call(self, method, url, payload=None):
        if payload:
            return self.rc.execute(method, url, data=json.dumps(payload), headers=self.headers, verify=self.verify)
        else:
            return self.rc.execute(method, url, headers=self.headers, verify=self.verify)

def _make_headers(api_key):
    return {
        "Content-Type": "application/json",
        "AppKey": api_key
    }
