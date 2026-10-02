# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
# pragma pylint: disable=unused-argument, line-too-long
# Generated with resilient-sdk v48.1.4243

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields
from fn_relations.lib.utilities import list_children


PACKAGE_NAME = "fn_relations"
FN_NAME = "relations_copy_task"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'relations_copy_task'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Copy a task from a Parent Incident down to the Children.
        Inputs:
            -   fn_inputs.relations_parent_incident_id
            -   fn_inputs.task_id
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        validate_fields(["relations_parent_incident_id", "task_id"], fn_inputs)

        relations_parent_incident_id = fn_inputs.relations_parent_incident_id
        task_id = fn_inputs.task_id
        self.LOG.info("relations_parent_incident_id: {}".format(relations_parent_incident_id))
        self.LOG.info("task_id: {}".format(task_id))


        self.LOG.info('Gathering Task from Incident')
        parent_task = self.rest_client().get('/tasks/{}?handle_format=names'.format(task_id))
        self.LOG.debug('Task Gathered: {}'.format(parent_task))
        task_variables = ['name', 'due_date', 'phase_id', 'required', 'instructions']
        child_task = {}
        for item in task_variables:
            child_task[item] = parent_task[item]
        child_task['name'] = 'Task {} from Parent: '.format(task_id) + child_task['name']
        self.LOG.debug('New Task: {}'.format(child_task))
        children_incidents = list_children(self.rest_client().get("/incidents/{}/table_data/dt_relations_child_incidents?handle_format=names".format(relations_parent_incident_id)))
        for child in children_incidents:
            self.LOG.info('Syncing Artifact to Child ID: {}'.format(child))
            copied_task = self.rest_client().post('/incidents/{}/tasks?handle_format=names'.format(child), child_task)
            self.LOG.info('Added Child Task -- Task ID: {0}'.format(copied_task['id']))

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        results = {'task': child_task, 'children': children_incidents}

        yield FunctionResult(results)
        # yield FunctionResult({}, success=False, reason="Bad call")
