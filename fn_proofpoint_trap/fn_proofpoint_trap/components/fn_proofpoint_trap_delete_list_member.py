# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, FunctionResult, FunctionError
from resilient_lib import ResultPayload, validate_fields
from fn_proofpoint_trap.lib.pptr_client import PPTRClient
from fn_proofpoint_trap.lib.helpers import CONFIG_DATA_SECTION, transform_kwargs, validate_opts

LOG = logging.getLogger(__name__)

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_proofpoint_trap_delete_list_member"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super().__init__(opts)
        self.options = opts.get("fn_proofpoint_trap", {})
        validate_opts(self)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_proofpoint_trap", {})
        validate_opts(self)

    @function("fn_proofpoint_trap_delete_list_member")
    def _fn_proofpoint_trap_delete_list_member_function(self, event, *args, **kwargs):
        """Function: Delete the member of a list."""
        try:
            params = transform_kwargs(kwargs) if kwargs else {}

            rp = ResultPayload(CONFIG_DATA_SECTION, **kwargs)

            # Get the function parameters:
            trap_list_id = kwargs.get("trap_list_id")  # number
            trap_member_id = kwargs.get("trap_member_id")  # number

            LOG.info("trap_list_id: %s", trap_list_id)
            LOG.info("trap_member_id: %s", trap_member_id)

            validate_fields(["trap_list_id", "trap_member_id"], kwargs)

            pptr = PPTRClient(self.opts, self.options)
            rtn = pptr.delete_list_member(**params)

            results = rp.done(True, rtn)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            LOG.exception("Exception in Resilient Function for Proofpoint TRAP.")
            yield FunctionError()
