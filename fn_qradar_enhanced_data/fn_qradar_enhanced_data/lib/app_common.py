# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
import logging
from urllib.parse import urljoin
from resilient_lib import str_to_bool, readable_datetime

LOG = logging.getLogger(__name__)

HEADER = { 'Content-Type': 'application/json' }

class AppCommon():
    def __init__(self, rc, options):
        self.api_key = options['api_key']
        self.api_secret = options['api_secret']
        self.reaqta_url = options['reaqta_url']
        self.api_version = options['api_version']
        self.rc = rc
        self.verify = str_to_bool(options.get("cafile", "false"))

    def get_filters(self):
        return self.filters

    def authenticate(self):
        params = {
            "secret": self.api_secret,
            "id": self.api_key
        }

        auth_url = self._get_uri('authenticate')

        response = self.rc.execute("POST", auth_url, json=params, headers=HEADER, verify=self.verify)
        return response.json()['token']

    def _get_uri(self, cmd):
        """build API url
        Args:
            cmd (str): portion of API: alerts, endpoints, policies
        Returns:
            str: complete URL
        """
        return urljoin(urljoin(self.reaqta_url, self.api_version), cmd)

    def _make_header(self, token):
        """Build API header using authorization token
        Args:
            token (str): authorization token
        Returns:
            dict: complete header
        """
        header = HEADER.copy()
        header['Authorization'] = "Bearer {}".format(token)

        return header

    def make_linkback_url(self, template_uri, entity_id):
        """Create a url to link back to the endpoint alert, case, etc.
        Args:
            template (str): portion of url to join with base url
            entity_id (str/int): id representing the alert, case, etc.
        Returns:
            str: completed url for linkback
        """
        return urljoin(self.reaqta_url, template_uri.format(entity_id))