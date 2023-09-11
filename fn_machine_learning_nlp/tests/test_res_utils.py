#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from fn_machine_learning_nlp.lib.res_utils import ResUtils
import resilient
import sys
import pandas as pds
import pytest


class OptParser(resilient.ArgumentParser):
    """
    This is a subclass of resilient.ArgumentParser. resilient.ArgumentParser takes care of both
        1. Reading app.config
        2. Validating required command line arguments.
    Here we just want app.config, we are parsing/validating commandline arguments in our main function.
    """

    def __init__(self, config_file=None):
        self.config_file = config_file or resilient.get_config_file()
        super(OptParser, self).__init__(config_file=self.config_file)
        #
        #   Note this is a trick used by resilient-circuits. resilient.ArgumentParser will
        #   validate the arguments of the command line. Since we use command line
        #   argument of input/output files, we don't want that validation, so we
        #   erase them before we call parse_args(). Then parse_args() only
        #   reads from app.config
        #
        sys.argv = sys.argv[0:1]
        self.opts = self.parse_args()

        if self.config:
            for section in self.config.sections():
                #
                # Handle sections other than [resilient] in app.config
                #
                items = dict((item.lower(), self.config.get(section, item)) for item in self.config.options(section))
                self.opts.update({section: items})

            resilient.parse_parameters(self.opts)


def test_get_artifact_des():
    artifact_json = {
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
                                     'is_external': False, 'id': 2, 'lname': 'tester-l', 'fname': 'tester-f',
                                     'locked': False,
                                     'last_login': 1571316984665, 'last_modified_time': 1571316984666,
                                     'create_date': 1565121110906, 'password_changed': False},
                         'hits': [],
                         'inc_owner': {'name': 'tester@example.com', 'type': 'user',
                                       'display_name': 'tester-f tester-l',
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
                         'type': {'name': 'IP Address', 'id': 1},
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

if __name__=="__main__":
    #
    #   Test 1: Extract des from artifacts
    #   Static function. Test data hard coded
    test_get_artifact_des()

    #
    #   Make connection to do other tests
    #
    opt_parser = OptParser(config_file=None)
    res_util = ResUtils()
    #
    #   Test 2: Connect
    #
    res_util.connect(opt_parser)
    assert (res_util.res_client is not None)

    #
    #   Test 3: Get all incidents. Make sure
    #   your server (app.config) has some incidents
    #
    res_util.download_incidents()
    #   check file
    dataframe = pds.read_csv("resilient-incidents.csv",
                             sep=',',
                             usecols=["id", "name", "description", "resolution_summary"],
                             skipinitialspace=True,
                             quotechar='"')
    #   size
    row_count = dataframe.shape[0]
    assert (row_count > 0)

    all_ids = []
    for index in range(row_count):
        row = dataframe.iloc[index]
        all_ids.append(int(row["id"]))
    print("Lowest id {}".format(min(all_ids)))
    print("Highest id {}".format(max(all_ids)))
    #
    #   Test 4: Download all artifacts
    #
    res_util.download_artifacts()

    #
    #   Test 5: get incidents after a given id
    #
    ret = res_util.get_incidents_after(min(all_ids))
    assert (len(ret) == len(all_ids) - 1)
    print("Done")
