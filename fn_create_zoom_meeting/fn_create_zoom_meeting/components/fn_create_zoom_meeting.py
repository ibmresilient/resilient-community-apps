# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from ..components.zoom_common import ZoomCommon
import pytz

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_create_zoom_meeting"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("create_zoom_meeting", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("create_zoom_meeting", {})

    @function("fn_create_zoom_meeting")
    def _fn_create_zoom_meeting_function(self, event, *args, **kwargs):
        """Function: This will return a meeting URL to connect to a zoom meeting"""
        try:
            log = logging.getLogger(__name__)

            # Get the function parameters:
            zoom_host_email = kwargs.get("zoom_host_email")  # text
            zoom_topic = kwargs.get("zoom_topic")  # text
            zoom_agenda = kwargs.get("zoom_agenda")  # text
            zoom_password = kwargs.get("zoom_password")  # text
            zoom_record_meeting = kwargs.get("zoom_record_meeting")  # boolean

            if type(zoom_record_meeting) is not bool:
                zoom_record_meeting = False

            zoom_api_url = self.options.get("zoom_api_url")
            zoom_api_key = self.options.get("zoom_api_key")
            zoom_api_secret = self.options.get("zoom_api_secret")
            zoom_api_timezone = self.options.get("zoom_api_timezone")

            if zoom_api_timezone is None:
                yield FunctionError("zoom_api_timezone is not defined in app.config")

            try:
                pytz.timezone(str(zoom_api_timezone))
            except pytz.exceptions.UnknownTimeZoneError:
                yield FunctionError("Invalid timezone provided in app.config")

            if zoom_api_url is None:
                yield FunctionError("zoom_api_url is not defined in app.config")

            if zoom_api_key is None:
                yield FunctionError("zoom_api_key is not defined in app.config")

            if zoom_api_secret is None:
                yield FunctionError("zoom_api_secret is not defined in app.config")

            if zoom_topic is None:
                zoom_topic = ""

            if zoom_password is None:
                zoom_password = ""

            self.common = ZoomCommon(zoom_api_url, zoom_api_key, zoom_api_secret)

            r = self.common.create_meeting(zoom_host_email, zoom_agenda, zoom_record_meeting, zoom_topic, zoom_password, zoom_api_timezone)

            yield FunctionResult(r)
        except Exception as e:
            log.error(e)
            yield FunctionError(e)
