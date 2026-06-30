# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
# pragma pylint: disable=unused-argument, line-too-long
# Generated with resilient-sdk v49.1.51

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields
import re

PACKAGE_NAME = "fn_relations"
FN_NAME = "relations_remove_child_relation"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'relations_remove_child_relation'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Used to remove the relation child relation from a Child incident as well as removing the parent relation from the Parent incident if it no longer has children.
        Inputs:
            -   fn_inputs.relations_child_incident_id
            -   fn_inputs.relations_remove_notes
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")


        # Example validating required fn_inputs
        validate_fields(["relations_child_incident_id", "relations_remove_notes"], fn_inputs)

        relations_child_incident_id = fn_inputs.relations_child_incident_id
        relations_remove_notes = fn_inputs.relations_remove_notes
        self.LOG.info("relations_child_incident_id: {}".format(relations_child_incident_id))
        self.LOG.info("relations_remove_notes: {}".format(relations_remove_notes))

        def remove_child(incident):
            incident["properties"]["relations_level"] = "None"
            incident["properties"]["relations_parent_id"] = None
            return(incident)


        def remove_parent(incident):
            incident["properties"]["relations_level"] = "None"
            return(incident)


        def recursive_note_removal_lookup(removal_incident_id, note_list):
            for note in note_list:
                if note['text']:
                    if 'Incident: <a href="#incidents/{0}'.format(removal_incident_id) in note['text']:
                        new_note_list.append(note)
                if note['children']:
                    recursive_note_removal_lookup(removal_incident_id, note['children'])


        regex = re.compile(r'#incidents/(\d+)"')
        parent_id = int(re.findall(regex, self.rest_client().get("/incidents/{}".format(relations_child_incident_id))['properties']['relations_parent_id'])[0])
        self.LOG.info('Parent ID: {}'.format(parent_id))

        self.LOG.info('Removing Child Relation')
        removed_child_incident = self.rest_client().get_put("/incidents/{}".format(relations_child_incident_id),remove_child)
        self.LOG.info('Child Relation Removed')
        self.LOG.debug('Incident details after Child Relation Removal: {}'.format(removed_child_incident))

        self.LOG.info('Removing Child Artifact')
        child_artifacts = self.rest_client().get("/incidents/{}/artifacts?handle_format=names".format(relations_child_incident_id))
        self.LOG.debug('Child Incident Artifacts: {}'.format(child_artifacts))
        for artifact in child_artifacts:
            if artifact['type'] == "related_parent_incident":
                self.LOG.debug('Related Parent Incident: {}'.format(artifact))
                self.rest_client().delete("/incidents/{0}/artifacts/{1}".format(relations_child_incident_id,artifact['id']))
                self.LOG.info('Removed Child Incident Artifact -- Artifact Type: {0} | Artifact ID: {1} | Artifact Value: {2}'.format(artifact['type'],artifact['id'],artifact['value']))

        self.LOG.info('Removing Child from Data Table')
        child_table = self.rest_client().get("/incidents/{}/table_data/dt_relations_child_incidents?handle_format=names".format(parent_id))
        self.LOG.debug('Parent Table of Children: {}'.format(child_table))
        for row in child_table['rows']:
            child_id = int(re.findall(regex, row['cells']['relations_incident_id']['value'])[0])
            if child_id == relations_child_incident_id:
                self.rest_client().delete('/incidents/{0}/table_data/dt_relations_child_incidents/row_data/{1}'.format(parent_id, row['id']))
                self.LOG.info('Removed Row -- Row ID: {0} | Incident ID: {1} | Incident Name: {2}'.format(row['id'], child_id, row['cells']['relations_incident_name']['value']))

        updated_child_table = self.rest_client().get("/incidents/{}/table_data/dt_relations_child_incidents?handle_format=names".format(parent_id))
        self.LOG.debug('Parent Table of Children after Child Removal: {}'.format(updated_child_table))
        if len(updated_child_table['rows']) == 0:
            self.LOG.info('No Additional Children. Removing Parent Relation.')
            self.rest_client().get_put("/incidents/{}".format(parent_id),remove_parent)
            self.LOG.info('Parent Relation Removed')
            self.LOG.info('Removing Parent Artifact')
            parent_artifacts = self.rest_client().get("/incidents/{}/artifacts?handle_format=names".format(parent_id))
            self.LOG.debug('Parent Incident Artifacts: {}'.format(child_artifacts))
            for artifact in parent_artifacts:
                if artifact['type'] == "related_parent_incident":
                    self.LOG.debug('Related Parent Incident: {}'.format(artifact))
                    self.rest_client().delete("/incidents/{0}/artifacts/{1}".format(parent_id,artifact['id']))
                    self.LOG.info('Removed Parent Incident Artifact -- Artifact Type: {0} | Artifact ID: {1} | Artifact Value: {2}'.format(artifact['type'],artifact['id'],artifact['value']))

        if relations_remove_notes:
            self.LOG.info('Removing Child Notes')
            child_comments = self.rest_client().get('/incidents/{0}/comments'.format(relations_child_incident_id))
            new_note_list = []
            recursive_note_removal_lookup(parent_id, child_comments)
            for child_note in new_note_list[::-1]:
                self.LOG.debug('Note Synced to Child: {}'.format(child_note))
                self.rest_client().delete('/incidents/{0}/comments/{1}'.format(relations_child_incident_id, child_note['id']))
                self.LOG.info('Removed Parent Note -- Note ID: {0} | Note Text: {1}'.format(child_note['id'],child_note['text']))

            parent_comments = self.rest_client().get('/incidents/{0}/comments'.format(parent_id))
            new_note_list = []
            recursive_note_removal_lookup(relations_child_incident_id, parent_comments)
            for parent_note in new_note_list[::-1]:
                self.LOG.debug('Note Synced to Parent: {}'.format(parent_note))
                self.rest_client().delete('/incidents/{0}/comments/{1}'.format(parent_id, parent_note['id']))
                self.LOG.info('Removed Parent Note -- Note ID: {0} | Note Text: {1}'.format(parent_note['id'],parent_note['text']))


        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        results = {'parent_incident': parent_id, 'child_incident': child_id}

        yield FunctionResult(results)
        # yield FunctionResult({}, success=False, reason="Bad call")
