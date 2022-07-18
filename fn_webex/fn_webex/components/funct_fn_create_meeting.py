# -*- coding: utf-8 -*-
# 
# """AppFunction implementation"""
from re import S
from fn_webex.lib.cisco_api import WebexAPI
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import IntegrationError, validate_fields, RequestsCommon, ResultPayload

PACKAGE_NAME = "fn_webex"
FN_NAME = "fn_create_meeting"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'fn_create_meeting'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)
        self.requiredParameters, self.meetingParameters = {}, {}
        self.opts = opts
        self.config_options = opts.get(PACKAGE_NAME, {})      
        

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Creates a WebEx meeting and returns the Host URL and Attendee URL.
        Inputs:
            -   fn_inputs.webex_meeting_name
            -   fn_inputs.webex_meeting_agenda
            -   fn_inputs.webex_meeting_start_time
            -   fn_inputs.webex_meeting_end_time
        """
        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        rp = ResultPayload(PACKAGE_NAME)

        self.requiredParameters["start"] = fn_inputs.webex_meeting_start_time
        self.requiredParameters["end"] = fn_inputs.webex_meeting_end_time
        self.requiredParameters["url"] = self.config_options.get("webex_site_url")
        self.requiredParameters["bearerID"] = self.config_options.get("webex_bearerid")
        self.requiredParameters["rc"] = RequestsCommon(self.opts, self.config_options)
        self.requiredParameters["timezone"] = self.config_options.get("webex_timezone", None)

        self.meetingParameters["siteURL"] = self.config_options.get("webex_siteurl", "")
        self.meetingParameters["hostEmail"] = self.config_options.get("hostEmail", "")
        self.meetingParameters["title"] = fn_inputs.webex_meeting_name
        self.meetingParameters["agenda"] = fn_inputs.webex_meeting_agenda
        self.meetingParameters["password"] = fn_inputs.webex_meeting_password
        self.meetingParameters["sendEmail"] = True

        validate_fields(["webex_meeting_start_time", "webex_meeting_end_time"], fn_inputs)
        validate_fields([{"name" : "webex_site_url", 
                         "name" : "webex_bearerID", 
                         "name" : "webex_timezone"}], self.config_options)

        fn_msg = self.get_fn_msg()
        self.LOG.info("fn_msg: %s", fn_msg)

        # Example interacting with REST API
        # res_client = self.rest_client()
        # function_details = res_client.get("/functions/{0}?handle_format=names".format(FN_NAME))

        webex = WebexAPI(self.requiredParameters, self.meetingParameters)
        response = webex.create_meeting()

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))
        results = rp.done(response.get("status"), response)

        yield FunctionResult(response)
