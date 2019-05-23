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
    """Component that implements Resilient function 'maas360_action """

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

    @function("maas360_action")
    def _maas360_action_function(self, event, *args, **kwargs):
        """Function: One MaaS360 Function that performs different actions based on the chosen Menu Item Rule.
        Available actions are: - Get Software Installed - Locate Device - Lock Device - Wipe Device - Cancel Pending Wipe

        Locate Device Function performs a real-time lookup on Android devices or provides last Known location on iOS and Windows Phone devices.
        The results is latitude and longitude information.

        Get Software Installed Function gets installed software for a device.
        """

        try:
            rp = ResultPayload(CONFIG_DATA_SECTION, **kwargs)

            # Validate fields
            validate_fields(['maas360_device_id'], kwargs)

            # Get the function parameters:
            device_id = kwargs.get("maas360_device_id")  # text
            action_type = self.get_select_param(kwargs.get("maas360_action_type"))  # select, values: "Get Software Installed", "Locate Device", "Lock Device", "Wipe Device", "Cancel Pending Wipe"

            LOG.info("maas360_device_id: %s", device_id)
            LOG.info("maas360_action_type: %s", action_type)

            # Create MaaS360Utils singleton
            maas360_utils = MaaS360Utils.get_the_maas360_utils(self.opts, CONFIG_DATA_SECTION)

            if action_type == "Get Software Installed":
                yield StatusMessage("Starting the Get Software Installed function")

                validate_fields(['maas360_get_software_installed_url'], self.options)
                soft_installed_url = self.options["maas360_get_software_installed_url"]
                action_results = maas360_utils.get_software_installed(soft_installed_url, device_id)
                if not action_results:
                    yield StatusMessage("No installed software found for the device id {}".format(device_id))
                else:
                    yield StatusMessage("Installed software was found for the device id {}".format(device_id))

            elif action_type == "Locate Device":
                yield StatusMessage("Starting the Locate Device function")

                validate_fields(['maas360_locate_device_url'], self.options)
                locate_device_url = self.options["maas360_locate_device_url"]

                action_results = maas360_utils.locate_device(locate_device_url, device_id)
                if not action_results:
                    yield StatusMessage("Location for device id {} isn't available".format(device_id))
                else:
                    yield StatusMessage("Location found for device id {}".format(device_id))

            elif action_type == "Lock Device":
                yield StatusMessage("Starting the Lock Device function")

                validate_fields(['maas360_lock_device_url'], self.options)
                lock_device_url = self.options["maas360_lock_device_url"]

                action_results = maas360_utils.lock_device(lock_device_url, device_id)
                if not action_results:
                    yield StatusMessage("Locking device with device id {} wasn't successful".format(device_id))
                else:
                    yield StatusMessage("Locking device with device id {} was successful".format(device_id))

            elif action_type == "Wipe Device":
                yield StatusMessage("Starting the Wipe Device function")

                validate_fields(['maas360_wipe_device_url', 'maas360_wipe_device_notify_me',
                                 'maas360_wipe_device_notify_user', 'maas360_wipe_device_notify_others'], self.options)
                wipe_device_url = self.options["maas360_wipe_device_url"]
                notify_me = self.options["maas360_wipe_device_notify_me"]
                notify_user = self.options["maas360_wipe_device_notify_user"]
                notify_others = self.options["maas360_wipe_device_notify_others"]

                action_results = maas360_utils.wipe_device(wipe_device_url, device_id, notify_me, notify_user, notify_others)
                if not action_results:
                    yield StatusMessage("Remote Wipe Device with device id {} wasn't successful".format(device_id))
                else:
                    yield StatusMessage("Remote Wipe Device with device id {} was successful".format(device_id))

            elif action_type == "Cancel Pending Wipe":
                yield StatusMessage("Starting the Cancel Pending Wipe function")

                validate_fields(['maas360_cancel_pending_wipe_url'], self.options)
                cancel_wipe_url = self.options["maas360_cancel_pending_wipe_url"]

                action_results = maas360_utils.cancel_pending_wipe(cancel_wipe_url, device_id)
                if not action_results:
                    yield StatusMessage("Cancel outstanding Remote Wipe sent to the device"
                                        " with device id {} wasn't successful".format(device_id))
                else:
                    yield StatusMessage("Cancel outstanding Remote Wipe sent to the device"
                                        " with device id {} was successful".format(device_id))

            else:
                raise FunctionError("Chosen action type {} doesn't match any of supported MaaS360 functions".
                                    format(action_type))

            results = rp.done(True, action_results)

            LOG.info(results)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as err:
            LOG.error(err)
            yield FunctionError(err)
