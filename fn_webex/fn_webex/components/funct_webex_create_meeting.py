# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
#
# """AppFunction implementation"""
from urllib import parse
from resilient_lib import validate_fields, IntegrationError
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult

from fn_webex.lib import constants
from fn_webex.lib.cisco_meetings import WebexMeetings
from fn_webex.lib.cisco_authentication import WebexAuthentication

PACKAGE_NAME = "fn_webex"
FN_NAME = "webex_create_meeting"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'webex_create_meeting'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)
        self.opts = opts
        self.required_parameters, self.meeting_parameters = {}, {}
        self.config_options = opts.get(PACKAGE_NAME, {})


    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        This function creates and schedules a Webex meeting.

        Fn Inputs:
        ----------
            start        (<str>) : Meeting start time
            end          (<str>) : Meeting end time
            title        (<str>) : Meeting title
            agenda       (<str>) : Meeting agenda
            password     (<str>) : Meeting password
            duration     (<int>) : Duration of the meeting
            sendEmail    (<Bool>): Send invite as email

        Config Options:
        ---------------
            timezone     (<str>) : Meeting timezone
            meetingsURL  (<str>) : A url of the webex meetings API
            sendEmail    (<bool>): Sends the meeting invite to the attendees

        Self Objects:
        -------------
            rc           (<rc>)  : A resilient wrapper for Requests object
            logger       (<logger>)      : A resilient wrapper for logger obhect
            resclient    (<rest_client>) : Rest client to interact with the SOAR instance

        Yields:
        -------
            (<FunctionResult>): States if the application was executed successfully or not.
                                Returns the response retrieved from the Webex endpoint in
                                the form of a dictionary.
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))
        validate_fields(["webex_meeting_name", "webex_send_email", "webex_meeting_duration"], fn_inputs)
        validate_fields(["webex_site_url", "webex_timezone", "client_id",
                        "client_secret", "refresh_token", "scope"], self.config_options)

        self.required_parameters["end"] = fn_inputs.webex_meeting_end_time if hasattr(fn_inputs, 'webex_meeting_end_time') else None
        self.required_parameters["start"] = fn_inputs.webex_meeting_start_time if hasattr(fn_inputs, 'webex_meeting_start_time') else None
        self.required_parameters["timezone"] = self.config_options.get("webex_timezone")
        self.required_parameters["meetingsURL"] = parse.urljoin(self.config_options.get("webex_site_url"), constants.MEETINGS_URL)

        self.required_parameters["rc"]  = self.rc
        self.required_parameters["logger"] = self.LOG
        self.required_parameters["resclient"] = self.rest_client()

        self.meeting_parameters["title"] = fn_inputs.webex_meeting_name
        self.meeting_parameters["agenda"] = fn_inputs.webex_meeting_agenda if hasattr(fn_inputs, 'webex_meeting_agenda') else None
        self.meeting_parameters["password"] = fn_inputs.webex_meeting_password if hasattr(fn_inputs, 'webex_meeting_password') else None
        self.meeting_parameters["duration"] = fn_inputs.webex_meeting_duration
        self.meeting_parameters["sendEmail"] = fn_inputs.webex_send_email

        fn_msg = self.get_fn_msg()
        self.LOG.info("Webex: %s", fn_msg)

        try:
            yield self.status_message(constants.MSG_CREATE_SECURITY)
            self.LOG.info(constants.MSG_CREATE_SECURITY)
            authenticator = WebexAuthentication(self.required_parameters, self.config_options)
            self.required_parameters["header"] = authenticator.authenticate()
            authenticated = True
            self.LOG.info(constants.MSG_SUCCESS_AUTHENTICATED)
            yield self.status_message(constants.MSG_SUCCESS_AUTHENTICATED)

        except IntegrationError as err:
            self.LOG.error(constants.MSG_FAILED_AUTH)
            yield self.status_message(constants.MSG_FAILED_AUTH)
            yield self.status_message("Failed to Authenticate : '{0}'".format(FN_NAME))
            yield FunctionResult(value=None, success=False, reason=str(err))

        if authenticated:
            try:
                webex = WebexMeetings(self.required_parameters, self.meeting_parameters)
                response = webex.create_meeting()
                yield self.status_message(constants.MSG_SUCCESS_EXECUTION.format(FN_NAME))

                if response.get("status_code") == 200:
                    yield FunctionResult(response, success=True)
                else:
                    yield FunctionResult(response, success=False, reason=response.get("message"))

            except IntegrationError as err:
                yield FunctionResult({"message" : str(err)}, success=False, reason=str(err))
