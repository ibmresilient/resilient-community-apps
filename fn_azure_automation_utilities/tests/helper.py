# -*- coding: utf-8 -*-
"""Helper for tests"""

PACKAGE_NAME = "fn_azure_automation_utilities"

config_data = """
[fn_azure_automation_utilities]
client_id=6193123c-ff2b-0366-933f-609dbdhse76f
client_secret=VmshQ~D_gt~dBFOxNlwrdsPwwU-vREmkdgGLAaLt
tenant_id=50bfhd3e-b999-434d-834d-13b87c68047b
subscription_id=a4b7eera-c7aa-4l04-8s8e-89e99dk46784
token_url=https://login.microsoftonline.com/50bfhd3e-b999-434d-834d-13b87c68047b/oauth2/v2.0/token
auth_url=https://login.microsoftonline.com/50bfhd3e-b999-434d-834d-13b87c68047b/oauth2/v2.0/authorize
scope = https://management.azure.com/user_impersonation openid profile offline_access
refresh_token = 0.AXwAdjrtUIm4TUOALRO4kr8Ee7zHLGYr_9
"""

def create_update_results():
    return {
        "name": "test-account",
        "systemData": {
            "createdAt": "2023-07-25T12:23:38.673+00:00",
            "lastModifiedAt": "2023-07-25T12:23:38.673+00:00"
        },
        "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/test-account",
        "type": "Microsoft.Automation/AutomationAccounts",
        "location": "East US 2",
        "tags": {},
        "etag": None,
        "properties": {
            "publicNetworkAccess": True,
            "disableLocalAuth": False,
            "sku": {
                "name": "Basic",
                "family": None,
                "capacity": None
            },
            "state": "Ok",
            "RegistrationUrl": "https://6eac8d3a-7fa7-4eda-8874-3b85d74365bc.agentsvc.eus2.azure-automation.net/accounts/6eac8d3a-7fa7-4eda-8874-3b85d74365bc",
            "encryption": {
                "keySource": "Microsoft.Automation",
                "identity": {
                    "userAssignedIdentity": None
                }
            },
            "automationHybridServiceUrl": "https://6eac8d3a-7fa7-4eda-8874-3b85d74365bc.jrds.eus2.azure-automation.net/automationAccounts/6eac8d3a-7fa7-4eda-8874-3b85d74365bc",
            "RuntimeConfiguration": {
                "powershell": {
                    "builtinModules": {
                        "Az": "8.0.0"
                    }
                },
                    "powershell7": {
                        "builtinModules": {
                            "Az": "8.0.0"
                        }
                }
            },
            "creationTime": "2023-07-25T12:23:38.673+00:00",
            "lastModifiedBy": None,
            "lastModifiedTime": "2023-07-25T12:23:38.673+00:00"
        }
    }

def get_automation_acc_results():
    return {
        "name": "testing352",
        "systemData": {
        "createdAt": "2023-07-25T12:05:22.16+00:00",
        "lastModifiedAt": "2023-07-25T12:05:22.16+00:00"
        },
        "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/testing352",
        "type": "Microsoft.Automation/AutomationAccounts",
        "location": "eastus",
        "identity": {
        "type": "SystemAssigned",
        "principalId": "ee616124-e026-4ca0-8c64-d34bae779faf",
        "tenantId": "50ad7d3e-b889-434d-802d-13b87c68047b"
        },
        "tags": {},
        "etag": None,
        "properties": {
        "publicNetworkAccess": True,
        "disableLocalAuth": False,
        "sku": {
            "name": "Basic",
            "family": None,
            "capacity": None
        },
        "state": "Ok",
        "RegistrationUrl": "https://99f846f3-c84d-4c96-af2b-cd0f7a5bd5d5.agentsvc.eus.azure-automation.net/accounts/99f846f3-c84d-4c96-af2b-cd0f7a5bd5d5",
        "encryption": {
            "keySource": "Microsoft.Automation",
            "identity": {
            "userAssignedIdentity": None
            }
        },
        "privateEndpointConnections": [],
        "automationHybridServiceUrl": "https://99f846f3-c84d-4c96-af2b-cd0f7a5bd5d5.jrds.eus.azure-automation.net/automationAccounts/99f846f3-c84d-4c96-af2b-cd0f7a5bd5d5",
        "RuntimeConfiguration": {
            "powershell": {
            "builtinModules": {
                "Az": "8.0.0"
            }
            },
            "powershell7": {
            "builtinModules": {
                "Az": "8.0.0"
            }
            }
        },
        "creationTime": "2023-07-25T12:05:22.16+00:00",
        "lastModifiedBy": None,
        "lastModifiedTime": "2023-07-25T12:05:22.16+00:00"
        }
    }

