# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
import dkim


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'email_header_validation_using_dkimarc"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_email_header_validation", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_email_header_validation", {})

    @function("email_header_validation_using_dkimarc")
    def _email_header_validation_using_dkimarc_function(self, event, *args, **kwargs):
        """Function: Analyzes the DKIM and ARC headers for an RFC822 formatted email."""
        try:
            # Get the function parameters:
            email_header_validation_target_email = kwargs.get("email_header_validation_target_email")  # text

            log = logging.getLogger(__name__)
            log.info("email_header_validation_target_email: %s", email_header_validation_target_email)

            yield StatusMessage("Analyzing email headers")
            # Initialize DKIM object and check for DKIM header
            dkim_email = dkim.DKIM(email_header_validation_target_email)
            dkim_header_exists = b"dkim-signature" in [header[0].lower() for header in dkim_email.headers]

            # Do header analysis
            dkim_results = dkim.dkim_verify(email_header_validation_target_email)
            arc_results = dkim.arc_verify(email_header_validation_target_email)

            # Form DKIM results statement
            if dkim_header_exists:
                if dkim_results:
                    dkim_message = 'success'
                else:
                    dkim_message = 'Most recent DKIM-Message-Signature did not validate'
            else:
                dkim_message = 'Message is not DKIM signed'

            results = {
                "dkim_verify": dkim_results,
                "arc_verify": arc_results[0] == 'pass',
                "dkim_message": dkim_message,
                "arc_message": arc_results[2]
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()