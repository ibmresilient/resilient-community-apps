# -*- coding: utf-8 -*-
#
# (c) Copyright IBM Corp. 2018. All Rights Reserved.
#
# Template Method Design Pattern for a search-and-wait-for-result command
#
# This file can be reused for composite commands.
#
import time
import logging
LOG = logging.getLogger(__name__)


class SearchTimeout(Exception):
    """ Query failed to complete in time specified """
    def __init__(self, search_id, search_status):
        fail_msg = "Query [{}] timed out. Final Status was [{}]".format(search_id, search_status)
        super(SearchTimeout, self).__init__(fail_msg)
        self.search_status = search_status


class SearchJobFailure(Exception):
    """ Search job creation failure"""
    def __init__(self, query):
        fail_msg = "Failed to create search job for query [{}] ".format(query)
        super(SearchJobFailure, self).__init__(fail_msg)


class SearchFailure(Exception):
    """ Search failed to execute """
    def __init__(self, search_id, search_status):
        fail_msg = "Query [{}] failed with status [{}]".format(search_id, search_status)
        super(SearchFailure, self).__init__(fail_msg)
        self.search_status = search_status


class SearchWaitCommand(object):
    # Constants
    SEARCH_STATUS_COMPLETED = 0
    SEARCH_STATUS_ERROR_STOP = 1
    SEARCH_STATUS_WAITING = 2
    SEARCH_STATUS_UNKNOWN_CONTINUE = 3

    def __init__(self, timeout=600, period=5):
        """

        :param timeout: Time out in secs
        :param polling: polling period in secs
        """
        self.search_timeout = timeout
        self.polling_period = period

    def get_search_id(self, query):
        """
        Subclass shall overrides this to implement the search to get a search/job id
        :param query:
        :return: return None if failed
        """
        return ""

    def check_status(self, search_id):
        """
        Override this to provide status of the search job
        :param search_id:
        :return: return one of the search status
        """
        return self.SEARCH_STATUS_ERROR_STOP

    def get_search_result(self, search_id):
        """
        Override this to get the search result
        :param search_id:
        :return:
        """
        return {}

    def perform_search(self, query):
        """
        This is the skeleton for search and wait command
        :param query: query string to perform search
        :return:
        """
        search_id = self.get_search_id(query)

        if search_id:
            # store the start time
            start_time = time.time()
            done = False

            while not done:
                status = self.check_status(search_id)
                if status == self.SEARCH_STATUS_COMPLETED:
                    done = True
                elif status == self.SEARCH_STATUS_ERROR_STOP:
                    raise SearchFailure(search_id, status)
                elif status == self.SEARCH_STATUS_WAITING:
                    done = False
                elif status == self.SEARCH_STATUS_UNKNOWN_CONTINUE:
                    LOG.debug("Status check unknown, continue")
                    done = False

                if not done:
                    # time_out is default to 10 minutes. If customer overrides it to 0, it
                    # will never timeout
                    if self.search_timeout != 0:
                        if time.time() - start_time > self.search_timeout:
                            raise SearchTimeout(search_id, status)
                    # polling_interval is defaulted to 5 sec
                    time.sleep(self.polling_period)
        else:
            LOG.error("search_id is None")
            raise SearchJobFailure(query)

        result = self.get_search_result(search_id)

        return result
