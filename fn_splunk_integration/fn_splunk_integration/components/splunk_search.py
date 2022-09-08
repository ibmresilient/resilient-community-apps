# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""AppFunction implementation"""

from fn_splunk_integration.util.splunk_constants import QUERY_PARAM, PACKAGE_NAME
from fn_splunk_integration.util.function_utils import make_query_string, get_servers_list, function_basics
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

        yield self.status_message("Starting App Function: '{}'".format(FN_NAME))

        validate_fields(["splunk_query"], fn_inputs)

        splunk_query_param = []
        for input in fn_inputs._asdict():
            if QUERY_PARAM in input:
                num = int(input.replace(QUERY_PARAM,''))-1
                # Add the param in the correct position in the list based on param number
                splunk_query_param.insert(num, fn_inputs._asdict().get(input))

        # Build query string with params
        query_string = make_query_string(fn_inputs.splunk_query, splunk_query_param)

        self.LOG.info("Splunk query to be executed: %s" % query_string)

        splunk, splunk_verify_cert = function_basics(fn_inputs, self.servers_list, utils=False)

        if fn_inputs.splunk_max_return:
            splunk.set_max_return(fn_inputs.splunk_max_return)

        splunk_result = splunk.execute_query(query_string)
        self.LOG.debug(splunk_result)

        yield self.status_message("Finished running App Function: '{}'".format(FN_NAME))

        # Produce a FunctionResult with the return value
        yield FunctionResult(splunk_result.get('events', {}))
