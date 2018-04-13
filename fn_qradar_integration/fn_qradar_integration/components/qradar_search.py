# -*- coding: utf-8 -*-
#
# (c) Copyright IBM Corp. 2018. All Rights Reserved.
#
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_qradar_integration.util.qradar_utils import QRadarClient
from fn_qradar_integration.util import function_utils


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'qradar_search"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_qradar_integration", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_qradar_integration", {})

    @function("qradar_search")
    def _qradar_search_function(self, event, *args, **kwargs):
        """Function: Search QRadar"""
        try:
            # Get the function parameters:
            qradar_query = self.get_textarea_param(kwargs.get("qradar_query"))  # textarea
            qradar_query_param1 = kwargs.get("qradar_query_param1")  # text
            qradar_query_param2 = kwargs.get("qradar_query_param2")  # text
            qradar_query_param3 = kwargs.get("qradar_query_param3")  # text
            qradar_query_param4 = kwargs.get("qradar_query_param4")  # text
            qradar_query_param5 = kwargs.get("qradar_query_param5")  # text
            qradar_query_range_start = kwargs.get("qradar_query_range_start")  # number
            qradar_query_range_end = kwargs.get("qradar_query_range_end")  # number

            log = logging.getLogger(__name__)
            log.info("qradar_query: %s", qradar_query)
            log.info("qradar_query_param1: %s", qradar_query_param1)
            log.info("qradar_query_param2: %s", qradar_query_param2)
            log.info("qradar_query_param3: %s", qradar_query_param3)
            log.info("qradar_query_param4: %s", qradar_query_param4)
            log.info("qradar_query_param5: %s", qradar_query_param5)
            log.info("qradar_query_range_start: %s", qradar_query_range_start)
            log.info("qradar_query_range_end: %s", qradar_query_range_end)

            qradar_verify_cert = True
            if "verify_cert" in self.options and self.options["verify_cert"] == "false":
                qradar_verify_cert = False

            log.debug("Connection to {} using {}".format(self.options["host"], self.options["username"]))

            query_string = function_utils.make_query_string(qradar_query,
                                                            [qradar_query_param1,
                                                             qradar_query_param2,
                                                             qradar_query_param3,
                                                             qradar_query_param4,
                                                             qradar_query_param5])

            log.info("Running query: " + query_string)

            yield StatusMessage("starting...")
            qradar_client = QRadarClient(host=self.options["host"],
                                         username=self.options["username"],
                                         password=self.options["qradarpassword"],
                                         token=None,
                                         cafile=qradar_verify_cert)

            result = qradar_client.ariel_search(query_string,
                                                range_start=qradar_query_range_start,
                                                range_end=qradar_query_range_end)

            yield StatusMessage("done...")
            yield FunctionResult(result)
        except Exception as e:
            log.error(str(e))
            yield FunctionError()