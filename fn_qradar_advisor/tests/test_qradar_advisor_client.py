# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.


from fn_qradar_advisor.lib.qradar_advisor_client import QRadarAdvisorClient
from fn_qradar_advisor.lib.qradar_advisor_client import CsrfTokenError
from fn_qradar_advisor.lib.qradar_advisor_client import QuickSearchError
from fn_qradar_advisor.lib.qradar_advisor_client import OffenseInsightsError
from fn_qradar_advisor.lib.qradar_advisor_client import QRadarOffenseAnalysis
from fn_qradar_advisor.lib.qradar_advisor_client import XFECredentialError
from fn_qradar_advisor.lib.qradar_advisor_client import QRadarFullSearch
from fn_qradar_advisor.lib.search_wait_command import SearchJobFailure
from fn_qradar_advisor.lib.search_wait_command import SearchFailure


from fn_qradar_advisor.lib.qradar_http_info import HttpInfo
import requests
from mock import Mock
from mock import patch
import mock
import json

import logging

logging.basicConfig(filename="testing.log", level=logging.DEBUG)

QRADAR_HOST = "the.qradar.host.com"
QRADAR_TOKEN = "bogus qradar token"
CSRF_TOKEN = "bogus csfr token"
QRADAR_APP_ID = 1234
QRADAR_API_BASE_URL=QRADAR_HOST+"/console/plugins/" + str(QRADAR_APP_ID) + "/app_proxy/api"
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

