# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

import requests
from qradar_http_info import HttpInfo
from search_wait_command import SearchWaitCommand
from search_wait_command import SearchJobFailure
from search_wait_command import SearchFailure
import json
import time

class CsrfTokenError(Exception):
    """ Exception in getting csrf token"""
    def __init__(self, url, message):
        fail_msg = "Requests to url [{}] throws exception. Error [{}]".format(url, message)
        super(CsrfTokenError, self).__init__(fail_msg)


class QuickSearchError(Exception):
    """ Exception in quick search"""
    def __init__(self, url, message):
        fail_msg = "Quick search using [{}] throws exception. Error [{}]".format(url, message)
        super(QuickSearchError, self).__init__(fail_msg)


class OffenseInsightsError(Exception):
    """ Exceptipn in fetching offense insights"""
    def __init__(self, url, message):
        fail_msg = "Offense insights using [{}] throws exception. Error [{}]".format(url, message)
        super(OffenseInsightsError, self).__init__(fail_msg)


class XFECredentialError(Exception):
    """
    The token provided in the app.config file has no enough permission?
    """
    def __init__(self, message):
        fail_msg = "Unauthorized XFE credentials used for the following: {}".format(message)
        super(XFECredentialError, self).__init__(fail_msg)


class QRadarAdvisorClient(object):

    def __init__(self, qradar_host, advisor_app_id, qradar_token, cafile, log):
        self.http_info = HttpInfo(qradar_host, advisor_app_id, qradar_token, cafile, log)
        self.full_search_stage = "stage3"
        self.full_search_timeout = 1200
        self.full_search_period = 5
        self.log = log

    def set_full_search_stage(self, stage):
        """

        :param stage:
        :return:
        """
        self.full_search_stage = stage

    def set_full_search_timeout(self, timeout):
        """

        :param timeout:
        :return:
        """
        self.full_search_timeout = timeout

    def set_full_search_period(self, period):
        """

        :param period:
        :return:
        """
        self.full_search_period = period

    def get_csrf_token(self):
        """
        The call to the "about" endpoint serves the way to fetch a CSRF token
        The CSRF token will be added to the session header
        :return: void
        """
        url = self.http_info.get_about_url()

        try:
            session = self.http_info.get_session()
            #
            # If the connection drops, and we
            #

            response = session.get(url=url,
                                   verify=self.http_info.get_cafile())
            #
            # The CSRF token is in the cookie. Add it to the
            # session header
            #
            self.http_info.update_session(session.cookies.get_dict())

        except Exception as e:
            self.log.error("Get token failed with exception:")
            self.log.error(str(e))
            raise CsrfTokenError(url, e.message)

    def full_search(self, search_value):
        """
        Full search for an indicator
        :param search_value: indicator value. For example "user:jsmith"
        :return: stix in json
        """
        #
        # Make sure we have the CSRF token
        #
        if not self.http_info.xsrf_token:
            self.get_csrf_token()

        full_search = QradarFullSearch(self.http_info,
                                       self.log,
                                       self.full_search_stage,
                                       self.full_search_timeout,
                                       self.full_search_period)

        stix_json = full_search.perform_search(search_value)

        return stix_json

    def full_search_by_id(self, search_id):
        """
        Get full search result for a search_id
        :param search_id:
        :return:
        """
        if not self.http_info.xsrf_token:
            self.get_csrf_token()

        full_search = QradarFullSearch(self.http_info,
                                       self.log,
                                       self.full_search_stage,
                                       self.full_search_timeout,
                                       self.full_search_period)

        stix_json = full_search.get_search_result(search_id)

        return stix_json

    def quick_search(self, search_value):
        """
        Do a quick search for an indicator
        :param search_value: indicator value. For example "8.8.8.8"
        :return: search result in json
        """
        if not self.http_info.xsrf_token:
            self.get_csrf_token()

        url = self.http_info.get_quick_search_url()

        data_dict = {"indicator": search_value}
        data = json.dumps(data_dict)
        response = None
        try:
            session = self.http_info.get_session()
            response = session.post(url=url,
                                    data=data,
                                    verify=self.http_info.get_cafile())
        except Exception as e:
            self.log.error("Quick search failed with exception:")
            self.log.error(str(e))
            raise QuickSearchError(url, e.message)

        return response.json()

    def offense_insights(self, offense_id):
        """
        Get the insights for an offense
        :param offense_id: QRadar offense id
        :return:
        """
        if not self.http_info.xsrf_token:
            self.get_csrf_token()

        url = self.http_info.get_offense_insigths_url(offense_id)
        session = self.http_info.get_session()

        try:
            response = session.get(url=url,
                                   data=None,
                                   verify=self.http_info.get_cafile())
        except Exception as e:
            self.log.error("Offense insights failed with exception:")
            self.log.error(str(e))
            raise OffenseInsightsError(url, e.message)

        return response.json()

    def offense_analysis(self, offense_id,
                         restart_if_existed=True, return_stage="stage3",
                         timeout=1200, period=5):
        """

        :param offense_id: id for offense
        :param restart_if_existed: QRadar Advisor keeps the analysis result. Set to False
                if just take the existing result. True to force restart
        :param return_stage: "stage1", "stage2", or "stage3"
        :param timeout: timeout for waiting for analysis result
        :param period: period for checking status
        :return: stix in json
        """
        if not self.http_info.xsrf_token:
            self.get_csrf_token()
        offense_analysis = QRadarOffenseAnalysis(http_info=self.http_info,
                                                 log=self.log,
                                                 return_stage=return_stage,
                                                 timeout=timeout,
                                                 period=period)

        stix_json = None
        if not restart_if_existed:
            # check if result already there
            stix_json = offense_analysis.get_search_result(offense_id)

        if not stix_json:
            # start the analysis
            stix_json = offense_analysis.perform_search(offense_id)

        return stix_json


