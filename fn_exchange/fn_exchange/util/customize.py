# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_exchange"""

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
    Parameters required reload codegen for the fn_exchange package
    """
    return {
        "package": u"fn_exchange",
        "message_destinations": [u"fn_exchange"],

        "functions": [
            u"exchange_create_meeting",
            u"exchange_delete_emails",
            u"exchange_find_emails",
            u"exchange_get_mailbox_info",
            u"exchange_move_emails",
            u"exchange_send_email"],

        "workflows": [
            u"example_of_exchange_create_meeting",
            u"example_of_exchange_delete_emails",
            u"example_of_exchange_find_emails",
            u"example_of_exchange_get_mailbox_info",
            u"example_of_exchange_move_emails",
            u"example_of_exchange_send_email",
            u"exchange_move_and_delete_folder"],

        "actions": [
            u"Exchange Create Meeting",
            u"Exchange Delete Emails",
            u"Exchange Find Emails",
            u"Exchange Get Mailbox Info",
            u"Exchange Move Emails",
            u"Exchange Move Folder Contents and Delete Folder",
            u"Exchange Send Email"],

        "incident_fields": [],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [],
        "automatic_tasks": [],
        "scripts": [],
        "playbooks": []
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 43.1.49

    Contents:
    - Message Destinations:
        - fn_exchange
    - Functions:
        - exchange_create_meeting
        - exchange_delete_emails
        - exchange_find_emails
        - exchange_get_mailbox_info
        - exchange_move_emails
        - exchange_move_folder_contents_and_delete_folder
        - exchange_send_email
    - Workflows:
        - example_of_exchange_create_meeting
        - example_of_exchange_delete_emails
        - example_of_exchange_find_emails
        - example_of_exchange_get_mailbox_info
        - example_of_exchange_move_emails
        - example_of_exchange_send_email
        - exchange_move_and_delete_folder
    - Rules:
        - Exchange Create Meeting
        - Exchange Delete Emails
        - Exchange Find Emails
        - Exchange Get Mailbox Info
        - Exchange Move Emails
        - Exchange Move Folder Contents and Delete Folder
        - Exchange Send Email
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)