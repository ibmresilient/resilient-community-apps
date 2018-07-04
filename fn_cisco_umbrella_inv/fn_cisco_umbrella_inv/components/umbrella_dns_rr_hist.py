# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

""" Resilient functions component to run an Umbrella investigate Query - DNS RR History for an IP Address or domain
against a Cisco Umbrella server """

# Set up:
# Destination: a Queue named "umbrella_investigate".
# Manual Action: Execute a REST query against a Cisco Umbrella server.

import json
import logging
from datetime import datetime

from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_cisco_umbrella_inv.util.resilient_inv import ResilientInv
from fn_cisco_umbrella_inv.util.helpers import validate_opts, validate_params, process_params, is_none, \
    create_attachment


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'umbrella_dns_rr_hist' of
    package fn_cisco_umbrella_inv.

    The Function does a Cisco Umbrella Investigate query lookup takes the following parameters:
        resource , dns_type

    An example of a set of query parameter might look like the following:

            umbinv_resource = "1.2.3.4" or resource = "example.com"
            umbinv_dns_type = "A"

    The Investigate Query will executes a REST call against the Cisco Umbrella Investigate server and returns a result
    in JSON format similar to the following.

        {'resource_name': 'cosmos.furnipict.com',
         'query_execution_time': '2018-05-02 16:03:15',
         "dns_rr_history": {  "rrs": [  {
                                  "rr": "www.example.com.",
                                  "ttl": 86400,
                                  "class": "IN",
                                  "type": "A",
                                  "name": "93.184.216.119"
                                }
                                ...
                                ...
                              ],
                              "features": {
                                "rr_count": 19,
                                "ld2_count": 10,
                                "ld3_count": 14,
                                "ld2_1_count": 7,
                                "ld2_2_count": 11,
                                "div_ld2": 0.5263157894736842,
                                "div_ld3": 0.7368421052631579,
                                "div_ld2_1": 0.3684210526315789,
                                "div_ld2_2": 0.5789473684210527
                              }
                        }
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

    @function("umbrella_dns_rr_hist")
    def _umbrella_dns_rr_hist_function(self, event, *args, **kwargs):
        """Function: Resilient Function : Cisco Umbrella Investigate for DNS RR History for a IP, Type and Domain Name"""
        try:
            # Get the function parameters:
            umbinv_resource = kwargs.get("umbinv_resource")  # text
            umbinv_dns_type = self.get_select_param(kwargs.get("umbinv_dns_type"))  # select, values: "A", "NS", "MX", "TXT", "CNAME"
            incident_id = kwargs.get("incident_id")  # number
            artifact_type = kwargs.get("artifact_type")  # text

            log = logging.getLogger(__name__)
            log.info("umbinv_resource: %s", umbinv_resource)
            log.info("umbinv_dns_type: %s", umbinv_dns_type)
            log.info("incident_id: %s", incident_id)
            log.info("artifact_type: %s", artifact_type)

            if is_none(umbinv_resource):
                raise ValueError("Required parameter 'umbinv_resource' not set")

            if is_none(umbinv_dns_type):
                raise ValueError("Required parameter 'umbinv_dns_type' not set")

            if is_none(incident_id):
                raise ValueError("Required parameter 'incident_id' not set")

            if is_none(artifact_type):
                raise ValueError("Required parameter 'artifa7ct_type' not set")

            yield StatusMessage("Starting...")
            res = None
            res_type = None
            process_result = {}
            func_name = event.name

            params = {"resource": umbinv_resource.strip(), "dns_type": umbinv_dns_type, "incident_id": incident_id,
                      "artifact_type": artifact_type}

            validate_params(params)
            process_params(params, process_result)

            if "_res" not in process_result or "_res_type" not in process_result:
                raise ValueError("Parameter 'umbinv_resource' was not processed correctly")
            else:
                res = process_result.pop("_res")
                res_type = process_result.pop("_res_type")

            if res_type != "domain_name" and res_type != "ip_address":
                raise ValueError("Parameter 'umbinv_resource' was an incorrect type '{}', should be a 'domain name', "
                                 "or an 'ip address'.".format(res_type))

            api_token = self.options.get("api_token")
            base_url = self.options.get("base_url")
            rinv = ResilientInv(api_token, base_url)

            yield StatusMessage("Running Cisco Investigate query...")
            rtn = rinv.rr_history(res, query_type=umbinv_dns_type)
            query_execution_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            if ("rrs" in rtn and len(rtn["rrs"]) == 0) \
                    or ("rrs_tf" in rtn and len(rtn["rrs_tf"]) == 0):
                log.debug(json.dumps(rtn))
                yield StatusMessage("No Results returned for resource '{}' with query type '{}'."
                                    .format(res, umbinv_dns_type))
                results = {}
            elif ("rrs" in rtn and len(rtn["rrs"]) > int(self.options.get("results_limit", "200"))) \
                    or ("rrs_tf" in rtn and len(rtn["rrs_tf"]) > int(self.options.get("results_limit", "200"))):

                att_report = create_attachment(self, func_name, res, params, rtn, query_execution_time)
                # Add in "query_execution_time" and "ip_address" to result to facilitate post-processing.
                results = {"over_limit": True, "resource_name": res, "att_name": att_report["name"],
                           "query_execution_time": query_execution_time}
                yield StatusMessage("Returning 'dns_rr_history' results for resource '{0}' as attachment: {1} ."
                                    .format(res,att_report["name"]))
            else:
                # Add in "query_execution_time" and "ip_address" to result to facilitate post-processing.
                results = {"dns_rr_history": json.loads(json.dumps(rtn)), "resource_name": res,
                           "query_execution_time": query_execution_time}
                yield StatusMessage("Returning 'dns_rr_history' results for resource '{}'.".format(res))

            yield StatusMessage("Done...")

            log.debug(json.dumps(results))
            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            log.exception("Exception in Resilient Function.")
            yield FunctionError()