# -*- coding: utf-8 -*-
# Generated with resilient-sdk v49.0.4423

"""Generate the Resilient customizations required for fn_slack"""

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
    Parameters required reload codegen for the fn_slack package
    """
    return {
        "package": u"fn_slack",
        "message_destinations": [u"slack"],
        "functions": [u"slack_archive_channel", u"slack_post_attachment", u"slack_post_message"],
        "workflows": [],
        "actions": [],
        "incident_fields": [],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [u"slack_conversations_db"],
        "automatic_tasks": [],
        "scripts": [],
        "playbooks": [u"example_archive_incident_slack_channel_pb", u"example_archive_task_slack_channel_pb", u"example_post_artifact_attachment_to_slack_pb", u"example_post_artifact_to_slack_pb", u"example_post_incident__task_attachment_to_slack_pb", u"example_post_incident_to_slack_pb", u"example_post_note_to_slack_pb", u"example_post_task_to_slack_pb"]
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 46.0.8131

    Contents:
    - Message Destinations:
        - slack
    - Functions:
        - slack_archive_channel
        - slack_post_attachment
        - slack_post_message
    - Workflows:
        - archive_slack_channel
        - create_slack_message
        - create_slack_reply
        - example_post_attachment_to_slack__artifact
        - slack_example_archive_slack_channel__task
        - slack_example_post_attachment_to_slack
        - slack_example_post_message_to_slack__artifact
        - slack_example_post_message_to_slack__task
    - Playbooks:
        - example_archive_incident_slack_channel_pb
        - example_archive_task_slack_channel_pb
        - example_post_artifact_attachment_to_slack_pb
        - example_post_artifact_to_slack_pb
        - example_post_incident__task_attachment_to_slack_pb
        - example_post_incident_to_slack_pb
        - example_post_note_to_slack_pb
        - example_post_task_to_slack_pb
    - Rules:
        - Example: Archive Incident Slack Channel
        - Example: Archive Task Slack Channel
        - Example: Post Artifact Attachment to Slack
        - Example: Post Artifact to Slack
        - Example: Post Incident / Task Attachment to Slack
        - Example: Post Incident to Slack
        - Example: Post Note to Slack
        - Example: Post Task to Slack
    - Data Tables:
        - slack_conversations_db
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)