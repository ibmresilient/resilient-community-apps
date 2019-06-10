# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
"""Generate Mock responses to simulate Cisco AMP for endpoinst for Unit and function tests """
import time
import re

from requests import HTTPError
from requests.models import Response

# Responses for standalone tests
def get_fingerprint_list():

    response = {"description": "Hash of type Malware MD5 Hash", "hashType": "MD5", "source": "WEBSERVICE",
                "groupIds": [], "data": ["582F9B6E0CC4C1DBBD772AAAF088CB3A"], "id": "B5F9985ED6C449A6905A0D570A5733FC",
                "name": "Blacklist"}

    return response


def add_fingerprint_list():
    return {u"id": u"B5F9985ED6C449A6905A0D570A5733FC"}

def delete_fingerprint_list():
    return ""

def update_fingerprint_list():
    return ""

def assign_fingerprint_list_to_group():
    return ""

def get_token():
    token = "abcd1234-a123-123a-123a-123456abcdef"
    return token

def get_version():
    response = {u'version': u'14.2.1031.0100', u'API_SEQUENCE': u'181118008', u'API_VERSION': u'1.0.0'}
    return response

def get_domains():
    response = [{u'enable': True, u'description': None, u'administratorCount': 1, u'companyName': u'',
                 u'createdTime': 1548481071820, u'contactInfo': None, u'id': u'908090000946C25D330E919313D23887',
                 u'name': u'Default'},
                {u'enable': True, u'description': None, u'administratorCount': 1, u'companyName': u'Resilient',
                 u'createdTime': 1550680668947, u'contactInfo': u'', u'id': u'A9B4B7160946C25D24B6AA458EF5557F',
                 u'name': u'JP_test_Domain'}]
    return response

