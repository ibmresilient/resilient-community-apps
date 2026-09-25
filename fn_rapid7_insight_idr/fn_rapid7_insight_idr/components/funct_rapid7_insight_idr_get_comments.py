# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# Generated with resilient-sdk v51.0.0.0.430

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields, SOARCommon
from fn_rapid7_insight_idr.lib.app_common import (AppCommon, ENTITY_COMMENT_HEADER, SOAR_HEADER, PACKAGE_NAME)

FN_NAME = "rapid7_insight_idr_get_comments"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'rapid7_insight_idr_get_comments'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Get the comments from a Rapid7 InsightIDR investigation and add any new ones as notes to the corresponding SOAR case.
        Inputs:
            -   fn_inputs.rapid7_insight_idr_rrn
            -   fn_inputs.rapid7_insight_idr_incident_id
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        validate_fields(["rapid7_insight_idr_rrn", "rapid7_insight_idr_incident_id"], fn_inputs)

        incident_id = fn_inputs.rapid7_insight_idr_incident_id
        r7_insight_idr_rrn = fn_inputs.rapid7_insight_idr_rrn

        soar_common = SOARCommon(self.rest_client())
        app_common = AppCommon(self.rc, PACKAGE_NAME, self.options)

        target_comments, error_msg  = app_common.get_comments(r7_insight_idr_rrn)

        # Create a list of formatted text for filtering just new comments.
        target_comment_list = []
        for comment in target_comments:
            formatted_text = app_common.format_rapid7_insight_idr_comment(comment)
            if formatted_text:
                target_comment_list.append(formatted_text)

        # Filter out the new Rapid7 InsightIDR comments by checking for header in the comment.
        new_comments = []
        if target_comment_list:
            new_comments = soar_common.filter_soar_comments(incident_id, target_comment_list, SOAR_HEADER)
            # Reverse the order so that older notes are post first.
            if new_comments:

                # Create a new note in SOAR for each new Rapid7 InsightIDR comment
                for comment in new_comments:
                    soar_common.create_case_comment(case_id=incident_id,
                                                    note=comment)

        results = {"count": len(new_comments)}

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        yield FunctionResult(results)
