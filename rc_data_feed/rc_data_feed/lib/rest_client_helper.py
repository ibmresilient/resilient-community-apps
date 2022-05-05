# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use, line-too-long

"""Feed component implementation."""

import logging
from threading import Lock
lock = Lock()

LOG = logging.getLogger(__name__)

class RestClientHelper:
    """
    This wrapper to rest_client is in place to support retry logic for the resilient API when the token has protentially
    expired. It's possible that other errors will be trapped, in which case regenerating the session identifier will
    have no adjerse effect.
    """
    def __init__(self, rest_client):
        self.rest_client = rest_client
        self._get_connection()

    def post(self, url, query):
        """
        perform the resilient post, catching exceptions that can be caused when the token expires
        """
        try:
            return self.inst_rest_client.post(url, query)
        except Exception as err:  # catch issues such as the token expiring
            LOG.warning("Reattempting connection to resilient %s", err)
            self._get_connection()
            return self.inst_rest_client.post(url, query)


    def search(self, search_input_dto):
        """
        perform the resilient search, catching exceptions that can be caused when the token expires
        """
        try:
            return self.inst_rest_client.search(search_input_dto)
        except Exception as err:  # catch issues such as the token expiring
            LOG.warning("Reattempting connection to resilient %s", err)
            self._get_connection()
            return self.inst_rest_client.search(search_input_dto)


    def get(self, query):
        """
        perform the resilient get, catching exceptions that can be caused when the token expires
        """
        try:
            return self.inst_rest_client.get(query)
        except Exception as err:  # catch issues such as the token expiring
            LOG.warning("Reattempting connection to resilient %s", err)
            self._get_connection()
            return self.inst_rest_client.get(query)


    def get_inst_rest_client(self):
        return self.inst_rest_client


    def _get_connection(self):
        lock.acquire()
        try:
            self.inst_rest_client = self.rest_client()
        finally:
            lock.release()
