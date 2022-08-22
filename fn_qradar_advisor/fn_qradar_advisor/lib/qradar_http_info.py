# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
import requests
import base64
import sys
if sys.version_info.major < 3:
    from urllib import quote 
else:
    # Python 3.x
    from urllib.parse import quote
from resilient_lib import RequestsCommon

QRADAR_PLUGIN_API_URL = "{host}/console/plugins/{app_id}/app_proxy/api"
QRADAR_OFFENSE_INSIGHTS_URL = "/investigations/offense/{offense_id}/insights"
QRADAR_INVESTIGATIONS = "/investigations"
QRADAR_QUICK_SEARCH_URL = "/investigations/search/quick"
QRADAR_FULL_SEARCH_URL = "/investigations/search/full"
QRADAR_FULL_SEARCH_RESULT_URL = "/investigations/search/full/{search_id}/stix/{stage}"
QRADAR_ABOUT_URL="/about"
QRADAR_ANALYSIS_URL = "/investigations/offense/{offense_id}/analysis"
QRADAR_ANALYSIS_STATUS_URL = "/investigations/offense/{offense_id}/analysis/status"
QRADAR_ANALYSIS_RESULT_URL = "/investigations/offense/{offense_id}/analysis/{stage}/stix"
QRADAR_ANALYTICS_RULE_BY_NAME_URL = "{host}/api/analytics/rules?fields=name%2C%20id%2C%20identifier&filter=name%20%3D%20%22{rule_name}%22"
QRADAR_GUI_APP_FRAMEWORK_APPLICATIONS_URL = "{host}/api/gui_app_framework/applications"

QRADAR_UCM_BASE_URL = "{host}/console/plugins/app_proxy:UseCaseManager_Service"
QRADAR_UCM_MAPPINGS_TACTICS = "/api/mappings/tactics"
QRADAR_UCM_MITRE_MITRE_COVERAGE = "/api/mitre/mitre_coverage/{rule_id}"

QRADAR_CFMA_MAPPINGS = "/mappings"
QRADAR_CFMA_TUNING="/config/tuning"

class HttpInfo(object):
    def __init__(self, qradar_host, advisor_app_id, qradar_token, cafile, log, opts=None, function_opts=None):
        if qradar_host.startswith("http"):
            # User wants to specify http or https
            self.host = qradar_host
        else:
            # Always assume https
            self.host = "https://" + qradar_host

        self.cafile = cafile
        self.app_id = advisor_app_id
        self.token = qradar_token
        self.xsrf_token = None
        self.log = log
        self.api_base_url = QRADAR_PLUGIN_API_URL.format(host=self.host, app_id=self.app_id)
        self.ucm_base_url = QRADAR_UCM_BASE_URL.format(host=self.host)

        self.session = requests.session()
        self.session.headers["Accept"] = "application/json"
        self.session.headers["Content-Type"] = "application/json"
        self.session.headers["SEC"] = self.token
        self.session.cookies["SEC"] = self.token
        self.session.proxies = RequestsCommon(opts, function_opts).get_proxies()

    def get_all_mappings(self):
        """
        Get the url to api/mappings
        :return:
        """
        return self.api_base_url + QRADAR_CFMA_MAPPINGS

    def get_tuning_url(self):
        """
        Get the url tp api/config/tuning endpoint
        :return:
        """
        return self.api_base_url + QRADAR_CFMA_TUNING

    def get_about_url(self):
        """
        Get the url to the api/about endpoint
        :return:
        """
        return self.api_base_url + QRADAR_ABOUT_URL

    def get_investigations_url(self):
        """
        Get the url to the api/investigations endpoint
        :return:
        """
        return self.api_base_url + QRADAR_INVESTIGATIONS

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

        if "X-TACTICS-XSRF-TOKEN" in self.session.headers:
            del self.session.headers["X-TACTICS-XSRF-TOKEN"]

    def update_session(self, cookies):
        """
        Extract the CSRF token from the cookies and store it in the
        session headers
        :param cookies:
        :return:
        """
        if "XSRF-TOKEN" in cookies:
            self.session.headers["X-XSRF-TOKEN"] = cookies["XSRF-TOKEN"]
            self.xsrf_token = cookies["XSRF-TOKEN"]

        if "TACTICS-XSRF-TOKEN" in cookies:
            self.update_session_tactics(cookies)

    def update_session_tactics(self, cookies):
        self.session.headers["X-TACTICS-XSRF-TOKEN"] = cookies["TACTICS-XSRF-TOKEN"]
        self.xsrf_token = cookies["TACTICS-XSRF-TOKEN"]

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

    def get_qradar_apps_url(self):
        """
        URL used to get the list of apps in QRadar instance.
        """
        return QRADAR_GUI_APP_FRAMEWORK_APPLICATIONS_URL.format(host=self.qradar_host)

    def get_qradar_get_rule_url(self, qradar_rule_name):
        """
        URL used to get the list of apps in QRadar instance.
        """
        url_encoded_rule_name = quote(qradar_rule_name)
        return QRADAR_ANALYTICS_RULE_BY_NAME_URL.format(host=self.host, rule_name=url_encoded_rule_name)

    def get_qradar_ucm_get_tactics_url(self):
        """
        URL used to get the list of apps in QRadar UCM MITRE ATT&CK tactics and techniques.
        """
        return self.ucm_base_url + QRADAR_UCM_MAPPINGS_TACTICS

    def get_qradar_ucm_get_mitre_mitre_coverage_url(self, rule_id):
        """
        URL used to get all rule and child mappings in QRadar UCM instances.
        """
        return self.ucm_base_url + QRADAR_UCM_MITRE_MITRE_COVERAGE.format(rule_id=rule_id)