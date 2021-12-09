# -*- coding: utf-8 -*-
#
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
#
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload
from fn_splunk_integration.util.function_utils import make_query_string, get_servers_list
from fn_splunk_integration.util.splunk_constants import QUERY_PARAM, PACKAGE_NAME
from fn_splunk_integration.util.splunk_utils import SplunkServers, SplunkClient

log = logging.getLogger(__name__)

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'splunk_search"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.servers_list = get_servers_list(opts)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.servers_list = get_servers_list(opts)

    @function("splunk_search")
    def _splunk_search_function(self, event, *args, **kwargs):
        """Function: """
        try:
            splunk_query_param = []
            # Get the function parameters:
            splunk_query = self.get_textarea_param(kwargs.get("splunk_query"))  # textarea
            # splunk_query_param1-10
            for i in range(1,11):
                locals()[f'{QUERY_PARAM}{i}'] = kwargs.get(QUERY_PARAM+str(i))
                splunk_query_param.append(locals()[f'{QUERY_PARAM}{i}'])
            splunk_max_return = kwargs.get("splunk_max_return")      # number
            splunk_label = kwargs.get("splunk_label")                # text

            options = SplunkServers.splunk_label_test(splunk_label, self.servers_list)

            # Log all the info
            log.info("splunk_query: %s", splunk_query)
            # Log splunk_query_param1-10
            for i in range(1,11):
                log.info("{}{}: {}".format(QUERY_PARAM, str(i), locals().get(QUERY_PARAM+str(i))))
            log.info("splunk_max_return: %d", splunk_max_return)
            log.info("splunk_label: %s", splunk_label)

            result_payload = ResultPayload(PACKAGE_NAME, **kwargs)

            splunk_verify_cert = False if options.get("verify_cert", "").lower() != "true" else True

            query_string = make_query_string(splunk_query, splunk_query_param)

            log.info("Splunk query to be executed: %s" % query_string)
            log.info("Splunk host: %s, port: %s, username: %s",
                     options.get("host"), options.get("port"), options.get("username"))

            wf_instance_id = event.message.get("workflow_instance", {}).get("workflow_instance_id", "no instance id found")
            yield StatusMessage("Starting 'splunk_search' that was running in workflow '{}'".format(wf_instance_id))

            splunk_client = SplunkClient(options.get("host"),
                                         port=options.get("port"),
                                         username=options.get("username"),
                                         password=options.get("splunkpassword"),
                                         verify=splunk_verify_cert)
            if splunk_max_return:
                splunk_client.set_max_return(splunk_max_return)

            splunk_result = splunk_client.execute_query(query_string)
            log.debug(splunk_result)

            yield StatusMessage("Finished 'splunk_search' that was running in workflow '{}'".format(wf_instance_id))

            # Produce a FunctionResult with the return value
            yield FunctionResult(result_payload.done(True, splunk_result.get('events', {})))
        except Exception as e:
            log.error("Function execution throws exception {}".format(str(e)))
            yield FunctionError(str(e))
