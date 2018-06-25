# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

""" Resilient functions component to run an Umbrella investigate Query - Threat Grid Integration samples against a
Cisco Umbrella server """

# Set up:
# Destination: a Queue named "umbrella_investigate".
# Manual Action: Execute a REST query against a Cisco Umbrella server.import logging
import logging
import json
from datetime import datetime

from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_cisco_umbrella_inv.util.resilient_inv import ResilientInv
from fn_cisco_umbrella_inv.util.helpers import validate_opts, validate_params, process_params,omit_params, \
    is_none


class FunctionComponent(ResilientComponent):
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
         'thread_grid_samples': {u'limit': 2,
                                 u'moreDataAvailable': True,
                                 u'samples': [{u'magicType': u'PE32 executable (GUI) Intel 80386, for MS Windows, UPX compressed',
                                               u'behaviors': [],
                                               u'sha1': u'ccdeb2319d6b924e359f563527404a0af3d1ac54',
                                               u'size': 22020, u'threatScore': 100,
                                               u'visible': False, u'lastSeen': 1518410873000,
                                               u'sha256': u'65f33f9e6d16918ba72bc20bcd85ebd75bc735df5666a843cab9c6dec9c0b1c1',
                                               u'avresults': [{u'product': u'ClamAV', u'signature': u'Win.Worm.Mydoom'}],
                                               u'firstSeen': 1518410872000, u'md5': u'0c340a220817e157346bef7976a0d0b6'},
                                             { u'magicType': u'PE32 executable (GUI) Intel 80386, for MS Windows, UPX compressed',
                                               u'behaviors': [],
                                               u'sha1': u'971d92e80764812f0abca9ccf3075f5e9cc6fa4a',
                                               u'size': 33616,
                                               u'threatScore': 100,
                                               u'visible': False,
                                               u'lastSeen': 1503550227000,
                                               u'sha256': u'eb19d33f6b157d814bef539e3625ab9d40b217271d7144e23b20effb677577b5',
                                               u'avresults': [{u'product': u'ClamAV', u'signature': u'Win.Worm.Mydoom'}],
                                               u'firstSeen': 1503550227000, u'md5': u'8d1bcddb2cbb143e2ade4622770f4849'}
                                             ],
                                 u'offset': 0,
                                 u'query': u'cisco.com', u'totalResults': 2
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

    @function("umbrella_threat_grid_samples")
    def _umbrella_threat_grid_samples_function(self, event, *args, **kwargs):
        """Function: Resilient Function : Cisco Umbrella Investigate for Threat Grid samples for domain, IP or URL resource."""
        try:
            # Get the function parameters:
            umbinv_resource = kwargs.get("umbinv_resource")  # text
            umbinv_limit = kwargs.get("umbinv_limit")  # number
            umbinv_offset = kwargs.get("umbinv_offset")  # number
            umbinv_sortby = kwargs.get("umbinv_sortby")  # text

            log = logging.getLogger(__name__)
            log.info("umbinv_resource: %s", umbinv_resource)
            log.info("umbinv_limit: %s", umbinv_limit)
            log.info("umbinv_offset: %s", umbinv_offset)
            log.info("umbinv_sortby: %s", umbinv_sortby)

            if is_none(umbinv_resource):
                raise ValueError("Required parameter 'umbinv_resource' not set")

            yield StatusMessage("Starting...")
            res = None
            res_type = None
            process_result = {}
            params = {"resource": umbinv_resource.strip(), "limit": umbinv_limit, "sortby": umbinv_sortby,
                      "offset": umbinv_offset}

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
            rtn = rinv.samples(res, **omit_params(params, ["resource", "resource_type"]))
            if "error" in rtn:
                log.debug(json.dumps(rtn))
                yield StatusMessage("Investigate returned 'error' status: '{}'.".format(rtn["error"]))
                results = {}
            elif len(rtn) == 0 or ("samples" in rtn and len(rtn["samples"]) == 0):
                log.debug(json.dumps(rtn))
                yield StatusMessage("No Results returned for resource '{}'.".format(res))
                results = {}
            else:
                query_execution_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                # Make each sample 'firstSeen' and "lastSeen" property more readable.
                for i in range(len(rtn["samples"])):
                    fs = rtn["samples"][i]["firstSeen"]
                    ls = rtn["samples"][i]["lastSeen"]
                    try:
                        secs = int(fs) / 1000
                        fs_readable = datetime.fromtimestamp(secs).strftime('%Y-%m-%d %H:%M:%S')
                        rtn["samples"][i]["first_seen_converted"] = fs_readable
                        secs = int(ls) / 1000
                        ls_readable = datetime.fromtimestamp(secs).strftime('%Y-%m-%d %H:%M:%S')
                        rtn["samples"][i]["last_seen_converted"] = ls_readable
                    except ValueError:
                        yield FunctionError('Timestamp value incorrectly specified')

                # Add "query_execution_time" and "domains" key to result to facilitate post-processing.
                results = {"thread_grid_samples": json.loads(json.dumps(rtn)), "resource_name": params["resource"],
                           "query_execution_time": query_execution_time}
                yield StatusMessage("Returning 'thread_grid_samples' results for resource '{}'.".format(res))

            yield StatusMessage("Done...")

            log.debug(json.dumps(results))
            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            log.exception("Exception in Resilient Function.")
            yield FunctionError()