def get_computers(type):
    response = {"all": ({u'sort': [{u'direction': u'ASC', u'property': u'COMPUTER_NAME', u'ascending': True}], u'number': 0, u'firstPage': True,
                          u'content': [{u'profileVersion': u'14.2.1031', u'elamOnOff': 1, u'avEngineOnOff': 1, u'profileChecksum': None, u'atpDeviceId': None, u'processorType': u'Intel64 Family 6 Model 15 Stepping 1', u'oslanguage': u'en-US', u'licenseId': None, u'licenseStatus': -1, u'group': {u'domain': {u'id': u'908090000946C25D330E919313D23887', u'name': u'Default'}, u'name': u'My Company', u'fullPathName': None, u'externalReferenceId': None, u'source': None, u'id': u'CAD80F000946C25D6C150831060AA326'}, u'uuid': u'EA650B42-D10A-7F9F-A1D2-0A58C4F4CEB1', u'groupUpdateProvider': False, u'edrStatus': 0, u'freeDisk': 52481970176, u'diskDrive': u'C:\\', u'osFunction': u'Server', u'processorClock': 2394, u'mobilePhone': u'', u'jobTitle': u'', u'lastHeuristicThreatTime': 0, u'osname': u'Windows Server 2012', u'winServers': [u'0.0.0.0', u'0.0.0.0'], u'deploymentMessage': u'', u'idsSerialNo': u'', u'employeeNumber': u'', u'snacLicenseId': None, u'lastSiteId': u'EE75B0850946C25D5287B58B5173A37C', u'uwf': 2, u'currentClientId': u'256B2B130946C25D40C83823AA2E5D4C', u'osbitness': u'x64', u'lastScanTime': 1552465622000, u'email': u'', u'securityVirtualAppliance': None, u'worstInfectionIdx': u'0', u'encryptedDevicePassword': None, u'lastServerId': u'7D6AAA6F0946C25D170B3A2D442500B6', u'kernel': None, u'lastUpdateTime': 1552471481568, u'ptpOnOff': 1, u'majorVersion': 14, u'lastConnectedIpAddr': u'192.168.194.93', u'agentVersion': u'14.2.1031.0100', u'deploymentRunningVersion': u'14.2.1031.0100', u'agentTimeStamp': 1552471481568, u'osfunction': u'Server', u'osMajor': 6, u'deploymentTargetVersion': u'14.2.1031.0100', u'osMinor': 2, u'osFlavorNumber': 79, u'logicalCpus': 0, u'deploymentPreVersion': u'', u'hypervisorVendorId': u'0', u'fbwf': 2, u'osversion': u'6.2', u'dnsServers': [u'192.168.192.29', u'FEC0:0000:0000:FFFF:0000:0000:0000:0001'], u'vsicStatus': 3, u'deleted': 0, u'deploymentStatus': u'302456832', u'computerTimeStamp': 1552388971500, u'bwf': 2, u'totalDiskSpace': 81567, u'homePhone': u'', u'daOnOff': 1, u'computerDescription': u'', u'pepOnOff': 1, u'bashStatus': 1, u'agentUsn': 942822, u'osName': u'Windows Server 2012', u'patternIdx': u'3F95B8098B9EEF1883B013F91C43AC72', u'employeeStatus': u'', u'tmpDevice': None, u'rebootRequired': 0, u'subnetMasks': [u'255.255.255.0', u'64'], u'minorVersion': 2, u'osservicePack': u'', u'lastSiteName': u'My Site', u'cidsEngineVersion': u'0.0.0.0', u'lastDeploymentTime': 1550585147000, u'isGrace': 0, u'computerUsn': 921686, u'agentId': u'6E5AA5CB0946C25D40C83823BB5107E6', u'cidsBrowserFfOnOff': 1, u'domainOrWorkgroup': u'WORKGROUP', u'svaId': None, u'loginDomain': u'LocalComputer', u'lastServerName': u'WIN-4OA0GKJN830', u'contentUpdate': 1, u'writeFiltersStatus': None, u'infected': 0, u'memory': 6441979904, u'osminor': 2, u'freeMem': 1933389824, u'officePhone': u'', u'lastVirusTime': 1551350764000, u'telemetryMid': u'890E283B-41D3-4340-A397-66F6AFCAF33E', u'idsVersion': u'', u'cidsBrowserIeOnOff': 1, u'publicKey': u'BgIAAACkAABSU0ExAAgAAAEAAQDfMtYpvbC2ZOrpGFbK76tuyp2MZ7/6EGsFrqAV3ZBMfvMllksVObpPYvDSc5vCjtzthb1301VADLAspayGytsdAj5z8+LLpOnJkHNg9tIunm1lLkBTitevI6G+nNjyKd7uPn3+bxjk1LL8g1exL2C2SMPEXubdUa1N5xwmhhPHp6PSIAjY74QUcNyplfvylMS9QRWoQ70mqNy9tLLef6+qCYWTqGa7QKXS0WUJs8sJMzWfCrpeMVAmU5/s3yEu+OI+9RKgOeSfy7wRzmAWHQTofjHkYGYqwXcwwLX7AbWjdcpYo0Kaecf8e5t2ZvWyR362EaNxn0HYSjpKraY1hLK1', u'quarantineDesc': u'Host Integrity check is disabled.\n Host Integrity policy has been disabled by the administrator.', u'cidsDrvMulfCode': 0, u'biosVersion': u'INTEL  - 6040000 PhoenixBIOS 4.0 Release 6.0', u'rebootReason': u'', u'telemetryHwid': u'A942D8EB-32C3-E42F-FE83-723FDC431F32', u'cidsSilentMode': 0, u'creationTime': 1550585043812, u'macAddresses': [u'00-50-56-8B-A6-C3', u'00-50-56-8B-A6-C3'], u'idsChecksum': None, u'operatingSystem': u'Windows Server 2012 ', u'osmajor': 6, u'virtualizationPlatform': u'Unknown', u'ipAddresses': [u'192.168.194.93', u'FE80:0000:0000:0000:FC67:074E:CD22:0188'], u'physicalCpus': 1, u'osBitness': u'x64', u'cidsDefsetVersion': u'190312061', u'cidsDrvOnOff': 1, u'computerName': u'WIN-4OA0GKJN830', u'logonUserName': u'Administrator', u'licenseExpiry': 0, u'osLanguage': u'en-US', u'gateways': [u'192.168.194.1', u'192.168.194.1', u'0.0.0.0', u'0.0.0.0'], u'uniqueId': u'D31AA16E0946C25D40C83823C500518B', u'department': u'', u'isNpvdiClient': 0, u'dhcpServer': u'0.0.0.0', u'description': u'', u'osflavorNumber': 79, u'tpmDevice': u'0', u'onlineStatus': 1, u'lastDownloadTime': 1551772684595, u'apOnOff': 1, u'timeZone': 480, u'fullName': u'', u'osVersion': u'6.2', u'attributeExtension': u'', u'atpServer': u'', u'tamperOnOff': 1, u'osServicePack': u'', u'agentType': u'105', u'serialNumber': u'VMware-42 0b 65 ea 0a d1 9f 7f-a1 d2 0a 58 c4 f4 ce b1', u'osElamStatus': 0, u'installType': u'0', u'profileSerialNo': u'CAD8-01/26/2019 08:00:11 062', u'hardwareKey': u'1771D79454E53469DF4B290C06C104C9', u'firewallOnOff': 1},
                            {u'profileVersion': u'14.2.1031', u'elamOnOff': 1, u'avEngineOnOff': 1, u'profileChecksum': None, u'atpDeviceId': None, u'processorType': u'Intel64 Family 6 Model 15 Stepping 1', u'oslanguage': u'en-US', u'licenseId': None, u'licenseStatus': -1, u'group': {u'domain': {u'id': u'908090000946C25D330E919313D23887', u'name': u'Default'}, u'name': u'My Company\\Group_2', u'fullPathName': None, u'externalReferenceId': None, u'source': None, u'id': u'CC00A6170946C25D35BD115E41F2F92C'}, u'uuid': u'87400B42-6E1A-D457-D45F-9804C4295C33', u'groupUpdateProvider': False, u'edrStatus': 0, u'freeDisk': 72927236096, u'diskDrive': u'c:\\', u'osFunction': u'Server', u'processorClock': 2394, u'mobilePhone': u'', u'jobTitle': u'', u'lastHeuristicThreatTime': 0, u'osname': u'Windows Server 2012', u'winServers': [u'0.0.0.0', u'0.0.0.0'], u'deploymentMessage': u'', u'idsSerialNo': u'', u'employeeNumber': u'', u'snacLicenseId': None, u'lastSiteId': u'EE75B0850946C25D5287B58B5173A37C', u'uwf': 2, u'currentClientId': u'D4B78D1E0946C25D25E6C0981F256F40', u'osbitness': u'x64', u'lastScanTime': 1552462444000, u'email': u'', u'securityVirtualAppliance': None, u'worstInfectionIdx': u'0', u'encryptedDevicePassword': None, u'lastServerId': u'7D6AAA6F0946C25D170B3A2D442500B6', u'kernel': None, u'lastUpdateTime': 1552471481568, u'ptpOnOff': 1, u'majorVersion': 14, u'lastConnectedIpAddr': u'192.168.194.93', u'agentVersion': u'14.2.1031.0100', u'deploymentRunningVersion': u'14.2.1031.0100', u'agentTimeStamp': 1552471481568, u'osfunction': u'Server', u'osMajor': 6, u'deploymentTargetVersion': u'14.2.1031.0100', u'osMinor': 2, u'osFlavorNumber': 79, u'logicalCpus': 0, u'deploymentPreVersion': u'14.2.1031.0100', u'hypervisorVendorId': u'0', u'fbwf': 2, u'osversion': u'6.2', u'dnsServers': [u'192.168.192.29', u'FEC0:0000:0000:FFFF:0000:0000:0000:0001'], u'vsicStatus': 3, u'deleted': 0, u'deploymentStatus': u'302456832', u'computerTimeStamp': 1552407060917, u'bwf': 2, u'totalDiskSpace': 81567, u'homePhone': u'', u'daOnOff': 1, u'computerDescription': u'', u'pepOnOff': 1, u'bashStatus': 1, u'agentUsn': 943464, u'osName': u'Windows Server 2012', u'patternIdx': u'3F95B8098B9EEF1883B013F91C43AC72', u'employeeStatus': u'', u'tmpDevice': None, u'rebootRequired': 0, u'subnetMasks': [u'255.255.255.0', u'64'], u'minorVersion': 2, u'osservicePack': u'', u'lastSiteName': u'My Site', u'cidsEngineVersion': u'0.0.0.0', u'lastDeploymentTime': 1551280983000, u'isGrace': 0, u'computerUsn': 927295, u'agentId': u'9530C0C30946C25D25E6C0988CF4F010', u'cidsBrowserFfOnOff': 1, u'domainOrWorkgroup': u'WORKGROUP', u'svaId': None, u'loginDomain': u'LocalComputer', u'lastServerName': u'WIN-4OA0GKJN830', u'contentUpdate': 1, u'writeFiltersStatus': None, u'infected': 0, u'memory': 4294496256, u'osminor': 2, u'freeMem': 2906599424, u'officePhone': u'', u'lastVirusTime': 1551350382000, u'telemetryMid': u'E4DCBEAE-DCCD-476C-8ECA-AEE154F0F59F', u'idsVersion': u'', u'cidsBrowserIeOnOff': 1, u'publicKey': u'BgIAAACkAABSU0ExAAgAAAEAAQAJWLeDFz6umLcsiKYxkbg+rl84pfQyjNVvzcC8dI6fqa8OzmMsuyMlDm2ShYAeNr7WkPLtDnfT/WoVDNQCHqLqgtRIZsYtWMUFLMXoq/u4RaThVlHEZiLS+tLDEcWWz/Iv75B2+5seHbeSV0/ZTVbYHLzRbTQnMetlbmKrvKXxoc1Aw5pKzTGeqqpTXczFEvLHIpHNp0SlbmPymGA5xag71CebfSLJfOu7YP2gMnnWLRPb1OTN3y0LQ0XQfTqOVNpwV8k5wJ52BRmwXSkY6HcvCQdX6GX/daV9kF3UBvd63rcau3tQI8n+GUr9rPDUlrnqYx5yWHoQI1jessq3darP', u'quarantineDesc': u'Host Integrity check is disabled.\n Host Integrity policy has been disabled by the administrator.', u'cidsDrvMulfCode': 0, u'biosVersion': u'INTEL  - 6040000 PhoenixBIOS 4.0 Release 6.0', u'rebootReason': u'', u'telemetryHwid': u'0414501C-2CC1-F574-8DAF-57BBCB2E0F34', u'cidsSilentMode': 0, u'creationTime': 1549052275576, u'macAddresses': [u'00-50-56-8B-0F-88', u'00-50-56-8B-0F-88'], u'idsChecksum': None, u'operatingSystem': u'Windows Server 2012 ', u'osmajor': 6, u'virtualizationPlatform': u'Unknown', u'ipAddresses': [u'192.168.194.93', u'FE80:0000:0000:0000:C180:8DB8:60AF:EFEC'], u'physicalCpus': 1, u'osBitness': u'x64', u'cidsDefsetVersion': u'190312061', u'cidsDrvOnOff': 1, u'computerName': u'WIN-N5KGH4CP3N3', u'logonUserName': u'Administrator', u'licenseExpiry': 0, u'osLanguage': u'en-US', u'gateways': [u'192.168.194.1', u'192.168.194.1', u'0.0.0.0', u'0.0.0.0'], u'uniqueId': u'89AD1BBB0946C25D25E6C0984E971D8A', u'department': u'', u'isNpvdiClient': 0, u'dhcpServer': u'0.0.0.0', u'description': u'', u'osflavorNumber': 79, u'tpmDevice': u'0', u'onlineStatus': 1, u'lastDownloadTime': 1551280968098, u'apOnOff': 1, u'timeZone': 480, u'fullName': u'', u'osVersion': u'6.2', u'attributeExtension': u'', u'atpServer': u'', u'tamperOnOff': 1, u'osServicePack': u'', u'agentType': u'105', u'serialNumber': u'VMware-42 0b 40 87 1a 6e 57 d4-d4 5f 98 04 c4 29 5c 33', u'osElamStatus': 0, u'installType': u'0', u'profileSerialNo': u'CC00-03/05/2019 11:50:56 570', u'hardwareKey': u'DC7D24D6465566D2941F35BC8D17801E', u'firewallOnOff': 1}],
                          u'lastPage': True, u'totalPages': 1, u'size': 20, u'totalElements': 2, u'numberOfElements': 2}
                        ),
                "hostname": ({u'sort': [{u'direction': u'ASC', u'property': u'COMPUTER_NAME', u'ascending': True}], u'number': 0, u'firstPage': True,
                          u'content': [{u'profileVersion': u'14.2.1031', u'elamOnOff': 1, u'avEngineOnOff': 1, u'profileChecksum': None, u'atpDeviceId': None, u'processorType': u'Intel64 Family 6 Model 15 Stepping 1', u'oslanguage': u'en-US', u'licenseId': None, u'licenseStatus': -1, u'group': {u'domain': {u'id': u'908090000946C25D330E919313D23887', u'name': u'Default'}, u'name': u'My Company', u'fullPathName': None, u'externalReferenceId': None, u'source': None, u'id': u'CAD80F000946C25D6C150831060AA326'}, u'uuid': u'EA650B42-D10A-7F9F-A1D2-0A58C4F4CEB1', u'groupUpdateProvider': False, u'edrStatus': 0, u'freeDisk': 52481970176, u'diskDrive': u'C:\\', u'osFunction': u'Server', u'processorClock': 2394, u'mobilePhone': u'', u'jobTitle': u'', u'lastHeuristicThreatTime': 0, u'osname': u'Windows Server 2012', u'winServers': [u'0.0.0.0', u'0.0.0.0'], u'deploymentMessage': u'', u'idsSerialNo': u'', u'employeeNumber': u'', u'snacLicenseId': None, u'lastSiteId': u'EE75B0850946C25D5287B58B5173A37C', u'uwf': 2, u'currentClientId': u'256B2B130946C25D40C83823AA2E5D4C', u'osbitness': u'x64', u'lastScanTime': 1552465622000, u'email': u'', u'securityVirtualAppliance': None, u'worstInfectionIdx': u'0', u'encryptedDevicePassword': None, u'lastServerId': u'7D6AAA6F0946C25D170B3A2D442500B6', u'kernel': None, u'lastUpdateTime': 1552471481568, u'ptpOnOff': 1, u'majorVersion': 14, u'lastConnectedIpAddr': u'192.168.194.93', u'agentVersion': u'14.2.1031.0100', u'deploymentRunningVersion': u'14.2.1031.0100', u'agentTimeStamp': 1552471481568, u'osfunction': u'Server', u'osMajor': 6, u'deploymentTargetVersion': u'14.2.1031.0100', u'osMinor': 2, u'osFlavorNumber': 79, u'logicalCpus': 0, u'deploymentPreVersion': u'', u'hypervisorVendorId': u'0', u'fbwf': 2, u'osversion': u'6.2', u'dnsServers': [u'192.168.192.29', u'FEC0:0000:0000:FFFF:0000:0000:0000:0001'], u'vsicStatus': 3, u'deleted': 0, u'deploymentStatus': u'302456832', u'computerTimeStamp': 1552388971500, u'bwf': 2, u'totalDiskSpace': 81567, u'homePhone': u'', u'daOnOff': 1, u'computerDescription': u'', u'pepOnOff': 1, u'bashStatus': 1, u'agentUsn': 942822, u'osName': u'Windows Server 2012', u'patternIdx': u'3F95B8098B9EEF1883B013F91C43AC72', u'employeeStatus': u'', u'tmpDevice': None, u'rebootRequired': 0, u'subnetMasks': [u'255.255.255.0', u'64'], u'minorVersion': 2, u'osservicePack': u'', u'lastSiteName': u'My Site', u'cidsEngineVersion': u'0.0.0.0', u'lastDeploymentTime': 1550585147000, u'isGrace': 0, u'computerUsn': 921686, u'agentId': u'6E5AA5CB0946C25D40C83823BB5107E6', u'cidsBrowserFfOnOff': 1, u'domainOrWorkgroup': u'WORKGROUP', u'svaId': None, u'loginDomain': u'LocalComputer', u'lastServerName': u'WIN-4OA0GKJN830', u'contentUpdate': 1, u'writeFiltersStatus': None, u'infected': 0, u'memory': 6441979904, u'osminor': 2, u'freeMem': 1933389824, u'officePhone': u'', u'lastVirusTime': 1551350764000, u'telemetryMid': u'890E283B-41D3-4340-A397-66F6AFCAF33E', u'idsVersion': u'', u'cidsBrowserIeOnOff': 1, u'publicKey': u'BgIAAACkAABSU0ExAAgAAAEAAQDfMtYpvbC2ZOrpGFbK76tuyp2MZ7/6EGsFrqAV3ZBMfvMllksVObpPYvDSc5vCjtzthb1301VADLAspayGytsdAj5z8+LLpOnJkHNg9tIunm1lLkBTitevI6G+nNjyKd7uPn3+bxjk1LL8g1exL2C2SMPEXubdUa1N5xwmhhPHp6PSIAjY74QUcNyplfvylMS9QRWoQ70mqNy9tLLef6+qCYWTqGa7QKXS0WUJs8sJMzWfCrpeMVAmU5/s3yEu+OI+9RKgOeSfy7wRzmAWHQTofjHkYGYqwXcwwLX7AbWjdcpYo0Kaecf8e5t2ZvWyR362EaNxn0HYSjpKraY1hLK1', u'quarantineDesc': u'Host Integrity check is disabled.\n Host Integrity policy has been disabled by the administrator.', u'cidsDrvMulfCode': 0, u'biosVersion': u'INTEL  - 6040000 PhoenixBIOS 4.0 Release 6.0', u'rebootReason': u'', u'telemetryHwid': u'A942D8EB-32C3-E42F-FE83-723FDC431F32', u'cidsSilentMode': 0, u'creationTime': 1550585043812, u'macAddresses': [u'00-50-56-8B-A6-C3', u'00-50-56-8B-A6-C3'], u'idsChecksum': None, u'operatingSystem': u'Windows Server 2012 ', u'osmajor': 6, u'virtualizationPlatform': u'Unknown', u'ipAddresses': [u'192.168.194.93', u'FE80:0000:0000:0000:FC67:074E:CD22:0188'], u'physicalCpus': 1, u'osBitness': u'x64', u'cidsDefsetVersion': u'190312061', u'cidsDrvOnOff': 1, u'computerName': u'WIN-4OA0GKJN830', u'logonUserName': u'Administrator', u'licenseExpiry': 0, u'osLanguage': u'en-US', u'gateways': [u'192.168.194.1', u'192.168.194.1', u'0.0.0.0', u'0.0.0.0'], u'uniqueId': u'D31AA16E0946C25D40C83823C500518B', u'department': u'', u'isNpvdiClient': 0, u'dhcpServer': u'0.0.0.0', u'description': u'', u'osflavorNumber': 79, u'tpmDevice': u'0', u'onlineStatus': 1, u'lastDownloadTime': 1551772684595, u'apOnOff': 1, u'timeZone': 480, u'fullName': u'', u'osVersion': u'6.2', u'attributeExtension': u'', u'atpServer': u'', u'tamperOnOff': 1, u'osServicePack': u'', u'agentType': u'105', u'serialNumber': u'VMware-42 0b 65 ea 0a d1 9f 7f-a1 d2 0a 58 c4 f4 ce b1', u'osElamStatus': 0, u'installType': u'0', u'profileSerialNo': u'CAD8-01/26/2019 08:00:11 062', u'hardwareKey': u'1771D79454E53469DF4B290C06C104C9', u'firewallOnOff': 1}],
                          u'lastPage': True, u'totalPages': 1, u'size': 20, u'totalElements': 1, u'numberOfElements': 1}
                        ),
                "non-compliant": ({u'sort': [{u'direction': u'ASC', u'property': u'COMPUTER_NAME', u'ascending': True}], u'number': 0, u'firstPage': True,
                          u'content': [{u'profileVersion': u'14.2.1031', u'elamOnOff': 0, u'avEngineOnOff': 1, u'profileChecksum': None, u'atpDeviceId': None, u'processorType': u'Intel64 Family 6 Model 15 Stepping 1', u'oslanguage': u'en-US', u'licenseId': None, u'licenseStatus': -1, u'group': {u'domain': {u'id': u'908090000946C25D330E919313D23887', u'name': u'Default'}, u'name': u'My Company', u'fullPathName': None, u'externalReferenceId': None, u'source': None, u'id': u'CAD80F000946C25D6C150831060AA326'}, u'uuid': u'EA650B42-D10A-7F9F-A1D2-0A58C4F4CEB1', u'groupUpdateProvider': False, u'edrStatus': 0, u'freeDisk': 52481970176, u'diskDrive': u'C:\\', u'osFunction': u'Server', u'processorClock': 2394, u'mobilePhone': u'', u'jobTitle': u'', u'lastHeuristicThreatTime': 0, u'osname': u'Windows Server 2012', u'winServers': [u'0.0.0.0', u'0.0.0.0'], u'deploymentMessage': u'', u'idsSerialNo': u'', u'employeeNumber': u'', u'snacLicenseId': None, u'lastSiteId': u'EE75B0850946C25D5287B58B5173A37C', u'uwf': 2, u'currentClientId': u'256B2B130946C25D40C83823AA2E5D4C', u'osbitness': u'x64', u'lastScanTime': 1552465622000, u'email': u'', u'securityVirtualAppliance': None, u'worstInfectionIdx': u'0', u'encryptedDevicePassword': None, u'lastServerId': u'7D6AAA6F0946C25D170B3A2D442500B6', u'kernel': None, u'lastUpdateTime': 1552471481568, u'ptpOnOff': 1, u'majorVersion': 14, u'lastConnectedIpAddr': u'192.168.194.93', u'agentVersion': u'14.2.1031.0100', u'deploymentRunningVersion': u'14.2.1031.0100', u'agentTimeStamp': 1552471481568, u'osfunction': u'Server', u'osMajor': 6, u'deploymentTargetVersion': u'14.2.1031.0100', u'osMinor': 2, u'osFlavorNumber': 79, u'logicalCpus': 0, u'deploymentPreVersion': u'', u'hypervisorVendorId': u'0', u'fbwf': 2, u'osversion': u'6.2', u'dnsServers': [u'192.168.192.29', u'FEC0:0000:0000:FFFF:0000:0000:0000:0001'], u'vsicStatus': 3, u'deleted': 0, u'deploymentStatus': u'302456832', u'computerTimeStamp': 1552388971500, u'bwf': 2, u'totalDiskSpace': 81567, u'homePhone': u'', u'daOnOff': 1, u'computerDescription': u'', u'pepOnOff': 1, u'bashStatus': 1, u'agentUsn': 942822, u'osName': u'Windows Server 2012', u'patternIdx': u'3F95B8098B9EEF1883B013F91C43AC72', u'employeeStatus': u'', u'tmpDevice': None, u'rebootRequired': 0, u'subnetMasks': [u'255.255.255.0', u'64'], u'minorVersion': 2, u'osservicePack': u'', u'lastSiteName': u'My Site', u'cidsEngineVersion': u'0.0.0.0', u'lastDeploymentTime': 1550585147000, u'isGrace': 0, u'computerUsn': 921686, u'agentId': u'6E5AA5CB0946C25D40C83823BB5107E6', u'cidsBrowserFfOnOff': 1, u'domainOrWorkgroup': u'WORKGROUP', u'svaId': None, u'loginDomain': u'LocalComputer', u'lastServerName': u'WIN-4OA0GKJN830', u'contentUpdate': 1, u'writeFiltersStatus': None, u'infected': 0, u'memory': 6441979904, u'osminor': 2, u'freeMem': 1933389824, u'officePhone': u'', u'lastVirusTime': 1551350764000, u'telemetryMid': u'890E283B-41D3-4340-A397-66F6AFCAF33E', u'idsVersion': u'', u'cidsBrowserIeOnOff': 1, u'publicKey': u'BgIAAACkAABSU0ExAAgAAAEAAQDfMtYpvbC2ZOrpGFbK76tuyp2MZ7/6EGsFrqAV3ZBMfvMllksVObpPYvDSc5vCjtzthb1301VADLAspayGytsdAj5z8+LLpOnJkHNg9tIunm1lLkBTitevI6G+nNjyKd7uPn3+bxjk1LL8g1exL2C2SMPEXubdUa1N5xwmhhPHp6PSIAjY74QUcNyplfvylMS9QRWoQ70mqNy9tLLef6+qCYWTqGa7QKXS0WUJs8sJMzWfCrpeMVAmU5/s3yEu+OI+9RKgOeSfy7wRzmAWHQTofjHkYGYqwXcwwLX7AbWjdcpYo0Kaecf8e5t2ZvWyR362EaNxn0HYSjpKraY1hLK1', u'quarantineDesc': u'Host Integrity check is disabled.\n Host Integrity policy has been disabled by the administrator.', u'cidsDrvMulfCode': 0, u'biosVersion': u'INTEL  - 6040000 PhoenixBIOS 4.0 Release 6.0', u'rebootReason': u'', u'telemetryHwid': u'A942D8EB-32C3-E42F-FE83-723FDC431F32', u'cidsSilentMode': 0, u'creationTime': 1550585043812, u'macAddresses': [u'00-50-56-8B-A6-C3', u'00-50-56-8B-A6-C3'], u'idsChecksum': None, u'operatingSystem': u'Windows Server 2012 ', u'osmajor': 6, u'virtualizationPlatform': u'Unknown', u'ipAddresses': [u'192.168.194.93', u'FE80:0000:0000:0000:FC67:074E:CD22:0188'], u'physicalCpus': 1, u'osBitness': u'x64', u'cidsDefsetVersion': u'190312061', u'cidsDrvOnOff': 1, u'computerName': u'WIN-4OA0GKJN830', u'logonUserName': u'Administrator', u'licenseExpiry': 0, u'osLanguage': u'en-US', u'gateways': [u'192.168.194.1', u'192.168.194.1', u'0.0.0.0', u'0.0.0.0'], u'uniqueId': u'D31AA16E0946C25D40C83823C500518B', u'department': u'', u'isNpvdiClient': 0, u'dhcpServer': u'0.0.0.0', u'description': u'', u'osflavorNumber': 79, u'tpmDevice': u'0', u'onlineStatus': 0, u'lastDownloadTime': 1551772684595, u'apOnOff': 1, u'timeZone': 480, u'fullName': u'', u'osVersion': u'6.2', u'attributeExtension': u'', u'atpServer': u'', u'tamperOnOff': 1, u'osServicePack': u'', u'agentType': u'105', u'serialNumber': u'VMware-42 0b 65 ea 0a d1 9f 7f-a1 d2 0a 58 c4 f4 ce b1', u'osElamStatus': 0, u'installType': u'0', u'profileSerialNo': u'CAD8-01/26/2019 08:00:11 062', u'hardwareKey': u'1771D79454E53469DF4B290C06C104C9', u'firewallOnOff': 1},
                            {u'profileVersion': u'14.2.1031', u'elamOnOff': 1, u'avEngineOnOff': 1, u'profileChecksum': None, u'atpDeviceId': None, u'processorType': u'Intel64 Family 6 Model 15 Stepping 1', u'oslanguage': u'en-US', u'licenseId': None, u'licenseStatus': -1, u'group': {u'domain': {u'id': u'908090000946C25D330E919313D23887', u'name': u'Default'}, u'name': u'My Company\\Group_2', u'fullPathName': None, u'externalReferenceId': None, u'source': None, u'id': u'CC00A6170946C25D35BD115E41F2F92C'}, u'uuid': u'87400B42-6E1A-D457-D45F-9804C4295C33', u'groupUpdateProvider': False, u'edrStatus': 0, u'freeDisk': 72927236096, u'diskDrive': u'c:\\', u'osFunction': u'Server', u'processorClock': 2394, u'mobilePhone': u'', u'jobTitle': u'', u'lastHeuristicThreatTime': 0, u'osname': u'Windows Server 2012', u'winServers': [u'0.0.0.0', u'0.0.0.0'], u'deploymentMessage': u'', u'idsSerialNo': u'', u'employeeNumber': u'', u'snacLicenseId': None, u'lastSiteId': u'EE75B0850946C25D5287B58B5173A37C', u'uwf': 2, u'currentClientId': u'D4B78D1E0946C25D25E6C0981F256F40', u'osbitness': u'x64', u'lastScanTime': 1552462444000, u'email': u'', u'securityVirtualAppliance': None, u'worstInfectionIdx': u'0', u'encryptedDevicePassword': None, u'lastServerId': u'7D6AAA6F0946C25D170B3A2D442500B6', u'kernel': None, u'lastUpdateTime': 1552471481568, u'ptpOnOff': 1, u'majorVersion': 14, u'lastConnectedIpAddr': u'192.168.194.93', u'agentVersion': u'14.2.1031.0100', u'deploymentRunningVersion': u'14.2.1031.0100', u'agentTimeStamp': 1552471481568, u'osfunction': u'Server', u'osMajor': 6, u'deploymentTargetVersion': u'14.2.1031.0100', u'osMinor': 2, u'osFlavorNumber': 79, u'logicalCpus': 0, u'deploymentPreVersion': u'14.2.1031.0100', u'hypervisorVendorId': u'0', u'fbwf': 2, u'osversion': u'6.2', u'dnsServers': [u'192.168.192.29', u'FEC0:0000:0000:FFFF:0000:0000:0000:0001'], u'vsicStatus': 3, u'deleted': 0, u'deploymentStatus': u'302456832', u'computerTimeStamp': 1552407060917, u'bwf': 2, u'totalDiskSpace': 81567, u'homePhone': u'', u'daOnOff': 1, u'computerDescription': u'', u'pepOnOff': 1, u'bashStatus': 1, u'agentUsn': 943464, u'osName': u'Windows Server 2012', u'patternIdx': u'3F95B8098B9EEF1883B013F91C43AC72', u'employeeStatus': u'', u'tmpDevice': None, u'rebootRequired': 0, u'subnetMasks': [u'255.255.255.0', u'64'], u'minorVersion': 2, u'osservicePack': u'', u'lastSiteName': u'My Site', u'cidsEngineVersion': u'0.0.0.0', u'lastDeploymentTime': 1551280983000, u'isGrace': 0, u'computerUsn': 927295, u'agentId': u'9530C0C30946C25D25E6C0988CF4F010', u'cidsBrowserFfOnOff': 1, u'domainOrWorkgroup': u'WORKGROUP', u'svaId': None, u'loginDomain': u'LocalComputer', u'lastServerName': u'WIN-4OA0GKJN830', u'contentUpdate': 1, u'writeFiltersStatus': None, u'infected': 0, u'memory': 4294496256, u'osminor': 2, u'freeMem': 2906599424, u'officePhone': u'', u'lastVirusTime': 1551350382000, u'telemetryMid': u'E4DCBEAE-DCCD-476C-8ECA-AEE154F0F59F', u'idsVersion': u'', u'cidsBrowserIeOnOff': 1, u'publicKey': u'BgIAAACkAABSU0ExAAgAAAEAAQAJWLeDFz6umLcsiKYxkbg+rl84pfQyjNVvzcC8dI6fqa8OzmMsuyMlDm2ShYAeNr7WkPLtDnfT/WoVDNQCHqLqgtRIZsYtWMUFLMXoq/u4RaThVlHEZiLS+tLDEcWWz/Iv75B2+5seHbeSV0/ZTVbYHLzRbTQnMetlbmKrvKXxoc1Aw5pKzTGeqqpTXczFEvLHIpHNp0SlbmPymGA5xag71CebfSLJfOu7YP2gMnnWLRPb1OTN3y0LQ0XQfTqOVNpwV8k5wJ52BRmwXSkY6HcvCQdX6GX/daV9kF3UBvd63rcau3tQI8n+GUr9rPDUlrnqYx5yWHoQI1jessq3darP', u'quarantineDesc': u'Host Integrity check is disabled.\n Host Integrity policy has been disabled by the administrator.', u'cidsDrvMulfCode': 0, u'biosVersion': u'INTEL  - 6040000 PhoenixBIOS 4.0 Release 6.0', u'rebootReason': u'', u'telemetryHwid': u'0414501C-2CC1-F574-8DAF-57BBCB2E0F34', u'cidsSilentMode': 0, u'creationTime': 1549052275576, u'macAddresses': [u'00-50-56-8B-0F-88', u'00-50-56-8B-0F-88'], u'idsChecksum': None, u'operatingSystem': u'Windows Server 2012 ', u'osmajor': 6, u'virtualizationPlatform': u'Unknown', u'ipAddresses': [u'192.168.194.93', u'FE80:0000:0000:0000:C180:8DB8:60AF:EFEC'], u'physicalCpus': 1, u'osBitness': u'x64', u'cidsDefsetVersion': u'190312061', u'cidsDrvOnOff': 1, u'computerName': u'WIN-N5KGH4CP3N3', u'logonUserName': u'Administrator', u'licenseExpiry': 0, u'osLanguage': u'en-US', u'gateways': [u'192.168.194.1', u'192.168.194.1', u'0.0.0.0', u'0.0.0.0'], u'uniqueId': u'89AD1BBB0946C25D25E6C0984E971D8A', u'department': u'', u'isNpvdiClient': 0, u'dhcpServer': u'0.0.0.0', u'description': u'', u'osflavorNumber': 79, u'tpmDevice': u'0', u'onlineStatus': 1, u'lastDownloadTime': 1551280968098, u'apOnOff': 1, u'timeZone': 480, u'fullName': u'', u'osVersion': u'6.2', u'attributeExtension': u'', u'atpServer': u'', u'tamperOnOff': 1, u'osServicePack': u'', u'agentType': u'105', u'serialNumber': u'VMware-42 0b 40 87 1a 6e 57 d4-d4 5f 98 04 c4 29 5c 33', u'osElamStatus': 0, u'installType': u'0', u'profileSerialNo': u'CC00-03/05/2019 11:50:56 570', u'hardwareKey': u'DC7D24D6465566D2941F35BC8D17801E', u'firewallOnOff': 1}],
                          u'lastPage': True, u'totalPages': 1, u'size': 2, u'totalElements': 2, u'numberOfElements': 2}
                        )

                }

    return response[type]

