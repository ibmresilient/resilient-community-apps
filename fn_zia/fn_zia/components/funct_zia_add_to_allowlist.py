# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload, validate_fields
import fn_zia.util.config as config
from fn_zia.lib.zia_client import ZiaClient
from fn_zia.lib.decorators import RateLimit as ratelimit

PACKAGE_NAME = "fn_zia"
FN_NAME = "funct_zia_add_to_allowlist"
LOG = logging.getLogger(__name__)


# Initialize the ratelimit decorator.
ratelimit(init=True, method="put")

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'funct_zia_add_to_allowlist''"""

    def __init__(self, opts):
        """Constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.fn_options = opts.get(PACKAGE_NAME, {})
        self.opts = opts
        validate_fields(config.REQUIRED_CONFIG_SETTINGS, self.fn_options)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.fn_options = opts.get(PACKAGE_NAME, {})
        self.opts = opts
        validate_fields(config.REQUIRED_CONFIG_SETTINGS, self.fn_options)

    @function(FN_NAME)
    def _funct_zia_add_to_allowlist_function(self, event, *args, **kwargs):
        """Function: None"""
        try:
            rp = ResultPayload(PACKAGE_NAME, **kwargs)

            # Get the wf_instance_id of the workflow this Function was called in
            wf_instance_id = event.message["workflow_instance"]["workflow_instance_id"]

            yield StatusMessage("Starting '{0}' running in workflow '{1}'".format(FN_NAME, wf_instance_id))


            # Get and validate required function inputs:
            fn_inputs = validate_fields(
                ["zia_allowlisturls",
                 "zia_activate"],
                kwargs)

            LOG.info("'{0}' inputs: %s", fn_inputs)

            yield StatusMessage("Validations complete. Starting business logic")

            allowlisturls = fn_inputs.get("zia_allowlisturls")
            activate = fn_inputs.get("zia_activate")

            ziacli = ZiaClient(self.opts, self.fn_options)

            result = {
                "response": ziacli.allowlist_action(allowlisturls, "ADD_TO_LIST")
            }

            if not result["response"].get("error_code", False):
                # Only attempt activation if main request didn't return an error.
                result["activation"] = ziacli.activate(activate)

            yield StatusMessage("Finished '{0}' that was running in workflow '{1}'".format(FN_NAME, wf_instance_id))

            results = rp.done(True, result)
            LOG.info("'%s' complete", FN_NAME)

            yield StatusMessage("Returning results for function '{}' with parameters '{}'."
                                .format(FN_NAME, ", ".join("{!s}={!r}".format(k,v) for (k,v) in fn_inputs.items())))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            yield FunctionError(e)
