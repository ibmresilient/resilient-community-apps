# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2019. All Rights Reserved.

"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'maas360_locate_device"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_maas360", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_maas360", {})

    @function("maas360_locate_device")
    def _maas360_locate_device_function(self, event, *args, **kwargs):
        """Function: Function performs a real-time lookup on Android devices or  provides Last Known location on iOS
           and Windows Phone devices. The results is latitude and longitude information."""
        try:
            # Get the function parameters:
            maas360_device_id = kwargs.get("maas360_device_id")  # text

            log = logging.getLogger(__name__)
            log.info("maas360_device_id: %s", maas360_device_id)

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