def get_groups():
    response = {u'sort': [{u'direction': u'ASC', u'property': u'NAME', u'ascending': True}], u'number': 0, u'firstPage': False,
                 u'content': [{u'policyDate': 1556542282626, u'domain': {u'id': u'908090000946C25D330E919313D23887', u'name': u'Default'},
                               u'numberOfRegisteredUsers': 0, u'description': u'', u'created': 1548481072007,
                               u'policySerialNumber': u'4CBD-04/29/2019 12:51:22 626', u'lastModified': 1548481072007,
                               u'fullPathName': u'My Company\\Default Group', u'createdBy': u'AF3C39A10A320801000000DBF200C60A',
                               u'numberOfPhysicalComputers': 0, u'customIpsNumber': u'', u'id': u'4CBD63EE0946C25D1011DB1872A1736A',
                               u'policyInheritanceEnabled': True, u'name': u'Default Group'},
                              {u'policyDate': 1556542282626, u'domain': {u'id': u'908090000946C25D330E919313D23887', u'name': u'Default'},
                               u'numberOfRegisteredUsers': 0, u'description': u'', u'created': 1551787280561,
                               u'policySerialNumber': u'36E0-04/29/2019 12:51:22 626', u'lastModified': 1551787280561,
                               u'fullPathName': u'My Company\\G_0027', u'createdBy': u'AF3C39A10A320801000000DBF200C60A',
                               u'numberOfPhysicalComputers': 0, u'customIpsNumber': u'', u'id': u'36E0B28B0946C25D06A29515DE448CF6',
                               u'policyInheritanceEnabled': True, u'name': u'G_0027'}
                              ],
                 u'lastPage': True,
                 u'totalPages': 1,
                 u'size': 2,
                 u'totalElements': 2,
                 u'numberOfElements': 2}

    return response

