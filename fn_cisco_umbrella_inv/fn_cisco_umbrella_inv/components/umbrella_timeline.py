# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.

""" SOAR functions component to run an Umbrella investigate Query - Timeline against a Cisco Umbrella server """

# Set up:
# Destination: a Queue named "umbrella_investigate".
# Manual Action: Execute a REST query against a Cisco Umbrella server.
from datetime import datetime

from resilient_circuits import AppFunctionComponent, FunctionResult, app_function
from fn_cisco_umbrella_inv.util.helpers import process_params, PACKAGE_NAME,\
    investigateClient, URIs
from resilient_lib import validate_fields

FN_NAME = "umbrella_timeline"

class FunctionComponent(AppFunctionComponent):
    """Component that implements SOAR function 'umbrella_timeline' of
    package fn_cisco_umbrella_inv.

    The Function does a Cisco Umbrella Investigate query lookup takes the following parameters:
        umbinv_resource

    An example of a set of query parameter might look like the following:
        umbinv_resource = "example.com" or umbinv_resource = "http://domain.org/index.html"

    The Investigate Query will execute a REST call against the Cisco Umbrella Investigate server and returns a result in
    JSON format similar to the following.

        {'resource_name': 'googlevideo.com'
         'query_execution_time': '2018-05-02 17:30:44',
         'timeline': [{'threatTypes': [],
                       'timestamp_converted': '2017-06-14 23:21:34',
                       'attacks': [],
                       'timestamp': 1497478894605,
                       'categories': []}
                     ]
        }
    """
    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """Function: SOAR Function: Cisco Umbrella Investigate Investigate for Timeline."""
        try:
            # Validate required input fields
            validate_fields(["umbinv_resource"], fn_inputs)
            # Get the function parameters:
            umbinv_resource = fn_inputs.umbinv_resource  # text
            self.LOG.info("resource: %s", umbinv_resource)

            yield self.status_message(f"Starting App Function: '{FN_NAME}'")
            res, res_type = None, None
            process_result = {}
            process_params({"resource": umbinv_resource.strip()}, process_result)

            if "_res" not in process_result or "_res_type" not in process_result:
                raise ValueError("Parameter 'umbinv_resource' was not processed correctly")
            else:
                res = process_result.pop("_res")
                res_type = process_result.pop("_res_type")

            if res_type not in ["domain_name", "ip_address", "url"]:
                raise ValueError(f"Parameter 'umbinv_resource' was an incorrect type '{res_type}', should be a 'domain name', "
                                 "an 'ip address' or a 'url'.")

            invClient = investigateClient(self.options, self.rc)

            yield self.status_message("Running Cisco Investigate query...")
            rtn = invClient.make_api_call("GET", URIs.get("timeline").format(res))

            results = {}
            query_execution_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            if len(rtn) == 0:
                yield self.status_message(f"No Results returned for resource '{res}'.")
            else:
                # Make timestamp more readable
                for x in range(len(rtn)):
                    try:
                        ts_readable = datetime.fromtimestamp(int(rtn[x]['timestamp'])/1000).strftime('%Y-%m-%d %H:%M:%S')
                        rtn[x]['timestamp_converted'] = ts_readable
                    except ValueError:
                        yield FunctionResult({}, success=False, reason='timestamp value incorrectly specified')
                # Add  "query_execution_time" to result to facilitate post-processing.
                results = {"timeline": rtn, "resource_name": res,
                           "query_execution_time": query_execution_time}
                yield self.status_message(f"Returning 'thread_grid_samples' results for resource '{res}'.")

            yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as err:
            yield FunctionResult({}, success=False, reason=str(err))
