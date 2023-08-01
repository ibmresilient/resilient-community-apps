# -*- coding: utf-8 -*-
# Generated with resilient-sdk v49.1.51

"""Generate the Resilient customizations required for fn_salesforce"""

import base64
import os
import io
try:
    from resilient import ImportDefinition
except ImportError:
    # Support Apps running on resilient-circuits < v35.0.195
    from resilient_circuits.util import ImportDefinition

RES_FILE = "data/export.res"


def codegen_reload_data():
    """
    Parameters required reload codegen for the fn_salesforce package
    """
    return {
        "package": u"fn_salesforce",
        "message_destinations": [u"fn_salesforce"],
        "functions": [u"salesforce_add_comment_to_salesforce_case", u"salesforce_create_case_in_salesforce", u"salesforce_get_account", u"salesforce_get_attachments_from_salesforce", u"salesforce_get_case", u"salesforce_get_case_comments", u"salesforce_get_contact", u"salesforce_get_user", u"salesforce_post_attachment_to_salesforce_case", u"salesforce_update_case_status"],
        "workflows": [],
        "actions": [],
        "incident_fields": [u"salesforce_account_id", u"salesforce_account_name", u"salesforce_case_id", u"salesforce_case_link", u"salesforce_case_number", u"salesforce_case_owner", u"salesforce_case_type", u"salesforce_contact_email", u"salesforce_contact_fax", u"salesforce_contact_id", u"salesforce_contact_name", u"salesforce_contact_phone", u"salesforce_origin", u"salesforce_owner_id", u"salesforce_status", u"salesforce_supplied_company", u"salesforce_supplied_email", u"salesforce_supplied_name", u"salesforce_supplied_phone"],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [],
        "automatic_tasks": [],
        "scripts": [],
        "playbooks": [u"salesforce_add_comment_to_salesforce_case", u"salesforce_close_case", u"salesforce_create_salesforce_case", u"salesforce_get_account", u"salesforce_get_attachments_from_salesforce_case", u"salesforce_get_contact", u"salesforce_post_artifact_file_to_salesforce_case", u"salesforce_post_attachment_to_salesforce_case", u"salesforce_send_note_to_salesforce_case", u"salesforce_update_account_details_in_soar", u"salesforce_update_case", u"salesforce_update_comments_from_salesforce_case", u"salesforce_update_contact_details_in_soar", u"salesforce_update_owner_details_in_soar", u"salesforce_write_owner_details_to_note"]
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 47.0.8304

    Contents:
    - Message Destinations:
        - fn_salesforce
    - Functions:
        - salesforce_add_comment_to_salesforce_case
        - salesforce_create_case_in_salesforce
        - salesforce_get_account
        - salesforce_get_attachments_from_salesforce
        - salesforce_get_case
        - salesforce_get_case_comments
        - salesforce_get_contact
        - salesforce_get_user
        - salesforce_post_attachment_to_salesforce_case
        - salesforce_update_case_status
    - Playbooks:
        - salesforce_add_comment_to_salesforce_case
        - salesforce_close_case
        - salesforce_create_salesforce_case
        - salesforce_get_account
        - salesforce_get_attachments_from_salesforce_case
        - salesforce_get_contact
        - salesforce_post_artifact_file_to_salesforce_case
        - salesforce_post_attachment_to_salesforce_case
        - salesforce_send_note_to_salesforce_case
        - salesforce_update_account_details_in_soar
        - salesforce_update_case
        - salesforce_update_comments_from_salesforce_case
        - salesforce_update_contact_details_in_soar
        - salesforce_update_owner_details_in_soar
        - salesforce_write_owner_details_to_note
    - Incident Fields:
        - salesforce_account_id
        - salesforce_account_name
        - salesforce_case_id
        - salesforce_case_link
        - salesforce_case_number
        - salesforce_case_owner
        - salesforce_case_type
        - salesforce_contact_email
        - salesforce_contact_fax
        - salesforce_contact_id
        - salesforce_contact_name
        - salesforce_contact_phone
        - salesforce_origin
        - salesforce_owner_id
        - salesforce_status
        - salesforce_supplied_company
        - salesforce_supplied_email
        - salesforce_supplied_name
        - salesforce_supplied_phone
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)