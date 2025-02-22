# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, line-too-long
# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload
from fn_mitre_integration.lib import mitre_attack, mitre_attack_utils

class FunctionComponent(ResilientComponent):
    """Component that implements SOAR function 'mitre_groups_technique_intersection"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.opts = opts
        self.options = opts.get("fn_mitre_integration", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.opts = opts
        self.options = opts.get("fn_mitre_integration", {})

    @function("mitre_groups_technique_intersection")
    def _mitre_groups_technique_intersection_function(self, event, *args, **kwargs):
        """Function: For given Techniques return the Groups that are know to use all of them."""
        try:
            # Get the function parameters:
            mitre_technique_name = kwargs.get("mitre_technique_name")  # text
            mitre_technique_id = kwargs.get("mitre_technique_id")  # text

            log = logging.getLogger(__name__)
            log.info("mitre_technique_name: %s", mitre_technique_name)
            log.info("mitre_technique_id: %s", mitre_technique_id)

            result_payload = ResultPayload("fn_mitre_integration", mitre_technique_name=mitre_technique_name,
                                           mitre_technique_id=mitre_technique_id)

            if not mitre_technique_id and not mitre_technique_name:
                raise ValueError("At least one of the inputs (mitre_technique_name or mitre_technique_id) "
                                 "are required.")

            yield StatusMessage("Getting technique information...")

            mitre_conn = mitre_attack.MitreAttackConnection(self.opts, self.options)

            techniques = mitre_attack_utils.get_multiple_techniques(mitre_conn, mitre_technique_ids=mitre_technique_id,
                                                                    mitre_technique_names=mitre_technique_name)

            intersection_query = ",".join([t.id for t in techniques])

            yield StatusMessage("Getting group intersection information...")
            groups = mitre_attack.MitreAttackGroup.get_by_technique_intersection(mitre_conn, techniques)

            if len(groups) == 0:
                yield StatusMessage("No groups were found using all of the given techniques. Done")
            else:
                yield StatusMessage("Done. Returning results.")

            # Storing the techniques specified to query this group
            for group in groups:
                group.technique_id = intersection_query

            groups = [x.dict_form() for x in groups]  # prepare the data for viewing

            # Produce a FunctionResult with the results
            yield FunctionResult(result_payload.done(True, {"mitre_groups": groups}))
        except Exception as e:
            yield FunctionError(e)
