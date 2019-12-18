# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
""" Incident poller for a ProofPoint TRAP server """

import logging
import time
import pprint
import re
from threading import Thread
from resilient_circuits import ResilientComponent, handler
from resilient import SimpleHTTPException
from resilient_lib.components.integration_errors import IntegrationError
from fn_proofpoint_trap.lib.helpers import validate_opts
from fn_proofpoint_trap.lib.pptr_client import PPTRClient

"""
Summary: 

    Threaded Poller to pull in Proofpoint TRAP Trap Incidents and Events    
    
    Naming:
    
        Resilient Incidents will be named in the following format:
        
        Proofpoint TRAP TRAP: {} - {}
            Incident Number
            Incident Description
            
        Data Table:
            Proofpoint TRAP TRAP Events
            
            API Name: proofpoint_trap_events
            
            Example Data for Table:
            
            {'attackDirection': 'inbound',
              'category': 'phish',
              'description': 'Redirected to known phishing site',
              'id': 18,
              'received': '2019-03-25T15:39:14Z',
              'severity': 'Info',
              'source': 'Proofpoint TRAP TAP',
              'state': 'Linked',
              'threatname': 'Redirected to known phishing site'}
              
        Additional Data for Incident:
        
            'incident_field_values': [{'name': 'Severity', 'value': 'Informational'},
                            {'name': 'Classification', 'value': 'Phishing'},
                            {'name': 'Attack Vector', 'value': 'Email'},
                            {'name': 'Abuse Disposition', 'value': None}],

        Message Destination:
            fn_proofpoint_trap
            
        Initial Functions:
            fn_proofpoint_trap_get_incident_details
                
                Input Fields:
                
                    trap_incident_id
                    
        Initial Codegen Performed:
            
             codegen -m fn_proofpoint_trap -f fn_proofpoint_trap_get_incident_details  
             --datatable proofpoint_trap_events -p fn_proofpoint_trap
                
                            
        Full Example Payload:
        
  {'assignee': 'Unassigned',
  'created_at': '2019-03-25T15:30:13Z',
  'description': '',
  'event_count': 14,
  'event_sources': ['Proofpoint TRAP TAP'],
  'events': [{'attackDirection': 'inbound',
              'category': 'phish',
              'id': 19,
              'received': '2019-03-26T18:44:49Z',
              'severity': 'Info',
              'source': 'Proofpoint TRAP TAP',
              'state': 'Linked'},
             {'attackDirection': 'inbound',
              'category': 'phish',
              'id': 22,
              'received': '2019-03-26T18:55:49Z',
              'severity': 'Info',
              'source': 'Proofpoint TRAP TAP',
              'state': 'Linked'},
             {'attackDirection': 'inbound',
              'category': 'phish',
              'description': 'Redirected to known phishing site',
              'id': 18,
              'received': '2019-03-25T15:39:14Z',
              'severity': 'Info',
              'source': 'Proofpoint TRAP TAP',
              'state': 'Linked',
              'threatname': 'Redirected to known phishing site'},
             {'attackDirection': 'inbound',
              'category': 'phish',
              'description': 'Redirected to known phishing site',
              'id': 20,
              'received': '2019-03-26T18:44:49Z',
              'severity': 'Info',
              'source': 'Proofpoint TRAP TAP',
              'state': 'Linked',
              'threatname': 'Redirected to known phishing site'},
             {'attackDirection': 'inbound',
              'category': 'phish',
              'description': 'Malicious content dropped during execution',
              'id': 23,
              'received': '2019-03-26T18:55:50Z',
              'severity': 'Info',
              'source': 'Proofpoint TRAP TAP',
              'state': 'Linked',
              'threatname': 'Malicious content dropped during execution'},
             {'attackDirection': 'inbound',
              'category': 'phish',
              'id': 17,
              'received': '2019-03-25T15:39:13Z',
              'severity': 'Info',
              'source': 'Proofpoint TRAP TAP',
              'state': 'Linked'},
             {'attackDirection': 'inbound',
              'category': 'phish',
              'id': 14,
              'received': '2019-03-25T15:34:13Z',
              'severity': 'Info',
              'source': 'Proofpoint TRAP TAP',
              'state': 'Linked'},
             {'attackDirection': 'inbound',
              'category': 'phish',
              'id': 13,
              'received': '2019-03-25T15:30:13Z',
              'severity': 'Info',
              'source': 'Proofpoint TRAP TAP',
              'state': 'Linked'},
             {'attackDirection': 'inbound',
              'category': 'phish',
              'description': 'Malicious content dropped during execution',
              'id': 15,
              'received': '2019-03-25T15:34:13Z',
              'severity': 'Info',
              'source': 'Proofpoint TRAP TAP',
              'state': 'Linked',
              'threatname': 'Malicious content dropped during execution'},
             {'attackDirection': 'inbound',
              'category': 'phish',
              'description': 'Redirected to known phishing site',
              'id': 21,
              'received': '2019-03-26T18:55:49Z',
              'severity': 'Info',
              'source': 'Proofpoint TRAP TAP',
              'state': 'Linked',
              'threatname': 'Redirected to known phishing site'},
             {'attackDirection': 'inbound',
              'category': 'phish',
              'description': 'Malicious content dropped during execution',
              'id': 25,
              'received': '2019-03-26T18:56:50Z',
              'severity': 'Info',
              'source': 'Proofpoint TRAP TAP',
              'state': 'Linked',
              'threatname': 'Malicious content dropped during execution'},
             {'attackDirection': 'inbound',
              'category': 'phish',
              'description': 'Malicious content dropped during execution',
              'id': 16,
              'received': '2019-03-25T15:39:13Z',
              'severity': 'Info',
              'source': 'Proofpoint TRAP TAP',
              'state': 'Linked',
              'threatname': 'Malicious content dropped during execution'},
             {'attackDirection': 'inbound',
              'category': 'phish',
              'description': 'Redirected to known phishing site',
              'id': 26,
              'received': '2019-03-26T18:56:49Z',
              'severity': 'Info',
              'source': 'Proofpoint TRAP TAP',
              'state': 'Linked',
              'threatname': 'Redirected to known phishing site'},
             {'attackDirection': 'inbound',
              'category': 'phish',
              'id': 24,
              'received': '2019-03-26T18:56:49Z',
              'severity': 'Info',
              'source': 'Proofpoint TRAP TAP',
              'state': 'Linked'}],
  'failed_quarantines': 0,
  'hosts': {'attacker': ['209.85.221.72',
                         'http://calina.info/payporte.php/',
                         '209.85.128.69',
                         'http://www.willype.info/house.php/'],
            'cnc': ['198.54.115.196',
                    '198.54.116.68',
                    '23.209.85.93',
                    '184.26.82.115',
                    '148.66.157.158',
                    '23.207.23.219',
                    '205.185.216.10',
                    '104.117.17.80',
                    '148.72.217.175',
                    '8.252.53.126'],
            'forensics': ['www.willype.info',
                          'calina.info',
                          'http://calina.info/payporte.php/',
                          'http://www.willype.info/house.php/?email=redacted_email',
                          'http://calina.info/payporte.php/?email=redacted_email',
                          'http://www.willype.info/house.php/']},
  'id': 7,
  'incident_field_values': [{'name': 'Severity', 'value': 'Informational'},
                            {'name': 'Classification', 'value': 'Phishing'},
                            {'name': 'Attack Vector', 'value': 'Email'},
                            {'name': 'Abuse Disposition', 'value': None}],
  'pending_quarantines': 0,
  'quarantine_results': [],
  'score': 1400,
  'state': 'New',
  'successful_quarantines': 0,
  'summary': 'Malicious content dropped during execution',
  'team': 'Unassigned',
  'updated_at': '2019-03-26T18:56:50Z',
  'users': []}
"""