def get_automation_module_activity_results():
    return {
        "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Microsoft.PowerShell.Management/activities/Add-Computer",
        "name": "Add-Computer",
        "type": None,
        "properties": {
            "definition": "",
            "description": "\nAdd-Computer [-DomainName] <string> -Credential <pscredential> [-ComputerName <string[]>] [-LocalCredential <pscredential>] [-UnjoinDomainCredential <pscredential>] [-OUPath <string>] [-Server <string>] [-Unsecure] [-Options <JoinOptions>] [-Restart] [-PassThru] [-NewName <string>] [-Force] [-WhatIf] [-Confirm] [<CommonParameters>]\n\nAdd-Computer [-WorkgroupName] <string> [-ComputerName <string[]>] [-LocalCredential <pscredential>] [-Credential <pscredential>] [-Restart] [-PassThru] [-NewName <string>] [-Force] [-WhatIf] [-Confirm] [<CommonParameters>]\n ^https://go.microsoft.com/fwlink/?LinkID=135194^",
            "type": None,
            "parameterSets": [
                {
                    "name": "Domain",
                    "parameters": [
                        {
                            "name": "PassThru",
                            "type": "System.Management.Automation.SwitchParameter",
                            "isMandatory": False,
                            "isDynamic": False,
                            "position": -2147483648,
                            "valueFromPipeline": False,
                            "valueFromPipelineByPropertyName": False,
                            "valueFromRemainingArguments": False,
                            "description": None,
                            "validationSet": []
                        },
                        {
                            "name": "Restart",
                            "type": "System.Management.Automation.SwitchParameter",
                            "isMandatory": False,
                            "isDynamic": False,
                            "position": -2147483648,
                            "valueFromPipeline": False,
                            "valueFromPipelineByPropertyName": False,
                            "valueFromRemainingArguments": False,
                            "description": None,
                            "validationSet": []
                        },
                        {
                            "name": "UnjoinDomainCredential",
                            "type": "System.Management.Automation.PSCredential",
                            "isMandatory": False,
                            "isDynamic": False,
                            "position": -2147483648,
                            "valueFromPipeline": False,
                            "valueFromPipelineByPropertyName": False,
                            "valueFromRemainingArguments": False,
                            "description": None,
                            "validationSet": []
                        },
                        {
                            "name": "Confirm",
                            "type": "System.Management.Automation.SwitchParameter",
                            "isMandatory": False,
                            "isDynamic": False,
                            "position": -2147483648,
                            "valueFromPipeline": False,
                            "valueFromPipelineByPropertyName": False,
                            "valueFromRemainingArguments": False,
                            "description": None,
                            "validationSet": []
                        },
                        {
                            "name": "Force",
                            "type": "System.Management.Automation.SwitchParameter",
                            "isMandatory": False,
                            "isDynamic": False,
                            "position": -2147483648,
                            "valueFromPipeline": False,
                            "valueFromPipelineByPropertyName": False,
                            "valueFromRemainingArguments": False,
                            "description": None,
                            "validationSet": []
                        },
                        {
                            "name": "LocalCredential",
                            "type": "System.Management.Automation.PSCredential",
                            "isMandatory": False,
                            "isDynamic": False,
                            "position": -2147483648,
                            "valueFromPipeline": False,
                            "valueFromPipelineByPropertyName": False,
                            "valueFromRemainingArguments": False,
                            "description": None,
                            "validationSet": []
                        },
                        {
                            "name": "OUPath",
                            "type": "System.String",
                            "isMandatory": False,
                            "isDynamic": False,
                            "position": -2147483648,
                            "valueFromPipeline": False,
                            "valueFromPipelineByPropertyName": False,
                            "valueFromRemainingArguments": False,
                            "description": None,
                            "validationSet": []
                        },
                        {
                            "name": "Server",
                            "type": "System.String",
                            "isMandatory": False,
                            "isDynamic": False,
                            "position": -2147483648,
                            "valueFromPipeline": False,
                            "valueFromPipelineByPropertyName": False,
                            "valueFromRemainingArguments": False,
                            "description": None,
                            "validationSet": []
                        },
                        {
                            "name": "WhatIf",
                            "type": "System.Management.Automation.SwitchParameter",
                            "isMandatory": False,
                            "isDynamic": False,
                            "position": -2147483648,
                            "valueFromPipeline": False,
                            "valueFromPipelineByPropertyName": False,
                            "valueFromRemainingArguments": False,
                            "description": None,
                            "validationSet": []
                        },
                        {
                            "name": "Options",
                            "type": "Microsoft.PowerShell.Commands.JoinOptions",
                            "isMandatory": False,
                            "isDynamic": False,
                            "position": -2147483648,
                            "valueFromPipeline": False,
                            "valueFromPipelineByPropertyName": False,
                            "valueFromRemainingArguments": False,
                            "description": None,
                            "validationSet": []
                        },
                        {
                            "name": "ComputerName",
                            "type": "System.String[]",
                            "isMandatory": False,
                            "isDynamic": False,
                            "position": -2147483648,
                            "valueFromPipeline": True,
                            "valueFromPipelineByPropertyName": True,
                            "valueFromRemainingArguments": False,
                            "description": None,
                            "validationSet": []
                        },
                        {
                            "name": "Credential",
                            "type": "System.Management.Automation.PSCredential",
                            "isMandatory": True,
                            "isDynamic": False,
                            "position": -2147483648,
                            "valueFromPipeline": False,
                            "valueFromPipelineByPropertyName": False,
                            "valueFromRemainingArguments": False,
                            "description": None,
                            "validationSet": []
                        },
                        {
                            "name": "NewName",
                            "type": "System.String",
                            "isMandatory": False,
                            "isDynamic": False,
                            "position": -2147483648,
                            "valueFromPipeline": False,
                            "valueFromPipelineByPropertyName": True,
                            "valueFromRemainingArguments": False,
                            "description": None,
                            "validationSet": []
                        },
                        {
                            "name": "Unsecure",
                            "type": "System.Management.Automation.SwitchParameter",
                            "isMandatory": False,
                            "isDynamic": False,
                            "position": -2147483648,
                            "valueFromPipeline": False,
                            "valueFromPipelineByPropertyName": False,
                            "valueFromRemainingArguments": False,
                            "description": None,
                            "validationSet": []
                        },
                        {
                            "name": "DomainName",
                            "type": "System.String",
                            "isMandatory": True,
                            "isDynamic": False,
                            "position": 0,
                            "valueFromPipeline": False,
                            "valueFromPipelineByPropertyName": False,
                            "valueFromRemainingArguments": False,
                            "description": None,
                            "validationSet": []
                        }
                    ]
                },
                {
                    "name": "Workgroup",
                    "parameters": [
                        {
                            "name": "PassThru",
                            "type": "System.Management.Automation.SwitchParameter",
                            "isMandatory": False,
                            "isDynamic": False,
                            "position": -2147483648,
                            "valueFromPipeline": False,
                            "valueFromPipelineByPropertyName": False,
                            "valueFromRemainingArguments": False,
                            "description": None,
                            "validationSet": []
                        },
                        {
                            "name": "Force",
                            "type": "System.Management.Automation.SwitchParameter",
                            "isMandatory": False,
                            "isDynamic": False,
                            "position": -2147483648,
                            "valueFromPipeline": False,
                            "valueFromPipelineByPropertyName": False,
                            "valueFromRemainingArguments": False,
                            "description": None,
                            "validationSet": []
                        },
                        {
                            "name": "Confirm",
                            "type": "System.Management.Automation.SwitchParameter",
                            "isMandatory": False,
                            "isDynamic": False,
                            "position": -2147483648,
                            "valueFromPipeline": False,
                            "valueFromPipelineByPropertyName": False,
                            "valueFromRemainingArguments": False,
                            "description": None,
                            "validationSet": []
                        },
                        {
                            "name": "Credential",
                            "type": "System.Management.Automation.PSCredential",
                            "isMandatory": False,
                            "isDynamic": False,
                            "position": -2147483648,
                            "valueFromPipeline": False,
                            "valueFromPipelineByPropertyName": False,
                            "valueFromRemainingArguments": False,
                            "description": None,
                            "validationSet": []
                        },
                        {
                            "name": "LocalCredential",
                            "type": "System.Management.Automation.PSCredential",
                            "isMandatory": False,
                            "isDynamic": False,
                            "position": -2147483648,
                            "valueFromPipeline": False,
                            "valueFromPipelineByPropertyName": False,
                            "valueFromRemainingArguments": False,
                            "description": None,
                            "validationSet": []
                        },
                        {
                            "name": "WhatIf",
                            "type": "System.Management.Automation.SwitchParameter",
                            "isMandatory": False,
                            "isDynamic": False,
                            "position": -2147483648,
                            "valueFromPipeline": False,
                            "valueFromPipelineByPropertyName": False,
                            "valueFromRemainingArguments": False,
                            "description": None,
                            "validationSet": []
                        },
                        {
                            "name": "ComputerName",
                            "type": "System.String[]",
                            "isMandatory": False,
                            "isDynamic": False,
                            "position": -2147483648,
                            "valueFromPipeline": True,
                            "valueFromPipelineByPropertyName": True,
                            "valueFromRemainingArguments": False,
                            "description": None,
                            "validationSet": []
                        },
                        {
                            "name": "NewName",
                            "type": "System.String",
                            "isMandatory": False,
                            "isDynamic": False,
                            "position": -2147483648,
                            "valueFromPipeline": False,
                            "valueFromPipelineByPropertyName": True,
                            "valueFromRemainingArguments": False,
                            "description": None,
                            "validationSet": []
                        },
                        {
                            "name": "Restart",
                            "type": "System.Management.Automation.SwitchParameter",
                            "isMandatory": False,
                            "isDynamic": False,
                            "position": -2147483648,
                            "valueFromPipeline": False,
                            "valueFromPipelineByPropertyName": False,
                            "valueFromRemainingArguments": False,
                            "description": None,
                            "validationSet": []
                        },
                        {
                            "name": "WorkgroupName",
                            "type": "System.String",
                            "isMandatory": True,
                            "isDynamic": False,
                            "position": 0,
                            "valueFromPipeline": False,
                            "valueFromPipelineByPropertyName": False,
                            "valueFromRemainingArguments": False,
                            "description": None,
                            "validationSet": []
                        }
                    ]
                }
            ],
            "outputTypes": [
                {
                    "name": "Microsoft.PowerShell.Commands.ComputerChangeInfo",
                    "type": "Microsoft.PowerShell.Commands.ComputerChangeInfo"
                }
            ],
            "creationTime": "2023-07-27T08:32:28.12+00:00",
            "lastModifiedTime": "2023-07-27T08:32:28.12+00:00"
        }
    }

