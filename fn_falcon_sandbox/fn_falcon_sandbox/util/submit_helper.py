# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
import time
import requests
import tempfile
import os
import re
from requests_toolbelt import MultipartEncoder
from fn_falcon_sandbox.util.constants import (
    HA_AVAILABLE_ENVS,
    HA_AVAILABLE_RUNTIME_ACTION_SCRIPTS,
    PARAM_NAMING_CONVENTION_RE,
)


def is_correct_naming_convention(test_str):
    """This function will return Boolean value based on whether or not 
        Parameter naming convention has been followed.
    """
    return re.search(PARAM_NAMING_CONVENTION_RE, test_str)

def write_temp_file(data, name=None):
    """This function writes content to a temporary file and 
        returns file path and list of files.
    """
    temp_files = []
    path = None

    if name:
        path = os.path.abspath(
            "{0}/{1}".format(tempfile.gettempdir(), name)
        )
    else:
        tf = tempfile.mkstemp()
        path = tf[1]

    fo = open(path, "wb")
    temp_files.append(path)
    fo.write(data)
    fo.close()
    return path, temp_files


def remove_temp_files(files):
    """This function removes all temporary files 
        created by this function.
    """
    for f in files:
        os.remove(f)


def falcon_sandbox_request_header(api_key):
    """ This function add API Key and 
        returns request header 
    """
    return {
        "accept": "application/json",
        "user-agent": "Falcon Sandbox",
        "api-key": api_key,
    }


def get_submission_queue_size(host_url, api_key):
    """ This function returns current submission queue size of Falcon Sandbox"""

    headers = falcon_sandbox_request_header(api_key)
    url = "{}/system/queue-size".format(host_url)
    response = requests.get(url, headers=headers)
    response_json = response.json()
    return response_json.get("value")


def get_file_attachment_and_metadata(
    res_client, incident_id, artifact_id=None, task_id=None, attachment_id=None
):
    """
    call the Resilient REST API to get the attachment or artifact data
    :param res_client: required for communication back to resilient
    :param incident_id: required
    :param artifact_id: optional
    :param task_id: optional
    :param attachment_id: optional
    :return: byte string of attachment
    """
    metadata = None
    if incident_id and artifact_id:
        data_uri = "/incidents/{}/artifacts/{}/contents".format(
            incident_id, artifact_id
        )
        metadata_url = "/incidents/{}/artifacts/{}".format(incident_id, artifact_id)
        metadata = res_client.get(metadata_url)["attachment"]
    elif attachment_id:
        if task_id:
            data_uri = "/tasks/{}/attachments/{}/contents".format(
                task_id, attachment_id
            )
            metadata_url = "/tasks/{}/attachments/{}".format(task_id, attachment_id)
        elif incident_id:
            data_uri = "/incidents/{}/attachments/{}/contents".format(
                incident_id, attachment_id
            )
            metadata_url = "/incidents/{}/attachments/{}".format(
                incident_id, attachment_id
            )
        else:
            raise ValueError("task_id or incident_id must be specified with attachment")
    else:
        raise ValueError("artifact or attachment or incident id must be specified")

    # Get the data
    attachment = res_client.get_content(data_uri)
    if not metadata:
        metadata = res_client.get(metadata_url)

    return attachment, metadata


def get_environment_id(env_name):
    """Returns corrresponding environment id"""
    return HA_AVAILABLE_ENVS.get(env_name)


def get_runtime_action_script(action_script):
    """Returns corrresponding action script code"""
    return HA_AVAILABLE_RUNTIME_ACTION_SCRIPTS.get(action_script)
