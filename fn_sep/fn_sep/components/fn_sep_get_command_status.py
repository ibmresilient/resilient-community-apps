# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
""" Resilient functions component to run a Symantec SEPM query - get command status """

# Set up:
# Destination: a Queue named "fn_sep".
# Manual Action: Execute a REST query against a SYMANTEC SEPM server.
import json
import logging

from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_sep.lib.sep_client import Sepclient
from resilient_lib import ResultPayload, validate_fields
from fn_sep.lib.helpers import transform_kwargs
from fn_sep.lib.results_processing import process_results

CONFIG_DATA_SECTION = "fn_sep"
LOG = logging.getLogger(__name__)

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_sep_get_command_status' of
    package fn_sep.

    The Function takes the following parameter:
            sep_commandid, sep_order, sep_pageindex, sep_pagesize, sep_sort

    An example of a set of query parameter might look like the following:
            sep_commandid = None
            sep_order = None
            sep_pageindex = None
            sep_pagesize = None
            sep_sort = None
            sep_status_type = "scan"

    The function will execute a REST api get request against a SYMANTEC  SEPM server for information on endpoints and
    returns a result in JSON format similar to the following.

    {
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

    @function("fn_sep_get_command_status")
    def _fn_sep_get_command_status_function(self, event, *args, **kwargs):
        """Function: Returns a list of computers with agents deployed on them. You can use parameters to narrow the search by IP address or hostname."""
        try:
            params = transform_kwargs(kwargs) if kwargs else {}

            # Instantiate result payload object.
            rp = ResultPayload(CONFIG_DATA_SECTION, **kwargs)

            # Get the function parameters:
            sep_commandid = kwargs.get("sep_commandid")  # text
            sep_order = kwargs.get("sep_order")  # text
            sep_pageindex = kwargs.get("sep_pageindex")  # number
            sep_pagesize = kwargs.get("sep_pagesize")  # number
            sep_sort = kwargs.get("sep_sort")  # text
            sep_status_type = kwargs.get("sep_status_type")  # text

            log = logging.getLogger(__name__)
            log.info("sep_commandid: %s", sep_commandid)
            log.info("sep_order: %s", sep_order)
            log.info("sep_pageindex: %s", sep_pageindex)
            log.info("sep_pagesize: %s", sep_pagesize)
            log.info("sep_sort: %s", sep_sort)
            log.info("sep_status_type: %s", sep_status_type)

            validate_fields(["sep_commandid", "sep_status_type"], kwargs)

            yield StatusMessage("Running Symantec SEP Get Computers query...")

            sep = Sepclient(self.options, params)

            rtn = process_results(sep.get_command_status(**params), sep_status_type)

            results = rp.done(True, rtn)

            yield StatusMessage("Returning Get Command Status results")

            log.debug(json.dumps(results["content"]))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            LOG.exception("Exception in Resilient Function for Symantec SEP.")
            yield FunctionError()