def get_policies_summary():
    response = {u'sort': None, u'number': 0, u'firstPage': True, u'content':
        [{u'domainid': u'908090000946C25D330E919313D23887', u'name': u'Firewall policy', u'subtype': None, u'enabled': True, u'sources': [], u'assignedtocloudgroups': None, u'policytype': u'fw', u'assignedtolocations': [{u'defaultLocationId': u'EC7E378A0946C25D39A1D3E8C5FB589B', u'locationIds': [u'EC7E378A0946C25D39A1D3E8C5FB589B'], u'groupId': u'CAD80F000946C25D6C150831060AA326'}], u'id': u'846A39040946C25D3AA897754E2EC515', u'desc': u'Created automatically during product installation.'},
         {u'domainid': u'908090000946C25D330E919313D23887', u'name': u'Quarantine Firewall policy', u'subtype': None, u'enabled': True, u'sources': [], u'assignedtocloudgroups': None, u'policytype': u'fw', u'assignedtolocations': None, u'id': u'2867FBA60946C25D300A05176DC01DE0', u'desc': u'Created automatically during product installation.'}], u'lastPage': True, u'totalPages': 1, u'size': 2, u'totalElements': 2, u'numberOfElements': 2}
    return response

def move_endpoint():
    response = [{u'responseMessage': u'OK', u'responseCode': u'200'}]
    return response

