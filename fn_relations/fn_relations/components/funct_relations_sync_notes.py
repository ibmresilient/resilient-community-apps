# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
# pragma pylint: disable=unused-argument, line-too-long
# Generated with resilient-sdk v49.1.51

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import IntegrationError, validate_fields
from fn_relations.lib.utilities import unix_to_datetime, list_children, locate_note_id
import re

PACKAGE_NAME = "fn_relations"
FN_NAME = "relations_sync_notes"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'relations_sync_notes'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Sync notes from the incident where the note is currently to the parent or child.
        Inputs:
            -   fn_inputs.relations_note_id
            -   fn_inputs.incident_id
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        validate_fields(["relations_note_id", "incident_id"], fn_inputs)

        relations_note_id = fn_inputs.relations_note_id
        incident_id = fn_inputs.incident_id
        self.LOG.info("incident_id: {}".format(incident_id))
        self.LOG.info("relations_note_id: {}".format(relations_note_id))


        self.LOG.info('Gathering Note from Incident')
        incident_note = self.rest_client().get('/incidents/{}/comments/{}?handle_format=names'.format(incident_id, relations_note_id))
        self.LOG.debug('Incident Note Gathered: {}'.format(incident_note))
        incident = self.rest_client().get("/incidents/{}?handle_format=names".format(incident_id))

        if incident['properties']['relations_level'] == 'Child':
            response_noteId = None
            if incident_note['parent_id']:
                self.LOG.info('Gathering Parent Note from Incident')
                parent_note = self.rest_client().get('/incidents/{}/comments/{}?handle_format=names'.format(incident_id, incident_note['parent_id']))
                self.LOG.debug('Parent Note Gathered: {}'.format(parent_note))

                self.LOG.info('Generating Response Note')
                html_note = []
                html_note.append('Response from Child Incident: <a href="#incidents/{0}" target="_blank">{0}</a><br>'.format(incident_id))

                if 'from Parent Incident:' in parent_note['text']:
                    self.LOG.info("Parsing Parent Note's Originating Note Info")
                    id_regex = re.compile(r'#incidents/(\d+)"')
                    sync_id = int(re.findall(id_regex, parent_note['text'])[0])
                    self.LOG.debug('Parent ID: {}'.format(sync_id))
                    noteId_regex = re.compile(r'Note ID: (\d+)')
                    response_noteId = int(re.findall(noteId_regex, parent_note['text'])[0])
                    self.LOG.debug('Originating Message Note ID: {}'.format(response_noteId))

                else:
                    self.LOG.info('Parsing Parent Incident ID')
                    id_regex = re.compile(r'#incidents/(\d+)"')
                    sync_id = int(re.findall(id_regex,incident['properties']['relations_parent_id'])[0])
                    self.LOG.debug('Parent ID: {}'.format(sync_id))
                    self.LOG.info('Collecting Parent Incident\'s Notes')
                    parent_incident_notes = self.rest_client().get('/incidents/{}/comments?handle_format=names'.format(sync_id))
                    response_noteId = locate_note_id(parent_note, parent_incident_notes)
                    self.LOG.debug('Originating Message Note ID: {}'.format(response_noteId))

            else:
                self.LOG.info('Parsing Parent Incident ID')
                id_regex = re.compile(r'#incidents/(\d+)"')
                sync_id = int(re.findall(id_regex,incident['properties']['relations_parent_id'])[0])
                self.LOG.debug('Parent ID: {}'.format(sync_id))

                self.LOG.info('Generating Synced Note')
                html_note = []
                html_note.append('Note from Child Incident: <a href="#incidents/{0}" target="_blank">{0}</a><br>'.format(incident_id))

            html_note.append('Note ID: {}<br>'.format(incident_note['id']))
            html_note.append("On Date: {}<br>".format(unix_to_datetime(incident_note["create_date"])))
            html_note.append("By: {}<br><br>".format(incident_note["user_name"]))
            html_note.append(incident_note["text"])
            if response_noteId:
                new_note = {"text": {"format": "html", "content": "".join(html_note)}, "parent_id": response_noteId}
            else:
                new_note =  {"text": {"format": "html", "content": "".join(html_note)}}
            self.LOG.debug('New Incident Note: {}'.format(new_note))
            posted_note = self.rest_client().post('/incidents/{}/comments?handle_format=names'.format(sync_id), new_note)
            self.LOG.info('Added Incident Note -- Incident ID: {0} | Note ID: {1}'.format(sync_id, posted_note['id']))


        elif incident['properties']['relations_level'] == 'Parent':
            if incident_note['parent_id']:
                self.LOG.info('Gathering Parent Note from Incident')
                parent_note = self.rest_client().get('/incidents/{}/comments/{}?handle_format=names'.format(incident_id, incident_note['parent_id']))
                self.LOG.debug('Parent Note Gathered: {}'.format(parent_note))

                if 'from Child Incident:' in parent_note['text']:
                    self.LOG.info("Parsing Parent Note's Originating Note Info")
                    id_regex = re.compile(r'#incidents/(\d+)"')
                    sync_id = int(re.findall(id_regex, parent_note['text'])[0])
                    self.LOG.debug('Parent ID: {}'.format(sync_id))
                    noteId_regex = re.compile(r'Note ID: (\d+)')
                    response_noteId = int(re.findall(noteId_regex, parent_note['text'])[0])
                    self.LOG.debug('Originating Message Note ID: {}'.format(response_noteId))

                    self.LOG.info('Generating Response Note')
                    html_note = []
                    html_note.append('Response from Parent Incident: <a href="#incidents/{0}" target="_blank">{0}</a><br>'.format(incident_id))
                    html_note.append('Note ID: {}<br>'.format(incident_note['id']))
                    html_note.append("On Date: {}<br>".format(unix_to_datetime(incident_note["create_date"])))
                    html_note.append("By: {}<br><br>".format(incident_note["user_name"]))
                    html_note.append(incident_note["text"])
                    new_note = {"text": {"format": "html", "content": "".join(html_note)}, "parent_id": response_noteId}
                    self.LOG.debug('New Incident Note: {}'.format(new_note))
                    posted_note = self.rest_client().post('/incidents/{}/comments?handle_format=names'.format(sync_id), new_note)
                    self.LOG.info('Added Incident Note -- Incident ID: {0} | Note ID: {1}'.format(sync_id, posted_note['id']))

                else:
                    self.LOG.info('Collecting Children Incidents.')
                    children_incidents = list_children(self.rest_client().get("/incidents/{}/table_data/dt_relations_child_incidents?handle_format=names".format(incident_id)))
                    self.LOG.debug('Child Incidents Found: {}'.format(str(children_incidents)))
                    child_relations = False
                    child_and_note = []
                    for child in children_incidents:
                        child_incident_notes = self.rest_client().get('/incidents/{}/comments?handle_format=names'.format(child))
                        child_note_id = locate_note_id(parent_note, child_incident_notes)
                        if child_note_id:
                            child_relations = True
                        child_and_note.append((child, child_note_id))
                        self.LOG.debug('Originating Child Message Note ID: {} from Child ID: {}'.format(child_note_id, child))

                    for child, note_id in child_and_note:
                        if child_relations:
                            if note_id:
                                self.LOG.info('Generating Synced Note')
                                html_note = []
                                html_note.append('Response from Parent Incident: <a href="#incidents/{0}" target="_blank">{0}</a><br>'.format(incident_id))
                                html_note.append('Note ID: {}<br>'.format(incident_note['id']))
                                html_note.append("On Date: {}<br>".format(unix_to_datetime(incident_note["create_date"])))
                                html_note.append("By: {}<br><br>".format(incident_note["user_name"]))
                                html_note.append(incident_note["text"])
                                new_note = {"text": {"format": "html", "content": "".join(html_note)}, "parent_id": note_id}
                                self.LOG.debug('New Incident Note: {}'.format(new_note))
                                posted_note = self.rest_client().post('/incidents/{}/comments?handle_format=names'.format(child), new_note)
                                self.LOG.info('Added Incident Note -- Incident ID: {0} | Note ID: {1}'.format(child, posted_note['id']))
                        else:
                            self.LOG.info('Generating Synced Note')
                            html_note = []
                            html_note.append('Note from Parent Incident: <a href="#incidents/{0}" target="_blank">{0}</a><br>'.format(incident_id))
                            html_note.append('Note ID: {}<br>'.format(incident_note['id']))
                            html_note.append("On Date: {}<br>".format(unix_to_datetime(incident_note["create_date"])))
                            html_note.append("By: {}<br><br>".format(incident_note["user_name"]))
                            html_note.append(incident_note["text"])
                            new_note =  {"text": {"format": "html", "content": "".join(html_note)}}
                            self.LOG.debug('New Incident Note: {}'.format(new_note))
                            posted_note = self.rest_client().post('/incidents/{}/comments?handle_format=names'.format(child), new_note)
                            self.LOG.info('Added Incident Note -- Incident ID: {0} | Note ID: {1}'.format(child, posted_note['id']))

            else:
                self.LOG.info('Generating Synced Note')
                html_note = []
                html_note.append('Note from Parent Incident: <a href="#incidents/{0}" target="_blank">{0}</a><br>'.format(incident_id))
                html_note.append('Note ID: {}<br>'.format(incident_note['id']))
                html_note.append("On Date: {}<br>".format(unix_to_datetime(incident_note["create_date"])))
                html_note.append("By: {}<br><br>".format(incident_note["user_name"]))
                html_note.append(incident_note["text"])
                new_note =  {"text": {"format": "html", "content": "".join(html_note)}}
                self.LOG.debug('New Incident Note: {}'.format(new_note))
                self.LOG.info('Collecting Children Incidents.')
                children_incidents = list_children(self.rest_client().get("/incidents/{}/table_data/dt_relations_child_incidents?handle_format=names".format(incident_id)))
                self.LOG.debug('Child Incidents Found: {}'.format(str(children_incidents)))
                for child in children_incidents:
                    self.LOG.debug('New Incident Note: {}'.format(new_note))
                    posted_note = self.rest_client().post('/incidents/{}/comments?handle_format=names'.format(child), new_note)
                    self.LOG.info('Added Incident Note -- Incident ID: {0} | Note ID: {1}'.format(child, posted_note['id']))
        else:
            raise IntegrationError("Incident does not have a relation level. Unable to sync note.")

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        results = {'new_note': new_note}

        yield FunctionResult(results)
        # yield FunctionResult({}, success=False, reason="Bad call")