def list_automation_accounts_by_resource_group_result():
    return {
        "value": [
            {
                "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/automation1",
                "location": "eastus",
                "name": "automation1",
                "type": "Microsoft.Automation/AutomationAccounts",
                "tags": {
                    "client": "sentinel"
                },
                "properties": {
                    "creationTime": "2023-04-28T14:04:03.0766667+00:00",
                    "lastModifiedTime": "2023-07-21T14:25:01.7+00:00",
                    "state": "Ok",
                    "publicNetworkAccess": True,
                    "disableLocalAuth": False
                },
                "identity": {
                    "type": "SystemAssigned",
                    "principalId": "5c1a54ee-a043-4852-9b87-ed53005d9c62",
                    "tenantId": "50ad7d3e-b889-434d-802d-13b87c68047b"
                }
            },
            {
                "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/testing352",
                "location": "eastus",
                "name": "testing352",
                "type": "Microsoft.Automation/AutomationAccounts",
                "tags": {},
                "properties": {
                    "creationTime": "2023-07-25T12:05:22.16+00:00",
                    "lastModifiedTime": "2023-07-25T12:05:22.16+00:00",
                    "state": "Ok",
                    "publicNetworkAccess": True,
                    "disableLocalAuth": False
                },
                "identity": {
                    "type": "SystemAssigned",
                    "principalId": "ee616124-e026-4ca0-8c64-d34bae779faf",
                    "tenantId": "50ad7d3e-b889-434d-802d-13b87c68047b"
                }
            },
            {
                "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183",
                "location": "Canada Central",
                "name": "tester183",
                "type": "Microsoft.Automation/AutomationAccounts",
                "tags": {},
                "properties": {
                    "creationTime": "2023-07-25T12:12:11.663+00:00",
                    "lastModifiedTime": "2023-07-25T12:12:11.663+00:00",
                    "state": "Ok",
                    "publicNetworkAccess": True,
                    "disableLocalAuth": False
                }
            }
        ]
    }

def list_automation_accounts_result():
    return {
        "value": [
            {
                "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/automation1",
                "location": "eastus",
                "name": "automation1",
                "type": "Microsoft.Automation/AutomationAccounts",
                "tags": {
                    "client": "sentinel"
                },
                "properties": {
                    "creationTime": "2023-04-28T14:04:03.0766667+00:00",
                    "lastModifiedTime": "2023-07-21T14:25:01.7+00:00",
                    "publicNetworkAccess": True,
                    "disableLocalAuth": False
                },
                "identity": {
                    "type": "SystemAssigned",
                    "principalId": "5c1a54ee-a043-4852-9b87-ed53005d9c62",
                    "tenantId": "50ad7d3e-b889-434d-802d-13b87c68047b"
                }
            },
            {
                "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/testing352",
                "location": "eastus",
                "name": "testing352",
                "type": "Microsoft.Automation/AutomationAccounts",
                "tags": {},
                "properties": {
                    "creationTime": "2023-07-25T12:05:22.16+00:00",
                    "lastModifiedTime": "2023-07-25T12:05:22.16+00:00",
                    "publicNetworkAccess": True,
                    "disableLocalAuth": False
                },
                "identity": {
                    "type": "SystemAssigned",
                    "principalId": "ee616124-e026-4ca0-8c64-d34bae779faf",
                    "tenantId": "50ad7d3e-b889-434d-802d-13b87c68047b"
                }
            },
            {
                "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183",
                "location": "Canada Central",
                "name": "tester183",
                "type": "Microsoft.Automation/AutomationAccounts",
                "tags": {},
                "properties": {
                    "creationTime": "2023-07-25T12:12:11.663+00:00",
                    "lastModifiedTime": "2023-07-25T12:12:11.663+00:00",
                    "publicNetworkAccess": True,
                    "disableLocalAuth": False
                }
            }
        ]
    }

