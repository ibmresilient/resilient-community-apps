# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# Generated with resilient-sdk v51.0.2.2.1096

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import (SOARCommon, validate_fields)
from fn_sumo_logic.lib.app_common import (PACKAGE_NAME, SOAR_HEADER, AppCommon)

PACKAGE_NAME = "fn_sumo_logic"
FN_NAME = "sumo_logic_get_insights_comments"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'sumo_logic_get_insights_comments'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Get comments from a Sumo Logic insight and add any new ones as notes to the corresponding SOAR case.
        Inputs:
            -   fn_inputs.sumo_logic_insight_id
            -   fn_inputs.sumo_logic_incident_id
        """
        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        validate_fields(["sumo_logic_insight_id", "sumo_logic_incident_id"], fn_inputs)
        incident_id = fn_inputs.sumo_logic_incident_id

        soar_common = SOARCommon(self.rest_client())
        app_common = AppCommon(PACKAGE_NAME, self.options)

        insights_comments, error_msg  = app_common.get_comments_from_insight(insight_id=fn_inputs.sumo_logic_insight_id)

        # Create a list of formatted text for filtering just new notes.
        insight_notes_list = []
        for note in insights_comments:
            formatted_text = app_common.format_insight_note(note)
            if formatted_text:
                insight_notes_list.append(formatted_text)

        # Filter out the new Sumo Logic comments by checking for header in the comment.
        new_notes = []
        if insight_notes_list:
            new_notes = soar_common.filter_soar_comments(incident_id, insight_notes_list, SOAR_HEADER)
            # Reverse the order so that older notes are post first.
            if new_notes:

                # Create a new note in SOAR for each new Sumo Logic comment
                for note in new_notes:
                    soar_common.create_case_comment(case_id=incident_id,
                                                    note=note)

        results = {"count": len(new_notes)}

        yield FunctionResult(results, success=False if error_msg else True, reason=error_msg)
