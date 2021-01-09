# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload, validate_fields
from fn_microsoft_defender.lib.defender_common import DefenderAPI, MACHINES_URL, PACKAGE_NAME

FUNCTION = "defender_quarantine_file"

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'defender_quarantine_file''"""

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
    def _defender_quarantine_file_function(self, event, *args, **kwargs):
        """Function: Quarantine a SHA-1 File"""
        try:
            yield StatusMessage("Starting 'defender_quarantine_file'")
            validate_fields(["tenant_id", "client_id", "app_secret"], self.options)
            validate_fields(["defender_machine_id",
                             "defender_description",
                             "defender_indicator_value"], kwargs)

            # Get the function parameters:
            defender_description = kwargs.get("defender_description")  # text
            defender_machine_id = kwargs.get("defender_machine_id")  # text
            defender_indicator_value = kwargs.get("defender_indicator_value")  # text

            log = logging.getLogger(__name__)
            log.info("defender_description: %s", defender_description)
            log.info("defender_machine_id: %s", defender_machine_id)
            log.info("defender_indicator_value: %s", defender_indicator_value)

            defender_api = DefenderAPI(self.options['tenant_id'],
                                       self.options['client_id'],
                                       self.options['app_secret'],
                                       self.opts,
                                       self.options)

            rp = ResultPayload(PACKAGE_NAME, **kwargs)

            payload = {
                "Sha1": defender_indicator_value,
                "Comment": defender_description
            }
            log.debug(payload)

            # build the url
            url = "/".join([MACHINES_URL, defender_machine_id, "StopAndQuarantineFile"])
            file_result, status, reason = defender_api.call(url, payload=payload, oper="POST")

            if not status:
                yield StatusMessage(u"{} failure. Status: {} Reason: {}".format(FUNCTION, status, reason))

            results = rp.done(status, file_result, reason=reason)

            yield StatusMessage("Finished 'defender_quarantine_file'")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
