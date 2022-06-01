# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use, line-too-long

"""This module contains utility/context classes useful in the processing of feeds."""

import abc


class FeedContext(object):  # pylint: disable=too-few-public-methods
    """
    This is a simple data structure used to hold things needed by the
    different feed destination classes.
    """
    def __init__(self, type_info, inc_id, rest_client_helper, is_deleted):
        self.type_info = type_info
        self.rest_client_helper = rest_client_helper
        self.inc_id = inc_id
        self.is_deleted = is_deleted


class FeedDestinationBase(object):  # pylint: disable=too-few-public-methods
    """Base class for all feeds."""
    def __init__(self):
        pass

    @abc.abstractmethod
    def send_data(self, context, payload):
        """
        Subclasses have to implement this.  It's where all the work
        happens (it's where the data gets written
        to the destination.
        """
        raise NotImplementedError