class QradarFullSearch(SearchWaitCommand):
    """
    Subclass of the SearchWaitCommand.
    """
    SEARCH_RETURN_DONE_STAGE3 = "DONE_STAGE3"
    SEARCH_RETURN_DONE = "DONE"

    def __init__(self, http_info, log, return_stage="stage3", timeout=1200, period=5):
        self.http_info = http_info
        self.log = log
        self.return_stage = return_stage
        self.period = period
        self.stage3_available = False
        super(QradarFullSearch, self).__init__(timeout, period)

    def get_search_id(self, search_value):
        """
        Start a full search of an indicator
        :param query: indicator value
        :return: search id
        """
        url = self.http_info.get_full_search_url()
        session = self.http_info.get_session()
        data_dict = {"indicator": search_value}
        data = json.dumps(data_dict)

        search_id = 0
        try:
            response = session.post(url=url,
                                    data=data,
                                    verify=self.http_info.get_cafile())
            ret_json = response.json()

            #
            # There should be only one search id since we did only one here
            #
            search_id = ret_json["search_ids"][0]
        except Exception as e:
            self.log.error("Failed to get search id for full search with exception:")
            self.log.error(e.message)
            raise SearchJobFailure(search_value)

        return search_id

    def check_status(self, search_id):
        """

        :param search_id:
        :return:
        """
        status = self.SEARCH_STATUS_WAITING

        url = self.http_info.get_full_search_status_url(search_id)
        session = self.http_info.get_session()

        try:
            response = session.get(url=url,
                                   verify=self.http_info.get_cafile())

            ret_json = response.json()
            search_status = ret_json["search_status"]
            self.log.info("Search {} status: {}".format(str(search_id), search_status))

            if response.status_code == 200:
                if search_status == self.SEARCH_RETURN_DONE:
                    status = self.SEARCH_STATUS_COMPLETED
                    #
                    # stage3 data is not available? Need to fall back to stage1?
                    #
                    self.stage3_available = False
                elif search_status == self.SEARCH_RETURN_DONE_STAGE3:
                    status = self.SEARCH_STATUS_COMPLETED
                    self.stage3_available = True
            elif response.status_code == 404:
                # The full search does not exist
                self.log.error("Search {} does not exist.".format(str(search_id)))
                status = self.SEARCH_STATUS_ERROR_STOP
        except Exception as e:
            self.log.error("Failed to get search status. Stop waiting for the result.")
            self.log.error(e.message)
            status = self.SEARCH_STATUS_ERROR_STOP
            raise SearchFailure(str(search_id), search_status)

        return status

    def get_search_result(self, search_id):
        """

        :param search_id:
        :return:
        """

        url = self.http_info.get_full_search_result_url(search_id, self.return_stage)
        if self.return_stage == "stage3":
            if self.stage3_available:
                #
                # user wants stage3 and stage3 is available
                #
                url = self.http_info.get_full_search_result_url(search_id, "stage3")
            else:
                #
                # user wants stage3, stage3 is not available. According to QRadar Advisor team,
                # stage2 is always available
                #
                url = self.http_info.get_full_search_result_url(search_id, "stage2")

        session = self.http_info.get_session()

        stix_json = None
        try:
            response = session.get(url=url,
                                   verify=self.http_info.get_cafile())
            self.log.info("Full search {} status {}".format(str(search_id), str(response)))
        except Exception as e:
            self.log.error("Failed to get full search result.")
            self.log.error(e.message)
            raise SearchFailure(str(search_id), str(response.status_code))

        if response.status_code == 200:
            stix_json = response.json()
        elif response.status_code == 404:
            raise SearchFailure(str(search_id), str(response.status_code))

        return stix_json


