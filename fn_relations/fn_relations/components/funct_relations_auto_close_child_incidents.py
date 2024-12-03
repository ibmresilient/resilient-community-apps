# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
# pragma pylint: disable=unused-argument, line-too-long
# Generated with resilient-sdk v49.1.51

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields
from fn_relations.lib.utilities import list_open_children


PACKAGE_NAME = "fn_relations"
FN_NAME = "relations_auto_close_child_incidents"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'relations_auto_close_child_incidents'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Close child incidents when the parent incident is closed.
        Inputs:
            -   fn_inputs.relations_parent_incident_id
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        # Example validating required fn_inputs
        validate_fields(["relations_parent_incident_id"], fn_inputs)

        relations_parent_incident_id = fn_inputs.relations_parent_incident_id
        self.LOG.info("relations_parent_incident_id: {}".format(relations_parent_incident_id))

        def close_child(incident):
            parent_incident = self.rest_client().get("/incidents/{}".format(relations_parent_incident_id))
            self.LOG.info('Updating Required on Close Fields')
            for req_field in req_fields:
                if req_field.get(None):
                    if list(req_field.values())[0] == 'resolution_summary':
                        incident[list(req_field.values())[0]] = "Per Resolution Summary of the Parent:<br><br>" + parent_incident[list(req_field.values())[0]]
                    else:
                        incident[list(req_field.values())[0]] = parent_incident[list(req_field.values())[0]]
                else:
                    incident[list(req_field.keys())[0]][list(req_field.values())[0]] = parent_incident[list(req_field.keys())[0]][list(req_field.values())[0]]
            incident["plan_status"] = 'C'
            incident["end_date"] = parent_incident['end_date']
            return(incident)


        self.LOG.info('Gathering Child Incident List')
        incidents = list_open_children(self.rest_client().get("/incidents/{}/table_data/dt_relations_child_incidents?handle_format=names".format(relations_parent_incident_id)))

        fields = self.rest_client().get("/types/incident/fields")
        self.LOG.info('Creating List of Fields Required on close')
        req_fields = []
        for field in fields:
            if field.get('required') == 'close':
                req_fields.append({field['prefix']: field['name']})
        self.LOG.debug('Fields required on Close: {}'.format(req_fields))

        for incident in incidents:
            self.LOG.info('Closing Incident: {}'.format(incident))
            self.rest_client().get_put("/incidents/{}".format(incident),close_child)


        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        results = {"incidents": incidents}

        yield FunctionResult(results)
        # yield FunctionResult({}, success=False, reason="Bad call")
