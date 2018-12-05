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
    """ Exception in fetching offense insights"""
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

        :param stage: "stage1", "stage2", or "stage3". This is the stage of result user wants
        :return:
        """
        self.full_search_stage = stage

    def set_full_search_timeout(self, timeout):
        """
        Set the time out value for a full search
        :param timeout: Time out in seconds
        :return:
        """
        self.full_search_timeout = timeout

    def set_full_search_period(self, period):
        """
        Set the period for checking status
        :param period: period in seconds
        :return:
        """
        self.full_search_period = period

    def get_csrf_token(self):
        """
        The call to the "about" endpoint serves as the way to fetch a CSRF token
        The CSRF token will be added to the session header
        :return: void
        """
        url = self.http_info.get_about_url()

        try:
            session = self.http_info.get_session()
            response = session.get(url=url,
                                   verify=self.http_info.get_cafile())
            #
            # The CSRF token is in the cookie. Add it to the
            # session header
            #
            if response.status_code == 200:
                self.http_info.update_session(session.cookies.get_dict())
            else:
                self.log.error("the about endpoint returns status {}".format(str(response.status_code)))
                raise CsrfTokenError(url, "Status {}".format(str(response.status_code)))
        except Exception as e:
            self.log.error("Get token failed with exception:")
            self.log.error(str(e))
            raise CsrfTokenError(url, e.message)

    def full_search(self, search_value):
        """
        Full search for an indicator
        :param search_value: indicator value. For example "user:jsmith"
        :return: stix2 in json
        """
        #
        # Make sure we have the CSRF token
        #
        if not self.http_info.xsrf_token:
            self.get_csrf_token()

        full_search = QRadarFullSearch(self.http_info,
                                       self.log,
                                       self.full_search_stage,
                                       self.full_search_timeout,
                                       self.full_search_period)

        stix_json = full_search.perform_search(search_value)

        return stix_json

    def full_search_by_id(self, search_id):
        """
        Get full search result for a search_id
        :param search_id: search id
        :return: stix2 in json
        """
        if not self.http_info.xsrf_token:
            self.get_csrf_token()

        full_search = QRadarFullSearch(self.http_info,
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
        :return: search result in json (Not stix2)
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
            if response.status_code != 200:
                error_msg = "Quick search using {} returns {}".format(url, str(response))
                self.log.error(error_msg)
                raise QuickSearchError(url, error_msg)

        except Exception as e:
            self.log.error("Quick search failed with exception:")
            self.log.error(str(e))
            raise QuickSearchError(url, e.message)

        return response.json()

    def offense_insights(self, offense_id):
        """
        Get the insights for an offense
        :param offense_id: QRadar offense id
        :return: summary in json (Not stix2)
        """
        if not self.http_info.xsrf_token:
            self.get_csrf_token()

        url = self.http_info.get_offense_insights_url(offense_id)
        session = self.http_info.get_session()

        try:
            response = session.get(url=url,
                                   data=None,
                                   verify=self.http_info.get_cafile())
            if response.status_code != 200:
                error_msg = "Offense insights using {} returns error {}".format(url, str(response))
                self.log.error(error_msg)
                raise OffenseInsightsError(url, error_msg)
        except Exception as e:
            self.log.error("Offense insights failed with exception:")
            self.log.error(str(e))
            raise OffenseInsightsError(url, e.message)

        return response.json()

    def offense_analysis(self, offense_id,
                         restart_if_existed=True, return_stage="stage3",
                         timeout=1200, period=5):
        """
        Do an analysis for a given offense
        :param offense_id: id for offense
        :param restart_if_existed: QRadar Advisor keeps the analysis result. Set to False
                if just take the existing result. True to force restart
        :param return_stage: "stage1", "stage2", or "stage3"
        :param timeout: timeout for waiting for analysis result
        :param period: period for checking status
        :return: stix2 in json
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


