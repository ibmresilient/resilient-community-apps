# -*- coding: utf-8 -*-

import pytest
import sys
import time
from collections import OrderedDict
from data_feeder_plugins.resilientfeed.resilientfeed import ResilientFeedDestination
from data_feeder_plugins.resilientfeed.resilient_common import Resilient
from rc_data_feed.lib.type_info import ActionMessageTypeInfo

TYPE_NAME = "all_types"

# master admin
MASTER_ADMIN_EMAIL = "a@example.com"
MASTER_ADMIN_PASSWORD = "Passw0rd"
TARGET_ORG = "sync"


APP_CONFIG = {
    "host": "localhost",
    "email": MASTER_ADMIN_EMAIL,
    "password": MASTER_ADMIN_PASSWORD,
    "port": 1443,
    "org": TARGET_ORG,
    "cafile": "false",
    "db_sync_file": "/tmp/proserve1.db"
}

TS = int(time.time())

INCIDENT_PAYLOAD = {
    "dtm": {},
    "cm": {
        "unassigneds": [
            {
                "geo": 1000,
                "count": 0
            },
            {
                "geo": 1001,
                "count": 0
            }
        ],
        "total": 0,
        "geo_counts": {}
    },
    "regulators": {
        "ids": [
            149
        ]
    },
    "hipaa": {
        "hipaa_adverse": None,
        "hipaa_misused": None,
        "hipaa_acquired": None,
        "hipaa_additional_misuse": None,
        "hipaa_breach": None,
        "hipaa_adverse_comment": "",
        "hipaa_misused_comment": "",
        "hipaa_acquired_comment": "",
        "hipaa_additional_misuse_comment": "",
        "hipaa_breach_comment": ""
    },
    "tasks": None,
    "artifacts": None,
    "name": "spear phishing attack",
    "description": None,
    "phase_id": 1004,
    "inc_training": False,
    "vers": 6,
    "addr": None,
    "city": None,
    "creator": {
        "id": 3,
        "fname": "Resilient",
        "lname": "Sysadmin",
        "display_name": "Resilient Sysadmin",
        "status": "A",
        "email": "a@example.com",
        "last_login": 1582242276723,
        "locked": False,
        "password_changed": False,
        "last_modified_time": 1582242276725,
        "create_date": 1562157359632,
        "is_external": False
    },
    "creator_principal": {
        "id": 3,
        "type": "user",
        "name": "a@example.com",
        "display_name": "Resilient Sysadmin"
    },
    "exposure_type_id": 1,
    "incident_type_ids": [
        22
    ],
    "reporter": None,
    "state": None,
    "country": None,
    "zip": None,
    "workspace": 1,
    "exposure": 0,
    "org_handle": 201,
    "members": [],
    "negative_pr_likely": None,
    "perms": {
        "read": True,
        "write": True,
        "comment": True,
        "assign": True,
        "close": True,
        "change_members": True,
        "attach_file": True,
        "read_attachments": True,
        "delete_attachments": True,
        "create_milestones": True,
        "list_milestones": True,
        "create_artifacts": True,
        "list_artifacts": True,
        "delete": True,
        "change_workspace": True
    },
    "confirmed": True,
    "task_changes": {
        "added": [],
        "removed": []
    },
    "assessment": "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>\n<assessment>\n    <rollups/>\n    <optional>There are 1 required and 0 optional tasks from 1 regulators.</optional>\n</assessment>\n",
    "data_compromised": None,
    "draft": False,
    "properties": {
        "custom_number": None,
        "custom_datetime": None,
        "custom_one": None,
        "campaign_task_id": None,
        "jira_url": "<a href=\"https://jira1-01.internal.resilientsystems.com/browse/INT-2061\">Link</a>",
        "messageID": None,
        "proofpoint_trap_incident_id": None,
        "ansible_value": None,
        "custom_org_resilient": None,
        "campaign_name": None,
        "jira_internal_url": "https://jira1-01.internal.resilientsystems.com/rest/api/2/issue/34000",
        "scheduler_demo": None,
        "campaign": None,
        "custom_bool": None,
        "campaign_id": None
    },
    "resolution_id": None,
    "resolution_summary": None,
    "pii": {
        "data_compromised": None,
        "determined_date": 1581456396053,
        "harmstatus_id": 2,
        "data_encrypted": None,
        "data_contained": None,
        "impact_likely": None,
        "data_source_ids": [],
        "data_format": None,
        "assessment": "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>\n<assessment>\n    <rollups/>\n    <optional>There are 1 required and 0 optional tasks from 1 regulators.</optional>\n</assessment>\n",
        "exposure": 0,
        "gdpr_harm_risk": None,
        "gdpr_lawful_data_processing_categories": [],
        "alberta_health_risk_assessment": None
    },
    "gdpr": {
        "gdpr_breach_circumstances": [],
        "gdpr_breach_type": None,
        "gdpr_personal_data": None,
        "gdpr_identification": None,
        "gdpr_consequences": None,
        "gdpr_final_assessment": None,
        "gdpr_breach_type_comment": None,
        "gdpr_personal_data_comment": None,
        "gdpr_identification_comment": None,
        "gdpr_consequences_comment": None,
        "gdpr_final_assessment_comment": None,
        "gdpr_subsequent_notification": None
    },
    "regulator_risk": {},
    "inc_last_modified_date": 1582048805147,
    "comments": None,
    "actions": [
        {
            "id": 14,
            "name": "Example: Ansible - Run a Module",
            "enabled": True
        },
        {
            "id": 15,
            "name": "Example: Ansible - Run a Playbook",
            "enabled": True
        },
        {
            "id": 25,
            "name": "Campaign Append",
            "enabled": True
        },
        {
            "id": 26,
            "name": "Campaign Close",
            "enabled": False
        },
        {
            "id": 27,
            "name": "Campaign Create",
            "enabled": True
        },
        {
            "id": 28,
            "name": "Campaign Remove",
            "enabled": False
        },
        {
            "id": 31,
            "name": "Example: Proofpoint TRAP: Get Incident Details",
            "enabled": True
        },
        {
            "id": 32,
            "name": "Example: Proofpoint TRAP: Get List Members",
            "enabled": True
        },
        {
            "id": 39,
            "name": "Demo Scheduler",
            "enabled": True
        },
        {
            "id": 38,
            "name": "Schedule a Rule to Run",
            "enabled": True
        },
        {
            "id": 49,
            "name": "delete rule3",
            "enabled": True
        },
        {
            "id": 42,
            "name": "List Scheduled Rules",
            "enabled": True
        },
        {
            "id": 55,
            "name": "Example: ElasticSearch Query from Incident",
            "enabled": True
        },
        {
            "id": 60,
            "name": "calc: sum",
            "enabled": True
        },
        {
            "id": 61,
            "name": "calc combined",
            "enabled": True
        },
        {
            "id": 59,
            "name": "calc: product",
            "enabled": True
        },
        {
            "id": 74,
            "name": "Ansible Tower List Jobs",
            "enabled": True
        },
        {
            "id": 75,
            "name": "Ansible Tower Run an Ad Hoc Command",
            "enabled": True
        },
        {
            "id": 81,
            "name": "Example: Post an Incident to Microsoft Teams",
            "enabled": True
        },
        {
            "id": 78,
            "name": "Ansible Tower Run Job - Incident",
            "enabled": True
        },
        {
            "id": 73,
            "name": "Ansible Tower List Job Templates",
            "enabled": True
        },
        {
            "id": 152,
            "name": "Example: Send Twilio SMS",
            "enabled": True
        },
        {
            "id": 153,
            "name": "Task Utils: Add Note to Task",
            "enabled": True
        },
        {
            "id": 154,
            "name": "Task Utils: Close Task (Activity Field)",
            "enabled": True
        },
        {
            "id": 155,
            "name": "Task Utils: Create Custom Task",
            "enabled": True
        },
        {
            "id": 156,
            "name": "Task Utils: Create Custom Task (Activity Field)",
            "enabled": True
        },
        {
            "id": 160,
            "name": "Example: Approval with Twilio",
            "enabled": True
        },
        {
            "id": 161,
            "name": "test taskutils",
            "enabled": True
        },
        {
            "id": 22,
            "name": "Data Feeder: Sync Incidents",
            "enabled": True
        },
        {
            "id": 158,
            "name": "Example: Twilio Receive Messages",
            "enabled": True
        },
        {
            "id": 169,
            "name": "Example: Create Jira Issue",
            "enabled": False
        }
    ],
    "admin_id": None,
    "creator_id": 3,
    "crimestatus_id": 3,
    "employee_involved": None,
    "end_date": None,
    "exposure_dept_id": None,
    "exposure_individual_name": None,
    "exposure_vendor_id": None,
    "jurisdiction_name": None,
    "jurisdiction_reg_id": None,
    "start_date": None,
    "inc_start": None,
    "org_id": 201,
    "is_scenario": False,
    "hard_liability": 0,
    "nist_attack_vectors": [],
    "id": 2241,
    "discovered_date": 1581456396053,
    "due_date": None,
    "create_date": 1581456623116,
    "owner_id": 3,
    "severity_code": 53,
    "plan_status": "A"
}


