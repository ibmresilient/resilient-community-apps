# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
import fn_maas360.util.selftest as selftest


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'maas360_locate_device"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_maas360", {})
        #selftest.selftest_function(opts)

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
            maas360_deviceid = kwargs.get("maas360_deviceid")  # text

            log = logging.getLogger(__name__)
            log.info("maas360_deviceid: %s", maas360_deviceid)

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