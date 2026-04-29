# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

"""Generate Mock responses to simulate Symantec SEP for Unit and function tests """
import re
import json
from sys import version_info
from requests import HTTPError
from requests.models import Response
import os

TESTS_DIR = os.path.dirname(os.path.realpath(__file__))
MOCK_ZIP = os.path.join(TESTS_DIR, "mock.zip")

# Responses for standalone tests
def get_fingerprint_list():

    return {"description": "Hash of type Malware MD5 Hash", "hashType": "MD5", "source": "WEBSERVICE",
                "groupIds": [], "data": ["582F9B6E0CC4C1DBBD772AAAF088CB3A"], "id": "B5F9985ED6C449A6905A0D570A5733FC",
                "name": "Blacklist"}

def add_fingerprint_list():
    return {"id": "B5F9985ED6C449A6905A0D570A5733FC"}

def delete_fingerprint_list():
    return ""

def update_fingerprint_list():
    return ""

def assign_fingerprint_list_to_group():
    return ""

def get_token():
    return "abcd1234-a123-123a-123a-123456abcdef"

def get_version():
    return {'version': '14.2.1031.0100', 'API_SEQUENCE': '181118008', 'API_VERSION': '1.0.0'}

def get_domains():
    return [{'enable': True, 'description': None, 'administratorCount': 1, 'companyName': '',
                 'createdTime': 1548481071820, 'contactInfo': None, 'id': '908090000946C25D330E919313D23887',
                 'name': 'Default'},
                {'enable': True, 'description': None, 'administratorCount': 1, 'companyName': 'Resilient',
                 'createdTime': 1550680668947, 'contactInfo': '', 'id': 'A9B4B7160946C25D24B6AA458EF5557F',
                 'name': 'JP_test_Domain'}]