class QRadarFullSearch(SearchWaitCommand):
    """
    Subclass of the SearchWaitCommand. This is for doing a full search of an indicator
    """
    SEARCH_RETURN_DONE_STAGE3 = "DONE_STAGE3"
    SEARCH_RETURN_DONE = "DONE"
    SEARCH_RETURN_NO_OBSERVABLES = "NO_OBSERVABLES"
    SEARCH_RETURN_ERROR = "ERROR"
    SEARCH_RETURN_ERROR_AUTH = "ERROR_AUTH"

    def __init__(self, http_info, log, return_stage="stage3", timeout=1200, period=5):
        self.http_info = http_info
        self.log = log
        self.return_stage = return_stage
        self.period = period
        self.stage3_available = False
        super(QRadarFullSearch, self).__init__(timeout, period)

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

            if response.status_code != 200:
                error_msg = "Get search id using {} failed: {}".format(url, str(response))
                self.log.error(error_msg)
                raise SearchJobFailure(error_msg)

            ret_json = response.json()
            #
            # There should be only one search id since we did only one here
            #
            if len(ret_json["search_ids"]) > 1:
                #
                # if for any reason get search id returns more than one, we log an error
                # and still use the first one
                self.log.error("Get search id returns {}".format(str(ret_json)))
            search_id = ret_json["search_ids"][0]
        except Exception as e:
            self.log.error("Failed to get search id for full search with exception:")
            self.log.error(e.message)
            raise SearchJobFailure(search_value)

        return search_id

    def check_status(self, search_id):
        """
        Check the status of a full search given the search id
        :param search_id: search id for the full search
        :return: search status defined in SearchWaitCommand super class
        """
        status = self.SEARCH_STATUS_WAITING

        url = self.http_info.get_full_search_status_url(search_id)
        session = self.http_info.get_session()

        try:
            response = session.get(url=url,
                                   verify=self.http_info.get_cafile())

            ret_json = response.json()

            if response.status_code == 200:
                search_status = ret_json["search_status"]
                self.log.info("Search {} status: {}".format(str(search_id), search_status))

                if search_status == self.SEARCH_RETURN_DONE:
                    status = self.SEARCH_STATUS_COMPLETED
                    #
                    # stage3 data is not available? Need to fall back to stage2.
                    #
                    self.stage3_available = False
                elif search_status == self.SEARCH_RETURN_DONE_STAGE3:
                    status = self.SEARCH_STATUS_COMPLETED
                    self.stage3_available = True
                elif search_status == self.SEARCH_RETURN_NO_OBSERVABLES:
                    status = self.SEARCH_STATUS_COMPLETED
                    self.stage3_available = False
                elif search_status == self.SEARCH_RETURN_ERROR:
                    self.log.error("Search {} returns ERROR.".format(str(search_id)))
                    status = self.SEARCH_STATUS_ERROR_STOP
                elif search_status == self.SEARCH_RETURN_ERROR_AUTH:
                    self.log.error("Search {} returns ERROR_AUTH.".format(str(search_id)))
                    status = self.SEARCH_STATUS_ERROR_STOP
            elif response.status_code == 404:
                # The full search does not exist
                self.log.error("Search {} does not exist.".format(str(search_id)))
                status = self.SEARCH_STATUS_ERROR_STOP
        except Exception as e:
            self.log.error("Failed to get search status. Stop waiting for the result.")
            self.log.error(e.message)
            status = self.SEARCH_STATUS_ERROR_STOP
            raise SearchFailure(str(search_id), str(status))

        return status

    def get_search_result(self, search_id):
        """
        Retrieve the full search result
        :param search_id: search id
        :return: stix2 in json
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
            raise SearchFailure(str(search_id), e.message)

        if response.status_code == 200:
            stix_json = response.json()
        elif response.status_code == 404:
            self.log.error("Search result for {} does not exist.".format(str(search_id)))
            raise SearchFailure(str(search_id), "Search result do not exist.")
        else:
            self.log.error("Search result for {} returns {}".format(str(search_id), str(response)))
            raise SearchFailure(str(search_id), str(response))

        return stix_json


class QRadarOffenseAnalysis(SearchWaitCommand):
    """
    QRadar offense analysis, a search and wait command
    """

    ANALYSIS_DONE_STATUS = "DONE"
    ANALYSIS_DONE_STAGE3 = "DONE_STAGE3"
    ANALYSIS_NO_OBSERVABLES = "NO_OBSERVABLES"
    ANALYSIS_ERROR = "ERROR"
    ANALYSIS_ERROR_AUTH = "ERROR_AUTH"

    def __init__(self, http_info, log, return_stage="stage3", timeout=1200, period=5):
        self.http_info = http_info
        self.log = log
        self.return_stage = return_stage
        self.period = period
        self.stage3_available = False
        super(QRadarOffenseAnalysis, self).__init__(timeout, period)

    def get_search_id(self, offense_id):
        """
        Start the analysis for this given offense
        :param offense_id: offense id
        :return: offense id
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
        :param search_id: same as the offense id
        :return: status defined in the SearchWaitCommand super class
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
                    self.stage3_available = False
                elif ret_json.get("status", "") == self.ANALYSIS_DONE_STAGE3:
                    status = self.SEARCH_STATUS_COMPLETED
                    self.stage3_available = True
                elif ret_status == self.ANALYSIS_NO_OBSERVABLES:
                    status = self.SEARCH_STATUS_COMPLETED
                    self.stage3_available = False
                elif ret_status == self.ANALYSIS_ERROR or ret_status == self.ANALYSIS_ERROR_AUTH:
                    status = self.SEARCH_STATUS_ERROR_STOP
                    self.stage3_available = False

            elif response.status_code == 403:
                #
                # Offense does not exist or not permission
                #
                self.log.error("Offense {} does not exist or no permission to read".format(str(offense_id)))
                status = self.SEARCH_STATUS_ERROR_STOP
        except Exception as e:
            self.log.error("Offense {} status exception: {}".format(str(offense_id), e.message))
            raise SearchFailure(str(search_id), e.message)

        return status

    def get_search_result(self, search_id):
        """
        Retrieve the analysis result
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

        except Exception as e:
            self.log.error("Exception in getting analysis result for {}:{}".format(str(offense_id), e.message))
            raise SearchFailure(search_id, e.message)

        if response.status_code == 200:
            self.log.info("Get analysis result for offense {}".format(str(offense_id)))
            stix_json = response.json()
        elif response.status_code == 403:
            self.log.error("Offense {} does not exist or no permission to read".format(str(offense_id)))
            raise SearchFailure(search_id, str(response))
        elif response.status_code == 404:
            self.log.error("Offense {} analysis does not exists".format(str(offense_id)))
            raise SearchFailure(search_id, str(response))
        else:
            #
            # There shall not be any other result according to /api/docs. But just in case
            #
            self.log.error("Offense {} analysis failed: {}".format(str(offense_id), str(response)))
            raise SearchFailure(search_id, str(response))

        return stix_json
