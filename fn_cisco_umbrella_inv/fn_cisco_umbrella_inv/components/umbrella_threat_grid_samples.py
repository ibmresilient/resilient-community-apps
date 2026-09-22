# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.

""" SOAR functions component to run an Umbrella investigate Query - Threat Grid Integration samples against a
Cisco Umbrella server """

# Set up:
# Destination: a Queue named "umbrella_investigate".
# Manual Action: Execute a REST query against a Cisco Umbrella server.import self.LOGging
from datetime import datetime

from resilient_circuits import AppFunctionComponent, FunctionResult, app_function
from fn_cisco_umbrella_inv.util.helpers import process_params, PACKAGE_NAME,\
    investigateClient, URIs
from resilient_lib import validate_fields

FN_NAME = "umbrella_threat_grid_samples"

class FunctionComponent(AppFunctionComponent):
    """Component that implements Resilient function 'umbrella_threat_grid_samples' of package fn_cisco_umbrella_inv.

    The Function does a Cisco Umbrella Investigate query lookup and takes the following parameters:
        umbinv_resource, umbinv_resource_type, umbinv_limit, umbinv_offset, umbinv_sortby

    An example of a set of query parameter might look like the following:
        umbinv_resource =  artifact.value
        umbinv_resource =  "domain"
        umbinv_limit = 5
        umbinv_sortby = "score"
        umbinv_offset = 0

    The Investigate Query will executes a REST call against the Cisco Umbrella Investigate server and returns a result
    in JSON format similar to the following.

        {'resource_name': 'cisco.com',
         'query_execution_time': '2018-04-30 15:30:42'
         'thread_grid_samples': {'limit': 2,
                                 'moreDataAvailable': True,
                                 'samples': [{'magicType': 'PE32 executable (GUI) Intel 80386, for MS Windows, UPX compressed',
                                               'behaviors': [],
                                               'sha1': 'ccdeb2319d6b924e359f563527404a0af3d1ac54',
                                               'size': 22020, 'threatScore': 100,
                                               'visible': False, 'lastSeen': 1518410873000,
                                               'sha256': '65f33f9e6d16918ba72bc20bcd85ebd75bc735df5666a843cab9c6dec9c0b1c1',
                                               'avresults': [{'product': 'ClamAV', 'signature': 'Win.Worm.Mydoom'}],
                                               'firstSeen': 1518410872000, 'md5': '0c340a220817e157346bef7976a0d0b6'},
                                             { 'magicType': 'PE32 executable (GUI) Intel 80386, for MS Windows, UPX compressed',
                                               'behaviors': [],
                                               'sha1': '971d92e80764812f0abca9ccf3075f5e9cc6fa4a',
                                               'size': 33616,
                                               'threatScore': 100,
                                               'visible': False,
                                               'lastSeen': 1503550227000,
                                               'sha256': 'eb19d33f6b157d814bef539e3625ab9d40b217271d7144e23b20effb677577b5',
                                               'avresults': [{'product': 'ClamAV', 'signature': 'Win.Worm.Mydoom'}],
                                               'firstSeen': 1503550227000, 'md5': '8d1bcddb2cbb143e2ade4622770f4849'}
                                             ],
                                 'offset': 0,
                                 'query': 'cisco.com', 'totalResults': 2
                               }
        }
    """
    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """Function: SOAR Function: Cisco Umbrella Investigate for Threat Grid samples for domain, IP or URL resource."""
        try:
            # Validate required input fields
            validate_fields(["umbinv_resource"], fn_inputs)
            # Get the function parameters:
            umbinv_resource = fn_inputs.umbinv_resource  # text
            umbinv_limit = getattr(fn_inputs, "umbinv_limit", None)  # number
            umbinv_offset = getattr(fn_inputs, "umbinv_offset", None)  # number
            umbinv_sortby = getattr(fn_inputs, "umbinv_sortby", None)  # text

            self.LOG.info("umbinv_resource: %s", umbinv_resource)
            self.LOG.info("umbinv_limit: %s", umbinv_limit)
            self.LOG.info("umbinv_offset: %s", umbinv_offset)
            self.LOG.info("umbinv_sortby: %s", umbinv_sortby)

            yield self.status_message(f"Starting App Function: '{FN_NAME}'")
            res, res_type = None, None
            process_result = {}
            process_params({"resource": umbinv_resource.strip(), "limit": umbinv_limit,
                            "sortby": umbinv_sortby, "offset": umbinv_offset},
                           process_result)

            if "_res" not in process_result or "_res_type" not in process_result:
                raise ValueError("Parameter 'umbinv_resource' was not processed correctly")
            else:
                res = process_result.pop("_res")
                res_type = process_result.pop("_res_type")

            if res_type != "domain_name" and res_type != "ip_address" and res_type != "url":
                raise ValueError(f"Parameter 'umbinv_resource' was an incorrect type '{res_type}', should be a 'domain name', "
                    "an 'ip address' or a 'url'.")

            invClient = investigateClient(self.options, self.rc)

            yield self.status_message("Running Cisco Investigate query...")
            rtn = invClient.make_api_call("GET",
                                     URIs.get("samples").format(res),
                                     params={'limit': umbinv_limit, 'offset': umbinv_offset, 'sortby': umbinv_sortby})

            results = {}
            if "error" in rtn:
                yield self.status_message(f"Investigate returned 'error' status: '{rtn.get('error')}'.")
            elif len(rtn) == 0 or ("samples" in rtn and len(rtn.get("samples")) == 0):
                yield self.status_message(f"No Results returned for resource '{res}'.")
            else:
                query_execution_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                # Make each sample 'firstSeen' and "lastSeen" property more readable.
                for i in range(len(rtn.get("samples"))):
                    fs = rtn.get("samples", [])[i].get("firstSeen", None)
                    ls = rtn.get("samples", [])[i].get("lastSeen", None)
                    try:
                        if fs:
                            fs_readable = datetime.fromtimestamp(int(fs)/1000).strftime('%Y-%m-%d %H:%M:%S')
                            rtn["samples"][i]["first_seen_converted"] = fs_readable
                        if ls:
                            ls_readable = datetime.fromtimestamp(int(ls)/1000).strftime('%Y-%m-%d %H:%M:%S')
                            rtn["samples"][i]["last_seen_converted"] = ls_readable
                    except ValueError:
                        yield FunctionResult({}, success=False, reason='Timestamp value incorrectly specified')

                # Add "query_execution_time" and "domains" key to result to facilitate post-processing.
                results = {"thread_grid_samples": rtn, "resource_name": umbinv_resource,
                           "query_execution_time": query_execution_time}
                yield self.status_message(f"Returning 'thread_grid_samples' results for resource '{res}'.")

            yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as err:
            yield FunctionResult({}, success=False, reason=str(err))
