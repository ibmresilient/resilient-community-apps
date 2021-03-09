# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

import sys
import json
import pytest
from requests.exceptions import HTTPError
from fn_cisco_asa.lib.cisco_asa_client import CiscoASAClient
from resilient_circuits.util import get_function_definition
from resilient_lib import IntegrationError, RequestsCommon

if sys.version_info.major == 2:
    from mock import patch
else:
    from unittest.mock import patch

PACKAGE_NAME = "fn_cisco_asa"

MOCKED_GLOBAL_OPTS = {
    "firewalls": "firewall_1,firewall_2",
    "network_object_lists": "BLACKLIST_IN, BLACKLIST_OUT"
}

MOCKED_FIREWALL_OPTS = {
    "host": "1.1.1.1",
    "username": "username",
    "password": "password"
}


def generate_response(content, status):
    class simResponse:
        def __init__(self, content, status):
            self.status_code = status
            self.content = content
            self.reason = "test"
            self.text = json.dumps(content)
            self.url = "test"

        def json(self):
            return json.loads(self.content)

        def raise_for_status(self):
            """Same from Requests.Response
            Raises stored :class:`HTTPError`, if one occurred."""

            http_error_msg = ''
            if isinstance(self.reason, bytes):
                # We attempt to decode utf-8 first because some servers
                # choose to localize their reason strings. If the string                    
                # # isn't utf-8, we fall back to iso-8859-1 for all other
                # encodings. (See PR #3538)
                try:
                    reason = self.reason.decode('utf-8')
                except UnicodeDecodeError:
                    reason = self.reason.decode('iso-8859-1')
            else:
                reason = self.reason

            if 400 <= self.status_code < 500:
                http_error_msg = u'%s Client Error: %s for url: %s' % (self.status_code, reason, self.url)

            elif 500 <= self.status_code < 600:
                http_error_msg = u'%s Server Error: %s for url: %s' % (self.status_code, reason, self.url)

            if http_error_msg:
                raise HTTPError(http_error_msg, response=self)

    return simResponse(content, status)


class TestCiscoASAClient(object):
    """ Tests for the Cisco ASA Client functions"""

    @pytest.mark.parametrize(
        "func_name", [
            ('cisco_asa_get_network_objects'),
            ('cisco_asa_add_network_object_to_network_object_group'),
            ('cisco_asa_add_artifact_to_network_object_group'),
            ('cisco_asa_remove_network_object_from_network_object_group'),
    ])
    def test_function_definition(self, func_name):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, func_name)
        assert func is not None

    @patch('fn_cisco_asa.lib.cisco_asa_client.rc.execute_call_v2')
    def test_get_network_object_group(self, get_mock):
        """ Test get_network_object_group"""
        print("Test get_network_object_group\n")
        sim_content = {"kind":"object#NetworkObjGroup",
            "selfLink":"https://192.168.1.162/api/objects/networkobjectgroups/BLACKLIST_IN",
            "name":"BLACKLIST_IN",
            "members":[
                {
                    "kind":"IPv4Address",
                    "value":"192.168.10.1"
                },
                {
                    "kind":"IPv4Address",
                    "value":"192.168.10.2"
                },
                {
                    "kind":"IPv4Address",
                    "value":"192.168.10.3"
                }
            ],
            "description":"",
        "objectId":"BLACKLIST_IN"
        }


        rc = RequestsCommon(MOCKED_FIREWALL_OPTS, MOCKED_FIREWALL_OPTS)
        asa_client = CiscoASAClient("firewall_1", MOCKED_GLOBAL_OPTS, MOCKED_FIREWALL_OPTS, rc)
 
        get_mock.return_value = generate_response(json.dumps(sim_content), 200)
        response = asa_client.get_network_object_group("BLACKLIST_IN")
        assert response == sim_content