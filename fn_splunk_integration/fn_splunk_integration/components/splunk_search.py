# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""AppFunction implementation"""

from fn_splunk_integration.util.splunk_utils import SplunkServers, SplunkClient
from fn_splunk_integration.util.splunk_constants import QUERY_PARAM, PACKAGE_NAME
from fn_splunk_integration.util.function_utils import make_query_string, get_servers_list
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields

FN_NAME = "splunk_search"

class FunctionComponent(AppFunctionComponent):
    """Component that implements SOAR function 'splunk_search"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)
        self.servers_list = get_servers_list(opts)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """Function: Search"""
        try:
            yield self.status_message("Starting App Function: '{}'".format(FN_NAME))

            validate_fields(["splunk_query"], fn_inputs)

            splunk_query_param = []
            for input in fn_inputs._asdict():
                if QUERY_PARAM in input:
                    splunk_query_param.append(fn_inputs._asdict().get(input))

            options = SplunkServers.splunk_label_test(fn_inputs.splunk_label, self.servers_list)

            # Log all the info
            self.LOG.info(str(fn_inputs))

            splunk_verify_cert = False if options.get("verify_cert", "").lower() != "true" else True

            query_string = make_query_string(fn_inputs.splunk_query, splunk_query_param)

            self.LOG.info("Splunk query to be executed: %s" % query_string)
            self.LOG.info("Splunk host: %s, port: %s, username: %s",
                     options.get("host"), options.get("port"), options.get("username"))

            splunk_client = SplunkClient(options.get("host"),
                                         port=options.get("port"),
                                         username=options.get("username"),
                                         password=options.get("splunkpassword"),
                                         verify=splunk_verify_cert)
            if fn_inputs.splunk_max_return:
                splunk_client.set_max_return(fn_inputs.splunk_max_return)

            splunk_result = splunk_client.execute_query(query_string)
            self.LOG.debug(splunk_result)

            yield self.status_message("Finished running App Function: '{}'".format(FN_NAME))

            # Produce a FunctionResult with the return value
            yield FunctionResult(splunk_result.get('events', {}))
        except Exception as err:
            yield FunctionResult({}, success=False, reason=str(err))
