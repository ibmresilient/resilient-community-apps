# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

import pytest
import logging
import os
import json
from fn_symantec_dlp.lib.jinja_common import JinjaEnvironment

SYMANTEC_DLP_CREATE_CASE = "../fn_symantec_dlp/lib/templates/dlp_create_case_template.jinja"

INCIDENT1 = {
    'staticIncidentDetails': {  
        'incidentId': 444,
        'infoMap': { 'creationDate': '2022-02-08T18:58:29',
                     'detectionDate': '2022-02-08T18:58:37'
                    }
    },
    'editableIncidentDetails': { 
        'infoMap': {   
                    'incidentStatusName': 'incident.status.New',
                    'severityId': 1
                    }
    },
    'sdlp_incident_url': 'https://server/#incidents/2444',

    'comments': [],
    'artifacts': [
    ]
}

RESULT1 = {
    'name': 'Symantec DLP Incident Id 444',
    'description': 'An incident imported using the Symantec DLP Integration',
    'severity_code': 'High',
    'discovered_date': 1644346682000,
    'start_date': 1644346683000,
    'incident_type_ids': [16],
    'properties': { 'sdlp_incident_id': 444,
                    'sdlp_incident_status': 'incident.status.New',
                    'sdlp_incident_url': {'format': "html",
                                          'content': "<a target='blank' href='https://server/#incidents/2444'>Symantec DLP Incident</a>"
                                         }
    },
    "artifacts": [],
"comments": []
}

LOG = logging.getLogger(__name__)

class TestSymantecDLP:
    def test_create_case(self):
        jinja_env = JinjaEnvironment()

        template_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), SYMANTEC_DLP_CREATE_CASE)
        result = jinja_env.make_payload_from_template(None, template_path, INCIDENT1)
        assert(RESULT1 == result)