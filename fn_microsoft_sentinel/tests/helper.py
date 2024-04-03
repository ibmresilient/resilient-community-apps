# -*- coding: utf-8 -*-
"""Helper for tests"""

PACKAGE_NAME = "fn_microsoft_sentinel"

config_data = '''
[fn_microsoft_sentinel]
azure_url = https://management.azure.com
tenant_id = bbb-ccc-aaa
client_id = bbb-ddd-aaa
app_secret = bbb-eee-aaa
polling_lookback = 120
polling_interval = 0
api_version = 2023-11-01
sentinel_profiles = profile_a
verify = false

[fn_microsoft_sentinel:profile_a]
subscription_id = bbb-fff-bbb
workspace_name = AzureWorkspace
resource_groupname = GroupName
max_alerts = 50
new_incident_filters = "status": ["New", "Active"], "severity": ["High", "Medium","Low"]
close_soar_case=true
'''

def create_comment_results():
    return {
        "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/demoassets/providers/Microsoft.OperationalInsights/workspaces/AzureSentinelDemo/providers/Microsoft.SecurityInsights/Incidents/e5a310d8-a920-428c-ba13-e04300c1d50c/Comments/253d7028-c522-11ee-98a9-fa89897771d7",
        "name": "253d7028-c522-11ee-98a9-fa89897771d7",
        "etag": "\"0602009e-0000-0100-0000-65c2820f0000\"",
        "type": "Microsoft.SecurityInsights/Incidents/Comments",
        "properties": {
            "message": "From IBM SOAR:\nTest comment",
            "createdTimeUtc": "2024-02-06T19:01:35.2742397Z",
            "lastModifiedTimeUtc": "2024-02-06T19:01:35.2742397Z",
            "author": {
                "objectId": "fb5360be-0c6a-4260-ae69-9b07dd735441",
                "email": None,
                "name": "Comment created from external application - MS Sentinel",
                "userPrincipalName": None
            }
        }
    }

