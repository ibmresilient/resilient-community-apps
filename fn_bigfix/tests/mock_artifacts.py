# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
"""Generate Mock responses to simulate BigFix for Unit and function tests """
import re
import time

def post_res_att(file_name, incident_id):
    return dict({u'task_at_id': None, u'vers': 2, u'name': file_name,
                 u'task_id': None, u'created': 1531959479048, u'inc_owner': 4,
                 u'task_members': None, u'task_custom': None, u'task_name': None,
                 u'actions': [], u'inc_name': u'BigFix', u'creator_id': 4,
                 u'content_type': u'text/plain', u'inc_id': incident_id, u'type': u'incident',
                 u'id': 1, u'size': 37261
                }
    )

def get_asset_properties():
    response = """
        <?xml version='1.0' ?>
        <report> Computer ID 13550086 Properties:
            <property> Quarantine Status
                <name> Quarantine Status Property </name>
                <value> False </value>
            </property>
            <property> Retrieved Property
                <name> Computer Name </name>
                <value> DESKTOP-TUKM3HF </value>
            </property>
            <property> Retrieved Property
                <name> OS </name>
                <value> Win10 10.0.15063.483 (1703) </value>
            </property>
            <property> Retrieved Property
                <name> CPU </name>
                <value> 2900 MHz Core i7-7820HQ </value>
            </property>
            <property> Retrieved Property
                <name> Last Report Time </name>
                <value> Tue, 24 Jul 2018 14:20:29 +0000 </value>
            </property>
            <property> Retrieved Property
                <name> Locked </name>
                <value> No </value>
            </property>
            <property> Retrieved Property
                <name> Lock Expiration </name>
                <value> None </value>
            </property>
            <property> Retrieved Property
                <name> BES Relay Selection Method </name>
                <value> Manual </value>
            </property>
            <property> Retrieved Property
                <name> Relay </name>
                <value> bigfix.test:52311 </value>
            </property>
            <property> Retrieved Property
                <name> Distance to BES Relay </name>
                <value> 0 </value>
            </property>
            <property> Retrieved Property
                <name> BES Relay Service Installed </name>
                <value> None </value>
            </property>
            <property> Retrieved Property
                <name> Relay Name of Client </name>
                <value> DESKTOP-TUKM3HF </value>
            </property>
            <property> Retrieved Property
                <name> DNS Name </name>
                <value> DESKTOP-TUKM3HF </value>
            </property>
        </report>
    """
    return response

def get_artifact_data_1():
    return list([{'computer_id': 12315195, 'failure': False, 'resp_time': 0, 'query_id': 1,
                  'result': u'True', 'computer_name': u'bigfix.test'},
                 {'computer_id': 13550086, 'failure': True, 'resp_time': 0, 'query_id': 1,
                  'result': u'Singular expression refers to nonexistent object.', 'computer_name': u'DESKTOP-TUKM3HF'}
    ])

def get_artifact_data_2():
    return list([{'computer_id': 12315195, 'failure': False, 'resp_time': 0, 'query_id': 1,
                  'result': u'True', 'computer_name': u'bigfix.test-1'},
                 {'computer_id': 12315196, 'failure': False, 'resp_time': 0, 'query_id': 1,
                  'result': u'True', 'computer_name': u'bigfix.test-2'},
                 {'computer_id': 13550086, 'failure': True, 'resp_time': 0, 'query_id': 1,
                  'result': False, 'computer_name': u'DESKTOP-TUKM3HF-1'},
                 {'computer_id': 13550087, 'failure': True, 'resp_time': 0, 'query_id': 1,
                  'result': False, 'computer_name': u'DESKTOP-TUKM3HF-2'},
                 {'computer_id': 13550088, 'failure': True, 'resp_time': 0, 'query_id': 1,
                  'result': False, 'computer_name': u'DESKTOP-TUKM3HF-3'}
    ])

def mocked_res_client(*args):

    """Function will be used by the mock to replace resilient client"""
    class MockResponse:
        def __init__(self, *arg):
            if arg and arg[0] == "post_attachment":
                self.file_name = arg[1]
                self.incident_id = arg[2]

        def __contains__(self, key):
            return True if key in self.__dict__.keys() else False

        def post_attachment(self, uri, filepath, filename=None, mimetype=None, data=None):
            if not "file_name" in self:
                self.file_name = filename
            if not "incident_id" in self:
                self.incident_id = uri.split('/')[2]
            return post_res_att(self.file_name, self.incident_id)

    return MockResponse(*args)

