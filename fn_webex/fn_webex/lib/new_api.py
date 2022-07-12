# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.

import re
import logging
import datetime
from urllib import request
import pytz

import requests

import configparser
from resilient_lib import  RequestsCommon
from resilient_circuits import FunctionError

DEFAULT_MEETING_LENGTH = 45

requiredParameters = {
    "rc"                          : RequestsCommon(),
    "start"                       : datetime.datetime.now(),
    "end"                         : datetime.datetime.now() + datetime.timedelta(minutes=20),
    "userId"                      : "admin@calvinwynne-8xjq.wbx.ai",
    "userPassword"                : "Q4Xr5bA0i]",
    "bearerID"                    : "NDc5ZTczNDAtMGU0MC00Y2Q0LThkNTEtZjExNzk0MzM5MTljZmVmZmM0NWYtMjNl_P0A1_f688574e-8402-4b53-864e-e725f4468887",
    "timzone"                     : "gmt05:30"
}

optionalParameters = {
    "siteURL"                     : "calvinwynne-8xjq.webex.com",
    "hostEmail"                   : "",
    "title"                       : "Sample Meeting VSCode",
    "password"                    : "abcd123",
    "agenda"                      : "to test sample meetings",
    "enabledAutoRecordMeeting"    : "false",
    "allowAnyUserToBeCoHost"      : "false",
    "enabledJoinBeforeHost"       : "false",
    "enableConnectAudioBeforeHost": "false",
    "excludePassword"             : "false",
    "publicMeeting"               : "false",
    "enabledWebcastView"          : "false",
    "enableAutomaticLock"         : "false",
    "allowFirstUserToBeCoHost"    : "false",
    "allowAuthenticatedDevices"   : "false",
    "sendEmail"                   : "true",
}


class WebexAPI:
    def __init__(self, requiredParameters, optionalParameters):
        self.optionalParameters = optionalParameters
        self.requiredParameters = requiredParameters
        self.meeting_start_time = self.requiredParameters["start"]
        self.meeting_end_time = self.check_endTime(self.requiredParameters["end"])
        self.header = self.generate_header(self.requiredParameters["bearerID"])

        self.webex_request()


    def check_endTime(self, meeting_end):
        if not self.meeting_start_time:
            self.meeting_start_time = datetime.datetime.now() + datetime.timedelta(minutes=2)
        if meeting_end is not None:
            if meeting_end < self.meeting_start_time:
                raise ValueError('End time must be after start time')
        else:
            meeting_end = self.meeting_start_time + datetime.timedelta(minutes=DEFAULT_MEETING_LENGTH)
        
        self.meeting_start_time = self.meeting_start_time.strftime('%Y-%m-%dT%H:%M:%S')
        return meeting_end.strftime('%Y-%m-%dT%H:%M:%S')


    def generate_header(self, bearerID):
        if not bearerID:
            raise ValueError("Bearer ID not specified")
        header = {
            'Authorization' : "Bearer {}".format(bearerID),
            'Content-Type'  :  'application/json'}
        return header

    def get_timeZones(self):
        pass

    def generate_meeting_parameters(self, meetingParameters):
        request_parameters = '{\"start\":\"' + self.meeting_start_time + '\", \"end\":\"' + self.meeting_end_time + '\"'
        for key in meetingParameters.keys():
            request_parameters +=  ', \"{}\":\"{}\" '.format(key, meetingParameters[key])
        print("\n\n\n")
        request_parameters +=  "}"
        print(request_parameters)
        print("\n\n\n")
        return 
        


    def webex_request(self):
        """Wrapper for requests, appends content-type and fills in site url"""
        url = 'https://webexapis.com/v1/meetings/'

        response = requests.post(url, data=self.generate_meeting_parameters(self.optionalParameters), headers=self.header)

        if response is None:
            raise FunctionError("Invalid METHOD passed to webex_request! Method: {}".format("POST"))

        if response.status_code != 200 and response.status_code != 201 and response.status_code != 401:
            raise FunctionError("API call failed! HTTP Status: {}, URL: {}".format(response.status_code, url))
        elif response.status_code == 401:
            # access token probably expired
            raise FunctionError("Security context is invalid, API returned 401!")

        return response
        

# WebexAPI(requiredParameters, optionalParameters)


import time

print(time.strftime("%z", time.localtime()))

print(time.mktimetm_year=2022, tm_mon=7, tm_mday=12, tm_hour=14, tm_min=24, tm_sec=28, tm_wday=1, tm_yday=193, tm_isdst=0))