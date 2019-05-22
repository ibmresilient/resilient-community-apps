# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
""" Resilient functions component to run a Symantec SEPM query - get fingerprint list """

# Set up:
# Destination: a Queue named "fn_sep".
# Manual Action: Execute a REST query against a SYMANTEC SEPM server.
import json
import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_sep.lib.sep_client import Sepclient
from resilient_lib import ResultPayload, validate_fields
from fn_sep.lib.helpers import transform_kwargs

CONFIG_DATA_SECTION = "fn_sep"

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_sep_assign_fingerprint_list_to_group' of
    package fn_sep.

    The Function takes the following parameters:
            sep_fingerprintlist_id, sep_group_id

    An example of a set of query parameter might look like the following:
            sep_fingerprintlist_id =
            sep_group_id =

    The function will execute a REST api get request against a SYMANTEC SEPM server for information on endpoints and
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

    @function("fn_sep_assign_fingerprint_list_to_group")
    def _fn_sep_assign_fingerprint_list_to_group_function(self, event, *args, **kwargs):
        """Function: Returns a list of computers with agents deployed on them. You can use parameters to narrow the search by IP address or hostname."""
        try:
            params = transform_kwargs(kwargs) if kwargs else {}

            # Instantiate result payload object
            rp = ResultPayload(CONFIG_DATA_SECTION, **kwargs)

            # Get the function parameters:
            sep_fingerprintlist_id = kwargs.get("sep_fingerprintlist_id")  # text
            sep_group_id = kwargs.get("sep_group_id")  # text

            log = logging.getLogger(__name__)
            log.info("sep_fingerprintlist_id: %s", sep_fingerprintlist_id)
            log.info("sep_group_id: %s", sep_group_id)

            validate_fields(["sep_fingerprintlist_id", "sep_group_id"], kwargs)

            yield StatusMessage("Running Symantec SEP Assign Fingerprint List to Group for Lock-down action ...")

            sep = Sepclient(self.options, params)

            rtn = sep.assign_fingerprint_list_to_group(**params)

            results = rp.done(True, rtn)
            yield StatusMessage("Returning 'Symantec SEP Assign Fingerprint List to Group for Lock-down' results")

            log.debug(json.dumps(results["content"]))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            log.exception("Exception in Resilient Function for Symantec SEP.")
            yield FunctionError()
