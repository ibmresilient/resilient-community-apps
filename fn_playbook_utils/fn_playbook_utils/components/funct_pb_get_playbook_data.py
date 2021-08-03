# -*- coding: utf-8 -*-
#(c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.
#pragma pylint: disable=unused-argument, no-self-use, line-too-long

"""AppFunction implementation"""
from cachetools import cached, TTLCache
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from fn_playbook_utils.lib.common import get_playbooks_by_incident_id, parse_inputs

PACKAGE_NAME = "fn_playbook_utils"
FN_NAME = "pb_get_playbook_data"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'pb_get_playbook_data'"""

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
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        min_id, max_id = parse_inputs(self.restclient, fn_inputs)

        yield self.status_message("Using min_incident: {} max_incident: {}".format(min_id, max_id))

        result_data = self.get_all_incident_playbooks(min_id, max_id)

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        yield FunctionResult(result_data)

    @cached(cache=TTLCache(maxsize=30, ttl=60))
    def get_all_incident_playbooks(self, min_id, max_id):
        # get all the incident data to return
        result_dict = {}
        result_data = {
            "org_id" : self.restclient.org_id,
            "min_id": min_id,
            "max_id": max_id,
            "playbook_content": result_dict
        }

        search_results = get_playbooks_by_incident_id(self.restclient, min_id, max_id)
        for pb in search_results['data']:
          if pb['incident_id'] in result_dict:
            result_dict[pb['incident_id']].append(pb)
          else:
            result_dict[pb['incident_id']] = [pb]

        return result_data
