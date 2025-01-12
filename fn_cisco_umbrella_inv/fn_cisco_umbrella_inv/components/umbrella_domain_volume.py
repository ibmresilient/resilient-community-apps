# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.

""" SOAR functions component to run an Umbrella investigate Query - Domain Volume against
a Cisco Umbrella server """

# Set up:
# Destination: a Queue named "umbrella_investigate".
# Manual Action: Execute a REST query against a Cisco Umbrella server.
from datetime import datetime

from resilient_circuits import AppFunctionComponent, FunctionResult, app_function
from fn_cisco_umbrella_inv.util.helpers import process_params, PACKAGE_NAME,\
    investigateClient, URIs, get_time_input
from resilient_lib import validate_fields

FN_NAME = "umbrella_domain_volume"

class FunctionComponent(AppFunctionComponent):
    """Component that implements SOAR function 'umbrella_domain_volume' of package fn_cisco_umbrella_inv.

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

    The Investigate Query will execute a REST call against the Cisco Umbrella Investigate server and returns a result in
    JSON format similar to the following.

    The Investigate Query will execute a REST call against the Cisco Umbrella Investigate server and returns a result
    in JSON format similar to the following.
        {
        'domain_name': 'cisco.com',
        'query_execution_time': '2018-04-25 19:21:33'
        'domain_volume': { 'dates': [1524589200000, 1524679200000],
                           'dates_converted': ['2018-04-24 18:00:00', '2018-04-25 19:00:00']
                           'queries': [2610011, 2576588, 2518676, 2361999, 2161170, 1992158, 1835777, 1847458, 1809848,
                           1791200, 1784312, 1776649, 1830100, 1939211, 2023009, 2075916, 2042269, 2065889, 2137081,
                           2442077, 2618018, 2690130, 2726822, 2650116, 0, 0]},
        }
    """
    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """Function: SOAR Function: Cisco Umbrella Investigate for Domain Volume."""
        try:
            # Validate required input fields
            validate_fields(["umbinv_domain", "umbinv_match"], fn_inputs)
            # Get the function parameters:
            umbinv_domain = fn_inputs.umbinv_domain  # text
            umbinv_match = self.get_select_param(getattr(fn_inputs, "umbinv_match", None))  # select, values: "all", "component", "exact"
            umbinv_start_epoch = getattr(fn_inputs, "umbinv_start_epoch", None)  # datetimepicker
            umbinv_start_relative = getattr(fn_inputs, "umbinv_start_relative", None)  # text
            umbinv_stop_epoch = getattr(fn_inputs, "umbinv_stop_epoch", None)  # datetimepicker
            umbinv_stop_relative = getattr(fn_inputs, "umbinv_stop_relative", None)  # text

            self.LOG.info("umbinv_domain: %s", umbinv_domain)
            self.LOG.info("umbinv_match: %s", umbinv_match)
            self.LOG.info("umbinv_start_epoch: %s", umbinv_start_epoch)
            self.LOG.info("umbinv_start_relative: %s", umbinv_start_relative)
            self.LOG.info("umbinv_stop_epoch: %s", umbinv_stop_epoch)
            self.LOG.info("umbinv_stop_relative: %s", umbinv_stop_relative)

            yield self.status_message(f"Starting App Function: '{FN_NAME}'")
            domain = None
            process_result = {}
            params = {"domain": umbinv_domain.strip(), "start_epoch": umbinv_start_epoch, "match": str(umbinv_match),
                "start_relative": umbinv_start_relative, "stop_epoch": umbinv_stop_epoch,
                "stop_relative": umbinv_stop_relative }

            process_params(params, process_result)

            if "_domain" not in process_result:
                 raise ValueError("Parameter 'umbinv_domain' was not processed correctly")
            else:
                domain = process_result.pop("_domain")

            invClient = investigateClient(self.options, self.rc)

            yield self.status_message("Running Cisco Investigate query...")

            rtn = invClient.make_api_call("GET",
                                          URIs.get("domain_volume").format(domain),
                                          params={"start": get_time_input(umbinv_start_epoch),
                                                  "stop": get_time_input(umbinv_stop_epoch),
                                                  "match": str(umbinv_match)})
            dates_converted = []
            for d in rtn.get("dates"):
                try:
                    dates_converted.append(datetime.fromtimestamp(int(d)/1000).strftime('%Y-%m-%d %H:%M:%S'))
                except ValueError:
                    yield FunctionResult({}, success=False, reason='timestamp value incorrectly specified')

            rtn["dates_converted"] = dates_converted
            query_execution_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            results = {"domain_volume": rtn, "domain_name": domain,
                       "query_execution_time": query_execution_time}
            yield self.status_message(f"Returning 'domain_volume' results for domain '{domain}'.")

            yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as err:
            yield FunctionResult({}, success=False, reason=str(err))
