# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.

import time
import logging
import datetime

from urllib import request
from resilient_lib import  RequestsCommon
from lib2to3.pytree import convert
from resilient_circuits import FunctionError

DEFAULT_MEETING_LENGTH = 45


class WebexAPI:
    def __init__(self, requiredParameters, optionalParameters):
        self.optionalParameters = optionalParameters
        self.requiredParameters = requiredParameters
        self.rc = self.requiredParameters.get("rc")
        self.header = self.generate_header(self.requiredParameters["bearerID"])
        self.timezone = self.get_timeZones(self.requiredParameters.get("timezone"))
        self.check_time(self.requiredParameters["start"], self.requiredParameters["end"])
        

    def convert_to_dict(self, to_convert):
        ret = {}
        for bracket in ["[", "]", "{", "}", "\""]:
            to_convert = to_convert.replace(bracket,"")
        for pair in to_convert.split(","):
            key = pair.split(":")[0]
            value = pair[len(key)+1:]
            ret[key] = value
        return ret


    def create_meeting(self):
        meetingOptions = self.generate_meeting_parameters(self.optionalParameters)
        response = self.webex_request("post", meetingOptions)

        if response.text == "":
            raise FunctionError("Failed to create meeting, null response")
        
        results = self.convert_to_dict(response.text)
        if response.status_code == 200:
            results["status"] = True
        else:
            results["status"] = False
        return results


    def check_time(self, meeting_start, meeting_end):
        if meeting_start is not None:
            meeting_start = datetime.datetime.fromtimestamp(meeting_start/1000)
        else :
            meeting_start = datetime.datetime.now() + datetime.timedelta(minutes=2)

        if meeting_end is not None:
            meeting_end = datetime.datetime.fromtimestamp(meeting_end/1000)
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
            'Content-Type'  : 'application/json'}
        return header


    def get_timeZones(self, timezone):
        if timezone is None:
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


    def generate_meeting_parameters(self, meetingParameters):
        request_parameters = '{\"start\":\"' + self.meeting_start_time + '\", \"end\":\"' + self.meeting_end_time + '\"'
        for key in meetingParameters.keys():
            request_parameters +=  ', \"{}\":\"{}\" '.format(key, meetingParameters[key])
        request_parameters +=  "}"
        return request_parameters


    def webex_request(self, method, data):
        """Wrapper for requests, appends content-type and fills in site url"""
        webexurl = self.requiredParameters.get("url")
        response = self.rc.execute_call_v2(method, webexurl, data=data,
                                        headers=self.header, proxies=self.rc.get_proxies())
        if response is None:
            raise FunctionError("Invalid METHOD passed to webex_request! Method: {}".format(method))
        if response.status_code != 200 and response.status_code != 201 and response.status_code != 401:
            raise FunctionError("API call failed! HTTP Status: {}, URL: {}".format(response.status_code, webexurl))
        elif response.status_code == 401:
            raise FunctionError("Security context is invalid, API returned 401!")
        return response