def quarantine_endpoints():
    response = {'commandID_computer': '09114E42730A479993DD6D94CF9CAA53'}
    return response

def scan_endpoints():
    response = {u'commandID_computer': u'0F0CBDD7EDFF4634B23FA11F5AB81FFC',
                u'commandID_group': u'BB37F78894DB451B8E8921EC127667A3'}
    return response

def get_command_status():
    response = {u'sort': [{u'direction': u'ASC', u'property': u'Begintime', u'ascending': True}], u'number': 0,
                u'firstPage': True,
                u'content': [{u'computerName': u'johnq1', u'subStateId': 0, u'binaryFileId': None, u'lastUpdateTime': None,
                   u'domainName': u'Default', u'hardwareKey': u'B791D1DF2BB8AA77D19B10E3BB395B81',
                   u'subStateDesc': None, u'stateId': 0, u'computerId': u'236A7100A9FE9DC50A4F1AC2819C158E',
                   u'computerIp': u'192.168.56.104', u'beginTime': None, u'currentLoginUserName': u'root',
                   u'resultInXML': None}, {u'computerName': u'WIN-N5KGH4CP3N3', u'subStateId': 0, u'binaryFileId': None,
                                           u'lastUpdateTime': u'2019-06-06T10:45:39Z', u'domainName': u'Default',
                                           u'hardwareKey': u'DC7D24D6465566D2941F35BC8D17801E', u'subStateDesc': u'',
                                           u'stateId': 3, u'computerId': u'89AD1BBB0946C25D25E6C0984E971D8A',
                                           u'computerIp': u'192.168.194.93', u'beginTime': u'2019-06-06T10:42:37Z',
                                           u'currentLoginUserName': u'Administrator',
                                           u'resultInXML': u'<EOC creator="Resilient" version="1.0" id="id">\n    <DataSource name="name" id="id" version="version"/>\n    <ScanType>QUICK_SCAN</ScanType>\n    <Threat time="" severity="" type="" category="">\n        <Description>Scan eoc for for suspicious hash of type Malware MD5 Hash and value 582F9B6E0CC4C1DBBD772AAAF088CB3A in the SEP environment.</Description>\n        <URL></URL>\n        <User></User>\n        <Attacker>\n        </Attacker>\n        <proxy ip=""/>\n        <Application></Application>\n    </Threat>\n    <Activity>\n        <OS id="0" name="name" version="version">\n            <Process>\n            </Process>\n            <Files>\n                <File name="" action="create">\n                    <Matched result="NO_MATCH"/></File>\n                <File name="" action="create">\n                    <Matched result="NO_MATCH"/></File>\n                <File name="" action="create">\n                    <Hash name="MD5" value="582f9b6e0cc4c1dbbd772aaaf088cb3a"/>\n                    <Matched result="NO_MATCH"/></File>\n            </Files>\n            <Registry>\n            </Registry>\n            <Network/>\n        </OS>\n    </Activity>\n</EOC>'},
                  {u'computerName': u'jqbf957root', u'subStateId': 0, u'binaryFileId': None,
                   u'lastUpdateTime': u'2019-06-06T10:53:53Z', u'domainName': u'Default',
                   u'hardwareKey': u'9FACFF634F892674CA3BF7EE995B565D', u'subStateDesc': u'', u'stateId': 3,
                   u'computerId': u'5FA95F22A9FE9DC50A4F1AC22197CDF4', u'computerIp': u'192.168.166.16',
                   u'beginTime': u'2019-06-06T10:42:37Z', u'currentLoginUserName': u'Administrator',
                   u'resultInXML': u'<EOC creator="Resilient" version="1.0" id="id">\n    <DataSource name="name" id="id" version="version"/>\n    <ScanType>QUICK_SCAN</ScanType>\n    <Threat time="" severity="" type="" category="">\n        <Description>Scan eoc for for suspicious hash of type Malware MD5 Hash and value 582F9B6E0CC4C1DBBD772AAAF088CB3A in the SEP environment.</Description>\n        <URL></URL>\n        <User></User>\n        <Attacker>\n        </Attacker>\n        <proxy ip=""/>\n        <Application></Application>\n    </Threat>\n    <Activity>\n        <OS id="0" name="name" version="version">\n            <Process>\n            </Process>\n            <Files>\n                <File name="" action="create">\n                    <Matched result="NO_MATCH"/></File>\n                <File name="" action="create">\n                    <Matched result="NO_MATCH"/></File>\n                <File name="" action="create">\n                    <Hash name="MD5" value="582f9b6e0cc4c1dbbd772aaaf088cb3a"/>\n                    <Matched result="NO_MATCH"/></File>\n            </Files>\n            <Registry>\n            </Registry>\n            <Network/>\n        </OS>\n    </Activity>\n</EOC>'},
                  {u'computerName': u'WIN-4OA0GKJN830', u'subStateId': 0, u'binaryFileId': None,
                   u'lastUpdateTime': u'2019-06-06T10:50:35Z', u'domainName': u'Default',
                   u'hardwareKey': u'1771D79454E53469DF4B290C06C104C9', u'subStateDesc': u'', u'stateId': 3,
                   u'computerId': u'D31AA16E0946C25D40C83823C500518B', u'computerIp': u'192.168.194.93',
                   u'beginTime': u'2019-06-06T10:42:39Z', u'currentLoginUserName': u'Administrator',
                   u'resultInXML': u'<EOC creator="Resilient" version="1.0" id="id">\n    <DataSource name="name" id="id" version="version"/>\n    <ScanType>QUICK_SCAN</ScanType>\n    <Threat time="" severity="" type="" category="">\n        <Description>Scan eoc for for suspicious hash of type Malware MD5 Hash and value 582F9B6E0CC4C1DBBD772AAAF088CB3A in the SEP environment.</Description>\n        <URL></URL>\n        <User></User>\n        <Attacker>\n        </Attacker>\n        <proxy ip=""/>\n        <Application></Application>\n    </Threat>\n    <Activity>\n        <OS id="0" name="name" version="version">\n            <Process>\n            </Process>\n            <Files>\n                <File name="" action="create">\n                    <Matched result="NO_MATCH"/></File>\n                <File name="" action="create">\n                    <Matched result="NO_MATCH"/></File>\n                <File name="" action="create">\n                    <Hash name="MD5" value="582f9b6e0cc4c1dbbd772aaaf088cb3a"/>\n                    <Matched result="NO_MATCH"/></File>\n            </Files>\n            <Registry>\n            </Registry>\n            <Network/>\n        </OS>\n    </Activity>\n</EOC>'}],
                u'lastPage': True, u'totalPages': 1, u'size': 20, u'totalElements': 4, u'numberOfElements': 4}
    return response

