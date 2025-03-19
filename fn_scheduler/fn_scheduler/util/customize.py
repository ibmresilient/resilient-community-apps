# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# Generated with resilient-sdk v51.0.2.2.1096

"""Generate the SOAR customizations required for fn_scheduler"""

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
    Parameters required reload codegen for the fn_scheduler package
    """
    return {
        "package": u"fn_scheduler",
        "message_destinations": [
            u"fn_scheduler"
        ],
        "functions": [
            u"create_a_scheduled_rule",
            u"list_scheduled_rules",
            u"remove_a_scheduled_rule",
            u"run_schedule_job_now",
            u"scheduled_rule_modify",
            u"scheduled_rule_pause",
            u"scheduled_rule_resume"
        ],
        "workflows": [],
        "actions": [],
        "incident_fields": [],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [
            u"scheduler_rules"
        ],
        "automatic_tasks": [],
        "scripts": [
            u"Write scheduled job to DataTable"
        ],
        "playbooks": [
            u"pb_scheduler_list_jobs",
            u"pb_scheduler_modify_job",
            u"pb_scheduler_pause_job",
            u"pb_scheduler_remove_job",
            u"pb_scheduler_resume_job",
            u"pb_scheduler_run_job_now",
            u"pb_scheduler_schedule_job",
            u"pb_scheduler_schedule_job_artifact",
            u"pb_scheduler_schedule_job_task"
        ]
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 51.0.0.0.9339

    Contents:
    - Message Destinations:
        - fn_scheduler
    - Functions:
        - create_a_scheduled_rule
        - list_scheduled_rules
        - remove_a_scheduled_rule
        - run_schedule_job_now
        - scheduled_rule_modify
        - scheduled_rule_pause
        - scheduled_rule_resume
    - Playbooks:
        - pb_scheduler_list_jobs
        - pb_scheduler_modify_job
        - pb_scheduler_pause_job
        - pb_scheduler_remove_job
        - pb_scheduler_resume_job
        - pb_scheduler_run_job_now
        - pb_scheduler_schedule_job
        - pb_scheduler_schedule_job_artifact
        - pb_scheduler_schedule_job_task
    - Data Tables:
        - scheduler_rules
    - Scripts:
        - Write scheduled job to DataTable
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)