created_inc_id = None

MSG_PAYLOAD = OrderedDict({"id":  TS,
                           "inc_id": 2301,
                           "test_text": u"ƀ Ɓ Ƃ ƃ Ƅ ƅ Ɔ Ƈ ƈ",
                           "test_int": 1000,
                           "test_date": 1550073347448,
                           "test_datetime": 1550073347448,
                           "test_bool": True
                           })

RESULT_PAYLOAD = {  "id":  TS,
                    "inc_id": 2301,
                    "test_text": u"ƀ Ɓ Ƃ ƃ Ƅ ƅ Ɔ Ƈ ƈ",
                    "test_int": 1000,
                    "test_bool": 1
                 }

if sys.version_info.major == 2:
    RESULT_PAYLOAD['test_date']     = "2019-02-13T15:55:47"
    RESULT_PAYLOAD['test_datetime'] = "2019-02-13T15:55:47+00:00"
else:
    RESULT_PAYLOAD['test_date']     = "2019-02-13T15:55:47.448000"
    RESULT_PAYLOAD['test_datetime'] = "2019-02-13T15:55:47.448000+00:00"

def test_incident():
    resilient_target = Resilient(APP_CONFIG, None)

    response = resilient_target.create_update_type(INCIDENT_PAYLOAD['id'], INCIDENT_PAYLOAD['org_id'], "incident", INCIDENT_PAYLOAD, INCIDENT_PAYLOAD['id'])

