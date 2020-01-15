#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from fn_resilient_ml.lib.res_utils import ResUtils

def test_get_artifact_des(json_artifacts=None):
    artifact_json = json_artifacts if json_artifacts else {
        "results":
    [{'inc_id': 2138,
      'result': {'value': '10.0.0.17',
                 'inc_id': 2138,
                 'inc_name': 'QRadar ID 97 , Access Denied  - 10.0.0.17',
                 'description': {'content': 'QRadar Offense Source: Source IP', 'format': 'text'},
                 'id': 79,
                 'creator_principal': {'name': 'tester@example.com', 'type': 'user',
                                       'display_name': 'tester-f tester-l', 'id': 2},
                 'type': {'name': 'IP Address', 'id': 1},
                 'actions': [],
                 'attachment': None,
                 'creator': {'status': 'A', 'email': 'tester@example.com', 'display_name': 'tester-f tester-l',
                             'is_external': False, 'id': 2, 'lname': 'tester-l', 'fname': 'tester-f', 'locked': False,
                             'last_login': 1571316984665, 'last_modified_time': 1571316984666,
                             'create_date': 1565121110906, 'password_changed': False},
                 'hits': [],
                 'inc_owner': {'name': 'tester@example.com', 'type': 'user', 'display_name': 'tester-f tester-l',
                               'id': 2},
                 'created': 1570105371707,
                 'pending_sources': [],
                 'perms': None,
                 'properties': [{'name': 'source', 'value': 'true'}],
                 'hash': 'd7719e6cd668fe84c7fd3d1dbac379d8007f25c9f69e70d5d253bbd28db20dc9',
                 'parent_id': None,
                 'relating': None
                 },
      'inc_name': 'QRadar ID 97 , Access Denied  - 10.0.0.17',
      'score': 3.3,
      'task_id': None,
      'obj_create_date': 1570105371707,
      'inc_owner_id': 2,
      'obj_creator_id': 2,
      'type_id': 'artifact',
      'obj_id': 79,
      'org_id': 201,
      'task_name': None
      },
     {'inc_id': 2136,
      'result': {'value': '10.0.0.17',
                 'inc_id': 2136,
                 'inc_name': 'QRadar ID 97 , Access Denied  - 10.0.0.17',
                 'description': {
                    'content': 'QRadar Offense Source: Source IP',
                    'format': 'text'},
                 'id': 73,
                 'creator_principal': {'name': 'tester@example.com',
                                       'type': 'user',
                                       'display_name': 'tester-f tester-l',
                                       'id': 2},
                 'type': {'name': 'IP Address','id': 1},
                 'actions': [],
                 'attachment': None,
                 'creator': {'status': 'A',
                           'email': 'tester@example.com',
                           'display_name': 'tester-f tester-l',
                           'is_external': False,
                           'id': 2,
                           'lname': 'tester-l',
                           'fname': 'tester-f',
                           'locked': False,
                           'last_login': 1571316984665,
                           'last_modified_time': 1571316984666,
                           'create_date': 1565121110906,
                           'password_changed': False},
                 'hits': [],
                 'inc_owner': {
                     'name': 'tester@example.com',
                     'type': 'user',
                     'display_name': 'tester-f tester-l', 'id': 2},
                 'created': 1570036653644,
                 'pending_sources': [],
                 'perms': None,
                 'properties': [{'name': 'source',
                                 'value': 'true'}],
                 'hash': 'd7719e6cd668fe84c7fd3d1dbac379d8007f25c9f69e70d5d253bbd28db20dc9',
                 'parent_id': None,
                 'relating': None},
      'inc_name': 'QRadar ID 97 , Access Denied  - 10.0.0.17',
      'score': 3.3,
      'task_id': None,
      'obj_create_date': 1570105371707,
      'inc_owner_id': 2,
      'obj_creator_id': 2,
      'type_id': 'artifact',
      'obj_id': 79,
      'org_id': 201,
      'task_name': None
      }
    ]
    }
    des = ResUtils.get_artifact_des(2138, artifact_json=artifact_json)

    assert len(des) > 0
    assert "10.0.0.17" in des
    assert "QRadar Offense Source: Source IP" in des
    print("Done")

if __name__ == "__main__":
    j_dict = None
    with open("resilient_artifacts.json", "r") as infile:
        j_dict = json.load(infile)
    test_get_artifact_des(j_dict)