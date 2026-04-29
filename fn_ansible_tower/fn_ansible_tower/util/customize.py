# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# Generated with resilient-sdk v51.0.2.2.1096

"""Generate the SOAR customizations required for fn_ansible_tower"""

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
    Parameters required reload codegen for the fn_ansible_tower package
    """
    return {
        "package": u"fn_ansible_tower",
        "message_destinations": [
            u"fn_ansible_tower"
        ],
        "functions": [
            u"ansible_tower_get_ad_hoc_command_results",
            u"ansible_tower_get_job_results",
            u"ansible_tower_launch_job_template",
            u"ansible_tower_list_job_templates",
            u"ansible_tower_list_jobs",
            u"ansible_tower_run_an_ad_hoc_command"
        ],
        "workflows": [
            u"ansible_tower_get_ad_hoc_command_results",
            u"ansible_tower_get_job_results",
            u"ansible_tower_launch_job_template",
            u"ansible_tower_list_job_templates",
            u"ansible_tower_list_jobs",
            u"ansible_tower_run_an_ad_hoc_command",
            u"ansible_tower_run_job__artifact",
            u"ansible_tower_run_job__incident"
        ],
        "actions": [
            u"Ansible Tower Get Ad Hoc Command Results",
            u"Ansible Tower Get Job Results",
            u"Ansible Tower List Job Templates",
            u"Ansible Tower List Jobs",
            u"Ansible Tower Run an Ad Hoc Command",
            u"Ansible Tower Run Job",
            u"Ansible Tower Run Job - Artifact",
            u"Ansible Tower Run Job - Incident"
        ],
        "incident_fields": [],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [
            u"ansible_tower_job_templates",
            u"ansible_tower_launched_jobs"
        ],
        "automatic_tasks": [],
        "scripts": [],
        "playbooks": [],
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 51.0.0.0.9340

    Contents:
    - Message Destinations:
        - fn_ansible_tower
    - Functions:
        - ansible_tower_get_ad_hoc_command_results
        - ansible_tower_get_job_results
        - ansible_tower_launch_job_template
        - ansible_tower_list_job_templates
        - ansible_tower_list_jobs
        - ansible_tower_run_an_ad_hoc_command
    - Workflows:
        - ansible_tower_get_ad_hoc_command_results
        - ansible_tower_get_job_results
        - ansible_tower_launch_job_template
        - ansible_tower_list_job_templates
        - ansible_tower_list_jobs
        - ansible_tower_run_an_ad_hoc_command
        - ansible_tower_run_job__artifact
        - ansible_tower_run_job__incident
    - Rules:
        - Ansible Tower Get Ad Hoc Command Results
        - Ansible Tower Get Job Results
        - Ansible Tower List Job Templates
        - Ansible Tower List Jobs
        - Ansible Tower Run an Ad Hoc Command
        - Ansible Tower Run Job
        - Ansible Tower Run Job - Artifact
        - Ansible Tower Run Job - Incident
    - Data Tables:
        - ansible_tower_job_templates
        - ansible_tower_launched_jobs
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)