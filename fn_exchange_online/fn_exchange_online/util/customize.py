# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# Generated with resilient-sdk v51.0.2.2.1096

"""Generate the SOAR customizations required for fn_exchange_online"""

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
    Parameters required reload codegen for the fn_exchange_online package
    """
    return {
        "package": u"fn_exchange_online",
        "message_destinations": [
            u"fn_exchange_online"
        ],
        "functions": [
            u"exchange_online_create_meeting",
            u"exchange_online_delete_email",
            u"exchange_online_delete_messages_from_query_results",
            u"exchange_online_get_email_user_profile",
            u"exchange_online_get_message",
            u"exchange_online_move_message_to_folder",
            u"exchange_online_query_emails",
            u"exchange_online_send_message",
            u"exchange_online_write_message_as_attachment"
        ],
        "workflows": [],
        "actions": [],
        "incident_fields": [],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [
            u"exo_message_query_results_dt"
        ],
        "automatic_tasks": [],
        "scripts": [],
        "playbooks": [
            u"example_exchange_online_create_artifacts",
            u"example_exchange_online_create_meeting",
            u"example_exchange_online_delete_message",
            u"example_exchange_online_delete_messages_from_query_results",
            u"example_exchange_online_get_user_profile",
            u"example_exchange_online_move_message_to_folder",
            u"example_exchange_online_query_messages",
            u"example_exchange_online_query_messages_on_artifact",
            u"example_exchange_online_send_message",
            u"example_exchange_online_write_message_eml_as_attachment",
            u"example_exchange_online_write_message_json_as_note"
        ]
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 51.0.0.0.9340

    Contents:
    - Message Destinations:
        - fn_exchange_online
    - Functions:
        - exchange_online_create_meeting
        - exchange_online_delete_email
        - exchange_online_delete_messages_from_query_results
        - exchange_online_get_email_user_profile
        - exchange_online_get_message
        - exchange_online_move_message_to_folder
        - exchange_online_query_emails
        - exchange_online_send_message
        - exchange_online_write_message_as_attachment
    - Playbooks:
        - example_exchange_online_create_artifacts
        - example_exchange_online_create_meeting
        - example_exchange_online_delete_message
        - example_exchange_online_delete_messages_from_query_results
        - example_exchange_online_get_user_profile
        - example_exchange_online_move_message_to_folder
        - example_exchange_online_query_messages
        - example_exchange_online_query_messages_on_artifact
        - example_exchange_online_send_message
        - example_exchange_online_write_message_eml_as_attachment
        - example_exchange_online_write_message_json_as_note
    - Data Tables:
        - exo_message_query_results_dt
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)