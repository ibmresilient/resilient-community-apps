# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.

from fn_qradar_advisor.lib.qradar_cafm_client import QRadarCafmClient
from fn_qradar_advisor.lib.qradar_cafm_client import TacticsTokenError
from fn_qradar_advisor.lib.qradar_cafm_client import GetAllMappingsError

import logging
from mock import Mock
from mock import patch


logging.basicConfig(filename="testing.log", level=logging.DEBUG)

QRADAR_HOST = "the.qradar.host.com"
QRADAR_TOKEN = "bogus qradar token"
CSRF_TOKEN = "bogus csfr token"
QRADAR_CAMF_ID = 1234
QRADAR_API_BASE_URL="https://" + QRADAR_HOST+"/console/plugins/" + str(QRADAR_CAMF_ID) + "/app_proxy/api"
QRADAR_VERIFY = False

# Util function to generate simulated requests response
def _generate_response(content, status):
    class SimResponse:
        def __init__(self, content, status):
            self.status_code = status
            self.content = content

        def json(self):
            return self.content

    return SimResponse(content, status)


class TestQRadarCamfClient(object):
    @patch("fn_qradar_advisor.lib.qradar_advisor_client.HttpInfo.update_session_tactics")
    @patch("fn_qradar_advisor.lib.qradar_advisor_client.HttpInfo.get_session")
    def test_get_tactics_token(self, mocked_get_session, mocked_update_session):

        mocked_cookies = Mock()

        mocked_session = Mock(cookies=mocked_cookies)
        mocked_get_session.return_value = mocked_session

        client = QRadarCafmClient(qradar_host=QRADAR_HOST,
                                  cafm_app_id=QRADAR_CAMF_ID,
                                  cafm_token=QRADAR_TOKEN,
                                  cafile=QRADAR_VERIFY,
                                  log=logging)

        mocked_session.get.return_value = _generate_response({}, 200)
        ret_cookies = {"TACTICS-XSRF-TOKEN": CSRF_TOKEN}
        mocked_cookies.get_dict.return_value = ret_cookies

        client.get_tactics_token()

        #
        # Assert that QRadarCamfClient is calling the /config/tuning endpoint
        url = QRADAR_API_BASE_URL + "/config/tuning"
        mocked_session.get.assert_called_with(url=url,
                                              verify=QRADAR_VERIFY)

        #
        # Assert that QRadarCamfClient is using the cookies (ret_cookies here)
        # returned from the mocked session to update the HttpInfo.
        #
        mocked_update_session.assert_called_with(ret_cookies)

        #
        # Verify error handling. Simulate that the /about endpoint returns 400
        #
        mocked_session.get.return_value = _generate_response({}, 400)
        try:
            client.get_tactics_token()
            assert False
        except TacticsTokenError:
            assert True

    @patch("fn_qradar_advisor.lib.qradar_advisor_client.HttpInfo.get_session")
    def test_get_all_mappings(self, mocked_get_session):
        mocked_cookies = Mock()
        mocked_session = Mock(cookies=mocked_cookies)
        mocked_get_session.return_value = mocked_session

        client = QRadarCafmClient(qradar_host=QRADAR_HOST,
                                  cafm_app_id=QRADAR_CAMF_ID,
                                  cafm_token=QRADAR_TOKEN,
                                  cafile=QRADAR_VERIFY,
                                  log=logging)

        assert not client.http_info.xsrf_token

        try:
            mocked_session.get.return_value = _generate_response({}, 400)
            client.get_all_mapping()
            assert  False
        except TacticsTokenError:
            #
            #   Because there is no tactics token returned
            #
            assert True

        #
        # Now put in a CSRF token, so it would not need to get one
        #
        client.http_info.xsrf_token = CSRF_TOKEN
        ret_cookies = {"TACTICS-XSRF-TOKEN": CSRF_TOKEN}
        mocked_cookies.get_dict.return_value = ret_cookies
        mocked_session.get.return_value = _generate_response({}, 400)

        try:
            client.get_all_mapping()
            assert False
        except GetAllMappingsError:
            assert True

        # Test a good one
        mocked_return = Mock()
        mocked_session.get.return_value = _generate_response(mocked_return, 200)

        mappings = client.get_all_mapping()

        assert mappings == mocked_return

    @patch("fn_qradar_advisor.lib.qradar_cafm_client.QRadarCafmClient.get_all_mapping")
    def test_find_tactic_mapping(self, mocked_get_all_mapping):
        mapping = {
            "Rule 1": "Execution",
            "Rule 2": "Initial Access"
        }

        mocked_get_all_mapping.return_value = mapping

        client = QRadarCafmClient(qradar_host=QRADAR_HOST,
                                  cafm_app_id=QRADAR_CAMF_ID,
                                  cafm_token=QRADAR_TOKEN,
                                  cafile=QRADAR_VERIFY,
                                  log=logging)

        ret = client.find_tactic_mapping("Rule not existed")

        assert ret == {}

        ret = client.find_tactic_mapping("Rule 1")
        assert ret == mapping["Rule 1"]
