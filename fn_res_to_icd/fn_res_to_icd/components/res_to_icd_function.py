
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

from functools import reduce  # forward compatibility for Python 3
import operator
import datetime as dt
import logging
import requests
import pytz
import xmltodict
from resilient_circuits import ResilientComponent, function, handler 
from resilient_circuits import StatusMessage, FunctionResult, FunctionError
import resilient_lib
from resilient_lib import ResultPayload

def get_from_dict(data_Dict, map_List):
    return reduce(operator.getitem, map_List, data_Dict)

def tz_from_utc_ms_ts(utc_ms_ts, tz_info):
    """Given millisecond utc timestamp and a timezone return datetimes
    :param utc_ms_ts: Unix UTC timestamp in milliseconds
    :param tz_info: timezone info
    :return: timezone aware datetime
    """
    # convert from time stamp to datetime
    utc_datetime = dt.datetime.utcfromtimestamp(utc_ms_ts / 1000.)
    # set the timezone to UTC, and then convert to desired timezone
    return utc_datetime.replace(tzinfo=pytz.timezone('UTC')).astimezone(tz_info)

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
        """Function: This function transfers a resilient with a qradar severity (1-10)
        to an icd ticket with a priority (4-1)"""
        try:
            # taken from config section
            icd_email = self.options.get("icd_email")
            icd_pass = self.options.get("icd_pass")
            incident_id = kwargs.get("incident_id")
            icd_priority = self.options.get("icd_priority")
            icd_qradar_severity = resilient_lib.str_to_bool(self.options.get('icd_qradar_severity'))
            #logging
            log = logging.getLogger(__name__)
            log.info("icd_email: %s", icd_email)
            log.info("icd_password: %s", icd_pass)
            log.info("icd_qradar_severity: %s", icd_qradar_severity)
            log.info("icd_priority: %s", icd_priority)
            log.info("incident_id: %s", incident_id)
            # Resilient client and api calls
            res_client = self.rest_client()
            incident_str = '/incidents/{incident_id}/'.format(incident_id=incident_id)
            artifact_str = '/incidents/{incident_id}/artifacts'.format(incident_id=incident_id)
            content = res_client.get(incident_str)
            art_content = res_client.get(artifact_str)
            # Time and date
            utc_ts = content['create_date']
            tz_dt = tz_from_utc_ms_ts(utc_ts, pytz.timezone('Etc/GMT+6'))
            timeval = tz_dt.isoformat()
            time = "Date and Time: {0}".format(timeval)
            #artifact population to icd ticket 
            details_payload = ''
            artifact_limit = len(art_content)-1
            i = 0
            try:
                while i <= artifact_limit:
                    if art_content[i].get('properties', False):
                        if art_content[i]['properties'][0]['name'] in ('source', 'destination'): 
                            details_payload += 'ID: {1} IP Address {2}: {0} \n'.format(art_content[i]['value'], art_content[i]['id'], art_content[i]['properties'][0]['name'].capitalize())
                            log.info(i)
                        else:
                            log.error("This artifact did not populate")
                    i += 1
            except Exception as artifact_error:
                log.info(artifact_error)
                log.error("Encountered an error parsing artifacts")
            ## QRadar severity checking
            if icd_qradar_severity:
                qradar_sev = content['properties']['qradar_severity']
                if not qradar_sev:
                    qradar_sev = 1  # number
                log.info("qradar_sev: %s", qradar_sev)
                if qradar_sev >= 1 and qradar_sev <= 3:
                    icd_priority = 4
                elif qradar_sev == 4:
                    icd_priority = 3
                elif qradar_sev >= 5 and qradar_sev <= 6:
                    icd_priority = 2
                elif qradar_sev >= 7:
                    icd_priority = 1
                else:
                    log.warning("You have not set a Qradar priority, icd priority will be min value (4)")
                    icd_priority = 4
            #take parameters into payload        
            payload = ResultPayload('fn_res_to_icd', **kwargs)
            # Params and Desk call
            params = {"DESCRIPTION" : time, "DESCRIPTION_LONGDESCRIPTION" : details_payload,
            "REPORTEDBYID" : "resilient_test@in.ibm.com", "logtype" : "CLIENTNOTE",
            "worklog.1.description" : "SECURITY ISSUE", "worklog.1.DESCRIPTION_LONGDESCRIPTION" : "SECURITY ISSUE",
            "INTERNALPRIORITY" : icd_priority, "SITEID" : "APPOPINT", "CLASSIFICATIONID" : "SECURITY ISSUE",
            "_lid" : icd_email, "_lpwd" : icd_pass} 
            response = requests.post("https://icdaas.sccd.ibmserviceengage.com/maximo_cbs-dev2/rest/os/MXINCIDENT/", params=params, verify=False)
            # xml conversion to dict and reading
            response_dict = xmltodict.parse(response.text)
            map_list = ["CreateMXINCIDENTResponse", "MXINCIDENTSet", "INCIDENT", "TICKETID"]
            icd_id = get_from_dict(response_dict, map_list)
            yield StatusMessage("Completed successfully")
            results = payload.done(success=True,content={
                "Incident escalated" : incident_id,
                "icd_id" : icd_id,
                "Details" : details_payload
            })
            # Produce a FunctionResult with the results
            yield FunctionResult(results)
            log.debug("RESULTS: %s", results)
            log.info("Complete")
        except Exception:
            yield FunctionError()
