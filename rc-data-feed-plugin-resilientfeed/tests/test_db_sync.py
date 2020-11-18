# -*- coding: utf-8 -*-
import pytest
import json
import time
from data_feeder_plugins.resilientfeed.resilient_common import DBSyncFactory

DB_FILE = "/tmp/test_{}.sqlite3".format(time.time())

@pytest.fixture
def db_conn():
    return DBSyncFactory.get_dbsync(202, DB_FILE, None, None, None) # org_id, sqllite_file, db_connection, db_user, db_pwd

def test_retry_task_insert_select_delete(db_conn):
    payload = {'actions': [], 'active': True, 'attachments_count': None, 'auto_deactivate': True,
               'cat_name': 'Detect/Analyze', 'category_id': None, 'closed_date': None,
               'creator_principal': {'display_name': 'Resilient Sysadmin', 'id': 3, 'name': 'a@example.com', 'type': 'user'},
               'custom': True, 'description': None, 'due_date': None, 'form': None, 'frozen': False, 'inc_id': 2305,
               'inc_name': 'sync first',
               'inc_owner_id': {'display_name': 'Resilient Sysadmin', 'id': 3, 'name': 'a@example.com', 'type': 'user'},
               'inc_training': False, 'init_date': 1583599025989,
               'instructions': {'format': 'text', 'content': 'Research current cyber threat intelligence and recently published \nvulnerability alerts to help focus your analysis. Sources include the \nUS-CERT National Cyber Awareness System accessible at \nhttps://www.us-cert.gov/ncas, the CERT vulnerability database at \nhttp://www.kb.cert.org/vuls/ or the NIST National Vulnerability Database at \nhttp://nvd.nist.gov/'},
               'members': None, 'name': 'Research current attack intelligence and recent vulnerabilities', 'notes': [],
               'notes_count': None, 'owner_fname': None, 'owner_id': None, 'owner_lname': None,
               'perms': {'assign': True, 'attach_file': True, 'change_members': True, 'close': True, 'comment': True, 'delete_attachments': True, 'read': True, 'read_attachments': True, 'write': True},
               'phase_id': {'name': 'Detect/Analyze'}, 'private': None, 'regs': {}, 'required': True, 'src_name': None,
               'status': 'Open', 'task_layout': None, 'user_notes': None}

    payload_str = json.dumps(payload)

    # create_retry_row(self, orig_org_id, orig_inc_id, type_name, orig_type_id,
    #                          org1_dep_type_name, org1_dep_type_id,
    #                          new_inc_id, payload):
    db_conn.create_retry_row(201, 1000, "incident", 1000,
                              "task", 2000,
                              None, payload_str, 1)
    db_conn.create_retry_row(201, 1000, "incident", 1000,
                              "task", 2001,
                              None, payload_str, 1)

    row_list = db_conn.find_retry_rows(201, 1000, "incident")

    # org1_type_id, org2_inc_id, org1_dep_type_name, org1_dep_type_id, payload
    assert row_list
    assert row_list[0][0] == 1000
    assert row_list[0][1] == None
    assert row_list[0][2] == "task"
    assert row_list[0][4] == payload_str

    assert row_list[0][0] == 1000
    assert row_list[0][1] == None
    assert row_list[0][2] == "task"
    assert row_list[0][4] == payload_str

    db_conn.delete_retry_rows(201, 1000, "incident", 1000)

    row_list = db_conn.find_retry_rows(201, 1000, "incident")

    assert not row_list

def test_retry_attachment_insert_select_delete(db_conn):
    """
    2020-03-16 12:06:51,627 INFO [resilient_common] adding attachment:337 to 209:2874
2020-03-16 12:06:51,645 ERROR [resilient_common] Unable to create attachment for file: US2J6497.ID
2020-03-16 12:06:51,646 ERROR [resilient_common] {'actions': [], 'content_type': 'application/octet-stream', 'created': 1583785008064, 'creator_id': {'display_name': 'Resilient Sysadmin', 'id': 3, 'name': 'a@example.com', 'type': 'user'}, 'inc_id': 2444, 'inc_name': 'sync intrusion', 'inc_owner': {'display_name': 'Resilient Sysadmin', 'id': 3, 'name': 'a@example.com', 'type': 'user'}, 'name': 'US2J6497.ID', 'size': 8646, 'task_at_id': {'id': 40, 'name': 'initial_triage'}, 'task_custom': True, 'task_id': 2259186, 'task_members': None, 'task_name': 'Initial Triage', 'type': 'task', 'uuid': '0cdf9c29-09de-4322-9fc0-74769d420de6', 'vers': 7}
2020-03-16 12:06:51,646 ERROR [resilient_common] Not Found:  {"success":false,"title":null,"message":"Unable to find object with ID 2,267,891","hints":
    :param db_conn:
    :return:
    """
    payload = {'actions': [], 'content_type': 'application/octet-stream', 'created': 1583785008064,
               'creator_id': {'display_name': 'Resilient Sysadmin', 'id': 3, 'name': 'a@example.com', 'type': 'user'},
               'inc_id': 2444, 'inc_name': 'sync intrusion',
               'inc_owner': {'display_name': 'Resilient Sysadmin', 'id': 3, 'name': 'a@example.com', 'type': 'user'},
               'name': 'US2J6497.ID', 'size': 8646, 'task_at_id': {'id': 40, 'name': 'initial_triage'},
               'task_custom': True, 'task_id': 2259186, 'task_members': None, 'task_name': 'Initial Triage',
               'type': 'task', 'uuid': '0cdf9c29-09de-4322-9fc0-74769d420de6', 'vers': 7}


    payload_str = json.dumps(payload)

    # create_retry_row(self, orig_org_id, orig_inc_id, type_name, orig_type_id,
    #                          org1_dep_type_name, org1_dep_type_id,
    #                          new_inc_id, payload):
    db_conn.create_retry_row(201, 1000, "task", 2267891,
                              "attachment", 337,
                             2874, payload_str, 1)

    row_list = db_conn.find_retry_rows(201, 1000, "task")

    # org1_type_id, org2_inc_id, org1_dep_type_name, org1_dep_type_id, payload
    assert row_list
    assert row_list[0][0] == 2267891
    assert row_list[0][1] == 2874
    assert row_list[0][2] == "attachment"
    assert row_list[0][3] == 337
    assert row_list[0][4] == payload_str

    db_conn.delete_retry_rows(201, 1000, "task", 2267891)

    row_list = db_conn.find_retry_rows(201, 1000, "task")

    assert not row_list