def list_automation_module_activities_results():
    return {
        "value": [
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/Add-AzApiManagementApiToGateway",
            "name": "Add-AzApiManagementApiToGateway",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Attaches an API to a gateway. ^https://docs.microsoft.com/powershell/module/az.apimanagement/add-azapimanagementapitogateway^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:17.043+00:00",
            "lastModifiedTime": "2022-07-06T05:49:17.043+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/Add-AzApiManagementApiToProduct",
            "name": "Add-AzApiManagementApiToProduct",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Adds an API to a product. ^https://docs.microsoft.com/powershell/module/az.apimanagement/add-azapimanagementapitoproduct^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:17.043+00:00",
            "lastModifiedTime": "2022-07-06T05:49:17.043+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/Add-AzApiManagementProductToGroup",
            "name": "Add-AzApiManagementProductToGroup",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Adds a product to a group. ^https://docs.microsoft.com/powershell/module/az.apimanagement/add-azapimanagementproducttogroup^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:17.043+00:00",
            "lastModifiedTime": "2022-07-06T05:49:17.043+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/Add-AzApiManagementRegion",
            "name": "Add-AzApiManagementRegion",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Adds new deployment regions to a PsApiManagement instance. ^https://docs.microsoft.com/powershell/module/az.apimanagement/add-azapimanagementregion^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:17.043+00:00",
            "lastModifiedTime": "2022-07-06T05:49:17.043+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/Add-AzApiManagementUserToGroup",
            "name": "Add-AzApiManagementUserToGroup",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Adds a user to a group. ^https://docs.microsoft.com/powershell/module/az.apimanagement/add-azapimanagementusertogroup^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:17.043+00:00",
            "lastModifiedTime": "2022-07-06T05:49:17.043+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/Backup-AzApiManagement",
            "name": "Backup-AzApiManagement",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Backs up an API Management service. ^https://docs.microsoft.com/powershell/module/az.apimanagement/backup-azapimanagement^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:17.043+00:00",
            "lastModifiedTime": "2022-07-06T05:49:17.043+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/Export-AzApiManagementApi",
            "name": "Export-AzApiManagementApi",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Exports an API to a file. ^https://docs.microsoft.com/powershell/module/az.apimanagement/export-azapimanagementapi^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:17.043+00:00",
            "lastModifiedTime": "2022-07-06T05:49:17.043+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/Get-AzApiManagement",
            "name": "Get-AzApiManagement",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Gets a list or a particular API Management Service description. ^https://docs.microsoft.com/powershell/module/az.apimanagement/get-azapimanagement^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:17.043+00:00",
            "lastModifiedTime": "2022-07-06T05:49:17.043+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/Get-AzApiManagementApi",
            "name": "Get-AzApiManagementApi",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Gets an API. ^https://docs.microsoft.com/powershell/module/az.apimanagement/get-azapimanagementapi^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:17.043+00:00",
            "lastModifiedTime": "2022-07-06T05:49:17.043+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/Get-AzApiManagementApiRelease",
            "name": "Get-AzApiManagementApiRelease",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Get the API Release. ^https://docs.microsoft.com/powershell/module/az.apimanagement/get-azapimanagementapirelease^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:17.043+00:00",
            "lastModifiedTime": "2022-07-06T05:49:17.043+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/Get-AzApiManagementApiRevision",
            "name": "Get-AzApiManagementApiRevision",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Gets details of all the API Revisions of an API ^https://docs.microsoft.com/powershell/module/az.apimanagement/get-azapimanagementapirevision^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:17.043+00:00",
            "lastModifiedTime": "2022-07-06T05:49:17.043+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/Get-AzApiManagementApiSchema",
            "name": "Get-AzApiManagementApiSchema",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Get the details of the API Schema ^https://docs.microsoft.com/powershell/module/az.apimanagement/get-azapimanagementapischema^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:17.043+00:00",
            "lastModifiedTime": "2022-07-06T05:49:17.043+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/Get-AzApiManagementApiVersionSet",
            "name": "Get-AzApiManagementApiVersionSet",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Get the details of the API Version Sets ^https://docs.microsoft.com/powershell/module/az.apimanagement/get-azapimanagementapiversionset^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:17.043+00:00",
            "lastModifiedTime": "2022-07-06T05:49:17.043+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/Get-AzApiManagementAuthorizationServer",
            "name": "Get-AzApiManagementAuthorizationServer",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Gets an API Management authorization server. ^https://docs.microsoft.com/powershell/module/az.apimanagement/get-azapimanagementauthorizationserver^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:17.043+00:00",
            "lastModifiedTime": "2022-07-06T05:49:17.043+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/Get-AzApiManagementAuthorizationServerClientSecret",
            "name": "Get-AzApiManagementAuthorizationServerClientSecret",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Gets an API Management authorization server client secret. ^https://docs.microsoft.com/powershell/module/az.apimanagement/get-azapimanagementauthorizationserverclientsecret^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:17.043+00:00",
            "lastModifiedTime": "2022-07-06T05:49:17.043+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/Get-AzApiManagementBackend",
            "name": "Get-AzApiManagementBackend",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Get the details of the Backend. ^https://docs.microsoft.com/powershell/module/az.apimanagement/get-azapimanagementbackend^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:17.043+00:00",
            "lastModifiedTime": "2022-07-06T05:49:17.043+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/Get-AzApiManagementCache",
            "name": "Get-AzApiManagementCache",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Get the details of the Cache. ^https://docs.microsoft.com/powershell/module/az.apimanagement/get-azapimanagementcache^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:17.043+00:00",
            "lastModifiedTime": "2022-07-06T05:49:17.043+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/Get-AzApiManagementCertificate",
            "name": "Get-AzApiManagementCertificate",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Gets API Management certificates configured for Mutual Authentication with Backend in the service. ^https://docs.microsoft.com/powershell/module/az.apimanagement/get-azapimanagementcertificate^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:17.043+00:00",
            "lastModifiedTime": "2022-07-06T05:49:17.043+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/Get-AzApiManagementDiagnostic",
            "name": "Get-AzApiManagementDiagnostic",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Get details of the Diagnostic configured at the service level or the Api Level. Diagnostics are used to log requests/responses from Api Management gateway. ^https://docs.microsoft.com/powershell/module/az.apimanagement/get-azapimanagementdiagnostic^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:17.043+00:00",
            "lastModifiedTime": "2022-07-06T05:49:17.043+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/Get-AzApiManagementGateway",
            "name": "Get-AzApiManagementGateway",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Gets all or specific API management Gateway. ^https://docs.microsoft.com/powershell/module/az.apimanagement/get-azapimanagementgateway^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:17.043+00:00",
            "lastModifiedTime": "2022-07-06T05:49:17.043+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/Get-AzApiManagementGatewayHostnameConfiguration",
            "name": "Get-AzApiManagementGatewayHostnameConfiguration",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Gets all or specific hostname configuration for the existing Gateway. ^https://docs.microsoft.com/powershell/module/az.apimanagement/get-azapimanagementgatewayhostnameconfiguration^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:17.043+00:00",
            "lastModifiedTime": "2022-07-06T05:49:17.043+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/Get-AzApiManagementGatewayKey",
            "name": "Get-AzApiManagementGatewayKey",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Gets keys of the existing Gateway ^https://docs.microsoft.com/powershell/module/az.apimanagement/get-azapimanagementgatewaykey^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:17.043+00:00",
            "lastModifiedTime": "2022-07-06T05:49:17.043+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/Get-AzApiManagementGroup",
            "name": "Get-AzApiManagementGroup",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Gets all or specific API management groups. ^https://docs.microsoft.com/powershell/module/az.apimanagement/get-azapimanagementgroup^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:17.043+00:00",
            "lastModifiedTime": "2022-07-06T05:49:17.043+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/Get-AzApiManagementIdentityProvider",
            "name": "Get-AzApiManagementIdentityProvider",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Get the identity provider configuration details. ^https://docs.microsoft.com/powershell/module/az.apimanagement/get-azapimanagementidentityprovider^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:17.043+00:00",
            "lastModifiedTime": "2022-07-06T05:49:17.043+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/Get-AzApiManagementIdentityProviderClientSecret",
            "name": "Get-AzApiManagementIdentityProviderClientSecret",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Get the identity provider client secret. ^https://docs.microsoft.com/powershell/module/az.apimanagement/get-azapimanagementidentityproviderclientsecret^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:17.043+00:00",
            "lastModifiedTime": "2022-07-06T05:49:17.043+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/Get-AzApiManagementLogger",
            "name": "Get-AzApiManagementLogger",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Gets API Management Logger objects. ^https://docs.microsoft.com/powershell/module/az.apimanagement/get-azapimanagementlogger^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:17.043+00:00",
            "lastModifiedTime": "2022-07-06T05:49:17.043+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/Get-AzApiManagementNamedValue",
            "name": "Get-AzApiManagementNamedValue",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Gets a list or a particular Named Value. ^https://docs.microsoft.com/powershell/module/az.apimanagement/get-azapimanagementnamedvalue^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:17.043+00:00",
            "lastModifiedTime": "2022-07-06T05:49:17.043+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/Get-AzApiManagementNamedValueSecretValue",
            "name": "Get-AzApiManagementNamedValueSecretValue",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Gets a secret value of the particular Named Value. ^https://docs.microsoft.com/powershell/module/az.apimanagement/get-azapimanagementnamedvaluesecretvalue^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:17.043+00:00",
            "lastModifiedTime": "2022-07-06T05:49:17.043+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/Get-AzApiManagementNetworkStatus",
            "name": "Get-AzApiManagementNetworkStatus",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Gets the Connectivity Status to the external resources on which the Api Management service depends from inside the Cloud Service. This also returns the DNS Servers as visible to the CloudService. ^https://docs.microsoft.com/powershell/module/az.apimanagement/get-azapimanagementnetworkstatus^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:17.043+00:00",
            "lastModifiedTime": "2022-07-06T05:49:17.043+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/Get-AzApiManagementOpenIdConnectProvider",
            "name": "Get-AzApiManagementOpenIdConnectProvider",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Gets OpenID Connect providers. ^https://docs.microsoft.com/powershell/module/az.apimanagement/get-azapimanagementopenidconnectprovider^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:17.043+00:00",
            "lastModifiedTime": "2022-07-06T05:49:17.043+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/Get-AzApiManagementOpenIdConnectProviderClientSecret",
            "name": "Get-AzApiManagementOpenIdConnectProviderClientSecret",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Gets OpenID Connect provider client secret. ^https://docs.microsoft.com/powershell/module/az.apimanagement/get-azapimanagementopenidconnectproviderclientsecret^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:17.043+00:00",
            "lastModifiedTime": "2022-07-06T05:49:17.043+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/Get-AzApiManagementOperation",
            "name": "Get-AzApiManagementOperation",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Gets a list or a specified API Operation. ^https://docs.microsoft.com/powershell/module/az.apimanagement/get-azapimanagementoperation^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:17.043+00:00",
            "lastModifiedTime": "2022-07-06T05:49:17.043+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/Get-AzApiManagementPolicy",
            "name": "Get-AzApiManagementPolicy",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Gets the specified scope policy. ^https://docs.microsoft.com/powershell/module/az.apimanagement/get-azapimanagementpolicy^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:17.043+00:00",
            "lastModifiedTime": "2022-07-06T05:49:17.043+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/Get-AzApiManagementProduct",
            "name": "Get-AzApiManagementProduct",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Gets a list or a particular product. ^https://docs.microsoft.com/powershell/module/az.apimanagement/get-azapimanagementproduct^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:17.043+00:00",
            "lastModifiedTime": "2022-07-06T05:49:17.043+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/Get-AzApiManagementSsoToken",
            "name": "Get-AzApiManagementSsoToken",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Gets a link with an SSO token to a deployed management portal of an API Management service. ^https://docs.microsoft.com/powershell/module/az.apimanagement/get-azapimanagementssotoken^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:17.043+00:00",
            "lastModifiedTime": "2022-07-06T05:49:17.043+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/Get-AzApiManagementSubscription",
            "name": "Get-AzApiManagementSubscription",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Gets subscriptions. ^https://docs.microsoft.com/powershell/module/az.apimanagement/get-azapimanagementsubscription^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:17.043+00:00",
            "lastModifiedTime": "2022-07-06T05:49:17.043+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/Get-AzApiManagementSubscriptionKey",
            "name": "Get-AzApiManagementSubscriptionKey",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Gets subscription keys. ^https://docs.microsoft.com/powershell/module/az.apimanagement/get-azapimanagementsubscriptionkey^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:17.043+00:00",
            "lastModifiedTime": "2022-07-06T05:49:17.043+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/Get-AzApiManagementTenantAccess",
            "name": "Get-AzApiManagementTenantAccess",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Gets the access configuration for a tenant. ^https://docs.microsoft.com/powershell/module/az.apimanagement/get-azapimanagementtenantaccess^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:17.043+00:00",
            "lastModifiedTime": "2022-07-06T05:49:17.043+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/Get-AzApiManagementTenantAccessSecret",
            "name": "Get-AzApiManagementTenantAccessSecret",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Gets the access configuration keys for a tenant. ^https://docs.microsoft.com/powershell/module/az.apimanagement/get-azapimanagementtenantaccesssecret^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:17.043+00:00",
            "lastModifiedTime": "2022-07-06T05:49:17.043+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/Get-AzApiManagementTenantGitAccess",
            "name": "Get-AzApiManagementTenantGitAccess",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Gets the Git access configuration for a tenant. ^https://docs.microsoft.com/powershell/module/az.apimanagement/get-azapimanagementtenantgitaccess^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:17.043+00:00",
            "lastModifiedTime": "2022-07-06T05:49:17.043+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/Get-AzApiManagementTenantGitAccessSecret",
            "name": "Get-AzApiManagementTenantGitAccessSecret",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Gets the Git access configuration keys for a tenant. ^https://docs.microsoft.com/powershell/module/az.apimanagement/get-azapimanagementtenantgitaccesssecret^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:17.043+00:00",
            "lastModifiedTime": "2022-07-06T05:49:17.043+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/Get-AzApiManagementTenantSyncState",
            "name": "Get-AzApiManagementTenantSyncState",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Gets the status of the most recent synchronization between the configuration database and the Git repository. ^https://docs.microsoft.com/powershell/module/az.apimanagement/get-azapimanagementtenantsyncstate^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:17.043+00:00",
            "lastModifiedTime": "2022-07-06T05:49:17.043+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/Get-AzApiManagementUser",
            "name": "Get-AzApiManagementUser",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Gets a user or users. ^https://docs.microsoft.com/powershell/module/az.apimanagement/get-azapimanagementuser^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:17.043+00:00",
            "lastModifiedTime": "2022-07-06T05:49:17.043+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/Get-AzApiManagementUserSsoUrl",
            "name": "Get-AzApiManagementUserSsoUrl",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Generates an SSO URL for a user. ^https://docs.microsoft.com/powershell/module/az.apimanagement/get-azapimanagementuserssourl^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:17.043+00:00",
            "lastModifiedTime": "2022-07-06T05:49:17.043+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/Import-AzApiManagementApi",
            "name": "Import-AzApiManagementApi",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Imports an API from a file or a URL. ^https://docs.microsoft.com/powershell/module/az.apimanagement/import-azapimanagementapi^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:17.043+00:00",
            "lastModifiedTime": "2022-07-06T05:49:17.043+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/New-AzApiManagement",
            "name": "New-AzApiManagement",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Creates an API Management deployment. ^https://docs.microsoft.com/powershell/module/az.apimanagement/new-azapimanagement^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:17.043+00:00",
            "lastModifiedTime": "2022-07-06T05:49:17.043+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/New-AzApiManagementApi",
            "name": "New-AzApiManagementApi",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Creates an API. ^https://docs.microsoft.com/powershell/module/az.apimanagement/new-azapimanagementapi^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:17.043+00:00",
            "lastModifiedTime": "2022-07-06T05:49:17.043+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/New-AzApiManagementApiRelease",
            "name": "New-AzApiManagementApiRelease",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Creates an API Release of an API Revision ^https://docs.microsoft.com/powershell/module/az.apimanagement/new-azapimanagementapirelease^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:17.043+00:00",
            "lastModifiedTime": "2022-07-06T05:49:17.043+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/New-AzApiManagementApiRevision",
            "name": "New-AzApiManagementApiRevision",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Creates a new Revision of an Existing API. ^https://docs.microsoft.com/powershell/module/az.apimanagement/new-azapimanagementapirevision^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:17.043+00:00",
            "lastModifiedTime": "2022-07-06T05:49:17.043+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/New-AzApiManagementApiSchema",
            "name": "New-AzApiManagementApiSchema",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Creates the new API Schema in the ApiManagement service ^https://docs.microsoft.com/powershell/module/az.apimanagement/new-azapimanagementapischema^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:17.043+00:00",
            "lastModifiedTime": "2022-07-06T05:49:17.043+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/New-AzApiManagementApiVersionSet",
            "name": "New-AzApiManagementApiVersionSet",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Creates an API Version Set. ^https://docs.microsoft.com/powershell/module/az.apimanagement/new-azapimanagementapiversionset^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:37.19+00:00",
            "lastModifiedTime": "2022-07-06T05:49:37.19+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/New-AzApiManagementAuthorizationServer",
            "name": "New-AzApiManagementAuthorizationServer",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Creates an authorization server. ^https://docs.microsoft.com/powershell/module/az.apimanagement/new-azapimanagementauthorizationserver^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:37.19+00:00",
            "lastModifiedTime": "2022-07-06T05:49:37.19+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/New-AzApiManagementBackend",
            "name": "New-AzApiManagementBackend",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Creates a new backend entity. ^https://docs.microsoft.com/powershell/module/az.apimanagement/new-azapimanagementbackend^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:37.19+00:00",
            "lastModifiedTime": "2022-07-06T05:49:37.19+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/New-AzApiManagementBackendCredential",
            "name": "New-AzApiManagementBackendCredential",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Creates a new Backend Credential contract. ^https://docs.microsoft.com/powershell/module/az.apimanagement/new-azapimanagementbackendcredential^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:37.19+00:00",
            "lastModifiedTime": "2022-07-06T05:49:37.19+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/New-AzApiManagementBackendProxy",
            "name": "New-AzApiManagementBackendProxy",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Creates a new Backend Proxy Object. ^https://docs.microsoft.com/powershell/module/az.apimanagement/new-azapimanagementbackendproxy^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:37.19+00:00",
            "lastModifiedTime": "2022-07-06T05:49:37.19+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/New-AzApiManagementBackendServiceFabric",
            "name": "New-AzApiManagementBackendServiceFabric",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Creates an object of `PsApiManagementServiceFabric` ^https://docs.microsoft.com/powershell/module/az.apimanagement/new-azapimanagementbackendservicefabric^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:37.19+00:00",
            "lastModifiedTime": "2022-07-06T05:49:37.19+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/New-AzApiManagementCache",
            "name": "New-AzApiManagementCache",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Creates a new Cache entity ^https://docs.microsoft.com/powershell/module/az.apimanagement/new-azapimanagementcache^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:37.19+00:00",
            "lastModifiedTime": "2022-07-06T05:49:37.19+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/New-AzApiManagementCertificate",
            "name": "New-AzApiManagementCertificate",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Creates an API Management certificate to be used during Authentication with Backend. ^https://docs.microsoft.com/powershell/module/az.apimanagement/new-azapimanagementcertificate^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:37.19+00:00",
            "lastModifiedTime": "2022-07-06T05:49:37.19+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/New-AzApiManagementContext",
            "name": "New-AzApiManagementContext",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Creates an instance of PsAzureApiManagementContext. ^https://docs.microsoft.com/powershell/module/az.apimanagement/new-azapimanagementcontext^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:37.19+00:00",
            "lastModifiedTime": "2022-07-06T05:49:37.19+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/New-AzApiManagementCustomHostnameConfiguration",
            "name": "New-AzApiManagementCustomHostnameConfiguration",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Creates an instance of `PsApiManagementCustomHostNameConfiguration`. ^https://docs.microsoft.com/powershell/module/az.apimanagement/new-azapimanagementcustomhostnameconfiguration^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:37.19+00:00",
            "lastModifiedTime": "2022-07-06T05:49:37.19+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/New-AzApiManagementDiagnostic",
            "name": "New-AzApiManagementDiagnostic",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Creates a new diagnostics at the Global scope or Api Scope. ^https://docs.microsoft.com/powershell/module/az.apimanagement/new-azapimanagementdiagnostic^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:37.19+00:00",
            "lastModifiedTime": "2022-07-06T05:49:37.19+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/New-AzApiManagementGateway",
            "name": "New-AzApiManagementGateway",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Creates new Gateway entity. ^https://docs.microsoft.com/powershell/module/az.apimanagement/new-azapimanagementgateway^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:37.19+00:00",
            "lastModifiedTime": "2022-07-06T05:49:37.19+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/New-AzApiManagementGatewayHostnameConfiguration",
            "name": "New-AzApiManagementGatewayHostnameConfiguration",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Creates a hostname configuratin for the existing Gateway. ^https://docs.microsoft.com/powershell/module/az.apimanagement/new-azapimanagementgatewayhostnameconfiguration^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:37.19+00:00",
            "lastModifiedTime": "2022-07-06T05:49:37.19+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/New-AzApiManagementGroup",
            "name": "New-AzApiManagementGroup",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Creates an API management group. ^https://docs.microsoft.com/powershell/module/az.apimanagement/new-azapimanagementgroup^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:37.19+00:00",
            "lastModifiedTime": "2022-07-06T05:49:37.19+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/New-AzApiManagementHttpMessageDiagnostic",
            "name": "New-AzApiManagementHttpMessageDiagnostic",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Creates an instance of PsApiManagementHttpMessageDiagnostic which is an Http Message diagnostic setting of the Diagnostic ^https://docs.microsoft.com/powershell/module/az.apimanagement/new-azapimanagementhttpmessagediagnostic^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:37.19+00:00",
            "lastModifiedTime": "2022-07-06T05:49:37.19+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/New-AzApiManagementIdentityProvider",
            "name": "New-AzApiManagementIdentityProvider",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Creates a new Identity Provider configuration. ^https://docs.microsoft.com/powershell/module/az.apimanagement/new-azapimanagementidentityprovider^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:37.19+00:00",
            "lastModifiedTime": "2022-07-06T05:49:37.19+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/New-AzApiManagementKeyVaultObject",
            "name": "New-AzApiManagementKeyVaultObject",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Creates an instance of PsApiManagementKeyVaultObject. ^https://docs.microsoft.com/powershell/module/az.apimanagement/new-azapimanagementkeyvaultobject^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:37.19+00:00",
            "lastModifiedTime": "2022-07-06T05:49:37.19+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/New-AzApiManagementLogger",
            "name": "New-AzApiManagementLogger",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Creates an API Management Logger. ^https://docs.microsoft.com/powershell/module/az.apimanagement/new-azapimanagementlogger^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:37.19+00:00",
            "lastModifiedTime": "2022-07-06T05:49:37.19+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/New-AzApiManagementNamedValue",
            "name": "New-AzApiManagementNamedValue",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Creates new Named Value. ^https://docs.microsoft.com/powershell/module/az.apimanagement/new-azapimanagementnamedvalue^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:37.19+00:00",
            "lastModifiedTime": "2022-07-06T05:49:37.19+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/New-AzApiManagementOpenIdConnectProvider",
            "name": "New-AzApiManagementOpenIdConnectProvider",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Creates an OpenID Connect provider. ^https://docs.microsoft.com/powershell/module/az.apimanagement/new-azapimanagementopenidconnectprovider^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:37.19+00:00",
            "lastModifiedTime": "2022-07-06T05:49:37.19+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/New-AzApiManagementOperation",
            "name": "New-AzApiManagementOperation",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Creates an API management operation. ^https://docs.microsoft.com/powershell/module/az.apimanagement/new-azapimanagementoperation^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:37.19+00:00",
            "lastModifiedTime": "2022-07-06T05:49:37.19+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/New-AzApiManagementPipelineDiagnosticSetting",
            "name": "New-AzApiManagementPipelineDiagnosticSetting",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Create Diagnostic settings for incoming/outgoing HTTP messages to the Gateway. ^https://docs.microsoft.com/powershell/module/az.apimanagement/new-azapimanagementpipelinediagnosticsetting^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:37.19+00:00",
            "lastModifiedTime": "2022-07-06T05:49:37.19+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/New-AzApiManagementProduct",
            "name": "New-AzApiManagementProduct",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Creates an API Management product. ^https://docs.microsoft.com/powershell/module/az.apimanagement/new-azapimanagementproduct^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:37.19+00:00",
            "lastModifiedTime": "2022-07-06T05:49:37.19+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/New-AzApiManagementRegion",
            "name": "New-AzApiManagementRegion",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Creates an instance of PsApiManagementRegion. ^https://docs.microsoft.com/powershell/module/az.apimanagement/new-azapimanagementregion^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:37.19+00:00",
            "lastModifiedTime": "2022-07-06T05:49:37.19+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/New-AzApiManagementResourceLocationObject",
            "name": "New-AzApiManagementResourceLocationObject",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Create a new resource location contract (used in Gateways). ^https://docs.microsoft.com/powershell/module/az.apimanagement/new-azapimanagementresourcelocationobject^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:37.19+00:00",
            "lastModifiedTime": "2022-07-06T05:49:37.19+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/New-AzApiManagementSamplingSetting",
            "name": "New-AzApiManagementSamplingSetting",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Create a new sampling setting for the Diagnostic ^https://docs.microsoft.com/powershell/module/az.apimanagement/new-azapimanagementsamplingsetting^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:37.19+00:00",
            "lastModifiedTime": "2022-07-06T05:49:37.19+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/New-AzApiManagementSslSetting",
            "name": "New-AzApiManagementSslSetting",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Creates an instance of PsApiManagementSslSetting ^https://docs.microsoft.com/powershell/module/az.apimanagement/new-azapimanagementsslsetting^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:37.19+00:00",
            "lastModifiedTime": "2022-07-06T05:49:37.19+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/New-AzApiManagementSubscription",
            "name": "New-AzApiManagementSubscription",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Creates a subscription. ^https://docs.microsoft.com/powershell/module/az.apimanagement/new-azapimanagementsubscription^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:37.19+00:00",
            "lastModifiedTime": "2022-07-06T05:49:37.19+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/New-AzApiManagementSystemCertificate",
            "name": "New-AzApiManagementSystemCertificate",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Creates an instance of `PsApiManagementSystemCertificate`. The certificate can be issued by private CA's and will be installed on the API Management service into `CertificateAuthority` or `Root` store. ^https://docs.microsoft.com/powershell/module/az.apimanagement/new-azapimanagementsystemcertificate^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:37.19+00:00",
            "lastModifiedTime": "2022-07-06T05:49:37.19+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/New-AzApiManagementUser",
            "name": "New-AzApiManagementUser",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Registers a new user. ^https://docs.microsoft.com/powershell/module/az.apimanagement/new-azapimanagementuser^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:37.19+00:00",
            "lastModifiedTime": "2022-07-06T05:49:37.19+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/New-AzApiManagementUserToken",
            "name": "New-AzApiManagementUserToken",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Generates a Shared Access Token for the User. ^https://docs.microsoft.com/powershell/module/az.apimanagement/new-azapimanagementusertoken^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:37.19+00:00",
            "lastModifiedTime": "2022-07-06T05:49:37.19+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/New-AzApiManagementVirtualNetwork",
            "name": "New-AzApiManagementVirtualNetwork",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Creates an instance of PsApiManagementVirtualNetwork. ^https://docs.microsoft.com/powershell/module/az.apimanagement/new-azapimanagementvirtualnetwork^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:37.19+00:00",
            "lastModifiedTime": "2022-07-06T05:49:37.19+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/Publish-AzApiManagementTenantGitConfiguration",
            "name": "Publish-AzApiManagementTenantGitConfiguration",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Publishes changes from a Git branch to the configuration database. ^https://docs.microsoft.com/powershell/module/az.apimanagement/publish-azapimanagementtenantgitconfiguration^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:37.19+00:00",
            "lastModifiedTime": "2022-07-06T05:49:37.19+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/Remove-AzApiManagement",
            "name": "Remove-AzApiManagement",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Removes an API Management service. ^https://docs.microsoft.com/powershell/module/az.apimanagement/remove-azapimanagement^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:37.19+00:00",
            "lastModifiedTime": "2022-07-06T05:49:37.19+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/Remove-AzApiManagementApi",
            "name": "Remove-AzApiManagementApi",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Removes an API. ^https://docs.microsoft.com/powershell/module/az.apimanagement/remove-azapimanagementapi^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:37.19+00:00",
            "lastModifiedTime": "2022-07-06T05:49:37.19+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/Remove-AzApiManagementApiFromGateway",
            "name": "Remove-AzApiManagementApiFromGateway",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Attaches an API to a gateway. ^https://docs.microsoft.com/powershell/module/az.apimanagement/remove-azapimanagementapifromgateway^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:37.19+00:00",
            "lastModifiedTime": "2022-07-06T05:49:37.19+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/Remove-AzApiManagementApiFromProduct",
            "name": "Remove-AzApiManagementApiFromProduct",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Removes an API from a product. ^https://docs.microsoft.com/powershell/module/az.apimanagement/remove-azapimanagementapifromproduct^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:37.19+00:00",
            "lastModifiedTime": "2022-07-06T05:49:37.19+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/Remove-AzApiManagementApiRelease",
            "name": "Remove-AzApiManagementApiRelease",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Removes a particular API Release ^https://docs.microsoft.com/powershell/module/az.apimanagement/remove-azapimanagementapirelease^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:37.19+00:00",
            "lastModifiedTime": "2022-07-06T05:49:37.19+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/Remove-AzApiManagementApiRevision",
            "name": "Remove-AzApiManagementApiRevision",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Removed a particular API Revision ^https://docs.microsoft.com/powershell/module/az.apimanagement/remove-azapimanagementapirevision^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:37.19+00:00",
            "lastModifiedTime": "2022-07-06T05:49:37.19+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/Remove-AzApiManagementApiSchema",
            "name": "Remove-AzApiManagementApiSchema",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Removes the API Schema from the API. ^https://docs.microsoft.com/powershell/module/az.apimanagement/remove-azapimanagementapischema^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:37.19+00:00",
            "lastModifiedTime": "2022-07-06T05:49:37.19+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/Remove-AzApiManagementApiVersionSet",
            "name": "Remove-AzApiManagementApiVersionSet",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Removes a particular Api Version Set ^https://docs.microsoft.com/powershell/module/az.apimanagement/remove-azapimanagementapiversionset^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:37.19+00:00",
            "lastModifiedTime": "2022-07-06T05:49:37.19+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/Remove-AzApiManagementAuthorizationServer",
            "name": "Remove-AzApiManagementAuthorizationServer",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Removes an authorization server. ^https://docs.microsoft.com/powershell/module/az.apimanagement/remove-azapimanagementauthorizationserver^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:37.19+00:00",
            "lastModifiedTime": "2022-07-06T05:49:37.19+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/Remove-AzApiManagementBackend",
            "name": "Remove-AzApiManagementBackend",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Removes a Backend. ^https://docs.microsoft.com/powershell/module/az.apimanagement/remove-azapimanagementbackend^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:37.19+00:00",
            "lastModifiedTime": "2022-07-06T05:49:37.19+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/Remove-AzApiManagementCache",
            "name": "Remove-AzApiManagementCache",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Removes the cache entity. ^https://docs.microsoft.com/powershell/module/az.apimanagement/remove-azapimanagementcache^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:37.19+00:00",
            "lastModifiedTime": "2022-07-06T05:49:37.19+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/Remove-AzApiManagementCertificate",
            "name": "Remove-AzApiManagementCertificate",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Removes an API Management certificate. ^https://docs.microsoft.com/powershell/module/az.apimanagement/remove-azapimanagementcertificate^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:37.19+00:00",
            "lastModifiedTime": "2022-07-06T05:49:37.19+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/Remove-AzApiManagementDiagnostic",
            "name": "Remove-AzApiManagementDiagnostic",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Remove the Diagnostic entity from Global or API level scope. ^https://docs.microsoft.com/powershell/module/az.apimanagement/remove-azapimanagementdiagnostic^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:37.19+00:00",
            "lastModifiedTime": "2022-07-06T05:49:37.19+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/Remove-AzApiManagementGateway",
            "name": "Remove-AzApiManagementGateway",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Detaches an API from a Gateway. ^https://docs.microsoft.com/powershell/module/az.apimanagement/remove-azapimanagementgateway^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:37.19+00:00",
            "lastModifiedTime": "2022-07-06T05:49:37.19+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/Remove-AzApiManagementGatewayHostnameConfiguration",
            "name": "Remove-AzApiManagementGatewayHostnameConfiguration",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Removes a hostname configuration from the existing Gateway. ^https://docs.microsoft.com/powershell/module/az.apimanagement/remove-azapimanagementgatewayhostnameconfiguration^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:37.19+00:00",
            "lastModifiedTime": "2022-07-06T05:49:37.19+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/Remove-AzApiManagementGroup",
            "name": "Remove-AzApiManagementGroup",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Removes an existing API management group. ^https://docs.microsoft.com/powershell/module/az.apimanagement/remove-azapimanagementgroup^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:37.19+00:00",
            "lastModifiedTime": "2022-07-06T05:49:37.19+00:00"
            }
        },
        {
            "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities/Remove-AzApiManagementIdentityProvider",
            "name": "Remove-AzApiManagementIdentityProvider",
            "type": None,
            "properties": {
            "definition": "",
            "description": "Removes an existing Identity Provider Configuration. ^https://docs.microsoft.com/powershell/module/az.apimanagement/remove-azapimanagementidentityprovider^",
            "type": None,
            "parameterSets": None,
            "outputTypes": None,
            "creationTime": "2022-07-06T05:49:37.19+00:00",
            "lastModifiedTime": "2022-07-06T05:49:37.19+00:00"
            }
        }
        ],
        "nextLink": "https://management.azure.com:443/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183/modules/Az.ApiManagement/activities?api-version=2019-06-01&$skip=100"
    }

