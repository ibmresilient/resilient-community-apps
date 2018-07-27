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

def get_response_artifact_data(query_id):
    response = {'123': ('{"reportingAgents": 2, "totalResults": 2, "results": [{"computerID": 12315195, '
                        '"computerName": "bigfix.test", "subQueryID": 1, "isFailure": false, "result": "False",'
                        '"ResponseTime": 0},{"computerID": 13550086, "computerName": "DESKTOP-TUKM3HF", "subQueryID": 1, '
                        '"isFailure": true,"result": "Singular expression refers to nonexistent object.", '
                        '"ResponseTime": 1000}]}'
                        ),
                '124':  ('{"reportingAgents": 4, "totalResults": 4, "results": [{"computerID": 12315195, '
                        '"computerName": "bigfix.test-1", "subQueryID": 1, "isFailure": false, "result": "True",'
                        '"ResponseTime": 10},{"computerID": 12315196, "computerName": "bigfix.test-2", '
                        '"subQueryID": 1, "isFailure": false, "result": "True","ResponseTime": 10},'
                        '{"computerID": 12315197, "computerName": "bigfix.test-2", "subQueryID": 1, "isFailure": false,'
                        '"result": "False", "ResponseTime": 10},{"computerID": 13550086, "computerName": "DESKTOP-TUKM3HF", '
                        '"subQueryID": 1, "isFailure": true,"result": "Singular expression refers to nonexistent object.", '
                        '"ResponseTime": 1000}]}'
                        )
                }
    return response[query_id]

def get_response_text_asset_props(computer_id):

    computer_id = str(computer_id)

    response =  {'13550086': (
                            '<?xml version="1.0" encoding="UTF-8"?>'
                            '<BESAPI xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="BESAPI.xsd">'
                                '<Query Resource="if(number of property results of bes computers whose (id of it = 13550086) &lt; 10000) then((name of source analysis of property of it|&quot;Retrieved Property&quot;,name of property of it,values of it) of property results of bes computers whose(id of it = 13550086)) else error &quot;Too Many Results&quot;">'
                                    '<Result>'
                                        '<Tuple>'
                                            '<Answer type="string">Quarantine Status</Answer>'
                                            '<Answer type="string">Quarantine Status Property</Answer>'
                                            '<Answer type="string">False</Answer>'
                                        '</Tuple>'
                                        '<Tuple>'
                                            '<Answer type="string">Retrieved Property</Answer>'
                                            '<Answer type="string">Computer Name</Answer>'
                                            '<Answer type="string">DESKTOP-TUKM3HF</Answer>'
                                        '</Tuple>'
                                        '<Tuple>'
                                            '<Answer type="string">Retrieved Property</Answer>'
                                            '<Answer type="string">OS</Answer>'
                                            '<Answer type="string">Win10 10.0.15063.483 (1703)</Answer>'
                                        '</Tuple>'
                                        '<Tuple>'
                                            '<Answer type="string">Retrieved Property</Answer>'
                                            '<Answer type="string">CPU</Answer>'
                                            '<Answer type="string">2900 MHz Core i7-7820HQ</Answer>'
                                        '</Tuple>'
                                        '<Tuple>'
                                            '<Answer type="string">Retrieved Property</Answer>'
                                            '<Answer type="string">Last Report Time</Answer>'
                                            '<Answer type="string">Thu, 26 Jul 2018 16:39:10 +0000</Answer>'
                                        '</Tuple>'
                                        '<Tuple>'
                                            '<Answer type="string">Retrieved Property</Answer>'
                                            '<Answer type="string">Relay</Answer>'
                                            '<Answer type="string">bigfix.test:52311</Answer>'
                                        '</Tuple>'
                                        '<Tuple>'
                                            '<Answer type="string">Retrieved Property</Answer>'
                                            '<Answer type="string">Distance to BES Relay</Answer>'
                                            '<Answer type="string">0</Answer>'
                                        '</Tuple>'
                                        '<Tuple>'
                                            '<Answer type="string">Retrieved Property</Answer>'
                                            '<Answer type="string">BES Relay Service Installed</Answer>'
                                            '<Answer type="string"></Answer>'
                                        '</Tuple>'
                                        '<Tuple>'
                                            '<Answer type="string">Retrieved Property</Answer>'
                                            '<Answer type="string">Relay Name of Client</Answer>'
                                            '<Answer type="string">DESKTOP-TUKM3HF</Answer>'
                                        '</Tuple>'
                                        '<Tuple>'
                                            '<Answer type="string">Retrieved Property</Answer>'
                                            '<Answer type="string">DNS Name</Answer>'
                                            '<Answer type="string">DESKTOP-TUKM3HF</Answer>'
                                        '</Tuple>'
                                    '</Result>'
                                    '<Evaluation>'
                                        '<Time>144.733ms</Time>'
                                        '<Plurality>Plural</Plurality>'
                                    '</Evaluation>'
                                '</Query>'
                            '</BESAPI>'
                             ),
                 '12315195': (
                            '<?xml version="1.0" encoding="UTF-8"?>'
                            '<BESAPI xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="BESAPI.xsd">'
                                '<Query Resource="if(number of property results of bes computers whose (id of it = 12315195) &lt; 10000) then((name of source analysis of property of it|&quot;Retrieved Property&quot;,name of property of it,values of it) of property results of bes computers whose(id of it = 12315195)) else error &quot;Too Many Results&quot;">'
                                    '<Result>'
                                        '<Tuple>'
                                            '<Answer type="string">Quarantine Status</Answer>'
                                            '<Answer type="string">Quarantine Status Property</Answer>'
                                            '<Answer type="string">False</Answer>'
                                        '</Tuple>'
                                        '<Tuple>'
                                            '<Answer type="string">Retrieved Property</Answer>'
                                            '<Answer type="string">Computer Name</Answer>'
                                            '<Answer type="string">bigfix.test</Answer>'
                                        '</Tuple>'
                                        '<Tuple>'
                                            '<Answer type="string">Retrieved Property</Answer>'
                                            '<Answer type="string">OS</Answer>'
                                            '<Answer type="string">Win10 10.0.15063.483 (1703)</Answer>'
                                        '</Tuple>'
                                        '<Tuple>'
                                            '<Answer type="string">Retrieved Property</Answer>'
                                            '<Answer type="string">CPU</Answer>'
                                            '<Answer type="string">2900 MHz Core i7-7820HQ</Answer>'
                                        '</Tuple>'
                                        '<Tuple>'
                                            '<Answer type="string">Retrieved Property</Answer>'
                                            '<Answer type="string">Last Report Time</Answer>'
                                            '<Answer type="string">Thu, 26 Jul 2018 16:39:10 +0000</Answer>'
                                        '</Tuple>'
                                        '<Tuple>'
                                            '<Answer type="string">Retrieved Property</Answer>'
                                            '<Answer type="string">Relay</Answer>'
                                            '<Answer type="string">bigfix.test:52311</Answer>'
                                        '</Tuple>'
                                        '<Tuple>'
                                            '<Answer type="string">Retrieved Property</Answer>'
                                            '<Answer type="string">Distance to BES Relay</Answer>'
                                            '<Answer type="string">0</Answer>'
                                        '</Tuple>'
                                        '<Tuple>'
                                            '<Answer type="string">Retrieved Property</Answer>'
                                            '<Answer type="string">BES Relay Service Installed</Answer>'
                                            '<Answer type="string"></Answer>'
                                        '</Tuple>'
                                        '<Tuple>'
                                            '<Answer type="string">Retrieved Property</Answer>'
                                            '<Answer type="string">Relay Name of Client</Answer>'
                                            '<Answer type="string">bigfix.test</Answer>'
                                        '</Tuple>'
                                        '<Tuple>'
                                            '<Answer type="string">Retrieved Property</Answer>'
                                            '<Answer type="string">DNS Name</Answer>'
                                            '<Answer type="string">bigfix.test</Answer>'
                                        '</Tuple>'
                                    '</Result>'
                                    '<Evaluation>'
                                        '<Time>144.733ms</Time>'
                                        '<Plurality>Plural</Plurality>'
                                    '</Evaluation>'
                                '</Query>'
                            '</BESAPI>'
                            )
                }
    return response[computer_id]

