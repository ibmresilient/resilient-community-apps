# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
#
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
#
"""
    IncidentFilter
    --------------
    Filter for incidents.

    Filters can be chained, so the Chain of Command design pattern is a good fit

    This is a superclass for concrete filters. It takes care of how to navigate to
    the next filter in the chain, so subclasses don't need to worry about it.
"""
import logging


class IncidentFilter(object):
    def __init__(self, next_filter=None, in_log=None):
        """
        Constructor.
        :param next_filter:     The next filter in the chain
        :param in_log:          Log
        """
        self.next_filter = next_filter
        self.log = in_log if in_log else logging.getLogger(__name__)

    def filter_implementation(self, incident):
        """
        Subclass needs to implement/override this.

        :param incident:        Input incident
        :return:                True to include
        """
        return True

    def shall_include_incident(self, incident):
        """
        A user just needs to call this. Template method design pattern is used here.
        This method will first call the filter_implementation that a subclass implements.
        Then it will take care of navigating to the next filter in the chain, so the
        subclass does not need to worry about it.

        All a subclass needs to do is to implement the filter_implement method.

        :param incident:        The incident to check
        :return:                True to include, false to exclude the input incident
        """
        shall_include_incident = self.filter_implementation(incident)

        if shall_include_incident:
            #
            #   Only need to check the next filter in the chain if we shall include
            #
            if self.next_filter is not None:
                shall_include_incident = self.next_filter.shall_include_incident(incident)

        return shall_include_incident

