# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
#
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
#
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_mitre_integration.lib import mitre_attack


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'mitre_technique_information'

    This function fetches the MITRE technique information from the
    MITRE STIX TAXII server.
    """

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_mitre_integration", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_mitre_integration", {})

    @function("mitre_technique_information")
    def _mitre_technique_information_function(self, event, *args, **kwargs):
        """Function: Get ATT&CK information about MITRE ATT&CK technique"""
        try:
            # Get the function parameters:
            mitre_technique_name = kwargs.get("mitre_technique_name")  # text
            mitre_technique_id = kwargs.get("mitre_technique_id")  # text
            mitre_technique_mitigation_only = kwargs.get("mitre_technique_mitigation_only")  # boolean

            log = logging.getLogger(__name__)
            log.info("mitre_technique_name: %s", mitre_technique_name)
            log.info("mitre_technique_id: %s", mitre_technique_id)
            log.info("mitre_technique_mitigation_only: %s", mitre_technique_mitigation_only)

            yield StatusMessage("starting...")
            yield StatusMessage("query MITRE STIX TAXII server. It might take several minutes...")

            mitre_att = mitre_attack.MitreAttack()
            tech = {}
            if mitre_technique_mitigation_only:
                tech = {
                    "name": mitre_technique_name,
                    "description": "",
                    "external_references": [{"url":""}],
                    "x_mitre_detection": "",
                    "mitre_tech_id": "",
                    "mitre_mitigation": mitre_att.get_tech_mitigation(tech_id=mitre_technique_id,
                                                                      tech_name=mitre_technique_name)
                }
            else:
                tech = mitre_att.get_tech(name=mitre_technique_name,
                                          ext_id=mitre_technique_id)

            yield StatusMessage("done...")
            log.info("MITRE tech: " + str(tech))
            results = tech

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            log.exception(str(e))
            yield FunctionError()