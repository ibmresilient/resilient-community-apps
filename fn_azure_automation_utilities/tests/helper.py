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

def create_account_results():
    return {
        "name": "test-account",
        "systemData": {
            "createdAt": "2023-07-25T12:23:38.673+00:00",
            "lastModifiedAt": "2023-07-25T12:23:38.673+00:00"
        },
        "id": "/subscriptions/abcdefgh-1234-abcd-1234-a1b2c3d4e5f6/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/test-account",
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

def update_account_results():
    return {
        "name": "autotester24",
        "systemData": {
        "createdAt": "2023-08-22T12:44:27.9+00:00",
        "lastModifiedAt": "2023-08-22T13:16:59.3333333+00:00"
        },
        "id": "/subscriptions/abcdefgh-1234-abcd-1234-a1b2c3d4e5f6/resourceGroups/demoassets/providers/Microsoft.Automation/automationAccounts/autotester24",
        "type": "Microsoft.Automation/AutomationAccounts",
        "location": "Canada East",
        "tags": {},
        "etag": None,
        "properties": {
        "publicNetworkAccess": False,
        "disableLocalAuth": False,
        "sku": {
            "name": "Basic",
            "family": None,
            "capacity": None
        },
        "state": "Ok",
        "RegistrationUrl": "https://55555555-3333-4444-bb0f-030397ea7fc1.agentsvc.yq.azure-automation.net/accounts/55555555-3333-4444-bb0f-030397ea7fc1",
        "encryption": {
            "keySource": "Microsoft.Automation",
            "identity": {
            "userAssignedIdentity": None
            }
        },
        "automationHybridServiceUrl": "https://55555555-3333-4444-bb0f-030397ea7fc1.jrds.yq.azure-automation.net/automationAccounts/55555555-3333-4444-bb0f-030397ea7fc1",
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
        "creationTime": "2023-08-22T12:44:27.9+00:00",
        "lastModifiedBy": None,
        "lastModifiedTime": "2023-08-22T13:16:59.3333333+00:00"
        }
    }

def get_acc_results():
    return {
        "name": "testing352",
        "systemData": {
        "createdAt": "2023-07-25T12:05:22.16+00:00",
        "lastModifiedAt": "2023-07-25T12:05:22.16+00:00"
        },
        "id": "/subscriptions/abcdefgh-1234-abcd-1234-a1b2c3d4e5f6/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/testing352",
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

def get_module_activity_results():
    return {
        "id": "/subscriptions/abcdefgh-1234-abcd-1234-a1b2c3d4e5f6/resourceGroups/demoassets/providers/Microsoft.Automation/automationAccounts/automation1/modules/Az.Advisor/activities/Set-AzAdvisorConfiguration",
        "name": "Set-AzAdvisorConfiguration",
        "type": None,
        "properties": {
            "definition": "",
            "description": "Updates or creates the Azure Advisor Configuration. ^https://docs.microsoft.com/powershell/module/az.advisor/set-azadvisorConfiguration^",
            "type": None,
            "parameterSets": [
                {
                    "name": "InputObjectLowCpuExcludeParameterSet",
                    "parameters": [
                        {
                            "name": "DefaultProfile",
                            "type": "Microsoft.Azure.Commands.Common.Authentication.Abstractions.Core.IAzureContextContainer",
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
                            "name": "Exclude",
                            "type": "System.Management.Automation.SwitchParameter",
                            "isMandatory": False,
                            "isDynamic": False,
                            "position": 2,
                            "valueFromPipeline": False,
                            "valueFromPipelineByPropertyName": False,
                            "valueFromRemainingArguments": False,
                            "description": None,
                            "validationSet": []
                        },
                        {
                            "name": "LowCpuThreshold",
                            "type": "System.Int32",
                            "isMandatory": True,
                            "isDynamic": False,
                            "position": 0,
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
                            "name": "InputObject",
                            "type": "Microsoft.Azure.Commands.Advisor.Cmdlets.Models.PsAzureAdvisorConfigurationData",
                            "isMandatory": False,
                            "isDynamic": False,
                            "position": 1,
                            "valueFromPipeline": True,
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
                        }
                    ]
                },
                {
                    "name": "InputObjectRgExcludeParameterSet",
                    "parameters": [
                        {
                            "name": "InputObject",
                            "type": "Microsoft.Azure.Commands.Advisor.Cmdlets.Models.PsAzureAdvisorConfigurationData",
                            "isMandatory": False,
                            "isDynamic": False,
                            "position": 1,
                            "valueFromPipeline": True,
                            "valueFromPipelineByPropertyName": False,
                            "valueFromRemainingArguments": False,
                            "description": None,
                            "validationSet": []
                        },
                        {
                            "name": "Exclude",
                            "type": "System.Management.Automation.SwitchParameter",
                            "isMandatory": False,
                            "isDynamic": False,
                            "position": 2,
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
                            "name": "ResourceGroupName",
                            "type": "System.String",
                            "isMandatory": False,
                            "isDynamic": False,
                            "position": 0,
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
                            "name": "DefaultProfile",
                            "type": "Microsoft.Azure.Commands.Common.Authentication.Abstractions.Core.IAzureContextContainer",
                            "isMandatory": False,
                            "isDynamic": False,
                            "position": -2147483648,
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
                    "name": "Microsoft.Azure.Commands.Advisor.Cmdlets.Models.PsAzureAdvisorConfigurationData",
                    "type": "Microsoft.Azure.Commands.Advisor.Cmdlets.Models.PsAzureAdvisorConfigurationData"
                }
            ],
            "creationTime": "2022-07-06T10:01:53.9133333+00:00",
            "lastModifiedTime": "2022-07-06T10:01:53.9133333+00:00"
        }
    }

def list_accounts_by_resource_group_results():
    return {
        "value": [
            {
                "id": "/subscriptions/abcdefgh-1234-abcd-1234-a1b2c3d4e5f6/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/automation1",
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
                "id": "/subscriptions/abcdefgh-1234-abcd-1234-a1b2c3d4e5f6/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/testing352",
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
                "id": "/subscriptions/abcdefgh-1234-abcd-1234-a1b2c3d4e5f6/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183",
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

def list_accounts_results():
    return {
        "value": [
            {
                "id": "/subscriptions/abcdefgh-1234-abcd-1234-a1b2c3d4e5f6/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/automation1",
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
                "id": "/subscriptions/abcdefgh-1234-abcd-1234-a1b2c3d4e5f6/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/testing352",
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
                "id": "/subscriptions/abcdefgh-1234-abcd-1234-a1b2c3d4e5f6/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/tester183",
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

def list_module_activities_results():
    return {
        "value": [
            {
                "id": "/subscriptions/abcdefgh-1234-abcd-1234-a1b2c3d4e5f6/resourceGroups/demoassets/providers/Microsoft.Automation/automationAccounts/automation1/modules/Az.Advisor/activities/Disable-AzAdvisorRecommendation",
                "name": "Disable-AzAdvisorRecommendation",
                "type": None,
                "properties": {
                    "definition": "",
                    "description": "Disable an Azure Advisor recommendation. ^https://docs.microsoft.com/powershell/module/az.advisor/disable-azadvisorrecommendation^",
                    "type": None,
                    "parameterSets": None,
                    "outputTypes": None,
                    "creationTime": "2022-07-06T10:01:53.9133333+00:00",
                    "lastModifiedTime": "2022-07-06T10:01:53.9133333+00:00"
                }
            },
            {
                "id": "/subscriptions/abcdefgh-1234-abcd-1234-a1b2c3d4e5f6/resourceGroups/demoassets/providers/Microsoft.Automation/automationAccounts/automation1/modules/Az.Advisor/activities/Enable-AzAdvisorRecommendation",
                "name": "Enable-AzAdvisorRecommendation",
                "type": None,
                "properties": {
                    "definition": "",
                    "description": "Enables Azure Advisor recommendation(s). ^https://docs.microsoft.com/powershell/module/az.advisor/enable-azadvisorrecommendation^",
                    "type": None,
                    "parameterSets": None,
                    "outputTypes": None,
                    "creationTime": "2022-07-06T10:01:53.9133333+00:00",
                    "lastModifiedTime": "2022-07-06T10:01:53.9133333+00:00"
                }
            },
            {
                "id": "/subscriptions/abcdefgh-1234-abcd-1234-a1b2c3d4e5f6/resourceGroups/demoassets/providers/Microsoft.Automation/automationAccounts/automation1/modules/Az.Advisor/activities/Get-AzAdvisorConfiguration",
                "name": "Get-AzAdvisorConfiguration",
                "type": None,
                "properties": {
                    "definition": "",
                    "description": "Get the Azure Advisor configurations for the given subscription or resource group. ^https://docs.microsoft.com/powershell/module/az.advisor/get-azadvisorconfiguration^",
                    "type": None,
                    "parameterSets": None,
                    "outputTypes": None,
                    "creationTime": "2022-07-06T10:01:53.9133333+00:00",
                    "lastModifiedTime": "2022-07-06T10:01:53.9133333+00:00"
                }
            },
            {
                "id": "/subscriptions/abcdefgh-1234-abcd-1234-a1b2c3d4e5f6/resourceGroups/demoassets/providers/Microsoft.Automation/automationAccounts/automation1/modules/Az.Advisor/activities/Get-AzAdvisorRecommendation",
                "name": "Get-AzAdvisorRecommendation",
                "type": None,
                "properties": {
                    "definition": "",
                    "description": "Gets a list of Azure Advisor recommendations. ^https://docs.microsoft.com/powershell/module/az.advisor/get-azadvisorrecommendation^",
                    "type": None,
                    "parameterSets": None,
                    "outputTypes": None,
                    "creationTime": "2022-07-06T10:01:53.9133333+00:00",
                    "lastModifiedTime": "2022-07-06T10:01:53.9133333+00:00"
                }
            },
            {
                "id": "/subscriptions/abcdefgh-1234-abcd-1234-a1b2c3d4e5f6/resourceGroups/demoassets/providers/Microsoft.Automation/automationAccounts/automation1/modules/Az.Advisor/activities/Set-AzAdvisorConfiguration",
                "name": "Set-AzAdvisorConfiguration",
                "type": None,
                "properties": {
                    "definition": "",
                    "description": "Updates or creates the Azure Advisor Configuration. ^https://docs.microsoft.com/powershell/module/az.advisor/set-azadvisorConfiguration^",
                    "type": None,
                    "parameterSets": None,
                    "outputTypes": None,
                    "creationTime": "2022-07-06T10:01:53.9133333+00:00",
                    "lastModifiedTime": "2022-07-06T10:01:53.9133333+00:00"
                }
            }
        ]
    }

def get_job_output_results():
    return "\r\nLocation              : eastus\r\nTags                  : {}\r\nJobCount              : 0\r\nRunbookType           : PowerShell\r\nParameters            : {}\r\nLogVerbose            : False\r\nLogProgress           : False\r\nLastModifiedBy        : \r\nState                 : Published\r\nResourceGroupName     : DemoAssets\r\nAutomationAccountName : automation1\r\nName                  : get_all_runbooks\r\nCreationTime          : 7/19/2023 3:39:27 PM +00:00\r\nLastModifiedTime      : 7/19/2023 4:03:24 PM +00:00\r\nDescription           : Return all runbooks\r\n\r\n\r\nEnvironments                                                                                                            \r\n------------                                                                                                            \r\n{[AzureChinaCloud, AzureChinaCloud], [AzureCloud, AzureCloud], [AzureGermanCloud, AzureGermanCloud], [AzureUSGovernme...\r\n\r\n"

def list_runbooks_by_automation_account_results():
    return {
        "value": [
            {
                "id": "/subscriptions/abcdefgh-1234-abcd-1234-a1b2c3d4e5f6/resourceGroups/demoassets/providers/Microsoft.Automation/automationAccounts/automation1/runbooks/AzureAutomationTutorialWithIdentity",
                "location": "eastus",
                "name": "AzureAutomationTutorialWithIdentity",
                "type": "Microsoft.Automation/AutomationAccounts/Runbooks",
                "tags": {},
                "properties": {
                "runbookType": "PowerShell",
                "state": "Published",
                "logVerbose": False,
                "logProgress": False,
                "logActivityTrace": 0,
                "creationTime": "2023-04-28T14:04:05.0066667+00:00",
                "lastModifiedTime": "2023-07-19T15:43:27.3633333+00:00"
                }
            },
            {
                "id": "/subscriptions/abcdefgh-1234-abcd-1234-a1b2c3d4e5f6/resourceGroups/demoassets/providers/Microsoft.Automation/automationAccounts/automation1/runbooks/AzureAutomationTutorialWithIdentityGraphical",
                "location": "eastus",
                "name": "AzureAutomationTutorialWithIdentityGraphical",
                "type": "Microsoft.Automation/AutomationAccounts/Runbooks",
                "tags": {},
                "properties": {
                "runbookType": "GraphPowerShell",
                "state": "Published",
                "logVerbose": False,
                "logProgress": False,
                "logActivityTrace": 0,
                "creationTime": "2023-04-28T14:04:05.1166667+00:00",
                "lastModifiedTime": "2023-07-19T15:43:36.2466667+00:00"
                }
            }
        ]
    }

def get_runbook_results():
    return {
        "id": "/subscriptions/abcdefgh-1234-abcd-1234-a1b2c3d4e5f6/resourceGroups/demoassets/providers/Microsoft.Automation/automationAccounts/automation1/runbooks/Hello_world",
        "name": "Hello_world",
        "type": "Microsoft.Automation/AutomationAccounts/Runbooks",
        "location": "eastus",
        "tags": {},
        "etag": "\"638246066435733333\"",
        "properties": {
            "description": "My first python 3 runbook",
            "logVerbose": False,
            "logProgress": False,
            "logActivityTrace": 0,
            "runbookType": "Python3",
            "parameters": {},
            "state": "Published",
            "jobCount": 0,
            "draft": None,
            "provisioningState": "Succeeded",
            "serviceManagementTags": None,
            "outputTypes": [],
            "creationTime": "2023-07-10T17:22:53.7066667+00:00",
            "lastModifiedBy": None,
            "lastModifiedTime": "2023-07-10T17:24:03.5733333+00:00"
        }
    }

def get_job_results():
    return {
        "id": "/subscriptions/abcdefgh-1234-abcd-1234-a1b2c3d4e5f6/resourceGroups/demoassets/providers/Microsoft.Automation/automationAccounts/automation1/jobs/1692024049238",
        "name": "1692024049238",
        "type": "Microsoft.Automation/AutomationAccounts/Jobs",
        "properties": {
            "jobId": "efe4db52-a124-4bea-9582-7b0c7f7133e4",
            "creationTime": "2023-08-14T14:42:29.5306946+00:00",
            "provisioningState": "Succeeded",
            "status": "Completed",
            "statusDetails": "None",
            "startedBy": "{scrubbed}",
            "startTime": "2023-08-14T14:42:41.9604553+00:00",
            "endTime": "2023-08-14T14:42:55.9297673+00:00",
            "lastModifiedTime": "2023-08-14T14:42:55.9297673+00:00",
            "lastStatusModifiedTime": "2023-08-14T14:42:55.9297673+00:00",
            "exception": None,
            "parameters": {
                "runbook_name": "get_all_runbooks"
            },
            "runOn": "",
            "runbook": {
                "name": "Get_given_runbook"
            }
        }
    }

def list_jobs_by_automation_account_results():
    return {
        "value": [
            {
                "id": "/subscriptions/abcdefgh-1234-abcd-1234-a1b2c3d4e5f6/resourceGroups/demoassets/providers/Microsoft.Automation/automationAccounts/automation1/jobs/1692024049238",
                "name": "1692024049238",
                "type": "Microsoft.Automation/AutomationAccounts/Jobs",
                "properties": {
                    "jobId": "efe4db52-a124-4bea-9582-7b0c7f7133e4",
                    "runbook": {"name": "Get_given_runbook"},
                    "provisioningState": "Succeeded",
                    "status": "Completed",
                    "creationTime": "2023-08-14T14:42:29.5306946+00:00",
                    "startTime": "2023-08-14T14:42:41.9604553+00:00",
                    "lastModifiedTime": "2023-08-14T14:42:55.9297673+00:00",
                    "endTime": "2023-08-14T14:42:55.9297673+00:00",
                    "runOn": ""
                }
            },
            {
                "id": "/subscriptions/abcdefgh-1234-abcd-1234-a1b2c3d4e5f6/resourceGroups/demoassets/providers/Microsoft.Automation/automationAccounts/automation1/jobs/1691761457680",
                "name": "1691761457680",
                "type": "Microsoft.Automation/AutomationAccounts/Jobs",
                "properties": {
                    "jobId": "ee72f62a-e732-41ea-a55a-1ae0e9a6d5e5",
                    "runbook": {"name": "Get_given_runbook"},
                    "provisioningState": "Succeeded",
                    "status": "Completed",
                    "creationTime": "2023-08-11T14:02:36.9532796+00:00",
                    "startTime": "2023-08-11T14:03:03.5818149+00:00",
                    "lastModifiedTime": "2023-08-11T14:03:16.661328+00:00",
                    "endTime": "2023-08-11T14:03:16.661328+00:00",
                    "runOn": ""
                }
            }
        ]
    }

def get_agent_registration_information_results():
    return {
        "id": "/subscriptions/abcdefgh-1234-abcd-1234-a1b2c3d4e5f6/resourceGroups/demoassets/providers/Microsoft.Automation/automationAccounts/automation1/agentRegistrationInformation/https://abcdefgh-1234-abcd-1234-a1b2c3d4e5f6.agentsvc.eus.azure-automation.net/accounts/abcdefgh-1234-abcd-1234-a1b2c3d4e5f6",
        "keys": {
            "primary": "1234RYKSRuyfmINzCvic0Oz7DpGskIbty5W12345QbKWlsYT0BGp6qzfwz12345678vuh28cqRMoxDD39Iut7w==",
            "secondary": "bC6hr123456789qPD2eeowEt9rDRqfJMnJmUOhP123450/x53Vezc3rqDhherrLzb123456MWhub+86IKwxssg=="
        },
        "endpoint": "https://abcdefgh-1234-abcd-1234-a1b2c3d4e5f6.agentsvc.eus.azure-automation.net/accounts/abcdefgh-1234-abcd-1234-a1b2c3d4e5f6",
        "dscMetaConfiguration": "\r\n\tinstance of MSFT_WebDownloadManager as $MSFT_WebDownloadManager1ref\r\n\t{\r\n\tResourceID = \"[ConfigurationRepositoryWeb]AzureAutomationDSC\";\r\n\t SourceInfo = \"C:\\\\OaaS-RegistrationMetaConfig2.ps1::20::9::ConfigurationRepositoryWeb\";\r\n\t RegistrationKey = \"1234RYKSRuyfmINzCvic0Oz7DpGskIbty5W12345QbKWlsYT0BGp6qzfwz12345678vuh28cqRMoxDD39Iut7w==\"; \r\n\t ServerURL = \"https://abcdefgh-1234-abcd-1234-a1b2c3d4e5f6.agentsvc.eus.azure-automation.net/accounts/abcdefgh-1234-abcd-1234-a1b2c3d4e5f6\";\r\n\t};\r\n\r\n\tinstance of MSFT_WebResourceManager as $MSFT_WebResourceManager1ref\r\n\t{\r\n\t SourceInfo = \"C:\\\\OaaS-RegistrationMetaConfig2.ps1::27::9::ResourceRepositoryWeb\";\r\n\t ServerURL = \"https://abcdefgh-1234-abcd-1234-a1b2c3d4e5f6.agentsvc.eus.azure-automation.net/accounts/abcdefgh-1234-abcd-1234-a1b2c3d4e5f6\";\r\n\t ResourceID = \"[ResourceRepositoryWeb]AzureAutomationDSC\";\r\n\t RegistrationKey = \"1234RYKSRuyfmINzCvic0Oz7DpGskIbty5W12345QbKWlsYT0BGp6qzfwz12345678vuh28cqRMoxDD39Iut7w==\"; \r\n\t};\r\n\r\n\tinstance of MSFT_WebReportManager as $MSFT_WebReportManager1ref\r\n\t{\r\n\t SourceInfo = \"C:\\\\OaaS-RegistrationMetaConfig2.ps1::34::9::ReportServerWeb\";\r\n\t ServerURL = \"https://abcdefgh-1234-abcd-1234-a1b2c3d4e5f6.agentsvc.eus.azure-automation.net/accounts/abcdefgh-1234-abcd-1234-a1b2c3d4e5f6\";\r\n\t ResourceID = \"[ReportServerWeb]AzureAutomationDSC\";\r\n\t RegistrationKey = \"1234RYKSRuyfmINzCvic0Oz7DpGskIbty5W12345QbKWlsYT0BGp6qzfwz12345678vuh28cqRMoxDD39Iut7w==\"; \r\n\t};\r\n\r\n\tinstance of MSFT_DSCMetaConfiguration as $MSFT_DSCMetaConfiguration1ref\r\n\t{\r\n\t RefreshMode = \"Pull\";\r\n\t AllowModuleOverwrite = False;\r\n\t ActionAfterReboot = \"ContinueConfiguration\";\r\n\t RefreshFrequencyMins = 30;\r\n\t RebootNodeIfNeeded = False;\r\n\t ConfigurationModeFrequencyMins = 15;\r\n\t ConfigurationMode = \"ApplyAndMonitor\";\r\n\r\n\t  ResourceModuleManagers = {\r\n\t  $MSFT_WebResourceManager1ref  \r\n\t};\r\n\t  ReportManagers = {\r\n\t  $MSFT_WebReportManager1ref  \r\n\t };\r\n\t  ConfigurationDownloadManagers = {\r\n\t  $MSFT_WebDownloadManager1ref  \r\n\t };\r\n\t};\r\n\r\n\tinstance of OMI_ConfigurationDocument\r\n\t{\r\n\t Version=\"2.0.0\";\r\n\t MinimumCompatibleVersion = \"2.0.0\";\r\n\t CompatibleVersionAdditionalProperties= { \"MSFT_DSCMetaConfiguration:StatusRetentionTimeInDays\" };\r\n\t Author=\"azureautomation\";\r\n\t GenerationDate=\"04/17/2015 11:41:09\";\r\n\t GenerationHost=\"azureautomation-01\";\r\n\t Name=\"RegistrationMetaConfig\";\r\n\t};\r\n\t"
    }

def regenerate_account_registration_key_results():
    return {
        "id": None,
        "keys": {
            "primary": "g+Z4E/12345678c/YbuFnwTe4yI12EYPRTdmFHVj+SI12345b0R8ghU8YNWe7BM3hjYDCzkqWhZGd0r5V4YHag==",
            "secondary": "bC6hr123456789qPD2eeowEt9rDRqfJMnJmUOhP123450/x53Vezc3rqDhherrLzb123456MWhub+86IKwxssg=="
        },
        "endpoint": "https://abcdefgh-1234-abcd-1234-a1b2c3d4e5f6.agentsvc.eus.azure-automation.net/accounts/abcdefgh-1234-abcd-1234-a1b2c3d4e5f6",
        "dscMetaConfiguration": None
    }

def create_credential_results():
    return {
        "id": "/subscriptions/abcdefgh-1234-abcd-1234-a1b2c3d4e5f6/resourceGroups/demoassets/providers/Microsoft.Automation/automationAccounts/automation1/credentials/tes43",
        "name": "tes43",
        "type": "Microsoft.Automation/AutomationAccounts/Credentials",
        "properties": {
            "userName": "tes43",
            "description": None,
            "creationTime": "2023-08-21T18:14:38.87+00:00",
            "lastModifiedTime": "2023-08-21T18:14:38.87+00:00"
        }
    }

def get_credential_results():
    return {
        "id": "/subscriptions/abcdefgh-1234-abcd-1234-a1b2c3d4e5f6/resourceGroups/demoassets/providers/Microsoft.Automation/automationAccounts/automation1/credentials/tes43",
        "name": "tes43",
        "type": "Microsoft.Automation/AutomationAccounts/Credentials",
        "properties": {
            "userName": "tes43",
            "description": None,
            "creationTime": "2023-08-21T18:14:38.87+00:00",
            "lastModifiedTime": "2023-08-21T18:14:38.87+00:00"
        }
    }

def list_credentials_by_automation_account_results():
    return {
        "value": [
            {
                "id": "/subscriptions/abcdefgh-1234-abcd-1234-a1b2c3d4e5f6/resourceGroups/demoassets/providers/Microsoft.Automation/automationAccounts/automation1/credentials/tes43",
                "name": "tes43",
                "type": "Microsoft.Automation/AutomationAccounts/Credentials",
                "properties": {
                "userName": "tes43",
                "description": None,
                "creationTime": "2023-08-21T18:14:38.87+00:00",
                "lastModifiedTime": "2023-08-21T18:14:38.87+00:00"
                }
            },
            {
                "id": "/subscriptions/abcdefgh-1234-abcd-1234-a1b2c3d4e5f6/resourceGroups/demoassets/providers/Microsoft.Automation/automationAccounts/automation1/credentials/test",
                "name": "test",
                "type": "Microsoft.Automation/AutomationAccounts/Credentials",
                "properties": {
                "userName": "tester",
                "description": None,
                "creationTime": "2023-07-19T15:33:17.5333333+00:00",
                "lastModifiedTime": "2023-07-19T15:33:17.5333333+00:00"
                }
            },
            {
                "id": "/subscriptions/abcdefgh-1234-abcd-1234-a1b2c3d4e5f6/resourceGroups/demoassets/providers/Microsoft.Automation/automationAccounts/automation1/credentials/test12",
                "name": "test12",
                "type": "Microsoft.Automation/AutomationAccounts/Credentials",
                "properties": {
                "userName": "test12",
                "description": None,
                "creationTime": "2023-08-21T18:12:39.2033333+00:00",
                "lastModifiedTime": "2023-08-21T18:12:39.2033333+00:00"
                }
            },
            {
                "id": "/subscriptions/abcdefgh-1234-abcd-1234-a1b2c3d4e5f6/resourceGroups/demoassets/providers/Microsoft.Automation/automationAccounts/automation1/credentials/test22",
                "name": "test22",
                "type": "Microsoft.Automation/AutomationAccounts/Credentials",
                "properties": {
                "userName": "test22",
                "description": None,
                "creationTime": "2023-08-21T18:10:15.51+00:00",
                "lastModifiedTime": "2023-08-21T18:10:15.51+00:00"
                }
            },
            {
                "id": "/subscriptions/abcdefgh-1234-abcd-1234-a1b2c3d4e5f6/resourceGroups/demoassets/providers/Microsoft.Automation/automationAccounts/automation1/credentials/test32",
                "name": "test32",
                "type": "Microsoft.Automation/AutomationAccounts/Credentials",
                "properties": {
                "userName": "test32",
                "description": None,
                "creationTime": "2023-08-21T17:59:44.38+00:00",
                "lastModifiedTime": "2023-08-21T17:59:44.38+00:00"
                }
            }
        ]
    }

def update_credential_results():
    return {
        "id": "/subscriptions/abcdefgh-1234-abcd-1234-a1b2c3d4e5f6/resourceGroups/demoassets/providers/Microsoft.Automation/automationAccounts/automation1/credentials/test32",
        "name": "test32",
        "type": "Microsoft.Automation/AutomationAccounts/Credentials",
        "properties": {
            "userName": "tester",
            "description": "something",
            "creationTime": "2023-08-21T17:59:44.38+00:00",
            "lastModifiedTime": "2023-08-21T17:59:44.38+00:00"
        }
    }

def create_schedule_results():
    return {
        "id": "/subscriptions/abcdefgh-1234-abcd-1234-a1b2c3d4e5f6/resourceGroups/demoassets/providers/Microsoft.Automation/automationAccounts/automation1/schedules/tester1324",
        "name": "tester1324",
        "type": "Microsoft.Automation/AutomationAccounts/Schedules",
        "properties": {
            "description": "something",
            "startTime": "2023-08-25T08:40:00+00:00",
            "startTimeOffsetMinutes": 0.0,
            "expiryTime": "2023-08-25T08:40:00+00:00",
            "expiryTimeOffsetMinutes": 0.0,
            "isEnabled": True,
            "nextRun": "2023-08-25T08:40:00+00:00",
            "nextRunOffsetMinutes": 0.0,
            "interval": None,
            "frequency": "OneTime",
            "creationTime": "2023-08-24T15:31:44.2666667+00:00",
            "lastModifiedTime": "2023-08-24T15:31:44.2666667+00:00",
            "timeZone": "Etc/UTC",
            "advancedSchedule": None
        }
    }

def get_schedule_results():
    return {
        "id": "/subscriptions/abcdefgh-1234-abcd-1234-a1b2c3d4e5f6/resourceGroups/demoassets/providers/Microsoft.Automation/automationAccounts/automation1/schedules/tester1324",
        "name": "tester1324",
        "type": "Microsoft.Automation/AutomationAccounts/Schedules",
        "properties": {
        "description": "something",
        "startTime": "2023-08-25T08:40:00+00:00",
        "startTimeOffsetMinutes": 0.0,
        "expiryTime": "2023-08-25T08:40:00+00:00",
        "expiryTimeOffsetMinutes": 0.0,
        "isEnabled": True,
        "nextRun": "2023-08-25T08:40:00+00:00",
        "nextRunOffsetMinutes": 0.0,
        "interval": None,
        "frequency": "OneTime",
        "creationTime": "2023-08-24T15:31:44.2666667+00:00",
        "lastModifiedTime": "2023-08-24T15:31:44.2666667+00:00",
        "timeZone": "Etc/UTC",
        "advancedSchedule": None
        }
    }

def list_schedule_by_automation_account_results():
    return {
        "value": [
        {
            "id": "/subscriptions/abcdefgh-1234-abcd-1234-a1b2c3d4e5f6/resourceGroups/demoassets/providers/Microsoft.Automation/automationAccounts/automation1/schedules/s",
            "name": "s",
            "type": "Microsoft.Automation/AutomationAccounts/Schedules",
            "properties": {
            "description": "",
            "startTime": "2023-08-29T12:05:00-04:00",
            "startTimeOffsetMinutes": -240.0,
            "expiryTime": "2023-08-29T12:05:00-04:00",
            "expiryTimeOffsetMinutes": -240.0,
            "isEnabled": True,
            "nextRun": "2023-08-29T12:05:00-04:00",
            "nextRunOffsetMinutes": -240.0,
            "interval": None,
            "frequency": "OneTime",
            "creationTime": "2023-08-23T16:05:14.3633333+00:00",
            "lastModifiedTime": "2023-08-23T17:09:35.4666667+00:00",
            "timeZone": "America/New_York",
            "advancedSchedule": None
            }
        },
        {
            "id": "/subscriptions/abcdefgh-1234-abcd-1234-a1b2c3d4e5f6/resourceGroups/demoassets/providers/Microsoft.Automation/automationAccounts/automation1/schedules/tester",
            "name": "tester",
            "type": "Microsoft.Automation/AutomationAccounts/Schedules",
            "properties": {
            "description": "",
            "startTime": "2023-08-08T14:35:00-04:00",
            "startTimeOffsetMinutes": -240.0,
            "expiryTime": "2023-08-08T14:35:00-04:00",
            "expiryTimeOffsetMinutes": -240.0,
            "isEnabled": True,
            "nextRun": None,
            "nextRunOffsetMinutes": 0.0,
            "interval": None,
            "frequency": "OneTime",
            "creationTime": "2023-08-08T18:05:08.1333333+00:00",
            "lastModifiedTime": "2023-08-08T18:05:08.1333333+00:00",
            "timeZone": "America/New_York",
            "advancedSchedule": None
            }
        },
        {
            "id": "/subscriptions/abcdefgh-1234-abcd-1234-a1b2c3d4e5f6/resourceGroups/demoassets/providers/Microsoft.Automation/automationAccounts/automation1/schedules/tester1324",
            "name": "tester1324",
            "type": "Microsoft.Automation/AutomationAccounts/Schedules",
            "properties": {
            "description": "something",
            "startTime": "2023-08-25T08:40:00+00:00",
            "startTimeOffsetMinutes": 0.0,
            "expiryTime": "2023-08-25T08:40:00+00:00",
            "expiryTimeOffsetMinutes": 0.0,
            "isEnabled": True,
            "nextRun": "2023-08-25T08:40:00+00:00",
            "nextRunOffsetMinutes": 0.0,
            "interval": None,
            "frequency": "OneTime",
            "creationTime": "2023-08-24T15:31:44.2666667+00:00",
            "lastModifiedTime": "2023-08-24T15:31:44.2666667+00:00",
            "timeZone": "Etc/UTC",
            "advancedSchedule": None
            }
        }
        ]
    }

def update_schedule_results():
    return {
        "id": "/subscriptions/abcdefgh-1234-abcd-1234-a1b2c3d4e5f6/resourceGroups/demoassets/providers/Microsoft.Automation/automationAccounts/automation1/schedules/s",
        "name": "s",
        "type": "Microsoft.Automation/AutomationAccounts/Schedules",
        "properties": {
            "description": "",
            "startTime": "2023-08-29T12:05:00-04:00",
            "startTimeOffsetMinutes": -240.0,
            "expiryTime": "2023-08-29T12:05:00-04:00",
            "expiryTimeOffsetMinutes": -240.0,
            "isEnabled": False,
            "nextRun": "2023-08-29T12:05:00-04:00",
            "nextRunOffsetMinutes": -240.0,
            "interval": None,
            "frequency": "OneTime",
            "creationTime": "2023-08-23T16:05:14.3633333+00:00",
            "lastModifiedTime": "2023-08-23T17:09:35.4666667+00:00",
            "timeZone": "America/New_York",
            "advancedSchedule": None
        }
    }

def get_node_report_results():
    return {
        "id": "/subscriptions/abcdefgh-1234-abcd-1234-a1b2c3d4e5f6/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/automation1/nodes/24939717-e819-4059-aa08-82862c65f3c8/reports/3c47f0b6-aeb7-429a-a656-70f2a19ab22a",
        "reportId": "3c47f0b6-aeb7-429a-a656-70f2a19ab22a",
        "type": "Consistency",
        "startTime": "2023-09-06T13:30:01.9451859+00:00",
        "endTime": "2023-09-06T13:30:02.1606975+00:00",
        "lastModifiedTime": "2023-09-06T13:30:02.2533333+00:00",
        "status": "Compliant",
        "refreshMode": None,
        "rebootRequested": None,
        "reportFormatVersion": "2.0",
        "configurationVersion": "2.0.0",
        "errors": [],
        "resources": [],
        "metaConfiguration": None,
        "hostName": None,
        "iPV4Addresses": [],
        "iPV6Addresses": [],
        "numberOfResources": 0,
        "rawErrors": None
    }

def list_node_report_by_node_results():
    return {
        "value": [
            {
                "id": "/subscriptions/abcdefgh-1234-abcd-1234-a1b2c3d4e5f6/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/automation1/nodes/24939717-e819-4059-aa08-82862c65f3c8/reports/3c47f0b6-aeb7-429a-a656-70f2a19ab22a",
                "reportId": "3c47f0b6-aeb7-429a-a656-70f2a19ab22a",
                "type": "Consistency",
                "startTime": "2023-09-06T13:30:01.9451859+00:00",
                "endTime": "2023-09-06T13:30:02.1606975+00:00",
                "lastModifiedTime": "2023-09-06T13:30:02.2533333+00:00",
                "status": "Compliant",
                "configurationVersion": "2.0.0",
                "rebootRequested": None,
                "refreshMode": None,
                "reportFormatVersion": "2.0"
            },
            {
                "id": "/subscriptions/abcdefgh-1234-abcd-1234-a1b2c3d4e5f6/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/automation1/nodes/24939717-e819-4059-aa08-82862c65f3c8/reports/73335fdb-bf2b-4e91-9409-0766b7533424",
                "reportId": "73335fdb-bf2b-4e91-9409-0766b7533424",
                "type": "Consistency",
                "startTime": "2023-09-06T13:00:01.3984203+00:00",
                "endTime": "2023-09-06T13:00:01.591596+00:00",
                "lastModifiedTime": "2023-09-06T13:00:01.7+00:00",
                "status": "Compliant",
                "configurationVersion": "2.0.0",
                "rebootRequested": None,
                "refreshMode": None,
                "reportFormatVersion": "2.0"
            },
            {
                "id": "/subscriptions/abcdefgh-1234-abcd-1234-a1b2c3d4e5f6/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/automation1/nodes/24939717-e819-4059-aa08-82862c65f3c8/reports/c9152779-51af-4cc6-8d3e-d09089280beb",
                "reportId": "c9152779-51af-4cc6-8d3e-d09089280beb",
                "type": "Consistency",
                "startTime": "2023-09-06T12:30:01.4923996+00:00",
                "endTime": "2023-09-06T12:30:02.066503+00:00",
                "lastModifiedTime": "2023-09-06T12:30:02.17+00:00",
                "status": "Compliant",
                "configurationVersion": "2.0.0",
                "rebootRequested": None,
                "refreshMode": None,
                "reportFormatVersion": "2.0"
            }
        ]
    }

def list_statistics_by_automation_account_results():
    return {
        "value": [
            {
                "id": "/subscriptions/abcdefgh-1234-abcd-1234-a1b2c3d4e5f6/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/automation1/statistics/New",
                "counterProperty": "New",
                "counterValue": 0,
                "startTime": "2023-08-30T13:58:01.5985342+00:00",
                "endTime": "2023-09-06T13:58:01.5985342+00:00"
            },
            {
                "id": "/subscriptions/abcdefgh-1234-abcd-1234-a1b2c3d4e5f6/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/automation1/statistics/Activating",
                "counterProperty": "Activating",
                "counterValue": 0,
                "startTime": "2023-08-30T13:58:01.5985342+00:00",
                "endTime": "2023-09-06T13:58:01.5985342+00:00"
            },
            {
                "id": "/subscriptions/abcdefgh-1234-abcd-1234-a1b2c3d4e5f6/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/automation1/statistics/Running",
                "counterProperty": "Running",
                "counterValue": 0,
                "startTime": "2023-08-30T13:58:01.5985342+00:00",
                "endTime": "2023-09-06T13:58:01.5985342+00:00"
            },
            {
                "id": "/subscriptions/abcdefgh-1234-abcd-1234-a1b2c3d4e5f6/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/automation1/statistics/Completed",
                "counterProperty": "Completed",
                "counterValue": 0,
                "startTime": "2023-08-30T13:58:01.5985342+00:00",
                "endTime": "2023-09-06T13:58:01.5985342+00:00"
            },
            {
                "id": "/subscriptions/abcdefgh-1234-abcd-1234-a1b2c3d4e5f6/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/automation1/statistics/Failed",
                "counterProperty": "Failed",
                "counterValue": 0,
                "startTime": "2023-08-30T13:58:01.5985342+00:00",
                "endTime": "2023-09-06T13:58:01.5985342+00:00"
            }
        ]
    }

def list_usage_by_automation_account_results():
    return {
        "value": [
            {
                "name": {
                "value": "AccountUsage",
                "localizedValue": "AccountUsage"
                },
                "unit": "Minute",
                "currentValue": 0.0,
                "limit": -1,
                "throttleStatus": "NotThrottled"
            },
            {
                "name": {
                "value": "SubscriptionUsage",
                "localizedValue": "SubscriptionUsage"
                },
                "unit": "Minute",
                "currentValue": 0.0,
                "limit": -1,
                "throttleStatus": "NotThrottled"
            },
            {
                "name": {
                "value": "DscAccountUsage",
                "localizedValue": "DscAccountUsage"
                },
                "unit": "Count",
                "currentValue": 0.0,
                "limit": -1,
                "throttleStatus": "NotThrottled"
            }
        ]
    }

def mock_init():
    class MockClient(object):
        """ Add Mock connection data """

        def __init__(self):
            """ Mock """
            pass

        def create_account(self, payload):
            """ Mock create account results """
            return create_account_results()

        def update_account(self, payload):
            """ Mock update account results """
            return update_account_results()

        def delete_acount(self):
            """ Mock delete account results """
            class MockDeleteAccount(object):
                status_code = 200
                text = ""
                def __init__(self):
                    """ Mock """
                    pass

            return MockDeleteAccount()

        def get_account(self):
            """ Mock get account results """
            return get_acc_results()

        def get_module_activity(self, moduleName, activityName):
            """ Mock get module activity results """
            return get_module_activity_results()

        def list_accounts_by_resource_group(self):
            """ Mock list accounts by resource group results """
            return list_accounts_by_resource_group_results()

        def list_accounts(self):
            """ Mock list accounts results """
            return list_accounts_results()

        def list_module_activities(self, moduleName):
            """ Mock list module activities results """
            return list_module_activities_results()

        def run_runbook(self, runbook_name, job_name = 0, runbook_parameters = {}):
            """ Mock run runbook results """
            return {"name": job_name}

        def get_job_final_status(self, job_name, time_to_wait):
            """ Mock get job final status results """
            return "Completed"

        def get_job_results(self, job_name):
            """ Mock get job results results """
            return get_job_output_results()

        def get_runbook(self, runbook_name):
            """ Mock get runbook results """
            return get_runbook_results()

        def list_runbooks_by_automation_account(self):
            """ Mock list runbooks by automation account results """
            return list_runbooks_by_automation_account_results()

        def delete_runbook(self, runbook_name):
            """ Mock delete runbook results """
            class MockDeleteRunbook(object):
                status_code = 200
                text = ""
                def __init__(self):
                    """ Mock """
                    pass

            return MockDeleteRunbook()

        def get_job(self, job_name):
            """ Mock get job results """
            return get_job_results()

        def list_jobs_by_automation_account(self):
            """ Mock List jobs by automation account results """
            return list_jobs_by_automation_account_results()

        def stop_job(self, job_name):
            """ Mock stop job results """
            class MockStopJob(object):
                status_code = 200
                text = ""
                def __init__(self):
                    """ Mock """
                    pass

            return MockStopJob()

        def resume_job(self, job_name):
            """ Mock resume job results """
            class MockResumeJob(object):
                status_code = 200
                text = ""
                def __init__(self):
                    """ Mock """
                    pass

            return MockResumeJob()

        def suspend_job(self, job_name):
            """ Mock suspend job results """
            class MockSuspendJob(object):
                status_code = 200
                text = ""
                def __init__(self):
                    """ Mock """
                    pass

            return MockSuspendJob()

        def get_agent_registration_information(self):
            """ Mock get agent registration information results """
            return get_agent_registration_information_results()

        def regenerate_account_registration_key(self, payload):
            """ Mock regenerate account registration key results """
            return regenerate_account_registration_key_results()

        def create_credential(self, credential_name: str, payload: dict):
            """ Mock create credential results """
            return create_credential_results()

        def delete_credential(self, credential_name: str):
            """ Mock delete credential results """
            class MockDeleteCred(object):
                status_code = 200
                text = ""
                def __init__(self):
                    """ Mock """
                    pass

            return MockDeleteCred()

        def get_credential(self, credential_name: str):
            """ Mock get credential results """
            return get_credential_results()

        def list_credentials_by_automation_account(self):
            """ Mock list credentials by automation account results """
            return list_credentials_by_automation_account_results()

        def update_credential(self, credential_name: str, payload: dict):
            """ Mock update credential results """
            return update_credential_results()

        def create_schedule(self, schedule_name: str, payload: dict):
            """ Mock create schedule results """
            return create_schedule_results()

        def delete_schedule(self, schedule_name: str):
            """ Mock delete schedule results """
            class MockDeleteSchedule(object):
                status_code = 200
                text = ""
                def __init__(self):
                    """ Mock """
                    pass

            return MockDeleteSchedule()

        def get_schedule(self, schedule_name: str):
            """ Mock get schedule results """
            return get_schedule_results()

        def list_schedule_by_automation_account(self):
            """ Mock list schedule by automation account results """
            return list_schedule_by_automation_account_results()

        def update_schedule(self, schedule_name: str, payload: dict):
            """ Mock update schedule results """
            return update_schedule_results()

        def get_node_report(self, node_id: str, report_id: str):
            """ Mock get node report results """
            return get_node_report_results()

        def list_node_report_by_node(self, node_id: str):
            """ Mock list node report by node results """
            return list_node_report_by_node_results()

        def list_statistics_by_automation_account(self):
            """ Mock list statistics by automation account results """
            return list_statistics_by_automation_account_results()

        def list_usage_by_automation_account(self):
            """ Mock list usage by automation account results """
            return list_usage_by_automation_account_results()

    return MockClient()
