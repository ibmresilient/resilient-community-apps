# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2019. All Rights Reserved.

"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_maas360.lib.maas360_common import MaaS360Utils
from resilient_lib.components.function_result import ResultPayload
from resilient_lib.components.resilient_common import validate_fields
from resilient_lib.components.requests_common import RequestsCommon

CONFIG_DATA_SECTION = 'fn_maas360'
LOG = logging.getLogger(__name__)


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'maas360_locate_device

        Function performs a real-time lookup on Android devices or  provides Last Known location on iOS
        and Windows Phone devices. The results is latitude and longitude information.

        Locate Device returns a result in JSON format with an entry consisting of key value pairs:
            "content": {
                    "actionStatus":0, # 0:success; 1:error
                    "description":"The action was executed successfully on the device.",
                    "maas360DeviceID":"a2e13f",
                    "latitude":39.955994,
                    "locatedTime":"2018-11-05 21:34:08.0",
                    "longitude":-75.167178
                    }
    """

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)

        # Get app.config parameters.
        self.opts = opts
        self.options = opts.get(CONFIG_DATA_SECTION, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get(CONFIG_DATA_SECTION, {})

    @function("maas360_locate_device")
    def _maas360_locate_device_function(self, event, *args, **kwargs):
        """Function: Function performs a real-time lookup on Android devices or  provides Last Known location on iOS
           and Windows Phone devices. The results is latitude and longitude information."""
        try:
            rp = ResultPayload(CONFIG_DATA_SECTION, **kwargs)

            validate_fields(['maas360_host_url', 'maas360_billing_id', 'maas360_platform_id', 'maas360_app_id',
                             'maas360_app_version', 'maas360_app_access_key', 'maas360_username', 'maas360_auth_url',
                             'maas360_password', 'maas360_locate_device_url'],
                            self.options)
            validate_fields(['maas360_device_id'], kwargs)

            # Get the function parameters:
            device_id = kwargs.get("maas360_device_id")  # text

            LOG.info("maas360_device_id: %s", device_id)

            # Read configuration settings:
            host_url = self.options["maas360_host_url"]
            billing_id = self.options["maas360_billing_id"]
            platform_id = self.options["maas360_platform_id"]
            app_id = self.options["maas360_app_id"]
            app_version = self.options["maas360_app_version"]
            app_access_key = self.options["maas360_app_access_key"]
            username = self.options["maas360_username"]
            password = self.options["maas360_password"]
            auth_url = self.options["maas360_auth_url"]

            locate_device_url = self.options["maas360_locate_device_url"]

            yield StatusMessage("Starting the Locate Device function")

            # Make URL request
            rc = RequestsCommon(self.opts, self.options)

            maas360_utils = MaaS360Utils(host_url, billing_id, username, password, app_id, app_version, platform_id,
                                         app_access_key, auth_url, rc)

            location = maas360_utils.locate_device(locate_device_url, device_id)
            if not location:
                yield StatusMessage("Device location isn't available")
            else:
                yield StatusMessage("Device location found")

            results = rp.done(True, location)

            LOG.info(results)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as err:
            LOG.error(err)
            yield FunctionError(err)