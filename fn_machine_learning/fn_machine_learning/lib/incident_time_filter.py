# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
#
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
#
"""
    IncidentTimeFilter
    ------------------
    Filter incidents using time_start and time_end.

    This is a subclass of IncidentFilter
"""
from fn_machine_learning.lib.incident_filter import IncidentFilter
from datetime import datetime


class IncidentTimeFilter(IncidentFilter):
    #
    #   Format constant. This is the format we expect for time_start and time_end from app.config
    #
    TIME_FORMAT = "%Y-%m-%d"

    def __init__(self,
                 time_start=None,
                 time_end=None,
                 next_filter=None,
                 time_field="create_date",
                 in_log=None):
        """

        :param time_start:      Start time for filter
        :param time_end:        End time for filter
        :param next_filter:     Next filter (if any) in the filter chain
        :param time_field:      Time field of incident used to filter.
                                It can be "create_date", "discovered_date", "inc_start",
                                "start_date", or "end_date"
        :param in_log:          Log
        """
        self.time_start = time_start
        self.time_end = time_end
        self.time_field = time_field

        IncidentFilter.__init__(self,
                                next_filter=next_filter,
                                in_log=in_log)

    def set_time(self, time_start=None, time_end=None):
        """
        Set time_start and time_end for time filter

        :param time_start:      Start time for time filter
        :param time_end:        End time for time filter
        :return:                N/A
        """
        self.time_start = time_start
        self.time_end = time_end

    def filter_implementation(self, incident):
        """
        This is the template method to override.
        Use a time filter to filter incident

        :param incident:        Incident to check
        :return:                True to include, False to exclude
        """
        #
        #   Not a security feature. Ok to default it to True
        #
        shall_include = True

        #
        # Filter according to create_date
        #
        try:
            check_date = datetime.fromtimestamp(incident[self.time_field] / 1000.)
            if self.time_start is not None:
                try:
                    t_start = datetime.strptime(self.time_start, IncidentTimeFilter.TIME_FORMAT)
                    if t_start is not None and check_date < t_start:
                        shall_include = False
                except ValueError as e:
                    self.log.error("Exception in casting {} into datetime: {}".format(self.time_start, e))

            if self.time_end is not None:
                try:
                    t_end = datetime.strptime(self.time_end, IncidentTimeFilter.TIME_FORMAT)
                    if t_end is not None and check_date > t_end:
                        shall_include = False
                except ValueError as e:
                    self.log.error("Exception in casting {} into datetime: {}".format(self.time_end, e))

        except KeyError:
            shall_include = True
            self.log.error("{} is not found in incident".format(self.time_field))

        return shall_include