def get_response_action_status_success(action_id):

    response =  {'143': (
                        '<?xml version="1.0" encoding="UTF-8"?>'
                        '<BESAPI xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="BESAPI.xsd">'
                            '<ActionResults Resource="https://192.168.56.101:52311/api/action/143/status">'
                                '<ActionID>143</ActionID>'
                                '<Status>Open</Status>'
                                '<DateIssued>Thu, 26 Jul 2018 16:39:04 +0000</DateIssued>'
                                '<Computer ID="13550086" Name="DESKTOP-TUKM3HF">'
                                    '<Status>The action executed successfully.</Status>'
                                    '<State IsError="0">3</State>'
                                    '<ExitCode>1</ExitCode>'
                                    '<ApplyCount>1</ApplyCount>'
                                    '<RetryCount>1</RetryCount>'
                                    '<LineNumber>2</LineNumber>'
                                    '<StartTime>Thu, 26 Jul 2018 16:39:10 +0000</StartTime>'
                                    '<EndTime>Thu, 26 Jul 2018 16:39:10 +0000</EndTime>'
                                '</Computer>'
                            '</ActionResults>'
                        '</BESAPI>'
                        ),
                 '144': (
                        '<?xml version="1.0" encoding="UTF-8"?>'
                        '<BESAPI xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="BESAPI.xsd">'
                            '<ActionResults Resource="https://192.168.56.101:52311/api/action/144/status">'
                            '<ActionID>144</ActionID>'
                            '<Status>Open</Status>'
                            '<DateIssued>Mon, 20 Jun 2018 14:23:35 +0000</DateIssued>'
                            '<Computer ID="12315195" Name="bigfix.test">'
                                '<Status>The Fixlet which this action addresses is not relevant on this machine.</Status>'
                                '<State IsError="0">0</State>'
                                '<ApplyCount>0</ApplyCount>'
                                '<RetryCount>0</RetryCount>'
                                '<LineNumber>0</LineNumber>'
                            '</Computer>'
                        '</ActionResults>'
                        '</BESAPI>'
                        ),
                 '145': (
                        '<?xml version="1.0" encoding="UTF-8"?>'
                        '<BESAPI xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="BESAPI.xsd">'
                            '<ActionResults Resource="https://192.168.56.101:52311/api/action/145/status">'
                                '<ActionID>145</ActionID>'
                                '<Status>Open</Status>'
                                '<DateIssued>Thu, 19 May 2018 19:40:12 +0000</DateIssued>'
                                '<Computer ID="11656281" Name="server123">'
                                    '<Status>The action failed.</Status>'
                                    '<State IsError="0">4</State>'
                                    '<ExitCode>-2147024885</ExitCode>'
                                    '<ApplyCount>1</ApplyCount>'
                                    '<RetryCount>1</RetryCount>'
                                    '<LineNumber>23</LineNumber>'
                                    '<StartTime>Thu, 19 May 2018 19:44:07 +0000</StartTime>'
                                    '<EndTime>Thu, 19 May 2018 19:44:35 +0000</EndTime>'
                                '</Computer>'
                            '</ActionResults>'
                        '</BESAPI>'
                        )
                }
    return response[action_id]


