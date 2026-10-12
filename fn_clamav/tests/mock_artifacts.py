# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
"""Generate Mock responses to simulate Cisco AMP for endpoinst for Unit and function tests """
import re


def get_data(file_name, incident_id):
        pass


def get_metadata(file_name, incident_id):
    pass

def mocked_res_client(*args):

    """Function will be used by the mock to replace resilient client"""
    class MockResponse:
        def __init__(self, *arg):
            pass

        def __contains__(self, key):
            return True if key in self.__dict__.keys() else False

        def _get_data(self):
            return 'X5O!P%@AP[4\\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*'

        def _get_content(self, type):
            response = {
                         "incident_id": {u'task_at_id': None, u'vers': 50, u'name': u'incident_eicar.txt', u'task_id': None,
                                        u'created': 1544603748680, u'inc_owner': 4, u'task_members': None, u'task_custom': None,
                                        u'task_name': None, u'actions': [{u'enabled': True, u'id': 29,
                                                                          u'name': u'Example: ClamAV scan attachment'}],
                                        u'inc_name': u'ClamAV', u'creator_id': 4, u'content_type': u'text/plain', u'inc_id':
                                            2095, u'type': u'incident', u'id': 18, u'size': 69},

                         "artifact_id": {u'hits': [], u'hash': u'a39aee8e740f0344194a1b46ae62ceb1724e7ac02c2cb9c71c615f17a3bc49a7',
                                         u'description': None, u'creator': {u'status': u'A', u'password_changed': False,
                                                                            u'display_name': u'Resilient Sysadmin',
                                                                            u'is_external': False, u'email': u'a@a.com',
                                                                            u'lname': u'Sysadmin', u'create_date': 1514410126812,
                                                                            u'last_login': 1545068067059, u'fname': u'Resilient',
                                                                            u'last_modified_time': 1545068067059, u'locked': False, u'id': 4},
                                         u'inc_owner': 4, u'perms': {u'read': True, u'write': True, u'delete': True},
                                         u'created': 1544603975028, u'relating': None, u'value': u'artifact_eicar.txt',
                                         u'properties': None, u'parent_id': None, u'attachment': {u'task_at_id': None,
                                                                                                  u'vers': 50,
                                                                                                  u'name': u'artifact_eicar.txt',
                                                                                                  u'task_id': None, u'created': 1544603975061,
                                                                                                  u'inc_owner': 4, u'task_members':
                                                                                                      None, u'task_custom': None, u'task_name':
                                                                                                      None, u'actions': [],
                                                                                                  u'inc_name': u'ClamAV', u'creator_id': 4,
                                                                                                  u'content_type': u'text/plain',
                                                                                                  u'inc_id': 2095, u'type':
                                                                                                      u'artifact', u'id': 22,
                                                                                                  u'size': 69},
                                         u'inc_name': u'ClamAV', u'creator_principal': {u'display_name': u'Resilient Sysadmin',
                                                                                        u'type': u'user', u'id': 4, u'name': u'a@a.com'},
                                         u'inc_id': 2095, u'type': 7, u'id': 21, u'actions': [{u'enabled': True, u'id': 50,
                                                                                               u'name': u'Example: ClamAV scan artifact attachment'}],
                                         u'pending_sources': []},
                         "task_id": {u'task_at_id': None, u'vers': 50, u'name': u'task_eicar.txt', u'task_id': 2251251,
                                     u'created': 1544604120052, u'inc_owner': 4, u'task_members': None, u'task_custom': True,
                                     u'task_name': u'test task', u'actions':
                                         [{u'enabled': True, u'id': 29, u'name': u'Example: ClamAV scan attachment'}],
                                     u'inc_name': u'ClamAV', u'creator_id': 4, u'content_type': u'text/plain', u'inc_id': 2095,
                                     u'type': u'task', u'id': 25, u'size': 69},
                        }

            return response[type]

        def get(self, metadata_uri):
            if re.match("^/incidents/[0-9]+/attachments/[0-9]+$", metadata_uri):
                return self._get_content("incident_id")
            elif  re.match("^/incidents/[0-9]+/artifacts/[0-9]+$", metadata_uri):
                return self._get_content("artifact_id")
            elif re.match("^/tasks/[0-9]+/attachments/[0-9]+$", metadata_uri):
                return self._get_content("task_id")

        def get_content(self, data_uri):
            return self._get_data().encode()

    return MockResponse(*args)


def mocked_pyclamd_client(*args, **kwargs):

    class MockResponse:
        """Class will be used by the mock to replace pyclamd in circuits tests"""
        def __init__(self, host='127.0.0.1', port=3310, timeout=None):
            pass

        def ping(self):
            return True

        def scan_stream(self, stream, chunk_size=4096):
            dr = {"stream": ("FOUND", "Eicar-Test-Signature")}
            return dr

    return MockResponse(*args, **kwargs)



def get_mock_config():
    config_data = u"""[fn_clamav]
# hostname or ip address of Clamav server
host=localhost
# The TCP port Clamav listens on
port=3310
# Define socket timeout
timeout=500
"""
    return config_data