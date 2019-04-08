# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'maas360_delete_app"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_maas360", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_maas360", {})

    @function("maas360_delete_app")
    def _maas360_delete_app_function(self, event, *args, **kwargs):
        """Function: Function stops all distributions of the app and deletes the app."""
        try:
            # Get the function parameters:
            maas360_app_type = self.get_select_param(kwargs.get("maas360_app_type"))  # select, values: "iOS Enterprise Application", "iOS App Store Application", "Android Enterprise Application", "Android Market Application"
            maas360_app_id = kwargs.get("maas360_app_id")  # text

            log = logging.getLogger(__name__)
            log.info("maas360_app_type: %s", maas360_app_type)
            log.info("maas360_app_id: %s", maas360_app_id)

            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE
            #  yield StatusMessage("starting...")
            #  yield StatusMessage("done...")

            results = {
                "value": "xyz"
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()