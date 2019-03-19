# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
"""Generate Mock responses to simulate Cisco AMP for endpoinst for Unit and function tests """
import time
import re

from requests import HTTPError
from requests.models import Response

# Responses for standalone tests
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
                          u'content': [{u'profileVersion': u'14.2.1031', u'elamOnOff': 1, u'avEngineOnOff': 1, u'profileChecksum': None, u'atpDeviceId': None, u'processorType': u'Intel64 Family 6 Model 15 Stepping 1', u'oslanguage': u'en-US', u'licenseId': None, u'licenseStatus': -1, u'group': {u'domain': {u'id': u'908090000946C25D330E919313D23887', u'name': u'Default'}, u'name': u'My Company', u'fullPathName': None, u'externalReferenceId': None, u'source': None, u'id': u'CAD80F000946C25D6C150831060AA326'}, u'uuid': u'EA650B42-D10A-7F9F-A1D2-0A58C4F4CEB1', u'groupUpdateProvider': False, u'edrStatus': 0, u'freeDisk': 52481970176, u'diskDrive': u'C:\\', u'osFunction': u'Server', u'processorClock': 2394, u'mobilePhone': u'', u'jobTitle': u'', u'lastHeuristicThreatTime': 0, u'osname': u'Windows Server 2012', u'winServers': [u'0.0.0.0', u'0.0.0.0'], u'deploymentMessage': u'', u'idsSerialNo': u'', u'employeeNumber': u'', u'snacLicenseId': None, u'lastSiteId': u'EE75B0850946C25D5287B58B5173A37C', u'uwf': 2, u'currentClientId': u'256B2B130946C25D40C83823AA2E5D4C', u'osbitness': u'x64', u'lastScanTime': 1552465622000, u'email': u'', u'securityVirtualAppliance': None, u'worstInfectionIdx': u'0', u'encryptedDevicePassword': None, u'lastServerId': u'7D6AAA6F0946C25D170B3A2D442500B6', u'kernel': None, u'lastUpdateTime': 1552471481568, u'ptpOnOff': 1, u'majorVersion': 14, u'lastConnectedIpAddr': u'9.70.194.93', u'agentVersion': u'14.2.1031.0100', u'deploymentRunningVersion': u'14.2.1031.0100', u'agentTimeStamp': 1552471481568, u'osfunction': u'Server', u'osMajor': 6, u'deploymentTargetVersion': u'14.2.1031.0100', u'osMinor': 2, u'osFlavorNumber': 79, u'logicalCpus': 0, u'deploymentPreVersion': u'', u'hypervisorVendorId': u'0', u'fbwf': 2, u'osversion': u'6.2', u'dnsServers': [u'9.70.192.29', u'FEC0:0000:0000:FFFF:0000:0000:0000:0001'], u'vsicStatus': 3, u'deleted': 0, u'deploymentStatus': u'302456832', u'computerTimeStamp': 1552388971500, u'bwf': 2, u'totalDiskSpace': 81567, u'homePhone': u'', u'daOnOff': 1, u'computerDescription': u'', u'pepOnOff': 1, u'bashStatus': 1, u'agentUsn': 942822, u'osName': u'Windows Server 2012', u'patternIdx': u'3F95B8098B9EEF1883B013F91C43AC72', u'employeeStatus': u'', u'tmpDevice': None, u'rebootRequired': 0, u'subnetMasks': [u'255.255.255.0', u'64'], u'minorVersion': 2, u'osservicePack': u'', u'lastSiteName': u'My Site', u'cidsEngineVersion': u'0.0.0.0', u'lastDeploymentTime': 1550585147000, u'isGrace': 0, u'computerUsn': 921686, u'agentId': u'6E5AA5CB0946C25D40C83823BB5107E6', u'cidsBrowserFfOnOff': 1, u'domainOrWorkgroup': u'WORKGROUP', u'svaId': None, u'loginDomain': u'LocalComputer', u'lastServerName': u'WIN-4OA0GKJN830', u'contentUpdate': 1, u'writeFiltersStatus': None, u'infected': 0, u'memory': 6441979904, u'osminor': 2, u'freeMem': 1933389824, u'officePhone': u'', u'lastVirusTime': 1551350764000, u'telemetryMid': u'890E283B-41D3-4340-A397-66F6AFCAF33E', u'idsVersion': u'', u'cidsBrowserIeOnOff': 1, u'publicKey': u'BgIAAACkAABSU0ExAAgAAAEAAQDfMtYpvbC2ZOrpGFbK76tuyp2MZ7/6EGsFrqAV3ZBMfvMllksVObpPYvDSc5vCjtzthb1301VADLAspayGytsdAj5z8+LLpOnJkHNg9tIunm1lLkBTitevI6G+nNjyKd7uPn3+bxjk1LL8g1exL2C2SMPEXubdUa1N5xwmhhPHp6PSIAjY74QUcNyplfvylMS9QRWoQ70mqNy9tLLef6+qCYWTqGa7QKXS0WUJs8sJMzWfCrpeMVAmU5/s3yEu+OI+9RKgOeSfy7wRzmAWHQTofjHkYGYqwXcwwLX7AbWjdcpYo0Kaecf8e5t2ZvWyR362EaNxn0HYSjpKraY1hLK1', u'quarantineDesc': u'Host Integrity check is disabled.\n Host Integrity policy has been disabled by the administrator.', u'cidsDrvMulfCode': 0, u'biosVersion': u'INTEL  - 6040000 PhoenixBIOS 4.0 Release 6.0', u'rebootReason': u'', u'telemetryHwid': u'A942D8EB-32C3-E42F-FE83-723FDC431F32', u'cidsSilentMode': 0, u'creationTime': 1550585043812, u'macAddresses': [u'00-50-56-8B-A6-C3', u'00-50-56-8B-A6-C3'], u'idsChecksum': None, u'operatingSystem': u'Windows Server 2012 ', u'osmajor': 6, u'virtualizationPlatform': u'Unknown', u'ipAddresses': [u'9.70.194.93', u'FE80:0000:0000:0000:FC67:074E:CD22:0188'], u'physicalCpus': 1, u'osBitness': u'x64', u'cidsDefsetVersion': u'190312061', u'cidsDrvOnOff': 1, u'computerName': u'WIN-4OA0GKJN830', u'logonUserName': u'Administrator', u'licenseExpiry': 0, u'osLanguage': u'en-US', u'gateways': [u'9.70.194.1', u'9.70.194.1', u'0.0.0.0', u'0.0.0.0'], u'uniqueId': u'D31AA16E0946C25D40C83823C500518B', u'department': u'', u'isNpvdiClient': 0, u'dhcpServer': u'0.0.0.0', u'description': u'', u'osflavorNumber': 79, u'tpmDevice': u'0', u'onlineStatus': 1, u'lastDownloadTime': 1551772684595, u'apOnOff': 1, u'timeZone': 480, u'fullName': u'', u'osVersion': u'6.2', u'attributeExtension': u'', u'atpServer': u'', u'tamperOnOff': 1, u'osServicePack': u'', u'agentType': u'105', u'serialNumber': u'VMware-42 0b 65 ea 0a d1 9f 7f-a1 d2 0a 58 c4 f4 ce b1', u'osElamStatus': 0, u'installType': u'0', u'profileSerialNo': u'CAD8-01/26/2019 08:00:11 062', u'hardwareKey': u'1771D79454E53469DF4B290C06C104C9', u'firewallOnOff': 1},
                            {u'profileVersion': u'14.2.1031', u'elamOnOff': 1, u'avEngineOnOff': 1, u'profileChecksum': None, u'atpDeviceId': None, u'processorType': u'Intel64 Family 6 Model 15 Stepping 1', u'oslanguage': u'en-US', u'licenseId': None, u'licenseStatus': -1, u'group': {u'domain': {u'id': u'908090000946C25D330E919313D23887', u'name': u'Default'}, u'name': u'My Company\\Group_2', u'fullPathName': None, u'externalReferenceId': None, u'source': None, u'id': u'CC00A6170946C25D35BD115E41F2F92C'}, u'uuid': u'87400B42-6E1A-D457-D45F-9804C4295C33', u'groupUpdateProvider': False, u'edrStatus': 0, u'freeDisk': 72927236096, u'diskDrive': u'c:\\', u'osFunction': u'Server', u'processorClock': 2394, u'mobilePhone': u'', u'jobTitle': u'', u'lastHeuristicThreatTime': 0, u'osname': u'Windows Server 2012', u'winServers': [u'0.0.0.0', u'0.0.0.0'], u'deploymentMessage': u'', u'idsSerialNo': u'', u'employeeNumber': u'', u'snacLicenseId': None, u'lastSiteId': u'EE75B0850946C25D5287B58B5173A37C', u'uwf': 2, u'currentClientId': u'D4B78D1E0946C25D25E6C0981F256F40', u'osbitness': u'x64', u'lastScanTime': 1552462444000, u'email': u'', u'securityVirtualAppliance': None, u'worstInfectionIdx': u'0', u'encryptedDevicePassword': None, u'lastServerId': u'7D6AAA6F0946C25D170B3A2D442500B6', u'kernel': None, u'lastUpdateTime': 1552471481568, u'ptpOnOff': 1, u'majorVersion': 14, u'lastConnectedIpAddr': u'9.70.194.94', u'agentVersion': u'14.2.1031.0100', u'deploymentRunningVersion': u'14.2.1031.0100', u'agentTimeStamp': 1552471481568, u'osfunction': u'Server', u'osMajor': 6, u'deploymentTargetVersion': u'14.2.1031.0100', u'osMinor': 2, u'osFlavorNumber': 79, u'logicalCpus': 0, u'deploymentPreVersion': u'14.2.1031.0100', u'hypervisorVendorId': u'0', u'fbwf': 2, u'osversion': u'6.2', u'dnsServers': [u'9.70.192.29', u'FEC0:0000:0000:FFFF:0000:0000:0000:0001'], u'vsicStatus': 3, u'deleted': 0, u'deploymentStatus': u'302456832', u'computerTimeStamp': 1552407060917, u'bwf': 2, u'totalDiskSpace': 81567, u'homePhone': u'', u'daOnOff': 1, u'computerDescription': u'', u'pepOnOff': 1, u'bashStatus': 1, u'agentUsn': 943464, u'osName': u'Windows Server 2012', u'patternIdx': u'3F95B8098B9EEF1883B013F91C43AC72', u'employeeStatus': u'', u'tmpDevice': None, u'rebootRequired': 0, u'subnetMasks': [u'255.255.255.0', u'64'], u'minorVersion': 2, u'osservicePack': u'', u'lastSiteName': u'My Site', u'cidsEngineVersion': u'0.0.0.0', u'lastDeploymentTime': 1551280983000, u'isGrace': 0, u'computerUsn': 927295, u'agentId': u'9530C0C30946C25D25E6C0988CF4F010', u'cidsBrowserFfOnOff': 1, u'domainOrWorkgroup': u'WORKGROUP', u'svaId': None, u'loginDomain': u'LocalComputer', u'lastServerName': u'WIN-4OA0GKJN830', u'contentUpdate': 1, u'writeFiltersStatus': None, u'infected': 0, u'memory': 4294496256, u'osminor': 2, u'freeMem': 2906599424, u'officePhone': u'', u'lastVirusTime': 1551350382000, u'telemetryMid': u'E4DCBEAE-DCCD-476C-8ECA-AEE154F0F59F', u'idsVersion': u'', u'cidsBrowserIeOnOff': 1, u'publicKey': u'BgIAAACkAABSU0ExAAgAAAEAAQAJWLeDFz6umLcsiKYxkbg+rl84pfQyjNVvzcC8dI6fqa8OzmMsuyMlDm2ShYAeNr7WkPLtDnfT/WoVDNQCHqLqgtRIZsYtWMUFLMXoq/u4RaThVlHEZiLS+tLDEcWWz/Iv75B2+5seHbeSV0/ZTVbYHLzRbTQnMetlbmKrvKXxoc1Aw5pKzTGeqqpTXczFEvLHIpHNp0SlbmPymGA5xag71CebfSLJfOu7YP2gMnnWLRPb1OTN3y0LQ0XQfTqOVNpwV8k5wJ52BRmwXSkY6HcvCQdX6GX/daV9kF3UBvd63rcau3tQI8n+GUr9rPDUlrnqYx5yWHoQI1jessq3darP', u'quarantineDesc': u'Host Integrity check is disabled.\n Host Integrity policy has been disabled by the administrator.', u'cidsDrvMulfCode': 0, u'biosVersion': u'INTEL  - 6040000 PhoenixBIOS 4.0 Release 6.0', u'rebootReason': u'', u'telemetryHwid': u'0414501C-2CC1-F574-8DAF-57BBCB2E0F34', u'cidsSilentMode': 0, u'creationTime': 1549052275576, u'macAddresses': [u'00-50-56-8B-0F-88', u'00-50-56-8B-0F-88'], u'idsChecksum': None, u'operatingSystem': u'Windows Server 2012 ', u'osmajor': 6, u'virtualizationPlatform': u'Unknown', u'ipAddresses': [u'9.70.194.94', u'FE80:0000:0000:0000:C180:8DB8:60AF:EFEC'], u'physicalCpus': 1, u'osBitness': u'x64', u'cidsDefsetVersion': u'190312061', u'cidsDrvOnOff': 1, u'computerName': u'WIN-N5KGH4CP3N3', u'logonUserName': u'Administrator', u'licenseExpiry': 0, u'osLanguage': u'en-US', u'gateways': [u'9.70.194.1', u'9.70.194.1', u'0.0.0.0', u'0.0.0.0'], u'uniqueId': u'89AD1BBB0946C25D25E6C0984E971D8A', u'department': u'', u'isNpvdiClient': 0, u'dhcpServer': u'0.0.0.0', u'description': u'', u'osflavorNumber': 79, u'tpmDevice': u'0', u'onlineStatus': 1, u'lastDownloadTime': 1551280968098, u'apOnOff': 1, u'timeZone': 480, u'fullName': u'', u'osVersion': u'6.2', u'attributeExtension': u'', u'atpServer': u'', u'tamperOnOff': 1, u'osServicePack': u'', u'agentType': u'105', u'serialNumber': u'VMware-42 0b 40 87 1a 6e 57 d4-d4 5f 98 04 c4 29 5c 33', u'osElamStatus': 0, u'installType': u'0', u'profileSerialNo': u'CC00-03/05/2019 11:50:56 570', u'hardwareKey': u'DC7D24D6465566D2941F35BC8D17801E', u'firewallOnOff': 1}],
                          u'lastPage': True, u'totalPages': 1, u'size': 20, u'totalElements': 2, u'numberOfElements': 2}
                        ),
                "hostname": ({u'sort': [{u'direction': u'ASC', u'property': u'COMPUTER_NAME', u'ascending': True}], u'number': 0, u'firstPage': True,
                          u'content': [{u'profileVersion': u'14.2.1031', u'elamOnOff': 1, u'avEngineOnOff': 1, u'profileChecksum': None, u'atpDeviceId': None, u'processorType': u'Intel64 Family 6 Model 15 Stepping 1', u'oslanguage': u'en-US', u'licenseId': None, u'licenseStatus': -1, u'group': {u'domain': {u'id': u'908090000946C25D330E919313D23887', u'name': u'Default'}, u'name': u'My Company', u'fullPathName': None, u'externalReferenceId': None, u'source': None, u'id': u'CAD80F000946C25D6C150831060AA326'}, u'uuid': u'EA650B42-D10A-7F9F-A1D2-0A58C4F4CEB1', u'groupUpdateProvider': False, u'edrStatus': 0, u'freeDisk': 52481970176, u'diskDrive': u'C:\\', u'osFunction': u'Server', u'processorClock': 2394, u'mobilePhone': u'', u'jobTitle': u'', u'lastHeuristicThreatTime': 0, u'osname': u'Windows Server 2012', u'winServers': [u'0.0.0.0', u'0.0.0.0'], u'deploymentMessage': u'', u'idsSerialNo': u'', u'employeeNumber': u'', u'snacLicenseId': None, u'lastSiteId': u'EE75B0850946C25D5287B58B5173A37C', u'uwf': 2, u'currentClientId': u'256B2B130946C25D40C83823AA2E5D4C', u'osbitness': u'x64', u'lastScanTime': 1552465622000, u'email': u'', u'securityVirtualAppliance': None, u'worstInfectionIdx': u'0', u'encryptedDevicePassword': None, u'lastServerId': u'7D6AAA6F0946C25D170B3A2D442500B6', u'kernel': None, u'lastUpdateTime': 1552471481568, u'ptpOnOff': 1, u'majorVersion': 14, u'lastConnectedIpAddr': u'9.70.194.93', u'agentVersion': u'14.2.1031.0100', u'deploymentRunningVersion': u'14.2.1031.0100', u'agentTimeStamp': 1552471481568, u'osfunction': u'Server', u'osMajor': 6, u'deploymentTargetVersion': u'14.2.1031.0100', u'osMinor': 2, u'osFlavorNumber': 79, u'logicalCpus': 0, u'deploymentPreVersion': u'', u'hypervisorVendorId': u'0', u'fbwf': 2, u'osversion': u'6.2', u'dnsServers': [u'9.70.192.29', u'FEC0:0000:0000:FFFF:0000:0000:0000:0001'], u'vsicStatus': 3, u'deleted': 0, u'deploymentStatus': u'302456832', u'computerTimeStamp': 1552388971500, u'bwf': 2, u'totalDiskSpace': 81567, u'homePhone': u'', u'daOnOff': 1, u'computerDescription': u'', u'pepOnOff': 1, u'bashStatus': 1, u'agentUsn': 942822, u'osName': u'Windows Server 2012', u'patternIdx': u'3F95B8098B9EEF1883B013F91C43AC72', u'employeeStatus': u'', u'tmpDevice': None, u'rebootRequired': 0, u'subnetMasks': [u'255.255.255.0', u'64'], u'minorVersion': 2, u'osservicePack': u'', u'lastSiteName': u'My Site', u'cidsEngineVersion': u'0.0.0.0', u'lastDeploymentTime': 1550585147000, u'isGrace': 0, u'computerUsn': 921686, u'agentId': u'6E5AA5CB0946C25D40C83823BB5107E6', u'cidsBrowserFfOnOff': 1, u'domainOrWorkgroup': u'WORKGROUP', u'svaId': None, u'loginDomain': u'LocalComputer', u'lastServerName': u'WIN-4OA0GKJN830', u'contentUpdate': 1, u'writeFiltersStatus': None, u'infected': 0, u'memory': 6441979904, u'osminor': 2, u'freeMem': 1933389824, u'officePhone': u'', u'lastVirusTime': 1551350764000, u'telemetryMid': u'890E283B-41D3-4340-A397-66F6AFCAF33E', u'idsVersion': u'', u'cidsBrowserIeOnOff': 1, u'publicKey': u'BgIAAACkAABSU0ExAAgAAAEAAQDfMtYpvbC2ZOrpGFbK76tuyp2MZ7/6EGsFrqAV3ZBMfvMllksVObpPYvDSc5vCjtzthb1301VADLAspayGytsdAj5z8+LLpOnJkHNg9tIunm1lLkBTitevI6G+nNjyKd7uPn3+bxjk1LL8g1exL2C2SMPEXubdUa1N5xwmhhPHp6PSIAjY74QUcNyplfvylMS9QRWoQ70mqNy9tLLef6+qCYWTqGa7QKXS0WUJs8sJMzWfCrpeMVAmU5/s3yEu+OI+9RKgOeSfy7wRzmAWHQTofjHkYGYqwXcwwLX7AbWjdcpYo0Kaecf8e5t2ZvWyR362EaNxn0HYSjpKraY1hLK1', u'quarantineDesc': u'Host Integrity check is disabled.\n Host Integrity policy has been disabled by the administrator.', u'cidsDrvMulfCode': 0, u'biosVersion': u'INTEL  - 6040000 PhoenixBIOS 4.0 Release 6.0', u'rebootReason': u'', u'telemetryHwid': u'A942D8EB-32C3-E42F-FE83-723FDC431F32', u'cidsSilentMode': 0, u'creationTime': 1550585043812, u'macAddresses': [u'00-50-56-8B-A6-C3', u'00-50-56-8B-A6-C3'], u'idsChecksum': None, u'operatingSystem': u'Windows Server 2012 ', u'osmajor': 6, u'virtualizationPlatform': u'Unknown', u'ipAddresses': [u'9.70.194.93', u'FE80:0000:0000:0000:FC67:074E:CD22:0188'], u'physicalCpus': 1, u'osBitness': u'x64', u'cidsDefsetVersion': u'190312061', u'cidsDrvOnOff': 1, u'computerName': u'WIN-4OA0GKJN830', u'logonUserName': u'Administrator', u'licenseExpiry': 0, u'osLanguage': u'en-US', u'gateways': [u'9.70.194.1', u'9.70.194.1', u'0.0.0.0', u'0.0.0.0'], u'uniqueId': u'D31AA16E0946C25D40C83823C500518B', u'department': u'', u'isNpvdiClient': 0, u'dhcpServer': u'0.0.0.0', u'description': u'', u'osflavorNumber': 79, u'tpmDevice': u'0', u'onlineStatus': 1, u'lastDownloadTime': 1551772684595, u'apOnOff': 1, u'timeZone': 480, u'fullName': u'', u'osVersion': u'6.2', u'attributeExtension': u'', u'atpServer': u'', u'tamperOnOff': 1, u'osServicePack': u'', u'agentType': u'105', u'serialNumber': u'VMware-42 0b 65 ea 0a d1 9f 7f-a1 d2 0a 58 c4 f4 ce b1', u'osElamStatus': 0, u'installType': u'0', u'profileSerialNo': u'CAD8-01/26/2019 08:00:11 062', u'hardwareKey': u'1771D79454E53469DF4B290C06C104C9', u'firewallOnOff': 1}],
                          u'lastPage': True, u'totalPages': 1, u'size': 20, u'totalElements': 1, u'numberOfElements': 1}
                        )
                }

    return response[type]

