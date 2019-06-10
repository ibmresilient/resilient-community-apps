# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2019. All Rights Reserved.

"""Function implementation"""

import logging
import json
from fn_maas360.lib.maas360_common import MaaS360Utils
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib.components.function_result import ResultPayload
from resilient_lib.components.resilient_common import validate_fields

CONFIG_DATA_SECTION = 'fn_maas360'
LOG = logging.getLogger(__name__)


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'maas360_basic_search

        Function searches for devices by Device Name, Username, Phone Number, Platform, Device Status and other
        Device Identifiers.

        An example of optional search parameters are:

            partialDeviceName - Partial (Starts with) or full Device Name string that needs to be searched for - example "glindsey-ADR6400L"
            partialUsername - Partial (Starts with) or full Username string that needs to be searched for - example "dlindsey"
            partialPhoneNumber - Partial (Starts with) or full Phone Number that needs to be searched for - example "+18588885305"
            imeiMeid - Full IMEI or MEID of the device - example "99000032580168"
            platformName - Windows,  Mac , iOS,  BlackBerry,  Android , Windows Mobile,  Symbian,  Windows Phone 7,  Others 
            maas360DeviceId - Full MaaS360 Device ID string that needs to be searched for - example "androidc60775214"
            email - Full Email address string that needs to be searched for - example "TEST@EXAMPLE.COM""

            match - 0 (Default) indicates Partial match for Device Name, Username, Phone Number, 1 indicates Exact match
            pageSize - Limit number of devices returned at one time. Allowed page sizes: 25, 50, 100, 200, 250. Default value: 250
            sortAttribute - Possible values: lastReported (Default) or installedDate
            sortOrder - Possible values: asc or dsc (Default)
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

        # Reload app.config parameters.
        self.opts = opts
        self.options = opts.get(CONFIG_DATA_SECTION, {})

        # Reload options in maas360_utils singleton and reconnect to get a new token
        maas360_utils = MaaS360Utils.get_the_maas360_utils()
        maas360_utils.reload_options(opts)
        maas360_utils.reconnect()

    @function("maas360_basic_search")
    def _maas360_basic_search_function(self, event, *args, **kwargs):
        """Function: Function searches for devices by Device Name, Username, Phone Number, Platform,
        Device Status and other Device Identifiers."""

        try:
            rp = ResultPayload(CONFIG_DATA_SECTION, **kwargs)

            # Validate fields
            validate_fields(['maas360_basic_search_page_size'], self.options)

            # Get the function parameters:
            partial_device_name = kwargs.get("maas360_partial_device_name")  # text
            partial_username = kwargs.get("maas360_partial_username")  # text
            partial_phone_no = kwargs.get("maas360_partial_phone_no")  # text
            imei_meid = kwargs.get("maas360_imei_meid")  # text
            platform_name = self.get_select_param(kwargs.get("maas360_platform_name"))  # select, values: "Windows", "Mac", "iOS", "BlackBerry", "Android", "Windows Mobile", "Symbian", "Windows Phone 7", "Others"
            device_id = kwargs.get("maas360_device_id")  # text
            email = kwargs.get("maas360_email")  # text

            LOG.info("maas360_partial_device_name: %s", partial_device_name)
            LOG.info("maas360_partial_username: %s", partial_username)
            LOG.info("maas360_partial_phone_no: %s", partial_phone_no)
            LOG.info("maas360_imei_meid: %s", imei_meid)
            LOG.info("maas360_platform_name: %s", platform_name)
            LOG.info("maas360_device_id: %s", device_id)
            LOG.info("maas360_email: %s", email)

            # Add function inputs to Basic Search params
            query_string = {}

            MaaS360Utils.add_to_dict("partialDeviceName", partial_device_name, query_string)
            MaaS360Utils.add_to_dict("partialUsername", partial_username, query_string)
            MaaS360Utils.add_to_dict("partialPhoneNumber", partial_phone_no, query_string)
            MaaS360Utils.add_to_dict("imeiMeid", imei_meid, query_string)
            MaaS360Utils.add_to_dict("platformName", platform_name, query_string)
            MaaS360Utils.add_to_dict("maas360DeviceId", device_id, query_string)
            MaaS360Utils.add_to_dict("email", email, query_string)

            # At least one of the search parameters should be set, otherwise we can query the whole MaaS360 database.
            if not query_string:
                raise FunctionError(u"At least one of input function fields needs to be set for running "
                                    u"Basic Search function")

            # Read configuration settings:
            match = self.options.get("maas360_basic_search_match")
            page_size = self.options.get("maas360_basic_search_page_size")
            sort_attribute = self.options.get("maas360_basic_search_sort_attribute")
            sort_order = self.options.get("maas360_basic_search_sort_order")

            # Add config params to Basic Search params
            MaaS360Utils.add_to_dict("match", match, query_string)
            MaaS360Utils.add_to_dict("pageSize", page_size, query_string)
            MaaS360Utils.add_to_dict("sortAttribute", sort_attribute, query_string)
            MaaS360Utils.add_to_dict("sortOrder", sort_order, query_string)

            yield StatusMessage("Starting the Basic Search")

            # Create MaaS360Utils singleton
            maas360_utils = MaaS360Utils.get_the_maas360_utils(self.opts, CONFIG_DATA_SECTION)
            devices = maas360_utils.basic_search(query_string)
            if not devices:
                yield StatusMessage("No devices were found for the search params: {}".format(json.dumps(query_string)))

            count = devices.get("count")
            if not count:
                yield StatusMessage("No devices were found for the search params: {}".format(json.dumps(query_string)))
            else:
                yield StatusMessage("{} device/s were found for the search params: {}".format(count, json.dumps(query_string)))

            results = rp.done(True, devices)

            yield FunctionResult(results)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as err:
            LOG.error(err)
            yield FunctionError(err)
