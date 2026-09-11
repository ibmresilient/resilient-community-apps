# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.

""" SOAR functions component to run an Umbrella investigate Query - AS Information for a Domain against a
Cisco Umbrella server """

# Set up:
# Destination: a Queue named "umbrella_investigate".
# Manual Action: Execute a REST query against a Cisco Umbrella server.
from datetime import datetime

from resilient_circuits import AppFunctionComponent, FunctionResult, app_function
from fn_cisco_umbrella_inv.util.helpers import process_params, PACKAGE_NAME,\
    investigateClient, URIs, IP_PATTERN, IP_ERR
from resilient_lib import validate_fields

FN_NAME = "umbrella_ip_as_info"

class FunctionComponent(AppFunctionComponent):
    """Component that implements SOAR function 'umbrella_ip_as_info' of
    package fn_cisco_umbrella_inv.

    The Function does a Cisco Umbrella Investigate query lookup takes the following parameters:
        umbinv_resource

    An example of a set of query parameter might look like the following:
        umbinv_resource = 93.184.216.119 or umbinv_resource = "12345"

    The Investigate Query will executes a REST call against the Cisco Umbrella Investigate server and returns a result
    in JSON format similar to the following.

        {'ip_address': '93.184.216.119',
         'query_execution_time': '2018-04-26 11:09:12',
         'as_for_ip': [{'description': 'EDGECAST - MCI Communications Services, Inc. d/b/a Verizon Business, US 86400',
                        'cidr': '93.184.216.0/24',
                        'ir': 3,
                        'asn': 15133,
                        'creation_date': '2007-03-19'}
                      ]
        }

    Also for:
            umbinv_ipaddr = None
            umbinv_asn = 12345

        {'asn': '12345', 'query_execution_time': '2018-05-02 16:16:34'
         'prefixes_for_asn': [{'cidr': '212.47.32.0/19',
                               'geo': {'country_name': 'Italy', 'country_code': 'IT'}}],
        }
    """
    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """Function: SOAR Function: Cisco Umbrella Investigate for ASA information for an IP address."""
        try:
            # Validate required input fields
            validate_fields(["umbinv_resource"], fn_inputs)
            # Get the function parameters:
            umbinv_resource = fn_inputs.umbinv_resource  # text
            self.LOG.info("umbinv_resource: %s", umbinv_resource)

            yield self.status_message(f"Starting App Function: '{FN_NAME}'")
            res, res_type = None, None
            process_result = {}
            process_params({"resource": umbinv_resource.strip()}, process_result)

            if "_res" not in process_result or "_res_type" not in process_result:
                raise ValueError("Parameter 'umbinv_resource' was not processed correctly")
            else:
                res = process_result.pop("_res")
                res_type = process_result.pop("_res_type")

            invClient = investigateClient(self.options, self.rc)

            yield self.status_message("Running Cisco Investigate query...")
            query_execution_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            if res_type == "ip_address":
                if not IP_PATTERN.match(res):
                    raise IP_ERR
                rtn = invClient.make_api_call("GET", URIs.get("as_for_ip").format(res))
                # Add "query_execution_time" and "ip_address" key to result to facilitate post-processing.
                results = {"as_for_ip": rtn, "ip_address": res,
                           "query_execution_time": query_execution_time}
                yield self.status_message(f"Returning 'as_for_ip' results for ip address '{res}'.")

            elif res_type == "as_number":
                rtn = invClient.make_api_call("GET", URIs.get("prefixes_for_asn").format(res))
                # Add "query_execution_time" and "ip_address" key to result to facilitate post-processing.
                results = {"prefixes_for_asn": rtn, "asn": res,
                           "query_execution_time": query_execution_time}
                yield self.status_message(f"Returning 'prefixes_for_asn' results for AS number '{res}'.")
            else:
                raise ValueError(f"Parameter 'umbinv_resource' was an incorrect type '{res_type}' should be an 'ip address' "
                    "or an 'AS number'")

            yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as err:
            yield FunctionResult({}, success=False, reason=str(err))
