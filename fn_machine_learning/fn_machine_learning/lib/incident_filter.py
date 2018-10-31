# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
#
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
#
import logging
from datetime import datetime


class IncidentFilter(object):
    """
    Filter incidents.
        1. Time filter: time_start and time_end
        2. Others not implemented yet
    """
    TIME_FORMAT = "%Y-%m-%d"

    def __init__(self, time_start=None, time_end=None, in_log=None):
        self.time_start = time_start
        self.time_end = time_end
        self.log = in_log if in_log is not None else logging.getLogger(__name__)

    def set_time(self, time_start=None, time_end=None):
        """
        Set time_start and time_end for time filter
        :param time_start:
        :param time_end:
        :return:
        """
        self.time_start = time_start
        self.time_end = time_end

    def check_time_filter(self, incident):
        """
        Check if the input incident shall be included in the samples or not.
        :param incident: input incident
        :return: True for including it.
        """
        #
        #   Not a security feature. Ok to default it to True
        #
        shall_include = True

        #
        # Filter according to create_date
        #
        create_date = datetime.fromtimestamp(incident["create_date"] / 1000.)
        if self.time_start is not None:
            try:
                t_start = datetime.strptime(self.time_start, IncidentFilter.TIME_FORMAT)
                if t_start is not None and create_date < t_start:
                    shall_include = False
            except ValueError as e:
                t_start = None
                self.log.error("Exception in casting {} into datetime: {}".format(self.time_start, e))

        if self.time_end is not None:
            try:
                t_end = datetime.strptime(self.time_end, IncidentFilter.TIME_FORMAT)
                if t_end is not None and create_date > t_end:
                    shall_include = False
            except ValueError as e:
                t_end = None
                self.log.error("Exception in casting {} into datetime: {}".format(self.time_end, e))

        return shall_include

    def shall_include_incident(self, incident):
        """
        Check if the input incident shall be included in the samples or not.
        :param incident: input incident
        :return: True for including it.
        """
        include_time = self.check_time_filter(incident)

        #
        #   Other filters in the future
        #
        return include_time


