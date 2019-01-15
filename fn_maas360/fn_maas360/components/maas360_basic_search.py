# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2019. All Rights Reserved.

"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_maas360.lib.maas360_common import Maas360Utils
from resilient_lib.components.function_result import ResultPayload
from resilient_lib.components.integration_errors import IntegrationError
from resilient_lib.components.resilient_common import validate_fields


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'maas360_basic_search"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_maas360", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_maas360", {})

    @function("maas360_basic_search")
    def _maas360_basic_search_function(self, event, *args, **kwargs):
        """Function: Function searches for devices by Device Name, Username, Phone Number, Platform,
        Device Status and other Device Identifiers."""

        try:
            validate_fields(['maas360_url', 'maas360_billing_id', 'maas360_platform_id', 'maas360_app_id',
                             'maas360_app_version', 'maas360_app_access_key', 'maas360_username',
                             'maas360_password'], self.options)

            # Get the function parameters:
            maas360_device_name = kwargs.get("maas360_device_name")  # text
            maas360_username = kwargs.get("maas360_username")  # text
            maas360_phone_no = kwargs.get("maas360_phone_no")  # text
            maas360_imei_meid = kwargs.get("maas360_imei_meid")  # text
            maas360_platform_name = self.get_select_param(kwargs.get("maas360_platform_name"))  # select, values: "Windows", "Mac", "iOS", "BlackBerry", "Android", "Windows Mobile", "Symbian", "Windows Phone 7", "Others"
            maas360_device_id = kwargs.get("maas360_device_id")  # text
            maas360_email = kwargs.get("maas360_email")  # text

            log = logging.getLogger(__name__)
            log.info("maas360_device_name: %s", maas360_device_name)
            log.info("maas360_username: %s", maas360_username)
            log.info("maas360_phone_no: %s", maas360_phone_no)
            log.info("maas360_imei_meid: %s", maas360_imei_meid)
            log.info("maas360_platform_name: %s", maas360_platform_name)
            log.info("maas360_device_id: %s", maas360_device_id)
            log.info("maas360_email: %s", maas360_email)

            # Read configuration settings:
            # Required
            url = self.options["maas360_url"]
            billing_id = self.options["maas360_billing_id"]
            platform_id = self.options["maas360_platform_id"]
            app_id = self.options["maas360_app_id"]
            app_version = self.options["maas360_app_version"]
            app_access_key = self.options["maas360_app_access_key"]
            username = self.options["maas360_username"]
            password = self.options["maas360_password"]

            # Optional
            basic_search_url = self.options.get("maas360_basic_search_url")
            basic_search_match = self.options.get("maas360_basic_search_match")  # int?
            basic_search_pageSize = self.options.get("maas360_basic_search_pageSize")  # int?
            basic_search_sortAttribute = self.options.get("maas360_basic_search_sortAttribute")
            basic_search_sortOrder = self.options.get("maas360_basic_search_sortOrder")

            yield StatusMessage("starting...")
            maas360_utils = Maas360Utils(url, billing_id, username, password, app_id, app_version, platform_id, app_access_key)

            #  yield StatusMessage("done...")

            results = {
                "value": "xyz"
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()