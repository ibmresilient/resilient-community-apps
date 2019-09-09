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

            if not mitre_technique_name and not mitre_technique_id:
                raise ValueError("Neither name nor id is provided for getting technique information.")

            yield StatusMessage("starting...")
            yield StatusMessage("querying MITRE STIX TAXII server. It might take several minutes...")

            mitre_conn = mitre_attack.MitreAttackConnection()
            techniques = mitre_attack.MitreAttackTechnique.get(mitre_conn, name=mitre_technique_name,
                                                               id=mitre_technique_id)

            if techniques is None or not len(techniques):
                raise ValueError(
                    "Technique with name/id {}/{} can't be found".format(mitre_technique_name, mitre_technique_id))

            techs = []
            for technique in techniques:
                tech_dict = technique.dict_form()
                tech_dict.update(
                    {
                        "mitre_mitigations": [x.dict_form() for x in technique.get_mitigations(mitre_conn)]
                    }
                )
                techs.append(tech_dict)

            yield StatusMessage("done...")

            results = {
                "mitre_techniques": techs
            }
            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            log.exception(str(e))
            yield FunctionError()