def get_computers(type):
    response = {"all": ({'sort': [{'direction': 'ASC', 'property': 'COMPUTER_NAME', 'ascending': True}], 'number': 0, 'firstPage': True,
                          'content': [{'profileVersion': '14.2.1031', 'elamOnOff': 1, 'avEngineOnOff': 1, 'profileChecksum': None, 'atpDeviceId': None, 'processorType': 'Intel64 Family 6 Model 15 Stepping 1', 'oslanguage': 'en-US', 'licenseId': None, 'licenseStatus': -1, 'group': {'domain': {'id': '908090000946C25D330E919313D23887', 'name': 'Default'}, 'name': 'My Company', 'fullPathName': None, 'externalReferenceId': None, 'source': None, 'id': 'CAD80F000946C25D6C150831060AA326'}, 'uuid': 'EA650B42-D10A-7F9F-A1D2-0A58C4F4CEB1', 'groupUpdateProvider': False, 'edrStatus': 0, 'freeDisk': 52481970176, 'diskDrive': 'C:\\', 'osFunction': 'Server', 'processorClock': 2394, 'mobilePhone': '', 'jobTitle': '', 'lastHeuristicThreatTime': 0, 'osname': 'Windows Server 2012', 'winServers': ['0.0.0.0', '0.0.0.0'], 'deploymentMessage': '', 'idsSerialNo': '', 'employeeNumber': '', 'snacLicenseId': None, 'lastSiteId': 'EE75B0850946C25D5287B58B5173A37C', 'uwf': 2, 'currentClientId': '256B2B130946C25D40C83823AA2E5D4C', 'osbitness': 'x64', 'lastScanTime': 1552465622000, 'email': '', 'securityVirtualAppliance': None, 'worstInfectionIdx': '0', 'encryptedDevicePassword': None, 'lastServerId': '7D6AAA6F0946C25D170B3A2D442500B6', 'kernel': None, 'lastUpdateTime': 1552471481568, 'ptpOnOff': 1, 'majorVersion': 14, 'lastConnectedIpAddr': '192.168.194.93', 'agentVersion': '14.2.1031.0100', 'deploymentRunningVersion': '14.2.1031.0100', 'agentTimeStamp': 1552471481568, 'osfunction': 'Server', 'osMajor': 6, 'deploymentTargetVersion': '14.2.1031.0100', 'osMinor': 2, 'osFlavorNumber': 79, 'logicalCpus': 0, 'deploymentPreVersion': '', 'hypervisorVendorId': '0', 'fbwf': 2, 'osversion': '6.2', 'dnsServers': ['192.168.192.29', 'FEC0:0000:0000:FFFF:0000:0000:0000:0001'], 'vsicStatus': 3, 'deleted': 0, 'deploymentStatus': '302456832', 'computerTimeStamp': 1552388971500, 'bwf': 2, 'totalDiskSpace': 81567, 'homePhone': '', 'daOnOff': 1, 'computerDescription': '', 'pepOnOff': 1, 'bashStatus': 1, 'agentUsn': 942822, 'osName': 'Windows Server 2012', 'patternIdx': '3F95B8098B9EEF1883B013F91C43AC72', 'employeeStatus': '', 'tmpDevice': None, 'rebootRequired': 0, 'subnetMasks': ['255.255.255.0', '64'], 'minorVersion': 2, 'osservicePack': '', 'lastSiteName': 'My Site', 'cidsEngineVersion': '0.0.0.0', 'lastDeploymentTime': 1550585147000, 'isGrace': 0, 'computerUsn': 921686, 'agentId': '6E5AA5CB0946C25D40C83823BB5107E6', 'cidsBrowserFfOnOff': 1, 'domainOrWorkgroup': 'WORKGROUP', 'svaId': None, 'loginDomain': 'LocalComputer', 'lastServerName': 'WIN-4OA0GKJN830', 'contentUpdate': 1, 'writeFiltersStatus': None, 'infected': 0, 'memory': 6441979904, 'osminor': 2, 'freeMem': 1933389824, 'officePhone': '', 'lastVirusTime': 1551350764000, 'telemetryMid': '890E283B-41D3-4340-A397-66F6AFCAF33E', 'idsVersion': '', 'cidsBrowserIeOnOff': 1, 'publicKey': 'BgIAAACkAABSU0ExAAgAAAEAAQDfMtYpvbC2ZOrpGFbK76tuyp2MZ7/6EGsFrqAV3ZBMfvMllksVObpPYvDSc5vCjtzthb1301VADLAspayGytsdAj5z8+LLpOnJkHNg9tIunm1lLkBTitevI6G+nNjyKd7uPn3+bxjk1LL8g1exL2C2SMPEXubdUa1N5xwmhhPHp6PSIAjY74QUcNyplfvylMS9QRWoQ70mqNy9tLLef6+qCYWTqGa7QKXS0WUJs8sJMzWfCrpeMVAmU5/s3yEu+OI+9RKgOeSfy7wRzmAWHQTofjHkYGYqwXcwwLX7AbWjdcpYo0Kaecf8e5t2ZvWyR362EaNxn0HYSjpKraY1hLK1', 'quarantineDesc': 'Host Integrity check is disabled.\n Host Integrity policy has been disabled by the administrator.', 'cidsDrvMulfCode': 0, 'biosVersion': 'INTEL  - 6040000 PhoenixBIOS 4.0 Release 6.0', 'rebootReason': '', 'telemetryHwid': 'A942D8EB-32C3-E42F-FE83-723FDC431F32', 'cidsSilentMode': 0, 'creationTime': 1550585043812, 'macAddresses': ['00-50-56-8B-A6-C3', '00-50-56-8B-A6-C3'], 'idsChecksum': None, 'operatingSystem': 'Windows Server 2012 ', 'osmajor': 6, 'virtualizationPlatform': 'Unknown', 'ipAddresses': ['192.168.194.93', 'FE80:0000:0000:0000:FC67:074E:CD22:0188'], 'physicalCpus': 1, 'osBitness': 'x64', 'cidsDefsetVersion': '190312061', 'cidsDrvOnOff': 1, 'computerName': 'WIN-4OA0GKJN830', 'logonUserName': 'Administrator', 'licenseExpiry': 0, 'osLanguage': 'en-US', 'gateways': ['192.168.194.1', '192.168.194.1', '0.0.0.0', '0.0.0.0'], 'uniqueId': 'D31AA16E0946C25D40C83823C500518B', 'department': '', 'isNpvdiClient': 0, 'dhcpServer': '0.0.0.0', 'description': '', 'osflavorNumber': 79, 'tpmDevice': '0', 'onlineStatus': 1, 'lastDownloadTime': 1551772684595, 'apOnOff': 1, 'timeZone': 480, 'fullName': '', 'osVersion': '6.2', 'attributeExtension': '', 'atpServer': '', 'tamperOnOff': 1, 'osServicePack': '', 'agentType': '105', 'serialNumber': 'VMware-42 0b 65 ea 0a d1 9f 7f-a1 d2 0a 58 c4 f4 ce b1', 'osElamStatus': 0, 'installType': '0', 'profileSerialNo': 'CAD8-01/26/2019 08:00:11 062', 'hardwareKey': '1771D79454E53469DF4B290C06C104C9', 'firewallOnOff': 1},
                            {'profileVersion': '14.2.1031', 'elamOnOff': 1, 'avEngineOnOff': 1, 'profileChecksum': None, 'atpDeviceId': None, 'processorType': 'Intel64 Family 6 Model 15 Stepping 1', 'oslanguage': 'en-US', 'licenseId': None, 'licenseStatus': -1, 'group': {'domain': {'id': '908090000946C25D330E919313D23887', 'name': 'Default'}, 'name': 'My Company\\Group_2', 'fullPathName': None, 'externalReferenceId': None, 'source': None, 'id': 'CC00A6170946C25D35BD115E41F2F92C'}, 'uuid': '87400B42-6E1A-D457-D45F-9804C4295C33', 'groupUpdateProvider': False, 'edrStatus': 0, 'freeDisk': 72927236096, 'diskDrive': 'c:\\', 'osFunction': 'Server', 'processorClock': 2394, 'mobilePhone': '', 'jobTitle': '', 'lastHeuristicThreatTime': 0, 'osname': 'Windows Server 2012', 'winServers': ['0.0.0.0', '0.0.0.0'], 'deploymentMessage': '', 'idsSerialNo': '', 'employeeNumber': '', 'snacLicenseId': None, 'lastSiteId': 'EE75B0850946C25D5287B58B5173A37C', 'uwf': 2, 'currentClientId': 'D4B78D1E0946C25D25E6C0981F256F40', 'osbitness': 'x64', 'lastScanTime': 1552462444000, 'email': '', 'securityVirtualAppliance': None, 'worstInfectionIdx': '0', 'encryptedDevicePassword': None, 'lastServerId': '7D6AAA6F0946C25D170B3A2D442500B6', 'kernel': None, 'lastUpdateTime': 1552471481568, 'ptpOnOff': 1, 'majorVersion': 14, 'lastConnectedIpAddr': '192.168.194.93', 'agentVersion': '14.2.1031.0100', 'deploymentRunningVersion': '14.2.1031.0100', 'agentTimeStamp': 1552471481568, 'osfunction': 'Server', 'osMajor': 6, 'deploymentTargetVersion': '14.2.1031.0100', 'osMinor': 2, 'osFlavorNumber': 79, 'logicalCpus': 0, 'deploymentPreVersion': '14.2.1031.0100', 'hypervisorVendorId': '0', 'fbwf': 2, 'osversion': '6.2', 'dnsServers': ['192.168.192.29', 'FEC0:0000:0000:FFFF:0000:0000:0000:0001'], 'vsicStatus': 3, 'deleted': 0, 'deploymentStatus': '302456832', 'computerTimeStamp': 1552407060917, 'bwf': 2, 'totalDiskSpace': 81567, 'homePhone': '', 'daOnOff': 1, 'computerDescription': '', 'pepOnOff': 1, 'bashStatus': 1, 'agentUsn': 943464, 'osName': 'Windows Server 2012', 'patternIdx': '3F95B8098B9EEF1883B013F91C43AC72', 'employeeStatus': '', 'tmpDevice': None, 'rebootRequired': 0, 'subnetMasks': ['255.255.255.0', '64'], 'minorVersion': 2, 'osservicePack': '', 'lastSiteName': 'My Site', 'cidsEngineVersion': '0.0.0.0', 'lastDeploymentTime': 1551280983000, 'isGrace': 0, 'computerUsn': 927295, 'agentId': '9530C0C30946C25D25E6C0988CF4F010', 'cidsBrowserFfOnOff': 1, 'domainOrWorkgroup': 'WORKGROUP', 'svaId': None, 'loginDomain': 'LocalComputer', 'lastServerName': 'WIN-4OA0GKJN830', 'contentUpdate': 1, 'writeFiltersStatus': None, 'infected': 0, 'memory': 4294496256, 'osminor': 2, 'freeMem': 2906599424, 'officePhone': '', 'lastVirusTime': 1551350382000, 'telemetryMid': 'E4DCBEAE-DCCD-476C-8ECA-AEE154F0F59F', 'idsVersion': '', 'cidsBrowserIeOnOff': 1, 'publicKey': 'BgIAAACkAABSU0ExAAgAAAEAAQAJWLeDFz6umLcsiKYxkbg+rl84pfQyjNVvzcC8dI6fqa8OzmMsuyMlDm2ShYAeNr7WkPLtDnfT/WoVDNQCHqLqgtRIZsYtWMUFLMXoq/u4RaThVlHEZiLS+tLDEcWWz/Iv75B2+5seHbeSV0/ZTVbYHLzRbTQnMetlbmKrvKXxoc1Aw5pKzTGeqqpTXczFEvLHIpHNp0SlbmPymGA5xag71CebfSLJfOu7YP2gMnnWLRPb1OTN3y0LQ0XQfTqOVNpwV8k5wJ52BRmwXSkY6HcvCQdX6GX/daV9kF3UBvd63rcau3tQI8n+GUr9rPDUlrnqYx5yWHoQI1jessq3darP', 'quarantineDesc': 'Host Integrity check is disabled.\n Host Integrity policy has been disabled by the administrator.', 'cidsDrvMulfCode': 0, 'biosVersion': 'INTEL  - 6040000 PhoenixBIOS 4.0 Release 6.0', 'rebootReason': '', 'telemetryHwid': '0414501C-2CC1-F574-8DAF-57BBCB2E0F34', 'cidsSilentMode': 0, 'creationTime': 1549052275576, 'macAddresses': ['00-50-56-8B-0F-88', '00-50-56-8B-0F-88'], 'idsChecksum': None, 'operatingSystem': 'Windows Server 2012 ', 'osmajor': 6, 'virtualizationPlatform': 'Unknown', 'ipAddresses': ['192.168.194.93', 'FE80:0000:0000:0000:C180:8DB8:60AF:EFEC'], 'physicalCpus': 1, 'osBitness': 'x64', 'cidsDefsetVersion': '190312061', 'cidsDrvOnOff': 1, 'computerName': 'WIN-N5KGH4CP3N3', 'logonUserName': 'Administrator', 'licenseExpiry': 0, 'osLanguage': 'en-US', 'gateways': ['192.168.194.1', '192.168.194.1', '0.0.0.0', '0.0.0.0'], 'uniqueId': '89AD1BBB0946C25D25E6C0984E971D8A', 'department': '', 'isNpvdiClient': 0, 'dhcpServer': '0.0.0.0', 'description': '', 'osflavorNumber': 79, 'tpmDevice': '0', 'onlineStatus': 1, 'lastDownloadTime': 1551280968098, 'apOnOff': 1, 'timeZone': 480, 'fullName': '', 'osVersion': '6.2', 'attributeExtension': '', 'atpServer': '', 'tamperOnOff': 1, 'osServicePack': '', 'agentType': '105', 'serialNumber': 'VMware-42 0b 40 87 1a 6e 57 d4-d4 5f 98 04 c4 29 5c 33', 'osElamStatus': 0, 'installType': '0', 'profileSerialNo': 'CC00-03/05/2019 11:50:56 570', 'hardwareKey': 'DC7D24D6465566D2941F35BC8D17801E', 'firewallOnOff': 1}],
                          'lastPage': True, 'totalPages': 1, 'size': 20, 'totalElements': 2, 'numberOfElements': 2}
                        ),
                "hostname": ({'sort': [{'direction': 'ASC', 'property': 'COMPUTER_NAME', 'ascending': True}], 'number': 0, 'firstPage': True,
                          'content': [{'profileVersion': '14.2.1031', 'elamOnOff': 1, 'avEngineOnOff': 1, 'profileChecksum': None, 'atpDeviceId': None, 'processorType': 'Intel64 Family 6 Model 15 Stepping 1', 'oslanguage': 'en-US', 'licenseId': None, 'licenseStatus': -1, 'group': {'domain': {'id': '908090000946C25D330E919313D23887', 'name': 'Default'}, 'name': 'My Company', 'fullPathName': None, 'externalReferenceId': None, 'source': None, 'id': 'CAD80F000946C25D6C150831060AA326'}, 'uuid': 'EA650B42-D10A-7F9F-A1D2-0A58C4F4CEB1', 'groupUpdateProvider': False, 'edrStatus': 0, 'freeDisk': 52481970176, 'diskDrive': 'C:\\', 'osFunction': 'Server', 'processorClock': 2394, 'mobilePhone': '', 'jobTitle': '', 'lastHeuristicThreatTime': 0, 'osname': 'Windows Server 2012', 'winServers': ['0.0.0.0', '0.0.0.0'], 'deploymentMessage': '', 'idsSerialNo': '', 'employeeNumber': '', 'snacLicenseId': None, 'lastSiteId': 'EE75B0850946C25D5287B58B5173A37C', 'uwf': 2, 'currentClientId': '256B2B130946C25D40C83823AA2E5D4C', 'osbitness': 'x64', 'lastScanTime': 1552465622000, 'email': '', 'securityVirtualAppliance': None, 'worstInfectionIdx': '0', 'encryptedDevicePassword': None, 'lastServerId': '7D6AAA6F0946C25D170B3A2D442500B6', 'kernel': None, 'lastUpdateTime': 1552471481568, 'ptpOnOff': 1, 'majorVersion': 14, 'lastConnectedIpAddr': '192.168.194.93', 'agentVersion': '14.2.1031.0100', 'deploymentRunningVersion': '14.2.1031.0100', 'agentTimeStamp': 1552471481568, 'osfunction': 'Server', 'osMajor': 6, 'deploymentTargetVersion': '14.2.1031.0100', 'osMinor': 2, 'osFlavorNumber': 79, 'logicalCpus': 0, 'deploymentPreVersion': '', 'hypervisorVendorId': '0', 'fbwf': 2, 'osversion': '6.2', 'dnsServers': ['192.168.192.29', 'FEC0:0000:0000:FFFF:0000:0000:0000:0001'], 'vsicStatus': 3, 'deleted': 0, 'deploymentStatus': '302456832', 'computerTimeStamp': 1552388971500, 'bwf': 2, 'totalDiskSpace': 81567, 'homePhone': '', 'daOnOff': 1, 'computerDescription': '', 'pepOnOff': 1, 'bashStatus': 1, 'agentUsn': 942822, 'osName': 'Windows Server 2012', 'patternIdx': '3F95B8098B9EEF1883B013F91C43AC72', 'employeeStatus': '', 'tmpDevice': None, 'rebootRequired': 0, 'subnetMasks': ['255.255.255.0', '64'], 'minorVersion': 2, 'osservicePack': '', 'lastSiteName': 'My Site', 'cidsEngineVersion': '0.0.0.0', 'lastDeploymentTime': 1550585147000, 'isGrace': 0, 'computerUsn': 921686, 'agentId': '6E5AA5CB0946C25D40C83823BB5107E6', 'cidsBrowserFfOnOff': 1, 'domainOrWorkgroup': 'WORKGROUP', 'svaId': None, 'loginDomain': 'LocalComputer', 'lastServerName': 'WIN-4OA0GKJN830', 'contentUpdate': 1, 'writeFiltersStatus': None, 'infected': 0, 'memory': 6441979904, 'osminor': 2, 'freeMem': 1933389824, 'officePhone': '', 'lastVirusTime': 1551350764000, 'telemetryMid': '890E283B-41D3-4340-A397-66F6AFCAF33E', 'idsVersion': '', 'cidsBrowserIeOnOff': 1, 'publicKey': 'BgIAAACkAABSU0ExAAgAAAEAAQDfMtYpvbC2ZOrpGFbK76tuyp2MZ7/6EGsFrqAV3ZBMfvMllksVObpPYvDSc5vCjtzthb1301VADLAspayGytsdAj5z8+LLpOnJkHNg9tIunm1lLkBTitevI6G+nNjyKd7uPn3+bxjk1LL8g1exL2C2SMPEXubdUa1N5xwmhhPHp6PSIAjY74QUcNyplfvylMS9QRWoQ70mqNy9tLLef6+qCYWTqGa7QKXS0WUJs8sJMzWfCrpeMVAmU5/s3yEu+OI+9RKgOeSfy7wRzmAWHQTofjHkYGYqwXcwwLX7AbWjdcpYo0Kaecf8e5t2ZvWyR362EaNxn0HYSjpKraY1hLK1', 'quarantineDesc': 'Host Integrity check is disabled.\n Host Integrity policy has been disabled by the administrator.', 'cidsDrvMulfCode': 0, 'biosVersion': 'INTEL  - 6040000 PhoenixBIOS 4.0 Release 6.0', 'rebootReason': '', 'telemetryHwid': 'A942D8EB-32C3-E42F-FE83-723FDC431F32', 'cidsSilentMode': 0, 'creationTime': 1550585043812, 'macAddresses': ['00-50-56-8B-A6-C3', '00-50-56-8B-A6-C3'], 'idsChecksum': None, 'operatingSystem': 'Windows Server 2012 ', 'osmajor': 6, 'virtualizationPlatform': 'Unknown', 'ipAddresses': ['192.168.194.93', 'FE80:0000:0000:0000:FC67:074E:CD22:0188'], 'physicalCpus': 1, 'osBitness': 'x64', 'cidsDefsetVersion': '190312061', 'cidsDrvOnOff': 1, 'computerName': 'WIN-4OA0GKJN830', 'logonUserName': 'Administrator', 'licenseExpiry': 0, 'osLanguage': 'en-US', 'gateways': ['192.168.194.1', '192.168.194.1', '0.0.0.0', '0.0.0.0'], 'uniqueId': 'D31AA16E0946C25D40C83823C500518B', 'department': '', 'isNpvdiClient': 0, 'dhcpServer': '0.0.0.0', 'description': '', 'osflavorNumber': 79, 'tpmDevice': '0', 'onlineStatus': 1, 'lastDownloadTime': 1551772684595, 'apOnOff': 1, 'timeZone': 480, 'fullName': '', 'osVersion': '6.2', 'attributeExtension': '', 'atpServer': '', 'tamperOnOff': 1, 'osServicePack': '', 'agentType': '105', 'serialNumber': 'VMware-42 0b 65 ea 0a d1 9f 7f-a1 d2 0a 58 c4 f4 ce b1', 'osElamStatus': 0, 'installType': '0', 'profileSerialNo': 'CAD8-01/26/2019 08:00:11 062', 'hardwareKey': '1771D79454E53469DF4B290C06C104C9', 'firewallOnOff': 1}],
                          'lastPage': True, 'totalPages': 1, 'size': 20, 'totalElements': 1, 'numberOfElements': 1}
                        ),
                "non-compliant": ({'sort': [{'direction': 'ASC', 'property': 'COMPUTER_NAME', 'ascending': True}], 'number': 0, 'firstPage': True,
                          'content': [{'profileVersion': '14.2.1031', 'elamOnOff': 0, 'avEngineOnOff': 1, 'profileChecksum': None, 'atpDeviceId': None, 'processorType': 'Intel64 Family 6 Model 15 Stepping 1', 'oslanguage': 'en-US', 'licenseId': None, 'licenseStatus': -1, 'group': {'domain': {'id': '908090000946C25D330E919313D23887', 'name': 'Default'}, 'name': 'My Company', 'fullPathName': None, 'externalReferenceId': None, 'source': None, 'id': 'CAD80F000946C25D6C150831060AA326'}, 'uuid': 'EA650B42-D10A-7F9F-A1D2-0A58C4F4CEB1', 'groupUpdateProvider': False, 'edrStatus': 0, 'freeDisk': 52481970176, 'diskDrive': 'C:\\', 'osFunction': 'Server', 'processorClock': 2394, 'mobilePhone': '', 'jobTitle': '', 'lastHeuristicThreatTime': 0, 'osname': 'Windows Server 2012', 'winServers': ['0.0.0.0', '0.0.0.0'], 'deploymentMessage': '', 'idsSerialNo': '', 'employeeNumber': '', 'snacLicenseId': None, 'lastSiteId': 'EE75B0850946C25D5287B58B5173A37C', 'uwf': 2, 'currentClientId': '256B2B130946C25D40C83823AA2E5D4C', 'osbitness': 'x64', 'lastScanTime': 1552465622000, 'email': '', 'securityVirtualAppliance': None, 'worstInfectionIdx': '0', 'encryptedDevicePassword': None, 'lastServerId': '7D6AAA6F0946C25D170B3A2D442500B6', 'kernel': None, 'lastUpdateTime': 1552471481568, 'ptpOnOff': 1, 'majorVersion': 14, 'lastConnectedIpAddr': '192.168.194.93', 'agentVersion': '14.2.1031.0100', 'deploymentRunningVersion': '14.2.1031.0100', 'agentTimeStamp': 1552471481568, 'osfunction': 'Server', 'osMajor': 6, 'deploymentTargetVersion': '14.2.1031.0100', 'osMinor': 2, 'osFlavorNumber': 79, 'logicalCpus': 0, 'deploymentPreVersion': '', 'hypervisorVendorId': '0', 'fbwf': 2, 'osversion': '6.2', 'dnsServers': ['192.168.192.29', 'FEC0:0000:0000:FFFF:0000:0000:0000:0001'], 'vsicStatus': 3, 'deleted': 0, 'deploymentStatus': '302456832', 'computerTimeStamp': 1552388971500, 'bwf': 2, 'totalDiskSpace': 81567, 'homePhone': '', 'daOnOff': 1, 'computerDescription': '', 'pepOnOff': 1, 'bashStatus': 1, 'agentUsn': 942822, 'osName': 'Windows Server 2012', 'patternIdx': '3F95B8098B9EEF1883B013F91C43AC72', 'employeeStatus': '', 'tmpDevice': None, 'rebootRequired': 0, 'subnetMasks': ['255.255.255.0', '64'], 'minorVersion': 2, 'osservicePack': '', 'lastSiteName': 'My Site', 'cidsEngineVersion': '0.0.0.0', 'lastDeploymentTime': 1550585147000, 'isGrace': 0, 'computerUsn': 921686, 'agentId': '6E5AA5CB0946C25D40C83823BB5107E6', 'cidsBrowserFfOnOff': 1, 'domainOrWorkgroup': 'WORKGROUP', 'svaId': None, 'loginDomain': 'LocalComputer', 'lastServerName': 'WIN-4OA0GKJN830', 'contentUpdate': 1, 'writeFiltersStatus': None, 'infected': 0, 'memory': 6441979904, 'osminor': 2, 'freeMem': 1933389824, 'officePhone': '', 'lastVirusTime': 1551350764000, 'telemetryMid': '890E283B-41D3-4340-A397-66F6AFCAF33E', 'idsVersion': '', 'cidsBrowserIeOnOff': 1, 'publicKey': 'BgIAAACkAABSU0ExAAgAAAEAAQDfMtYpvbC2ZOrpGFbK76tuyp2MZ7/6EGsFrqAV3ZBMfvMllksVObpPYvDSc5vCjtzthb1301VADLAspayGytsdAj5z8+LLpOnJkHNg9tIunm1lLkBTitevI6G+nNjyKd7uPn3+bxjk1LL8g1exL2C2SMPEXubdUa1N5xwmhhPHp6PSIAjY74QUcNyplfvylMS9QRWoQ70mqNy9tLLef6+qCYWTqGa7QKXS0WUJs8sJMzWfCrpeMVAmU5/s3yEu+OI+9RKgOeSfy7wRzmAWHQTofjHkYGYqwXcwwLX7AbWjdcpYo0Kaecf8e5t2ZvWyR362EaNxn0HYSjpKraY1hLK1', 'quarantineDesc': 'Host Integrity check is disabled.\n Host Integrity policy has been disabled by the administrator.', 'cidsDrvMulfCode': 0, 'biosVersion': 'INTEL  - 6040000 PhoenixBIOS 4.0 Release 6.0', 'rebootReason': '', 'telemetryHwid': 'A942D8EB-32C3-E42F-FE83-723FDC431F32', 'cidsSilentMode': 0, 'creationTime': 1550585043812, 'macAddresses': ['00-50-56-8B-A6-C3', '00-50-56-8B-A6-C3'], 'idsChecksum': None, 'operatingSystem': 'Windows Server 2012 ', 'osmajor': 6, 'virtualizationPlatform': 'Unknown', 'ipAddresses': ['192.168.194.93', 'FE80:0000:0000:0000:FC67:074E:CD22:0188'], 'physicalCpus': 1, 'osBitness': 'x64', 'cidsDefsetVersion': '190312061', 'cidsDrvOnOff': 1, 'computerName': 'WIN-4OA0GKJN830', 'logonUserName': 'Administrator', 'licenseExpiry': 0, 'osLanguage': 'en-US', 'gateways': ['192.168.194.1', '192.168.194.1', '0.0.0.0', '0.0.0.0'], 'uniqueId': 'D31AA16E0946C25D40C83823C500518B', 'department': '', 'isNpvdiClient': 0, 'dhcpServer': '0.0.0.0', 'description': '', 'osflavorNumber': 79, 'tpmDevice': '0', 'onlineStatus': 0, 'lastDownloadTime': 1551772684595, 'apOnOff': 1, 'timeZone': 480, 'fullName': '', 'osVersion': '6.2', 'attributeExtension': '', 'atpServer': '', 'tamperOnOff': 1, 'osServicePack': '', 'agentType': '105', 'serialNumber': 'VMware-42 0b 65 ea 0a d1 9f 7f-a1 d2 0a 58 c4 f4 ce b1', 'osElamStatus': 0, 'installType': '0', 'profileSerialNo': 'CAD8-01/26/2019 08:00:11 062', 'hardwareKey': '1771D79454E53469DF4B290C06C104C9', 'firewallOnOff': 1},
                            {'profileVersion': '14.2.1031', 'elamOnOff': 1, 'avEngineOnOff': 1, 'profileChecksum': None, 'atpDeviceId': None, 'processorType': 'Intel64 Family 6 Model 15 Stepping 1', 'oslanguage': 'en-US', 'licenseId': None, 'licenseStatus': -1, 'group': {'domain': {'id': '908090000946C25D330E919313D23887', 'name': 'Default'}, 'name': 'My Company\\Group_2', 'fullPathName': None, 'externalReferenceId': None, 'source': None, 'id': 'CC00A6170946C25D35BD115E41F2F92C'}, 'uuid': '87400B42-6E1A-D457-D45F-9804C4295C33', 'groupUpdateProvider': False, 'edrStatus': 0, 'freeDisk': 72927236096, 'diskDrive': 'c:\\', 'osFunction': 'Server', 'processorClock': 2394, 'mobilePhone': '', 'jobTitle': '', 'lastHeuristicThreatTime': 0, 'osname': 'Windows Server 2012', 'winServers': ['0.0.0.0', '0.0.0.0'], 'deploymentMessage': '', 'idsSerialNo': '', 'employeeNumber': '', 'snacLicenseId': None, 'lastSiteId': 'EE75B0850946C25D5287B58B5173A37C', 'uwf': 2, 'currentClientId': 'D4B78D1E0946C25D25E6C0981F256F40', 'osbitness': 'x64', 'lastScanTime': 1552462444000, 'email': '', 'securityVirtualAppliance': None, 'worstInfectionIdx': '0', 'encryptedDevicePassword': None, 'lastServerId': '7D6AAA6F0946C25D170B3A2D442500B6', 'kernel': None, 'lastUpdateTime': 1552471481568, 'ptpOnOff': 1, 'majorVersion': 14, 'lastConnectedIpAddr': '192.168.194.93', 'agentVersion': '14.2.1031.0100', 'deploymentRunningVersion': '14.2.1031.0100', 'agentTimeStamp': 1552471481568, 'osfunction': 'Server', 'osMajor': 6, 'deploymentTargetVersion': '14.2.1031.0100', 'osMinor': 2, 'osFlavorNumber': 79, 'logicalCpus': 0, 'deploymentPreVersion': '14.2.1031.0100', 'hypervisorVendorId': '0', 'fbwf': 2, 'osversion': '6.2', 'dnsServers': ['192.168.192.29', 'FEC0:0000:0000:FFFF:0000:0000:0000:0001'], 'vsicStatus': 3, 'deleted': 0, 'deploymentStatus': '302456832', 'computerTimeStamp': 1552407060917, 'bwf': 2, 'totalDiskSpace': 81567, 'homePhone': '', 'daOnOff': 1, 'computerDescription': '', 'pepOnOff': 1, 'bashStatus': 1, 'agentUsn': 943464, 'osName': 'Windows Server 2012', 'patternIdx': '3F95B8098B9EEF1883B013F91C43AC72', 'employeeStatus': '', 'tmpDevice': None, 'rebootRequired': 0, 'subnetMasks': ['255.255.255.0', '64'], 'minorVersion': 2, 'osservicePack': '', 'lastSiteName': 'My Site', 'cidsEngineVersion': '0.0.0.0', 'lastDeploymentTime': 1551280983000, 'isGrace': 0, 'computerUsn': 927295, 'agentId': '9530C0C30946C25D25E6C0988CF4F010', 'cidsBrowserFfOnOff': 1, 'domainOrWorkgroup': 'WORKGROUP', 'svaId': None, 'loginDomain': 'LocalComputer', 'lastServerName': 'WIN-4OA0GKJN830', 'contentUpdate': 1, 'writeFiltersStatus': None, 'infected': 0, 'memory': 4294496256, 'osminor': 2, 'freeMem': 2906599424, 'officePhone': '', 'lastVirusTime': 1551350382000, 'telemetryMid': 'E4DCBEAE-DCCD-476C-8ECA-AEE154F0F59F', 'idsVersion': '', 'cidsBrowserIeOnOff': 1, 'publicKey': 'BgIAAACkAABSU0ExAAgAAAEAAQAJWLeDFz6umLcsiKYxkbg+rl84pfQyjNVvzcC8dI6fqa8OzmMsuyMlDm2ShYAeNr7WkPLtDnfT/WoVDNQCHqLqgtRIZsYtWMUFLMXoq/u4RaThVlHEZiLS+tLDEcWWz/Iv75B2+5seHbeSV0/ZTVbYHLzRbTQnMetlbmKrvKXxoc1Aw5pKzTGeqqpTXczFEvLHIpHNp0SlbmPymGA5xag71CebfSLJfOu7YP2gMnnWLRPb1OTN3y0LQ0XQfTqOVNpwV8k5wJ52BRmwXSkY6HcvCQdX6GX/daV9kF3UBvd63rcau3tQI8n+GUr9rPDUlrnqYx5yWHoQI1jessq3darP', 'quarantineDesc': 'Host Integrity check is disabled.\n Host Integrity policy has been disabled by the administrator.', 'cidsDrvMulfCode': 0, 'biosVersion': 'INTEL  - 6040000 PhoenixBIOS 4.0 Release 6.0', 'rebootReason': '', 'telemetryHwid': '0414501C-2CC1-F574-8DAF-57BBCB2E0F34', 'cidsSilentMode': 0, 'creationTime': 1549052275576, 'macAddresses': ['00-50-56-8B-0F-88', '00-50-56-8B-0F-88'], 'idsChecksum': None, 'operatingSystem': 'Windows Server 2012 ', 'osmajor': 6, 'virtualizationPlatform': 'Unknown', 'ipAddresses': ['192.168.194.93', 'FE80:0000:0000:0000:C180:8DB8:60AF:EFEC'], 'physicalCpus': 1, 'osBitness': 'x64', 'cidsDefsetVersion': '190312061', 'cidsDrvOnOff': 1, 'computerName': 'WIN-N5KGH4CP3N3', 'logonUserName': 'Administrator', 'licenseExpiry': 0, 'osLanguage': 'en-US', 'gateways': ['192.168.194.1', '192.168.194.1', '0.0.0.0', '0.0.0.0'], 'uniqueId': '89AD1BBB0946C25D25E6C0984E971D8A', 'department': '', 'isNpvdiClient': 0, 'dhcpServer': '0.0.0.0', 'description': '', 'osflavorNumber': 79, 'tpmDevice': '0', 'onlineStatus': 1, 'lastDownloadTime': 1551280968098, 'apOnOff': 1, 'timeZone': 480, 'fullName': '', 'osVersion': '6.2', 'attributeExtension': '', 'atpServer': '', 'tamperOnOff': 1, 'osServicePack': '', 'agentType': '105', 'serialNumber': 'VMware-42 0b 40 87 1a 6e 57 d4-d4 5f 98 04 c4 29 5c 33', 'osElamStatus': 0, 'installType': '0', 'profileSerialNo': 'CC00-03/05/2019 11:50:56 570', 'hardwareKey': 'DC7D24D6465566D2941F35BC8D17801E', 'firewallOnOff': 1}],
                          'lastPage': True, 'totalPages': 1, 'size': 2, 'totalElements': 2, 'numberOfElements': 2}
                        )
                }

    return response.get(type)

