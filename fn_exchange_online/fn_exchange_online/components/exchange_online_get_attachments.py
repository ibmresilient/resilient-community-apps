# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'exchange_online_get_attachments"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_exchange_online", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_exchange_online", {})

    @function("exchange_online_get_attachments")
    def _exchange_online_get_attachments_function(self, event, *args, **kwargs):
        """Function: Get the attachments of an Exchange Online email."""
        try:
            # Get the wf_instance_id of the workflow this Function was called in
            wf_instance_id = event.message["workflow_instance"]["workflow_instance_id"]

            # Get the function parameters:
            exo_email_address = kwargs.get("exo_email_address")  # text
            exo_messages_id = kwargs.get("exo_messages_id")  # text

            log = logging.getLogger(__name__)
            log.info("exo_email_address: %s", exo_email_address)
            log.info("exo_messages_id: %s", exo_messages_id)

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