# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2019. All Rights Reserved.

import sys
import pytest
from fn_maas360.lib.maas360_common import MaaS360Utils
from resilient_lib.components.integration_errors import IntegrationError

if sys.version_info.major == 2:
    from mock import patch, Mock
else:
    from unittest.mock import patch, Mock


class TestMaaS360(object):
    """ Tests for the fn_maas360 functions"""

    @staticmethod
    def _create_maas360_utils():
        """
        Create MaaS360Utils instance
        :return: MaaS360Utils
        """

        return MaaS360Utils("maas360_url", "billing_id", "username", "password", "app_id", "app_version",
                            "platform_id", "app_access_key", "auth_url")

    @patch('fn_maas360.lib.maas360_common.RequestsCommon.execute_call')
    def test_generate_auth_token(self, mocked_api_call):
        """ Test generate_auth_token"""
        print("Test generate_auth_token\n")

        mocked_api_call.return_value = {
            "authResponse": {
                "authToken": "d817df94",
                "errorCode": 0
            }
        }

        maas360_utils = self._create_maas360_utils()
        assert maas360_utils.get_auth_token() == "d817df94"

    @pytest.mark.parametrize("results", [
        {"authResponse": {"errorCode": 1}},
        {"authResponse": None}
    ])
    @patch('fn_maas360.lib.maas360_common.RequestsCommon.execute_call')
    def test_generate_auth_token_error(self, mocked_api_call, results):
        """ Test generate_auth_token error"""
        print("Test generate_auth_token error\n")

        mocked_api_call.return_value = results

        try:
            self._create_maas360_utils()
            assert False
        except IntegrationError:
            assert True

    @patch('fn_maas360.lib.maas360_common.RequestsCommon.execute_call')
    def test_generate_auth_token_side_effect_err(self, mocked_api_call):
        """ Test generate_auth_token side effect error"""
        print("Test generate_auth_token side effect error\n")

        mocked_api_call.side_effect = IntegrationError('Some error here')

        try:
            self._create_maas360_utils()
            assert False
        except IntegrationError:
            assert True

    @patch('fn_maas360.lib.maas360_common.MaaS360Utils.generate_auth_token')
    @patch('fn_maas360.lib.maas360_common.RequestsCommon.execute_call')
    def test_basic_search(self, mocked_api_call, mocked_auth_token):
        """ Test Basic Search"""
        print("Test Basic Search\n")

        mocked_auth_token.return_value = "mocked_auth_token"
        mocked_api_call.return_value = {
            "devices": {
                "device": {"maas360DeviceID": "androidc60775214"},
                "count": 1
            }
        }

        maas360_utils = self._create_maas360_utils()
        devices = maas360_utils.basic_search("basic_search_url", "query_string")
        assert devices == {"device": {"maas360DeviceID": "androidc60775214"}, "count": 1}

    @patch('fn_maas360.lib.maas360_common.MaaS360Utils.generate_auth_token')
    @patch('fn_maas360.lib.maas360_common.RequestsCommon.execute_call')
    def test_basic_search_side_effect_error(self, mocked_api_call, mocked_auth_token):
        """ Test Basic Search side effect error"""
        print("Test Search for devices in Maas360 side effect error\n")

        mocked_auth_token.return_value = "mocked_auth_token"
        mocked_api_call.side_effect = IntegrationError('Some error here')

        try:
            maas360_utils = self._create_maas360_utils()
            maas360_utils.basic_search("basic_search_url", "query_string")
            assert False
        except IntegrationError:
            assert True

    @patch('fn_maas360.lib.maas360_common.MaaS360Utils.generate_auth_token')
    def test_get_auth_headers(self, mocked_auth_token):
        """ Test get auth headers"""
        print("Test get auth headers\n")
        mocked_auth_token.return_value = "mocked_auth_token"

        maas360_utils = self._create_maas360_utils()
        headers = maas360_utils.get_auth_headers("content_type_header")
        assert headers == {"Accept": "application/json",
                           "Content-Type": "content_type_header",
                           "Authorization": "MaaS token='mocked_auth_token'"}

    @pytest.mark.parametrize("inputs,results", [
        ({
            "actionResponse": {
                "actionStatus": 0,
                "maas360DeviceID": "ApplC7CSG5PBHG75",
                "latitude": 39.955994,
                "longitude": -75.167178}},
         {
            "actionStatus": 0,
            "maas360DeviceID": "ApplC7CSG5PBHG75",
            "latitude": 39.955994,
            "longitude": -75.167178}),
        ({"actionResponse": None}, None)
    ])
    @patch('fn_maas360.lib.maas360_common.MaaS360Utils.generate_auth_token')
    @patch('fn_maas360.lib.maas360_common.RequestsCommon.execute_call')
    def test_locate_device(self, mocked_api_call, mocked_auth_token, inputs, results):
        """ Test Locate device"""
        print("Test Locate device\n")

        mocked_auth_token.return_value = "mocked_auth_token"
        mocked_api_call.return_value = inputs

        maas360_utils = self._create_maas360_utils()
        action_response = maas360_utils.locate_device("locate_device_url", "device_id")
        assert action_response == results

    @patch('fn_maas360.lib.maas360_common.MaaS360Utils.generate_auth_token')
    @patch('fn_maas360.lib.maas360_common.RequestsCommon.execute_call')
    def test_locate_device_side_effect_error(self, mocked_api_call, mocked_auth_token):
        """ Test Locate device side effect error"""
        print("Test Locate device side effect error\n")

        mocked_auth_token.return_value = "mocked_auth_token"
        mocked_api_call.side_effect = IntegrationError('Some error here')

        try:
            maas360_utils = self._create_maas360_utils()
            maas360_utils.locate_device("locate_device_url", "query_string")
            assert False
        except IntegrationError:
            assert True

    @patch('fn_maas360.lib.maas360_common.MaaS360Utils.generate_auth_token')
    @patch('fn_maas360.lib.maas360_common.RequestsCommon.execute_call')
    def test_locate_device_error(self, mocked_api_call, mocked_auth_token):
        """ Test Locate device side effect error"""
        print("Test Locate device side effect error\n")

        mocked_auth_token.return_value = "mocked_auth_token"
        mocked_api_call.return_value = {
            "actionResponse": {
                "actionStatus": 1
            }
        }

        try:
            maas360_utils = self._create_maas360_utils()
            maas360_utils.locate_device("locate_device_url", "query_string")
            assert False
        except IntegrationError:
            assert True

    @pytest.mark.parametrize("inputs,results", [
        ({"deviceSoftwares": {"deviceSw": "mock_value"}},
         {"deviceSw": "mock_value"}),
        ({"deviceSoftwares": None}, None)
    ])
    @patch('fn_maas360.lib.maas360_common.MaaS360Utils.generate_auth_token')
    @patch('fn_maas360.lib.maas360_common.RequestsCommon.execute_call')
    def test_get_software_installed(self, mocked_api_call, mocked_auth_token, inputs, results):
        """ Test Get Software installed"""
        print("Test Get Software installed\n")

        mocked_auth_token.return_value = "mocked_auth_token"
        mocked_api_call.return_value = inputs

        maas360_utils = self._create_maas360_utils()
        action_response = maas360_utils.get_software_installed("soft_install_url", "device_id")
        assert action_response == results

    @patch('fn_maas360.lib.maas360_common.MaaS360Utils.generate_auth_token')
    @patch('fn_maas360.lib.maas360_common.RequestsCommon.execute_call')
    def test_lget_software_installed_side_effect_error(self, mocked_api_call, mocked_auth_token):
        """ Test Get Software installed side effect error"""
        print("Test Get Software installed side effect error\n")

        mocked_auth_token.return_value = "mocked_auth_token"
        mocked_api_call.side_effect = IntegrationError('Some error here')

        try:
            maas360_utils = self._create_maas360_utils()
            maas360_utils.get_software_installed("soft_install_url", "query_string")
            assert False
        except IntegrationError:
            assert True



