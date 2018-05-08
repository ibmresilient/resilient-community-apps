# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

""" Resilient functions component to run an Umbrella investigate Query - Timeline against a Cisco Umbrella server """

# Set up:
# Destination: a Queue named "umbrella_investigate".
# Manual Action: Execute a REST query against a Cisco Umbrella server.
import logging
import json
from datetime import datetime, time

from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_cisco_umbrella_inv.util.resilient_inv import ResilientInv
from fn_cisco_umbrella_inv.util.helpers import init_env, validate_opts, validate_params, process_params, is_none

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'umbrella_dns_rr_hist' of
    package fn_cisco_umbrella_inv.

    The Function does a Cisco Umbrella Investigate query lookup takes the following parameters:
        umbinv_resource

    An example of a set of query parameter might look like the following:

            umbinv_resource = "example.com" or umbinv_resource = "http://domain.org/index.html"

    The Investigate Query will executs a REST call agaist the Cisco Umbrell Investigate server and returns a result in
    JSON format similar to the following.


       'timeline':[
          {
             u'threatTypes':[

             ],
             'source':u'googlevideo.com',
             u'attacks':[

             ],
             u'timestamp':1497478894605,
             'timestamp_converted':'2017-06-14 23:21:34',
             u'categories':[

             ]
          }
       ]


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
            init_env(self)

            self._params = {"resource": umbinv_resource.strip()}

            validate_params(self)
            process_params(self)

            if not hasattr(self, '_res'):
               raise ValueError("Parameter 'umbinv_resource' was not processed correctly")

            api_token = self.options.get("api_token")
            base_url = self.options.get("base_url")
            rinv = ResilientInv(api_token,base_url)

            yield StatusMessage("Running Cisco Investigate query...")
            rtn = rinv.timeline(self._res)
            query_execution_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            if len(rtn) == 0:
                log.debug(json.dumps(rtn))
                yield StatusMessage("No Results returned for resource '{}'.".format(self._res))
                results = {}
            else:
                # Make timestamp more readable
                for x in range(len(rtn)):
                    try:
                        rtn[x]['source'] = umbinv_resource
                        secs = int(rtn[x]['timestamp']) / 1000
                        ts_readable = datetime.fromtimestamp(secs).strftime('%Y-%m-%d %H:%M:%S')
                        rtn[x]['timestamp_converted'] = ts_readable
                    except ValueError:
                        yield FunctionError('timestamp value incorrectly specified')
                # Add  "query_execution_time" to result to facilitate post-processing.
                results = {"timeline": json.loads(json.dumps(rtn)), "query_execution_time": query_execution_time}
            yield StatusMessage("done...")

            log.debug(json.dumps(results))
            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            logging.exception("Exception in Resilient Function.")
            yield FunctionError()