def get_groups():
    response = None
    return response

def get_policies_summary():
    response = {u'sort': None, u'number': 0, u'firstPage': True, u'content':
        [{u'domainid': u'908090000946C25D330E919313D23887', u'name': u'Firewall policy', u'subtype': None, u'enabled': True, u'sources': [], u'assignedtocloudgroups': None, u'policytype': u'fw', u'assignedtolocations': [{u'defaultLocationId': u'EC7E378A0946C25D39A1D3E8C5FB589B', u'locationIds': [u'EC7E378A0946C25D39A1D3E8C5FB589B'], u'groupId': u'CAD80F000946C25D6C150831060AA326'}], u'id': u'846A39040946C25D3AA897754E2EC515', u'desc': u'Created automatically during product installation.'},
         {u'domainid': u'908090000946C25D330E919313D23887', u'name': u'Quarantine Firewall policy', u'subtype': None, u'enabled': True, u'sources': [], u'assignedtocloudgroups': None, u'policytype': u'fw', u'assignedtolocations': None, u'id': u'2867FBA60946C25D300A05176DC01DE0', u'desc': u'Created automatically during product installation.'}], u'lastPage': True, u'totalPages': 1, u'size': 2, u'totalElements': 2, u'numberOfElements': 2}
    return response

def move_client():
    response = [{u'responseMessage': u'OK', u'responseCode': u'200'}]
    return response