def get_groups():
    return {'sort': [{'direction': 'ASC', 'property': 'NAME', 'ascending': True}], 'number': 0, 'firstPage': False,
                 'content': [{'policyDate': 1556542282626, 'domain': {'id': '908090000946C25D330E919313D23887', 'name': 'Default'},
                               'numberOfRegisteredUsers': 0, 'description': '', 'created': 1548481072007,
                               'policySerialNumber': '4CBD-04/29/2019 12:51:22 626', 'lastModified': 1548481072007,
                               'fullPathName': 'My Company\\Default Group', 'createdBy': 'AF3C39A10A320801000000DBF200C60A',
                               'numberOfPhysicalComputers': 0, 'customIpsNumber': '', 'id': '4CBD63EE0946C25D1011DB1872A1736A',
                               'policyInheritanceEnabled': True, 'name': 'Default Group'},
                              {'policyDate': 1556542282626, 'domain': {'id': '908090000946C25D330E919313D23887', 'name': 'Default'},
                               'numberOfRegisteredUsers': 0, 'description': '', 'created': 1551787280561,
                               'policySerialNumber': '36E0-04/29/2019 12:51:22 626', 'lastModified': 1551787280561,
                               'fullPathName': 'My Company\\G_0027', 'createdBy': 'AF3C39A10A320801000000DBF200C60A',
                               'numberOfPhysicalComputers': 0, 'customIpsNumber': '', 'id': '36E0B28B0946C25D06A29515DE448CF6',
                               'policyInheritanceEnabled': True, 'name': 'G_0027'}
                              ],
                 'lastPage': True,
                 'totalPages': 1,
                 'size': 2,
                 'totalElements': 2,
                 'numberOfElements': 2}

