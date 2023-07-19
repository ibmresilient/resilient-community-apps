# -*- coding: utf-8 -*-
# Generated with resilient-sdk v49.1.51

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields, SOARCommon
from fn_salesforce.lib.app_common import (AppCommon, ENTITY_COMMENT_HEADER, SOAR_HEADER, PACKAGE_NAME)

PACKAGE_NAME = "fn_salesforce"
FN_NAME = "salesforce_get_case_comments"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'salesforce_get_case_comments'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Get the comments from the Salesforce case.
        Inputs:
            -   fn_inputs.incident_id
            -   fn_inputs.salesforce_case_id
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        validate_fields(["incident_id", "salesforce_case_id"], fn_inputs)

        incident_id = fn_inputs.incident_id
        salesforce_case_id = fn_inputs.salesforce_case_id

        soar_common = SOARCommon(self.rest_client())
        app_common = AppCommon(self.rc, self.PACKAGE_NAME, self.options)

        sf_case_comments = app_common.get_case_comments(salesforce_case_id)

        # Create a list of formatted text for filtering just new comments.
        sf_case_comment_list = []
        for comment in sf_case_comments:
            formatted_text = app_common.format_salesforce_comment(comment)
            if formatted_text:
                sf_case_comment_list.append(formatted_text)

        # Filter out the new Salesforce comments by checking for header in the comment.
        new_comments = []
        if sf_case_comment_list:
            new_comments = soar_common.filter_soar_comments(incident_id, sf_case_comment_list, SOAR_HEADER)
            # Reverse the order so that older notes are post first.
            if new_comments:
                new_comments.reverse()

                # Create a new note in SOAR for each new Salesforce comment
                for comment in new_comments:
                    #note = "<b>{}:</b><br>{}".format(ENTITY_COMMENT_HEADER, comment)
                    soar_common.create_case_comment(case_id=incident_id,
                                                    note=comment, 
                                                    entity_comment_id=None, 
                                                    entity_comment_header=ENTITY_COMMENT_HEADER)

        results = {"count": len(new_comments)}

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        yield FunctionResult(results)

