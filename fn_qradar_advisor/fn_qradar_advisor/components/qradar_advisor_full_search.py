# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
#
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
#

"""Function implementation"""

import json
import logging

from fn_qradar_advisor.lib import stix_utils
from fn_qradar_advisor.lib import stix_tree
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_qradar_advisor.lib.qradar_advisor_client import QRadarAdvisorClient


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'qradar_advisor_full_search"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_qradar_advisor", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_qradar_advisor", {})

    @function("qradar_advisor_full_search")
    def _qradar_advisor_full_search_function(self, event, *args, **kwargs):
        """Function: Perform a QRadar Advisor full search on an indicator.
        The indicator is given as the qradar_advisor_search_value of the input.
        Another input is qradar_advisor_result_stage. This can be "stage1", "stage2", or "stage3".
        The return from QRadar Advisor is a report in stix format.
        Then this function calls util funtions from lib to
        1. extract observables from objects
        2. generate a html representation of the stix objects
        3. generate a summary
        All of the above 3 will be returned to Resilient server, together with the raw stix
        """
        try:
            # Get the function parameters:
            qradar_advisor_search_value = kwargs.get("qradar_advisor_search_value")  # text
            qradar_advisor_result_stage = self.get_select_param(kwargs.get("qradar_advisor_result_stage"))  # select, values: "stage1", "stage2", "stage3"

            log = logging.getLogger(__name__)
            log.info("qradar_advisor_search_value: %s", qradar_advisor_search_value)
            log.info("qradar_advisor_result_stage: %s", qradar_advisor_result_stage)

            qradar_verify_cert = True
            if "verify_cert" in self.options and self.options["verify_cert"] == "false":
                qradar_verify_cert = False

            yield StatusMessage("starting...")

            # Warn the user
            yield  StatusMessage("Watson Search with Local Context could take up to 15 minutes...")

            stix_json = None

            client = QRadarAdvisorClient(qradar_host=self.options["qradar_host"],
                                         qradar_token=self.options["qradar_advisor_token"],
                                         advisor_app_id=self.options["qradar_advisor_app_id"],
                                         cafile=qradar_verify_cert,
                                         log=log)

            full_search_timeout = self.options.get("full_search_timeout", 1200)
            full_search_period = self.options.get("full_search_period", 5)

            log.debug("Using timeout: {}".format(str(full_search_timeout)))
            log.debug("Using period: {}".format(str(full_search_period)))

            client.full_search_timeout = int(full_search_timeout)
            client.full_search_period = int(full_search_period)

            client.set_full_search_stage(qradar_advisor_result_stage)

            stix_json = client.full_search(qradar_advisor_search_value)

            #
            # extract list of observables from this stix bundle
            #
            observables = stix_utils.get_observables(stix_json=stix_json,
                                                     log=log)
            #
            # generate a folder-tree like structure in html for this stix bundle
            #
            html_str = stix_tree.get_html(stix_json, log)

            yield StatusMessage("Returning {} observables".format(str(len(observables))))

            #
            # no insights
            #
            summary = "Watson Search with Local Context of indicator {} returns {} observables.".format(qradar_advisor_search_value,
                                                                                                        str(len(observables)))
            if len(observables) == 1:
                summary = "Watson Search with Local Context of indicator {} returns {} observable.".format(qradar_advisor_search_value,
                                                                                                           str(len(observables)))

            results = {
                "observables": observables,
                "note": html_str,
                "summary": summary,
                "stix": stix_json
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            log.error(e.message)
            yield FunctionError(e.message)
