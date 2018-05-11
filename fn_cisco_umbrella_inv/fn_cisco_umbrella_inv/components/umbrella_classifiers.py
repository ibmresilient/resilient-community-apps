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
from fn_cisco_umbrella_inv.util.helpers import init_env, validate_opts, validate_params, process_params, is_none

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'umbrella_classifiers' of
    package fn_cisco_umbrella_inv.

    The Function does a Cisco Umbrella Investigate query lookup takes the following parameters:
        umbinv_domain, umbinv_classifiers_endpoint

    An example of a set of query parameter might look like the following:

            umbinv_domain = "cosmos.furnipict.com"
            umbinv_classifiers_endpoint = "classifiers"

    The Investigate Query will executs a REST call against the Cisco Umbrell Investigate server and returns a result in
    JSON format similar to the following.


        {'domain_name': 'cosmos.furnipict.com',
         'query_execution_time': '2018-05-02 15:59:14'
         'classifiers_classifiers': {u'securityCategories': [u'Malware'],
                                     u'attacks': [u'Neutrino'],
                                     u'threatTypes': [u'Exploit Kit']},
        }

    Also for:

            umbinv_domain = "cosmos.furnipict.com"
            umbinv_classifiers_endpoint = "info"


        {'classifiers_info': {u'firstQueried': 1479496560000},
         'domain_name': 'cosmos.furnipict.com',
         'query_execution_time': '2018-05-02 16:03:15'
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
            umbinv_classifiers_endpoint = self.get_select_param(kwargs.get("umbinv_classifiers_endpoint"))  # select, values: "classifiers", "info"

            log = logging.getLogger(__name__)

            log.info("umbinv_domain: %s", umbinv_domain)
            log.info("umbinv_classifiers_endpoint: %s", umbinv_classifiers_endpoint)


            if is_none(umbinv_domain):
                raise ValueError("Required parameter 'umbinv_domain' not set.")

            if is_none(umbinv_classifiers_endpoint):
                raise ValueError("Required parameter 'umbinv_classifiers_endpoint' not set.")

            yield StatusMessage("Starting...")
            init_env(self)

            self._params = {"domain": umbinv_domain.strip(), "classifiers_endpoint": umbinv_classifiers_endpoint}

            validate_params(self)
            process_params(self)

            if not hasattr(self, '_domain'):
               raise ValueError("Parameter 'umbinv_domain' was not processed correctly")

            api_token = self.options.get("api_token")
            base_url = self.options.get("base_url")
            rinv = ResilientInv(api_token,base_url)

            yield StatusMessage("Running Cisco Investigate query...")
            if (umbinv_classifiers_endpoint == "classifiers"):
                # Add metadata of "query_execution_time", "min_id" and "max_id" keys to make it easier in post-processing.
                rtn = rinv.classifiers_classifiers(self._domain)
                query_execution_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                results = {"classifiers_classifiers": json.loads(json.dumps(rtn)), "domain_name": self._domain,
                           "query_execution_time": query_execution_time}
            elif (umbinv_classifiers_endpoint == "info"):
                rtn = rinv.classifiers_info(self._domain)
                query_execution_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                # Add "query_execution_time" and "domains" key to result to facilitate post-processing.
                results = {"classifiers_info": json.loads(json.dumps(rtn)), "domain_name": self._domain,
                           "query_execution_time": query_execution_time}
            yield StatusMessage("done...")

            log.debug(json.dumps(results))
            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            log.exception("Exception in Resilient Function.")
            yield FunctionError()