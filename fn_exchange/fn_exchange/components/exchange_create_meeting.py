# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

from resilient_circuits import (AppFunctionComponent, app_function,
                                StatusMessage)

from fn_exchange.lib.exchange_helper import PACKAGE_NAME, ResultsHandler
from fn_exchange.lib.exchange_utils import exchange_interface


FN_NAME = "exchange_create_meeting"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'exchange_find_emails' """

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Creates a meeting and sends out invitation to required attendees and optional attendees.

        Inputs:
        -------
        username                <str> : Primary email account to be used
        subject                 <str> : Subject for the meeting invite
        body                    <str> : Body for the meeting invite
        required_attendees      <str> : List of required attendees (comma separated)
        optional_attendees      <str> : List of optional attendees (comma separated)
        start_time         <datetime> : Meeting start time and date
        end_time           <datetime> : Meeting end time and date

        Returns:
        --------
            Response <dict> : A response with the meeting details or the error message
                              if the meeting creation process failed
        """
        rh = ResultsHandler(package_name=PACKAGE_NAME, fn_inputs=fn_inputs)
        function_parameters = {}
        function_parameters["username"] = getattr(fn_inputs, "exchange_email", None)
        function_parameters["start_time"] = getattr(fn_inputs, "exchange_meeting_start_time", None)
        function_parameters["end_time"] = getattr(fn_inputs, "exchange_meeting_end_time", None)
        function_parameters["subject"] = getattr(fn_inputs, "exchange_meeting_subject", None)
        function_parameters["body"] = getattr(fn_inputs, "exchange_meeting_body", None)
        function_parameters["required_attendees"] = getattr(fn_inputs, "exchange_required_attendees", None)
        function_parameters["optional_attendees"] = getattr(fn_inputs, "exchange_optional_attendees", None)

        try:
            utils = exchange_interface(self.rc, self.options)
            yield StatusMessage(f"Successfully connected to {function_parameters.get('emails')}")

            yield StatusMessage("Sending out meeting invite")
            results = utils.create_meeting(function_parameters)
            yield StatusMessage("Meeting invite created and sent!")
            yield rh.success(results)

        except Exception as err:
            yield rh.fail(reason=str(err))