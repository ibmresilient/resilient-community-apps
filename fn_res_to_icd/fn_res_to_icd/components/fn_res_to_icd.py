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
from resilient_lib import ResultPayload
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
            
            incident_id=kwargs.get("incident_id")
            log = logging.getLogger(__name__)
            log.info("incident_id: %s", incident_id)

            # Resilient client and api calls
            res_client = self.rest_client()
            incident_str='/incidents/{incident_id}/'.format(incident_id=incident_id)
            artifact_str='/incidents/{incident_id}/artifacts'.format(incident_id=incident_id)
            content=res_client.get(incident_str)
            art_content=res_client.get(artifact_str)

            # Time and date
            utc_ts = content['create_date']
            tz_dt = tz_from_utc_ms_ts(utc_ts, pytz.timezone('Etc/GMT+6'))
            timeval=tz_dt.isoformat()
            time="Date and Time: {0}".format(timeval)

            #artifact population to icd ticket 
            icd_priority = 1
            details_payload=''
            artifact_limit=len(art_content)
            i = 0
            try:
                while i < artifact_limit:
                    if art_content[i]['properties'][0]['name'] in ('source' , 'destination'): 
                        details_payload +='ID: {1} IP Address {2}: {0} \n'.format(art_content[i]['value'],art_content[i]['id'],art_content[i]['properties'][0]['name'].capitalize())
                        i += 1
            except:
                log.error("Some artifacts may not have populated, please double check on icd desk")
            
            ## QRadar severity checking

            qradar_sev = content['properties']['qradar_severity']  # number
            log.info("qradar_sev: %s", qradar_sev)
            payload = ResultPayload('fn_res_to_icd', **kwargs)

            if qradar_sev >= 1 and qradar_sev <= 3:
                icd_priority = 4
            elif qradar_sev == 4:
                icd_priority = 3
            elif qradar_sev >= 5 and qradar_sev <=6:
                icd_priority = 2
            elif qradar_sev >=7:
                icd_priority = 1
            else:
                log.warning("You have not set a Qradar priority, icd priority will be min value (4)")
                icd_priority = 4
            
            # Params and Desk call
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
            response = requests.post("https://icdaas.sccd.ibmserviceengage.com/maximo_cbs-dev2/rest/os/MXINCIDENT/", params=params, verify=False)
        
            # xml conversion to dict and reading
            response_dict=xmltodict.parse(response.text)
            map_list= ["CreateMXINCIDENTResponse","MXINCIDENTSet","INCIDENT","TICKETID"]
            icd_id = getFromDict(response_dict,map_list)
            
            yield StatusMessage("Completed successfully")
            results = payload.done(success=True,content={
                "Incident escalated" : incident_id,
                "icd_id":icd_id,
                "Details":details_payload
            })
            
            # Produce a FunctionResult with the results
            yield FunctionResult(results)
            log.debug("RESULTS: %s", results)
            log.info("Complete")
        except Exception:
            yield FunctionError()