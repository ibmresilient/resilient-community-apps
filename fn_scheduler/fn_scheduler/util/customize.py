# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_scheduler"""

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
        "message_destinations": [u"fn_scheduler"],
        "functions": [u"create_a_scheduled_rule", u"list_scheduled_rules", u"remove_a_scheduled_rule", u"scheduled_rule_modify", u"scheduled_rule_pause", u"scheduled_rule_resume"],
        "workflows": [u"list_schedules", u"modify_a_scheduled_rule", u"pause_a_scheduled_job", u"remove_a_schedule", u"resume_a_scheduled_job", u"schedule_a_rule_to_run__task", u"schedule_a_rule_to_run_artifact", u"schedule_rule_to_run"],
        "actions": [u"List Scheduled Jobs", u"Modify a Scheduled Job", u"Pause a Scheduled Job", u"Remove a Scheduled Job", u"Resume a Scheduled Job", u"Schedule a Rule/Playbook to Run", u"Schedule a Rule/Playbook to Run - Artifact", u"Schedule a Rule/Playbook to Run - Task"],
        "incident_fields": [],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [u"scheduler_rules"],
        "automatic_tasks": [],
        "scripts": []
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM Resilient Platform Version: 41.2.41

    Contents:
    - Message Destinations:
        - fn_scheduler
    - Functions:
        - create_a_scheduled_rule
        - list_scheduled_rules
        - remove_a_scheduled_rule
        - scheduled_rule_modify
        - scheduled_rule_pause
        - scheduled_rule_resume
    - Workflows:
        - list_schedules
        - modify_a_scheduled_rule
        - pause_a_scheduled_job
        - remove_a_schedule
        - resume_a_scheduled_job
        - schedule_a_rule_to_run__task
        - schedule_a_rule_to_run_artifact
        - schedule_rule_to_run
    - Rules:
        - List Scheduled Jobs
        - Modify a Scheduled Job
        - Pause a Scheduled Job
        - Remove a Scheduled Job
        - Resume a Scheduled Job
        - Schedule a Rule/Playbook to Run
        - Schedule a Rule/Playbook to Run - Artifact
        - Schedule a Rule/Playbook to Run - Task
    - Data Tables:
        - scheduler_rules
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)