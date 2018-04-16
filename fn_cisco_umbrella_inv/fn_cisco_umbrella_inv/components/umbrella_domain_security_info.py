# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

""" Resilient functions component to run an Umbrella investigate Query - Security Information for a Domain against a Cisco
Umbrella server """

# Set up:
# Destination: a Queue named "umbrella_investigate".
# Manual Action: Execute a REST query against a Cisco Umbrella server.
import json
import logging

from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_cisco_umbrella_inv.util.resilient_inv import ResilientInv
from fn_cisco_umbrella_inv.util.helpers import validate_opts, validate_params, process_params

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'umbrella_dns_rr_hist' of
    package fn_cisco_umbrella_inv.

    The Function does a Cisco Umbrella Investigate query lookup takes the following parameters:
        domain

    An example of a set of query parameter might look like the following:

            domain = "example.com"

    The Investigate Query will executs a REST call agaist the Cisco Umbrell Investigate server and returns a result in
    JSON format similar to the following.Note: The Function adds an extra "domain_name" field in the returned result to
    aid post-processing.

            'security_info':{
              u'domain_name':u'example.com',
              u'found':True,
              u'geodiversity_normalized':[
                 [
                    u'??',
                    0.5706777350888877
                 ],

                  ...
                 [
                    u'DZ',
                    0.000126500569665041
                 ]
              ],
              u'geodiversity':[
                 [
                    u'US',
                    0.4534
                 ],
                  ...

                 [
                    u'LB',
                    0.0001
                 ]
              ],
              u'dga_score':0.0,
              u'rip_score':0.0,
              u'asn_score':-0.041783697445309576,
              u'securerank2':100.0,
              u'popularity':100.0,
              u'geoscore':0.0,
              u'attack':u'',
              u'pagerank':40.914368,
              u'entropy':2.521640636343318,
              u'ks_test':0.0,
              u'prefix_score':0.0,
              u'perplexity':0.2327827581680193,
              u'fastflux':False,
              u'threat_type':u'',
              u'tld_geodiversity':[

              ]
           }

    """
    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_cisco_umbrella_inv", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_cisco_umbrella_inv", {})

    @function("umbrella_domain_security_info")
    def _umbrella_domain_security_info_function(self, event, *args, **kwargs):
        """Function: Resilient Function : Cisco Umbrella Security Investigate for Information for a Domain"""
        try:
            # Get the function parameters:
            umbinv_domain = kwargs.get("umbinv_domain")  # text

            log = logging.getLogger(__name__)
            log.info("umbinv_domain: %s", umbinv_domain)

            if umbinv_domain is None:
                raise ValueError("Required parameter 'umbinv_domain' not set")

            self._params = {"domain": umbinv_domain}

            yield StatusMessage("Starting...")
            validate_opts(self)
            validate_params(self)
            process_params(self)

            if not hasattr(self, '_domain'):
                raise ValueError("Parameter 'umbinv_domain' was not processed correctly")

            api_token = self.options.get("api_token")
            rinv = ResilientInv(api_token)

            yield StatusMessage("Running Cisco Investigate query...")
            rtn = rinv.security(self._domain)
            # Add in domain name it ran against to result.
            rtn["domain_name"] = self._domain
            results = {"security_info": json.loads(json.dumps(rtn))}
            yield StatusMessage("done...")

            log.debug(json.dumps(results))
            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()