def get_incident_alerts_results():
    return {
        "value": [
            {
                "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/demoassets/providers/Microsoft.OperationalInsights/workspaces/AzureSentinelDemo/providers/Microsoft.SecurityInsights/Entities/ec7cd79e-dd28-5e7b-094d-af3574027758",
                "name": "ec7cd79e-dd28-5e7b-094d-af3574027758",
                "type": "Microsoft.SecurityInsights/Entities",
                "kind": "SecurityAlert",
                "properties": {
                    "systemAlertId": "ec7cd79e-dd28-5e7b-094d-af3574027758",
                    "tactics": [
                        "PreAttack"
                    ],
                    "alertDisplayName": "Suspected brute-force attack attempt",
                    "description": "Brute-force attack is a common attack technique for finding valid credentials to the database. By submitting many users/passwords combinations, an attacker can guess a correct one.\r\nOnce obtained, an attacker can have full access to the database. While this specific alert doesn't indicate a successful brute-force, it is advised to take safety measures to protect your resource against this attack.\r\nTo investigate this suspected brute-force attempt, review it's origin (based on the application name and IP/Location), and try to find out whether it's recognized to you, or suspicious.\r\nIf you believe this to be an attack on your database, use firewall rules to limit the access to your resource, and make sure you use strong passwords and not well known user names.\r\nAlso, consider using only AAD authentication to further enhance your security posture.\r\n",
                    "remediationSteps": [
                        "* Apply [workflow automation](https://go.microsoft.com/fwlink/?linkid=2174808) to block future attacks.",
                        "* Consider [blocking the IP address](https://go.microsoft.com/fwlink/?linkid=2099055) of the attacking client and hardening your firewall.",
                        "* When possible, use [Windows authentication](https://go.microsoft.com/fwlink/?linkid=2129121) and disable SQL Server authentication.",
                        "* Use [strong passwords](https://go.microsoft.com/fwlink/?linkid=2099068) and avoid reusing them across multiple databases.",
                        "* If applicable, disable default and well known application/database accounts such as SA."
                    ],
                    "confidenceLevel": "Unknown",
                    "severity": "High",
                    "vendorName": "Microsoft",
                    "productName": "Azure Security Center",
                    "productComponentName": "Databases",
                    "alertType": "SQL.VM_BruteForce",
                    "processingEndTime": "2024-02-06T19:03:15.7566188Z",
                    "status": "New",
                    "endTimeUtc": "2024-02-06T19:02:44Z",
                    "startTimeUtc": "2024-02-06T19:02:44Z",
                    "timeGenerated": "2024-02-06T19:03:17.5439712Z",
                    "compromisedEntity": "PAMSqlSv",
                    "providerAlertId": "2516950546359999999_bd8e4a80-5adb-4012-95de-8efeae6973cd",
                    "alertLink": "https://portal.azure.com/#blade/Microsoft_Azure_Security_AzureDefenderForData/AlertBlade/alertId/2516950546359999999_bd8e4a80-5adb-4012-95de-8efeae6973cd/subscriptionId/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroup/DemoAssets/referencedFrom/alertDeepLink/location/centralus",
                    "resourceIdentifiers": [
                        {
                            "type": "AzureResource",
                            "resourceId": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/DemoAssets/providers/Microsoft.Compute/virtualMachines/PAMSqlSv",
                            "subscriptionId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
                        },
                        {
                            "type": "LogAnalytics",
                            "workspaceId": "c6c712b0-dc3d-4408-945a-4bde1db6579b",
                            "subscriptionId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                            "agentId": "7db452ea-1cae-4079-94a5-85dc76156e96"
                        }
                    ],
                    "additionalData": {
                        "MTP_Classification": "Unknown",
                        "StoreAlertPublisher": "{\"Succeeded\":true,\"Reason\":null,\"PublishTime\":\"2024-02-06T19:03:16.660682Z\"}",
                        "AlertMessageEnqueueTime": "2024-02-06T19:03:17.588Z",
                        "OriginalProductName": "Azure Security Center",
                        "OriginalProductComponentName": "Databases",
                        "effectiveSubscriptionId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
                    },
                    "friendlyName": "Suspected brute-force attack attempt",
                    "timeGenerated_ms": 1707246197000
                }
            }
        ]
    }

def get_incident_comments_results():
    return {
        "value": [
            {
                "id": "/subscriptions/a4b7e24a-xxxx-4d84-xxxx-89e99b336784/resourceGroups/demoassets/providers/Microsoft.OperationalInsights/workspaces/AzureSentinelDemo/providers/Microsoft.SecurityInsights/Incidents/6c98642b-7248-4b4d-994e-32443f100e78/Comments/cdd41cd8-7d4e-4b7a-976f-f409938fe791",
                "name": "cdd41cd8-7d4e-4b7a-976f-f409938fe791",
                "type": "Microsoft.SecurityInsights/Incidents/Comments",
                "properties": {
                    "message": "bye",
                    "createdTimeUtc": "2023-03-13T17:19:47.2791036Z",
                    "author": {
                        "objectId": "43dd7b73-6a70-475e-88c3-609a9f30b514",
                        "email": "admin@example.com",
                        "name": "Admin",
                        "userPrincipalName": "admin@example.com"
                    }
                }
            }
        ]
    }

