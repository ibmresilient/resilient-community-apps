# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

from resilient_circuits import (AppFunctionComponent, app_function,
                                StatusMessage)

from fn_exchange.lib.exchange_helper import PACKAGE_NAME, INPUTS_MAP, ResultsHandler
from fn_exchange.lib.exchange_utils import exchange_interface
from fn_exchange.lib.exchange_configure_tab import init_exchange_tab


FN_NAME = "exchange_create_meeting"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'exchange_find_emails' """

    def __init__(self, opts):
        init_exchange_tab()
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Creates a meeting and sends out invitation to required attendees and optional attendees.

        Inputs:
        -------
        The values returned from fn_inputs are mapped to easier readable variable names using the 
        INPUT_MAP that is found in fn_exchange.lib.exchange_helper
        
        exchange_email                   <str> : Primary email account to be used
        meeting_subject                  <str> : Subject for the meeting invite
        meeting_body                     <str> : Body for the meeting invite
        exchange_required_attendees      <str> : List of required attendees (comma separated)
        exchange_optional_attendees      <str> : List of optional attendees (comma separated)
        exchange_location                <str> : Venue details or online meeting link
        exchange_online_meeting          <str> : Specifies if its a online meeting
        exchange_meeting_start_time <datetime> : Meeting start time and date
        exchange_meeting_end_time   <datetime> : Meeting end time and date

        Returns:
        --------
            Response <dict> : A response with the meeting details or the error message
                              if the meeting creation process failed
        """
        rh = ResultsHandler(package_name=PACKAGE_NAME, fn_inputs=fn_inputs)
        function_parameters = {}
        for key, value in fn_inputs._asdict().items():
            function_parameters[INPUTS_MAP[key]] = value

        try:
            utils = exchange_interface(self.rc, self.options)
            yield StatusMessage(f"Successfully connected to {function_parameters.get('email')}")

            yield StatusMessage("Sending out meeting invite")
            results = utils.create_meeting(function_parameters)
            yield StatusMessage("Meeting invite created and sent!")
            yield rh.success(results)

        except Exception as err:
            yield rh.fail(reason=str(err))
