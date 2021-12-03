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
from fn_splunk_integration.util.splunk_constants import QUERY_PARAM, PACKAGE_NAME
from fn_splunk_integration.util.splunk_utils import SplunkServers

log = logging.getLogger(__name__)

class FunctionComponent(ResilientComponent):

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.servers_list = function_utils.get_servers_list(opts, "init")
        function_utils.update_splunk_servers_select_list(opts, self.servers_list)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.servers_list = function_utils.get_servers_list(opts, "reload")

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
            params_list = []
            # Get the function parameters:
            splunk_threat_intel_type = kwargs.get("splunk_threat_intel_type")  # text
            # splunk_query_param1-10
            for i in range(1,11):
                locals()[f'{QUERY_PARAM}{i}'] = kwargs.get(QUERY_PARAM+str(i))
                params_list.append(locals()[f'{QUERY_PARAM}{i}'])

            splunk_label = kwargs.get("splunk_label")                          # text

            options = SplunkServers.splunk_label_test(splunk_label, self.servers_list)

            splunk_verify_cert = True
            if "verify_cert" in options and options["verify_cert"] == "false":
                splunk_verify_cert = False

            # Log all the info
            log.info("splunk_threat_intel_type: %s", splunk_threat_intel_type)
            # Log splunk_query_param1-10
            for i in range(1,11):
                log.info("{}{}: {}".format(QUERY_PARAM, str(i), locals().get(QUERY_PARAM+str(i))))
            log.info("splunk_verify_cert: %s", str(splunk_verify_cert))
            log.info("splunk_label: %s", splunk_label)

            wf_instance_id = event.message.get("workflow_instance", {}).get("workflow_instance_id", "no instance id found")
            yield StatusMessage("Starting 'splunk_add_intel_item' that was running in workflow '{}'".format(wf_instance_id))

            result_payload = ResultPayload(PACKAGE_NAME, **kwargs)

            # build the dict used to add threat intel item
            item_dict = function_utils.make_item_dict(params_list)
            # log it for debug
            log.debug("item dict: {}".format(str(item_dict)))

            splnk_utils = splunk_utils.SplunkUtils(host=options["host"],
                                                   port=options["port"],
                                                   username=options["username"],
                                                   password=options["splunkpassword"],
                                                   verify=splunk_verify_cert)

            splunk_result = splnk_utils.add_threat_intel_item(threat_type=splunk_threat_intel_type,
                                                       threat_dict=item_dict,
                                                       cafile=splunk_verify_cert)

            yield StatusMessage("Finished 'splunk_add_intel_item' that was running in workflow '{}'".format(wf_instance_id))

            # Produce a FunctionResult with the results
            yield FunctionResult(result_payload.done(True, splunk_result.get('content', {})))
        except Exception as e:
            log.error("Function execution throws exception {}".format(str(e)))
            yield FunctionError()