def get_incident_alert_entities_results():
    return {
        "value": {
            "entities": [
                {
                    "id": "/subscriptions/a4b7e24a-xxxx-4d84-xxxx-89e99b336784/resourceGroups/demoassets/providers/Microsoft.OperationalInsights/workspaces/AzureSentinelDemo/providers/Microsoft.SecurityInsights/entities/fca87582-43c0-5af8-fdec-dfda212ee53c",
                    "name": "fca87582-43c0-5af8-fdec-dfda212ee53c",
                    "type": "Microsoft.SecurityInsights/entities",
                    "kind": "Ip",
                    "properties": {
                        "address": "1.1.1.1",
                        "friendlyName": "1.1.1.1"
                    },
                    "soar_artifact_type": "IP Address",
                    "resilient_artifact_value": "1.1.1.1"
                },
                {
                    "id": "/subscriptions/a4b7e24a-xxxx-4d84-xxxx-89e99b336784/resourceGroups/demoassets/providers/Microsoft.OperationalInsights/workspaces/AzureSentinelDemo/providers/Microsoft.SecurityInsights/entities/fd328c82-310e-6bb5-1d3b-f1c635dd5f20",
                    "name": "fd328c82-310e-6bb5-1d3b-f1c635dd5f20",
                    "type": "Microsoft.SecurityInsights/entities",
                    "kind": "AzureResource",
                    "properties": {
                        "resourceId": "/subscriptions/a4b7e24a-xxxx-4d84-xxxx-89e99b336784/resourcegroups/demoassets/providers/microsoft.compute/virtualmachines/logforwarder",
                        "subscriptionId": "a4b7e24a-xxxx-4d84-xxxx-89e99b336784",
                        "friendlyName": "logforwarder"
                    },
                    "soar_artifact_type": "String",
                    "resilient_artifact_value": "logforwarder"
                },
                {
                    "id": "/subscriptions/a4b7e24a-xxxx-4d84-xxxx-89e99b336784/resourceGroups/demoassets/providers/Microsoft.OperationalInsights/workspaces/AzureSentinelDemo/providers/Microsoft.SecurityInsights/entities/a41bc108-5e1e-7f62-4294-7412e5319c81",
                    "name": "a41bc108-5e1e-7f62-4294-7412e5319c81",
                    "type": "Microsoft.SecurityInsights/entities",
                    "kind": "Host",
                    "properties": {
                        "azureID": "/subscriptions/a4b7e24a-xxxx-4d84-xxxx-89e99b336784/resourcegroups/demoassets/providers/microsoft.compute/virtualmachines/logforwarder",
                        "friendlyName": "/subscriptions/a4b7e24a-xxxx-4d84-xxxx-89e99b336784/resourcegroups/demoassets/providers/microsoft.compute/virtualmachines/logforwarder"
                    },
                    "soar_artifact_type": "System Name",
                    "resilient_artifact_value": "/subscriptions/a4b7e24a-xxxx-4d84-xxxx-89e99b336784/resourcegroups/demoassets/providers/microsoft.compute/virtualmachines/logforwarder"
                }
            ]
        }
    }

def update_incident_results():
    return {
        "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/demoassets/providers/Microsoft.OperationalInsights/workspaces/AzureSentinelDemo/providers/Microsoft.SecurityInsights/Incidents/e5a310d8-a920-428c-ba13-e04300c1d50c",
        "name": "e5a310d8-a920-428c-ba13-e04300c1d50c",
        "etag": "\"06022ab4-0000-0100-0000-65c2829b0000\"",
        "type": "Microsoft.SecurityInsights/Incidents",
        "properties": {
            "title": "Suspected brute-force attack attempt",
            "description": "Brute-force attack is a common attack technique for finding valid credentials to the database. By submitting many users/passwords combinations, an attacker can guess a correct one. Once obtained, an attacker can have full access to the database. While this specific alert doesn't indicate a successful brute-force, it is advised to take safety measures to protect your resource against this attack. To investigate this suspected brute-force attempt, review it's origin (based on the application name and IP/Location), and try to find out whether it's recognized to you, or suspicious. If you believe this to be an attack on your database, use firewall rules to limit the access to your resource, and make sure you use strong passwords and not well known user names. Also, consider using only AAD authentication to further enhance your security posture.",
            "severity": "Medium",
            "status": "New",
            "owner": {
                "objectId": None,
                "email": None,
                "assignedTo": None,
                "userPrincipalName": None
            },
            "labels": [],
            "lastModifiedTimeUtc": "2024-02-06T19:03:55.9750177Z",
            "createdTimeUtc": "2024-02-06T18:31:01.9288406Z",
            "incidentNumber": 3946,
            "additionalData": {
                "alertsCount": 1,
                "bookmarksCount": 0,
                "commentsCount": 1,
                "alertProductNames": [
                    "Azure Security Center"
                ],
                "tactics": [
                     "PreAttack"
                ]
            },
            "relatedAnalyticRuleIds": [
                "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/demoassets/providers/Microsoft.OperationalInsights/workspaces/AzureSentinelDemo/providers/Microsoft.SecurityInsights/alertRules/14fefa89-3cdd-429f-923b-b524aa8c65c3"
            ],
            "incidentUrl": "https://portal.azure.com/#asset/Microsoft_Azure_Security_Insights/Incident/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/demoassets/providers/Microsoft.OperationalInsights/workspaces/AzureSentinelDemo/providers/Microsoft.SecurityInsights/Incidents/e5a310d8-a920-428c-ba13-e04300c1d50c",
            "providerName": "Azure Sentinel",
            "providerIncidentId": "3946"
        }
    }

