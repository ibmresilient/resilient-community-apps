# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields, SOARCommon
from fn_randori.lib.app_common import AppCommon

PACKAGE_NAME = "fn_randori"
FN_NAME = "randori_update_notes_from_randori_target"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'randori_update_notes_from_randori_target'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Query Randori target and add any new notes to the SOAR case.
        Inputs:
            -   fn_inputs.randori_target_id
            -   fn_inputs.incident_id
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        validate_fields(["incident_id", "randori_target_id"], fn_inputs)

        incident_id = fn_inputs.incident_id
        target_id = fn_inputs.randori_target_id

        soar_common = SOARCommon(self.rest_client())
        app_common = AppCommon(self.rc, self.PACKAGE_NAME, self.options)

        target_comments = app_common.get_target_comments(target_id)

        # Create a list of formatted text for filtering just new commments.
        target_comment_text = []
        for comment in target_comments:
            formatted_text = app_common.format_randori_comment(comment)
            if formatted_text:
                target_comment_text.append(formatted_text)

        # Filter out the new Randori comments by checking for header in the comment.
        new_comments = soar_common.filter_soar_comments(incident_id, target_comment_text)

        # Reverse the order so that older notes are post first.
        new_comments.reverse()

        # Create a new note in SOAR for each new Randori comment
        for comment in new_comments:
            soar_common.create_case_comment(case_id=incident_id,
                                            note=comment,
                                            entity_comment_header="Created by Randori")

        results = {"notes_created": len(new_comments)}

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        yield FunctionResult(results)