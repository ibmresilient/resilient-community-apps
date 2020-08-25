# -*- coding: utf-8 -*-
#
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
#
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload
from fn_splunk_integration.util import function_utils, splunk_utils

SECTION_HDR = "fn_splunk_integration"

class FunctionComponent(ResilientComponent):

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get(SECTION_HDR, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get(SECTION_HDR, {})

    @function("splunk_add_intel_item")
    def _splunk_add_intel_item_function(self, event, *args, **kwargs):
        """Function: Add a new splunk es threat intelligence item to the collections
        splunk_thread_intel_type: ip_intel, user_intel,...., or registry_intel
        splunk_query_param1: field1 name of the dict used to create the item;
        splunk_query_param2: field1 value;
        splunk_query_param3: field2 name;
        splunk_query_param4: field2 value;
        ....."""
        try:
            # Get the function parameters:
            splunk_threat_intel_type = kwargs.get("splunk_threat_intel_type")  # text
            splunk_query_param1 = kwargs.get("splunk_query_param1")  # text
            splunk_query_param2 = kwargs.get("splunk_query_param2")  # text
            splunk_query_param3 = kwargs.get("splunk_query_param3")  # text
            splunk_query_param4 = kwargs.get("splunk_query_param4")  # text
            splunk_query_param5 = kwargs.get("splunk_query_param5")  # text
            splunk_query_param6 = kwargs.get("splunk_query_param6")  # text
            splunk_query_param7 = kwargs.get("splunk_query_param7")  # text
            splunk_query_param8 = kwargs.get("splunk_query_param8")  # text
            splunk_query_param9 = kwargs.get("splunk_query_param9")  # text
            splunk_query_param10 = kwargs.get("splunk_query_param10")  # text

            splunk_verify_cert = True
            if "verify_cert" in self.options and self.options["verify_cert"] == "false":
                splunk_verify_cert = False

            log = logging.getLogger(__name__)
            log.info("splunk_threat_intel_type: %s", splunk_threat_intel_type)
            log.info("splunk_query_param1: %s", splunk_query_param1)
            log.info("splunk_query_param2: %s", splunk_query_param2)
            log.info("splunk_query_param3: %s", splunk_query_param3)
            log.info("splunk_query_param4: %s", splunk_query_param4)
            log.info("splunk_query_param5: %s", splunk_query_param5)
            log.info("splunk_query_param6: %s", splunk_query_param6)
            log.info("splunk_query_param7: %s", splunk_query_param7)
            log.info("splunk_query_param8: %s", splunk_query_param8)
            log.info("splunk_query_param9: %s", splunk_query_param9)
            log.info("splunk_query_param10: %s", splunk_query_param10)
            log.info("splunk_verify_cert: %s", str(splunk_verify_cert))

            yield StatusMessage("starting...")

            result_payload = ResultPayload(SECTION_HDR, **kwargs)

            # build the dict used to add threat intel item
            item_dict = function_utils.make_item_dict([splunk_query_param1,
                                                       splunk_query_param2,
                                                       splunk_query_param3,
                                                       splunk_query_param4,
                                                       splunk_query_param5,
                                                       splunk_query_param6,
                                                       splunk_query_param7,
                                                       splunk_query_param8,
                                                       splunk_query_param9,
                                                       splunk_query_param10])
            # log it for debug
            log.debug("item dict: {}".format(str(item_dict)))

            splnk_utils = splunk_utils.SplunkUtils(host=self.options["host"],
                                                   port=self.options["port"],
                                                   username=self.options["username"],
                                                   password=self.options["splunkpassword"],
                                                   verify=splunk_verify_cert)

            splunk_result = splnk_utils.add_threat_intel_item(threat_type=splunk_threat_intel_type,
                                                       threat_dict=item_dict,
                                                       cafile=splunk_verify_cert)

            yield StatusMessage("done...")

            # Produce a FunctionResult with the results
            yield FunctionResult(result_payload.done(True, splunk_result.get('content', {})))
        except Exception as e:
            log.error("Function execution throws exception {}".format(str(e)))
            yield FunctionError()