class QRadarOffenseAnalysis(SearchWaitCommand):
    """

    """

    ANALYSIS_DONE_STATUS = "DONE"
    ANALYSIS_DONE_STAGE3 = "DONE_STAGE3"

    def __init__(self, http_info, log, return_stage="stage3", timeout=1200, period=5):
        self.http_info = http_info
        self.log = log
        self.return_stage = return_stage
        self.period = period
        self.stage3_available = False
        super(QRadarOffenseAnalysis, self).__init__(timeout, period)

    def get_search_id(self, offense_id):
        """

        :param query:
        :return:
        """
        url = self.http_info.get_analysis_url(offense_id)
        session = self.http_info.get_session()

        search_id = 0
        try:
            response = session.post(url=url,
                                    verify=self.http_info.get_cafile())
        except Exception as e:
            self.log.error("Failed to start search for offense analysis with exception:")
            self.log.error(e.message)
            raise SearchJobFailure(str(offense_id))

        self.log.info("Start offense {} analysis returns {}".format(str(offense_id), str(response)))
        if response.status_code == 200:
            #
            # Good. The search id is just the offense_id
            #
            search_id = offense_id
        elif response.status_code == 401:
            self.log.error("Unauthorized XFE credentials. Offense analysis for {} failed".format(offense_id))
            raise XFECredentialError("Offense analysis for {}".format(str(offense_id)))
        elif response.status_code == 403:
            self.log.error("Offense {} does not exist or user does not have permission to view the offense.".format(offense_id))
            raise SearchJobFailure(str(offense_id))
        elif response.status_code == 429:
            self.log.error("Analysis limit has been met. Failed to start analysis for offense {}".format(str(offense_id)))
            raise SearchJobFailure(str(offense_id))
        else:
            self.log.error("Offense {} analysis failed to start.".format(str(offense_id)))
            raise SearchJobFailure(str(offense_id))

        return search_id

    def check_status(self, search_id):
        """
        Check the status of offense analysis
        :param search_id:
        :return:
        """
        status = self.SEARCH_STATUS_WAITING

        offense_id = search_id
        url = self.http_info.get_analysis_status_url(offense_id)
        session = self.http_info.get_session()

        try:
            response = session.get(url=url,
                                   verify=self.http_info.get_cafile())

            if response.status_code == 200:
                ret_json = response.json()
                ret_status = ret_json.get("status", "")
                self.log.info("Analysis status for offense {}: {}".format(str(offense_id), ret_status))

                if ret_json.get("status", "") == self.ANALYSIS_DONE_STATUS:
                    status = self.SEARCH_STATUS_COMPLETED
                    self.stag3_available = False
                elif ret_json.get("status", "") == self.ANALYSIS_DONE_STAGE3:
                    status = self.SEARCH_STATUS_COMPLETED
                    self.stag3_available = True
            elif response.status_code == 403:
                #
                # Offense does not exist or not permission
                #
                self.log.error("Offense {} does not exist or no permission to read".formet(str(offense_id)))
                status = self.SEARCH_STATUS_ERROR_STOP
        except Exception as e:
            self.log.error("Offense {} status exception: {}".format(str(offense_id), e.message))
            raise SearchFailure(str(search_id), e.message)

        return status

    def get_search_result(self, search_id):
        """

        :param search_id: same as offense_id
        :return:
        """
        url = self.http_info.get_analysis_result_url(search_id, self.return_stage)
        if self.return_stage == "stage3":
            if self.stage3_available:
                #
                # user wants stage3 and stage3 is available
                #
                url = self.http_info.get_analysis_result_url(search_id, "stage3")
            else:
                #
                # user wants stage3, stage3 is not available. According to QRadar Advisor team,
                # stage2 is always available
                #
                url = self.http_info.get_analysis_result_url(search_id, "stage2")

        offense_id = search_id
        session = self.http_info.get_session()

        stix_json = None
        try:
            response = session.get(url=url,
                                   verify=self.http_info.get_cafile())

            if response.status_code == 200:
                self.log.info("Get analysis result for offense {}".format(str(offense_id)))
                stix_json = response.json()
            elif response.status_code == 403:
                self.log.error("Offense {} does not exist or no permission to read".format(str(offense_id)))
            elif response.status_code == 404:
                self.log.error("Offense {} analysis does not exists".format((str(offense_id))))
        except Exception as e:
            self.log.error("Exception in getting analysis result for {}:{}".format(str(offense_id), e.message))

        return stix_json