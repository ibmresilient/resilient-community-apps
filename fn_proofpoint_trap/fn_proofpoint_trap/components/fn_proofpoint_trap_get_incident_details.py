# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
""" Resilient functions component to run a ProofPoint TRAP query - get incident details. """

# Set up:
# Destination: a Queue named "fn_proofpoint_trap".
# Manual Action: Execute a REST query against a ProofPoint TRAP server.

import logging

from resilient_circuits import ResilientComponent, function, handler, FunctionResult, FunctionError
from resilient_lib import ResultPayload, validate_fields
from fn_proofpoint_trap.lib.pptr_client import PPTRClient
from fn_proofpoint_trap.lib.helpers import CONFIG_DATA_SECTION, transform_kwargs, validate_opts

LOG = logging.getLogger(__name__)

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_proofpoint_trap_get_incident_details"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_proofpoint_trap", {})
        validate_opts(self)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_proofpoint_trap", {})
        validate_opts(self)

    @function("fn_proofpoint_trap_get_incident_details")
    def _fn_proofpoint_trap_get_incident_details_function(self, event, *args, **kwargs):
        """Function: Fetch Incident Details from Proofpoint TRAP"""

        try:
            params = transform_kwargs(kwargs) if kwargs else {}
            rp = ResultPayload(CONFIG_DATA_SECTION, **kwargs)
            # Get the function parameters:
            trap_incident_id = kwargs.get("trap_incident_id")  # number

            LOG.info("trap_incident_id: %s", trap_incident_id)


            validate_fields(["trap_incident_id"], kwargs)

            pptr = PPTRClient(self.opts, self.options)
            rtn = pptr.get_incident_details(**params)
            if isinstance(rtn, dict) and "error" in rtn:
                results = rtn
            else:
                results = rp.done(True, rtn)
                results["data"] = rtn["data"]
                results["href"] = rtn["href"]

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            LOG.exception("Exception in Resilient Function for Proofpoint TRAP.")
            yield FunctionError()
