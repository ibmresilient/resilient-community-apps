# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
"""Generate Mock responses to simulate Cisco AMP for endpoinst for Unit and function tests """
import time
import re
from requests.models import Response
UUID_PATTERN = re.compile(r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$")
# Responses for standalone tests
def get_computer():
    response = ('{"version": "v1.2.0",'
     '"metadata": {"links": {"self": "https://api.amp.cisco.com/v1/computers/00da1a57-b833-43ba-8ea2-79a5ab21908f"}},'
     '"data": {"connector_guid": "00da1a57-b833-43ba-8ea2-79a5ab21908f", "hostname": "Demo_AMP", "active": true,'
              '"links": {"computer": "https://api.amp.cisco.com/v1/computers/00da1a57-b833-43ba-8ea2-79a5ab21908f",'
                        '"trajectory": "https://api.amp.cisco.com/v1/computers/00da1a57-b833-43ba-8ea2-79a5ab21908f/trajectory",'
                        '"group": "https://api.amp.cisco.com/v1/groups/9d55c259-c960-488b-9b2d-06478fa19ee4"},'
              '"connector_version": "6.0.9.10685", "operating_system": "Windows 7, SP 1.0",'
              '"internal_ips": ["255.240.221.92"], "external_ip": "145.1.91.176",'
              '"group_guid": "9d55c259-c960-488b-9b2d-06478fa19ee4", "install_date": "2018-05-22T16:53:27Z",'
              '"network_addresses": [{"mac": "a0:28:f5:c3:71:d5", "ip": "255.240.221.92"}],'
              '"policy": {"guid": "a98a0f97-4d54-4175-9eef-b8dee9c8e74b", "name": "Audit"},'
              '"last_seen": "2018-05-22T16:53:27Z"}}'
    )
    return response

def get_computers():
    response = ('{"version": "v1.2.0", "metadata": {'
                    '"links": {"self": "https://api.amp.cisco.com/v1/computers?group_guid=4cb5b3b4-b33e-4825-98e9-97d2b5b1a4d3"},'
                    '"results": {"total": 6, "current_item_count": 4, "index": 4, "items_per_page": 500}}, '
                '"data": ['
                    '{"connector_guid": "0b471b7e-2243-40ef-8691-904627c32754", "hostname": "Demo_AMP_Exploit_Prevention_Audit",'
                     '"active": true,'
                     '"links": {"computer": "https://api.amp.cisco.com/v1/computers/0b471b7e-2243-40ef-8691-904627c32754",'
                               '"trajectory": "https://api.amp.cisco.com/v1/computers/0b471b7e-2243-40ef-8691-904627c32754/trajectory",'
                               '"group": "https://api.amp.cisco.com/v1/groups/4cb5b3b4-b33e-4825-98e9-97d2b5b1a4d3"},'
                     '"connector_version": "6.0.9.10685", "operating_system": "Windows 7, SP 1.0", "internal_ips": ["60.132.82.150"],'
                     '"external_ip": "225.216.192.205", "group_guid": "4cb5b3b4-b33e-4825-98e9-97d2b5b1a4d3",'
                     '"install_date": "2018-05-22T16:53:27Z",'
                     '"network_addresses": [{"mac": "62:56:31:9a:33:56", "ip": "60.132.82.150"}],'
                     '"policy": {"guid": "51450374-366c-4759-9099-7baa138c499f", "name": "Triage"}},'
                    '{"connector_guid": "160fb8db-331d-45d2-bd3c-38aacfd236d6", "hostname": "Demo_AMP_Threat_Quarantined",'
                     '"active": true,'
                     '"links": {"computer": "https://api.amp.cisco.com/v1/computers/160fb8db-331d-45d2-bd3c-38aacfd236d6",'
                               '"trajectory": "https://api.amp.cisco.com/v1/computers/160fb8db-331d-45d2-bd3c-38aacfd236d6/trajectory",'
                               '"group": "https://api.amp.cisco.com/v1/groups/4cb5b3b4-b33e-4825-98e9-97d2b5b1a4d3"},'
                     '"connector_version": "6.0.9.10685", "operating_system": "Windows 7, SP 1.0", "internal_ips": ["69.199.68.14"],'
                     '"external_ip": "49.221.161.222", "group_guid": "4cb5b3b4-b33e-4825-98e9-97d2b5b1a4d3",'
                     '"install_date": "2018-05-22T16:53:28Z",'
                     '"network_addresses": [{"mac": "e1:47:3d:a3:23:b0", "ip": "69.199.68.14"}],'
                     '"policy": {"guid": "51450374-366c-4759-9099-7baa138c499f", "name": "Triage"}},'
                    '{"connector_guid": "b521d75e-2340-4e7c-9f68-b40bdb236246", "hostname": "Demo_Qakbot_1", "active": true,'
                     '"links": {"computer": "https://api.amp.cisco.com/v1/computers/b521d75e-2340-4e7c-9f68-b40bdb236246",'
                               '"trajectory": "https://api.amp.cisco.com/v1/computers/b521d75e-2340-4e7c-9f68-b40bdb236246/trajectory",'
                               '"group": "https://api.amp.cisco.com/v1/groups/4cb5b3b4-b33e-4825-98e9-97d2b5b1a4d3"},'
                     '"connector_version": "6.0.9.10685", "operating_system": "Windows 7, SP 1.0", "internal_ips": ["103.8.51.69"],'
                     '"external_ip": "58.129.151.26", "group_guid": "4cb5b3b4-b33e-4825-98e9-97d2b5b1a4d3",'
                     '"install_date": "2018-05-22T16:53:25Z",'
                     '"network_addresses": [{"mac": "a1:90:19:43:1e:91", "ip": "103.8.51.69"}],'
                     '"policy": {"guid": "51450374-366c-4759-9099-7baa138c499f", "name": "Triage"}},'
                    '{"connector_guid": "daa7a764-514d-4309-9d7a-0ec4e7b136cd", "hostname": "Demo_Ramnit", "active": true,'
                     '"links": {"computer": "https://api.amp.cisco.com/v1/computers/daa7a764-514d-4309-9d7a-0ec4e7b136cd",'
                               '"trajectory": "https://api.amp.cisco.com/v1/computers/daa7a764-514d-4309-9d7a-0ec4e7b136cd/trajectory",'
                               '"group": "https://api.amp.cisco.com/v1/groups/4cb5b3b4-b33e-4825-98e9-97d2b5b1a4d3"},'
                     '"connector_version": "6.0.9.10685", "operating_system": "Windows 7, SP 1.0",'
                     '"internal_ips": ["115.222.74.181"], "external_ip": "85.215.55.144",'
                    '"group_guid": "4cb5b3b4-b33e-4825-98e9-97d2b5b1a4d3", "install_date": "2018-05-22T16:53:22Z",'
                     '"network_addresses": [{"mac": "2d:f0:67:49:86:8d", "ip": "115.222.74.181"}],'
                     '"policy": {"guid": "51450374-366c-4759-9099-7baa138c499f", "name": "Triage"}}]}'
                )
    return response




def get_activity():
    response = ('{"version":"v1.2.0", "metadata":{'
                    '"links":{"self": "https://api.amp.cisco.com/v1/computers/activity?q=SearchProtocolHost.exe"},'
                    '"results":{"total":4, "current_item_count":4, "index":0, "items_per_page":500}},'
                    '"data": ['
                        '{"connector_guid": "0df31cae-120d-4fbc-ad7f-b0e7e96c01e5", "hostname": "Demo_Dyre", "active": true,'
                         '"links": {"computer": "https://api.amp.cisco.com/v1/computers/0df31cae-120d-4fbc-ad7f-b0e7e96c01e5",'
                                   '"trajectory": "https://api.amp.cisco.com/v1/computers/0df31cae-120d-4fbc-ad7f-b0e7e96c01e5/trajectory?q=SearchProtocolHost.exe",'
                                   '"group": "https://api.amp.cisco.com/v1/groups/b077d6bc-bbdf-42f7-8838-a06053fbd98a"}'
                        '},'
                        '{"connector_guid": "8c7c18d3-c1b4-4fa8-8d46-b6e467cdbae8", "hostname": "Demo_Upatre", "active": true,'
                         '"links": {"computer": "https://api.amp.cisco.com/v1/computers/8c7c18d3-c1b4-4fa8-8d46-b6e467cdbae8",'
                                   '"trajectory": "https://api.amp.cisco.com/v1/computers/8c7c18d3-c1b4-4fa8-8d46-b6e467cdbae8/trajectory?q=SearchProtocolHost.exe",'
                                   '"group": "https://api.amp.cisco.com/v1/groups/b077d6bc-bbdf-42f7-8838-a06053fbd98a"}'
                        '},'
                        '{"connector_guid": "ad29d359-dac9-4940-9c7e-c50e6d32ee6f", "hostname": "Demo_CozyDuke", "active": true,'
                         '"links": {"computer": "https://api.amp.cisco.com/v1/computers/ad29d359-dac9-4940-9c7e-c50e6d32ee6f",'
                                   '"trajectory": "https://api.amp.cisco.com/v1/computers/ad29d359-dac9-4940-9c7e-c50e6d32ee6f/trajectory?q=SearchProtocolHost.exe",'
                                   '"group": "https://api.amp.cisco.com/v1/groups/b077d6bc-bbdf-42f7-8838-a06053fbd98a"}'
                        '},'
                        '{"connector_guid": "af73d9d5-ddc5-4c93-9c6d-d5e6b5c5eb01", "hostname": "WIN-S1AC1PI6L5L", "active": true,'
                         '"links": {"computer": "https://api.amp.cisco.com/v1/computers/af73d9d5-ddc5-4c93-9c6d-d5e6b5c5eb01",'
                                   '"trajectory": "https://api.amp.cisco.com/v1/computers/af73d9d5-ddc5-4c93-9c6d-d5e6b5c5eb01/trajectory?q=SearchProtocolHost.exe",'
                                   '"group": "https://api.amp.cisco.com/v1/groups/b077d6bc-bbdf-42f7-8838-a06053fbd98a"}'
                        '}'
                    ']'
                '}'
    )
    return response

def get_computer_trajectory():
    response = ('{"version": "v1.2.0", "metadata": {'
                 '"links": {"self": "https://api.amp.cisco.com/v1/computers/ad29d359-dac9-4940-9c7e-c50e6d32ee6f/trajectory"}},'
                    '"data": {'
                        '"computer": {"connector_guid": "ad29d359-dac9-4940-9c7e-c50e6d32ee6f", "hostname": "Demo_CozyDuke", "active": true,'
                                     '"links": {'
                                        '"computer": "https://api.amp.cisco.com/v1/computers/ad29d359-dac9-4940-9c7e-c50e6d32ee6f",'
                                        '"trajectory": "https://api.amp.cisco.com/v1/computers/ad29d359-dac9-4940-9c7e-c50e6d32ee6f/trajectory",'
                                        '"group": "https://api.amp.cisco.com/v1/groups/b077d6bc-bbdf-42f7-8838-a06053fbd98a"},'
                                    '"connector_version": "4.1.7.10201", "operating_system": "Windows 7, SP 1.0",'
                                    '"internal_ips": ["87.27.44.37"],'
                                    '"external_ip": "93.111.140.204",'
                                    '"group_guid": "b077d6bc-bbdf-42f7-8838-a06053fbd98a", "install_date": "2016-05-20T19:20:00Z",'
                                    '"network_addresses": [{"mac": "09:de:6b:a8:74:10", "ip": "87.27.44.37"}],'
                                    '"policy": {"guid": "89912c9e-8dbd-4c2b-a1d8-dee8a0c2bb29", "name": "Audit Policy"}},'
                        '"events": [{"timestamp": 1502989429,'
                                    '"timestamp_nanoseconds": 659151942,'
                                    '"date": "2017-08-17T17:03:49+00:00",'
                                    '"event_type": "NFM",'
                                    '"group_guids": ["b077d6bc-bbdf-42f7-8838-a06053fbd98a"],'
                                    '"network_info": { "dirty_url": "http://www.sanjosemaristas.com/app/index.php?", "remote_ip": "188.120.225.17",'
                                                      '"remote_port": 80, "local_ip": "192.168.1.3", "local_port": 54233,'
                                                      '"nfm": {"direction": "Outgoing connection from", "protocol": "TCP"},'
                                                      '"parent": {"disposition": "Clean", '
                                                                 '"identity": {"sha256": "5ad3c37e6f2b9db3ee8b5aeedc474645de90c66e3d95f8620c48102f1eba4124"}'
                                                      '}'
                                                    '}'
                                   '},'
                                   '{"timestamp": 1502989426,'
                                    '"timestamp_nanoseconds": 155931927,'
                                    '"date": "2017-08-17T17:03:46+00:00",'
                                    '"event_type": "NFM",'
                                    '"group_guids": ["b077d6bc-bbdf-42f7-8838-a06053fbd98a"],'
                                    '"network_info": {"dirty_url": "http://www.sanjosemaristas.com/app/index.php?", "remote_ip": "188.120.225.17",'
                                                 '"remote_port": 80, "local_ip": "192.168.1.3", "local_port": 54232,'
                                                 '"nfm": { "direction": "Outgoing connection from","protocol": "TCP"},'
                                                 '"parent": { "disposition": "Clean",'
                                                             '"identity": {"sha256": "5ad3c37e6f2b9db3ee8b5aeedc474645de90c66e3d95f8620c48102f1eba4124"}'
                                                           '}'
                                                '}'
                                   '}'
                                  ']'
                    '}'
                '}'
    )
    return response

def get_file_lists():

    response = ('{"version": "v1.2.0", '
                '"data": ['
                    '{"guid": "9710a198-b95a-462a-b184-9e688968fd94", "type": "simple_custom_detections",'
                     '"name": "File Blacklist",'
                     '"links": {"file_list": "https://api.amp.cisco.com/v1/file_lists/9710a198-b95a-462a-b184-9e688968fd94"}}],'
                 '"metadata": {"results": {"index": 0, "total": 1, "items_per_page": 500, "current_item_count": 1},'
                              '"links": {"self": "https://api.amp.cisco.com/v1/file_lists/simple_custom_detections"}}'
                '}'
    )
    return response

def get_file_list_files(sha256):

    if sha256:
        k = "s256"
    else:
        k = "None"

    response = {"None": ('{"version": "v1.2.0",'
                         '"data": {"items": [], "guid": "9710a198-b95a-462a-b184-9e688968fd94", "name": "File Blacklist", "policies": ['
                               ' {"guid": "a98a0f97-4d54-4175-9eef-b8dee9c8e74b", "name": "Audit",'
                                 '"links": {"policy": "https://api.amp.cisco.com/v1/policies/a98a0f97-4d54-4175-9eef-b8dee9c8e74b"}},'
                                '{"guid": "fdf4c7f9-b0de-41bf-9d86-d0fae7aa5267", "name": "Audit",'
                                 '"links": {"policy": "https://api.amp.cisco.com/v1/policies/fdf4c7f9-b0de-41bf-9d86-d0fae7aa5267"}},'
                                '{"guid": "99a9d07e-59a3-41d4-a9d7-c73c0cd43bae", "name": "Audit",'
                                 '"links": {"policy": "https://api.amp.cisco.com/v1/policies/99a9d07e-59a3-41d4-a9d7-c73c0cd43bae"}},'
                                '{"guid": "175c473a-7942-4cf2-877d-6fdd476f0b9a", "name": "Domain Controller",'
                                 '"links": {"policy": "https://api.amp.cisco.com/v1/policies/175c473a-7942-4cf2-877d-6fdd476f0b9a"}},'
                                '{"guid": "7aac0dca-7782-414f-b19b-83dec31ea131", "name": "Protect",'
                                 '"links": {"policy": "https://api.amp.cisco.com/v1/policies/7aac0dca-7782-414f-b19b-83dec31ea131"}},'
                                '{"guid": "abc537e0-d0fa-4a20-aefe-a50bf17cef2a", "name": "Protect",'
                                 '"links": {"policy": "https://api.amp.cisco.com/v1/policies/abc537e0-d0fa-4a20-aefe-a50bf17cef2a"}},'
                                '{"guid": "aef1226d-1df1-400f-8791-4db8f9b2eee3", "name": "Protect",'
                                 '"links": {"policy": "https://api.amp.cisco.com/v1/policies/aef1226d-1df1-400f-8791-4db8f9b2eee3"}},'
                                '{"guid": "1945af96-2026-4f77-805d-59565079ec88", "name": "Server",'
                                 '"links": {"policy": "https://api.amp.cisco.com/v1/policies/1945af96-2026-4f77-805d-59565079ec88"}},'
                                '{"guid": "51450374-366c-4759-9099-7baa138c499f", "name": "Triage",'
                                 '"links": {"policy": "https://api.amp.cisco.com/v1/policies/51450374-366c-4759-9099-7baa138c499f"}},'
                                '{"guid": "3b27e1e3-cde3-4750-a571-031ae4e111bc", "name": "Triage",'
                                 '"links": {"policy": "https://api.amp.cisco.com/v1/policies/3b27e1e3-cde3-4750-a571-031ae4e111bc"}}]'
                                '},'
                         '"metadata": {"results": {"index": 10, "total": 1, "items_per_page": 500, "current_item_count": 0},'
                                      '"links": {"self": "https://api.amp.cisco.com/v1/file_lists/e773a9eb-296c-40df-98d8-bed46322589d/files"}}'
                         '}'
                        ),
                "s256": ('{"version": "v1.2.0",'
                          '"data": { "sha256": "e93faae7706644387cd3383aaf1bd9919f9f441acce498f15391eb60eb54288b",'
                                    '"source": "Created by entering SHA-256 via Public api.",'
                                    '"links": {'
                                        '"file_list": "https://api.amp.cisco.com/v1/file_lists/e773a9eb-296c-40df-98d8-bed46322589d"}'
                           '},'
                          '"metadata": {'
                            '"links": {"self": "https://api.amp.cisco.com/v1/file_lists/e773a9eb-296c-40df-98d8-bed46322589d/files/e93faae7706644387cd3383aaf1bd9919f9f441acce498f15391eb60eb54288b"}'
                          '}'
                         '}'
                        )
               }

    return response[k]

def mocked_amp_client(*args):

    class MockResponse:
        """Class will be used by the mock to replace amp_client in circuits tests"""
        def __init__(self, *arg):
            self.r = Response()

        def __contains__(self, key):
            return True if key in self.__dict__.keys() else False

        def get_computers(self, group_guid=None, limit=None, hostname=None, internal_ip=None, external_ip=None):
            self.r._content = get_computers()
            return self.r.json()

        def get_computer(self, connector_guid):
            self.r._content = get_computer()
            return self.r.json()

        def get_computer_trajectory(self, connector_guid, limit=None):
            self.r._content = get_computer_trajectory()
            return self.r.json()

        def get_activity(self, q, limit=None, offset=None):
            self.r._content = get_activity()
            return self.r.json()

        def get_file_lists(self, name, limit=None, offset=None):
            self.r._content = get_file_lists()
            return self.r.json()

        def get_file_list_files(self, file_list_guid, sha256, limit=None, offset=None):
            self.r._content = get_file_list_files(bool(sha256))
            return self.r.json()

    return MockResponse(*args)

def mocked_session(*args, **kwargs):
    class MockSession:
        """Class will be used by the mock to replace get and post requests in standalone tests"""
        def __init__(self, *arg, **kwargs):
            self.status_code = 200

        def raise_for_status(self):
            pass

        def get(self, url, **kwargs):

            if url == "/v1/computers/":
                return MockGetResponse(get_computers(), 200)
            elif re.match("^/v1/computers/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$", url):
                return MockGetResponse(get_computer(), 200)
            elif re.match("^/v1/computers/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/trajectory/$", url):
                return MockGetResponse(get_computer_trajectory(), 200)
            elif url == "/v1/computers/activity":
                return MockGetResponse(get_activity(), 200)
            elif url == "/v1/file_lists/simple_custom_detections":
                return MockGetResponse(get_file_lists(), 200)
            elif re.match("^/v1/file_lists/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/files$", url):
                return MockGetResponse(get_file_list_files(False), 200)
            elif re.match("^/v1/file_lists/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/files/[a-fA-F0-9]{64}$", url):
                return MockGetResponse(get_file_list_files(True), 200)
            else:
                return MockGetResponse(None, 404)
    return MockSession(*args, **kwargs)

class MockGetResponse:
    """Class will be used by the mock to replace get and post requests in standalone tests"""
    def __init__(self, *args, **kwargs):
        self.r = Response()
        self.r._content = args[0]
        self.r.status_code = args[1]
        test=1

    def json(self):
        return self.r.json()

    def raise_for_status(self):
        pass

def get_mock_config():
    config_data = u"""[fn_cisco_amp4ep]
base_url=https://api.amp.cisco.com/
api_version=v1
# The client id will be generated on the Cisco AMP for endpoints dashboard.
client_id=01234abcde56789efedc
# The api_token will be generated on the Cisco AMP for endpoints dashboard and will be will be in uuid format.
api_token=abcd1234-a123-123a-123a-123456abcdef
"""
    return config_data