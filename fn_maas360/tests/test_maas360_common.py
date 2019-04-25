# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2019. All Rights Reserved.

import sys
import pytest
from fn_maas360.lib.maas360_common import MaaS360Utils, APP_TYPE_DICT, TARGET_DEVICES_DICT
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
         {"deviceSw": "mock_value"})
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
    def test_get_software_installed_side_effect_error(self, mocked_api_call, mocked_auth_token):
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

    @pytest.mark.parametrize("inputs,results", [
        ({"actionResponse": {"maas360DeviceID": "mock_device_id"}},
         {"maas360DeviceID": "mock_device_id"})
    ])
    @patch('fn_maas360.lib.maas360_common.MaaS360Utils.generate_auth_token')
    @patch('fn_maas360.lib.maas360_common.RequestsCommon.execute_call')
    def test_lock_device(self, mocked_api_call, mocked_auth_token, inputs, results):
        """ Test Lock Device"""
        print("Test Lock Device\n")

        mocked_auth_token.return_value = "mocked_auth_token"
        mocked_api_call.return_value = inputs

        maas360_utils = self._create_maas360_utils()
        action_response = maas360_utils.lock_device("lock_url", "device_id")
        assert action_response == results

    @patch('fn_maas360.lib.maas360_common.MaaS360Utils.generate_auth_token')
    @patch('fn_maas360.lib.maas360_common.RequestsCommon.execute_call')
    def test_lock_device_side_effect_error(self, mocked_api_call, mocked_auth_token):
        """ Test Lock Device side effect error"""
        print("Test Lock Device side effect error\n")

        mocked_auth_token.return_value = "mocked_auth_token"
        mocked_api_call.side_effect = IntegrationError('Some error here')

        try:
            maas360_utils = self._create_maas360_utils()
            maas360_utils.lock_device("lock_url", "device_id")
            assert False
        except IntegrationError:
            assert True

    @pytest.mark.parametrize("inputs,results", [
        ({"actionResponse": {"maas360DeviceID": "mock_device_id"}},
         {"maas360DeviceID": "mock_device_id"})
    ])
    @patch('fn_maas360.lib.maas360_common.MaaS360Utils.generate_auth_token')
    @patch('fn_maas360.lib.maas360_common.RequestsCommon.execute_call')
    def test_wipe_device(self, mocked_api_call, mocked_auth_token, inputs, results):
        """ Test Wipe Device"""
        print("Test Wipe Device\n")

        mocked_auth_token.return_value = "mocked_auth_token"
        mocked_api_call.return_value = inputs

        maas360_utils = self._create_maas360_utils()
        action_response = maas360_utils.wipe_device("wipe_url", "device_id", "notify_me", "notify_user", "notify_others")
        assert action_response == results

    @patch('fn_maas360.lib.maas360_common.MaaS360Utils.generate_auth_token')
    @patch('fn_maas360.lib.maas360_common.RequestsCommon.execute_call')
    def test_wipe_device_side_effect_error(self, mocked_api_call, mocked_auth_token):
        """ Test Wipe Device side effect error"""
        print("Test Wipe Device side effect error\n")

        mocked_auth_token.return_value = "mocked_auth_token"
        mocked_api_call.side_effect = IntegrationError('Some error here')

        try:
            maas360_utils = self._create_maas360_utils()
            maas360_utils.wipe_device("wipe_url", "device_id", "notify_me", "notify_user", "notify_others")
            assert False
        except IntegrationError:
            assert True

    @pytest.mark.parametrize("inputs,results", [
        ({"actionResponse": {"maas360DeviceID": "mock_device_id"}},
         {"maas360DeviceID": "mock_device_id"})
    ])
    @patch('fn_maas360.lib.maas360_common.MaaS360Utils.generate_auth_token')
    @patch('fn_maas360.lib.maas360_common.RequestsCommon.execute_call')
    def test_cancel_pending_wipe(self, mocked_api_call, mocked_auth_token, inputs, results):
        """ Test Cancel Pending Wipe"""
        print("Test Cancel Pending Wipe\n")

        mocked_auth_token.return_value = "mocked_auth_token"
        mocked_api_call.return_value = inputs

        maas360_utils = self._create_maas360_utils()
        action_response = maas360_utils.cancel_pending_wipe("cancel_wipe_url", "device_id")
        assert action_response == results

    @patch('fn_maas360.lib.maas360_common.MaaS360Utils.generate_auth_token')
    @patch('fn_maas360.lib.maas360_common.RequestsCommon.execute_call')
    def test_cancel_pending_wipe_side_effect_error(self, mocked_api_call, mocked_auth_token):
        """ Test Cancel Pending Wipe side effect error"""
        print("Test Cancel Pending Wipe side effect error\n")

        mocked_auth_token.return_value = "mocked_auth_token"
        mocked_api_call.side_effect = IntegrationError('Some error here')

        try:
            maas360_utils = self._create_maas360_utils()
            maas360_utils.cancel_pending_wipe("cancel_wipe_url", "device_id")
            assert False
        except IntegrationError:
            assert True

    @pytest.mark.parametrize("inputs,results", [
        ("iOS Enterprise Application", 1),
        ("iOS App Store Application", 2),
        ("Android Enterprise Application", 3),
        ("Android Market Application", 4)
    ])
    def test_app_type_dict(self, inputs, results):
        """ Test APP_TYPE_DICT"""
        print("Test APP_TYPE_DICT\n")

        app_type_int_value = APP_TYPE_DICT.get(inputs)
        assert app_type_int_value == results

    @pytest.mark.parametrize("inputs,results", [
        ("All Devices", 0),
        ("Device Group", 1),
        ("Specific Device", 2)
    ])
    def test_app_target_devices_dict(self, inputs, results):
        """ Test TARGET_DEVICES_DICT"""
        print("Test TARGET_DEVICES_DICT\n")

        target_device_int_value = TARGET_DEVICES_DICT.get(inputs)
        assert target_device_int_value == results

    @pytest.mark.parametrize("value,results", [
        ("deviceID", {"key": "deviceID"}),
        (None, {})
    ])
    @patch('fn_maas360.lib.maas360_common.MaaS360Utils.generate_auth_token')
    def test_add_to_dict(self, mocked_auth_token, value, results):
        """ Test add to dict"""
        print("Test add to dict\n")

        mocked_auth_token.return_value = "mocked_auth_token"
        maas360_utils = self._create_maas360_utils()

        params = {}
        maas360_utils.add_to_dict("key", value, params)
        assert params == results

    @pytest.mark.parametrize("inputs,results", [
        ({"actionResponse": {"maas360DeviceID": "mock_device_id"}},
         {"maas360DeviceID": "mock_device_id"})
    ])
    @patch('fn_maas360.lib.maas360_common.MaaS360Utils.generate_auth_token')
    @patch('fn_maas360.lib.maas360_common.RequestsCommon.execute_call')
    def test_stop_app_distribution(self, mocked_api_call, mocked_auth_token, inputs, results):
        """ Test Stop App Distribution"""
        print("Test Stop App Distribution\n")

        mocked_auth_token.return_value = "mocked_auth_token"
        mocked_api_call.return_value = inputs

        maas360_utils = self._create_maas360_utils()
        action_response = maas360_utils.stop_app_distribution("cancel_wipe_url", "iOS Enterprise Application",
                                                              "installed_app_id", "Specific Device", "device_id",
                                                              "device_group_id")
        assert action_response == results

    @patch('fn_maas360.lib.maas360_common.MaaS360Utils.generate_auth_token')
    @patch('fn_maas360.lib.maas360_common.RequestsCommon.execute_call')
    def test_stop_app_distribution_side_effect_error(self, mocked_api_call, mocked_auth_token):
        """ Test Stop App Distribution side effect error"""
        print("Test Stop App Distribution side effect error\n")

        mocked_auth_token.return_value = "mocked_auth_token"
        mocked_api_call.side_effect = IntegrationError('status_code: 400, msg: N/A')

        try:
            maas360_utils = self._create_maas360_utils()
            maas360_utils.stop_app_distribution("cancel_wipe_url", "iOS Enterprise Application", "installed_app_id",
                                                "Specific Device", "device_id", "device_group_id")
            assert False
        except IntegrationError as err:
            if "status_code: 400, msg: N/A" in err.value:
                assert True
            else:
                assert False

    @patch('fn_maas360.lib.maas360_common.MaaS360Utils.generate_auth_token')
    @patch('fn_maas360.lib.maas360_common.RequestsCommon.execute_call')
    def test_stop_app_distribution_side_effect_error2(self, mocked_api_call, mocked_auth_token):
        """ Test Stop App Distribution side effect error 2"""
        print("Test Stop App Distribution side effect error 2\n")

        mocked_auth_token.return_value = "mocked_auth_token"
        mocked_api_call.side_effect = IntegrationError('some error here')

        try:
            maas360_utils = self._create_maas360_utils()
            maas360_utils.stop_app_distribution("cancel_wipe_url", "iOS Enterprise Application", "installed_app_id",
                                                "Specific Device", "device_id", "device_group_id")
            assert False
        except IntegrationError as err:
            if "status_code: 400, msg: N/A" in err.value:
                assert False
            else:
                assert True

    @pytest.mark.parametrize("inputs,results", [
        ({"actionResponse": {"maas360DeviceID": "mock_device_id"}},
         {"maas360DeviceID": "mock_device_id"})
    ])
    @patch('fn_maas360.lib.maas360_common.MaaS360Utils.generate_auth_token')
    @patch('fn_maas360.lib.maas360_common.RequestsCommon.execute_call')
    def test_delete_app(self, mocked_api_call, mocked_auth_token, inputs, results):
        """ Test Delete App"""
        print("Test Delete App\n")

        mocked_auth_token.return_value = "mocked_auth_token"
        mocked_api_call.return_value = inputs

        maas360_utils = self._create_maas360_utils()
        action_response = maas360_utils.delete_app("cancel_wipe_url", "iOS Enterprise Application", "installed_app_id")
        assert action_response == results

    @patch('fn_maas360.lib.maas360_common.MaaS360Utils.generate_auth_token')
    @patch('fn_maas360.lib.maas360_common.RequestsCommon.execute_call')
    def test_delete_app_side_effect_error(self, mocked_api_call, mocked_auth_token):
        """ Test Delete App side effect error"""
        print("Test Delete App side effect error\n")

        mocked_auth_token.return_value = "mocked_auth_token"
        mocked_api_call.side_effect = IntegrationError('Some error here')

        try:
            maas360_utils = self._create_maas360_utils()
            maas360_utils.delete_app("cancel_wipe_url", "iOS Enterprise Application", "installed_app_id")
            assert False
        except IntegrationError:
            assert True
