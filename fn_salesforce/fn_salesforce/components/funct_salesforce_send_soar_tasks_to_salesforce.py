# -*- coding: utf-8 -*-
# Generated with resilient-sdk v49.1.51

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import SOARCommon, validate_fields, clean_html
from fn_salesforce.lib.app_common import (AppCommon, PACKAGE_NAME)

PACKAGE_NAME = "fn_salesforce"
FN_NAME = "salesforce_send_soar_tasks_to_salesforce"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'salesforce_send_soar_tasks_to_salesforce'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: None
        Inputs:
            -   fn_inputs.incident_id
            -   fn_inputs.salesforce_case_id
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        validate_fields(["incident_id", "salesforce_case_id"], fn_inputs)

        app_common = AppCommon(self.rc, self.PACKAGE_NAME, self.options)
        rest_client = self.rest_client()
        soar_common = SOARCommon(rest_client)
        
        # Get the tasks in the SOAR case and the Salesforce case
        soar_tasks = soar_common.get_case_tasks(fn_inputs.incident_id, True, True)
        sf_tasks = app_common.get_case_tasks(fn_inputs.salesforce_case_id)

        # Use a description header when sending SOAR tasks to Salesforce to easily identify 
        # where  
        description_header =  "Task from IBM SOAR case {0}:".format(fn_inputs.incident_id)
        soar_tasks_to_send = []
        for soar_task in soar_tasks:
            found = False
            # Search for the SOAR task in Salesforce task.
            # If the SOAR task name and the Salesforce task Subject are the same and the SOAR description
            # header appear in the header, then assume the task is already in Salesforce.
            for sf_task in sf_tasks:
                if soar_task.get("name") == sf_task.get("Subject") and description_header in sf_task.get("Description"):
                    found = True
                    break

            if not found:
                # SOAR task not found in Salesforce case, so add to list to send
                soar_tasks_to_send.append(soar_task)
            
        for soar_task in soar_tasks_to_send:
            description = "{0} {1}".format(description_header, clean_html(soar_task.get("instr_text")))

            salesforce_task_payload = {"WhatId": fn_inputs.salesforce_case_id,
                                       "Subject": soar_task.get("name", "Task from SOAR"),
                                       "Description": description,
                                       "Priority": "Normal" if soar_task.get("active") else "Complete", 
                                       "ActivityDate": soar_task.get("due_date")}
            response = app_common.create_task(salesforce_task_payload)

        results = {"task_count": len(soar_tasks_to_send)}

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        yield FunctionResult(results)
