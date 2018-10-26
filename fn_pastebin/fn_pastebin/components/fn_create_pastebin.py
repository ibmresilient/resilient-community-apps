# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_create_pastebin"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_pastebin", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_pastebin", {})

    @function("fn_create_pastebin")
    def _fn_create_pastebin_function(self, event, *args, **kwargs):
        """Function: Function that dumps any text/code to pastebin.com and returns a link to that paste"""
        try:
            # Get the function parameters:
            pastebin_code = kwargs.get("pastebin_code")  # text
            pastebin_name = kwargs.get("pastebin_name")  # text
            pastebin_format = kwargs.get("pastebin_format")  # text
            pastebin_privacy = kwargs.get("pastebin_privacy")  # number
            pastebin_expiration = kwargs.get("pastebin_expiration")  # text

            log = logging.getLogger(__name__)
            log.info("pastebin_code: %s", pastebin_code)
            log.info("pastebin_name: %s", pastebin_name)
            log.info("pastebin_format: %s", pastebin_format)
            log.info("pastebin_privacy: %s", pastebin_privacy)
            log.info("pastebin_expiration: %s", pastebin_expiration)

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