def move_endpoint():
    return [{'responseMessage': 'OK', 'responseCode': '200'}]

def quarantine_endpoints():
    return {'commandID_computer': '09114E42730A479993DD6D94CF9CAA53', "commandID_group": "89637CF1D7204D028522C81C4389301B"}

def scan_endpoints():
    return {'commandID_computer': '0F0CBDD7EDFF4634B23FA11F5AB81FFC',
                'commandID_group': 'BB37F78894DB451B8E8921EC127667A3'}

def get_command_status():
    return {'sort': [{'direction': 'ASC', 'property': 'Begintime', 'ascending': True}], 'number': 0,
                'firstPage': True,
                'content': [{'computerName': 'johnq1', 'subStateId': 0, 'binaryFileId': None, 'lastUpdateTime': None,
                   'domainName': 'Default', 'hardwareKey': 'B791D1DF2BB8AA77D19B10E3BB395B81',
                   'subStateDesc': None, 'stateId': 0, 'computerId': '236A7100A9FE9DC50A4F1AC2819C158E',
                   'computerIp': '192.168.56.104', 'beginTime': None, 'currentLoginUserName': 'root',
                   'resultInXML': None}, {'computerName': 'WIN-N5KGH4CP3N3', 'subStateId': 0, 'binaryFileId': None,
                                           'lastUpdateTime': '2019-06-06T10:45:39Z', 'domainName': 'Default',
                                           'hardwareKey': 'DC7D24D6465566D2941F35BC8D17801E', 'subStateDesc': '',
                                           'stateId': 3, 'computerId': '89AD1BBB0946C25D25E6C0984E971D8A',
                                           'computerIp': '192.168.194.93', 'beginTime': '2019-06-06T10:42:37Z',
                                           'currentLoginUserName': 'Administrator',
                                           'resultInXML': '<EOC creator="Resilient" version="1.0" id="id">\n    <DataSource name="name" id="id" version="version"/>\n    <ScanType>QUICK_SCAN</ScanType>\n    <Threat time="" severity="" type="" category="">\n        <Description>Scan eoc for suspicious hash of type Malware MD5 Hash and value 582F9B6E0CC4C1DBBD772AAAF088CB3A in the SEP environment.</Description>\n        <URL></URL>\n        <User></User>\n        <Attacker>\n        </Attacker>\n        <proxy ip=""/>\n        <Application></Application>\n    </Threat>\n    <Activity>\n        <OS id="0" name="name" version="version">\n            <Process>\n            </Process>\n            <Files>\n                <File name="" action="create">\n                    <Matched result="NO_MATCH"/></File>\n                <File name="" action="create">\n                    <Matched result="NO_MATCH"/></File>\n                <File name="" action="create">\n                    <Hash name="MD5" value="582f9b6e0cc4c1dbbd772aaaf088cb3a"/>\n                    <Matched result="NO_MATCH"/></File>\n            </Files>\n            <Registry>\n            </Registry>\n            <Network/>\n        </OS>\n    </Activity>\n</EOC>'},
                  {'computerName': 'jqbf957root', 'subStateId': 0, 'binaryFileId': None,
                   'lastUpdateTime': '2019-06-06T10:53:53Z', 'domainName': 'Default',
                   'hardwareKey': '9FACFF634F892674CA3BF7EE995B565D', 'subStateDesc': '', 'stateId': 3,
                   'computerId': '5FA95F22A9FE9DC50A4F1AC22197CDF4', 'computerIp': '192.168.166.16',
                   'beginTime': '2019-06-06T10:42:37Z', 'currentLoginUserName': 'Administrator',
                   'resultInXML': '<EOC creator="Resilient" version="1.0" id="id">\n    <DataSource name="name" id="id" version="version"/>\n    <ScanType>QUICK_SCAN</ScanType>\n    <Threat time="" severity="" type="" category="">\n        <Description>Scan eoc for suspicious hash of type Malware MD5 Hash and value 582F9B6E0CC4C1DBBD772AAAF088CB3A in the SEP environment.</Description>\n        <URL></URL>\n        <User></User>\n        <Attacker>\n        </Attacker>\n        <proxy ip=""/>\n        <Application></Application>\n    </Threat>\n    <Activity>\n        <OS id="0" name="name" version="version">\n            <Process>\n            </Process>\n            <Files>\n                <File name="" action="create">\n                    <Matched result="NO_MATCH"/></File>\n                <File name="" action="create">\n                    <Matched result="NO_MATCH"/></File>\n                <File name="" action="create">\n                    <Hash name="MD5" value="582f9b6e0cc4c1dbbd772aaaf088cb3a"/>\n                    <Matched result="NO_MATCH"/></File>\n            </Files>\n            <Registry>\n            </Registry>\n            <Network/>\n        </OS>\n    </Activity>\n</EOC>'},
                  {'computerName': 'WIN-4OA0GKJN830', 'subStateId': 0, 'binaryFileId': None,
                   'lastUpdateTime': '2019-06-06T10:50:35Z', 'domainName': 'Default',
                   'hardwareKey': '1771D79454E53469DF4B290C06C104C9', 'subStateDesc': '', 'stateId': 3,
                   'computerId': 'D31AA16E0946C25D40C83823C500518B', 'computerIp': '192.168.194.93',
                   'beginTime': '2019-06-06T10:42:39Z', 'currentLoginUserName': 'Administrator',
                   'resultInXML': '<EOC creator="Resilient" version="1.0" id="id">\n    <DataSource name="name" id="id" version="version"/>\n    <ScanType>QUICK_SCAN</ScanType>\n    <Threat time="" severity="" type="" category="">\n        <Description>Scan eoc for suspicious hash of type Malware MD5 Hash and value 582F9B6E0CC4C1DBBD772AAAF088CB3A in the SEP environment.</Description>\n        <URL></URL>\n        <User></User>\n        <Attacker>\n        </Attacker>\n        <proxy ip=""/>\n        <Application></Application>\n    </Threat>\n    <Activity>\n        <OS id="0" name="name" version="version">\n            <Process>\n            </Process>\n            <Files>\n                <File name="" action="create">\n                    <Matched result="NO_MATCH"/></File>\n                <File name="" action="create">\n                    <Matched result="NO_MATCH"/></File>\n                <File name="" action="create">\n                    <Hash name="MD5" value="582f9b6e0cc4c1dbbd772aaaf088cb3a"/>\n                    <Matched result="NO_MATCH"/></File>\n            </Files>\n            <Registry>\n            </Registry>\n            <Network/>\n        </OS>\n    </Activity>\n</EOC>'}],
                'lastPage': True, 'totalPages': 1, 'size': 20, 'totalElements': 4, 'numberOfElements': 4}

