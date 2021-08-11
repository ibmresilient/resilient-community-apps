# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.

"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload, validate_fields
from fn_microsoft_defender.lib.defender_common import DefenderAPI, convert_date, MACHINES_URL, PACKAGE_NAME, make_filter_url

FUNCTION = "defender_find_machines_by_filter"

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'defender_find_machines_by_filter''"""

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
        """Function: Find Defender Machine(s) by filter"""
        try:
            yield StatusMessage("Starting 'defender_find_machines_by_filter'")
            validate_fields(["tenant_id", "client_id", "app_secret"], self.options)
            validate_fields(["defender_filter_name", "defender_filter_value"], kwargs)

            # Get the function parameters:
            defender_filter_name = kwargs.get("defender_filter_name")  # datepicker
            defender_filter_value = kwargs.get("defender_filter_value")  # text

            log = logging.getLogger(__name__)
            log.info("defender_filter_name: %s", defender_filter_name)
            log.info("defender_filter_value: %s", defender_filter_value)

            # HTTP GET  https://api.securitycenter.microsoft.com/api/machines?$filter=startswith(computerDnsName,'mymachine')
            # GET /api/machines/findbyip(ip='{IP}',timestamp={TimeStamp})
            url = make_filter_url(MACHINES_URL, defender_filter_name, defender_filter_value)

            # Get the function parameters:
            log = logging.getLogger(__name__)
            defender_api = DefenderAPI(self.options['tenant_id'],
                                       self.options['client_id'],
                                       self.options['app_secret'],
                                       self.opts,
                                       self.options)

            rp = ResultPayload(PACKAGE_NAME, **kwargs)
            machines_result, status, reason = defender_api.call(url)

            # convert the timestamp
            if status:
                yield StatusMessage("Machines found: {}".format(len(machines_result['value'])))
                for machine in machines_result['value']:
                    machine['firstSeen_ts'] = convert_date(machine['firstSeen'])
                    machine['lastSeen_ts'] = convert_date(machine['lastSeen'])
            else:
                yield StatusMessage(u"{} failure. Status: {} Reason: {}".format(FUNCTION, status, reason))

            yield StatusMessage("Finished 'defender_find_machines_by_filter'")

            results = rp.done(status, machines_result, reason=reason)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
