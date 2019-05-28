# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import collections
import requests,json
import pprint
import xmltodict
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from functools import reduce  # forward compatibility for Python 3
import operator

def getFromDict(dataDict, mapList):
    return reduce(operator.getitem, mapList, dataDict)


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
            # Get the function parameters
            incident_id=kwargs.get("incident_id")
            log = logging.getLogger(__name__)
            log.info("incident_id: %s", incident_id)

            res_client = self.rest_client()
            incident_str='/incidents/{incident_id}/'.format(incident_id=incident_id)
            artifact_str='/incidents/{incident_id}/artifacts'.format(incident_id=incident_id)
         
            content=res_client.get(incident_str)
            art_content=res_client.get(artifact_str)
            pprint.pprint(art_content)
            #pprint.pprint(content)
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

            log.info("qradar_sev: %s", qradar_sev)
            params = dict([ ("DESCRIPTION", "My name is SEAN"),
            ("DESCRIPTION_LONGDESCRIPTION", art_content[1]),
            ("REPORTEDBYID", "resilient_test@in.ibm.com"),
            ("logtype", "CLIENTNOTE"),
            ("worklog.1.description", "Test Incident"),
            ("worklog.1.DESCRIPTION_LONGDESCRIPTION", "Ticket made is from test Environment.Please close the incident."),
            ("INTERNALPRIORITY", icd_priority),
            ("SITEID","APPOPINT"),
            ("CLASSIFICATIONID", "SECURITY ISSUE"),
            ("_lid", "resilient_test@in.ibm.com"),
            ("_lpwd", "Welcome@1234") ])
            #["CreateMXINCIDENTResponse"]["@xmlns"]["MXINCIDENTSet'"]["INCIDENT"]["@rowstamp"]["WORKLOG"]["@rowstamp"]["RECORDKEY"]
            response = requests.post("https://icdaas.sccd.ibmserviceengage.com/maximo_cbs-dev2/rest/os/MXINCIDENT/", params=params, verify=False)
            pprint.pprint(response.status_code)
            #pprint.pprint(response.text)
            response_dict=xmltodict.parse(response.text)
            
            map_list= ["CreateMXINCIDENTResponse","MXINCIDENTSet","INCIDENT","TICKETID"]
            icd_id = getFromDict(response_dict,map_list)
            pprint.pprint(icd_id)
            

            results = {
                "Incident escalated" : incident_id,
                "icd_id":icd_id
            }
            
            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()