# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2019. All Rights Reserved.

"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_maas360.lib.maas360_common import MaaS360Utils
from resilient_lib.components.function_result import ResultPayload
from resilient_lib.components.resilient_common import validate_fields

CONFIG_DATA_SECTION = 'fn_maas360'
LOG = logging.getLogger(__name__)


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'maas360_stop_app_distribution"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)

        # Get app.config parameters.
        self.opts = opts
        self.options = opts.get(CONFIG_DATA_SECTION, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        # Reload app.config parameters.
        self.opts = opts
        self.options = opts.get(CONFIG_DATA_SECTION, {})

        # Reload options in maas360_utils singleton and reconnect to get a new token
        maas360_utils = MaaS360Utils.get_the_maas360_utils()
        maas360_utils.reload_options(opts)
        maas360_utils.reconnect()

    @function("maas360_stop_app_distribution")
    def _maas360_stop_app_distribution_function(self, event, *args, **kwargs):
        """Function: Function stops a specific distributions of an app."""

        try:
            rp = ResultPayload(CONFIG_DATA_SECTION, **kwargs)

            # Validate fields
            validate_fields(['maas360_app_id', 'maas360_app_type', 'maas360_target_devices'], kwargs)

            # Get the function parameters:
            app_type = self.get_select_param(kwargs.get("maas360_app_type"))  # select, values: "iOS Enterprise Application", "iOS App Store Application", "Android Enterprise Application", "Android Market Application"
            installed_app_id = kwargs.get("maas360_app_id")  # text
            target_devices = self.get_select_param(kwargs.get("maas360_target_devices"))  # select, values: "All Devices", "Device Group", "Specific Device"
            device_id = kwargs.get("maas360_device_id")  # text
            device_group_id = kwargs.get("maas360_device_group_id")  # text

            LOG.info("maas360_app_type: %s", app_type)
            LOG.info("maas360_app_id: %s", installed_app_id)
            LOG.info("maas360_target_devices: %s", target_devices)
            LOG.info("maas360_device_id: %s", device_id)
            LOG.info("maas360_device_group_id: %s", device_group_id)

            if target_devices == "Device Group" and device_group_id is None:
                raise FunctionError(u"maas360_device_group_id must be defined")
            if target_devices == "Specific Device" and device_id is None:
                raise FunctionError(u"maas360_device_id must be defined")

            yield StatusMessage("Starting the Stop App Distribution")

            # Create MaaS360Utils singleton
            maas360_utils = MaaS360Utils.get_the_maas360_utils(self.opts, CONFIG_DATA_SECTION)
            stop_app_results = maas360_utils.stop_app_distribution(app_type, installed_app_id, target_devices,
                                                                   device_id, device_group_id)
            if not stop_app_results:
                yield StatusMessage("Stop App Distribution for app id {} wasn't successful".format(installed_app_id))
            else:
                yield StatusMessage("Stop App Distribution for app id {} was successful".format(installed_app_id))

            results = rp.done(True, stop_app_results)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as err:
            LOG.error(err)
            yield FunctionError(err)
