# -*- coding: utf-8 -*-
# Copyright © IBM Corporation 2010, 2020
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
"""
Defined Custom Exceptions
"""
RESPONSE_CODE_SUCCESS = 200
RESPONSE_HTTP_SUCCESS = "<Response [200]>"
RESPONSE_CODE_SUCCESS_CREATED = 201
RESPONSE_CODE_SUCCESS_ACCEPTED = 202
RESPONSE_CODE_SUCCESS_NO_CONTENT = 204

valid_codes = (RESPONSE_CODE_SUCCESS,
               RESPONSE_HTTP_SUCCESS,
               RESPONSE_CODE_SUCCESS_CREATED,
               RESPONSE_CODE_SUCCESS_ACCEPTED,
               RESPONSE_CODE_SUCCESS_NO_CONTENT)


class ResilientAppConfigError(Exception):
    """
    Custom Exception class - Resilient App Config Errors
    """
    def __init__(self, msg):
        super(ResilientAppConfigError, self).__init__(msg)
        self.msg = msg

    def __str__(self):
        return repr(self.msg)


class GuardiumApiError(Exception):
    """
    Custom Exception class - Guardium Restful Service Call Errors
    """
    def __init__(self, message, error_code=0):
        super(GuardiumApiError, self).__init__(message)
        self.error_code = error_code
        self.msg = message

    def __str__(self):
        return "ErrorCode: {}, ErrorMessage {}".format(self.error_code, self.msg)


class GuardiumApiParamsError(Exception):
    """
    Custom Exception class - Guardium API Params Errors
    """
    def __init__(self, message, valid_params, error_code=0):
        super(GuardiumApiParamsError, self).__init__(message)
        self.error_code = error_code
        self.msg = message
        self.valid_param = valid_params

    def __str__(self):
        return "ErrorCode: {}, Valid Params: {}, ErrorMessage {}".format(self.error_code, self.valid_param, self.msg)


def check_for_invalid_response(response):
    """
    Function to check Guardium Restful call response validity
    :param response: Guardium Restful call response object
    :return:
    """
    if response.status_code not in valid_codes:
        if not response.content is None and len(response.content) > 0:
            error_message = response.content.splitlines()[0]
        else:
            if response.status_code == 400:
                error_message = "Malformed Guardium API request, size of url is too long. Please check request size."
            else:
                error_message = ""
        raise GuardiumApiError(error_message, response.status_code)

    elif isinstance(response.json(), dict):
        if len(response.json()) == 2:
            if "ErrorMessage" in response.json() and "ErrorCode" in response.json():
                raise GuardiumApiError(response.json()["ErrorMessage"], response.json()["ErrorCode"])
        elif len(response.json()) == 3:
            if "ErrorMessage" in response.json() and "ErrorCode" in response.json() and "ValidParameterValues" in response.json():
                raise GuardiumApiParamsError(response.json()["ErrorMessage"], response.json()["ValidParameterValues"],
                                             response.json()["ErrorCode"])


class TabledataRestCallError(Exception):
    """
    Custom Exception class - Resilient Table Rest Call Errors
    """
    def __init__(self, msg):
        super(TabledataRestCallError, self).__init__(msg)
        self.msg = msg

    def __str__(self):
        return repr(self.msg)


class ResilientActionError(Exception):
    """
    Custom Exception class - Resilient Errors
    """
    def __init__(self, msg):
        super(ResilientActionError, self).__init__(msg)
        self.msg = msg

    def __str__(self):
        return repr(self.msg)
