# -*- coding: utf-8 -*-
#
# Copyright IBM Corp. - Confidential Information
#
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from function_utils import make_query_string as make_query_string
import splunk_utils

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'splunk_search"""

    # Member variables
    splunk_password = None
    app_config = None

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_splunk_integration", {})
        self.app_config = opts.get(splunk_utils.SPLUNK_SECTION, {})

        #
        # Somehow keyrings only works for the resilient section
        #
        args = dict(opts)
        self.splunk_password = args["resilient"]["splunkpassword"]

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_splunk_integration", {})

    @function("splunk_search")
    def _splunk_search_function(self, event, *args, **kwargs):
        """Function: """
        try:
            # Get the function parameters:
            splunk_query = self.get_textarea_param(kwargs.get("splunk_query"))  # textarea
            splunk_query_param1 = kwargs.get("splunk_query_param1")  # text
            splunk_query_param2 = kwargs.get("splunk_query_param2")  # text
            splunk_query_param3 = kwargs.get("splunk_query_param3")  # text
            splunk_query_param4 = kwargs.get("splunk_query_param4")  # text
            splunk_query_param5 = kwargs.get("splunk_query_param5")  # text
            splunk_max_return = kwargs.get("splunk_max_return")      # number

            log = logging.getLogger(__name__)
            log.info("splunk_query: %s", splunk_query)
            log.info("splunk_query_param1: %s", splunk_query_param1)
            log.info("splunk_query_param2: %s", splunk_query_param2)
            log.info("splunk_query_param3: %s", splunk_query_param3)
            log.info("splunk_query_param4: %s", splunk_query_param4)
            log.info("splunk_query_param5: %s", splunk_query_param5)
            log.info("splunk_max_return: %d", splunk_max_return)

            splunk_query_param = [splunk_query_param1, splunk_query_param2, splunk_query_param3,
                                  splunk_query_param4, splunk_query_param5]
            query_string = make_query_string(splunk_query, splunk_query_param)

            log.info("Splunk query to be executed: %s" % query_string)
            log.info("Splunk host: %s, port: %s, username: %s",
                     self.app_config["host"], self.app_config["port"], self.app_config["username"])

            yield StatusMessage("starting...")
            splunk_client = splunk_utils.SplunkClient(self.app_config["host"],
                                                      port=int(self.app_config["port"]),
                                                      username=self.app_config["username"],
                                                      password=self.splunk_password)
            if splunk_max_return:
                splunk_client.set_max_return(splunk_max_return)

            result = splunk_client.execute_query(query_string)
            log.info("Splunk search returns: " + str(result))

            yield StatusMessage("done...")

            # Produce a FunctionResult with the return value
            yield FunctionResult(result)
        except Exception as e:
            yield FunctionError(str(e))