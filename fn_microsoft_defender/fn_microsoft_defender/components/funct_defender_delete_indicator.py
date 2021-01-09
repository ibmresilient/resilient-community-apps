# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload, validate_fields
from fn_microsoft_defender.lib.defender_common import DefenderAPI, INDICATOR_URL, PACKAGE_NAME

FUNCTION = "defender_delete_indicator"


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'defender_delete_indicator''"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.opts = opts
        self.options = opts.get(PACKAGE_NAME, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.opts = opts
        self.options = opts.get(PACKAGE_NAME, {})

    @function(FUNCTION)
    def _defender_delete_indicator_function(self, event, *args, **kwargs):
        """Function: None"""
        try:
            yield StatusMessage("Starting 'defender_delete_indicator'")
            validate_fields(["tenant_id", "client_id", "app_secret"], self.options)
            validate_fields(["defender_indicator_id"], kwargs)

            # Get the function parameters:
            defender_indicator_id = kwargs.get("defender_indicator_id")  # text

            log = logging.getLogger(__name__)
            log.info("defender_indicator_id: %s", defender_indicator_id)

            defender_api = DefenderAPI(self.options['tenant_id'],
                                       self.options['client_id'],
                                       self.options['app_secret'],
                                       self.opts,
                                       self.options)

            rp = ResultPayload(PACKAGE_NAME, **kwargs)

            url = "/".join([INDICATOR_URL, defender_indicator_id])

            indicator_payload, status, reason = defender_api.call(url, oper="DELETE")

            if not status:
                yield StatusMessage("{} failure. Status: {} Reason: {}".format(FUNCTION, status, reason))

            yield StatusMessage("Finished 'defender_list_indicators'")

            results = rp.done(status, indicator_payload, reason=reason)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
