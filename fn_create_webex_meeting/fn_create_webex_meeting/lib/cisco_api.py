# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

import requests
import re
import logging
import datetime
import pytz

from resilient_circuits import FunctionError

DEFAULT_MEETING_LENGTH = 60

class WebexAPI:
    def __init__(self, options, meeting_start_time, meeting_end_time):
        self.opts = options

        self.meeting_start_time = meeting_start_time
        if meeting_end_time is not None:
            if meeting_start_time:
                if meeting_end_time < meeting_start_time:
                    raise ValueError('End time must be after start time')
            else:
                raise ValueError('If an end time is specified, a start time must also be specified')
        self.meeting_end_time = meeting_end_time

    def webex_request(self, path=None, method="GET", query=None, headers=None):
        """Wrapper for requests, appends content-type and fills in site url"""
        url = self.opts.get("webex_site_url") + path

        if "http" not in url:
            url = "https://" + url

        if headers is None:
            headers = {}

        if method == "POST":
            headers["Content-Type"] = "application/xml"

        response = None
        if method == "GET":
            response = requests.get(url, headers=headers)
        elif method == "POST":
            response = requests.post(url, data=query, headers=headers)

        if response is None:
            raise FunctionError("Invalid METHOD passed to webex_request! Method: {}".format(method))

        if response.status_code != 200 and response.status_code != 201 and response.status_code != 401:
            raise FunctionError("API call failed! HTTP Status: {}, URL: {}".format(response.status_code, url))
        elif response.status_code == 401:
            # access token probably expired
            raise FunctionError("Security context is invalid, API returned 401!")

        return response

    def generate_get_timezones_xml(self):
        """Generates the XML used to request a list of timezones and their properties"""
        security_context = self.generate_security_context()

        timezone_xml = """<?xml version="1.0" encoding="UTF-8"?>
        <serv:message xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:serv="http://www.webex.com/schemas/2002/06/service">
        <header>""" + security_context + """</header>
        <body>
        <bodyContent xsi:type="site.LstTimeZone">
        </bodyContent>
        </body>
        </serv:message>"""

        return timezone_xml

    def get_timezone_info(self):
        """Gets a list of timezones, then parses the results for timezone specified by user in app.config"""
        timezone_xml = self.generate_get_timezones_xml()

        path = "/WBXService/XMLService"

        log = logging.getLogger(__name__)

        response = self.webex_request(path, "POST", timezone_xml)

        status_regex = "<serv:result>(.*)<\/serv:result>"
        status_regex_search = re.search(status_regex, response.text)

        # check if call failed
        if status_regex_search is not None and status_regex_search.group(1) == "FAILURE":
            return {"id": 0, "gmt_hour": 0, "gmt_minute": 0}

        timezone_pattern = re.compile(r'<ns1:timeZoneID>([0-9]*)<\/ns1:timeZoneID><ns1:gmtOffset>[\-0-9]*<\/ns1:gmtOffset><ns1:description>([a-zA-Z+\-0-9:,\s\(\).&;]*)<\/ns1:description>')
        gmt_time_pattern = r'GMT([\-+0-9]*):([0-9]*)'

        for m in re.finditer(timezone_pattern, response.text):
            if self.opts["timezone"] in m.group(2):
                gmt_time_match = re.search(gmt_time_pattern, m.group(2))
                gmt_hour = 0
                gmt_minute = 0

                if gmt_time_match:
                    gmt_hour = int(gmt_time_match.group(1))
                    gmt_minute = int(gmt_time_match.group(2))

                return {"id": str(m.group(1)), "gmt_hour": gmt_hour, "gmt_minute": gmt_minute}

        return {"id": 0, "gmt_hour": 0, "gmt_minute": 0}

    def generate_security_context(self):
        """Generates the security context required by the API for authentication"""
        xml = """<securityContext>
        <webExID>""" + self.opts.get("email") + """</webExID>
        <password>""" + self.opts.get("password") + """</password>
        <siteName>""" + self.opts.get("sitename") + """</siteName>
        </securityContext>"""

        return xml

    def generate_meeting_data(self):
        """Generates partial XML that is used to create a meeting"""
        meeting_password = self.opts.get("meeting_password")
        meeting_name = self.opts.get("meeting_name")
        meeting_agenda = self.opts.get("meeting_agenda")

        timezone_info = self.get_timezone_info()
        if type(timezone_info.get("id")) is int and timezone_info.get("id") is 0:
            raise FunctionError("Unable to find timezone for string %s" % self.opts.get("timezone"))

        utc_offset = datetime.timedelta(hours=timezone_info["gmt_hour"], minutes=timezone_info["gmt_minute"])
        now = datetime.datetime.now(pytz.utc)

        timezones_with_offset = list({tz for tz in map(pytz.timezone, pytz.all_timezones_set)
                                      if now.astimezone(tz).utcoffset() == utc_offset})
        if self.meeting_start_time is None:
            time = datetime.datetime.now(tz=timezones_with_offset[0])
            duration = DEFAULT_MEETING_LENGTH
        else:
            time = datetime.datetime.fromtimestamp(self.meeting_start_time/1000, tz=timezones_with_offset[0])
            if self.meeting_end_time:
                duration = (self.meeting_end_time/1000 - self.meeting_start_time/1000)/60
            else:
                duration = DEFAULT_MEETING_LENGTH
        meeting_time = time.strftime("%m/%d/%Y %H:%M:%S")

        xml = """<accessControl>
        <meetingPassword>{}</meetingPassword>
        </accessControl>
        <metaData>
        <confName>{}</confName>
        <agenda>{}</agenda>
        </metaData>
        <schedule>
        <startDate>{}</startDate>
        <duration>{}</duration>
        <timeZoneID>{}</timeZoneID>
        </schedule>""".format(meeting_password, meeting_name, meeting_agenda, meeting_time, duration,
                              timezone_info.get("id"))

        return xml

    def generate_create_meeting_xml(self):
        """Generates the entire XML data used to create a meeting"""
        security_context = self.generate_security_context()
        meeting_data = self.generate_meeting_data()

        meeting_xml = """<?xml version="1.0" encoding="UTF-8"?>
        <serv:message xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:serv="http://www.webex.com/schemas/2002/06/service">
        <header>""" + security_context + """</header>
        <body>
        <bodyContent xsi:type="java:com.webex.service.binding.meeting.CreateMeeting">
        """ + meeting_data + """</bodyContent>
        </body>
        </serv:message>"""

        return meeting_xml

    def create_meeting(self):
        """Creates a meeting based on options specified in app.config and function args"""
        meeting_xml = self.generate_create_meeting_xml()

        path = "/WBXService/XMLService"

        response = self.webex_request(path, "POST", meeting_xml)

        if response.text == "":
            raise FunctionError("Failed to create meeting, null response")

        status_regex = "<serv:result>(.*)<\/serv:result>"
        failure_reason_regex = "<serv:reason>(.*)<\/serv:reason>"

        status_regex_search = re.search(status_regex, response.text)
        failure_reason_regex_search = re.search(failure_reason_regex, response.text)

        results = {}

        if status_regex_search is not None:
            results["status"] = status_regex_search.group(1)

        if failure_reason_regex_search is not None:
            results["fail_reason"] = failure_reason_regex_search.group(1)
            return results

        success_details_regex = "<serv:host>(.*)<\/serv:host>\s*<serv:attendee>(.*)<\/serv:attendee>"

        success_details_regex_search = re.search(success_details_regex, response.text)

        if success_details_regex_search is not None:
            results["host_url"] = success_details_regex_search.group(1)
            results["attendee_url"] = success_details_regex_search.group(2)

        return results
