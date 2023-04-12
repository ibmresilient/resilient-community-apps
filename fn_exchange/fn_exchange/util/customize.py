# -*- coding: utf-8 -*-
# Generated with resilient-sdk v48.0.4034

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

        "message_destinations": [
            u"fn_exchange"],

        "functions": [
            u"exchange_create_meeting",
            u"exchange_delete_emails",
            u"exchange_find_emails",
            u"exchange_get_mailbox_info",
            u"exchange_move_emails",
            u"exchange_send_email"],

        "playbooks": [
            u"playbook_exchange_move_and_delete_folder_contents",
            u"example_playbook_for_exchange_create_meetings",
            u"playbooks_exchange_delete_email",
            u"playbooks_exchange_find_email",
            U"playbook_exchange_get_mailbox_info",
            u"playbooks_exchange_move_email",
            u"playbooks_exchange_send_email"],

        "datatables": [
            u"exchange_email_information_dt",
            u"exchange_dt_meeting_information"],

        "scripts": [
            u"Push Emails to DataTables"],

        "workflows": [],
        "actions": [],
        "incident_fields": [],
        "incident_artifact_types": [],
        "incident_types": [],
        "automatic_tasks": []}


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 47.0.8304

    Contents:
    - Message Destinations:
        - fn_exchange
    - Functions:
        - exchange_create_meeting
        - exchange_delete_emails
        - exchange_find_emails
        - exchange_get_mailbox_info
        - exchange_move_emails
        - exchange_send_email
    - Playbooks:
        - example_playbook_for_exchange_create_meetings
        - playbook_exchange_get_mailbox_info
        - playbook_exchange_move_and_delete_folder_contents
        - playbooks_exchange_delete_email
        - playbooks_exchange_find_email
        - playbooks_exchange_move_email
        - playbooks_exchange_send_email
    - Data Tables:
        - exchange_dt_meeting_information
        - exchange_email_information_dt
    - Scripts:
        - Push Emails to DataTables
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)
