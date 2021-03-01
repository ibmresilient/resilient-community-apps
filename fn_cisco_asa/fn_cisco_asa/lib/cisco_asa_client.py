# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.

"""Cisco ASA REST API client"""

import os
import sys
import base64
import logging
from resilient_lib import RequestsCommon

LOG = logging.getLogger(__name__)


def get_headers(username, password):
    url_key = u'{0}:{1}'.format(username, password)

    # It must be Base64-encoded. Handled different on Python 2 vs 3.
    if sys.version_info[0] == 2:
        auth_token = base64.b64encode(bytes(url_key).encode("utf-8"))
    else:
        auth_token = base64.b64encode(bytes(url_key, 'ascii')).decode('ascii')

    # Create the headers
    headers = {'Authorization': u'Basic {0}'.format(auth_token),
               'Content-Type': 'application/json', 
               'User-Agent': 'REST API Agent'}
    return headers

class CiscoASAClient(object):
    def __init__(self, options, rc):
        # Read the configuration options
        self.rc = rc
        self.base_url = "https://{0}".format(options.get("host"))
        self.username = options.get("username")
        self.password = options.get("password")
        self.cafile = options.get("cafile")
        self.bundle = os.path.expanduser(self.cafile) if self.cafile else False

        self.is_ASAv = options.get("is_asav")
        self.headers = get_headers(self.username, self.password)
    
    def get_network_object_group(self, group):
        # Pass the parameters in the URL not in the payload for this endpoint only.
        url = u"{0}/api/objects/networkobjectgroups/{1}".format(self.base_url, group)

        response = self.rc.execute_call_v2("get", url, headers=self.headers, verify=self.bundle,
                                           proxies=self.rc.get_proxies())
        LOG.debug(u"Response: %s", response.text)
        response.raise_for_status()
        return response.json()

    def write_memory(self):
        url = u"{0}/api/commands/writemem".format(self.base_url)

        response = self.rc.execute_call_v2("post", url, headers=self.headers, verify=self.bundle,
                                           proxies=self.rc.get_proxies())
        LOG.debug(u"Response: %s", response.text)
        response.raise_for_status()
        return response.json()