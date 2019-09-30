# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload
from fn_mitre_integration.lib import mitre_attack

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'mitre_groups_using_technique"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_mitre_integration", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_mitre_integration", {})

    @function("mitre_groups_using_technique")
    def _mitre_groups_using_technique_function(self, event, *args, **kwargs):
        """Function: Get a list of groups that are using the given technique(s)."""
        try:
            mitre_technique_name = kwargs.get("mitre_technique_name")  # text
            mitre_technique_id = kwargs.get("mitre_technique_id")  # text

            log = logging.getLogger(__name__)
            log.info("mitre_technique_name: %s", mitre_technique_name)
            log.info("mitre_technique_id: %s", mitre_technique_id)

            result_payload = ResultPayload("fn_mitre_integration", mitre_technique_name=mitre_technique_name,
                                           mitre_technique_id=mitre_technique_id)

            if not mitre_technique_id and not mitre_technique_name:
                raise ValueError("At least one of the inputs(mitre_technique_name or mitre_technique_id) "
                                 "should be provided.")

            yield StatusMessage("starting...")
            yield StatusMessage("Getting technique information...")

            mitre_conn = mitre_attack.MitreAttackConnection()

            if mitre_technique_id is not None:
                # Try id first, because it's less ambiguous
                technique_ids = mitre_technique_id.split(',')
                techniques = []
                for t_id in technique_ids:
                    technique = mitre_attack.MitreAttackTechnique.get_by_id(mitre_conn, t_id)
                    if not technique:
                        raise ValueError("Technique with id {} doesn't exist".format(t_id))
                    techniques.extend(technique)
            else:
                # It's possible for multiple tactics to have the same name
                # And we want to make sure that all of them are processed in that case
                technique_names = mitre_technique_name.split(',')
                techniques = []
                for name in technique_names:
                    technique = mitre_attack.MitreAttackTechnique.get_by_name(mitre_conn, name)
                    if not technique:
                        raise ValueError("Techniques with name {} don't exist".format(name))
                    techniques.extend(technique)

            yield StatusMessage("Getting group information...")
            groups = []
            for technique in techniques:
                groups.extend(mitre_attack.MitreAttackGroup.get_by_technique(mitre_conn, technique))

            yield StatusMessage("Done. Returning results")
            groups = [x.dict_form() for x in groups]  # prepare the data for viewing

            results = {
                "mitre_groups": groups
            }
            # Produce a FunctionResult with the results
            yield FunctionResult(result_payload.done(True, results))
        except Exception as e:
            log.exception(str(e))
            yield FunctionError()