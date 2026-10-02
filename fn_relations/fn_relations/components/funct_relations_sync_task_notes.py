# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
# pragma pylint: disable=unused-argument, line-too-long
# Generated with resilient-sdk v48.1.4243

"""AppFunction implementation"""

import re
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import IntegrationError, validate_fields
from fn_relations.lib.utilities import unix_to_datetime, list_children, locate_note_id

PACKAGE_NAME = "fn_relations"
FN_NAME = "relations_sync_task_notes"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'relations_sync_task_notes'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Sync Task notes from a copied Task back to parent originating Task.
        Inputs:
            -   fn_inputs.relations_note_id
            -   fn_inputs.task_id
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        validate_fields(["relations_note_id", "task_id"], fn_inputs)

        relations_note_id = fn_inputs.relations_note_id
        task_id = fn_inputs.task_id
        self.LOG.info("relations_parent_incident_id: {}".format(relations_note_id))
        self.LOG.info("task_id: {}".format(task_id))


        self.LOG.info('Gathering Note from Task')
        task_note = self.rest_client().get('/tasks/{}/comments/{}?handle_format=names'.format(task_id, relations_note_id))
        self.LOG.debug('Task Note Gathered: {}'.format(task_note))
        incident = self.rest_client().get("/incidents/{}?handle_format=names".format(task_note["inc_id"]))

        if incident['properties']['relations_level'] == 'Child':
            response_noteId = None
            if task_note['parent_id']:
                self.LOG.info('Gathering Parent Note from Task')
                parent_task_note = self.rest_client().get('/tasks/{}/comments/{}?handle_format=names'.format(task_id, task_note['parent_id']))
                self.LOG.debug('Parent Task Note Gathered: {}'.format(parent_task_note))
                self.LOG.info('Generating Synced Note')
                html_note = []
                html_note.append('Response from Child Incident: <a href="#incidents/{0}" target="_blank">{0}</a><br>'.format(task_note["inc_id"]))

                if 'from Parent Incident:' in parent_task_note['text']:
                    self.LOG.info("Parsing Parent Task Note's Originating Note Info")
                    taskId_regex = re.compile(r'Task: <a href="#incidents/\d+\?taskId=(\d+)\&')
                    noteId_regex = re.compile(r'Note ID: (\d+)')
                    parent_task_id = re.findall(taskId_regex, parent_task_note['text'])[0]
                    self.LOG.debug('Originating Message Task ID: {}'.format(parent_task_id))
                    response_noteId = re.findall(noteId_regex, parent_task_note['text'])[0]
                    self.LOG.debug('Originating Message Note ID: {}'.format(response_noteId))

                else:
                    self.LOG.info('Parsing Parent Incident Task ID')
                    regex = re.compile(r'Task (\d+) from Parent:')
                    parent_task_id = re.findall(regex, task_note['task_name'])[0]
                    self.LOG.debug('Parsed Parent Task ID: {}'.format(parent_task_id))
                    self.LOG.info('Collecting Parent Task\'s Notes')
                    parent_incident_task_notes = self.rest_client().get('/tasks/{}/comments?handle_format=names'.format(parent_task_id))
                    response_noteId = locate_note_id(parent_task_note, parent_incident_task_notes)
                    self.LOG.debug('Originating Message Note ID: {}'.format(response_noteId))

            else:
                self.LOG.info('Parsing Parent Incident Task ID')
                regex = re.compile(r'Task (\d+) from Parent:')
                parent_task_id = re.findall(regex, task_note['task_name'])[0]
                self.LOG.debug('Parsed Parent Task ID: {}'.format(parent_task_id))

                self.LOG.info('Generating Synced Note')
                html_note = []
                html_note.append('Note from Child Incident: <a href="#incidents/{0}" target="_blank">{0}</a><br>'.format(task_note["inc_id"]))

            html_note.append('Task: <a href="#incidents/{}?taskId={}&tabName=comments" target="_blank">{}</a><br>'.format(task_note["inc_id"], task_note["task_id"], task_note["task_name"]))
            html_note.append('Note ID: {}<br>'.format(task_note['id']))
            html_note.append("On Date: {}<br>".format(unix_to_datetime(task_note["create_date"])))
            html_note.append("By: {}<br><br>".format(task_note["user_name"]))
            html_note.append(task_note["text"])
            if response_noteId:
                new_note = {"text": {"format": "html", "content": "".join(html_note)}, "parent_id": response_noteId}
            else:
                new_note = {"text": {"format": "html", "content": "".join(html_note)}}
            self.LOG.debug('New Task Note: {}'.format(new_note))
            posted_note = self.rest_client().post('/tasks/{}/comments?handle_format=names'.format(parent_task_id), new_note)
            self.LOG.info('Added Task Note -- Task ID: {0} | Note ID: {1}'.format(parent_task_id, posted_note['id']))

        elif incident['properties']['relations_level'] == 'Parent':
            if task_note['parent_id']:
                self.LOG.info('Gathering Parent Note from Task')
                parent_task_note = self.rest_client().get('/tasks/{}/comments/{}?handle_format=names'.format(task_id, task_note['parent_id']))
                self.LOG.debug('Parent Task Note Gathered: {}'.format(parent_task_note))
                if 'from Child Incident:' in parent_task_note['text']:
                    self.LOG.info("Parsing Parent Task Note's Originating Note Info")
                    taskId_regex = re.compile(r'Task: <a href="#incidents/\d+\?taskId=(\d+)\&')
                    noteId_regex = re.compile(r'Note ID: (\d+)')
                    response_taskId = re.findall(taskId_regex, parent_task_note['text'])[0]
                    self.LOG.debug('Originating Message Task ID: {}'.format(response_taskId))
                    response_noteId = re.findall(noteId_regex, parent_task_note['text'])[0]
                    self.LOG.debug('Originating Message Note ID: {}'.format(response_noteId))

                    self.LOG.info('Generating Response Note')
                    html_note = []
                    html_note.append('Response from Parent Incident: <a href="#incidents/{0}" target="_blank">{0}</a><br>'.format(task_note["inc_id"]))
                    html_note.append('Task: <a href="#incidents/{}?taskId={}&tabName=comments" target="_blank">{}</a><br>'.format(task_note["inc_id"], task_note["task_id"], task_note["task_name"]))
                    html_note.append('Note ID: {}<br>'.format(task_note['id']))
                    html_note.append("On Date: {}<br>".format(unix_to_datetime(task_note["create_date"])))
                    html_note.append("By: {}<br><br>".format(task_note["user_name"]))
                    html_note.append(task_note["text"])
                    new_note = {"text": {"format": "html", "content": "".join(html_note)}, "parent_id": response_noteId}
                    self.LOG.debug('New Task Note: {}'.format(new_note))
                    posted_note = self.rest_client().post('/tasks/{}/comments?handle_format=names'.format(response_taskId), new_note)
                    self.LOG.info('Added Task Note -- Task ID: {0} | Note ID: {1}'.format(response_taskId, posted_note['id']))

                else:
                    self.LOG.info('Collecting Children Incidents.')
                    children_incidents = list_children(self.rest_client().get("/incidents/{}/table_data/dt_relations_child_incidents?handle_format=names".format(task_note["inc_id"])))
                    self.LOG.debug('Child Incidents Found: {}'.format(str(children_incidents)))

                    children_tasks = []
                    for child in children_incidents:
                        self.LOG.info("Checking Incident's {} Tasks".format(child))
                        tasks = self.rest_client().get('/incidents/{}/tasks?handle_format=names'.format(child))
                        self.LOG.debug('Tasks Found: {}'.format(str(tasks)))
                        for task in tasks:
                            if task_note['task_name'] in task['name']:
                                self.LOG.debug('Located Related Task ID: {}'.format(task['id']))
                                children_tasks.append(task['id'])
                    child_relations = False
                    task_and_note = []
                    for child_task in children_tasks:
                        self.LOG.info("Checking Task's {} Notes.".format(child_task))
                        child_incident_task_notes = self.rest_client().get('/tasks/{}/comments?handle_format=names'.format(child_task))
                        self.LOG.debug("Task Notes Found: {}".format(child_incident_task_notes))
                        response_noteId = locate_note_id(parent_task_note, child_incident_task_notes)
                        if response_noteId:
                            child_relations = True
                        task_and_note.append((child_task, response_noteId))
                        self.LOG.debug('Originating Task Note ID: {} from Task: {}'.format(response_noteId, child_task))

                    for child_task_id, note_id in task_and_note:
                        if child_relations:
                            if note_id:
                                self.LOG.info('Generating Synced Note')
                                html_note = []
                                html_note.append('Response from Parent Incident: <a href="#incidents/{0}" target="_blank">{0}</a><br>'.format(task_note["inc_id"]))
                                html_note.append('Task: <a href="#incidents/{}?taskId={}&tabName=comments" target="_blank">{}</a><br>'.format(task_note["inc_id"], task_note["task_id"], task_note["task_name"]))
                                html_note.append('Note ID: {}<br>'.format(task_note['id']))
                                html_note.append("On Date: {}<br>".format(unix_to_datetime(task_note["create_date"])))
                                html_note.append("By: {}<br><br>".format(task_note["user_name"]))
                                html_note.append(task_note["text"])
                                new_note = {"text": {"format": "html", "content": "".join(html_note)}, "parent_id": note_id}
                                self.LOG.debug('New Task Note: {}'.format(new_note))
                                posted_note = self.rest_client().post('/tasks/{}/comments?handle_format=names'.format(child_task_id), new_note)
                                self.LOG.info('Added Task Note -- Task ID: {0} | Note ID: {1}'.format(child_task_id, posted_note['id']))
                        else:
                            self.LOG.info('Generating Synced Note')
                            html_note = []
                            html_note.append('Note from Parent Incident: <a href="#incidents/{0}" target="_blank">{0}</a><br>'.format(task_note["inc_id"]))
                            html_note.append('Task: <a href="#incidents/{}?taskId={}&tabName=comments" target="_blank">{}</a><br>'.format(task_note["inc_id"], task_note["task_id"], task_note["task_name"]))
                            html_note.append('Note ID: {}<br>'.format(task_note['id']))
                            html_note.append("On Date: {}<br>".format(unix_to_datetime(task_note["create_date"])))
                            html_note.append("By: {}<br><br>".format(task_note["user_name"]))
                            html_note.append(task_note["text"])
                            new_note = {"text": {"format": "html", "content": "".join(html_note)}}
                            self.LOG.debug('New Task Note: {}'.format(new_note))
                            posted_note = self.rest_client().post('/tasks/{}/comments?handle_format=names'.format(child_task_id), new_note)
                            self.LOG.info('Added Task Note -- Task ID: {0} | Note ID: {1}'.format(child_task_id, posted_note['id']))

            else:
                self.LOG.info('Collecting Children Incidents.')
                children_incidents = list_children(self.rest_client().get("/incidents/{}/table_data/dt_relations_child_incidents?handle_format=names".format(task_note["inc_id"])))
                self.LOG.debug('Child Incidents Found: {}'.format(str(children_incidents)))
                self.LOG.info('Generating Synced Note')
                html_note = []
                html_note.append('Note from Parent Incident: <a href="#incidents/{0}" target="_blank">{0}</a><br>'.format(task_note["inc_id"]))
                html_note.append('Task: <a href="#incidents/{}?taskId={}&tabName=comments" target="_blank">{}</a><br>'.format(task_note["inc_id"], task_note["task_id"], task_note["task_name"]))
                html_note.append('Note ID: {}<br>'.format(task_note['id']))
                html_note.append("On Date: {}<br>".format(unix_to_datetime(task_note["create_date"])))
                html_note.append("By: {}<br><br>".format(task_note["user_name"]))
                html_note.append(task_note["text"])
                new_note = {"text": {"format": "html", "content": "".join(html_note)}}
                self.LOG.debug('New Task Note: {}'.format(new_note))

                for child in children_incidents:
                    self.LOG.info("Checking Incident's {} Tasks".format(child))
                    tasks = self.rest_client().get('/incidents/{}/tasks?handle_format=names'.format(child))
                    self.LOG.debug('Tasks Found: {}'.format(str(tasks)))
                    for task in tasks:
                        if task_note['task_name'] in task['name']:
                            self.LOG.debug('Located Related Task ID: {}'.format(task['id']))
                            child_task_id = task['id']
                            break
                    self.LOG.debug('Matched Child Task ID: {} to Parent Task ID: {}'.format(child_task_id, task_note["task_id"]))
                    posted_note = self.rest_client().post('/tasks/{}/comments?handle_format=names'.format(child_task_id), new_note)
                    self.LOG.info('Added Task Note -- Task ID: {0} | Note ID: {1}'.format(child_task_id, posted_note['id']))

        else:
            raise IntegrationError("Incident does not have a relation level. Unable to sync note.")

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        results = {'new_note': new_note}

        yield FunctionResult(results)
        # yield FunctionResult({}, success=False, reason="Bad call")