def get_command_status_remediation():
    return {'sort': [{'direction': 'ASC', 'property': 'Begintime', 'ascending': True}], 'number': 0,
                 'firstPage': True, 'content': [{'computerName': 'WIN-N5KGH4CP3N3', 'subStateId': 0,
                                                   'binaryFileId': None, 'lastUpdateTime': '2019-06-11T11:14:53Z',
                                                   'domainName': 'Default', 'hardwareKey': 'DC7D24D6465566D2941F35BC8D17801E',
                                                   'subStateDesc': '', 'stateId': 3,
                                                   'computerId': '89AD1BBB0946C25D25E6C0984E971D8A',
                                                   'computerIp': '192.168.194.94', 'beginTime': '2019-06-11T11:14:48Z',
                                                   'currentLoginUserName': 'Administrator',
                                                   'resultInXML': '<EOC creator="Resilient" version="1.0" id="id">\n    <DataSource name="name" id="id" version="version"/>\n    <ScanType>FULL_SCAN</ScanType>\n    <RemediationAction>REMEDIATE</RemediationAction>\n    <Threat time="" severity="" type="" category="">\n        <Description>Remediate endpoint for suspect file C:\\temp\\where_copy.exe</Description>\n        <URL></URL>\n        <User></User>\n        <Attacker>\n        </Attacker>\n        <proxy ip=""/>\n        <Application></Application>\n    </Threat>\n    <Activity>\n        <OS id="0" name="name" version="version">\n            <Process>\n            </Process>\n            <Files>\n                <File name="C:\\temp\\where_copy.exe" action="create">\n                    <Hash name="SHA256" value="bfe4fd780b47e8d4e5661d4c3881d114e8631e84a686e3bb8aad85d4af20454a"/>\n                    <Matched result="HASH_MATCH" value="C:\\$Recycle.Bin\\S-1-5-21-3046121036-4288610245-94028597-500\\$REPUASN.exe" remediation="FAILED" hashType="SHA256"/>\n                    <Matched result="HASH_MATCH" value="C:\\$Recycle.Bin\\S-1-5-21-3046121036-4288610245-94028597-500\\$RMRY4I0.exe" remediation="FAILED" hashType="SHA256"/>\n                    <Matched result="HASH_MATCH" value="C:\\temp\\where-copy.exe" remediation="FAILED" hashType="SHA256"/>\n                    <Matched result="HASH_MATCH" value="C:\\temp\\where.exe" remediation="FAILED" hashType="SHA256"/>\n                    <Matched result="HASH_MATCH" value="C:\\temp\\where_copy.exe" remediation="FAILED" hashType="SHA256"/>\n                    <Matched result="HASH_MATCH" value="C:\\Users\\Administrator\\Desktop\\where-copy(2).exe" remediation="FAILED" hashType="SHA256"/>\n                    <Matched result="HASH_MATCH" value="C:\\Users\\Administrator\\Desktop\\where-copy.exe" remediation="FAILED" hashType="SHA256"/>\n                    <Matched result="HASH_MATCH" value="C:\\Users\\Administrator\\Documents\\where_copy.exe" remediation="FAILED" hashType="SHA256"/>\n                    <Matched result="HASH_MATCH" value="C:\\Windows\\SysWOW64\\where.exe" remediation="FAILED" hashType="SHA256"/></File>\n                <File name="C:\\temp\\where_copy.exe" action="create">\n                    <Matched result="FULL_MATCH" value="C:\\temp\\where_copy.exe" remediation="UNSUPPORTED" hashType="SHA256" hashValue="bfe4fd780b47e8d4e5661d4c3881d114e8631e84a686e3bb8aad85d4af20454a"/></File>\n                <File name="C:\\temp\\where_copy.exe" action="create">\n                    <Matched result="FULL_MATCH" value="C:\\temp\\where_copy.exe" remediation="UNSUPPORTED" hashType="SHA256" hashValue="bfe4fd780b47e8d4e5661d4c3881d114e8631e84a686e3bb8aad85d4af20454a"/></File>\n            </Files>\n            <Registry>\n            </Registry>\n            <Network/>\n        </OS>\n    </Activity>\n</EOC>'}],
                 'lastPage': True, 'totalPages': 1, 'size': 20, 'totalElements': 1, 'numberOfElements': 1
    }

