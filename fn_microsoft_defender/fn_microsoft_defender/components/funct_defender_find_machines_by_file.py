# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# Copyright IBM Corp. 2010, 2020 - Confidential Information

"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload, validate_fields
from fn_microsoft_defender.lib.defender_common import DefenderAPI, convert_date, FILES_URL, PACKAGE_NAME

FUNCTION = "defender_find_machines_by_file"

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'defender_find_machines_by_file''"""

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
    def _defender_find_machines_by_file_function(self, event, *args, **kwargs):
        """Function: Find machines which match a given file hash"""
        try:
            yield StatusMessage("Starting 'defender_find_machines_by_file'")
            validate_fields(["tenant_id", "client_id", "app_secret"], self.options)
            validate_fields(["defender_indicator_value"], kwargs)

            # Get the function parameters:
            defender_indicator_value = kwargs.get("defender_indicator_value")  # text

            log = logging.getLogger(__name__)
            log.info(u"defender_indicator_value: %s", defender_indicator_value)

            # Get the function parameters:
            defender_api = DefenderAPI(self.options['tenant_id'],
                                       self.options['client_id'],
                                       self.options['app_secret'],
                                       self.opts,
                                       self.options)

            rp = ResultPayload(PACKAGE_NAME, **kwargs)
            url = FILES_URL.format(defender_indicator_value)
            machines_result, status, reason = defender_api.call(url, content_type=None)

            if not status:
                yield StatusMessage(u"{} failure. Status: {} Reason: {}".format(FUNCTION, status, reason))

            # convert dates to timestamps
            if status:
                yield StatusMessage("Machines found: {}".format(len(machines_result['value'])))
                for machine in machines_result['value']:
                    machine['firstSeen_ts'] = convert_date(machine['firstSeen'])
                    machine['lastSeen_ts'] = convert_date(machine['lastSeen'])

            results = rp.done(status, machines_result, reason=reason)

            yield StatusMessage("Finished 'defender_find_machines_by_file'")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
