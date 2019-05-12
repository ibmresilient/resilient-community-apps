# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_cb_protection.util.bit9_client import CbProtectClient
from resilient_lib import validate_fields

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'bit9_file_instance_update"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_cb_protection", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_cb_protection", {})

    @function("bit9_file_instance_update")
    def _bit9_file_instance_update_function(self, event, *args, **kwargs):
        """Function: Update the approval state of a file instance"""
        try:
            validate_fields(["bit9_file_instance_id", "bit9_file_instance_localstate"], kwargs)
            # Get the function parameters:
            bit9_file_instance_id = kwargs.get("bit9_file_instance_id")  # number
            bit9_file_instance_localstate = kwargs.get("bit9_file_instance_localstate")  # number

            log = logging.getLogger(__name__)
            log.info(u"bit9_file_instance_id: %s", bit9_file_instance_id)
            log.info(u"bit9_file_instance_localstate: %s", bit9_file_instance_localstate)

            payload = {
                "localState": bit9_file_instance_localstate
            }

            bit9_client = CbProtectClient(self.options)
            results = bit9_client.update_file_instance(bit9_file_instance_id, payload)

            log.info("Done")
            log.debug(results)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()