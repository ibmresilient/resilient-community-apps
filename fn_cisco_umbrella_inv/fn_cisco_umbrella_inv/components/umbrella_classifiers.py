# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

""" Resilient functions component to run an Umbrella investigate Query - Classifiers against a Cisco Umbrella server """

# Set up:
# Destination: a Queue named "umbrella_investigate".
# Manual Action: Execute a REST query against a Cisco Umbrella server.
import logging
import json
from datetime import datetime, time

from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_cisco_umbrella_inv.util.resilient_inv import ResilientInv
from fn_cisco_umbrella_inv.util.helpers import validate_opts, validate_params, process_params, is_none

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'umbrella_classifiers' of
    package fn_cisco_umbrella_inv.

    The Function does a Cisco Umbrella Investigate query lookup takes the following parameters:
        umbinv_domain, umbinv_classifiers_endpoint

    An example of a set of query parameter might look like the following:

            umbinv_domain = "cosmos.furnipict.com"

    The Investigate Query will executs a REST call against the Cisco Umbrell Investigate server and returns a result in
    JSON format similar to the following.


        {'domain_name': 'cosmos.furnipict.com',
         'query_execution_time': '2018-06-18 11:53:01'
         'classifiers_info': {u'first_queried_converted': u'2016-11-18 19:16:00', u'firstQueried': 1479496560000},
         'classifiers_classifiers': {u'securityCategories': [u'Malware'], u'attacks': [u'Neutrino'],
                                     u'threatTypes': [u'Exploit Kit']}
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

    @function("umbrella_classifiers")
    def _umbrella_classifiers_function(self, event, *args, **kwargs):
        """Function: Resilient Function : Cisco Umbrella Investigate for  Classifiers."""
        try:
            # Get the function parameters:
            umbinv_domain = kwargs.get("umbinv_domain") # text

            log = logging.getLogger(__name__)

            log.info("umbinv_domain: %s", umbinv_domain)

            if is_none(umbinv_domain):
                raise ValueError("Required parameter 'umbinv_domain' not set.")

            yield StatusMessage("Starting...")
            domain = None
            process_result = {}
            params = {"domain": umbinv_domain.strip()}

            validate_params(params)
            process_params(params, process_result)

            if "_domain" not in process_result:
                 raise ValueError("Parameter 'umbinv_domain' was not processed correctly")
            else:
                domain = process_result.pop("_domain")

            api_token = self.options.get("api_token")
            base_url = self.options.get("base_url")
            rinv = ResilientInv(api_token, base_url)

            yield StatusMessage("Running Cisco Investigate query...")
            classifiers_res = True
            info_res = True
            # Run against 'classifiers' endpoint
            rtn_classifiers = rinv.classifiers_classifiers(domain)
            # Run against 'info' endpoint
            rtn_info = rinv.classifiers_info(domain)
            query_execution_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            if ("securityCategories" in rtn_classifiers and not rtn_classifiers["securityCategories"]) and \
                    ("attacks" in rtn_classifiers and not rtn_classifiers["attacks"]) and \
                    ("threatTypes" in rtn_classifiers and not rtn_classifiers["threatTypes"]):
                classifiers_res = False

            if "firstQueried" in rtn_info and rtn_info["firstQueried"] is None:
                info_res = False
            else:
                # Make 'firstQueried' more readable
                fq = rtn_info["firstQueried"]
                try:
                    secs = int(fq) / 1000
                    fq_readable = datetime.fromtimestamp(secs).strftime('%Y-%m-%d %H:%M:%S')
                    rtn_info["first_queried_converted"] = fq_readable
                except ValueError:
                    yield FunctionError('timestamp value incorrectly specified')

            if not classifiers_res and not info_res:
                log.debug(json.dumps(rtn_classifiers))
                log.debug(json.dumps(rtn_info))
                results = {}
                yield StatusMessage("No Results returned for domain '{}'.".format(domain))
            else:
                # Add "query_execution_time" and "domain_name" to result to facilitate post-processing.
                results = {"classifiers_classifiers": json.loads(json.dumps(rtn_classifiers)),
                            "classifiers_info": json.loads(json.dumps(rtn_info)),
                            "domain_name": domain,
                            "query_execution_time": query_execution_time}
                yield StatusMessage("Returning 'classifiers and info' results for domain '{}'.".format(domain))

            yield StatusMessage("done...")

            log.debug(json.dumps(results))
            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            log.exception("Exception in Resilient Function.")
            yield FunctionError()