def get_command_status_processed():
    response =  {u'sort': [{u'direction': u'ASC', u'property': u'Begintime', u'ascending': True}], 'total_match_ep_count': 2,
                'total_remediation_count': 0, 'total_ep_count': 4, u'number': 0, u'firstPage': True, 'total_match_count': 2,
                u'content': [{u'computerName': u'WIN-N5KGH4CP3N3', u'subStateId': 0, u'binaryFileId': None,
                              u'lastUpdateTime': u'2019-06-06T11:56:31Z', u'domainName': u'Default',
                              u'hardwareKey': u'DC7D24D6465566D2941F35BC8D17801E', u'subStateDesc': u'', u'stateId': 3,
                              'scan_result': {'match_count': 1, 'remediation_count': 0, 'PARTIAL_MATCHES': [], 'HASH_MATCHES': [],
                                              'artifact_type': 'File Name',
                                              'FULL_MATCHES': [{'hashType': 'SHA256', 'hashValue': 'b82758fc5f737a58078d3c60e2798a70d895443a86aa39adf52dec70e98c2bed',
                                                                'result': 'FULL_MATCH', 'value': 'C:\\temp\\My_file_1.txt'}],
                                              'artifact_value': 'C:\\temp\\My_file_1.txt', 'MATCH': True}, u'computerId': u'89AD1BBB0946C25D25E6C0984E971D8A',
                              u'computerIp': u'192.168.194.93', u'beginTime': u'2019-06-06T11:56:26Z', u'currentLoginUserName': u'Administrator', 
                              u'resultInXML': u'<EOC creator="Resilient" version="1.0" id="id">\n    <DataSource name="name" id="id" version="version"/>\n    <ScanType>QUICK_SCAN</ScanType>\n    <Threat time="" severity="" type="" category="">\n        <Description>Scan eoc for for suspicious hash of type File Path and value C:\\temp\\My_file_1.txt in the SEP environment.</Description>\n        <URL></URL>\n        <User></User>\n        <Attacker>\n        </Attacker>\n        <proxy ip=""/>\n        <Application></Application>\n    </Threat>\n    <Activity>\n        <OS id="0" name="name" version="version">\n            <Process>\n            </Process>\n            <Files>\n                <File name="C:\\temp\\My_file_1.txt" action="create">\n                    <Matched result="FULL_MATCH" value="C:\\temp\\My_file_1.txt" hashType="SHA256" hashValue="b82758fc5f737a58078d3c60e2798a70d895443a86aa39adf52dec70e98c2bed"/></File>\n                <File name="C:\\temp\\My_file_1.txt" action="create">\n                    <Matched result="FULL_MATCH" value="C:\\temp\\My_file_1.txt" hashType="SHA256" hashValue="b82758fc5f737a58078d3c60e2798a70d895443a86aa39adf52dec70e98c2bed"/></File>\n                <File name="C:\\temp\\My_file_1.txt" action="create">\n                    <Matched result="FULL_MATCH" value="C:\\temp\\My_file_1.txt" hashType="SHA256" hashValue="b82758fc5f737a58078d3c60e2798a70d895443a86aa39adf52dec70e98c2bed"/></File>\n            </Files>\n            <Registry>\n            </Registry>\n            <Network/>\n        </OS>\n    </Activity>\n</EOC>'},
                             {u'computerName': u'WIN-4OA0GKJN830', u'subStateId': 0, u'binaryFileId': None,
                              u'lastUpdateTime': u'2019-06-06T11:56:32Z', u'domainName': u'Default',
                              u'hardwareKey': u'1771D79454E53469DF4B290C06C104C9', u'subStateDesc': u'', u'stateId': 3, 
                              'scan_result': {'match_count': 1, 'remediation_count': 0, 'PARTIAL_MATCHES': [], 'HASH_MATCHES': [], 
                                              'artifact_type': 'File Name', 
                                              'FULL_MATCHES': [{'hashType': 'SHA256', 'hashValue': 'b82758fc5f737a58078d3c60e2798a70d895443a86aa39adf52dec70e98c2bed', 
                                                                'result': 'FULL_MATCH', 'value': 'C:\\temp\\My_file_1.txt'}], 
                                              'artifact_value': 'C:\\temp\\My_file_1.txt', 'MATCH': True}, u'computerId': u'D31AA16E0946C25D40C83823C500518B', 
                              u'computerIp': u'192.168.194.93', u'beginTime': u'2019-06-06T11:56:27Z', u'currentLoginUserName': u'Administrator', 
                              u'resultInXML': u'<EOC creator="Resilient" version="1.0" id="id">\n    <DataSource name="name" id="id" version="version"/>\n    <ScanType>QUICK_SCAN</ScanType>\n    <Threat time="" severity="" type="" category="">\n        <Description>Scan eoc for for suspicious hash of type File Path and value C:\\temp\\My_file_1.txt in the SEP environment.</Description>\n        <URL></URL>\n        <User></User>\n        <Attacker>\n        </Attacker>\n        <proxy ip=""/>\n        <Application></Application>\n    </Threat>\n    <Activity>\n        <OS id="0" name="name" version="version">\n            <Process>\n            </Process>\n            <Files>\n                <File name="C:\\temp\\My_file_1.txt" action="create">\n                    <Matched result="FULL_MATCH" value="C:\\temp\\My_file_1.txt" hashType="SHA256" hashValue="b82758fc5f737a58078d3c60e2798a70d895443a86aa39adf52dec70e98c2bed"/></File>\n                <File name="C:\\temp\\My_file_1.txt" action="create">\n                    <Matched result="FULL_MATCH" value="C:\\temp\\My_file_1.txt" hashType="SHA256" hashValue="b82758fc5f737a58078d3c60e2798a70d895443a86aa39adf52dec70e98c2bed"/></File>\n                <File name="C:\\temp\\My_file_1.txt" action="create">\n                    <Matched result="FULL_MATCH" value="C:\\temp\\My_file_1.txt" hashType="SHA256" hashValue="b82758fc5f737a58078d3c60e2798a70d895443a86aa39adf52dec70e98c2bed"/></File>\n            </Files>\n            <Registry>\n            </Registry>\n            <Network/>\n        </OS>\n    </Activity>\n</EOC>'}
                             ], 
                 u'lastPage': True, 'total_remediation_ep_count': 0, u'totalPages': 1, u'size': 20, u'totalElements': 2, 
                 'total_not_completed': 1, 'overall_command_state': 'In progress', u'numberOfElements': 2
                 }
    return response



