# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
#
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
#
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_mitre_integration.lib import mitre_attack_utils
from resilient_lib import ResultPayload


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'mitre_tactic_information

        This function takes a tactic name or id and returns techniques this
        tactic uses

    """

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_mitre_integration", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_mitre_integration", {})

    @function("mitre_tactic_information")
    def _mitre_tactic_information_function(self, event, *args, **kwargs):
        """Function: Get information about MITRE tactic"""
        try:
            # Get the function parameters:
            mitre_tactic_id = kwargs.get("mitre_tactic_id")  # text
            mitre_tactic_name = kwargs.get("mitre_tactic_name")  # text

            log = logging.getLogger(__name__)
            log.info("mitre_tactic_id: %s", mitre_tactic_id)
            log.info("mitre_tactic_name: %s", mitre_tactic_name)

            if not mitre_tactic_id and not mitre_tactic_name:
                raise ValueError("Neither name nor id is provided for getting tactic information.")

            result_payload = ResultPayload("fn_mitre_integration", mitre_tactic_id=mitre_tactic_id,
                                           mitre_tactic_name=mitre_tactic_name)
            yield StatusMessage("starting...")
            yield StatusMessage("query MITRE STIX TAXII server, and it can take several minutes....")

            tactics = mitre_attack_utils.get_tactics_and_techniques(tactic_names=mitre_tactic_name,
                                                                    tactic_ids=mitre_tactic_id)
            yield StatusMessage("done...")

            results = {
                "mitre_tactics": tactics
            }
            # Produce a FunctionResult with the results
            yield FunctionResult(result_payload.done(True, results))
        except Exception as e:
            log.exception(str(e))
            yield FunctionError()
