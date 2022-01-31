# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from fn_sentinelone.lib.resilient_common import ResilientCommon
from fn_sentinelone.lib.sentinelone_common import SentinelOneClient

PACKAGE_NAME = "fn_sentinelone"
FN_NAME = "sentinelone_update_notes_from_sentinelone"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'sentinelone_update_notes_from_sentinelone'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Query SentinelOne threat and add any new threat notes to the SOAR incident.
        Inputs:
            -   fn_inputs.incident_id
            -   fn_inputs.sentinelone_threat_id
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        incident_id = fn_inputs.incident_id
        threat_id = fn_inputs.sentinelone_threat_id

        resilient_api = ResilientCommon(self.rest_client())
        sentinelone_api = SentinelOneClient(self.opts, self.options)

        threat_notes = sentinelone_api.get_threat_notes(threat_id)

        new_comments = resilient_api.filter_resilient_comments(incident_id, threat_notes)

        for comment in new_comments:
            resilient_api.create_incident_comment(incident_id,
                                                  comment['id'],
                                                  comment['text'])
        results = {"success": True,
                   "notes_created": len(new_comments)}      

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        yield FunctionResult(results)