# Map of Proofpoint TRAP event field to data table column
PROOFPOINT_TRAP_EVENTS_MAP = {
    'id': 'event_id',
    'description': 'event_description',
    'category': 'event_category',
    'attackDirection': 'event_attackdirection',
    'severity': 'event_severity',
    'source': 'event_source',
    'threatname': 'event_threatname',
    'state': 'event_state',
    'received': 'event_received',
}

# API Name(s) of Data Table(s)
DATA_TABLE_IDS = [
    'proofpoint_trap_events',
]

# Incident Fields returned from TRAP inside the
# incident_field_values list
#   List of Dictionaries
#   Format Example for list items:
#   {'name': 'Classification', 'value': 'Phishing' }
INCIDENT_FIELD_NAMES = [
    'Severity',
    'Classification',
    'Attack Vector',
    'Abuse Disposition',
]

# Relevant TIMESTAMPS from TRAP
TIMESTAMPS = [
    'created_at',
    'updated_at',
]

# Incident Types
# API Field is incident_type_ids @ Resilient (int)
# API Field is incident_field_values where name: Classification (dict)
CLASS2TYPEID = {
    'MALWARE' : 19,
    'Malware': 19,
    'Phishing': 22,
    'phish': 22,
    'Denial of Service': 21,
    'Other': 18,
    'Communication Error': 17,
    'System Intrusion': 20,

}

