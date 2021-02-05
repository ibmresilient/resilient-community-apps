# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.

"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import validate_fields, ResultPayload, RequestsCommon
from fn_create_webex_meeting.lib.cisco_api import WebexAPI

PACKAGE_NAME = 'fn_create_webex_meeting'

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_create_webex_meeting"""

    def load_opts(self, opts):
        """
        Get app.config values and validate them.
        """
        self.options = opts.get(PACKAGE_NAME, {})
        self.opts = opts

        # Validate required fields
        required_fields = ["webex_email", "webex_password", "webex_site_url", "webex_timezone"]
        validate_fields(required_fields, self.options)

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.load_opts(opts)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.load_opts(opts)

    @function("fn_create_webex_meeting")
    def _fn_create_webex_meeting_function(self, event, *args, **kwargs):
        """Function: Creates a webex meeting and returns the URL"""
        try:
            rp = ResultPayload(PACKAGE_NAME, **kwargs)

            opts = dict()
            opts["rc"] = RequestsCommon(self.opts, self.options)
            opts["webex_site_url"] = self.options.get("webex_site_url")
            opts["email"] = self.options.get("webex_email")
            opts["password"] = self.options.get("webex_password")
            opts["sitename"] = self.options.get("webex_site", None)
            opts["timezone"] = self.options.get("webex_timezone")

            if self.options.get("webex_site_id"):
                opts["site_id"] = self.options.get("webex_site_id")
            if self.options.get("webex_partner_id"):
                opts["partner_id"] = self.options.get("webex_partner_id")

            webex_meeting_name = kwargs.get("webex_meeting_name")  # text
            webex_meeting_password = kwargs.get("webex_meeting_password")  # text
            webex_meeting_agenda = kwargs.get("webex_meeting_agenda")  # text
            webex_meeting_start_time = kwargs.get("webex_meeting_start_time") # time
            webex_meeting_end_time = kwargs.get("webex_meeting_end_time") # time

            opts["meeting_password"] = webex_meeting_password
            opts["meeting_name"] = webex_meeting_name
            opts["meeting_agenda"] = webex_meeting_agenda

            self.common = WebexAPI(opts, webex_meeting_start_time, webex_meeting_end_time)

            response = self.common.create_meeting()

            if response.get("status") == "SUCCESS":
                success = True
            else:
                success = False
            results = rp.done(success, response)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as err:
            yield FunctionError(err)
