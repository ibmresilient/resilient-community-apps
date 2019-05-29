# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import collections
import requests,json
import pprint
import xmltodict
import datetime as dt
import pytz
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
import resilient_lib 
from functools import reduce  # forward compatibility for Python 3
import operator

def getFromDict(dataDict, mapList):
    return reduce(operator.getitem, mapList, dataDict)

def tz_from_utc_ms_ts(utc_ms_ts, tz_info):
    """Given millisecond utc timestamp and a timezone return dateime

    :param utc_ms_ts: Unix UTC timestamp in milliseconds
    :param tz_info: timezone info
    :return: timezone aware datetime
    """
    # convert from time stamp to datetime
    utc_datetime = dt.datetime.utcfromtimestamp(utc_ms_ts / 1000.)

    # set the timezone to UTC, and then convert to desired timezone
    return utc_datetime.replace(tzinfo=pytz.timezone('UTC')).astimezone(tz_info)


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
            utc_ts = content['create_date']
            tz_dt = tz_from_utc_ms_ts(utc_ts, pytz.timezone('Etc/GMT+6'))
            timeval=tz_dt.isoformat()
            time="Date and Time: {1}".format(timeval)

            #for i in art_content:
            #    pprint.pprint(type(i))
            details_payload=''
            artifact_limit=1
            i = 0
            try:
                artifact_limit=int(input("How many artifacts do you wish to populate?"))
                while i < artifact_limit:
                    if art_content[i]['properties'][0]['name'] in ('source' , 'destination'): 
                        details_payload +='ID: {1} IP Address {2}: {0} \n'.format(art_content[i]['value'],art_content[i]['id'],art_content[i]['properties'][0]['name'].capitalize())
                        i += 1
            except:
                log.error("Some artifacts may not have populated due to incorrect usage")
            
            
            yield StatusMessage("starting...")
            #pprint.pprint(art_content)
            
            #pprint.pprint(content)
            qradar_sev = content['properties']['qradar_severity']  # number
            #qradar_sev=6
            
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
            params =  { "DESCRIPTION": time ,
             "DESCRIPTION_LONGDESCRIPTION": details_payload ,
             "REPORTEDBYID": "resilient_test@in.ibm.com" ,
             "logtype": "CLIENTNOTE" ,
             "worklog.1.description": "SECURITY ISSUE" ,
             "worklog.1.DESCRIPTION_LONGDESCRIPTION": "SECURITY ISSUE" ,
             "INTERNALPRIORITY": icd_priority ,
             "SITEID":"APPOPINT" ,
             "CLASSIFICATIONID": "SECURITY ISSUE" ,
             "_lid": "resilient_test@in.ibm.com" ,
             "_lpwd": "Welcome@1234"  } 
            #["CreateMXINCIDENTResponse"]["@xmlns"]["MXINCIDENTSet'"]["INCIDENT"]["@rowstamp"]["WORKLOG"]["@rowstamp"]["RECORDKEY"]
            response = requests.post("https://icdaas.sccd.ibmserviceengage.com/maximo_cbs-dev2/rest/os/MXINCIDENT/", params=params, verify=False)
            #pprint.pprint(response.status_code)
            #pprint.pprint(response.text)
        
            response_dict=xmltodict.parse(response.text)
            #response_dict=dict(response_obj)
            
            #icd_id = 2
            map_list= ["CreateMXINCIDENTResponse","MXINCIDENTSet","INCIDENT","TICKETID"]
            icd_id = getFromDict(response_dict,map_list)
            
            yield StatusMessage("Completed successfully")
            results = {
                "Incident escalated" : incident_id,
                "icd_id":icd_id,
                "Details":details_payload
            }
            
            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()