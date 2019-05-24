#-*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import requests, pprint
import json
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_res_to_icd"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_res_to_icd", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_res_to_icd", {})

    @function("fn_res_to_icd")
    def _fn_res_to_icd_function(self, event, *args, **kwargs):
        """Function: This function transfers an qradar severity to a priority on the icd ticket"""
        try:
            # Get the wf_instance_id of the workflow this Function was called in
            wf_instance_id = event.message["workflow_instance"]["workflow_instance_id"]
            res_client = self.rest_client()
         
            content=res_client.get('/incidents/2101/')
            
            pprint.pprint(content)
            qradar_sev = content['properties']['qradar_severity']  # number
            #qradar_sev=6
            yield StatusMessage("starting...")
            icd_priority = 1

            if qradar_sev >= 1 and qradar_sev <= 3:
                icd_priority = 4
            elif qradar_sev == 4:
                icd_priority = 3
            elif qradar_sev >= 5 and qradar_sev <=6:
                icd_priority = 2
            elif qradar_sev >=7:
                icd_priority = 1
            else:
                log.warning("You have not set a Qradar priority, icd will be 4")
                icd_priority = 4


            log = logging.getLogger(__name__)
            log.info("qradar_sev: %s", qradar_sev)
            params = dict([ ("DESCRIPTION", "My name is SEAN"),
            ("DESCRIPTION_LONGDESCRIPTION", "We can now put in descriptions"),
            ("REPORTEDBYID", "resilient_test@in.ibm.com"),
            ("logtype", "CLIENTNOTE"),
            ("worklog.1.description", "Test Incident"),
            ("worklog.1.DESCRIPTION_LONGDESCRIPTION", "Ticket made is from test Environment.Please close the incident."),
            ("INTERNALPRIORITY", str(icd_priority)),
            ("SITEID","APPOPINT"),
            ("CLASSIFICATIONID", "SECURITY ISSUE"),
            ("_lid", "resilient_test@in.ibm.com"),
            ("_lpwd", "Welcome@1234") ])

            response = requests.post("https://icdaas.sccd.ibmserviceengage.com/maximo_cbs-dev2/rest/os/MXINCIDENT/", params=params, verify=False)


            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE
            #  yield StatusMessage("starting...")
            yield StatusMessage("done...")

            results = {
                "value": "xyz"
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
