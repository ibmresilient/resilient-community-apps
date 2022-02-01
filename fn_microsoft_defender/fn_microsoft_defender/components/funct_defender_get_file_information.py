# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# Copyright IBM Corp. 2010, 2020 - Confidential Information

"""AppFunction implementation"""

import logging
from resilient_circuits import ResilientComponent, function, FunctionResult, FunctionError, StatusMessage
from resilient_lib import ResultPayload, validate_fields
from fn_microsoft_defender.lib.defender_common import DefenderAPI, FILES_URL, PACKAGE_NAME

FN_NAME = "defender_get_file_information"


class FunctionComponent(ResilientComponent):
    """Component that implements function 'defender_get_file_information'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get(PACKAGE_NAME, {})

    @function(FN_NAME)
    def _defender_find_machines_by_file_function(self, event, *args, **kwargs):
        """
        Function: None
        Inputs:
            -   fn_inputs.defender_file_hash
        """
        try:
            yield StatusMessage("Starting '{}'".format(FN_NAME))
            validate_fields(["tenant_id", "client_id", "app_secret"], self.options)
            validate_fields(["defender_file_hash"], kwargs)

            # Get the function parameters:
            defender_file_hash = kwargs.get("defender_file_hash")  # text

            log = logging.getLogger(__name__)
            log.info(u"defender_file_hash: %s", defender_file_hash)

            # Get the function parameters:
            defender_api = DefenderAPI(self.options['tenant_id'],
                                        self.options['client_id'],
                                        self.options['app_secret'],
                                        self.opts,
                                        self.options)

            rp = ResultPayload(PACKAGE_NAME, **kwargs)
            url = FILES_URL.format(defender_file_hash)
            file_result, status, reason = defender_api.call(url, content_type=None)

            if not status:
                yield StatusMessage(u"{} failure. Status: {} Reason: {}".format(FN_NAME, status, reason))

            results = rp.done(status, file_result, reason=reason)

            yield StatusMessage("Finished '{}'".format(FN_NAME))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()