class TestQRadarAdvisorClient(object):
    @patch("fn_qradar_advisor.lib.qradar_advisor_client.HttpInfo.update_session")
    @patch("fn_qradar_advisor.lib.qradar_advisor_client.HttpInfo.get_session")
    def test_get_csrf_token(self, mocked_get_session, mocked_update_session):

        mocked_cookies = Mock()
        # Use this to mock the member variables
        mocked_session = Mock(cookies=mocked_cookies)
        mocked_get_session.return_value = mocked_session

        client = QRadarAdvisorClient(qradar_host=QRADAR_HOST,
                                     advisor_app_id=QRADAR_APP_ID,
                                     qradar_token=QRADAR_TOKEN,
                                     cafile=QRADAR_VERIFY,
                                     log=logging)

        mocked_session.get.return_value = _generate_response({}, 200)
        ret_cookies = {"XSRF-TOKEN": CSRF_TOKEN}
        mocked_cookies.get_dict.return_value = ret_cookies

        client.get_csrf_token()

        #
        # Assert that QRadarAdvisorClient is calling the /about endpoint to get CSRF token
        #
        url = QRADAR_API_BASE_URL + "/about"
        mocked_session.get.assert_called_with(url=url,
                                              verify=QRADAR_VERIFY)
        #
        # Assert that QRadarAdvisorClient is using the cookies (ret_cookies here)
        # returned from the mocked session to update the HttpInfo.
        #
        mocked_update_session.assert_called_with(ret_cookies)


        #
        # Verify error handling. Simulate that the /about endpoint returns 400
        #
        mocked_session.get.return_value = _generate_response({}, 400)
        try:
            client.get_csrf_token()
            assert False
        except CsrfTokenError:
            assert True

    def test_set_methods(self):
        stage = "stage1"
        timeout = 3600
        period = 10

        client = QRadarAdvisorClient(qradar_host=QRADAR_HOST,
                                     advisor_app_id=QRADAR_APP_ID,
                                     qradar_token=QRADAR_TOKEN,
                                     cafile=False,
                                     log=logging)
        client.set_full_search_stage(stage)
        assert client.full_search_stage == stage

        client.set_full_search_timeout(timeout)
        assert client.full_search_timeout == timeout

        client.set_full_search_period(period)
        assert client.full_search_period == period

    @patch("fn_qradar_advisor.lib.qradar_advisor_client.HttpInfo.update_session")
    @patch("fn_qradar_advisor.lib.qradar_advisor_client.HttpInfo.get_session")
    @patch("fn_qradar_advisor.lib.qradar_advisor_client.QRadarFullSearch.perform_search")
    def test_full_search(self, mocked_perform_search, mocked_get_session, mocked_update_session):

        #
        # First verify that if there is no CSRF token, the full_search
        # function will call get_csrf_token to get one
        #
        mocked_cookies = Mock()
        # Use this to mock the member variables
        mocked_session = Mock(cookies=mocked_cookies)
        mocked_get_session.return_value = mocked_session

        client = QRadarAdvisorClient(qradar_host=QRADAR_HOST,
                                     advisor_app_id=QRADAR_APP_ID,
                                     qradar_token=QRADAR_TOKEN,
                                     cafile=QRADAR_VERIFY,
                                     log=logging)
        #
        # when a QRadarAdvisorClient is instantiated, its http_info shall
        # has no csrf token
        #
        assert not client.http_info.xsrf_token

        try:
            mocked_session.get.return_value = _generate_response({}, 400)
            client.full_search("Does not matter")
            assert False
        except CsrfTokenError:
            #
            # because the CSRF token is None, full_search has to call get_csrf_token
            # to get it. Since we returned 400 above, the full_search call
            # shall throw this exception
            #
            assert True

        #
        # Now put a CSRF token
        #
        client.http_info.xsrf_token = CSRF_TOKEN
        ret_cookies = {"XSRF-TOKEN": CSRF_TOKEN}
        mocked_cookies.get_dict.return_value = ret_cookies

        #
        # This time full_search will call the full search endpoint
        #

        stix_json = {"type":"bundles"}
        mocked_perform_search.return_value = stix_json

        search_value = "user:jsmith"

        ret = client.full_search(search_value)
        mocked_perform_search.assert_called_with(search_value)

        assert ret == stix_json


    @patch("fn_qradar_advisor.lib.qradar_advisor_client.HttpInfo.update_session")
    @patch("fn_qradar_advisor.lib.qradar_advisor_client.HttpInfo.get_session")
    @patch("fn_qradar_advisor.lib.qradar_advisor_client.QRadarFullSearch.get_search_result")
    def test_full_search_by_id(self, mocked_get_search_result, mocked_get_session, mocked_update_session):

        #
        # First verify that if there is no CSRF token, the full_search
        # function will call get_csrf_token to get one
        #
        mocked_cookies = Mock()
        # Use this to mock the member variables
        mocked_session = Mock(cookies=mocked_cookies)
        mocked_get_session.return_value = mocked_session

        client = QRadarAdvisorClient(qradar_host=QRADAR_HOST,
                                     advisor_app_id=QRADAR_APP_ID,
                                     qradar_token=QRADAR_TOKEN,
                                     cafile=QRADAR_VERIFY,
                                     log=logging)
        #
        # when a QRadarAdvisorClient is instantiated, its http_info shall
        # has no csrf token
        #
        assert not client.http_info.xsrf_token

        try:
            mocked_session.get.return_value = _generate_response({}, 400)
            client.full_search_by_id(123456)
            assert False
        except CsrfTokenError:
            #
            # because the CSRF token is None, full_search has to call get_csrf_token
            # to get it. Since we returned 400 above, the full_search call
            # shall throw this exception
            #
            assert True

        #
        # Now put a CSRF token
        #
        client.http_info.xsrf_token = CSRF_TOKEN
        ret_cookies = {"XSRF-TOKEN": CSRF_TOKEN}
        mocked_cookies.get_dict.return_value = ret_cookies

        #
        # This time full_search will call the full search endpoint
        #

        stix_json = {"type":"bundles"}
        mocked_get_search_result.return_value = stix_json

        search_id = 1234

        ret = client.full_search_by_id(search_id)
        mocked_get_search_result.assert_called_with(search_id)

        assert ret == stix_json

    @patch("fn_qradar_advisor.lib.qradar_advisor_client.HttpInfo.update_session")
    @patch("fn_qradar_advisor.lib.qradar_advisor_client.HttpInfo.get_session")
    def test_quick_search(self, mocked_get_session, mocked_update_session):
        #
        # First verify that if there is no CSRF token, the full_search
        # function will call get_csrf_token to get one
        #
        mocked_cookies = Mock()
        # Use this to mock the member variables
        mocked_session = Mock(cookies=mocked_cookies)
        mocked_get_session.return_value = mocked_session

        client = QRadarAdvisorClient(qradar_host=QRADAR_HOST,
                                     advisor_app_id=QRADAR_APP_ID,
                                     qradar_token=QRADAR_TOKEN,
                                     cafile=QRADAR_VERIFY,
                                     log=logging)
        #
        # when a QRadarAdvisorClient is instantiated, its http_info shall
        # has no csrf token
        #
        assert not client.http_info.xsrf_token

        try:
            mocked_session.get.return_value = _generate_response({}, 400)
            client.quick_search("Not matter here")
            assert False
        except CsrfTokenError:
            #
            # because the CSRF token is None, full_search has to call get_csrf_token
            # to get it. Since we returned 400 above, the full_search call
            # shall throw this exception
            #
            assert True

        #
        # Now put a CSRF token
        #
        client.http_info.xsrf_token = CSRF_TOKEN
        ret_cookies = {"XSRF-TOKEN": CSRF_TOKEN}
        mocked_cookies.get_dict.return_value = ret_cookies

        url = QRADAR_API_BASE_URL + "/search/quick"

        search_value = "user:jsmith"

        search_dict = {"indicator": search_value}
        dict_str = json.dumps(search_dict)
        quick_search_result = {"suspicious_observables":[],
                               "other_observables":[]}

        mocked_session.post.return_value = _generate_response(quick_search_result, 200)

        ret = client.quick_search(search_value)

        assert ret == quick_search_result
        mocked_session.post.assert_called_with(url=url,
                                               data=dict_str,
                                               verify=QRADAR_VERIFY)

        #
        # Verify status_code other than 200 shall result in exception
        #
        mocked_session.post.return_value = _generate_response(quick_search_result, 422)
        try:
            client.quick_search(search_value)
            assert False
        except QuickSearchError:
            assert True

        #
        # Verify exception of post call
        #
        mocked_session.post.side_effect = Exception("Some error exception")
        try:
            client.quick_search(search_value)
            assert False
        except QuickSearchError:
            assert True

    @patch("fn_qradar_advisor.lib.qradar_advisor_client.HttpInfo.update_session")
    @patch("fn_qradar_advisor.lib.qradar_advisor_client.HttpInfo.get_session")
    def test_offense_insights(self, mocked_get_session, mocked_update_session):
        #
        # First verify that if there is no CSRF token, the full_search
        # function will call get_csrf_token to get one
        #
        mocked_cookies = Mock()
        # Use this to mock the member variables
        mocked_session = Mock(cookies=mocked_cookies)
        mocked_get_session.return_value = mocked_session

        client = QRadarAdvisorClient(qradar_host=QRADAR_HOST,
                                     advisor_app_id=QRADAR_APP_ID,
                                     qradar_token=QRADAR_TOKEN,
                                     cafile=QRADAR_VERIFY,
                                     log=logging)
        #
        # when a QRadarAdvisorClient is instantiated, its http_info shall
        # has no csrf token
        #
        assert not client.http_info.xsrf_token

        try:
            mocked_session.get.return_value = _generate_response({}, 400)
            client.offense_insights(12345678)
            assert False
        except CsrfTokenError:
            #
            # because the CSRF token is None, full_search has to call get_csrf_token
            # to get it. Since we returned 400 above, the full_search call
            # shall throw this exception
            #
            assert True

        #
        # Now put a CSRF token
        #
        client.http_info.xsrf_token = CSRF_TOKEN
        ret_cookies = {"XSRF-TOKEN": CSRF_TOKEN}
        mocked_cookies.get_dict.return_value = ret_cookies

        offense_id = 12345

        url = QRADAR_API_BASE_URL + "/offense/" + str(offense_id) + "/insights"
        ret_json = {"insights": "Sample insights from Watson"}

        mocked_session.get.return_value = _generate_response(ret_json, 200)

        ret = client.offense_insights(offense_id)

        assert ret == ret_json

        #
        # Now test non 200 status_code
        #
        try:
            mocked_session.get.return_value = _generate_response(ret_json, 403)
            client.offense_insights(offense_id)
            assert False
        except OffenseInsightsError:
            assert True


        #
        # Test exception
        #
        try:
            mocked_session.get.side_effect = Exception("Some error exception")
            client.offense_insights(offense_id)
            assert False
        except OffenseInsightsError:
            assert True

    @patch("fn_qradar_advisor.lib.qradar_advisor_client.HttpInfo.get_session")
    @patch("fn_qradar_advisor.lib.qradar_advisor_client.QRadarOffenseAnalysis.perform_search")
    @patch("fn_qradar_advisor.lib.qradar_advisor_client.QRadarOffenseAnalysis.get_search_result")
    def test_offense_analysis(self,
                              mocked_get_search_result,
                              mocked_perform_search,
                              mocked_get_session):

        #
        # First verify that if there is no CSRF token, the full_search
        # function will call get_csrf_token to get one
        #
        mocked_cookies = Mock()
        # Use this to mock the member variables
        mocked_session = Mock(cookies=mocked_cookies)
        mocked_get_session.return_value = mocked_session

        client = QRadarAdvisorClient(qradar_host=QRADAR_HOST,
                                     advisor_app_id=QRADAR_APP_ID,
                                     qradar_token=QRADAR_TOKEN,
                                     cafile=QRADAR_VERIFY,
                                     log=logging)
        #
        # when a QRadarAdvisorClient is instantiated, its http_info shall
        # has no csrf token
        #
        assert not client.http_info.xsrf_token

        try:
            mocked_session.get.return_value = _generate_response({}, 400)
            client.offense_analysis(123456)
            assert False
        except CsrfTokenError:
            #
            # because the CSRF token is None, full_search has to call get_csrf_token
            # to get it. Since we returned 400 above, the full_search call
            # shall throw this exception
            #
            assert True

        #
        # Now put a CSRF token
        #
        client.http_info.xsrf_token = CSRF_TOKEN
        ret_cookies = {"XSRF-TOKEN": CSRF_TOKEN}
        mocked_cookies.get_dict.return_value = ret_cookies

        #
        # This time offense_analysis shall call the QRadarOffenseAnalysis
        #

        stix_json = {"type": "bundles"}

        mocked_get_search_result.return_value = stix_json
        mocked_perform_search.return_value = stix_json

        offense_id = 12345

        ret = client.offense_analysis(offense_id,
                                      restart_if_existed=False)

        assert ret == stix_json
        # because we set restart_if_existed=False, verify we call get_search_result
        # directly
        mocked_get_search_result.assert_called_with(offense_id)

        ret = client.offense_analysis(offense_id,
                                      restart_if_existed=True)

        assert ret == stix_json
        # because we set restart_if_existed=True, verify we call perform_search
        # to start a new analysis
        mocked_perform_search.assert_called_with(offense_id)