def mocked_sep_client(*args):

    class MockResponse:
        """Class will be used by the mock to replace amp_client in circuits tests"""
        def __init__(self, *arg):
            self.r = Response()

        def __contains__(self, key):
            return True if key in self.__dict__.keys() else False

        def get_computers(self, computername=None, domain=None, lastupdate=None, order=None, os=None, pageindex=None,
                      pagesize=None, sort=None):
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

        def move_client(self, group_id, hardwarekey):
            return move_client()
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
            elif args[0].lower() == "get":
                if re.match("^https://192.168.1.2:8446/sepm/api/v1/version$", args[1]):
                    return get_version()
                elif re.match("^https://192.168.1.2:8446/sepm/api/v1/domains$", args[1]):
                    return get_domains()
                elif re.match("^https://192.168.1.2:8446/sepm/api/v1/computers$", args[1]):
                    return get_computers()
                elif re.match("^https://192.168.1.2:8446/sepm/api/v1/groups$", args[1]):
                    return get_groups()
                elif re.match("^https://192.168.1.2:8446/sepm/api/v1/policies/summary", args[1]):
                    return get_policies_summary()
            elif args[0].lower() == "patch":
                if re.match("^https://192.168.1.2:8446/sepm/api/v1/computers$", args[1]):
                    return move_client()

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
"""
    return config_data
