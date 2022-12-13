# -*- coding: utf-8 -*-
#(c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.
#pragma pylint: disable=unused-argument, no-self-use, line-too-long

"""AppFunction implementation"""
from cachetools import cached, TTLCache
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from fn_playbook_utils.lib.common import parse_inputs

PACKAGE_NAME = "fn_playbook_utils"
FN_NAME = "pb_get_workflow_data"

WORKFLOW_INSTANCES_URL = "/incidents/{}/workflow_instances"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'pb_get_workflow_data'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)
        self.restclient = self.rest_client()

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Get information on workflows run for this incident or for a range of incidents
        Inputs:
            -   fn_inputs.pb_min_incident_id
            -   fn_inputs.pb_max_incident_id
            -   fn_inputs.pb_min_incident_date
            -   fn_inputs.pb_max_incident_date
            -   fn_inputs.pb_object_name
            -   fn_inputs.pb_object_type
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        min_id, max_id = parse_inputs(self.restclient, fn_inputs)

        yield self.status_message("Using min_incident: {} max_incident: {}".format(min_id, max_id))
        result_data = self.get_all_incident_workflows(min_id, max_id)

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        yield FunctionResult(result_data)

    @cached(cache=TTLCache(maxsize=10000, ttl=60))
    def get_incident_workflow(self, incident_id):
        url = WORKFLOW_INSTANCES_URL.format(incident_id)
        return self.restclient.get(uri=url)

    @cached(cache=TTLCache(maxsize=30, ttl=60))
    def get_all_incident_workflows(self, min_id, max_id):
        # get all the incident data to return
        result_dict = {}
        result_data = {
            "org_id" : self.restclient.org_id,
            "min_id": min_id,
            "max_id": max_id,
            "workflow_content": result_dict
        }
        # don't continue if no values
        if bool(min_id and max_id):
            for inc_id in range(min_id, max_id+1):
                try:
                    inc_workflows = self.get_incident_workflow(inc_id)
                    result_dict[inc_id] = inc_workflows
                except BaseException:
                    pass

        return result_data
