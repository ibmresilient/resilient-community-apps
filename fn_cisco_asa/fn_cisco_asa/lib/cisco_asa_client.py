# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.

"""Cisco ASA REST API client"""

import os
import sys
import base64
import logging
from resilient_lib import RequestsCommon, validate_fields, IntegrationError

LOG = logging.getLogger(__name__)


def get_headers(username, password):
    url_key = u'{0}:{1}'.format(username, password)

    string_encoded_url_key = base64.b64encode(str.encode(str(url_key)))
    auth_token = string_encoded_url_key.decode("utf-8")

    # Create the headers
    headers = {'Authorization': u'Basic {0}'.format(auth_token),
               'Content-Type': 'application/json', 
               'User-Agent': 'REST API Agent'}
    return headers

class CiscoASAClient(object):
    def __init__(self, global_options, options, rc):
        # Read the configuration options
        required_fields = ["host"]
        validate_fields(required_fields, options)

        self.rc = rc
        self.host = options.get("host")
        self.base_url = "https://{0}".format(self.host)
        self.username = options.get("username", global_options.get("username"))
        self.password = options.get("password", global_options.get("password"))
        if self.username is None or self.password is None:
            raise IntegrationError("Cisco ASA username and password must be defined.")
        self.cafile = options.get("cafile")
        self.bundle = os.path.expanduser(self.cafile) if self.cafile else False

        self.headers = get_headers(self.username, self.password)
    
    def get_network_object_group(self, group):
        # Pass the parameters in the URL not in the payload for this endpoint only.
        url = u"{0}/api/objects/networkobjectgroups/{1}".format(self.base_url, group)

        response = self.rc.execute_call_v2("get", url, headers=self.headers, verify=self.bundle,
                                           proxies=self.rc.get_proxies())
        return response.json()

    def write_memory(self):
        url = u"{0}/api/commands/writemem".format(self.base_url)

        response = self.rc.execute_call_v2("post", url, headers=self.headers, verify=self.bundle,
                                           proxies=self.rc.get_proxies())
        return response