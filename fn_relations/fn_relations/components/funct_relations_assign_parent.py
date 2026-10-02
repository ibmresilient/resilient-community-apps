# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
# pragma pylint: disable=unused-argument, line-too-long
# Generated with resilient-sdk v49.1.51

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import IntegrationError, validate_fields
from fn_relations.lib.utilities import unix_to_datetime, list_children, list_artifacts
from fn_relations.lib.configure_tab import init_relations_layout

PACKAGE_NAME = "fn_relations"
FN_NAME = "relations_assign_parent"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'relations_assign_parent'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

        # initialize the layouts for this tabs, sections, etc.
        init_relations_layout(opts)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Create a parent/child relationship between the 2 incidents provided.
        Inputs:
            -   fn_inputs.relations_parent_incident_id
            -   fn_inputs.relations_child_incident_id
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        validate_fields(["relations_parent_incident_id", "relations_child_incident_id"], fn_inputs)

        relations_parent_incident_id = fn_inputs.relations_parent_incident_id
        relations_child_incident_id = fn_inputs.relations_child_incident_id
        self.LOG.info("relations_child_incident_id: {}".format(relations_child_incident_id))
        self.LOG.info("relations_parent_incident_id: {}".format(relations_parent_incident_id))

        def update_parent(incident):
            incident["properties"]["relations_level"] = "Parent"
            return(incident)


        def update_child(incident):
            incident["properties"]["relations_level"] = "Child"
            incident["properties"]["relations_parent_id"] = '<div class="rte"><div><a href="#incidents/{0}" target="_blank">{0}</a></div></div>'.format(relations_parent_incident_id)
            return(incident)


        def recursive_note_copy(parent_note_id, note_list):
            for note in note_list:
                if note['text']:
                    self.LOG.info('Generating Synced Note')
                    html_note = []
                    html_note.append("Note from Child Incident: <a href='#incidents/{0}' target='_blank'>{0}</a><br>".format(note["inc_id"]))
                    html_note.append('Note ID: {}<br>'.format(note['id']))
                    html_note.append("On Date: {}<br>".format(unix_to_datetime(note["create_date"])))
                    html_note.append("By: {}<br><br>".format(note["user_name"]))
                    html_note.append(note["text"])
                    new_note = {"text": {"format": "html", "content": "".join(html_note)}, "parent_id": parent_note_id}
                    self.LOG.debug('New Note: {}'.format(new_note))
                    synced_note = self.rest_client().post("/incidents/{}/comments".format(relations_parent_incident_id), new_note)
                    self.LOG.info('Added Parent Note -- Note ID: {0} | Note Text: {1}'.format(synced_note['id'],synced_note['text']))

                if note['children']:
                    recursive_note_copy(synced_note['id'], note['children'])


        """Verify the Parent Incident"""
        try:
            self.rest_client().get("/incidents/{}".format(relations_parent_incident_id))
        except Exception as e:
            if type(e).__name__ == 'SimpleHTTPException':
                raise IntegrationError("Parent incident provided does not exist: {}".format(relations_parent_incident_id))
            else:
                raise IntegrationError(e)

        """Verify that Child and Parent Incidents are Different"""
        if relations_child_incident_id == relations_parent_incident_id:
            raise IntegrationError("Parent and Child incident can not be the same incident: {}".format(relations_parent_incident_id))

        """Update the child"""
        self.LOG.info('Updating Child Incident')
        updated_child_incident = self.rest_client().get_put("/incidents/{}".format(relations_child_incident_id), update_child)
        self.LOG.debug('Updated Child Incident: {}'.format(updated_child_incident))

        child_artifacts = self.rest_client().get("/incidents/{}/artifacts?handle_format=names".format(relations_child_incident_id))
        child_artifact_values = list_artifacts(child_artifacts)
        self.LOG.debug('Child Related Parent Incidents: {}'.format(child_artifact_values))
        if relations_parent_incident_id not in child_artifact_values:
            self.LOG.info('Adding Child Artifact')
            new_artifact = {'description': 'Parent Incident ID in Relationship',
                            'type': 'related_parent_incident',
                            'value': relations_parent_incident_id}
            self.LOG.debug('New Child Artifact: {}'.format(new_artifact))
            posted_child_artifact = self.rest_client().post("/incidents/{}/artifacts".format(relations_child_incident_id),new_artifact)[0]
            self.LOG.info('Added Child Incident Artifact -- Artifact Type: {0} | Artifact ID: {1} | Artifact Value: {2}'.format(posted_child_artifact['type'],posted_child_artifact['id'],posted_child_artifact['value']))
            child_artifact_results = {"success": True, "content": posted_child_artifact}
        else:
            self.LOG.info('Child Artifact Already Exists')
            child_artifact_results = {"success": False, "content": "Parent Already in Artifacts"}
        self.LOG.info("Child Updated")

        """Update the parent"""
        self.LOG.info('Updating Parent Incident')
        updated_parent_incident = self.rest_client().get_put("/incidents/{}".format(relations_parent_incident_id), update_parent)
        self.LOG.debug('Updated Parent Incident: {}'.format(updated_parent_incident))

        child_table = self.rest_client().get("/incidents/{}/table_data/dt_relations_child_incidents?handle_format=names".format(relations_parent_incident_id))
        children_incidents = list_children(child_table)
        self.LOG.debug('Children Incidents of Parent: {}'.format(children_incidents))
        if relations_child_incident_id not in children_incidents:
            self.LOG.info('Adding Child Incident Row')
            child_incident = self.rest_client().get("/incidents/{}".format(relations_child_incident_id))
            new_row = {'cells': {'relations_incident_id': {'value': '<div class="rte"><div><a href="#incidents/{0}" target="_blank">{0}</a></div></div>'.format(child_incident['id'])},
                                 'relations_incident_name': {'value': child_incident['name']},
                                 'relations_incident_status': {'value': 'Active' if child_incident['plan_status'] == 'A' else 'Closed'}
                       }}
            self.LOG.debug('New Child Incident Row: {}'.format(new_row))
            posted_row = self.rest_client().post("/incidents/{}/table_data/dt_relations_child_incidents/row_data?handle_format=names".format(relations_parent_incident_id),new_row)
            self.LOG.info('Added Row -- Row ID: {0} | Incident ID: {1} | Incident Name: {2}'.format(posted_row['id'],child_incident['id'],posted_row['cells']['relations_incident_name']['value']))
            table_additions_results = {"success": True, "content": posted_row}
        else:
            self.LOG.info('Child Incident Already in Data Table')
            table_additions_results = {"success": False, "content": "Incident Already in Data Table"}

        parent_artifacts = self.rest_client().get("/incidents/{}/artifacts?handle_format=names".format(relations_parent_incident_id))
        parent_artifact_values = list_artifacts(parent_artifacts)
        self.LOG.debug('Parent Related Parent Incidents: {}'.format(parent_artifact_values))
        if relations_parent_incident_id not in parent_artifact_values:
            self.LOG.info('Adding Parent Artifact')
            new_artifact = {'description': 'Parent Incident ID in Relationship',
                            'type': 'related_parent_incident',
                            'value': relations_parent_incident_id}
            self.LOG.debug('New Parent Artifact: {}'.format(new_artifact))
            posted_parent_artifact = self.rest_client().post("/incidents/{}/artifacts".format(relations_parent_incident_id),new_artifact)[0]
            self.LOG.info('Added Parent Incident Artifact -- Artifact Type: {0} | Artifact ID: {1} | Artifact Value: {2}'.format(posted_parent_artifact['type'],posted_parent_artifact['id'],posted_parent_artifact['value']))
            parent_artifact_results = {"success": True, "content": posted_parent_artifact}
        else:
            self.LOG.info('Parent Artifact Already Exists')
            parent_artifact_results = {"success": False, "content": "Parent Already in Artifacts"}
        self.LOG.info("Parent Updated")

        """Sync Notes from Child to Parent"""
        self.LOG.info('Checking for Child Notes to Sync')
        notes = self.rest_client().get("/incidents/{}/comments".format(relations_child_incident_id))
        if len(notes) > 0:
            recursive_note_copy(None, notes)
            self.LOG.info("Notes Synced")
        else:
            self.LOG.info("No Notes to Sync")

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        results = {
            'child_artifact_results': child_artifact_results,
            'table_addition_results': table_additions_results,
            'parent_artifact_results': parent_artifact_results,
            'notes_synced': len(notes)
        }

        yield FunctionResult(results)
        # yield FunctionResult({}, success=False, reason="Bad call")
