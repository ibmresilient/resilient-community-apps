# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

""" Resilient functions component to run an Umbrella investigate Query - Timeline against a Cisco Umbrella server """

# Set up:
# Destination: a Queue named "umbrella_investigate".
# Manual Action: Execute a REST query against a Cisco Umbrella server.
import logging
import json
from datetime import datetime

from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_cisco_umbrella_inv.util.resilient_inv import ResilientInv
from fn_cisco_umbrella_inv.util.helpers import validate_opts, validate_params, process_params, is_none

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'umbrella_dns_rr_hist' of
    package fn_cisco_umbrella_inv.

    The Function does a Cisco Umbrella Investigate query lookup takes the following parameters:
        umbinv_resource

    An example of a set of query parameter might look like the following:

            umbinv_resource = "example.com" or umbinv_resource = "http://domain.org/index.html"

    The Investigate Query will executs a REST call agaist the Cisco Umbrell Investigate server and returns a result in
    JSON format similar to the following.


        {'resource_name': 'googlevideo.com'
         'query_execution_time': '2018-05-02 17:30:44',
         'timeline': [{u'threatTypes': [],
                       u'timestamp_converted': u'2017-06-14 23:21:34',
                       u'attacks': [],
                       u'timestamp': 1497478894605,
                       u'categories': []}
                     ]
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

    @function("umbrella_timeline")
    def _umbrella_timeline_function(self, event, *args, **kwargs):
        """Function: Resilient Function : Cisco Umbrella Investigate Investigate for  Timeline."""
        try:
            # Get the function parameters:
            umbinv_resource = kwargs.get("umbinv_resource")  # text

            log = logging.getLogger(__name__)

            log.info("resource: %s", umbinv_resource)

            if is_none(umbinv_resource):
                raise ValueError("Required parameter 'umbinv_resource' not set")

            yield StatusMessage("Starting...")
            res = None
            res_type = None
            process_result = {}
            params = {"resource": umbinv_resource.strip()}

            validate_params(params)
            process_params(params, process_result)

            if "_res" not in process_result or "_res_type" not in process_result:
                raise ValueError("Parameter 'umbinv_resource' was not processed correctly")
            else:
                res = process_result.pop("_res")
                res_type = process_result.pop("_res_type")

            if res_type != "domain_name" and res_type != "ip_address" and res_type != "url":
                raise ValueError("Parameter 'umbinv_resource' was an incorrect type '{}', should be a 'domain name', "
                                 "an 'ip address' or a 'url'.".format(res_type))

            api_token = self.options.get("api_token")
            base_url = self.options.get("base_url")
            rinv = ResilientInv(api_token, base_url)

            yield StatusMessage("Running Cisco Investigate query...")
            rtn = rinv.timeline(res)
            query_execution_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            if len(rtn) == 0:
                log.debug(json.dumps(rtn))
                yield StatusMessage("No Results returned for resource '{}'.".format(res))
                results = {}
            else:
                # Make timestamp more readable
                for x in range(len(rtn)):
                    try:
                        secs = int(rtn[x]['timestamp']) / 1000
                        ts_readable = datetime.fromtimestamp(secs).strftime('%Y-%m-%d %H:%M:%S')
                        rtn[x]['timestamp_converted'] = ts_readable
                    except ValueError:
                        yield FunctionError('timestamp value incorrectly specified')
                # Add  "query_execution_time" to result to facilitate post-processing.
                results = {"timeline": json.loads(json.dumps(rtn)), "resource_name": res,
                           "query_execution_time": query_execution_time}
                yield StatusMessage("Returning 'thread_grid_samples' results for resource '{}'.".format(res))

            yield StatusMessage("done...")

            log.debug(json.dumps(results))
            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            log.exception("Exception in Resilient Function.")
            yield FunctionError()