# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

""" Resilient functions component to run an Umbrella investigate Query - Threat Grid Integration sample against a
Cisco Umbrella server """

# Set up:
# Destination: a Queue named "umbrella_investigate".
# Manual Action: Execute a REST query against a Cisco Umbrella server.import logging
import logging
import json
from datetime import datetime

from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_cisco_umbrella_inv.util.resilient_inv import ResilientInv
from fn_cisco_umbrella_inv.util.helpers import validate_opts, validate_params, process_params, omit_params, \
    is_none


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'umbrella_threat_grid_sample' of package fn_cisco_umbrella_inv.

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
         'sample_basic': {u'magicType': u'PE32 executable (GUI) Intel 80386 (stripped to external PDB), for MS Windows',
                          u'behaviors': [{u'category': [u'file'],
                                          u'hits': 1,
                                          u'severity': 90,
                                          u'title': u'Process Modified a File in a System Directory',
                                          u'tags': [u'executable', u'file', u'process'],
                                          u'confidence': 100,
                                          u'threat': 90,
                                          u'name': u'modified-file-in-system-dir'},
                                            ...
                                            ...
                                       ],
                          u'sha1': u'00bf659061121200c1e5469fbe31d100418b149e',
                          u'size': 228864,
                          u'threatScore': 100,
                          u'connections': {u'connections': [{u'threatTypes': [],
                                                             u'popularity1Month': None,
                                                             u'name': u'195.22.28.198',
                                                             u'attacks': [],
                                                             u'popularity3Month': None,
                                                             u'popularity': None,
                                                             u'firstQueried': None,
                                                             u'popularityWeek': None,
                                                             u'securityCategories': [],
                                                             u'ips': [],
                                                             u'lastCommit': None,
                                                             u'urls': [], u'type': u'IP',
                                                             u'firstSeen': 1460762759000,
                                                             u'lastSeen': 1460762759000
                                                            },
                                                                ...
                                                                ...
                                                           ]
                                           u'totalResults': 5,
                                           u'limit': 5,
                                           u'moreDataAvailable': True,
                                           u'offset': 0
                                          },
                          u'visible': True,
                          u'lastSeen': 1460762759000,
                          u'samples': {u'totalResults': 0,
                                       u'limit': 5,
                                       u'moreDataAvailable': False,
                                       u'samples': [], u'offset': 0
                                      },
                          u'sha256': u'414e38ed0b5d507734361c2ba94f734252ca33b8259ca32334f32c4dba69b01c',
                          u'avresults': [],
                          u'firstSeen': 1460762759000,
                          u'md5': u'6d8b70d20b1182546bc58ce7f90549d7'
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
        validate_opts(self)

    @function("umbrella_threat_grid_sample")
    def _umbrella_threat_grid_sample_function(self, event, *args, **kwargs):
        """Function: Resilient Function : Cisco Umbrella Investigate for Threat Grid sample for an MD5, SHA1 or SHA256 hash ."""
        try:
            # Get the function parameters:
            umbinv_hash = kwargs.get("umbinv_hash")  # text
            umbinv_sample_endpoint = self.get_select_param(kwargs.get(
                "umbinv_sample_endpoint"))  # select, values: "basic", "artifacts", "connections", "samples", "behaviors"
            umbinv_limit = kwargs.get("umbinv_limit")  # number
            umbinv_offset = kwargs.get("umbinv_offset")  # number

            log = logging.getLogger(__name__)
            log.info("umbinv_hash: %s", umbinv_hash)
            log.info("umbinv_sample_endpoint: %s", umbinv_sample_endpoint)
            log.info("umbinv_limit: %s", umbinv_limit)
            log.info("umbinv_offset: %s", umbinv_offset)

            if is_none(umbinv_hash):
                raise ValueError("Required parameter 'umbinv_hash' not set")

            if is_none(umbinv_sample_endpoint):
                raise ValueError("Required parameter 'umbinv_sample_endpoint' not set")

            yield StatusMessage("Starting...")
            hash = None
            process_result = {}
            params = {"hash": umbinv_hash.strip(), "sample_endpoint": umbinv_sample_endpoint,
                      "limit": umbinv_limit, "offset": umbinv_offset}

            validate_params(params)
            process_params(params, process_result)

            if "_hash" not in process_result:
               raise ValueError("Parameter 'umbinv_hash' was not processed correctly")
            else:
                hash = process_result.pop("_hash")

            api_token = self.options.get("api_token")
            base_url = self.options.get("base_url")
            rinv = ResilientInv(api_token, base_url)

            yield StatusMessage("Running Cisco Investigate query...")
            params = omit_params(params, ["hash", "sample_endpoint"])
            if umbinv_sample_endpoint == "basic":
                rtn = rinv.sample(hash, **params)
                result_header = "sample_basic"
            elif umbinv_sample_endpoint == "artifacts":
                rtn = rinv.sample_artifacts(hash, **params)
                result_header = "sample_artifacts"
            elif umbinv_sample_endpoint == "connections":
                rtn = rinv.sample_connections(hash, **params)
                result_header = "sample_connections"
            elif umbinv_sample_endpoint == "samples":
                rtn = rinv.sample_samples(hash, **params)
                result_header = "sample_samples"
            elif umbinv_sample_endpoint == "behaviors":
                rtn = rinv.sample_behaviors(hash, **params)
                result_header = "sample_behaviors"
            else :
                raise ValueError("Incorrect value for parameter parameter 'umbinv_sample_endpoint'.")
            query_execution_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            if ("error" in rtn and len(rtn["error"]) != 0):
                log.debug(json.dumps(rtn))
                yield StatusMessage("Umbrella Investigate returned error message '{}'.".format(rtn["error"]))
                results = {}
            else:
                # Add "query_execution_time" and "hash" key to result to facilitate post-processing.
                results = {result_header: json.loads(json.dumps(rtn)), "hash": hash,
                           "query_execution_time": query_execution_time}
                yield StatusMessage("Returning '{}' results for hash '{}'.".format(result_header, hash))

            yield StatusMessage("Done...")

            log.debug(json.dumps(results))
            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            log.exception("Exception in Resilient Function.")
            yield FunctionError()