def get_command_status_processed():
    return {'sort': [{'direction': 'ASC', 'property': 'Begintime', 'ascending': True}], 'total_match_ep_count': 2,
                'total_remediation_count': 0, 'total_ep_count': 4, 'number': 0, 'firstPage': True, 'total_match_count': 2,
                'content': [{'computerName': 'WIN-N5KGH4CP3N3', 'subStateId': 0, 'binaryFileId': None,
                              'lastUpdateTime': '2019-06-06T11:56:31Z', 'domainName': 'Default',
                              'hardwareKey': 'DC7D24D6465566D2941F35BC8D17801E', 'subStateDesc': '', 'stateId': 3,
                              'scan_result': {'match_count': 1, 'remediation_count': 0, 'PARTIAL_MATCHES': [], 'HASH_MATCHES': [],
                                              'artifact_type': 'File Name',
                                              'FULL_MATCHES': [{'hashType': 'SHA256', 'hashValue': 'b82758fc5f737a58078d3c60e2798a70d895443a86aa39adf52dec70e98c2bed',
                                                                'result': 'FULL_MATCH', 'value': 'C:\\temp\\My_file_1.txt'}],
                                              'artifact_value': 'C:\\temp\\My_file_1.txt', 'MATCH': True}, 'computerId': '89AD1BBB0946C25D25E6C0984E971D8A',
                              'computerIp': '192.168.194.93', 'beginTime': '2019-06-06T11:56:26Z', 'currentLoginUserName': 'Administrator', 
                              'resultInXML': '<EOC creator="Resilient" version="1.0" id="id">\n    <DataSource name="name" id="id" version="version"/>\n    <ScanType>QUICK_SCAN</ScanType>\n    <Threat time="" severity="" type="" category="">\n        <Description>Scan eoc for suspicious hash of type File Path and value C:\\temp\\My_file_1.txt in the SEP environment.</Description>\n        <URL></URL>\n        <User></User>\n        <Attacker>\n        </Attacker>\n        <proxy ip=""/>\n        <Application></Application>\n    </Threat>\n    <Activity>\n        <OS id="0" name="name" version="version">\n            <Process>\n            </Process>\n            <Files>\n                <File name="C:\\temp\\My_file_1.txt" action="create">\n                    <Matched result="FULL_MATCH" value="C:\\temp\\My_file_1.txt" hashType="SHA256" hashValue="b82758fc5f737a58078d3c60e2798a70d895443a86aa39adf52dec70e98c2bed"/></File>\n                <File name="C:\\temp\\My_file_1.txt" action="create">\n                    <Matched result="FULL_MATCH" value="C:\\temp\\My_file_1.txt" hashType="SHA256" hashValue="b82758fc5f737a58078d3c60e2798a70d895443a86aa39adf52dec70e98c2bed"/></File>\n                <File name="C:\\temp\\My_file_1.txt" action="create">\n                    <Matched result="FULL_MATCH" value="C:\\temp\\My_file_1.txt" hashType="SHA256" hashValue="b82758fc5f737a58078d3c60e2798a70d895443a86aa39adf52dec70e98c2bed"/></File>\n            </Files>\n            <Registry>\n            </Registry>\n            <Network/>\n        </OS>\n    </Activity>\n</EOC>'},
                             {'computerName': 'WIN-4OA0GKJN830', 'subStateId': 0, 'binaryFileId': None,
                              'lastUpdateTime': '2019-06-06T11:56:32Z', 'domainName': 'Default',
                              'hardwareKey': '1771D79454E53469DF4B290C06C104C9', 'subStateDesc': '', 'stateId': 3, 
                              'scan_result': {'match_count': 1, 'remediation_count': 0, 'PARTIAL_MATCHES': [], 'HASH_MATCHES': [], 
                                              'artifact_type': 'File Name', 
                                              'FULL_MATCHES': [{'hashType': 'SHA256', 'hashValue': 'b82758fc5f737a58078d3c60e2798a70d895443a86aa39adf52dec70e98c2bed', 
                                                                'result': 'FULL_MATCH', 'value': 'C:\\temp\\My_file_1.txt'}], 
                                              'artifact_value': 'C:\\temp\\My_file_1.txt', 'MATCH': True}, 'computerId': 'D31AA16E0946C25D40C83823C500518B', 
                              'computerIp': '192.168.194.93', 'beginTime': '2019-06-06T11:56:27Z', 'currentLoginUserName': 'Administrator', 
                              'resultInXML': '<EOC creator="Resilient" version="1.0" id="id">\n    <DataSource name="name" id="id" version="version"/>\n    <ScanType>QUICK_SCAN</ScanType>\n    <Threat time="" severity="" type="" category="">\n        <Description>Scan eoc for suspicious hash of type File Path and value C:\\temp\\My_file_1.txt in the SEP environment.</Description>\n        <URL></URL>\n        <User></User>\n        <Attacker>\n        </Attacker>\n        <proxy ip=""/>\n        <Application></Application>\n    </Threat>\n    <Activity>\n        <OS id="0" name="name" version="version">\n            <Process>\n            </Process>\n            <Files>\n                <File name="C:\\temp\\My_file_1.txt" action="create">\n                    <Matched result="FULL_MATCH" value="C:\\temp\\My_file_1.txt" hashType="SHA256" hashValue="b82758fc5f737a58078d3c60e2798a70d895443a86aa39adf52dec70e98c2bed"/></File>\n                <File name="C:\\temp\\My_file_1.txt" action="create">\n                    <Matched result="FULL_MATCH" value="C:\\temp\\My_file_1.txt" hashType="SHA256" hashValue="b82758fc5f737a58078d3c60e2798a70d895443a86aa39adf52dec70e98c2bed"/></File>\n                <File name="C:\\temp\\My_file_1.txt" action="create">\n                    <Matched result="FULL_MATCH" value="C:\\temp\\My_file_1.txt" hashType="SHA256" hashValue="b82758fc5f737a58078d3c60e2798a70d895443a86aa39adf52dec70e98c2bed"/></File>\n            </Files>\n            <Registry>\n            </Registry>\n            <Network/>\n        </OS>\n    </Activity>\n</EOC>'}
                             ], 
                 'lastPage': True, 'total_remediation_ep_count': 0, 'totalPages': 1, 'size': 20, 'totalElements': 2, 
                 'total_not_completed': 1, 'overall_command_state': 'In progress', "scan_artifact_value": "C:\\temp\\My_file_1.txt", 'numberOfElements': 2
    }

