# -*- coding: utf-8 -*-
# Generated with resilient-sdk v49.1.51

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import SOARCommon, validate_fields, clean_html, build_task_url
from fn_salesforce.lib.app_common import (AppCommon, PACKAGE_NAME)

FN_NAME = "salesforce_sync_tasks_between_cases"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'salesforce_sync_tasks_between_cases'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Synchronize tasks between Salesforce case and SOAR case.
        Inputs:
            -   fn_inputs.incident_id
            -   fn_inputs.salesforce_case_id
            -   fn_inputs.task_sync_direction
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        validate_fields(["incident_id", "salesforce_case_id"], fn_inputs)

        app_common = AppCommon(self.PACKAGE_NAME, self.options)
        rest_client = self.rest_client()
        soar_common = SOARCommon(rest_client)
        
        # Get the tasks in the SOAR case and the Salesforce case
        soar_tasks = soar_common.get_case_tasks(fn_inputs.incident_id, True, True)
        sf_tasks = app_common.get_case_tasks(fn_inputs.salesforce_case_id)

        # Use a description header when sending SOAR tasks to Salesforce to easily identify 
        # where the originated from so we don't sent multiple times.
        soar_description_header =  "Task from IBM SOAR case {0}:".format(fn_inputs.incident_id)
        sf_description_header =  "Task from Salesforce case {0}:".format(fn_inputs.salesforce_case_id)

        soar_tasks_to_send = []
        if fn_inputs.task_sync_direction in ["Salesforce", "Both"]:
            # Look for SOAR tasks to send to Salesforce 

            for soar_task in soar_tasks:
                found = False
                # First check if this task came from SOAR, then we don't need to add to SOAR.
                if soar_task.get("instr_text") and sf_description_header in soar_task.get("instr_text"):
                    continue
                # Search for the SOAR task in Salesforce task.
                # If the SOAR task name and the Salesforce task Subject are the same and the SOAR description
                # header appear in the header, then assume the task is already in Salesforce.
                for sf_task in sf_tasks:
                    if soar_task.get("name") == sf_task.get("Subject") and soar_description_header in sf_task.get("Description", ""):
                        found = True
                        break

                if not found:
                    # SOAR task not found in Salesforce case, so add to list to send
                    soar_tasks_to_send.append(soar_task)
            
            for soar_task in soar_tasks_to_send:
                task_link = build_task_url(rest_client.base_url, fn_inputs.incident_id, soar_task.get("id"), rest_client.org_id)
                description = "{0} {1} {2}".format(soar_description_header, task_link, clean_html(soar_task.get("instr_text")))

                salesforce_task_payload = {"WhatId": fn_inputs.salesforce_case_id,
                                           "Subject": soar_task.get("name", "Task from SOAR"),
                                           "Description": description,
                                           "Priority": "Normal" if soar_task.get("active") else "Complete", 
                                           "ActivityDate": soar_task.get("due_date")}
                response = app_common.create_task(salesforce_task_payload)

        sf_tasks_to_get = []
        if fn_inputs.task_sync_direction in ["SOAR", "Both"]:
            # Look for Salesforce tasks to send to SOAR
            for sf_task in sf_tasks:
                found = False
                # First check if this task came from SOAR, then we don't need to add to SOAR.
                if sf_task.get("Description") and soar_description_header in sf_task.get("Description"):
                    continue
                # Search for the Salesforce tasks not in SOAR.
                # If the SOAR task name and the Salesforce task Subject are the same and the SOAR description
                # header does not appear in the header, then assume the task is already is from Salesforce.
                for soar_task in soar_tasks:
                    if (soar_task.get("name") == sf_task.get("Subject")) and sf_description_header in soar_task.get("instr_text"):
                        found = True
                        break

                if not found:
                    # Salesforce task not found in SOAR case, so add to list to send
                    sf_tasks_to_get.append(sf_task)

            # Add the tasks to SOAR case
            for sf_task in sf_tasks_to_get:
                sf_task_link = app_common.make_linkback_url(entity_type='Task', entity_id=sf_task.get("Id"))
                description = "{0} {1} {2}".format(sf_description_header, sf_task_link, sf_task.get("Description"))
                soar_task_payload = {"name": sf_task.get("Subject"),
                                     "instr_text": description,
                                     "due_date": sf_task.get("ActivityDate")}
            
                rest_client.post("/incidents/{}/tasks".format(fn_inputs.incident_id), soar_task_payload)

        results = {"task_count_to_salesforce": len(soar_tasks_to_send),
                   "task_count_to_soar": len(sf_tasks_to_get)}

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        yield FunctionResult(results)
