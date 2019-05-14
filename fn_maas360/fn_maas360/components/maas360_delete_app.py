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
    """Component that implements Resilient function 'maas360_delete_app"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)

        # Get app.config parameters.
        self.opts = opts
        self.options = opts.get(CONFIG_DATA_SECTION, {})

        # Create MaaS360Utils
        MaaS360Utils.get_the_maas360_utils(opts, CONFIG_DATA_SECTION)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        # Reload app.config parameters.
        self.opts = opts
        self.options = opts.get(CONFIG_DATA_SECTION, {})

        # Reload options in maas360_utils and reconnect to get a new token
        maas360_utils = MaaS360Utils.get_the_maas360_utils(opts, CONFIG_DATA_SECTION)
        maas360_utils.reload_options(opts)
        maas360_utils.reconnect()

    @function("maas360_delete_app")
    def _maas360_delete_app_function(self, event, *args, **kwargs):
        """Function: Function stops all distributions of the app and deletes the app."""
        try:
            rp = ResultPayload(CONFIG_DATA_SECTION, **kwargs)

            # Validate fields
            # validate_fields(['maas360_host_url', 'maas360_billing_id', 'maas360_platform_id', 'maas360_app_id',
            #                  'maas360_app_version', 'maas360_app_access_key', 'maas360_username', 'maas360_auth_url',
            #                  'maas360_password', 'maas360_delete_app_url'], self.options)
            validate_fields(['maas360_delete_app_url'], self.options)
            validate_fields(['maas360_app_id', 'maas360_app_type'], kwargs)

            # Get the function parameters:
            app_type = self.get_select_param(kwargs.get("maas360_app_type"))  # select, values: "iOS Enterprise Application", "iOS App Store Application", "Android Enterprise Application", "Android Market Application"
            installed_app_id = kwargs.get("maas360_app_id")  # text

            LOG.info("maas360_app_type: %s", app_type)
            LOG.info("maas360_app_id: %s", installed_app_id)

            # Read configuration settings:
            # host_url = self.options["maas360_host_url"]
            # billing_id = self.options["maas360_billing_id"]
            # platform_id = self.options["maas360_platform_id"]
            # app_id = self.options["maas360_app_id"]
            # app_version = self.options["maas360_app_version"]
            # app_access_key = self.options["maas360_app_access_key"]
            # username = self.options["maas360_username"]
            # password = self.options["maas360_password"]
            # auth_url = self.options["maas360_auth_url"]

            delete_app_url = self.options["maas360_delete_app_url"]

            yield StatusMessage("Starting the Delete App")

            # maas360_utils = MaaS360Utils(host_url, billing_id, username, password, app_id, app_version, platform_id,
            #                              app_access_key, auth_url, self.opts, self.options)

            maas360_utils = MaaS360Utils.get_the_maas360_utils(self.opts, CONFIG_DATA_SECTION)

            delete_app_results = maas360_utils.delete_app(delete_app_url, app_type, installed_app_id)
            if not delete_app_results:
                yield StatusMessage("Delete App for app id {} wasn't successful".format(installed_app_id))
            else:
                yield StatusMessage("Delete App for app id {} was successful".format(installed_app_id))

            results = rp.done(True, delete_app_results)

            LOG.info(results)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as err:
            LOG.error(err)
            yield FunctionError(err)