'''
def test_datafeeder_sync():
    """
    test that all fields sent for a elastic_feed are present
    :return:
    """
    resilient_target = Resilient(APP_CONFIG)

    context = Context()
    es_feed.send_data(context, MSG_PAYLOAD)

    # test the results
    result = ES.get(index=INDEX, doc_type=TYPE_NAME, id=MSG_PAYLOAD['id'])

    for key, value in RESULT_PAYLOAD.items():
        assert result["_source"][key] == value

    assert result["_version"] == 1

def test_update():
    """
    test that all fields sent for a elastic_feed are present
    :return:
    """
    es_feed = ElasticFeedDestination(None, APP_CONFIG)

    context = Context()

    update_payload = MSG_PAYLOAD.copy()
    update_payload['test_text'] = "a" * 100
    update_result = RESULT_PAYLOAD.copy()
    update_result['test_text'] = update_payload['test_text']

    es_feed.send_data(context, update_payload)

    # test the results
    ES.indices.refresh(index=INDEX)

    result = ES.get(index=INDEX, doc_type=TYPE_NAME, id=update_payload['id'])

    for key, value in update_result.items():
        assert result["_source"][key] == value

    # depends on previous tests
    assert result["_version"] == 2

def test_alter():
    """
    test that all fields sent for a elastic_feed are present
    :return:
    """
    es_feed = ElasticFeedDestination(None, APP_CONFIG)

    context = Context()

    update_payload = MSG_PAYLOAD.copy()
    update_payload['alter_text'] = "this is a new column " + str(TS)
    update_result = RESULT_PAYLOAD.copy()
    update_result['alter_text'] = update_payload['alter_text']

    result = es_feed.send_data(context, update_payload)

    # test the results
    ES.indices.refresh(index=INDEX)

    test_result = ES.get(index=INDEX, doc_type=TYPE_NAME, id=update_payload['id'])

    for key, value in update_result.items():
        assert test_result["_source"][key] == value

    # depends on previous tests
    assert test_result["_version"] == 3

def test_delete():
    es_feed = ElasticFeedDestination(None, APP_CONFIG)

    context = Context(is_deleted=True)

    es_feed.send_data(context, MSG_PAYLOAD)

    # test the results
    with pytest.raises(Exception) as err:
        test_result = ES.get(index=INDEX, doc_type=TYPE_NAME, id=MSG_PAYLOAD['id'])
        assert err['found'] == False


class Context():
    """
    This class mimics that which is received when the message is dequeued from a message destination
    """
    def __init__(self, is_deleted=False):
        self.inc_id = RESULT_PAYLOAD['inc_id']
        self.type_info = ActionMessageTypeInfo(RESULT_PAYLOAD['id'],
                                               TYPE_INFO_MAP,
                                               None)        # no res_client is used
        # patch the two functions which make calls back to resilient to use our own dto objects
        self.type_info.get_all_fields = self.get_all_fields
        self.type_info.get_type = self.get_type
        self.is_deleted = is_deleted

    def get_all_fields(self, refresh=False):
        """
        mock the results
        :param refresh:
        :return:
        """
        return ALL_FIELDS_DTO

    def get_type(self, type_id):
        """
        mock the results
        :param type_id:
        :return:
        """
        return TYPE_DTO

# all_types object fields
FIELDS = {
    "id": {
        "id": 1,
        "name": "id",
        "prefix": None,
        "internal": False,
        "type_id": 1,
        "input_type": "number"
    },
    "inc_id": {
        "id": 2,
        "name": "inc_id",
        "prefix": None,
        "internal": False,
        "type_id": 1,
        "input_type": "number"
    },
    "test_text": {
        "id": 3,
        "name": "test_text",
        "prefix": None,
        "internal": False,
        "type_id": 2,
        "input_type": "text"
    },
    "test_int": {
        "id": 4,
        "name": "test_int",
        "prefix": None,
        "internal": False,
        "type_id": 1,
        "input_type": "number"
    },
    "test_date": {
        "id": 5,
        "name": "test_date",
        "internal": False,
        "type_id": 3,
        "input_type": "datepicker"
    },
    "test_datetime": {
        "id": 6,
        "name": "test_datetime",
        "prefix": None,
        "internal": False,
        "type_id": 4,
        "input_type": "datetimepicker",
    },
    "test_bool": {
        "id": 7,
        "name": "test_bool",
        "prefix": None,
        "internal": False,
        "type_id": 5,
        "input_type": "boolean"
    },
    "alter_text": {
        "id": 8,
        "name": "alter_text",
        "prefix": None,
        "internal": False,
        "type_id": 2,
        "input_type": "text"
    }
}

# format returned from api call /types/{type_id}
TYPE_DTO = {
    "id": 1,
    "type_id": 10,
    "type_name": "all_types",
    "fields": FIELDS
}

# format returned from /types/{type_id}/fields
ALL_FIELDS_DTO = [FIELDS[key] for key in FIELDS.keys()]

# format of data off the message queue
TYPE_INFO_MAP = {
    "all_types": {
        "fields": FIELDS
    }
}
'''