class TestQRadarFullSearch(object):
    @patch("fn_qradar_advisor.lib.qradar_advisor_client.HttpInfo.get_session")
    def test_get_qradar_full_search(self, mocked_get_session):

        mocked_cookies = Mock()
        # Use this to mock the member variables
        mocked_session = Mock(cookies=mocked_cookies)
        mocked_get_session.return_value = mocked_session

        search_value = "user:jsmith"

        url = QRADAR_API_BASE_URL + "/search/full"

        data_str = json.dumps({"indicator": search_value})
        search_id = 123
        not_used = 456
        ret_dict = {
            "search_ids":[search_id, not_used]
        }

        mocked_session.post.return_value = _generate_response(ret_dict, 200)

        http_info = HttpInfo(qradar_host=QRADAR_HOST,
                             advisor_app_id=QRADAR_APP_ID,
                             qradar_token=QRADAR_TOKEN,
                             cafile=True,
                             log=logging)
        timeout=3600
        period=10
        return_stage = "stage3"
        full_search = QRadarFullSearch(http_info=http_info,
                                       log=logging,
                                       return_stage=return_stage,
                                       timeout=3600,
                                       period=10)

        #
        # Verify member variables are set by instructor
        #
        assert full_search.search_timeout == timeout
        assert full_search.period == period
        assert full_search.return_stage == return_stage

        #
        # 1. Test get_search_id
        #
        ret = full_search.get_search_id(search_value)

        assert ret == search_id
        mocked_session.post.assert_called_with(url=url,
                                               data=data_str,
                                               verify=True)

        #
        # Test non-200 status code
        #
        mocked_session.post.return_value = _generate_response(ret_dict, 401)
        try:
            full_search.get_search_id(search_value)
            assert False
        except SearchJobFailure:
            assert True

        #
        # Test exception handling
        #
        mocked_session.post.side_effect = Exception("Some error exception")
        try:
            full_search.get_search_id(search_value)
            assert False
        except SearchJobFailure:
            assert True

        #
        # 2.Test check_status
        #

        url = QRADAR_API_BASE_URL + "/search/full/" + str(search_id)
        ret_dict = {
            "search_status": "PROCESSING STAGE3"
        }
        mocked_session.get.return_value = _generate_response(ret_dict, 200)

        ret = full_search.check_status(search_id)

        # QRadar Advisor returns PROCESSING STAGE3, we shall wait
        assert ret == full_search.SEARCH_STATUS_WAITING
        mocked_session.get.assert_called_with(url=url,
                                              verify=True)

        ret_dict["search_status"] = "DONE"

        ret = full_search.check_status(search_id)
        assert ret == full_search.SEARCH_STATUS_COMPLETED

        # If QRadar Advisor returns DONE, this means no stage3 data
        assert full_search.stage3_available == False

        ret_dict["search_status"] = "DONE_STAGE3"
        ret = full_search.check_status(search_id)
        assert ret == full_search.SEARCH_STATUS_COMPLETED

        # If QRadar Advisor returns DONE, this means no stage3 data
        assert full_search.stage3_available == True

        # Test status_code = 404. This means the search job does not
        # exist, we shall stop
        mocked_session.get.return_value = _generate_response(ret_dict, 404)
        ret = full_search.check_status(search_id)
        assert ret == full_search.SEARCH_STATUS_ERROR_STOP

        # Test exception handling
        mocked_session.get.side_effect = Exception("Some error")
        try:
            full_search.check_status(search_id)
            assert False
        except SearchFailure:
            assert True

        #
        # 3. Test get_search_result
        #

        # Test if user asks for stage3 but stage3 is not available
        full_search.return_stage = "stage3"
        full_search.stage3_available = False

        # We shall query stage2 data
        url = QRADAR_API_BASE_URL + "/search/full/" + str(search_id) + "/stix/stage2"

        stix_json = {
            "type": "bundle"
        }

        mocked_session.get.return_value = _generate_response(stix_json, 200)

        mocked_session.get.side_effect = None
        ret = full_search.get_search_result(search_id)
        assert ret == stix_json
        mocked_session.get.assert_called_with(url=url,
                                              verify=True)

        # stage3 is available
        full_search.stage3_available = True

        # We shall query stage3 data
        url = QRADAR_API_BASE_URL + "/search/full/" + str(search_id) + "/stix/stage3"

        ret = full_search.get_search_result(search_id)
        assert ret == stix_json
        mocked_session.get.assert_called_with(url=url,
                                              verify=True)

        # status_doce = 404 handling
        mocked_session.get.return_value = _generate_response(stix_json, 404)

        try:
            full_search.get_search_result(search_id)
            assert False
        except SearchFailure as e:
            assert True

        # other status_doce  handling
        mocked_session.get.return_value = _generate_response(stix_json, 400)

        try:
            full_search.get_search_result(search_id)
            assert False
        except SearchFailure as e:
            assert True

        # Exception handling
        mocked_session.get.side_effect = Exception("Some error")
        try:
            full_search.get_search_result(search_id)
            assert False
        except SearchFailure as e:
            assert True


