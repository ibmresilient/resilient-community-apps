# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

import logging
import re
import requests
from bs4 import BeautifulSoup as bsoup
from resilient_circuits import ResilientComponent, function, handler
from resilient_circuits import StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload, readable_datetime, validate_fields

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'res_to_icd_function"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_res_to_icd", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_res_to_icd", {})

    @function("res_to_icd_function")
    def _res_to_icd_function_function(self, event, *args, **kwargs):
        try:
            # taken from config section
            icd_email = self.options.get("icd_email")
            icd_pass = self.options.get("icd_pass")
            incident_id = kwargs.get("incident_id")
            icd_priority = self.options.get("icd_priority")
            icd_field_severity = self.options.get('icd_field_severity')
            icd_url = self.options.get('icd_url')
            # Payload and validation
            payload = ResultPayload('fn_res_to_icd', **kwargs)
            validate_fields(['icd_email','icd_pass','icd_field_severity','icd_priority'],kwargs)
            #logging
            log = logging.getLogger(__name__)
            log.info("icd_email: %s", icd_email)
            log.info("icd_password: %s", icd_pass)
            log.info("icd_field_severity: %s", icd_field_severity)
            log.info("icd_priority: %s", icd_priority)
            log.info("incident_id: %s", incident_id)
            log.info("icd_url: %s", icd_url)
            # Resilient client and api calls
            res_client = self.rest_client()
            incident_str = '/incidents/{incident_id}/'.format(incident_id=incident_id)
            artifact_str = '/incidents/{incident_id}/artifacts'.format(incident_id=incident_id)
            if icd_field_severity:
                fieldsev_str = '/types/{type}/fields/{field}'.format(type='incident', field=icd_field_severity)
                field_severity = res_client.get(fieldsev_str)
            content = res_client.get(incident_str)
            art_content = res_client.get(artifact_str)
            # Time and date
            timestamp = content['create_date']
            timeval = readable_datetime(timestamp, milliseconds=True, rtn_format='%Y-%m-%dT%H:%M:%SZ')
            time = "Date and Time: {0}".format(timeval)
            #artifact population to icd ticket
            details_payload = ''
            artifact_limit = len(art_content)-1
            i = 0
            if field_severity:
                try:
                    for i in range(0, min(artifact_limit, len(art_content))):
                        if art_content[i].get('properties', False):
                            if art_content[i]['properties'][0]['name'] in ('source', 'destination'):
                                details_payload += 'ID: {1} IP Address {2}: {0} \n'.format(art_content[i]['value'], art_content[i]['id'], art_content[i]['properties'][0]['name'].capitalize())
                                log.info(i)
                            else:
                                log.error("This artifact did not populate")
                except Exception as artifact_error:
                    log.info(artifact_error)
                    log.error("Encountered an error parsing artifacts")
            ## General field severity checking
            if field_severity:
                try:
                    field_sev = field_severity['values']
                except:
                    field_sev = field_severity['name']
                if not field_sev:
                    field_sev = 1  # number
                log.info("field_sev: %s", field_sev)
                icd_priority_lookup = [0, 4, 4, 4, 3, 2, 2, 1]
                try:
                    icd_priority = icd_priority_lookup[field_sev]
                except:
                    log.warning("You have not set a priority, icd priority will be set to min value (4)")
                    icd_priority = 4
            # Params and Desk call
            params = {"DESCRIPTION" : time,
            "DESCRIPTION_LONGDESCRIPTION" : details_payload,
            "REPORTEDBYID" : icd_email,
            "logtype" : "CLIENTNOTE",
            "worklog.1.description" : "SECURITY ISSUE",
            "worklog.1.DESCRIPTION_LONGDESCRIPTION" : "SECURITY ISSUE",
            "INTERNALPRIORITY" : icd_priority,
            "SITEID" : "APPOPINT", "CLASSIFICATIONID" : "SECURITY ISSUE",
            "_lid" : icd_email,
            "_lpwd" : icd_pass}
            endpoint = "/rest/os/MXINCIDENT/"
            base_url= icd_url + endpoint
            response = requests.post(url=base_url, params=params, verify=False)
            xmldata = bsoup(response.text,"html.parser")
            icd_id = '{0}'.format(xmldata.createmxincidentresponse.mxincidentset.incident.ticketid)
            icd_id = re.sub('[ticket<>/d]', '', icd_id)
            yield StatusMessage("Completed successfully")
            results = payload.done(success=True, content={
                "incident_escalated" : incident_id,
                "icd_id" : icd_id,
                "details" : details_payload
            })
            # Produce a FunctionResult with the results
            yield FunctionResult(results)
            log.info("Complete")
        except Exception:
            yield FunctionError()