def get_incident_entities_results():
    return {
        "value": [
            {
                'id': '/subscriptions/a4b7e24a-xxxx-4d84-xxxx-89e99b336784/resourceGroups/demoassets/providers/Microsoft.OperationalInsights/workspaces/AzureSentinelDemo/providers/Microsoft.SecurityInsights/Incidents/6c98642b-7248-4b4d-994e-32443f100e78/relations/6c98642b-7248-4b4d-994e-32443f100e78_8a2fe554-9e4e-8298-cd70-4159a5494b7e',
                'name': '6c98642b-7248-4b4d-994e-32443f100e78_8a2fe554-9e4e-8298-cd70-4159a5494b7e',
                'type': 'Microsoft.SecurityInsights/Incidents/relations',
                'properties': {
                    'relatedResourceId': '/subscriptions/a4b7e24a-xxxx-4d84-xxxx-89e99b336784/resourceGroups/demoassets/providers/Microsoft.OperationalInsights/workspaces/AzureSentinelDemo/providers/Microsoft.SecurityInsights/entities/8a2fe554-9e4e-8298-cd70-4159a5494b7e',
                    'relatedResourceName': '8a2fe554-9e4e-8298-cd70-4159a5494b7e',
                    'relatedResourceType': 'Microsoft.SecurityInsights/entities',
                    'relatedResourceKind': 'SecurityAlert'
                }
            }
        ]
    }

def sentinel_get_incident_entities_results():
    return {
        "6c98642b-7248-4b4d-994e-32443f100e78_8a2fe554-9e4e-8298-cd70-4159a5494b7e": [
            {
                "id": "/subscriptions/a4b7e24a-xxxx-4d84-xxxx-89e99b336784/resourceGroups/demoassets/providers/Microsoft.OperationalInsights/workspaces/AzureSentinelDemo/providers/Microsoft.SecurityInsights/entities/fca87582-43c0-5af8-fdec-dfda212ee53c",
                "name": "fca87582-43c0-5af8-fdec-dfda212ee53c",
                "type": "Microsoft.SecurityInsights/entities",
                "kind": "Ip",
                "properties": {
                    "address": "1.1.1.1",
                    "friendlyName": "1.1.1.1"
                },
                "soar_artifact_type": "IP Address",
                "resilient_artifact_value": "1.1.1.1"
            },
            {
                "id": "/subscriptions/a4b7e24a-xxxx-4d84-xxxx-89e99b336784/resourceGroups/demoassets/providers/Microsoft.OperationalInsights/workspaces/AzureSentinelDemo/providers/Microsoft.SecurityInsights/entities/fd328c82-310e-6bb5-1d3b-f1c635dd5f20",
                "name": "fd328c82-310e-6bb5-1d3b-f1c635dd5f20",
                "type": "Microsoft.SecurityInsights/entities",
                "kind": "AzureResource",
                "properties": {
                    "resourceId": "/subscriptions/a4b7e24a-xxxx-4d84-xxxx-89e99b336784/resourcegroups/demoassets/providers/microsoft.compute/virtualmachines/logforwarder",
                    "subscriptionId": "a4b7e24a-xxxx-4d84-xxxx-89e99b336784",
                    "friendlyName": "logforwarder"
                },
                "soar_artifact_type": "String",
                "resilient_artifact_value": "logforwarder"
            },
            {
                "id": "/subscriptions/a4b7e24a-xxxx-4d84-xxxx-89e99b336784/resourceGroups/demoassets/providers/Microsoft.OperationalInsights/workspaces/AzureSentinelDemo/providers/Microsoft.SecurityInsights/entities/a41bc108-5e1e-7f62-4294-7412e5319c81",
                "name": "a41bc108-5e1e-7f62-4294-7412e5319c81",
                "type": "Microsoft.SecurityInsights/entities",
                "kind": "Host",
                "properties": {
                    "azureID": "/subscriptions/a4b7e24a-xxxx-4d84-xxxx-89e99b336784/resourcegroups/demoassets/providers/microsoft.compute/virtualmachines/logforwarder",
                    "friendlyName": "/subscriptions/a4b7e24a-xxxx-4d84-xxxx-89e99b336784/resourcegroups/demoassets/providers/microsoft.compute/virtualmachines/logforwarder"
                },
                "soar_artifact_type": "System Name",
                "resilient_artifact_value": "/subscriptions/a4b7e24a-xxxx-4d84-xxxx-89e99b336784/resourcegroups/demoassets/providers/microsoft.compute/virtualmachines/logforwarder"
            }
        ]
    }