class TestQRadarOffenseAnalysis(object):

    @patch("fn_qradar_advisor.lib.qradar_advisor_client.HttpInfo.get_session")
    def test_get_qradar_offense_analysis(self, mocked_get_session):

        mocked_cookies = Mock()
        # Use this to mock the member variables
        mocked_session = Mock(cookies=mocked_cookies)
        mocked_get_session.return_value = mocked_session

        offense_id = 1234

        url = QRADAR_API_BASE_URL + "/offense/" + str(offense_id) + "/analysis"

        ret_dict = {
            "status": "PROCESSING_LOCAL"
        }

        mocked_session.post.return_value = _generate_response(ret_dict, 200)

        http_info = HttpInfo(qradar_host=QRADAR_HOST,
                             advisor_app_id=QRADAR_APP_ID,
                             qradar_token=QRADAR_TOKEN,
                             cafile=True,
                             log=logging)
        timeout = 3600
        period = 10
        return_stage = "stage3"
        offense_analysis = QRadarOffenseAnalysis(http_info=http_info,
                                                 log=logging,
                                                 return_stage=return_stage,
                                                 timeout=3600,
                                                 period=10)

        #
        # Verify member variables are set by instructor
        #
        assert offense_analysis.search_timeout == timeout
        assert offense_analysis.period == period
        assert offense_analysis.return_stage == return_stage

        #
        # 1. Test get_search_id
        #
        ret = offense_analysis.get_search_id(offense_id)

        assert ret == offense_id
        mocked_session.post.assert_called_with(url=url,
                                               verify=True)

        #
        # Test 401 status code
        #
        mocked_session.post.return_value = _generate_response(ret_dict, 401)
        try:
            offense_analysis.get_search_id(offense_id)
            assert False
        except XFECredentialError:
            assert True

        #
        # Test 403 status code
        #
        mocked_session.post.return_value = _generate_response(ret_dict, 403)
        try:
            offense_analysis.get_search_id(offense_id)
            assert False
        except SearchJobFailure:
            assert True

        #
        # Test 429 status code
        #
        mocked_session.post.return_value = _generate_response(ret_dict, 429)
        try:
            offense_analysis.get_search_id(offense_id)
            assert False
        except SearchJobFailure:
            assert True

        #
        # Test 400 status code
        #
        mocked_session.post.return_value = _generate_response(ret_dict, 400)
        try:
            offense_analysis.get_search_id(offense_id)
            assert False
        except SearchJobFailure:
            assert True

        #
        # Test exception handling
        #
        mocked_session.post.side_effect = Exception("Some error exception")
        try:
            offense_analysis.get_search_id(offense_id)
            assert False
        except SearchJobFailure:
            assert True

        #
        # 2.Test check_status
        #

        url = QRADAR_API_BASE_URL + "/offense/" + str(offense_id) + "/analysis/status"
        ret_dict = {
            "status": "PROCESSING STAGE3"
        }
        mocked_session.get.return_value = _generate_response(ret_dict, 200)

        ret = offense_analysis.check_status(offense_id)

        # QRadar Advisor returns PROCESSING STAGE3, we shall wait
        assert ret == offense_analysis.SEARCH_STATUS_WAITING
        mocked_session.get.assert_called_with(url=url,
                                              verify=True)

        ret_dict["status"] = "DONE"

        ret = offense_analysis.check_status(offense_id)
        assert ret == offense_analysis.SEARCH_STATUS_COMPLETED

        # If QRadar Advisor returns DONE, this means no stage3 data
        assert offense_analysis.stage3_available == False

        ret_dict["status"] = "DONE_STAGE3"
        ret = offense_analysis.check_status(offense_id)
        assert ret == offense_analysis.SEARCH_STATUS_COMPLETED

        # If QRadar Advisor returns DONE, this means no stage3 data
        assert offense_analysis.stage3_available == True

        # Test status_code = 403. This means the search job does not
        # exist, we shall stop
        mocked_session.get.return_value = _generate_response(ret_dict, 403)
        ret = offense_analysis.check_status(offense_id)
        assert ret == offense_analysis.SEARCH_STATUS_ERROR_STOP

        # Test exception handling
        mocked_session.get.side_effect = Exception("Some error")
        try:
            offense_analysis.check_status(offense_id)
            assert False
        except SearchFailure:
            assert True

        #
        # 3. Test get_search_result
        #

        # Test if user asks for stage3 but stage3 is not available
        offense_analysis.return_stage = "stage3"
        offense_analysis.stage3_available = False

        # We shall query stage2 data
        url = QRADAR_API_BASE_URL + "/offense/" + str(offense_id) + "/analysis/stage2/stix"

        stix_json = {
            "type": "bundle"
        }

        mocked_session.get.return_value = _generate_response(stix_json, 200)

        mocked_session.get.side_effect = None
        ret = offense_analysis.get_search_result(offense_id)
        assert ret == stix_json
        mocked_session.get.assert_called_with(url=url,
                                              verify=True)

        # stage3 is available
        offense_analysis.stage3_available = True

        # We shall query stage3 data
        url = QRADAR_API_BASE_URL + "/offense/" + str(offense_id) + "/analysis/stage3/stix"

        ret = offense_analysis.get_search_result(offense_id)
        assert ret == stix_json
        mocked_session.get.assert_called_with(url=url,
                                              verify=True)

        # status_doce = 404 handling
        mocked_session.get.return_value = _generate_response(stix_json, 404)

        try:
            offense_analysis.get_search_result(offense_id)
            assert False
        except SearchFailure as e:
            assert True

        # status_doce = 403 handling
        mocked_session.get.return_value = _generate_response(stix_json, 403)

        try:
            offense_analysis.get_search_result(offense_id)
            assert False
        except SearchFailure as e:
            assert True

        # other status_doce  handling
        mocked_session.get.return_value = _generate_response(stix_json, 400)

        try:
            offense_analysis.get_search_result(offense_id)
            assert False
        except SearchFailure as e:
            assert True

        # Exception handling
        mocked_session.get.side_effect = Exception("Some error")
        try:
            offense_analysis.get_search_result(offense_id)
            assert False
        except SearchFailure as e:
            assert True