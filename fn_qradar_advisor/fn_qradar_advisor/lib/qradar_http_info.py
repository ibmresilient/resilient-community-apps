# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
import requests
import base64

QRADAR_PULGIN_API_URL = "{host}/console/plugins/{app_id}/app_proxy/api"
QRADAR_OFFENSE_INSIGHTS_URL="/offense/{offense_id}/insights"
QRADAR_QUICK_SEARCH_URL = "/search/quick"
QRADAR_FULL_SEARCH_URL = "/search/full"
QRADAR_FULL_SEARCH_RESULT_URL = "/search/full/{search_id}/stix/{stage}"
QRADAR_ABOUT_URL="/about"
QRADAR_ANALYSIS_URL = "/offense/{offense_id}/analysis"
QRADAR_ANALYSIS_STATUS_URL = "/offense/{offense_id}/analysis/status"
QRADAR_ANALYSIS_RESULT_URL = "/offense/{offense_id}/analysis/{stage}/stix"


class HttpInfo(object):
    def __init__(self, qradar_host, advisor_app_id, qradar_token, cafile, log):
        self.host = qradar_host
        self.cafile = cafile
        self.app_id = advisor_app_id
        self.token = qradar_token
        self.xsrf_token = None
        self.log = log
        self.api_base_url = QRADAR_PULGIN_API_URL.format(host=self.host, app_id=self.app_id)

        self.session = requests.session()
        self.session.headers["Accept"] = "application/json"
        self.session.headers["Content-Type"] = "application/json"
        self.session.cookies["SEC"] = self.token

    def get_about_url(self):
        """
        Get the url to the api/about endpoint
        :return:
        """
        return self.api_base_url + QRADAR_ABOUT_URL

    def get_quick_search_url(self):
        """
        url for quick search
        :return:
        """
        return self.api_base_url + QRADAR_QUICK_SEARCH_URL

    def get_full_search_url(self):
        """
        Full search endpoint
        :return:
        """
        return self.api_base_url + QRADAR_FULL_SEARCH_URL

    def get_full_search_status_url(self, search_id):
        """
        Full search status endpoint
        :param search_id:
        :return:
        """
        return (self.api_base_url + QRADAR_FULL_SEARCH_URL +"/{}").format(str(search_id))

    def get_full_search_result_url(self, search_id, stage):
        """
        url for full search result
        :param search_id: search id
        :param stage: "stage1", "stage2", or "stage3"
        :return:
        """
        sid = str(search_id)
        url = (self.api_base_url + QRADAR_FULL_SEARCH_RESULT_URL).format(search_id=sid, stage=stage)
        return url

    def get_analysis_url(self, offense_id):
        """
        URL to start offense analysis
        :param offense_id:
        :return:
        """
        return (self.api_base_url + QRADAR_ANALYSIS_URL).format(offense_id=str(offense_id))

    def get_analysis_status_url(self, offense_id):
        """
        URL for the offense analysis status
        :param offense_id:
        :return:
        """
        return (self.api_base_url + QRADAR_ANALYSIS_STATUS_URL).format(offense_id=str(offense_id))

    def get_analysis_result_url(self, offense_id, stage):
        """
        URL for stix result of an offense analysis
        :param offense_id:
        :param stage: "stage1", "stage2", or "stage3"
        :return:
        """
        return (self.api_base_url + QRADAR_ANALYSIS_RESULT_URL).format(offense_id=str(offense_id),
                                                                       stage=stage)

    def get_cafile(self):
        """
        False to skip validating https cert
        :return:
        """
        return self.cafile

    def reset_session(self):
        #
        # remove the "old" CSRF token
        #
        if "X-XSRF-TOKEN" in self.session.headers:
            del self.session.headers["X-XSRF-TOKEN"]

    def update_session(self, cookies):
        """
        Extract the CSRF token from the cookies and store it in the
        session headers
        :param cookies:
        :return:
        """
        self.session.headers["X-XSRF-TOKEN"] = cookies["XSRF-TOKEN"]
        self.xsrf_token = cookies["XSRF-TOKEN"]

    def get_session(self):
        """
        Get the session
        :return:
        """
        return self.session

    def get_offense_insights_url(self, offense_id):
        """
        URL for offense insights
        :param offense_id: offense id
        :return:
        """
        url = self.api_base_url + QRADAR_OFFENSE_INSIGHTS_URL.format(offense_id=offense_id)
        return url