def execute_runbook_results():
    return "\r\nLocation              : eastus\r\nTags                  : {}\r\nJobCount              : 0\r\nRunbookType           : PowerShell\r\nParameters            : {}\r\nLogVerbose            : False\r\nLogProgress           : False\r\nLastModifiedBy        : \r\nState                 : Published\r\nResourceGroupName     : DemoAssets\r\nAutomationAccountName : automation1\r\nName                  : get_all_runbooks\r\nCreationTime          : 7/19/2023 3:39:27 PM +00:00\r\nLastModifiedTime      : 7/19/2023 4:03:24 PM +00:00\r\nDescription           : Return all runbooks\r\n\r\n\r\nEnvironments                                                                                                            \r\n------------                                                                                                            \r\n{[AzureChinaCloud, AzureChinaCloud], [AzureCloud, AzureCloud], [AzureGermanCloud, AzureGermanCloud], [AzureUSGovernme...\r\n\r\n"

def mock_init():
    class MockClient(object):
        """ Add Mock connection data """

        def __init__(self):
            """ Mock """
            pass

        def create_update_automation_account(self, payload):
            """ Mock create/update automation account return """
            return create_update_results()

        def delete_automation_acount(self):
            """ Mock delete automation account return """
            class MockDeleteAccount(object):
                status_code = 200
                text = ""
                def __init__(self):
                    """ Mock """
                    pass

            return MockDeleteAccount()

        def get_automation_account(self):
            """ Mock get automation account return """
            return get_automation_acc_results()

        def get_automation_module_activity(self, moduleName, activityName):
            """ Mock get automation module activity return """
            return get_automation_module_activity_results()

        def list_automation_accounts_by_resource_group(self):
            """ Mock list automation accounts by resource group return """
            return list_automation_accounts_by_resource_group_result()

        def list_automation_accounts(self):
            """ Mock list automation accounts return """
            return list_automation_accounts_result()

        def list_automation_module_activities(self, moduleName):
            """ Mock list automation module activities return """
            return list_automation_module_activities_results()

        def run_runbook(self, runbook_name, job_name = 0, runbook_parameters = {}):
            """ Mock run runbook return """
            return {"name": job_name}

        def get_job_final_status(self, job_name, time_to_wait):
            """ Mock get job final status return """
            return "Completed"

        def get_runbook_results(self, job_name):
            """ Mock get runbook results return """
            return execute_runbook_results()

    return MockClient()