def get_file_content():
    response = "SGkgdGhlcmU="
    return response

def upload_file():
    response = {"commandID": "171969C124D54C069D7018914AA02184"}
    return response

def post_res_att(file_name, incident_id):
    return dict({u'task_at_id': None, u'vers': 2, u'name': file_name,
                 u'task_id': None, u'created': 1531959479048, u'inc_owner': 4,
                 u'task_members': None, u'task_custom': None, u'task_name': None,
                 u'actions': [], u'inc_name': u'BigFix', u'creator_id': 4,
                 u'content_type': u'text/plain', u'inc_id': incident_id, u'type': u'incident',
                 u'id': 1, u'size': 37261
                }
    )

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

        def get_policies_summary(self, policy_type=None, domainid=None):
            return get_policies_summary()

        def move_endpoint(self, groupid, hardwarekey):
            return move_endpoint()

        def quarantine_endpoints(self, group_ids=None, computer_ids=None, undo=None):
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
                elif re.match("^https://192.168.1.2:8446/sepm/api/v1/policies/summary", args[1]):
                    return get_policies_summary()
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


def get_mock_config():
    config_data = u"""[fn_cisco_amp4ep]
base_path=/sepm/api/v1
auth_path=/sepm/api/v1/identity/authenticate
host=192.168.1.2
port=8446
username=admin
password=password
domain=Default
results_limit=6
"""
    return config_data
