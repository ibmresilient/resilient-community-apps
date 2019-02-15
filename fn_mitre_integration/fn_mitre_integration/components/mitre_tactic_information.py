# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_mitre_integration.lib import mitre_attack_utils


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

            yield StatusMessage("starting...")
            yield StatusMessage("Query MITRE TAXII server, and it can take several minutes....")

            tactics = mitre_attack_utils.get_techniques(mitre_tactic_name)

            yield StatusMessage("done...")

            results = {
                "mitre_tactics": tactics
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            log.exception(str(e))
            yield FunctionError()
