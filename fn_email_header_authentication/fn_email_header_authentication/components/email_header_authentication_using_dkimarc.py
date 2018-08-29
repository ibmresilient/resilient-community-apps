# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'email_header_authentication_using_dkimarc"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_email_header_authentication", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_email_header_authentication", {})

    @function("email_header_authentication_using_dkimarc")
    def _email_header_authentication_using_dkimarc_function(self, event, *args, **kwargs):
        """Function: """
        try:
            # Get the function parameters:
            email_header_authentication_target_email = kwargs.get("email_header_authentication_target_email")  # text

            log = logging.getLogger(__name__)
            log.info("email_header_authentication_target_email: %s", email_header_authentication_target_email)

            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE
            #  yield StatusMessage("starting...")
            #  yield StatusMessage("done...")

            results = {
                "value": "xyz"
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()