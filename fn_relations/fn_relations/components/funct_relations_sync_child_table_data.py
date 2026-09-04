# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
# pragma pylint: disable=unused-argument, line-too-long
# Generated with resilient-sdk v49.1.51

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields
import re

PACKAGE_NAME = "fn_relations"
FN_NAME = "relations_sync_child_table_data"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'relations_sync_child_table_data'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Update data within the Parent Table if the Child data changes.
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


        self.LOG.info('Gathering Incident Data')
        child_incident = self.rest_client().get("/incidents/{}".format(relations_child_incident_id))
        self.LOG.info('Gathering the Child Incidents Data Table')
        child_table = self.rest_client().get("/incidents/{}/table_data/dt_relations_child_incidents?handle_format=names".format(relations_parent_incident_id))
        self.LOG.debug('Child Incidents Data Table: {}'.format(child_table))
        for row in child_table['rows']:
            childid_regex = re.compile(r'#incidents/(\d+)"')
            incident_id = int(re.findall(childid_regex,row['cells']['relations_incident_id']['value'])[0])
            self.LOG.debug('Incident ID Found: {}'.format(incident_id))
            if incident_id == relations_child_incident_id:
                self.LOG.info('Updating Child Row')
                row['cells']['relations_incident_name']['value'] = child_incident['name']
                row['cells']['relations_incident_status']['value'] = 'Active' if child_incident['plan_status'] == 'A' else 'Closed'
                row_id = row['id']
                updated_row = row
                self.LOG.debug('Updated Row: {}'.format(updated_row))
        self.LOG.info('Pushing Updated Row')
        posted_row = self.rest_client().put('/incidents/{}/table_data/dt_relations_child_incidents/row_data/{}?handle_format=names'.format(relations_parent_incident_id,row_id),updated_row)
        self.LOG.info('Row Updated -- Row ID: {0} | Incident ID: {1} | Incident Name: {2}'.format(posted_row['id'],child_incident['id'],posted_row['cells']['relations_incident_name']['value']))


        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        results = {"response": posted_row}

        yield FunctionResult(results)
        # yield FunctionResult({}, success=False, reason="Bad call")
