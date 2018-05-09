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
from fn_cisco_umbrella_inv.util.helpers import init_env, validate_opts, validate_params, process_params,omit_params, \
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

    @function("umbrella_threat_grid_samples")
    def _umbrella_threat_grid_samples_function(self, event, *args, **kwargs):
        """Function: Resilient Function : Cisco Umbrella Investigate for Threat Grid samples for domain, IP or URL resource."""
        try:
            # Get the function parameters:
            umbinv_resource = kwargs.get("umbinv_resource")  # text
            umbinv_resource_type = self.get_select_param(kwargs.get("umbinv_resource_type"))  # select, values: "domain_name", "ip_address", "url"
            umbinv_limit = kwargs.get("umbinv_limit")  # number
            umbinv_offset = kwargs.get("umbinv_offset")  # number
            umbinv_sortby = kwargs.get("umbinv_sortby")  # text

            log = logging.getLogger(__name__)
            log.info("umbinv_resource: %s", umbinv_resource)
            log.info("umbinv_resource_type: %s", umbinv_resource_type)
            log.info("umbinv_limit: %s", umbinv_limit)
            log.info("umbinv_offset: %s", umbinv_offset)
            log.info("umbinv_sortby: %s", umbinv_sortby)

            if is_none(umbinv_resource):
                raise ValueError("Required parameter 'umbinv_resource' not set")

            if is_none(umbinv_resource_type):
                raise ValueError("Required parameter 'umbinv_resource_type' not set")

            yield StatusMessage("Starting...")
            init_env(self)

            self._params = {"resource": umbinv_resource.strip(), "resource_type": umbinv_resource_type,
                            "limit": umbinv_limit, "sortby": umbinv_sortby, "offset": umbinv_offset}

            validate_params(self)
            process_params(self)

            if not hasattr(self, '_res'):
               raise ValueError("Parameter 'umbinv_resource' was not processed correctly")

            api_token = self.options.get("api_token")
            base_url = self.options.get("base_url")
            rinv = ResilientInv(api_token, base_url)

            yield StatusMessage("Running Cisco Investigate query...")
            rtn = rinv.samples(self._res, **omit_params(self._params, ["resource", "resource_type"]))
            if len(rtn["samples"]) == 0:
                log.debug(json.dumps(rtn))
                yield StatusMessage("No Results returned for regular expression '{}'.".format(self._regex))
                results = {}
            else:
                query_execution_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                # Add "query_execution_time" and "domains" key to result to facilitate post-processing.
                results = {"thread_grid_samples": json.loads(json.dumps(rtn)), "resource_name": self._res,
                           "query_execution_time": query_execution_time}
            yield StatusMessage("Done...")

            log.debug(json.dumps(results))
            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()