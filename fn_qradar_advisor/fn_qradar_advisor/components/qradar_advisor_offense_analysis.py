# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import json
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_qradar_advisor.lib.qradar_advisor_client import QRadarAdvisorClient
from fn_qradar_advisor.lib import stix_utils
from fn_qradar_advisor.lib import stix_tree


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'qradar_advisor_offense_analysis"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_qradar_advisor", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_qradar_advisor", {})

    @function("qradar_advisor_offense_analysis")
    def _qradar_advisor_offense_analysis_function(self, event, *args, **kwargs):
        """Function:
        This function performs two tasks:
        1. call the QRadar Advisor REST API to retrieve insights for a given QRadar offense
        2. call the QRadar Advisor REST API to perform analysis on the QRadar offense
        The input is qradar_offense_id in the input.
        The reply from QRadar Advisor analysis is in stix format. This function then
        1. extract the observables from the stix objects
        2. generate a html representation for the stix
        The return to Resilient server includes the above two, together with the raw replies for
        offense insights and offense analysis."""
        try:
            # Get the function parameters:
            qradar_offense_id = kwargs.get("qradar_offense_id")  # text
            qradar_advisor_result_stage = self.get_select_param(kwargs.get("qradar_advisor_result_stage"))  # select, values: "stage1", "stage2", "stage3"
            qradar_analysis_restart_if_existed = kwargs.get("qradar_analysis_restart_if_existed")  # boolean

            log = logging.getLogger(__name__)
            log.info("qradar_offense_id: %s", qradar_offense_id)
            log.info("qradar_advisor_result_stage: %s", qradar_advisor_result_stage)
            log.info("qradar_analysis_restart_if_existed: %s", qradar_analysis_restart_if_existed)

            qradar_verify_cert = True
            if "verify_cert" in self.options and self.options["verify_cert"] == "false":
                qradar_verify_cert = False

            yield StatusMessage("starting...")

            if qradar_analysis_restart_if_existed:
                # User wants restart a new analysis. Warn him/her it could take some time
                yield StatusMessage("Restarting a new analysis. It could take up to 15 minutes...")

            offense_analysis_timeout = int(self.options.get("offense_analysis_timeout", 1200))
            offense_analysis_period = int(self.options.get("offense_analysis_period", 5))

            log.debug("Using timeout: {}".format(str(offense_analysis_timeout)))
            log.debug("Using period: {}".format(str(offense_analysis_period)))

            client = QRadarAdvisorClient(qradar_host=self.options["qradar_host"],
                                         qradar_token=self.options["qradar_advisor_token"],
                                         advisor_app_id=self.options["qradar_advisor_app_id"],
                                         cafile=qradar_verify_cert,
                                         log=log)
            stix_json = client.offense_analysis(offense_id=qradar_offense_id,
                                                restart_if_existed=qradar_analysis_restart_if_existed,
                                                return_stage=qradar_advisor_result_stage,
                                                timeout=offense_analysis_timeout,
                                                period=offense_analysis_period)
            #
            # extract list of observables from this stix bundle
            #
            observables = stix_utils.get_observables(stix_json=stix_json,
                                                     log=log)
            #
            # generate a folder-tree like structure in html for this stix bundle
            #
            html_str = stix_tree.get_html(stix_json, log)

            #
            # get the insights for this offense
            #
            insights = client.offense_insights(offense_id=qradar_offense_id)

            yield StatusMessage("done...")
            yield StatusMessage("Returning {} observables".format(str(len(observables))))

            results = {
                "observables": observables,
                "note": html_str,
                "insights": insights,       # Return the raw insights dict
                "stix": stix_json           # Return the raw stix2 dict
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            log.error(e.message)
            yield FunctionError(e.message)
