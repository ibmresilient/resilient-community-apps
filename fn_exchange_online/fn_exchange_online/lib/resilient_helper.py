# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
import sys
from io import StringIO, BytesIO
from datetime import datetime
from resilient_lib import IntegrationError, write_file_attachment

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
        attachment_name = "{0}-{1}.txt".format(name_prefix, dt.strftime(TIME_FORMAT))
        if sys.version_info.major < 3:
            datastream = StringIO(note)
        else:
            datastream = BytesIO(note.encode("utf-8"))

        attachment = write_file_attachment(rest_client, attachment_name, datastream, incident_id, None)
        return attachment

    except Exception as err:
        raise IntegrationError(err)


def create_incident_comment(rest_client, incident_id, note):
    """
    Add a comment to the specified Resilient Incident by ID
    :param incident_id:  Resilient Incident ID
    :param note: Content to be added as note
    :return: Response from Resilient for debug
    """
    try:
        uri = '/incidents/{}/comments'.format(incident_id)

        note_json = {
            'format': 'html',
            'content': note
        }
        payload = {'text': note_json}
        comment_response = rest_client.post(uri=uri, payload=payload)
        return comment_response

    except Exception as err:
        raise IntegrationError(err)
