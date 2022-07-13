# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.
import time
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
    "start"                       : datetime.datetime.now() + datetime.timedelta(minutes=2),
    "end"                         : datetime.datetime.now() + datetime.timedelta(minutes=20),
    "userId"                      : "admin@calvinwynne-8xjq.wbx.ai",
    "userPassword"                : "Q4Xr5bA0i]",
    "bearerID"                    : "NjVjZDFlNjAtODAyOC00MGMxLThlODQtMzVmYmE2YTk0MjdhOTNhMzY3YmItZmY5_P0A1_f688574e-8402-4b53-864e-e725f4468887",
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
        self.test_get_timeZones()
        self.test_generate_header()
        self.optionalParameters = optionalParameters
        self.requiredParameters = requiredParameters
        self.header = self.generate_header(self.requiredParameters["bearerID"])
        self.timezone = self.get_timeZones()
        self.check_time(self.requiredParameters["start"], self.requiredParameters["end"])
        self.webex_request()

    def check_time(self, meeting_start, meeting_end):
        if not meeting_start:
            self.meeting_start = datetime.datetime.now() + datetime.timedelta(minutes=2)
        if meeting_end is not None:
            if meeting_end < meeting_start:
                raise ValueError('End time must be after start time')
        else:
            meeting_end = meeting_start + datetime.timedelta(minutes=DEFAULT_MEETING_LENGTH)
        
        self.meeting_start_time = meeting_start.strftime('%Y-%m-%dT%H:%M:%S') + self.timezone
        self.meeting_end_time   = meeting_end.strftime('%Y-%m-%dT%H:%M:%S') + self.timezone

    def generate_header(self, bearerID):
        if not bearerID:
            raise ValueError("Bearer ID not specified")
        header = {
            'Authorization' : "Bearer {}".format(bearerID),
            'Content-Type'  :  'application/json'}
        return header

    def test_generate_header(self):
        assert(isinstance(self.generate_header("ID123"), dict))
        assert(self.generate_header("ID123")["Authorization"] == "Bearer ID123")
        assert(self.generate_header("ID123")["Content-Type" ] == "application/json")
        try:
            self.generate_header(None)
        except ValueError as msg:
            print(msg)

    def get_timeZones(self, timezone=None):
        if not timezone:
            return time.strftime("%z", time.localtime())
        else:
            timezone = timezone.strip()
        formatted_timezone = ""
        _temp = timezone.split(" ")
        if len(_temp) > 1:
            if "gmt" in _temp[0].lower() or "utc" in _temp[0].lower():
                if "-" not in _temp[1] and "+" not in _temp[1]:
                    formatted_timezone = "+"
                formatted_timezone += _temp[1].replace(":", "")
            else:
                raise ValueError("Unsupported timezone specified. Supported timezones GMT or UTC")
        elif len(_temp) == 1:
            if "-" not in timezone and "+" not in timezone:
                formatted_timezone = "+"
            formatted_timezone += timezone.replace(":", "")
        
        if not formatted_timezone[1:].isdigit():
            raise ValueError("Invalid Timezone format. Expected format GMT -01:00")
        return formatted_timezone 


    def test_get_timeZones(self):
        assert(self.get_timeZones("GMT 05:30")   == "+0530")
        assert(self.get_timeZones("GMT +05:30")  == "+0530")
        assert(self.get_timeZones("GMT -05:30")  == "-0530")
        assert(self.get_timeZones("UTC -05:30")  == "-0530")
        assert(self.get_timeZones("GMT 0530")    == "+0530")
        assert(self.get_timeZones(" GMT 0530  ") == "+0530")
        assert(self.get_timeZones("0530")        == "+0530")
        assert(self.get_timeZones(" -05:30  ")    == "-0530")
        assert(self.get_timeZones() == time.strftime("%z", time.localtime()))

        try:
            self.get_timeZones("GMT 05:£30")
        except ValueError as msg:
            print(msg)

        try:
            self.get_timeZones("IST 05:30")
        except ValueError as msg:
            print(msg)


    def generate_meeting_parameters(self, meetingParameters):
        request_parameters = '{\"start\":\"' + self.meeting_start_time + '\", \"end\":\"' + self.meeting_end_time + '\"'
        for key in meetingParameters.keys():
            request_parameters +=  ', \"{}\":\"{}\" '.format(key, meetingParameters[key])
        print("\n\n\n")
        request_parameters +=  "}"
        print(request_parameters)
        print("\n\n\n")
        return request_parameters

    def webex_request(self):
        """Wrapper for requests, appends content-type and fills in site url"""
        url = 'https://webexapis.com/v1/meetings/'

        # response = requests.post(url, data=self.generate_meeting_parameters(self.optionalParameters), headers=self.header)
        rc = self.requiredParameters["rc"]
        response = rc.execute_call_v2("post", url, data=self.generate_meeting_parameters(self.optionalParameters), headers=self.header, proxies=rc.get_proxies())

        if response is None:
            raise FunctionError("Invalid METHOD passed to webex_request! Method: {}".format("POST"))

        if response.status_code != 200 and response.status_code != 201 and response.status_code != 401:
            raise FunctionError("API call failed! HTTP Status: {}, URL: {}".format(response.status_code, url))
        elif response.status_code == 401:
            # access token probably expired
            raise FunctionError("Security context is invalid, API returned 401!")

        return response
        

WebexAPI(requiredParameters, optionalParameters)