# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=line-too-long
from io import BytesIO
from datetime import datetime
import base64
import logging
from resilient_lib import IntegrationError, write_file_attachment, get_file_attachment
LOG = logging.getLogger(__name__)

TIME_FORMAT = '%Y-%m-%dT%H:%M:%S'

def create_incident_attachment(rest_client, incident_id, note, name_prefix):
    """
    Add an attachment to the specified Resilient Incident by ID
    :param incident_id:  Resilient Incident ID
    :param note: Content to be added as attachment
    :param name_prefix: name prefix of the attachment name
    :return: Resilient attachment
    """
    try:
        dt = datetime.now()
        attachment_name = f"{name_prefix}-{dt.strftime(TIME_FORMAT)}.txt"
        datastream = BytesIO(note.encode("utf-8"))

        attachment = write_file_attachment(rest_client, attachment_name, datastream, incident_id, None)
        return attachment

    except Exception as err:
        raise IntegrationError(err) from err


def create_incident_comment(rest_client, incident_id, note):
    """
    Add a comment to the specified Resilient Incident by ID
    :param incident_id:  Resilient Incident ID
    :param note: Content to be added as note
    :return: Response from Resilient for debug
    """
    try:
        uri = f"/incidents/{incident_id}/comments"

        note_json = {
            'format': 'html',
            'content': note
        }
        payload = {'text': note_json}
        comment_response = rest_client.post(uri=uri, payload=payload)
        return comment_response

    except Exception as err:
        raise IntegrationError(err) from err

def get_attachment_id(rest_client, incident_id, attachment_name):
    """
    Get an incident attachment ID given it's name.
    If the attachment does not exist, gracefully fail by returning None.
    :param rest_client: Resilient REST API client
    :param incident_id: Resilient incident ID
    :param attachment_name: Resilient incident attachment name
    :return: incident attachment ID
    """
    # Get incident attachments
    url = f"/incidents/{incident_id}/attachments"
    attachments = rest_client.get(url)

    # Find a name that matches provided name, return the ID
    id = None
    for attachment in attachments:
        if attachment["name"] ==  attachment_name:
            id = attachment["id"]
            break
    if not id:
        LOG.error("Attachment name '%s' not found on the incident! Skipping that attachment.", attachment_name)
    return id

def get_incident_file_attachment(rest_client, incident_id, attachment_name):
    """
    Get incident file attachment data from Resilient.
    Gracefully fail by returning null if the attachment is not found.
    :param rest_client: Resilient REST API client
    :param incident_id: Resilient incident ID
    :param attachment_name: name of the attachment to get
    :return: base64 encoded attachment data, attachment ID
    """
    # Get the attachment ID
    attachment_id = get_attachment_id(rest_client, incident_id, attachment_name)
    if not attachment_id:
        return None, None

    # Get the attachment data content, base64 encode it, and decode bytes to string
    content = get_file_attachment(rest_client, incident_id, attachment_id=attachment_id)
    encoded_content = base64.b64encode(content).decode("utf-8")
    return encoded_content, attachment_id

def check_status_code(status_code):
    """
    Check if the HTTP status code is in 200 Range
    :param status_code: HTTP Status Code
    :return: boolean value 
    """
    # Logic for checking status code between 200 and 300 
    if int(status_code/100) == 2:
        return True
    else: 
        return False
