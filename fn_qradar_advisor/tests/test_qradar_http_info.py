# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

#
# Test file for qradar_http_info.py
#
from fn_qradar_advisor.lib.qradar_http_info import HttpInfo

class TestQRadarHttpInfo(object):

    def test_qradar_http_info(self):
        """

        :return:
        """
        host = "myhost.com"
        app_id = "12345"
        token = "abcdef1234567890"
        cafile = False

        http_info = HttpInfo(qradar_host=host,
                             advisor_app_id=app_id,
                             qradar_token=token,
                             cafile=cafile,
                             log=None)

        api_base_url = host + "/console/plugins/" + str(app_id) + "/app_proxy/api"

        # about url
        about_url = http_info.get_about_url()
        assert about_url == api_base_url + "/about"

        # quick search url
        quick_search_url = http_info.get_quick_search_url()
        assert quick_search_url == api_base_url + "/search/quick"

        # full search url
        full_search_url = http_info.get_full_search_url()
        assert full_search_url == api_base_url + "/search/full"

        # full search status
        search_id = 100
        assert http_info.get_full_search_status_url(search_id) == api_base_url + "/search/full/" + str(search_id)

        # full search result
        stage = "stage3"
        assert http_info.get_full_search_result_url(search_id, stage) == api_base_url + "/search/full/" + str(search_id) + "/stix/" + stage

        # analysis url
        offense_id = 123
        assert http_info.get_analysis_url(offense_id) == api_base_url + "/offense/" + str(offense_id) + "/analysis"

        # analysis status
        assert http_info.get_analysis_status_url(offense_id) == api_base_url + "/offense/" + str(offense_id) + "/analysis/status"

        # analysis result
        assert http_info.get_analysis_result_url(offense_id, stage) == api_base_url + "/offense/" + str(offense_id) + "/analysis/" + stage + "/stix"

        # offense insights
        assert http_info.get_offense_insights_url(offense_id) == api_base_url + "/offense/" + str(offense_id) + "/insights"

        # verify cert
        assert http_info.get_cafile() == cafile

        # token
        assert http_info.get_session().cookies["SEC"] == token

        # test reset
        http_info.get_session().headers["X-XSRF-TOKEN"] = "Fake CSRF Token"
        http_info.reset_session()
        assert "X-XSRF-TOKEN" not in http_info.get_session().headers

        cookies = {
            "XSRF-TOKEN": "New CSRF Token from QRadar Advidor"
        }
        http_info.update_session(cookies)
        assert http_info.get_session().headers["X-XSRF-TOKEN"] == cookies["XSRF-TOKEN"]


