# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_qradar_advisor.lib.qradar_advisor_client import QRadarAdvisorClient
import json


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'qradar_advisor_quick_search"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_qradar_advisor", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_qradar_advisor", {})

    @function("qradar_advisor_quick_search")
    def _qradar_advisor_quick_search_function(self, event, *args, **kwargs):
        """Function:
        Perform a QRadar Advisor quick search for an indicator.
        The indicator is given as qradar_advisor_search_value in the input.
        The QRadar Advisor reply is in json format.
        This function forwards the QRadar Advisor reply to Resilient server, so
        that user can process it in post-process script. """
        try:
            # Get the function parameters:
            qradar_advisor_search_value = kwargs.get("qradar_advisor_search_value")  # text

            log = logging.getLogger(__name__)
            log.info("qradar_advisor_search_value: %s", qradar_advisor_search_value)

            qradar_verify_cert = True
            if "verify_cert" in self.options and self.options["verify_cert"] == "false":
                qradar_verify_cert = False

            yield StatusMessage("starting...")
            client = QRadarAdvisorClient(qradar_host=self.options["qradar_host"],
                                         qradar_token=self.options["qradar_advisor_token"],
                                         advisor_app_id=self.options["qradar_advisor_app_id"],
                                         cafile=qradar_verify_cert,
                                         log=log)

            ret_json = client.quick_search(qradar_advisor_search_value)

            yield StatusMessage("done...")

            log.debug("Return json is:{}".format(json.dumps(ret_json)))

            results = ret_json

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            log.error(e.message)
            yield FunctionError(e.message)