""" "incident_type_ids": [
    {
      "name": "System Intrusion",
      "id": 20
    },
    {
      "name": "Lost documents / files / records",
      "id": 4
    },
    {
      "name": "Lost PC / laptop / tablet",
      "id": 3
    },
    {
      "name": "Denial of Service",
      "id": 21
    },
    {
      "name": "Communication error (fax; email)",
      "id": 17
    },
    {
      "name": "Improper disposal: digital asset(s)",
      "id": 6
    },
    {
      "name": "Lost PDA / smartphone",
      "id": 1
    },
    {
      "name": "Improper disposal: documents / files",
      "id": 7
    },
    {
      "name": "Malware",
      "id": 19
    },
    {
      "name": "Lost storage device / media",
      "id": 8
    }
  ]
"""


# Nist Attack Vectors
# API Field is nist_attack_vectors @ Resilient
# API Field is incident_field_values where name: Attack Vectors @ TRAP
NIST_VECTORS = {
    'Email': 4,
    'Impersonation': 5,
    'Attrition': 2,
    'External Media': 1,
    'Improper Usage': 6,
    'Loss or Theft of Equipment': 7,
    'Web': 3,
    'Other': 8,
}

"""
 "nist_attack_vectors": [
    {
      "name": "External/Removable Media",
      "id": 1
    },
    {
      "name": "Loss or Theft of Equipment",
      "id": 7
    },
    {
      "name": "Attrition (Denial-of-Service and Brute-Force Attacks)",
      "id": 2
    },
    {
      "name": "Other",
      "id": 8
    },
    {
      "name": "Improper Usage",
      "id": 6
    },
    {
      "name": "Web",
      "id": 3
    },
    {
      "name": "E-mail",
      "id": 4
    },
    {
      "name": "Impersonation",
      "id": 5
    }
  ]
"""

# Abuse Disposition Fields
# API Field is confirmed @ Resilient
# API Field is incident_field_values where name: Abuse Disposition @ TRAP
ABUSE_DISPOSITION = {
    None: False,
    'None': False,
    'Confirmed': True
}

# API Field is severity_code @ Resilient
# API Field is  incident_field_values where name: Severity @ TRAP
INCIDENT_SEVERITY = {
    # Resilient has no informational so temporarily filter down to Low
    'Informational': 100,
    'Low': 100,
    'Medium': 101,
    'High': 102

}

# Custom Incident Fields
CUSTOM_FIELDS = [
    # TRAP Incidents id field to be posted to Resilient Incidents
    'proofpoint_trap_incident_id',
]

## Regular Expression Definitions for Artifact Extraction
REGEX_DEFS = {
    'URL': r'^((?:http(?:s)?\://)[a-zA-Z0-9\.\?\#\&\=\/_-]{1,})$',
    'IP Address':  r'^((?:[0-9]{1,3}\.){3}(?:[0-9]{1,3}))$',
    'DNS Name': r'^((?!(?:http(s)?:\/\/?))(?:(?:[\w-]{1,}[\.])){1,}([a-zA-Z]{2,}))$',
}

LOG = logging.getLogger(__name__)