def post_response_artifact_query(action_type):
    response = {"DeleteFile": (
                                '<?xml version="1.0" encoding="UTF-8"?>'
                                '<BESAPI xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="BESAPI.xsd">'
                                '<ClientQuery Resource="http://192.168.56.101:52311/api/clientquery/142"><ID>142</ID>'
                                '</ClientQuery></BESAPI>'
                              ),
                "KillProcess": (
                                '<?xml version="1.0" encoding="UTF-8"?>'
                                '<BESAPI xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="BESAPI.xsd">'
                                '<ClientQuery Resource="http://192.168.56.101:52311/api/clientquery/144"><ID>144</ID>'
                                '</ClientQuery></BESAPI>'
                              )
               }
    return response[action_type]

def post_response_artifact_remediate(action_type):
    response = {"DeleteFile": (
                                '<?xml version="1.0" encoding="UTF-8"?>'
                                '<BESAPI xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="BESAPI.xsd">'
                                    '<Action Resource="https://192.168.56.101:52311/api/action/142" LastModified="Thu, 26 Jul 2018 15:57:48 +0000">'
                                        '<Name>Delete File /tmp/testfile.txt</Name>'
                                        '<ID>142</ID>'
                                    '</Action>'
                                '</BESAPI>'
                              ),
                "DeleteRegKey": (
                                '<?xml version="1.0" encoding="UTF-8"?>'
                                '<BESAPI xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="BESAPI.xsd">'
                                    '<Action Resource="https://192.168.56.101:52311/api/action/143" LastModified="Thu, 26 Jul 2018 15:57:48 +0000">'
                                        '<Name>Delete Registry Key HKLM\SOFTWARE\JP\JP2\com.jp.browsercore</Name>'
                                        '<ID>143</ID>'
                                    '</Action>'
                                '</BESAPI>'
                              )
    }
    return response[action_type]
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

def mocked_requests(*args, **kwargs):

    """Function will be used by the mock to replace get and post requests """
    class MockResponse:
        def __init__(self, *arg, **kwargs):
            self.status_code = 200
            if arg and "/api/query?" in arg[0]:
                computer_id = arg[0].split("id of it = ",1)[1].split(')',1)[0]
                self.text = get_response_text_asset_props(computer_id)
            elif arg and "/api/clientqueryresults/" in arg[0]:
                query_id = arg[0].split('/')[5].split('?',1)[0]
                self.text = get_response_artifact_data(query_id)
                test=1
            elif arg and "/api/clientquery" in arg[0]:
                if "exists file" in kwargs["data"]:
                    self.text = post_response_artifact_query("DeleteFile")
                elif "exists process" in kwargs["data"]:
                    self.text = post_response_artifact_query("KillProcess")
            elif arg and "/api/actions" in arg[0]:
                if "Delete File" in kwargs["data"]:
                    self.text = post_response_artifact_remediate("DeleteFile")
                elif "Delete Registry Key" in kwargs["data"]:
                    self.text = post_response_artifact_remediate("DeleteRegKey")
            elif arg and "/response_text" in arg[0]:
                self.text = get_response_text_asset_props(arg[1])
            elif arg and "/api/action" in arg[0]:
                action_id = arg[0].split('/')[5]
                self.text = get_response_action_status_success(action_id)

    return MockResponse(*args, **kwargs)
