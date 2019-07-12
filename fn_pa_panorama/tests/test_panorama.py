# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
import json
from requests.exceptions import HTTPError
from mock import patch
from resilient_circuits.util import get_function_definition
from fn_pa_panorama.util.panorama_util import PanoramaClient

PACKAGE_NAME = "fn_pa_panorama"


class TestPanoramaCreateAddress:
    """ Tests for the panorama_create_address function"""

    mocked_opts = {
        "fn_pa_panorama": {
            "location": "fake_location",
            "api_key": "fake_api_key",
            "panorama_host": "http://fake_host"
        }
    }

    def _generateResponse(self, content, status):
        class simResponse:
            def __init__(self, content, status):
                self.status_code = status
                self.content = content
                self.reason = "test"

            def json(self):
                return json.loads(self.content)

            def raise_for_status(self):
                """Same from Requests.Response
                Raises stored :class:`HTTPError`, if one occurred."""

                http_error_msg = ''
                if isinstance(self.reason, bytes):
                    # We attempt to decode utf-8 first because some servers
                    # choose to localize their reason strings. If the string
                    # isn't utf-8, we fall back to iso-8859-1 for all other
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

    @pytest.mark.parametrize(
        "func_name", [
            ('panorama_create_address'),
            ('panorama_edit_address_group'),
            ('panorama_edit_users_in_a_group'),
            ('panorama_get_address_groups'),
            ('panorama_get_addresses'),
            ('panorama_get_users_in_a_group'),
    ])
    def test_function_definition(self, func_name):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, func_name)
        assert func is not None

    @patch("requests.request")
    def test_get_addresses(self, mocked_requests_get):
        sim_content = {
            "@code": "19",
            "@status": "success",
            "result": {
                "@count": "4",
                "@total-count": "4",
                "entry": [
                    {
                        "@location": "vsys",
                        "@name": "Test",
                        "@vsys": "vsys1",
                        "ip-netmask": "1.1.1.1"
                    },
                    {
                        "@location": "vsys",
                        "@name": "9.9.9.9",
                        "@vsys": "vsys1",
                        "description": "9.9.9.9",
                        "ip-netmask": "9.9.9.9"
                    },
                    {
                        "@location": "vsys",
                        "@name": "google.com",
                        "@vsys": "vsys1",
                        "description": "google.com",
                        "fqdn": "google.com"
                    },
                    {
                        "@location": "vsys",
                        "@name": "8.8.8.8",
                        "@vsys": "vsys1",
                        "description": "8.8.8.8",
                        "ip-netmask": "8.8.8.8"
                    }
                ]
            }
        }
        mocked_requests_get.return_value = self._generateResponse(json.dumps(sim_content), 200)
        pc = PanoramaClient(self.mocked_opts, None, None)
        result = pc.get_addresses()
        assert result == sim_content

    @patch("requests.request")
    def test_get_addresses_groups(self, mocked_requests_get):
        sim_content = {
            "@code": "19",
            "@status": "success",
            "result": {
                "@count": "1",
                "@total-count": "1",
                "entry": [
                    {
                        "@location": "vsys",
                        "@name": "Blocked Group",
                        "@vsys": "vsys1",
                        "description": "None",
                        "static": {
                            "member": [
                                "Test",
                                "google.com",
                                "8.8.8.8"
                            ]
                        }
                    }
                ]
            }
        }
        mocked_requests_get.return_value = self._generateResponse(json.dumps(sim_content), 200)
        pc = PanoramaClient(self.mocked_opts, None, None)
        result = pc.get_address_groups("Blocked_Group")
        assert result == sim_content

    @patch("requests.request")
    def test_edit_address_group(self, mocked_requests_get):
        sim_content = {
            "@code": "20",
            "@status": "success",
            "msg": "command succeeded"
        }
        body = {
            "entry": {
                "@name": "Blocked Group",
                "description": "None",
                "static": {
                    "member": ["google.com", "8.8.8.8"]
                }
            }
        }
        mocked_requests_get.return_value = self._generateResponse(json.dumps(sim_content), 200)
        pc = PanoramaClient(self.mocked_opts, None, None)
        result = pc.edit_address_groups("Blocked_Group", json.dumps(body))
        assert result == sim_content

    @patch("requests.request")
    def test_create_address(self, mocked_requests_get):
        sim_content = {
            "@code": "20",
            "@status": "success",
            "msg": "command succeeded"
        }
        body = {
            "@code": "20",
            "@status": "success",
            "msg": "command succeeded"
        }
        mocked_requests_get.return_value = self._generateResponse(json.dumps(sim_content), 200)
        pc = PanoramaClient(self.mocked_opts, None, None)
        result = pc.add_address("2.2.2.2", json.dumps(body))
        assert result == sim_content

    @patch("requests.request")
    def test_get_users_in_a_group(self, mocked_requests_get):
        sim_content = '<response status="success" code="19"><result total-count="1" count="1"><entry name="Blocked_Users" admin="admin" dirtyId="14" time="2019/06/27 07:51:28"/></result></response>'
        body_xpath = "/config/shared/local-user-database/user-group/entry[@name=\\'Blocked_Users\\']"
        mocked_requests_get.return_value = self._generateResponse(sim_content, 200)
        pc = PanoramaClient(self.mocked_opts, None, None)
        result = pc.get_users_in_a_group( body_xpath)
        assert result == sim_content

    @patch("requests.request")
    def test_edit_users_in_a_group(self, mocked_requests_get):
        sim_content = '<response status="success" code="20"><msg>command succeeded</msg></response>'
        body_xpath = "/config/shared/local-user-database/user-group/entry[@name=\\'Blocked_Users\\']"
        xml = """<entry name="Blocked_Users">
                    <user>
                      <member>Blocked_User</member>
                    </user>
                </entry>"""
        mocked_requests_get.return_value = self._generateResponse(sim_content, 200)
        pc = PanoramaClient(self.mocked_opts, None, None)
        result = pc.edit_users_in_a_group(body_xpath, xml)
        assert result == sim_content
