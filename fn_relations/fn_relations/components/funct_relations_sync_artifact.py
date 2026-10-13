# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
# pragma pylint: disable=unused-argument, line-too-long
# Generated with resilient-sdk v48.1.4243

"""AppFunction implementation"""

import re
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import IntegrationError, validate_fields
from fn_relations.lib.utilities import list_children


PACKAGE_NAME = "fn_relations"
FN_NAME = "relations_sync_artifact"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'relations_sync_artifact'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Sync Artifacts from the incident where the artifact is currently to the parent or child.
        Inputs:
            -   fn_inputs.incident_id
            -   fn_inputs.artifact_id
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        validate_fields(["incident_id", "artifact_id"], fn_inputs)

        incident_id = fn_inputs.incident_id
        artifact_id = fn_inputs.artifact_id
        self.LOG.info("incident_id: {}".format(incident_id))
        self.LOG.info("artifact_id: {}".format(artifact_id))


        self.LOG.info('Gathering Artifact from Incident')
        artifact_data = self.rest_client().get('/incidents/{}/artifacts/{}?handle_format=names'.format(incident_id, artifact_id))
        self.LOG.debug('Artifact Gathered: {}'.format(artifact_data))
        artifact_variables = ['type', 'value', 'description']
        new_artifact = {}
        for item in artifact_variables:
            new_artifact[item] = artifact_data[item]
        if new_artifact['description']:
            new_artifact['description'] = 'Artifact Synced from incident {}. '.format(incident_id) + new_artifact['description']
        else:
            new_artifact['description'] = 'Artifact Synced from incident {}.'.format(incident_id)
        self.LOG.debug('New Artifact: {}'.format(new_artifact))
        incident = self.rest_client().get("/incidents/{}?handle_format=names".format(incident_id))

        if incident['properties']['relations_level'] == 'Child':
            self.LOG.info('Raising Child Artifact')
            id_regex = re.compile(r'#incidents/(\d+)"')
            sync_id = int(re.findall(id_regex,incident['properties']['relations_parent_id'])[0])
            self.LOG.info('Parent ID: {}'.format(sync_id))
            synced_artifact = self.rest_client().post('/incidents/{}/artifacts'.format(sync_id), new_artifact)
            self.LOG.info('Added Child Artifact -- Artifact ID: {0}'.format(synced_artifact[0]['id']))
            results = {'artifact': new_artifact, 'incidents': [sync_id]}
        elif incident['properties']['relations_level'] == 'Parent':
            self.LOG.info('Pushing Parent Artifact')
            children_incidents = list_children(self.rest_client().get("/incidents/{}/table_data/dt_relations_child_incidents?handle_format=names".format(incident_id)))
            for child in children_incidents:
                self.LOG.info('Syncing Artifact to Child ID: {}'.format(child))
                synced_artifact = self.rest_client().post('/incidents/{}/artifacts'.format(child), new_artifact)
                self.LOG.info('Added Parent Artifact -- Artifact ID: {0}'.format(synced_artifact[0]['id']))
            self.LOG.info("Artifacts Synced")
            results = {'artifact': new_artifact, 'incidents': children_incidents}
        else:
            raise IntegrationError("Incident does not have a relation level. Unable to sync note.")

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        yield FunctionResult(results)
        # yield FunctionResult({}, success=False, reason="Bad call")