def get_command_status_prefilter(type):
    response = {"match": ({ 'sort': [{'direction': 'ASC', 'property': 'Begintime', 'ascending': True}],
                            'total_match_ep_count': 1, 'total_remediation_count': 2, 'total_ep_count': 1, 'number': 0,
                             'firstPage': True, 'total_match_count': 3,
                             'content': [{'computerName': 'WIN-N5KGH4CP3N3', 'subStateId': 0, 'binaryFileId': None,
                                           'lastUpdateTime': '2019-06-11T11:14:53Z', 'domainName': 'Default',
                                           'hardwareKey': 'DC7D24D6465566D2941F35BC8D17801E', 'subStateDesc': '', 'stateId': 3,
                                           'scan_result': {'match_count': 3, 'remediation_count': 2, 'PARTIAL_MATCHES': [],
                                                           'HASH_MATCHES': [{'remediation': 'SUCCEEDED', 'hashType': 'SHA256', 'result': 'HASH_MATCH', 'value': 'C:\\temp\\where-copy.exe'},
                                                                            {'remediation': 'SUCCEEDED', 'hashType': 'SHA256', 'result': 'HASH_MATCH', 'value': 'C:\\temp\\where.exe'}],
                                                           'artifact_type': 'SHA256 hash', 'FULL_MATCHES': [{'remediation': 'UNSUPPORTED', 'hashType': 'SHA256', 'hashValue': 'bfe4fd780b47e8d4e5661d4c3881d114e8631e84a686e3bb8aad85d4af20454a', 'result': 'FULL_MATCH', 'value': 'C:\\temp\\where_copy.exe'}],
                                                           'artifact_value': 'bfe4fd780b47e8d4e5661d4c3881d114e8631e84a686e3bb8aad85d4af20454a', 'fail_remediation_count': 9, 'MATCH': True},
                                           'computerId': '89AD1BBB0946C25D25E6C0984E971D8A', 'computerIp': '192.168.194.94', 'beginTime': '2019-06-11T11:14:48Z',
                                           'currentLoginUserName': 'Administrator', 'resultInXML': ''}],
                             'lastPage': True, 'total_fail_remediation_count': 0, 'total_remediation_ep_count': 1, 'totalPages': 1,
                             'size': 20, 'totalElements': 1, 'total_not_completed': 0, 'overall_command_state': 'Completed',
                             'numberOfElements': 1
                        }),
                "no_match":   ({'sort': [{'direction': 'ASC', 'property': 'Begintime', 'ascending': True}],
                                'total_match_ep_count': 0, 'total_remediation_count': 0, 'total_ep_count': 4, 'number': 0,
                                'firstPage': True, 'total_match_count': 0,
                                'content': [
                                   {'computerName': 'johnq1', 'subStateId': 0, 'binaryFileId': None,
                                    'lastUpdateTime': None, 'domainName': 'Default',
                                    'hardwareKey': 'B791D1DF2BB8AA77D19B10E3BB395B81', 'subStateDesc': None,
                                    'stateId': 0, 'computerId': '236A7100A9FE9DC50A4F1AC2819C158E',
                                    'computerIp': '192.168.56.104', 'beginTime': None, 'currentLoginUserName': 'root',
                                    'resultInXML': None},
                                   {'computerName': 'jqbf957root', 'subStateId': 0, 'binaryFileId': None,
                                    'lastUpdateTime': '2019-06-12T09:28:54Z', 'domainName': 'Default',
                                    'hardwareKey': '9FACFF634F892674CA3BF7EE995B565D', 'subStateDesc': '',
                                    'stateId': 3,
                                    'scan_result': {'match_count': 0, 'remediation_count': 0, 'PARTIAL_MATCHES': [],
                                                    'HASH_MATCHES': [], 'artifact_type': '', 'FULL_MATCHES': [],
                                                    'artifact_value': '', 'fail_remediation_count': 0, 'MATCH': False},
                                    'computerId': '5FA95F22A9FE9DC50A4F1AC22197CDF4', 'computerIp': '192.168.166.16',
                                    'beginTime': '2019-06-12T09:28:49Z', 'currentLoginUserName': 'Administrator',
                                    'resultInXML': ''},
                                   {'computerName': 'WIN-N5KGH4CP3N3', 'subStateId': 0, 'binaryFileId': None,
                                    'lastUpdateTime': '2019-06-12T09:28:55Z', 'domainName': 'Default',
                                    'hardwareKey': 'DC7D24D6465566D2941F35BC8D17801E', 'subStateDesc': '',
                                    'stateId': 3,
                                    'scan_result': {'match_count': 0, 'remediation_count': 0, 'PARTIAL_MATCHES': [],
                                                    'HASH_MATCHES': [], 'artifact_type': '', 'FULL_MATCHES': [],
                                                    'artifact_value': '', 'fail_remediation_count': 0, 'MATCH': False},
                                    'computerId': '89AD1BBB0946C25D25E6C0984E971D8A', 'computerIp': '192.168.194.94',
                                    'beginTime': '2019-06-12T09:28:50Z', 'currentLoginUserName': 'Administrator',
                                    'resultInXML': ''},
                                   {'computerName': 'WIN-4OA0GKJN830', 'subStateId': 0, 'binaryFileId': None,
                                    'lastUpdateTime': '2019-06-12T09:28:57Z', 'domainName': 'Default',
                                    'hardwareKey': '1771D79454E53469DF4B290C06C104C9', 'subStateDesc': '',
                                    'stateId': 3,
                                    'scan_result': {'match_count': 0, 'remediation_count': 0, 'PARTIAL_MATCHES': [],
                                                    'HASH_MATCHES': [], 'artifact_type': '', 'FULL_MATCHES': [],
                                                    'artifact_value': '', 'fail_remediation_count': 0, 'MATCH': False},
                                    'computerId': 'D31AA16E0946C25D40C83823C500518B', 'computerIp': '192.168.194.93',
                                    'beginTime': '2019-06-12T09:28:52Z', 'currentLoginUserName': 'Administrator',
                                    'resultInXML': ''}],
                                'lastPage': True, 'total_fail_remediation_count': 0, 'total_remediation_ep_count': 0,
                                'totalPages': 1, 'size': 20, 'totalElements': 4, 'total_not_completed': 1,
                                'overall_command_state': 'In progress', 'numberOfElements': 4}
                           )
                }
    return response[type]

