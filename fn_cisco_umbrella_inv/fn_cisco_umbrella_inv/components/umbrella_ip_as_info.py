# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

""" Resilient functions component to run an Umbrella investigate Query - AS Information for a Domain against a
Cisco Umbrella server """

# Set up:
# Destination: a Queue named "umbrella_investigate".
# Manual Action: Execute a REST query against a Cisco Umbrella server.
import json
import logging
from datetime import datetime

from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_cisco_umbrella_inv.util.resilient_inv import ResilientInv
from fn_cisco_umbrella_inv.util.helpers import validate_opts, validate_params, process_params, is_none

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'umbrella_ip_as_info' of
    package fn_cisco_umbrella_inv.

    The Function does a Cisco Umbrella Investigate query lookup takes the following parameters:
        umbinv_resource

    An example of a set of query parameter might look like the following:

            umbinv_resource = 93.184.216.119 or umbinv_resource = "12345"


    The Investigate Query will executes a REST call against the Cisco Umbrella Investigate server and returns a result
    in JSON format similar to the following.

        {'ip_address': '93.184.216.119',
         'query_execution_time': '2018-04-26 11:09:12',
         'as_for_ip': [{u'description': u'EDGECAST - MCI Communications Services, Inc. d/b/a Verizon Business, US 86400',
                        u'cidr': u'93.184.216.0/24',
                        u'ir': 3,
                        u'asn': 15133,
                        u'creation_date': u'2007-03-19'}
                      ]
        }

    Also for:

            umbinv_ipaddr = None
            umbinv_asn = 12345

        {'asn': '12345', 'query_execution_time': '2018-05-02 16:16:34'
         'prefixes_for_asn': [{u'cidr': u'212.47.32.0/19',
                               u'geo': {u'country_name': u'Italy', u'country_code': u'IT'}}],
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

    @function("umbrella_ip_as_info")
    def _umbrella_ip_as_info_function(self, event, *args, **kwargs):
        """Function: Resilient Function : Cisco Umbrella Investigate for ASA information for an IP address."""
        try:
            # Get the function parameters:
            umbinv_resource = kwargs.get("umbinv_resource")  # text

            log = logging.getLogger(__name__)
            log.info("umbinv_resource: %s", umbinv_resource)

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

            api_token = self.options.get("api_token")
            base_url = self.options.get("base_url")
            rinv = ResilientInv(api_token, base_url)

            yield StatusMessage("Running Cisco Investigate query...")
            if res_type == "ip_address":
                rtn = rinv.as_for_ip(res)
                # Add "query_execution_time" and "ip_address" key to result to facilitate post-processing.
                query_execution_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                results = {"as_for_ip": json.loads(json.dumps(rtn)), "ip_address": res,
                           "query_execution_time": query_execution_time}
                yield StatusMessage("Returning 'as_for_ip' results for ip address '{}'.".format(res))

            elif res_type == "as_number":
                rtn = rinv.prefixes_for_asn(res)
                # Add "query_execution_time" and "ip_address" key to result to facilitate post-processing.
                query_execution_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                results = {"prefixes_for_asn": json.loads(json.dumps(rtn)), "asn": res,
                           "query_execution_time": query_execution_time}
                yield StatusMessage("Returning 'prefixes_for_asn' results for AS number '{}'.".format(res))
            else:
                raise ValueError("Parameter 'umbinv_resource' was an incorrect type '{}' should be an 'ip address' "
                                 "or an 'AS number'".format(res_type))

            yield StatusMessage("Done...")

            log.debug(json.dumps(results))
            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            log.exception("Exception in Resilient Function.")
            yield FunctionError()