def mocked_bigfix_client(*args):

    """Function will be used by the mock to replace bigfix_client"""
    class MockResponse:
        def __init__(self, *arg):
            if arg and arg[0] == "get_bf_action_status":
                self.result_type = arg[1]
                self.end_time = arg[2]

        def __contains__(self, key):
            return True if key in self.__dict__.keys() else False

        def get_bf_action_status(self, bigfix_action_id):
            if not "result_type" in self:
                return self._get_bf_action_status(bigfix_action_id)
            else:
                return self._get_bf_action_status_standalone(self.result_type, self.end_time)

        def send_kill_process_remediation_message(self, bigfix_artifact_value, bigfix_asset_id):
            return  self._send_kill_process_remediation_message()

        def send_stop_service_remediation_message(self, bigfix_artifact_value, bigfix_asset_id):
            return  self._send_stop_service_remediation_message()

        def send_delete_registry_key_remediation_message(self, bigfix_artifact_value, bigfix_asset_id):
            return  self._send_delete_registry_key_remediation_message()

        def send_delete_file_remediation_message(self, bigfix_artifact_value, bigfix_asset_id):
            return  self._send_delete_file_remediation_message()

        def get_bf_computer_by_ip(self, bigfix_artifact_value):
            return self._get_bf_computer_by_ip()

        def get_bf_computer_by_file_path(self, bigfix_artifact_value):
            return  self._get_bf_computer_by_file_path()

        def get_bf_computer_by_process_name(self, bigfix_artifact_value):
            return  self._get_bf_computer_by_process_name()

        def get_bf_computer_by_service_name(self, bigfix_artifact_value):
            return  self._get_bf_computer_by_service_name()

        def get_bf_computer_by_registry_key_name_value(self, bigfix_artifact_value, bigfix_artifact_properties_name,
                                                       bigfix_artifact_properties_value):
            return  self._get_bf_computer_by_registry_key_name_value()

        def get_bf_computer_properties(self, bigfix_asset_id):
            return  self._get_bf_computer_properties()

        @staticmethod
        def _get_bf_action_status(bigfix_action_id):
            if bigfix_action_id == 123:
                return "The action executed successfully."
            elif bigfix_action_id == 124:
                return "The Fixlet which this action addresses is not relevant on this machine."
            elif bigfix_action_id == 125:
                return "The action failed."

        @staticmethod
        def _return_response(end_time, response):
            if time.time() > end_time:
                return response
            else:
                return None

        @staticmethod
        def _get_bf_action_status_standalone(result_type, end_time):
            if result_type == "success":
                return MockResponse._return_response(end_time, "The action executed successfully.")
            elif result_type == "not_relevant":
                return MockResponse._return_response(end_time,
                                       "The Fixlet which this action addresses is not relevant on this machine.")
            elif result_type == "failed":
                return MockResponse._return_response(end_time, "The action failed.")
            elif result_type == "timedout":
                return MockResponse._return_response(end_time, "The action executed successfully.")

        @staticmethod
        def _send_kill_process_remediation_message():
            return 128

        @staticmethod
        def _send_stop_service_remediation_message():
            return 129

        @staticmethod
        def _send_delete_registry_key_remediation_message():
            return 130

        @staticmethod
        def _send_delete_file_remediation_message():
            return 127

        @staticmethod
        def _get_bf_computer_by_ip():
            return get_artifact_data_2()

        @staticmethod
        def _get_bf_computer_by_file_path():
            return get_artifact_data_2()

        @staticmethod
        def _get_bf_computer_by_process_name():
            return get_artifact_data_2()

        @staticmethod
        def _get_bf_computer_by_service_name():
            return get_artifact_data_2()

        @staticmethod
        def _get_bf_computer_by_registry_key_name_value():
            return get_artifact_data_2()

        @staticmethod
        def _get_bf_computer_properties():
            return get_asset_properties()

    return MockResponse(*args)