def soar_incident_mock():
    return {
        'name': 'Sentinel Incident 3972 - Suspicious authentication activity on one endpoint',
        'description': '<div>None</div>',
        'phase_id': 'Respond',
        'vers': 14,
        'properties': {
            'sentinel_incident_assigned_to': 'None',
            'sentinel_incident_classification': '',
            'sentinel_incident_id': '3972',
            'sentinel_incident_classification_reason': '',
            'sentinel_incident_tactics': 'InitialAccess',
            'sentinel_profile': 'profile_a',
            'sentinel_incident_classification_comment': '',
            'internal_customizations_field': None,
            'sentinel_incident_url': '<a href="https://portal.azure.com/#asset/Microsoft_Azure_Security_Insights/Incident/subscriptions/a4b7e24a-xxxx-4d84-xxxx-89e99b336784/resourceGroups/demoassets/providers/Microsoft.OperationalInsights/workspaces/AzureSentinelDemo/providers/Microsoft.SecurityInsights/Incidents/63f75ad5-bee4-4fe3-aeb6-43d0df142713">Sentinel Incident</a>',
            'sentinel_incident_labels': '',
            'sentinel_incident_number':'63f75ad5-bee4-4fe3-aeb6-43d0df142713',
            'sentinel_incident_status': 'Active'
        },
        'resolution_id': None,
        'resolution_summary': None,
        'severity_code': "Medium",
        'plan_status': 'A'
    }

class MockSOAR:
    """ Mock SOAR connection """
    def __init__(self, rest_client):
        """ Mock """
        pass
    
    def filter_resilient_comments(self, incident_id, sentinel_comments):
        """ Mock filter_resilient_comments results """
        return get_incident_comments_results().get("value", [])
    
    def get_soar_incident(self, incident_id):
        """ Mock get_soar_incident results """
        return soar_incident_mock()

class MockClient:
    """ Add Mock connection data """

    def __init__(self, opts, options):
        """ Mock """
        pass

    def create_comment(self, profile_data, sentinel_incident_id, note):
        """ Mock create_comment results """
        return create_comment_results(), True, ""
    
    def get_incident_alerts(self, profile_data, sentinel_incident_id):
        """ Mock get_incident_alert results """
        return get_incident_alerts_results(), True, ""
    
    def get_comments(self, profile_data, sentinel_incident_id):
        """ Mock get_comments results """
        return get_incident_comments_results(), True, ""
    
    def get_incident_alert_entities(self, alert_url):
        """ Mock get_incident_alert_entities results """
        return get_incident_alert_entities_results(), True, ""
    
    def get_incident_entities(self, profile_data, sentinel_incident_id):
        """ Mock get_incident_entities results """
        return get_incident_entities_results(), True, ""
    
    def create_update_incident(self, profile_data, sentinel_incident_id, incident_payload):
        """ Mock create_update_incident results """
        return update_incident_results(), True, ""
