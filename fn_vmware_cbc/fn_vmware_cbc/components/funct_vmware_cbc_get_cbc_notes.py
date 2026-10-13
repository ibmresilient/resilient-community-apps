# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# Generated with resilient-sdk v51.0.1.1.824

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import (validate_fields, SOARCommon)
from fn_vmware_cbc.lib.app_common import (AppCommon, SOAR_HEADER, PACKAGE_NAME)

PACKAGE_NAME = "fn_vmware_cbc"
FN_NAME = "vmware_cbc_get_cbc_notes"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'vmware_cbc_get_cbc_notes'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Get the alert or threat notes of the specified Carbon Black Cloud alert or threat id.
        Inputs:
            -   fn_inputs.vmware_cbc_id
            -   fn_inputs.vmware_cbc_note_type
            -   fn_inputs.vmware_cbc_incident_id
        """
        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        validate_fields(["vmware_cbc_id", "vmware_cbc_incident_id", "vmware_cbc_note_type"], fn_inputs)
        incident_id = fn_inputs.vmware_cbc_incident_id

        soar_common = SOARCommon(self.rest_client())
        app_common = AppCommon(PACKAGE_NAME, self.options)

        cbc_notes, error_msg  = app_common.get_cbc_notes(id=fn_inputs.vmware_cbc_id, 
                                                         note_type=fn_inputs.vmware_cbc_note_type)

        # Create a list of formatted text for filtering just new notes.
        cbc_note_list = []
        for note in cbc_notes:
            formatted_text = app_common.format_cbc_note(note)
            if formatted_text:
                cbc_note_list.append(formatted_text)

        # Filter out the new VMware CBC notes by checking for header in the note.
        new_notes = []
        if cbc_note_list:
            new_notes = soar_common.filter_soar_comments(incident_id, cbc_note_list, SOAR_HEADER)
            # Reverse the order so that older notes are post first.
            if new_notes:

                # Create a new note in SOAR for each new VMware CBC note
                for note in new_notes:
                    soar_common.create_case_comment(case_id=incident_id,
                                                    note=note)

        results = {"count": len(new_notes)}

        yield FunctionResult(results, success=False if error_msg else True, reason=error_msg)