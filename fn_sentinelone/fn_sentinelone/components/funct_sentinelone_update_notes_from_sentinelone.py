# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import SOARCommon
from fn_sentinelone.lib.app_common import (AppCommon, PACKAGE_NAME, SOAR_HEADER)

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

        soar_common = SOARCommon(self.rest_client())
        app_common = AppCommon(self.rc, PACKAGE_NAME, self.options)

        threat_notes = app_common.get_threat_notes(threat_id)

        # Create a list of formatted text for filtering just new comments.
        threat_note_list = []
        for comment in threat_notes:
            formatted_text = app_common.format_threat_note(comment)
            if formatted_text:
                threat_note_list.append(formatted_text)

        new_comments = []
        if threat_note_list:
            new_comments = soar_common.filter_soar_comments(incident_id, threat_note_list, SOAR_HEADER)

        if new_comments:

            for comment in new_comments:
                soar_common.create_case_comment(case_id = incident_id,
                                                note=comment)

        results = {"success": True,
                   "notes_created": len(new_comments)}      

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        yield FunctionResult(results)
