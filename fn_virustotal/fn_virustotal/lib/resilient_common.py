# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

import re
from resilient_circuits.rest_helper import get_resilient_client as get_client
from resilient_lib import IntegrationError

INCIDENT_FRAGMENT = '#incidents'

def get_input_entity(client, incident_id, attachment_id, artifact_id, task_id):

    re_uri_match_pattern = r"""(?:(?:https?|ftp):\/\/|\b(?:[a-z\d]+\.))(?:(?:[^\s()<>]+|\((?:[^\s()<>]+|(?:\([^\s()<>]+\)))?\))+(?:\((?:[^\s()<>]+|(?:\(?:[^\s()<>]+\)))?\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))?"""
    entity = {"incident_id": incident_id, "id": None, "type": "", "meta_data": None, "data": None}

    if (attachment_id):
        entity["id"] = attachment_id
        entity["type"] = "attachment"
        if task_id:
            entity["task_id"] = task_id
            entity["meta_data"] = client.get("/tasks/{0}/attachments/{1}".format(entity["task_id"], entity["id"]))
            if entity["meta_data"].get("name"):
                entity["name"] = entity["meta_data"]["name"]
            entity["data"] = client.get_content("/tasks/{0}/attachments/{1}/contents".format(entity["task_id"], entity["id"]))
        else:
            entity["meta_data"] = client.get("/incidents/{0}/attachments/{1}".format(entity["incident_id"], entity["id"]))
            if entity["meta_data"].get("name"):
                entity["name"] = entity["meta_data"]["name"]
            entity["data"] = client.get_content("/incidents/{0}/attachments/{1}/contents".format(entity["incident_id"], entity["id"]))

    elif (artifact_id):
        entity["id"] = artifact_id
        entity["type"] = "artifact"
        entity["meta_data"] = client.get("/incidents/{0}/artifacts/{1}".format(entity["incident_id"], entity["id"]))

        # handle if artifact has attachment
        if (entity["meta_data"]["attachment"]):
            entity["name"] = entity["meta_data"]["attachment"]["name"]
            entity["data"] = client.get_content("/incidents/{0}/artifacts/{1}/contents".format(entity["incident_id"], entity["id"]))

        # else handle if artifact.value contains an URI using RegEx
        else:
            match = re.match(re_uri_match_pattern, entity["meta_data"]["value"])

            if (match):
                entity["uri"] = match.group()

            else:
                raise IntegrationError("Artifact has no attachment or supported URI")

    else:
        raise ValueError('attachment_id AND artifact_id both None')

    return entity

def get_resilient_client(opts):
    """Get a connected instance of SimpleClient for Resilient REST API"""
    resilient_client = get_client(opts)
    return resilient_client