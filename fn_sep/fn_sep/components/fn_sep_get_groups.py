# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
""" Resilient functions component to run a Symantec SEPM query - get groups. """

# Set up:
# Destination: a Queue named "fn_sep".
# Manual Action: Execute a REST query against a SYMANTEC SEPM server.
import json
import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_sep.lib.sep_client import Sepclient
from resilient_lib import ResultPayload
from fn_sep.lib.helpers import transform_kwargs

CONFIG_DATA_SECTION = "fn_sep"
LOG = logging.getLogger(__name__)

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_sep_get_groups' of package fn_sep.
    The function can be used to query to get information on groups.

    The Function takes the following parameter:
        sep_domain, sep_fullpathname, sep_mode, sep_order, sep_pageindex, sep_pagesize, sep_sort,

        An example of a set of query parameter might look like the following:
                sep_domain = None
                sep_fullpathname = None
                sep_mode = None
                sep_order = None
                sep_pageindex = None
                sep_pagesize = None
                sep_sort = None

    The function will execute a REST api get request against a SYMANTEC SEPM server for information on group and
    returns a result in JSON format similar to the following.

    {
        "inputs": {"sep_domain": null, "sep_fullpathname": null, "sep_mode": null, "sep_order: null,
                   "sep_pageindex": null, "sep_pagesize": null, "sep_sort": null},
        "metrics": {'package': 'fn-sep', 'timestamp': '2019-03-01 12:46:27', 'package_version': '1.0.0',
        "host": 'myhost, 'version': '1.0', 'execution_time_ms': 1085},
        "success': True,
        'content': {
                      "sort": [
                        {
                          "direction": "ASC",
                          "property": "NAME",
                          "ascending": true
                        }
                      ],
                      "number": 0,
                      "firstPage": true,
                       "group_name", "group_id", "group_description", "fullPathName"]
                      "content": [
                        {
                          ...
                          "domain": {
                            "id": "908090000946C25D330E919313D23887",
                            "name": "Default"
                          },
                          ...
                          "description": "",
                          ...
                          "fullPathName": "My Company\\Default Group",
                          ...
                          "id": "4CBD63EE0946C25D1011DB1872A1736A",
                          ...
                          "name": "Default Group"
                        },
                        {
                          ...
                        }
                      ],
                      "lastPage": true,
                      "totalPages": 1,
                      "size": 25,
                      "totalElements": 2,
                      "numberOfElements": 2
        },
        "raw": '<<a string representation of content.>>',
        "reason": None, 'version': '1.0'
    }
    """
    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get(CONFIG_DATA_SECTION, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get(CONFIG_DATA_SECTION, {})

    @function("fn_sep_get_groups")
    def _fn_sep_get_groups_function(self, event, *args, **kwargs):
        """Function: Gets a group list."""
        try:
            params = transform_kwargs(kwargs) if kwargs else {}
            # Instantiate result payload object.
            rp = ResultPayload(CONFIG_DATA_SECTION, **kwargs)

            # Get the function parameters:
            sep_domain = kwargs.get("sep_domain")  # text
            sep_fullpathname = kwargs.get("sep_fullpathname")  # text
            sep_mode = kwargs.get("sep_mode")  # text
            sep_order = kwargs.get("sep_order")  # text
            sep_pageindex = kwargs.get("sep_pageindex")  # number
            sep_pagesize = kwargs.get("sep_pagesize")  # number
            sep_sort = kwargs.get("sep_sort")  # text

            log = logging.getLogger(__name__)
            log.info("sep_domain: %s", sep_domain)
            log.info("sep_fullpathname: %s", sep_fullpathname)
            log.info("sep_mode: %s", sep_mode)
            log.info("sep_order: %s", sep_order)
            log.info("sep_pageindex: %s", sep_pageindex)
            log.info("sep_pagesize: %s", sep_pagesize)
            log.info("sep_sort: %s", sep_sort)

            yield StatusMessage("Running Symantec SEP Get Groups query...")

            sep = Sepclient(self.options, params)

            rtn = sep.get_paginated_results(sep.get_groups, **params)

            results = rp.done(True, rtn)
            yield StatusMessage("Returning 'Symantec SEP Get Groups' results")

            log.debug(json.dumps(results["content"]))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            LOG.exception("Exception in Resilient Function for Symantec SEP.")
            yield FunctionError()
