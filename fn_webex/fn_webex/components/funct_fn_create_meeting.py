# -*- coding: utf-8 -*-
# 
# """AppFunction implementation"""
from re import S
from fn_webex.lib.cisco_api import WebexAPI
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import IntegrationError, validate_fields, RequestsCommon

PACKAGE_NAME = "fn_webex"
FN_NAME = "fn_create_meeting"

'''
requiredParameters = {
    "start"                       : datetime.datetime.now() + datetime.timedelta(minutes=2),
    "end"                         : datetime.datetime.now() + datetime.timedelta(minutes=20),
    "url"                         : "https://webexapis.com/v1/meetings/",
    "bearerID"                    : "MDViZWYyOWYtNGQwMC00OGRlLWE3MzMtZTc3NDNiODU3ZTYzNzEyZWE1N2UtNzll_PF84_602d7d50-4ed5-40fc-a8ad-63646501cd00"
    "rc"                          : ""
    "timzone"                     : "gmt 05:30",
}

meetingParameters = {
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
'''

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

        print("\n\n\n\n", fn_msg, "\n\n\n\n")
        # self.LOG.info("fn_msg: %s", fn_msg)

        # Example validating app_configs
        # validate_fields([
        #     {"name": "api_key", "placeholder": "<your-api-key>"},
        #     {"name": "base_url", "placeholder": "<api-base-url>"}],
        #     self.app_configs)

        # Example validating required fn_inputs
        # validate_fields(["required_input_one", "required_input_two"], fn_inputs)

        # Example accessing optional attribute in fn_inputs (this is similar for app_configs)
        # optional_input = fn_inputs.optional_input if hasattr(fn_inputs, "optional_input") else "Default Value"

        # Example getting access to self.get_fn_msg()
        # fn_msg = self.get_fn_msg()
        # self.LOG.info("fn_msg: %s", fn_msg)

        # Example interacting with REST API
        # res_client = self.rest_client()
        # function_details = res_client.get("/functions/{0}?handle_format=names".format(FN_NAME))

        # Example raising an exception
        # raise IntegrationError("Example raising custom error")

        ##############################################
        # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE #
        ##############################################
        webex = WebexAPI(self.requiredParameters, self.meetingParameters)
        response = webex.create_meeting()
        # Call API implementation example:
        # params = {
        #     "api_key": self.app_configs.api_key,
        #     "ip_address": fn_inputs.artifact_value
        # }
        #
        # response = self.rc.execute(
        #     method="get",
        #     url=self.app_configs.api_base_url,
        #     params=params
        # )
        #
        # results = response.json()
        #
        # yield self.status_message("Endpoint reached successfully and returning results for App Function: '{0}'".format(FN_NAME))
        #
        # yield FunctionResult(results)
        ##############################################

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        # Note this is only used for demo purposes! Put your own key/value pairs here that you want to access on the Platform
        if response.get("status") == "SUCCESS":
            success = True
        else:
            success = False
        results = rp.done(success, response)

        print(response.text)
        yield FunctionResult(response.text)
        # yield FunctionResult({}, success=False, reason="Bad call")
