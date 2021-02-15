# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.

"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload, validate_fields, readable_datetime
from fn_microsoft_defender.lib.defender_common import DefenderAPI, convert_date, MACHINES_URL, PACKAGE_NAME

FUNCTION = "defender_find_machines"

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'defender_find_machines''"""

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
    def _defender_find_machines_function(self, event, *args, **kwargs):
        """Function: Find Defender Machine(s) by IP address"""
        try:
            yield StatusMessage("Starting 'defender_find_machines'")
            validate_fields(["tenant_id", "client_id", "app_secret"], self.options)
            validate_fields(["defender_indicator_value", "defender_lookback_timeframe"], kwargs)

            # Get the function parameters:
            defender_lookback_timeframe = kwargs.get("defender_lookback_timeframe")  # datepicker
            defender_indicator_value = kwargs.get("defender_indicator_value")  # text

            log = logging.getLogger(__name__)
            log.info("defender_lookback_timeframe: %s", defender_lookback_timeframe)
            log.info("defender_indicator_value: %s", defender_indicator_value)

            # GET /api/machines/findbyip(ip='{IP}',timestamp={TimeStamp})
            timestamp_str = readable_datetime(defender_lookback_timeframe)
            query = "findbyip(ip='{}',timestamp={})".format(defender_indicator_value, timestamp_str)
            url = "/".join([MACHINES_URL, query])

            # Get the function parameters:
            log = logging.getLogger(__name__)
            defender_api = DefenderAPI(self.options['tenant_id'],
                                       self.options['client_id'],
                                       self.options['app_secret'],
                                       self.opts,
                                       self.options)

            rp = ResultPayload(PACKAGE_NAME, **kwargs)
            machines_result, status, reason = defender_api.call(url, content_type=None)

            # convert the timestamp
            if status:
                yield StatusMessage("Machines found: {}".format(len(machines_result['value'])))
                for machine in machines_result['value']:
                    machine['firstSeen_ts'] = convert_date(machine['firstSeen'])
            else:
                yield StatusMessage(u"{} failure. Status: {} Reason: {}".format(FUNCTION, status, reason))

            yield StatusMessage("Finished 'defender_find_machines'")

            results = rp.done(status, machines_result, reason=reason)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
