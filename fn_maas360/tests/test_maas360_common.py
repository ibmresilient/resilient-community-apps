# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2019. All Rights Reserved.

import sys
import pytest
from resilient_lib.components.requests_common import RequestsCommon
from fn_maas360.lib.maas360_common import MaaS360Utils
if sys.version_info.major == 2:
    from mock import patch, Mock
else:
    from unittest.mock import patch, Mock


class TestMaaS360(object):
    """ Tests for the fn_maas360 functions"""

    @patch('resilient_lib.components.requests_common.RequestsCommon')
    def test_get_devices(self, mocked_api_call):
        """ Test get devices from Maas360"""
        print("Test get devices from Maas360\n")

        mocked_api_call.side_effect = {
            "devices": {
                "device": {"maas360DeviceID": "androidc60775214"},
                "count": 1
                }
        }

        rc = RequestsCommon()

        maas360_utils = MaaS360Utils("maas360_url", "billing_id", "username", "password", "app_id", "app_version",
                                     "platform_id", "app_access_key", rc)

        count, devices = maas360_utils.get_devices("basic_search_url", "query_string")

        assert count == 1
        assert devices == {"device": {"maas360DeviceID": "androidc60775214"},
                           "count": 1}
