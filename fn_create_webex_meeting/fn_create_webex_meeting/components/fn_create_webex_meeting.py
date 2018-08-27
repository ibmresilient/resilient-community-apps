# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from ..lib.cisco_api import WebexAPI


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_create_webex_meeting"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("create_webex_meeting", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("create_webex_meeting", {})

    @function("fn_create_webex_meeting")
    def _fn_create_webex_meeting_function(self, event, *args, **kwargs):
        """Function: Creates a webex meeting and returns the URL"""
        try:
            webex_email = self.options.get("webex_email")
            if webex_email is None:
                yield FunctionError("webex_email is not defined in app.config")

            webex_password = self.options.get("webex_password")
            if webex_password is None:
                yield FunctionError("webex_password is not defined in app.config")

            webex_site = self.options.get("webex_site")
            if webex_site is None:
                yield FunctionError("webex_site is not defined in app.config")

            webex_site_url = self.options.get("webex_site_url")
            if webex_site_url is None:
                yield FunctionError("webex_site_url is not defined in app.config")

            webex_timezone = self.options.get("webex_timezone")
            if webex_timezone is None:
                yield FunctionError("webex_timezone is not defined in app.config")


            opts = dict()
            opts["webex_site_url"] = webex_site_url
            opts["email"] = webex_email
            opts["password"] = webex_password
            opts["sitename"] = webex_site
            opts["timezone"] = webex_timezone

            webex_meeting_name = kwargs.get("webex_meeting_name")  # text
            webex_meeting_password = kwargs.get("webex_meeting_password")  # text
            webex_meeting_agenda = kwargs.get("webex_meeting_agenda")  # text
            webex_meeting_start_time = kwargs.get("webex_meeting_start_time") # time
            webex_meeting_end_time = kwargs.get("webex_meeting_end_time") # time

            opts["meeting_password"] = webex_meeting_password
            opts["meeting_name"] = webex_meeting_name
            opts["meeting_agenda"] = webex_meeting_agenda

            self.common = WebexAPI(opts, webex_meeting_start_time, webex_meeting_end_time)

            result = self.common.create_meeting()

            if result.get("status") == "FAILURE":
                yield FunctionError(result.get("fail_reason"))

            # Produce a FunctionResult with the results
            yield FunctionResult(result)
        except Exception as e:
            yield FunctionError(e.message)
