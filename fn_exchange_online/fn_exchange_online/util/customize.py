# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_exchange_online"""

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
        "message_destinations": [u"fn_exchange_online"],
        "functions": [u"exchange_online_delete_email", u"exchange_online_delete_messages_from_query_results", u"exchange_online_move_message_to_folder", u"exchange_online_get_email_user_profile", u"exchange_online_create_meeting", u"exchange_online_query_emails", u"exchange_online_get_message", u"exchange_online_write_message_as_attachment", u"exchange_online_send_message"],
        "workflows": [u"example_exchange_online_delete_email", u"example_exchange_online_delete_messages_from_query_results", u"example_exchange_online_create_meeting", u"example_exchange_online_move_message_to_folder", u"example_exchange_online_get_message", u"example_exchange_online_get_user_profile", u"example_exchange_online_send_message", u"example_exchange_online_write_message_as_attachment", u"example_exchange_online_query_emails", u"example_exchange_online_query_messages_of_a_group"],
        "actions": [u"Example: Exchange Online Query Messages", u"Example: Exchange Online Create Meeting", u"Example: Exchange Online Write Message JSON as Note", u"Example: Exchange Online Create Artifacts", u"Example: Exchange Online Get User Profile", u"Example: Exchange Online Delete Message", u"Example: Exchange Online Query Messages on Artifact", u"Example: Exchange Online Send Message", u"Example: Exchange Online Delete Messages from Query Results", u"Example: Exchange Online Move Message to Folder", u"Example: Exchange Online Write Message EML as Attachment"],
        "incident_fields": [],
        "incident_artifact_types": [],
        "datatables": [u"exo_message_query_results_dt"],
        "automatic_tasks": [],
        "scripts": [u"Exchange Online Create Artifacts from Message"],
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM Resilient Platform Version: 37.0.0

    Contents:
    - Message Destinations:
        - fn_exchange_online
    - Functions:
        - exchange_online_delete_email
        - exchange_online_delete_messages_from_query_results
        - exchange_online_move_message_to_folder
        - exchange_online_get_email_user_profile
        - exchange_online_create_meeting
        - exchange_online_query_emails
        - exchange_online_get_message
        - exchange_online_write_message_as_attachment
        - exchange_online_send_message
    - Workflows:
        - example_exchange_online_delete_email
        - example_exchange_online_delete_messages_from_query_results
        - example_exchange_online_create_meeting
        - example_exchange_online_move_message_to_folder
        - example_exchange_online_get_message
        - example_exchange_online_get_user_profile
        - example_exchange_online_send_message
        - example_exchange_online_write_message_as_attachment
        - example_exchange_online_query_emails
        - example_exchange_online_query_messages_of_a_group
    - Rules:
        - Example: Exchange Online Query Messages
        - Example: Exchange Online Create Meeting
        - Example: Exchange Online Write Message JSON as Note
        - Example: Exchange Online Create Artifacts
        - Example: Exchange Online Get User Profile
        - Example: Exchange Online Delete Message
        - Example: Exchange Online Query Messages on Artifact
        - Example: Exchange Online Send Message
        - Example: Exchange Online Delete Messages from Query Results
        - Example: Exchange Online Move Message to Folder
        - Example: Exchange Online Write Message EML as Attachment
    - Data Tables:
        - exo_message_query_results_dt
    - Scripts:
        - Exchange Online Create Artifacts from Message
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)