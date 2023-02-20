# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

from resilient_circuits import (AppFunctionComponent, app_function,
                                StatusMessage)

from fn_exchange.lib.exchange_helper import PACKAGE_NAME, INPUTS_MAP, ResultsHandler
from fn_exchange.lib.exchange_utils import exchange_interface

FN_NAME = "exchange_send_email"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'exchange_find_emails' """

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Send email to a list of recipients and save it to the SENT folder of the mailbox

        Inputs:
        -------
            exchange_email    <str> : Primary email account to be used
            recipients  <str> : Mail ids of the recipients (comma separated)
            msg_body    <str> : Body of the mail
            msg_subject <str> : Mail subject

        Returns:
        --------
            Response <dict> : A response with the email sent and or the error message
                              if the operation failed
        """
        rh = ResultsHandler(package_name=PACKAGE_NAME, fn_inputs=fn_inputs)
        function_parameters = {}
        
        function_parameters = {}
        for key, value in fn_inputs._asdict().items():
            function_parameters[INPUTS_MAP[key]] = value

        if not function_parameters.get("username"):
            function_parameters["username"] = self.options.get('username')
            self.LOG.info('No connection email was specified, using value from config file')

        for parameter in function_parameters:
            self.LOG.info(f"{parameter} : {str(function_parameters.get(parameter))}")

        try:
            utils = exchange_interface(self.rc, self.options)
            yield StatusMessage(f"Successfully connected to {function_parameters.get('emails')}")

            results = utils.create_email_message(function_parameters)

            yield StatusMessage("Email sent!")
            yield rh.success(results)

        except Exception as err:
            yield rh.fail(reason=str(err))
