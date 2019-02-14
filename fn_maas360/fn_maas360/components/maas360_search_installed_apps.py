# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2019. All Rights Reserved.

"""Function implementation"""

import logging
import json
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_maas360.lib.maas360_common import MaaS360Utils
from resilient_lib.components.function_result import ResultPayload
from resilient_lib.components.resilient_common import validate_fields

CONFIG_DATA_SECTION = 'fn_maas360'
LOG = logging.getLogger(__name__)


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'maas360_search_installed_apps"""

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

    @function("maas360_search_installed_apps")
    def _maas360_search_installed_apps_function(self, event, *args, **kwargs):
        """Function: Function searches for all installed Apps across all devices by App Name, App ID and Platform."""

        def add_to_dict(key, value, params):
            """
            Adds a key-value pair to a dictionary.
            :param params
            :param key:
            :param value:
            """
            if value:
                params[key] = value

        try:
            rp = ResultPayload(CONFIG_DATA_SECTION, **kwargs)

            # Validate fields
            validate_fields(['maas360_host_url', 'maas360_billing_id', 'maas360_platform_id', 'maas360_app_id',
                             'maas360_app_version', 'maas360_app_access_key', 'maas360_username', 'maas360_auth_url',
                             'maas360_password', 'maas360_search_installed_apps_url',
                             'maas360_search_installed_apps_page_size'], self.options)

            # Get the function parameters:
            maas360_partial_app_name = kwargs.get("maas360_partial_app_name")  # text
            maas360_app_id = kwargs.get("maas360_app_id")  # text
            maas360_app_platform = self.get_select_param(kwargs.get("maas360_app_platform"))  # select, values: "iOS", "Android", "BlackBerry"

            LOG.info("maas360_partial_app_name: %s", maas360_partial_app_name)
            LOG.info("maas360_app_id: %s", maas360_app_id)
            LOG.info("maas360_app_platform: %s", maas360_app_platform)

            # Add function inputs to Basic Search params
            query_string = {}

            add_to_dict("partialAppName", maas360_partial_app_name, query_string)
            add_to_dict("appID", maas360_app_id, query_string)
            add_to_dict("platform", maas360_app_platform, query_string)

            # At least one of the search parameters should be set, otherwise we can query the whole MaaS360 database.
            if not query_string:
                raise FunctionError(u"At least one of input function fields needs to be set for running "
                                    u"Search Installed Apps function")

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

            search_installed_apps_url = self.options["maas360_search_installed_apps_url"]
            search_installed_apps_page_size = self.options["maas360_search_installed_apps_page_size"]

            # Add config params to Basic Search params
            add_to_dict("pageSize", search_installed_apps_page_size, query_string)

            yield StatusMessage("Starting the Search Installed Apps")

            maas360_utils = MaaS360Utils(host_url, billing_id, username, password, app_id, app_version, platform_id,
                                         app_access_key, auth_url, self.opts, self.options)

            apps = maas360_utils.search_installed_apps(search_installed_apps_url, query_string)
            if not apps:
                yield StatusMessage("No apps were found for the search params: {}".format(json.dumps(query_string)))
            else:
                yield StatusMessage("XXX app/s were found for the search params: {}".format(json.dumps(query_string)))

            results = rp.done(True, apps)

            LOG.info(results)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as err:
            LOG.error(err)
            yield FunctionError(err)
