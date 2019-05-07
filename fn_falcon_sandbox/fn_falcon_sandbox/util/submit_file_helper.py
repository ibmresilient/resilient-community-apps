# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
import time
import requests
import tempfile
import os
from requests_toolbelt import MultipartEncoder
from resilient_circuits import FunctionError

AVAILABLE_ENVS = {
                    "Android Static Analysis": "200",
                    "Linux (Ubuntu 16.04, 64 bit)": "300",
                    "Windows 7 32 bit": "100",
                    "Windows 7 32 bit (HWP Support)": "110",
                    "Windows 7 64 bit": "120"
                }
AVAILABLE_RUNTIME_ACTION_SCRIPTS = {
    "Default analysis": "default.au3",
    "Heavy Anti-Evasion": "default_maxantievasion.au3",
    "Random desktop files": "default_randomfiles.au3",
    "Random desktop theme": "default_randomtheme.au3",
    "Open Internet Explorer": "default_openie.au3",
    "Default browser analysis": "default_browser.au3"
}
# List of runtime resilient function parameters and their default value
LIST_OF_RUNTIME_PARAMS = [
    "falcon_sandbox_environment_id",
    "falcon_sandbox_action_script",
    "falcon_sandbox_no_share_third_party",
    "falcon_sandbox_allow_community_access",
    "falcon_sandbox_comment",
    "falcon_sandbox_priority",
    "falcon_sandbox_environment_variable",
    "falcon_sandbox_custom_run_time",
    "falcon_sandbox_submit_name",
    "falcon_sandbox_custom_date_time",
    "falcon_sandbox_document_password",
    "falcon_sandbox_tor_enabled_analysis",
]

def write_temp_file(data, name=None):
    temp_files = []
    path = None

    if (name):
        path = "{0}/{1}".format(tempfile.gettempdir(), name)
    else:
        tf = tempfile.mkstemp()
        path = tf[1]

    fo = open(path, 'wb')
    temp_files.append(path)
    fo.write(data)
    fo.close()
    return path, temp_files

def remove_temp_files(files):
    for f in files:
        os.remove(f)

def falcon_sandbox_request_header(api_key):
    return {
            "accept": "application/json", 
            "user-agent": "Falcon Sandbox",
            "api-key": "{}".format(api_key) 
        }

def get_submission_queue_size(host_url, api_key):
    """ This function returns current submission queue size of Falcon Sandbox"""

    headers = falcon_sandbox_request_header(api_key)
    url = "{}/system/queue-size".format(host_url)
    response = requests.get(url, headers=headers)
    response_json = response.json()
    return response_json['value']

def get_attachment_uri(incident_id, task_id, artifact_id, attachment_id):
    """ This function determines user's choice from inputs 
        and then returns attachment URI and metadata URI
    """
    attachment_src = 'incident'
    if task_id:
        file_metadata_uri = "/tasks/{}/attachments/{}".format(task_id, attachment_id)
        file_uri = "/tasks/{}/attachments/{}/contents".format(task_id, attachment_id)
    elif artifact_id:
        file_metadata_uri = "/incidents/{0}/artifacts/{1}".format(incident_id, artifact_id)
        file_uri = "/incidents/{0}/artifacts/{1}/contents".format(incident_id, artifact_id)
        attachment_src = 'artifact'
    else:
        file_metadata_uri = "/incidents/{}/attachments/{}".format(incident_id, attachment_id)
        file_uri = "/incidents/{}/attachments/{}/contents".format(incident_id, attachment_id)
        attachment_src = 'task'

    return file_uri, file_metadata_uri, attachment_src

def get_environment_id(env_name):
    return AVAILABLE_ENVS.get(env_name)

def get_runtime_action_script(action_script):
    return AVAILABLE_RUNTIME_ACTION_SCRIPTS.get(action_script)

def submit_file_to_falcon_sandbox(host_url, header, submit_payload):
    url = "{}/submit/file".format(host_url)
    response = requests.post(url, headers=header, data=submit_payload)
    return response.json()

def get_report_status(host_url, header, job_id):
    url = "{}/report/{}/state".format(host_url, job_id)
    response = requests.get(url, headers=header)
    return response.json()

def get_report_summary(host_url, header, job_id):
    url = "{}/report/{}/summary".format(host_url, job_id)
    response = requests.get(url, headers=header)
    return response.json()