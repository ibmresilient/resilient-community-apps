# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2021. All Rights Reserved.
class RequestError(Exception):
    """ Request error"""
    def __init__(self, url, message):
        fail_msg = "Request to url [{}] throws exception. Error [{}]".format(url, message)
        super(RequestError, self).__init__(fail_msg)

class DeleteError(Exception):
    """ Request error"""
    def __init__(self, url, message):
        fail_msg = "Delete request to url [{}] throws exception. Error [{}]".format(url, message)
        super(DeleteError, self).__init__(fail_msg)

class LabelError(Exception):
    def __init__(self, qradar_label):
        fail_msg = "{} did not match labels given in the app.config".format(qradar_label)
        super(LabelError, self).__init__(fail_msg)

class ResilientActionError(Exception):
    """
    Custom Exception class - Resilient Errors
    """
    def __init__(self, msg):
        super(ResilientActionError, self).__init__(msg)
        self.msg = msg

    def __str__(self):
        return repr(self.msg)