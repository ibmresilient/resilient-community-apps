# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

""" Resilient functions component to run an Umbrella investigate Query - Domain Volume against
a Cisco Umbrella server """

# Set up:
# Destination: a Queue named "umbrella_investigate".
# Manual Action: Execute a REST query against a Cisco Umbrella server.
import json
import logging
from datetime import datetime

from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_cisco_umbrella_inv.util.resilient_inv import ResilientInv
from fn_cisco_umbrella_inv.util.helpers import validate_opts, validate_params, process_params, omit_params, \
    is_none

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'umbrella_domain_volume' of package fn_cisco_umbrella_inv.

    The Function does a Cisco Umbrella Investigate query lookup and takes the following parameters:
            umbinv_domain, umbinv_match, [umbinv_start_epoch or umbinv_start_relative], [umbinv_stop_epoch or \
            umbinv_stop_relative]

    An example of a set of query parameter might look like the following:

            umbinv_domain = artifact.value
            umbinv_start_epoch = None
            umbinv_start_relative = "-1days"
            umbinv_stop_epoch = None
            umbinv_stop_relative = "now"
            umbinv_match = "all"

    The Investigate Query will executs a REST call agaist the Cisco Umbrell Investigate server and returns a result in
    JSON format similar to the following.


    The Investigate Query will executs a REST call against the Cisco Umbrella Investigate server and returns a result
    in JSON format similar to the following.
        {
        'domain_name': 'cisco.com',
        'query_execution_time': '2018-04-25 19:21:33'
        'domain_volume': { u'dates': [1524589200000, 1524679200000],
                           u'dates_converted': [u'2018-04-24 18:00:00', u'2018-04-25 19:00:00']
                           u'queries': [2610011, 2576588, 2518676, 2361999, 2161170, 1992158, 1835777, 1847458, 1809848,
                           1791200, 1784312, 1776649, 1830100, 1939211, 2023009, 2075916, 2042269, 2065889, 2137081,
                           2442077, 2618018, 2690130, 2726822, 2650116, 0, 0]},
        }
    """
    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_cisco_umbrella_inv", {})
        validate_opts(self)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_cisco_umbrella_inv", {})
        validate_opts(self)

    @function("umbrella_domain_volume")
    def _umbrella_domain_volume_function(self, event, *args, **kwargs):
        """Function: Resilient Function : Cisco Umbrella Investigate for Domain Volume."""
        try:
            # Get the function parameters:
            umbinv_domain = kwargs.get("umbinv_domain")  # text
            umbinv_match = self.get_select_param(kwargs.get("umbinv_match"))  # select, values: "all", "component", "exact"
            umbinv_start_epoch = kwargs.get("umbinv_start_epoch")  # datetimepicker
            umbinv_start_relative = kwargs.get("umbinv_start_relative")  # text
            umbinv_stop_epoch = kwargs.get("umbinv_stop_epoch")  # datetimepicker
            umbinv_stop_relative = kwargs.get("umbinv_stop_relative")  # text

            log = logging.getLogger(__name__)
            log.info("umbinv_domain: %s", umbinv_domain)
            log.info("umbinv_match: %s", umbinv_match)
            log.info("umbinv_start_epoch: %s", umbinv_start_epoch)
            log.info("umbinv_start_relative: %s", umbinv_start_relative)
            log.info("umbinv_stop_epoch: %s", umbinv_stop_epoch)
            log.info("umbinv_stop_relative: %s", umbinv_stop_relative)

            if is_none(umbinv_domain):
                raise ValueError("Required parameter 'umbinv_domain' not set")

            if is_none(umbinv_match):
                raise ValueError("Required parameter 'umbinv_match' not set")

            yield StatusMessage("Starting...")
            domain = None
            process_result = {}
            params = {"domain": umbinv_domain.strip(), "start_epoch": umbinv_start_epoch, "match": str(umbinv_match),
                      "start_relative": umbinv_start_relative, "stop_epoch": umbinv_stop_epoch,
                      "stop_relative": umbinv_stop_relative }

            validate_params(params)
            process_params(params, process_result)

            if "_domain" not in process_result:
                 raise ValueError("Parameter 'umbinv_domain' was not processed correctly")
            else:
                domain = process_result.pop("_domain")

            api_token = self.options.get("api_token")
            base_url = self.options.get("base_url")
            rinv = ResilientInv(api_token, base_url)

            yield StatusMessage("Running Cisco Investigate query...")
            rtn = rinv.domain_volume(domain, **omit_params(params, ["domain"]))
            dates_converted = []
            for d in rtn["dates"]:
                try:
                    secs = int(d) / 1000
                    ts_readable = datetime.fromtimestamp(secs).strftime('%Y-%m-%d %H:%M:%S')
                    dates_converted.append(ts_readable)
                except ValueError:
                    yield FunctionError('timestamp value incorrectly specified')
            rtn["dates_converted"] = dates_converted
            query_execution_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            results = {"domain_volume": json.loads(json.dumps(rtn)), "domain_name": domain,
                       "query_execution_time": query_execution_time}
            yield StatusMessage("Returning 'domain_volume' results for domain '{}'.".format(domain))

            yield StatusMessage("Done...")

            log.debug(json.dumps(results))
            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            log.exception("Exception in Resilient Function.")
            yield FunctionError()