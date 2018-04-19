# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

""" Resilient functions component to run an Umbrella investigate Query - Domain Status and Categorization against a
Cisco Umbrella server """

# Set up:
# Destination: a Queue named "umbrella_investigate".
# Manual Action: Execute a REST query against a Cisco Umbrella server.
import json
import logging
from datetime import datetime

from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_cisco_umbrella_inv.util.resilient_inv import ResilientInv
from fn_cisco_umbrella_inv.util.helpers import validate_opts, validate_params, process_params


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'umbrella_domain_status_and_category' of
    package fn_cisco_umbrella_inv.

    The Function does a Cisco Umbrella Investigate query lookup takes the following parameters:
        umbinv_domains, umbinv_showlabels, umbinv_status_endpoint

    An example of a set of query parameter might look like the following:

            umbinv_domains = "amazon.com" or umbinv_domains = '"google.com","yahoo.com"' \
                or umbinv_domains = '"google.com" "yahoo.com"'
            umbinv_showlables = True/Falsed (boolean)
            umbinv_status_endpoint = "categorization" or status_endpoint = "categories"

    For status_endpoint = "categorization", the Investigate Query will executes a REST call against the Cisco Umbrella
    Investigate server and returns a result in JSON format similar to the following for single domain. Note: The
    Function adds an extra "domains" field in the returned result to aid post-processing.

         {'domains': [u'amazon.com'],
          'statuses': {u'amazon.com': {u'status': 1,
                                       u'content_categories': [u'Ecommerce/Shopping'],
                                       u'security_categories': []
                                      }
                      }
        }
    For status_endpoint = "categories", the Investigate Query will executes a REST call against the Cisco Umbrella
    Investigate server and returns a result in JSON format similar to the following giving a list of category numbers
    mapped to strings. Note: The Function adds extra "min_id" and "max_id" field in the returned result to aid
    post-processing.

        {"min_id": 0,
         "max_id": 150,
         "categories": {"133": "Safe for Kids",
                        "132": "SaaS and B2B",
                        "131": "Real Estate",
                        ...
                        ...
                        "141": "Organisation Email"
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

    @function("umbrella_domain_status_and_category")
    def _umbrella_domain_status_and_category_function(self, event, *args, **kwargs):
        """Function: Resilient Function : Cisco Umbrella Investigate for Domain Status and Categorization."""
        try:
            # Get the function parameters:
            umbinv_domains = kwargs.get("umbinv_domains")  # text
            umbinv_showlabels = kwargs.get("umbinv_showlabels")  # boolean
            umbinv_status_endpoint = self.get_select_param(kwargs.get("umbinv_status_endpoint"))  # select, values: "categorization", "categories"

            log = logging.getLogger(__name__)
            log.info("umbinv_domains: %s", umbinv_domains)
            log.info("umbinv_showlabels: %s", umbinv_showlabels)
            log.info("umbinv_status_endpoint: %s", umbinv_status_endpoint)

            if umbinv_status_endpoint is None:
                raise ValueError("Required parameter 'umbinv_status_endpoint' not set")

            self._params = {"domains": umbinv_domains.strip(), "showlabels": umbinv_showlabels, "status_endpoint": umbinv_status_endpoint}
            if umbinv_showlabels:
                self._params.setdefault('showlabels', None)

            yield StatusMessage("Starting...")

            validate_params(self)
            process_params(self)

            if (umbinv_status_endpoint == "categorization") and (not hasattr(self, '_domain') and not hasattr(self, '_domains')):
                raise ValueError("Parameter 'umbinv_domains' was not processed correctly")

            api_token = self.options.get("api_token")
            base_url = self.options.get("base_url")
            rinv = ResilientInv(api_token,base_url)

            yield StatusMessage("Running Cisco Investigate query...")
            if (umbinv_status_endpoint == "categories"):
                cat_keys = []
                # Add metadata of "query_execution_time", "min_id" and "max_id" keys to make it easier in post-processing.
                rtn = rinv.categories()
                query_execution_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                for c in rtn:
                    cat_keys.append(c)
                    cat_keys_int = map(int, cat_keys)
                results = {"categories": json.loads(json.dumps(rtn)), "min_id": min(cat_keys_int),
                           "max_id": max(cat_keys_int), "query_execution_time": query_execution_time}
            elif (umbinv_status_endpoint == "categorization"):
                dom_list = []
                if hasattr(self, '_domains'):
                    rtn = rinv.categorization(self._domains, self._params["showlabels"])
                elif hasattr(self, '_domain'):
                    rtn = rinv.categorization(self._domain, self._params["showlabels"])
                for d in rtn:
                    dom_list.append(d)
                query_execution_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                # Add "query_execution_time" and "domains" key to result to facilitate post-processing.
                results = {"statuses": json.loads(json.dumps(rtn)), "domains": dom_list,
                           "query_execution_time": query_execution_time}
            yield StatusMessage("Done...")

            log.debug(json.dumps(results))
            #Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            logging.exception("Exception in Resilient Function.")
            yield FunctionError()