def get_file_content():
    return bytearray("SGkgdGhlcmU=", "utf8")

def upload_file():
    return {"commandID": "171969C124D54C069D7018914AA02184"}

def post_res_att(file_name, incident_id):
    return dict({'task_at_id': None, 'vers': 2, 'name': file_name,
                 'task_id': None, 'created': 1531959479048, 'inc_owner': 4,
                 'task_members': None, 'task_custom': None, 'task_name': None,
                 'actions': [], 'inc_name': 'BigFix', 'creator_id': 4,
                 'content_type': 'text/plain', 'inc_id': incident_id, 'type': 'incident',
                 'id': 1, 'size': 37261
                }
    )

def get_test_zip():
    with open(MOCK_ZIP, 'rb') as mockzip:
        data = mockzip.read()
    return data

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
            if "file_name" not in self:
                self.file_name = filename
            if "incident_id" not in self:
                self.incident_id = uri.split('/')[2]
            return post_res_att(self.file_name, self.incident_id)

    return MockResponse(*args)


def mocked_sep_client(*args):

    class MockResponse:
        """Class will be used by the mock to replace amp_client in circuits tests"""
        def __init__(self, *arg):
            self.r = Response()

        def __contains__(self, key):
            return True if key in self.__dict__.keys() else False

        def add_fingerprint_list(self, fingerprintlist_name=None, description=None, domainid=None, hash_value=None):
            return add_fingerprint_list()

        def get_fingerprint_list(self, fingerprintlist_id=None, domainid=None, fingerprintlist_name=None):
            return get_fingerprint_list()

        def update_fingerprint_list(self, fingerprintlist_id=None, fingerprintlist_name=None, description=None,
                                    domainid=None, hash_value=None):
            return update_fingerprint_list()

        def delete_fingerprint_list(self, fingerprintlist_id=None):
            return delete_fingerprint_list()

        def assign_fingerprint_list_to_group(self, groupid, fingerprintlist_id=None):
            return assign_fingerprint_list_to_group()

        def get_computers(self, computername=None, domain=None, lastupdate=None, order=None, os=None, pageindex=None,
                          pagesize=None, sort=None, status=None, status_details=None, matching_endpoint_ids=None):
            if computername:
                return get_computers("hostname")
            else:
                return get_computers("all")

        def get_domains(self):
            return get_domains()

        def get_groups(self, domain=None, fullpathname=None, mode=None, order=None, os=None, pageindex=None,
                       pagesize=None, sort=None):
            return get_groups()

        def move_endpoint(self, groupid, hardwarekey):
            return move_endpoint()

        def quarantine_endpoints(self, group_ids=None, computer_ids=None, hardware_keys=None, undo=None):
            return quarantine_endpoints()

        def scan_endpoints(self, computer_ids=None, group_ids=None, scan_type=None, file_path=None, sha256=None,
                           sha1=None, md5=None, description=None, scan_action=None):
            return scan_endpoints()

        def get_command_status(self, commandid=None, order=None, pageindex=None, pagesize=None, sort=None,
                               status_type=None, matching_endpoint_ids=None, incident_id=None):
            return get_command_status()

        def get_file_content(self, file_id=None):
            return get_file_content()

        def upload_file(self, file_path=None, computer_ids=None, sha256=None, md5=None, sha1=None, source=None):
            return upload_file()

        def get_paginated_results(self, get_method, **params):
            return get_method(**params)

    return MockResponse(*args)


def mocked_request(*args, **kwargs):
    class MockSession:
        """Class will be used by the mock to replace get and post requests in standalone tests"""
        def __init__(self, *arg, **kwargs):
            # Mock
            pass

        def execute_call(self, *args, **kwargs):
            if args[0].lower() == "post":
                if re.match("^https://192.168.1.2:8446/sepm/api/v1/identity/authenticate$", args[1]):
                    return MockGetResponse(get_token(), None, 200)
                elif re.match("^https://192.168.1.2:8446/sepm/api/v1/policy-objects/fingerprints$", args[1]):
                    return add_fingerprint_list()
                elif re.match("^https://192.168.1.2:8446/sepm/api/v1/policy-objects/fingerprints/.*$", args[1]):
                    return update_fingerprint_list()
                elif re.match("^https://192.168.1.2:8446/sepm/api/v1/command-queue/files", args[1]):
                    return upload_file()
                elif re.match("^https://192.168.1.2:8446/sepm/api/v1/command-queue/quarantine$", args[1]):
                    return quarantine_endpoints()
                elif re.match("^https://192.168.1.2:8446/sepm/api/v1/command-queue/eoc$", args[1]):
                    return scan_endpoints()
            elif args[0].lower() == "get":
                if re.match("^https://192.168.1.2:8446/sepm/api/v1/version$", args[1]):
                    return get_version()
                elif re.match("^https://192.168.1.2:8446/sepm/api/v1/domains$", args[1]):
                    return get_domains()
                elif re.match("^https://192.168.1.2:8446/sepm/api/v1/computers$", args[1]):
                    if kwargs["params"]["computerName"] is None:
                        return get_computers("all")
                    else:
                        return get_computers("hostname")
                elif re.match("^https://192.168.1.2:8446/sepm/api/v1/groups$", args[1]):
                    return get_groups()
                elif re.match("^https://192.168.1.2:8446/sepm/api/v1/policy-objects/fingerprints", args[1]):
                    return get_fingerprint_list()
                elif re.match("^https://192.168.1.2:8446/sepm/api/v1/command-queue/file/.*/content$", args[1]):
                    return get_file_content()
                elif re.match("^https://192.168.1.2:8446/sepm/api/v1/command-queue/.*", args[1]):
                    return get_command_status()
            elif args[0].lower() == "patch":
                if re.match("^https://192.168.1.2:8446/sepm/api/v1/computers$", args[1]):
                    return move_endpoint()
            elif args[0].lower() == "delete":
                if re.match("^https://192.168.1.2:8446/sepm/api/v1/policy-objects/fingerprints", args[1]):
                    return delete_fingerprint_list()
            elif args[0].lower() == "put":
                if re.match("^https://192.168.1.2:8446/sepm/api/v1/groups/.*/system-lockdown/fingerprints", args[1]):
                    return assign_fingerprint_list_to_group()

        def __getitem__(self, key):
            return getattr(self, key)

    return MockSession(*args, **kwargs)

class MockGetResponse:
    """Class will be used by the mock to replace get and post requests in standalone tests"""
    def __init__(self, *args, **kwargs):
        self.headers = {}
        self.r = Response()
        if args[0]:
            self.token = args[0]
        if args[1]:
            self.r._content = (args[1]).encode()
        self.status_code = args[2]
        self.r.status_code = args[2]

    def __getitem__(self, key):
        return getattr(self, key)


def mocked_request_session(*args, **kwargs):
    class MockGetResponseSession:
        """Class will be used by the mock to replace get and post requests in standalone tests"""
        def __init__(self, *args, **kwargs):
            self.headers = {}
            self.r = Response()
            if args[0].lower() == "get":
                if re.match("^https://192.168.1.2:8446/sepm/api/v1/command-queue/file/.*/content$", args[1]):
                    self.content = get_test_zip()
                else:
                    self.content = json.dumps(get_computers("all"))
                self.status_code = 200
            elif args[0].lower() == "patch":
                self.content = json.dumps(move_endpoint())
                self.status_code = 200
            elif args[0].lower() == "post":
                self.content = json.dumps(upload_file())
                self.status_code = 200
            elif args[0].lower() == "put":
                self.content = json.dumps(assign_fingerprint_list_to_group())
                self.status_code = 200
            elif args[0].lower() == "delete":
                self.content = json.dumps(delete_fingerprint_list())
                self.status_code = 200
            if version_info.major == 3:
                if not isinstance(self.content, bytes):
                    self.content = bytes(self.content, "utf8")

        def json(self):
            return json.loads(self.content)

        def raise_for_status(self):
            """Raises stored :class:`HTTPError`, if one occurred."""

            http_error_msg = ''

            if self.status_code in range(200, 203):
                pass

            if http_error_msg:
                raise HTTPError(http_error_msg, response=self)
    return MockGetResponseSession(*args, **kwargs)

def get_mock_config():
    return """[fn_cisco_amp4ep]
base_path=/sepm/api/v1
auth_path=/sepm/api/v1/identity/authenticate
host=192.168.1.2
port=8446
username=admin
password=password
domain=Default
results_limit=6
"""
