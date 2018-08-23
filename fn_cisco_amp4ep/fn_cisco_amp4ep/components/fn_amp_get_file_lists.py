# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import json
from datetime import datetime

from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_cisco_amp4ep.lib.amp_client import Ampclient
from fn_cisco_amp4ep.lib.helpers import validate_opts, validate_params

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_amp_get_file_lists"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_cisco_amp4ep", {})
        validate_opts(self)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_cisco_amp4ep", {})
        validate_opts(self)

    @function("fn_amp_get_file_lists")
    def _fn_amp_get_file_lists_function(self, event, *args, **kwargs):
        """Function: Returns a list of simple custom detection file lists. You can filter this list by name."""
        try:
            # Get the function parameters:
            amp_scd_name = kwargs.get("amp_scd_name")  # text
            amp_limit = kwargs.get("amp_limit")  # number
            amp_offset = kwargs.get("amp_offset")  # number

            log = logging.getLogger(__name__)
            log.info("amp_scd_name: %s", amp_scd_name)
            log.info("amp_limit: %s", amp_limit)
            log.info("amp_offset: %s", amp_offset)

            yield StatusMessage("Starting...")

            params = {"name": amp_scd_name, "limit": amp_limit, "offset": amp_offset  }

            validate_params(params)

            amp = Ampclient(self.options)

            yield StatusMessage("Running Cisco AMP for endpoints get file lists ...")
            rtn = amp.get_file_lists(**params)
            query_execution_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            # Add in "query_execution_time" and "ip_address" to result to facilitate post-processing.
            results = {"file_lists": rtn, "query_execution_time": query_execution_time}
            yield StatusMessage("Returning 'file lists' results.")

            yield StatusMessage("Done...")

            log.debug(json.dumps(results))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()