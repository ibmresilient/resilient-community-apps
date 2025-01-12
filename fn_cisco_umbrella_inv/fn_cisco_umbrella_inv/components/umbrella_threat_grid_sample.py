# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.

""" SOAR functions component to run an Umbrella investigate Query - Threat Grid Integration sample against a
Cisco Umbrella server """

# Set up:
# Destination: a Queue named "umbrella_investigate".
# Manual Action: Execute a REST query against a Cisco Umbrella server.import self.LOGging
from datetime import datetime

from resilient_circuits import AppFunctionComponent, FunctionResult, app_function
from fn_cisco_umbrella_inv.util.helpers import process_params, PACKAGE_NAME,\
    investigateClient, URIs
from resilient_lib import validate_fields

FN_NAME = "umbrella_threat_grid_sample"

class FunctionComponent(AppFunctionComponent):
    """Component that implements SOAR function 'umbrella_threat_grid_sample' of package fn_cisco_umbrella_inv.

    The Function does a Cisco Umbrella Investigate query lookup and takes the following parameters:
        umbinv_hash, umbinv_sample_endpoint, umbinv_limit, umbinv_offset

    An example of a set of query parameter might look like the following:
            umbinv_hash =  artifact.value
            umbinv_sample_endpoint = "basic"
            umbinv_limit = 5
            umbinv_offset = 0

    The Investigate Query will executes a REST call against the Cisco Umbrella Investigate server and returns a result
    in JSON format similar to the following.

        {'hash': '414e38ed0b5d507734361c2ba94f734252ca33b8259ca32334f32c4dba69b01c',
         'query_execution_time': '2018-05-01 12:23:19'},
         'sample_basic': {'magicType': 'PE32 executable (GUI) Intel 80386 (stripped to external PDB), for MS Windows',
                          'behaviors': [{'category': ['file'],
                                          'hits': 1,
                                          'severity': 90,
                                          'title': 'Process Modified a File in a System Directory',
                                          'tags': ['executable', 'file', 'process'],
                                          'confidence': 100,
                                          'threat': 90,
                                          'name': 'modified-file-in-system-dir'},
                                       ],
                          'sha1': '00bf659061121200c1e5469fbe31d100418b149e',
                          'size': 228864,
                          'threatScore': 100,
                          'connections': {'connections': [{'threatTypes': [],
                                                             'popularity1Month': None,
                                                             'name': '195.22.28.198',
                                                             'attacks': [],
                                                             'popularity3Month': None,
                                                             'popularity': None,
                                                             'firstQueried': None,
                                                             'popularityWeek': None,
                                                             'securityCategories': [],
                                                             'ips': [],
                                                             'lastCommit': None,
                                                             'urls': [], 'type': 'IP',
                                                             'firstSeen': 1460762759000,
                                                             'lastSeen': 1460762759000
                                                            },
                                                           ]
                                           'totalResults': 5,
                                           'limit': 5,
                                           'moreDataAvailable': True,
                                           'offset': 0
                                          },
                          'visible': True,
                          'lastSeen': 1460762759000,
                          'samples': {'totalResults': 0,
                                       'limit': 5,
                                       'moreDataAvailable': False,
                                       'samples': [], 'offset': 0
                                      },
                          'sha256': '414e38ed0b5d507734361c2ba94f734252ca33b8259ca32334f32c4dba69b01c',
                          'avresults': [],
                          'firstSeen': 1460762759000,
                          'md5': '6d8b70d20b1182546bc58ce7f90549d7'
                         }
        }
    """
    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """Function: SOAR Function: Cisco Umbrella Investigate for Threat Grid sample for an MD5, SHA1 or SHA256 hash."""
        try:
            # Validate required input fields
            validate_fields(["umbinv_hash", "umbinv_sample_endpoint"], fn_inputs)
            # Get the function parameters:
            umbinv_hash = fn_inputs.umbinv_hash  # text
            umbinv_sample_endpoint = self.get_select_param(getattr(fn_inputs, "umbinv_sample_endpoint", None))  # select, values: "basic", "artifacts", "connections", "samples", "behaviors"
            umbinv_limit = getattr(fn_inputs, "umbinv_limit", None)  # number
            umbinv_offset = getattr(fn_inputs, "umbinv_offset", None)  # number

            self.LOG.info("umbinv_hash: %s", umbinv_hash)
            self.LOG.info("umbinv_sample_endpoint: %s", umbinv_sample_endpoint)
            self.LOG.info("umbinv_limit: %s", umbinv_limit)
            self.LOG.info("umbinv_offset: %s", umbinv_offset)

            yield self.status_message(f"Starting App Function: '{FN_NAME}'")
            hash = None
            process_result = {}
            process_params({"hash": umbinv_hash.strip(), "sample_endpoint": umbinv_sample_endpoint,
                            "limit": umbinv_limit, "offset": umbinv_offset},
                           process_result)

            if "_hash" not in process_result:
               raise ValueError("Parameter 'umbinv_hash' was not processed correctly")
            else:
                hash = process_result.pop("_hash")

            invClient = investigateClient(self.options, self.rc)

            yield self.status_message("Running Cisco Investigate query...")
            uri, result_header = None, None
            if umbinv_sample_endpoint == "basic":
                uri = URIs.get("sample").format(hash)
                result_header = "sample_basic"
            elif umbinv_sample_endpoint == "artifacts":
                uri = URIs.get("sample_artifacts").format(hash)
                result_header = "sample_artifacts"
            elif umbinv_sample_endpoint == "connections":
                uri = URIs.get("sample_connections").format(hash)
                result_header = "sample_connections"
            elif umbinv_sample_endpoint == "samples":
                uri = URIs.get("sample_samples").format(hash)
                result_header = "sample_samples"
            elif umbinv_sample_endpoint == "behaviors":
                uri = URIs.get("sample_behaviors").format(hash)
                result_header = "sample_behaviors"
            else:
                raise ValueError("Incorrect value for parameter parameter 'umbinv_sample_endpoint'.")
            # Make api call to Cisco Umbrella Investigate
            if result_header == "sample_basic":
                rtn = invClient.make_api_call("GET", uri)
            else:
                rtn = invClient.make_api_call("GET", uri,
                    params={"limit": umbinv_limit, "offset": umbinv_offset})

            results = {}
            query_execution_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            if ("error" in rtn and len(rtn.get("error")) != 0):
                yield self.status_message(f"Umbrella Investigate returned error message '{rtn.get('error')}'.")
            else:
                # Add "query_execution_time" and "hash" key to result to facilitate post-processing.
                results = {result_header: rtn, "hash": hash,
                           "query_execution_time": query_execution_time}
                yield self.status_message(f"Returning '{result_header}' results for hash '{hash}'.")

            yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as err:
            yield FunctionResult({}, success=False, reason=str(err))
