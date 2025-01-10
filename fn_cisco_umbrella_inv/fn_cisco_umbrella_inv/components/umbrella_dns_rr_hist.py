# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.

""" SOAR functions component to run an Umbrella investigate Query - DNS RR History for an IP Address or domain
against a Cisco Umbrella server """

# Set up:
# Destination: a Queue named "umbrella_investigate".
# Manual Action: Execute a REST query against a Cisco Umbrella server.
from datetime import datetime

from resilient_circuits import AppFunctionComponent, FunctionResult, app_function
from resilient_lib import validate_fields
from fn_cisco_umbrella_inv.util.helpers import create_attachment, PACKAGE_NAME, investigateClient,\
    URIs, UNSUPPORTED_DNS_QUERY, SUPPORTED_DNS_TYPES, IP_PATTERN

FN_NAME = "umbrella_dns_rr_hist"

class FunctionComponent(AppFunctionComponent):
    """Component that implements SOAR function 'umbrella_dns_rr_hist' of package fn_cisco_umbrella_inv.
    This function can only be used with legacy version of Cisco Umbrella Investigate.

    The Function does a Cisco Umbrella Investigate query lookup takes the following parameters:
        resource, dns_type

    An example of a set of query parameter might look like the following:
            umbinv_resource = "1.2.3.4" or resource = "example.com"
            umbinv_dns_type = "A" or "CNAME" or "NS" or "MX"

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
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """Function: SOAR Function: Cisco Umbrella Investigate for DNS RR History for a IP, Type or Domain Name"""
        try:
            validate_fields(["umbinv_resource", "umbinv_dns_type", "incident_id", "artifact_type"], fn_inputs)
            # Get the function parameters:
            umbinv_resource = fn_inputs.umbinv_resource  # text
            umbinv_dns_type = fn_inputs.umbinv_dns_type  # select, values: "A", "NS", "MX", "TXT", "CNAME"
            incident_id = fn_inputs.incident_id  # number
            artifact_type = fn_inputs.artifact_type  # text

            self.LOG.info("umbinv_resource: %s", umbinv_resource)
            self.LOG.info("umbinv_dns_type: %s", umbinv_dns_type)
            self.LOG.info("incident_id: %s", incident_id)
            self.LOG.info("artifact_type: %s", artifact_type)

            yield self.status_message(f"Starting App Function: '{FN_NAME}'")

            params = {"resource": umbinv_resource.strip(), "dns_type": umbinv_dns_type, "incident_id": incident_id,
                "artifact_type": artifact_type}

            invClient = investigateClient(self.options, self.rc)

            yield self.status_message("Running Cisco Investigate query...")

            if umbinv_dns_type not in SUPPORTED_DNS_TYPES:
                raise UNSUPPORTED_DNS_QUERY
            # query the domain
            uri = URIs.get("ip_rr_history" if IP_PATTERN.match(umbinv_resource) else "domain_rr_history").format(umbinv_dns_type, umbinv_resource)
            rtn = invClient.make_api_call("GET", uri)

            results = {}
            query_execution_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            if ("rrs" in rtn and len(rtn.get("rrs")) == 0) or ("rrs_tf" in rtn and len(rtn.get("rrs_tf")) == 0):
                yield self.status_message(f"No Results returned for resource '{umbinv_resource}' with query type '{umbinv_dns_type}'.")
            elif ("rrs" in rtn and len(rtn.get("rrs")) > int(self.options.get("results_limit", "200"))) \
                    or ("rrs_tf" in rtn and len(rtn.get("rrs_tf")) > int(self.options.get("results_limit", "200"))):

                att_report = create_attachment(self, FN_NAME, umbinv_resource, params, rtn, query_execution_time)
                # Add in "query_execution_time" and "ip_address" to result to facilitate post-processing.
                results = {"over_limit": True, "resource_name": umbinv_resource, "att_name": att_report.get("name"),
                           "query_execution_time": query_execution_time}
                yield self.status_message(f"Returning 'dns_rr_history' results for resource '{umbinv_resource}' as attachment: {att_report.get('name')}.")
            else:
                # Add in "query_execution_time" and "ip_address" to result to facilitate post-processing.
                results = {"dns_rr_history": rtn, "resource_name": umbinv_resource,
                           "query_execution_time": query_execution_time}
                yield self.status_message(f"Returning 'dns_rr_history' results for resource '{umbinv_resource}'.")

            yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as err:
            yield FunctionResult({}, success=False, reason=str(err))