class PPTRIncidentPolling(ResilientComponent):
    """Component that polls for new data arriving from Proofpoint TRAP"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(PPTRIncidentPolling, self).__init__(opts)
        self.options = opts.get("fn_proofpoint_trap", {})
        validate_opts(self)
        self.stop_thread = False
        self.threads = []
        self.main()

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_proofpoint_trap", {})
        validate_opts(self)
        self.stop_thread = True
        self.main()

    def main(self):
        """main entry point, instiantiate polling thread"""
        # initialize last update to startup interval if present, otherwise update interval
        options = self.options
        startup_interval = options.get('startup_interval', None)
        if startup_interval is not None:
            startup_interval = int(startup_interval)
        self.lastupdate = startup_interval
        polling_interval = int(options.get("polling_interval", 0))
        # Use a timeout value of polling_interval (in secs) + 10 secs to wait for all threads to end.
        thread_timeout = (polling_interval * 60) + 10

        # Wait for threads to stop within thread timeout interval.
        stop_time = time.time() + thread_timeout
        while any(t.isAlive for t in self.threads) and (time.time() < stop_time):
            time.sleep(0.1)

        # Get rid of stopped threads from list.
        self.threads = [t for t in self.threads if t.is_alive()]

        if self.threads:
            # Polling threads still running raise runtime error.
            LOG.error("There were %d polling threads which did not stop within timeout period on restart",
                      len(self.threads))
            raise RuntimeError("There were {} polling threads which did not stop within timeout period on restart."
                               .format(len(self.threads)))

        # Turn off 'stop_thread' flag.
        self.stop_thread = False

        if polling_interval > 0:
            # Create and start polling thread
            thread = Thread(target=self.polling_thread)
            self.threads.append(thread)
            thread.daemon = True
            thread.start()
            LOG.info("Polling for incidents in Proofpoint TRAP every %d minutes", polling_interval)
        else:
            LOG.info("Polling for incidents in Proofpoint TRAP not enabled")

    def polling_thread(self):
        """contents of polling thread, alternately check for new data and wait"""
        pptr = PPTRClient(self.opts, self.options)

        while not self.stop_thread:

            incident_list = pptr.get_incidents(self.lastupdate)

            if 'error' in incident_list:
                LOG.warning(incident_list.get('error'))
                raise IntegrationError(incident_list.get('error'))

            try:
                ### BEGIN Processing incidents
                for incident in incident_list:
                    LOG.info("Proofpoint TRAP Incident ID %d discovered: %s", incident['id'], incident['summary'])
                    if len(self._find_resilient_incident_for_req(incident['id'], CUSTOM_FIELDS[0])) == 0:
                        # Assemble Data table for incident
                        i_table = self.make_data_table(incident['events'])

                        # Get Extra Incident Fields
                        i_fields = self.make_incident_fields(incident)

                        # Build out artifacts for incident
                        i_artifacts = self.make_incident_artifacts(incident)

                        # Create incident and return response
                        i_response = self.create_incident(i_fields, i_table)

                        # Add Artifacts
                        self.create_incident_artifact(i_response['id'], i_artifacts)

                        # Add raw event payload as note
                        i_comment = self.create_incident_comment(i_response['id'], incident)
                    else:
                        LOG.info("Incident already exists for TRAP Incident %d", incident['id'])
                        # TODO: Add checks for Artifacts and Data Table rows
                    # TODO: Check update_at against datetime.now and if the delta is greater than polling interval,
                    #       ensure that table data is up to date

            except TypeError as ex:
                LOG.error(ex)

            # Break out of loop before sleep if restart initiated.
            if self.stop_thread:
                break

            # Amount of time (seconds) to wait to check cases again, defaults to 10 mins if not set
            time.sleep(int(self.options.get("polling_interval", 10)) * 60)

    def make_data_table(self, events):
        """
        Assemble the Data Table for an incident from Events inside the TRAP incident payload

        :param events: Events passed from an Incident passed from poller
        :return  Returns assembled LIST of DICTs with proper Data Table column names and values

        Example Format of POST data:

        {
            "cells" : {
                "threat_id" :  {
                    "value": "abc123"
                }, "threat_status": {
                    "value": "Status Test"
                }

            }
        }


        """
        data_table = []
        for event in events:
            table_row = {}
            for key, val in PROOFPOINT_TRAP_EVENTS_MAP.items():
                if key in event.keys():
                    table_row[val] = {"value" : event[key]}
            data_table.append({"cells" : table_row})
            LOG.debug("Table Row created with values: %s", table_row)
        LOG.info("Data Table Assembled with %d rows", len(data_table))

        # TODO: POST Data Table to Resilient Incident
        LOG.debug(pprint.pformat(data_table, indent=4))
        return {'proofpoint_trap_events' : data_table}

    def make_incident_name(self, incident):
        """
        Placeholder Method to create Resilient Incident name
        Broken out to make extensible later

        :param incident: Incident Payload from Poller
        :return iname: String for Incident Name to be used in Search / Incident Creation
        """
        # Fill event summary when blank
        i_summary = incident['summary']
        if i_summary == '':
            i_summary = 'No Summary Provided'

        iname = "Proofpoint TRAP Incident: ID {} - {}".format(incident['id'], i_summary)
        LOG.debug("Incident Label Assembled: %s", iname)

        return iname

    def get_resilient_incidents(self):
        """
        Just a Placeholder to scrape all incident data from Resilient

        """
        r_incidents = []
        query_uri = '/incidents/query?return_level=partial'
        query = {
            'filters': [{
                'conditions': [
                    {
                        'field_name': 'plan_status',
                        'method': 'equals',
                        'value': 'A'
                    }
                ]
            }],
            'sorts': [{
                'field_name': 'create_date',
                'type': 'desc'
            }]
        }
        try:
            r_incidents = self.rest_client().post(query_uri, query)
        except SimpleHTTPException as ex:
            LOG.error("Failed to pull incidents:%s", ex)
            r_incidents = 'Failed'
        return r_incidents


    def create_incident(self, data, tables):
        """
        Create Resilient Incident

        :param data: Formatted DTO for Incident
        :param tables: List of Data Tables to add to
        :return: Return response from Resilient
        """
        try:
            resilient_client = self.rest_client()

            uri = '/incidents'
            # create Incident itself first
            incident_response = resilient_client.post(uri=uri, payload=data)
            # extract new Incident ID from response
            incident_id = incident_response['id']

            # attach ancilliary data to Incident
            # self.create_incident_artifact(incident_id, artifacts)

            for table_id, contents in tables.items():
                if contents:
                    if table_id in DATA_TABLE_IDS:
                        # table data, add row to specified data table
                        uri = '/incidents/{0}/table_data/{1}/row_data'.format(incident_id, table_id)
                        LOG.info("Attempting to create table with the following: %s", uri)

                        for content in contents:
                            resilient_client.post(uri=uri, payload=content)
                    else:
                        # other data, create Note with details
                        uri = '/incidents/{0}/comments'.format(incident_id)
                        LOG.info("Attempting to add note with the following: %s", uri)
                        for content in contents:
                            resilient_client.post(uri=uri, payload=content)
            return incident_response

        except SimpleHTTPException as ex:
            LOG.error('Something went wrong when attempting to create the Incident: %s', ex)


    def create_incident_comment(self, incident_id, data):
        """
        Add a comment to the specified Resilient Incident by ID

        :param incident_id:  Resilient Incident ID
        :param data: Content to be added as note
        :return: Response from Resilient for debug
        """
        try:
            uri = '/incidents/{}/comments'.format(incident_id)
            resilient_client = self.rest_client()
            heading = "Raw Proofpoint TRAP Event Payload:\n"
            note = {
                'format': 'text',
                'content': '{}{}'.format(heading, pprint.pformat(data, indent=4))
            }
            payload = {'text': note}
            comment_response = resilient_client.post(uri=uri, payload=payload)
            return comment_response

        except SimpleHTTPException as ex:
            LOG.error("Failed to add note for incident %d: %s", incident_id, ex)


    def create_incident_artifact(self, incident_id, data):
        """

        :param incident_id: Incident ID
        :param data: Dictionary returned from extraction
        :return:
        """
        try:
            uri = '/incidents/{}/artifacts'.format(incident_id)
            resilient_client = self.rest_client()

            for key, val in data.items():
                LOG.debug("Processing list of %s: %s", key, val)
                for _v in val:
                    _desc = "{} extracted from Proofpoint TRAP Incident".format(key)
                    payload = {
                        "type": key,
                        "value": _v,
                        "description": {
                            "format": "text",
                            "content": _desc
                        }
                    }
                    LOG.info("Attempting to create artifact %s for incident %d", payload, incident_id)
                    resilient_client.post(uri=uri, payload=payload)


        except SimpleHTTPException as ex:
            LOG.error("Failed to add artifact for incident %d: %s", incident_id, ex)


    def make_incident_fields(self, incident):
        """
        Assemble the Incident DTO Payload / Fields from TRAP Event Payload

        :param incident: Incident from Proofpoint TRAP
        :return:
        """
        # Create Placeholder with lists as values
        r_fields = {
            'name': self.make_incident_name(incident),
            'description': self.make_incident_description(incident),
            'nist_attack_vectors': [],
            'incident_type_ids': [],
            'discovered_date': incident.get('created_at'),
            'properties': {},

        }

        i_fields = incident['incident_field_values']

        for field in i_fields:
            # Map NIST Attack Vector. Default to Email
            if field['name'] == 'Attack Vector':
                r_fields['nist_attack_vectors'].append(NIST_VECTORS.get(field['value'], 4))
            # Map Classification to Incident Type, Default to Phishing
            elif field['name'] == 'Classification':
                r_fields['incident_type_ids'].append(CLASS2TYPEID.get(field['value'], 22))
            elif field['name'] == 'Severity':
                # Get Incident Severity. Default to Low
                r_fields['severity_code'] = INCIDENT_SEVERITY.get(field['value'], 100)
            elif field['name'] == 'Abuse Disposition':
                # Get Disposition, Default to None (unconfirmed)
                r_fields['confirmed'] = ABUSE_DISPOSITION.get(field['value'], None)
        r_fields['properties']['proofpoint_trap_incident_id'] = incident.get('id')

        return r_fields

    def make_incident_description(self, incident):
        """
        Make Incident description text

        :param incident: Raw TRAP Payload
        :return: Return formatted Description for Incident DTO
        """
        i_summary = incident.get('summary', "Proofpoint TRAP Incident - Lacks a summary")
        i_event_count = len(incident['events'])
        i_sources = incident.get('event_sources', 'No Sources Found')

        description = '{}\n\nTotal Events in incident: {}\n\nFrom: {}\n'.format(i_summary, i_event_count, i_sources)
        return {'format': 'text', 'content': description}


    def make_incident_artifacts(self, incident):
        """
        Extract Artifact data

        :param data: The hosts section of the TRAP Incident
        :return: Dictionary of Artifacts for event
        """
        host_categories = self.options.get('host_categories', None)
        if host_categories is not None:
            host_categories = host_categories.split(",")
        else:
            host_categories = ["forensics"]
        artifacts = {}

        if 'hosts' in incident:
            # Process the selected categories under hosts.
            for hcat in host_categories:
                if hcat in incident['hosts']:
                    for key, val in REGEX_DEFS.items():
                        if key not in artifacts:
                            artifacts[key] = []
                        artifacts[key].extend([x for x in incident['hosts'][hcat] if re.match(val, x)
                                               and x not in artifacts[key]])
        return artifacts


    def _find_resilient_incident_for_req(self, incident_id, idtype):
        """Return list of incidents if there are any with the same case ID, else returns empty list"""
        r_incidents = []
        query_uri = '/incidents/query?return_level=partial'
        query = {
            'filters': [{
                'conditions': [
                    {
                        'field_name': 'properties.{}'.format(idtype),
                        'method': 'equals',
                        'value': incident_id
                    },
                    {
                        'field_name': 'plan_status',
                        'method': 'equals',
                        'value': 'A'
                    }
                ]
            }],
            'sorts': [{
                'field_name': 'create_date',
                'type': 'desc'
            }]
        }
        try:
            r_incidents = self.rest_client().post(query_uri, query)
        except SimpleHTTPException:
            # Some versions of Resilient 30.2 onward have a bug that prevents query for numeric fields.
            # To work around this issue, let's try a different query, and filter the results. (Expensive!)
            query_uri = '/incidents/query?return_level=normal&field_handle={}'.format(incident_id)
            query = {
                'filters': [{
                    'conditions': [
                        {
                            'field_name': 'properties.{}'.format(idtype),
                            'method': 'has_a_value'
                        },
                        {
                            'field_name': 'plan_status',
                            'method': 'equals',
                            'value': 'A'
                        }
                    ]
                }]
            }

            try:
                r_incidents_tmp = self.rest_client().post(query_uri, query)

            except Exception as err:
                raise Exception("Exception '{}' while trying to get list of Resilient incidents.".format(err))

            r_incidents = [r_inc for r_inc in r_incidents_tmp
                           if r_inc['properties'].get(idtype) == incident_id]

        return r_incidents




