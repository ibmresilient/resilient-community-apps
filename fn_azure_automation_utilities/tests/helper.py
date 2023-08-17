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
        "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/demoassets/providers/Microsoft.Automation/automationAccounts/automation1/modules/Az.Advisor/activities/Set-AzAdvisorConfiguration",
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
                "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/demoassets/providers/Microsoft.Automation/automationAccounts/automation1/modules/Az.Advisor/activities/Disable-AzAdvisorRecommendation",
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
                "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/demoassets/providers/Microsoft.Automation/automationAccounts/automation1/modules/Az.Advisor/activities/Enable-AzAdvisorRecommendation",
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
                "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/demoassets/providers/Microsoft.Automation/automationAccounts/automation1/modules/Az.Advisor/activities/Get-AzAdvisorConfiguration",
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
                "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/demoassets/providers/Microsoft.Automation/automationAccounts/automation1/modules/Az.Advisor/activities/Get-AzAdvisorRecommendation",
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
                "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/demoassets/providers/Microsoft.Automation/automationAccounts/automation1/modules/Az.Advisor/activities/Set-AzAdvisorConfiguration",
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
                "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/demoassets/providers/Microsoft.Automation/automationAccounts/automation1/runbooks/AzureAutomationTutorialWithIdentity",
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
                "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/demoassets/providers/Microsoft.Automation/automationAccounts/automation1/runbooks/AzureAutomationTutorialWithIdentityGraphical",
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
        "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/demoassets/providers/Microsoft.Automation/automationAccounts/automation1/runbooks/Hello_world",
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
        "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/demoassets/providers/Microsoft.Automation/automationAccounts/automation1/jobs/1692024049238",
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
                "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/demoassets/providers/Microsoft.Automation/automationAccounts/automation1/jobs/1692024049238",
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
                "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/demoassets/providers/Microsoft.Automation/automationAccounts/automation1/jobs/1691761457680",
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

        def get_job_results(self, job_name):
            """ Mock get job results return """
            return get_job_output_results()

        def get_runbook(self, runbook_name):
            """ Mock get runbook return """
            return get_runbook_results()

        def list_runbooks_by_automation_account(self):
            """ Mock list runbooks by automation account return """
            return list_runbooks_by_automation_account_results()

        def delete_runbook(self, runbook_name):
            """ Mock delete runbook return """
            class MockDeleteRunbook(object):
                status_code = 200
                text = ""
                def __init__(self):
                    """ Mock """
                    pass

            return MockDeleteRunbook()

        def get_job(self, job_name):
            """ Mock get job return """
            return get_job_results()

        def list_jobs_by_automation_account(self):
            """ Mock List jobs by automation account return """
            return list_jobs_by_automation_account_results()

        def stop_automation_job(self, job_name):
            """ Mock stop automation job results """
            class MockStopJob(object):
                status_code = 200
                text = ""
                def __init__(self):
                    """ Mock """
                    pass

            return MockStopJob()

        def resume_automation_job(self, job_name):
            """ Mock resume automation job results """
            class MockResumeJob(object):
                status_code = 200
                text = ""
                def __init__(self):
                    """ Mock """
                    pass

            return MockResumeJob()

        def suspend_automation_job(self, job_name):
            """ Mock resume automation job results """
            class MockSuspendJob(object):
                status_code = 200
                text = ""
                def __init__(self):
                    """ Mock """
                    pass

            return MockSuspendJob()

    return MockClient()
