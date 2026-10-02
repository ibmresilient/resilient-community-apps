# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use


class GuardiumInsightsApiError(Exception):
    def __init__(self, msg):
        super(GuardiumInsightsApiError, self).__init__(msg)
        self.msg = msg

    def __str__(self):
        return repr(self.msg)


class TableDataRestCallError(Exception):
    def __init__(self, msg):
        self.Error_msg = msg

    def __str__(self):
        return repr(self.Error_msg)


class ResilientRestfulServiceError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return repr(self.msg)
