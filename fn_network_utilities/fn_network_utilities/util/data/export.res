{
  "action_order": [],
  "actions": [
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "artifact.type",
          "method": "in",
          "type": null,
          "value": [
            "DNS Name",
            "URL",
            "Email Sender",
            "Email Recipient",
            "String",
            "URL Referer",
            "URI Path"
          ]
        }
      ],
      "enabled": true,
      "export_key": "Example: Network Utilities Domain Distance",
      "id": 39,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Network Utilities Domain Distance",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "8912f85a-9384-4bc8-b9f5-9ade684f12d6",
      "view_items": [],
      "workflows": [
        "example_network_utilities_domain_distance"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "artifact.type",
          "method": "equals",
          "type": null,
          "value": "URL"
        }
      ],
      "enabled": true,
      "export_key": "Example: Network Utilities Expand URL",
      "id": 40,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Network Utilities Expand URL",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "1b63e89c-7d63-4dd8-8ea8-907f230bd178",
      "view_items": [],
      "workflows": [
        "example_network_utilities_expand_url"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "artifact.type",
          "method": "in",
          "type": null,
          "value": [
            "DNS Name",
            "URL",
            "URI Path"
          ]
        }
      ],
      "enabled": true,
      "export_key": "Example: Network Utilities Extract SSL Certificate from URL",
      "id": 41,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Network Utilities Extract SSL Certificate from URL",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "ca13e85b-5123-4f58-9491-1261c134348c",
      "view_items": [],
      "workflows": [
        "example_network_utilities_extract_ssl_cert_from_url"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "artifact.type",
          "method": "in",
          "type": null,
          "value": [
            "IP Address",
            "DNS Name",
            "URL"
          ]
        }
      ],
      "enabled": true,
      "export_key": "Example: Network Utilities Linux Shell Command",
      "id": 42,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Network Utilities Linux Shell Command",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "3eac8b4a-ea29-47e5-a8c9-22ae4f97c27b",
      "view_items": [],
      "workflows": [
        "example_network_utilities_linux_shell_command"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "artifact.type",
          "method": "in",
          "type": null,
          "value": [
            "IP Address",
            "DNS Name",
            "URL"
          ]
        }
      ],
      "enabled": true,
      "export_key": "Example: Network Utilities Local Shell Command",
      "id": 43,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Network Utilities Local Shell Command",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "026a67d7-ecbd-4b96-b05f-d32abb8a3e8e",
      "view_items": [],
      "workflows": [
        "example_network_utilities_local_command"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "artifact.type",
          "method": "in",
          "type": null,
          "value": [
            "IP Address",
            "DNS Name",
            "URL"
          ]
        }
      ],
      "enabled": true,
      "export_key": "Example: Network Utilities Windows Shell Command",
      "id": 44,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Network Utilities Windows Shell Command",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "f22d94ff-2041-4390-8eee-e56ebb7821bb",
      "view_items": [],
      "workflows": [
        "example_network_utilities_windows_shell_command"
      ]
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "export_date": 1677194623439,
  "export_format_version": 2,
  "export_type": null,
  "fields": [
    {
      "allow_default_value": false,
      "blank_option": false,
      "calculated": false,
      "changeable": true,
      "chosen": false,
      "default_chosen_by_server": false,
      "deprecated": false,
      "export_key": "__function/network_utilities_domain_name",
      "hide_notification": false,
      "id": 315,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "network_utilities_domain_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "network_utilities_domain_name",
      "tooltip": "",
      "type_id": 11,
      "uuid": "049f1125-47dd-4cce-aa2d-8464662ddd7a",
      "values": []
    },
    {
      "allow_default_value": false,
      "blank_option": false,
      "calculated": false,
      "changeable": true,
      "chosen": false,
      "default_chosen_by_server": false,
      "deprecated": false,
      "export_key": "__function/network_utilities_resilient_url",
      "hide_notification": false,
      "id": 316,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "network_utilities_resilient_url",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "network_utilities_resilient_url",
      "tooltip": "",
      "type_id": 11,
      "uuid": "26d43822-5958-4a49-a1cf-a1b7ec7ce941",
      "values": []
    },
    {
      "allow_default_value": false,
      "blank_option": false,
      "calculated": false,
      "changeable": true,
      "chosen": false,
      "default_chosen_by_server": false,
      "deprecated": false,
      "export_key": "__function/network_utilities_shell_params",
      "hide_notification": false,
      "id": 318,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "network_utilities_shell_params",
      "operation_perms": {},
      "operations": [],
      "placeholder": "0.0.0.0,sample_profile,param3",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "network_utilities_shell_params",
      "tooltip": "Comma separated list",
      "type_id": 11,
      "uuid": "47b2737a-4419-4139-b164-3abea0b8da45",
      "values": []
    },
    {
      "allow_default_value": false,
      "blank_option": false,
      "calculated": false,
      "changeable": true,
      "chosen": false,
      "default_chosen_by_server": false,
      "deprecated": false,
      "export_key": "__function/network_utilities_shell_command",
      "hide_notification": false,
      "id": 319,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "network_utilities_shell_command",
      "operation_perms": {},
      "operations": [],
      "placeholder": "remote_command:remote_computer",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "network_utilities_shell_command",
      "tooltip": "Use remote_shell_command:remote_computer syntax if network_utilities_remote_computer is left blank.",
      "type_id": 11,
      "uuid": "4f01a5af-4481-4a81-b995-982aaea91491",
      "values": []
    },
    {
      "allow_default_value": false,
      "blank_option": false,
      "calculated": false,
      "changeable": true,
      "chosen": false,
      "default_chosen_by_server": false,
      "deprecated": false,
      "export_key": "__function/network_utilities_remote_computer",
      "hide_notification": false,
      "id": 320,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "network_utilities_remote_computer",
      "operation_perms": {},
      "operations": [],
      "placeholder": "username:password@server",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "network_utilities_remote_computer",
      "tooltip": "Remote computer in place of the value used in the app.config",
      "type_id": 11,
      "uuid": "657405d6-87a7-4c6d-a93f-accf3a914516",
      "values": []
    },
    {
      "allow_default_value": false,
      "blank_option": false,
      "calculated": false,
      "changeable": true,
      "chosen": false,
      "default_chosen_by_server": false,
      "deprecated": false,
      "export_key": "__function/network_utilities_https_url",
      "hide_notification": false,
      "id": 321,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "network_utilities_https_url",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "network_utilities_https_url",
      "tooltip": "",
      "type_id": 11,
      "uuid": "681ea929-aae2-42ae-bfde-a26a05f1c1ab",
      "values": []
    },
    {
      "allow_default_value": false,
      "blank_option": false,
      "calculated": false,
      "changeable": true,
      "chosen": false,
      "default_chosen_by_server": false,
      "deprecated": false,
      "export_key": "__function/network_utilities_domain_list",
      "hide_notification": false,
      "id": 323,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "network_utilities_domain_list",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "network_utilities_domain_list",
      "tooltip": "",
      "type_id": 11,
      "uuid": "7ec18a05-6c97-4b68-baab-9f8d6c869a2d",
      "values": []
    },
    {
      "export_key": "incident/internal_customizations_field",
      "id": 0,
      "input_type": "text",
      "internal": true,
      "name": "internal_customizations_field",
      "read_only": true,
      "text": "Customizations Field (internal)",
      "type_id": 0,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa1"
    }
  ],
  "functions": [
    {
      "created_date": 1675211719808,
      "description": {
        "content": "Identifies similarity between a suspicious domain name and a list of valid domain names.  Low distance result indicates a possible spoof attempt.",
        "format": "text"
      },
      "destination_handle": "fn_network_utilities",
      "display_name": "Network Utilities: Domain Distance",
      "export_key": "network_utilities_domain_distance",
      "id": 20,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1677075062483,
      "name": "network_utilities_domain_distance",
      "tags": [],
      "uuid": "862f0096-cf1d-4f56-89bb-750e1c794221",
      "version": 2,
      "view_items": [
        {
          "content": "049f1125-47dd-4cce-aa2d-8464662ddd7a",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "7ec18a05-6c97-4b68-baab-9f8d6c869a2d",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        {
          "actions": [],
          "description": null,
          "name": "Example: Network Utilities Domain Distance",
          "object_type": "artifact",
          "programmatic_name": "example_network_utilities_domain_distance",
          "tags": [],
          "uuid": null,
          "workflow_id": 34
        }
      ]
    },
    {
      "created_date": 1675211719870,
      "description": {
        "content": "Takes a URL (mostly shortened) and follows it through redirects as it expands. The results include each URL, which are added to a new artifact.",
        "format": "text"
      },
      "destination_handle": "fn_network_utilities",
      "display_name": "Network Utilities: Expand URL",
      "export_key": "network_utilities_expand_url",
      "id": 21,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1677075104782,
      "name": "network_utilities_expand_url",
      "tags": [],
      "uuid": "3aef1c42-2c9e-4a7a-9421-8fab3a45e4f1",
      "version": 2,
      "view_items": [
        {
          "content": "26d43822-5958-4a49-a1cf-a1b7ec7ce941",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        {
          "actions": [],
          "description": null,
          "name": "Example: Network Utilities Expand URL",
          "object_type": "artifact",
          "programmatic_name": "example_network_utilities_expand_url",
          "tags": [],
          "uuid": null,
          "workflow_id": 35
        }
      ]
    },
    {
      "created_date": 1675211719931,
      "description": {
        "content": "This function takes in a HTTPS URL or DNS input, establishes a connection and then attempts to acquire the SSL certificate. If successful, the function then saves the certificate as an artifact of type \u2018X509 Certificate File\u2019. Works on most URLs including those with self-signed or expired certificates.",
        "format": "text"
      },
      "destination_handle": "fn_network_utilities",
      "display_name": "Network Utilities: Extract SSL Cert From URL",
      "export_key": "network_utilities_extract_ssl_cert_from_url",
      "id": 22,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1677075352832,
      "name": "network_utilities_extract_ssl_cert_from_url",
      "tags": [],
      "uuid": "7808f13e-7f37-4694-8303-66df82e8d958",
      "version": 2,
      "view_items": [
        {
          "content": "681ea929-aae2-42ae-bfde-a26a05f1c1ab",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        {
          "actions": [],
          "description": null,
          "name": "Example: Network Utilities Extract SSL Cert from URL",
          "object_type": "artifact",
          "programmatic_name": "example_network_utilities_extract_ssl_cert_from_url",
          "tags": [],
          "uuid": null,
          "workflow_id": 36
        }
      ]
    },
    {
      "created_date": 1675211719990,
      "description": {
        "content": "This function allows your workflows/playbooks to execute shell-scripts remotely via a linux machine, and return the result into the workflow/playbook. The results include the `stdout` and `stderr` streams, the return code, and information about the execution time. If the output of the shell script is JSON, it is returned as structured data. Results can then be added to the incident as file attachments, artifacts, data tables, or any other uses.",
        "format": "text"
      },
      "destination_handle": "fn_network_utilities",
      "display_name": "Network Utilities: Linux Shell Command",
      "export_key": "network_utilities_linux_shell_command",
      "id": 23,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1677075773138,
      "name": "network_utilities_linux_shell_command",
      "tags": [],
      "uuid": "743e7638-20e7-4cc5-ab80-f669d641c438",
      "version": 2,
      "view_items": [
        {
          "content": "4f01a5af-4481-4a81-b995-982aaea91491",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "657405d6-87a7-4c6d-a93f-accf3a914516",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "47b2737a-4419-4139-b164-3abea0b8da45",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        {
          "actions": [],
          "description": null,
          "name": "Example: Network Utilities Linux Shell Command",
          "object_type": "artifact",
          "programmatic_name": "example_network_utilities_linux_shell_command",
          "tags": [],
          "uuid": null,
          "workflow_id": 37
        }
      ]
    },
    {
      "created_date": 1675211720049,
      "description": {
        "content": "This function allows your workflows/playbooks to execute shell-scripts locally and return the result into the workflow/playbook. The results include the `stdout` and `stderr` streams, the return code, and information about the execution time. If the output of the shell script is JSON, it is returned as structured data. Results can then be added to the incident as file attachments, artifacts, data tables, or any other uses.",
        "format": "text"
      },
      "destination_handle": "fn_network_utilities",
      "display_name": "Network Utilities: Local Shell Command",
      "export_key": "network_utilities_local_shell_command",
      "id": 24,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1677075795743,
      "name": "network_utilities_local_shell_command",
      "tags": [],
      "uuid": "bdcffebf-b4ae-4566-a2e9-5d68c3f43ce4",
      "version": 2,
      "view_items": [
        {
          "content": "47b2737a-4419-4139-b164-3abea0b8da45",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "4f01a5af-4481-4a81-b995-982aaea91491",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        {
          "actions": [],
          "description": null,
          "name": "Example: Network Utilities Local Command",
          "object_type": "artifact",
          "programmatic_name": "example_network_utilities_local_command",
          "tags": [],
          "uuid": null,
          "workflow_id": 38
        }
      ]
    },
    {
      "created_date": 1675211720107,
      "description": {
        "content": "This function allows your workflows/playbooks to execute shell-scripts remotely via a windows machine, and return the result into the workflow/playbook. The results include the `stdout` and `stderr` streams, the return code, and information about the execution time. If the output of the shell script is JSON, it is returned as structured data. Results can then be added to the incident as file attachments, artifacts, data tables, or any other uses.",
        "format": "text"
      },
      "destination_handle": "fn_network_utilities",
      "display_name": "Network Utilities: Windows Shell Command",
      "export_key": "network_utilities_windows_shell_command",
      "id": 25,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1677075995319,
      "name": "network_utilities_windows_shell_command",
      "tags": [],
      "uuid": "c7da65e5-7760-4e63-9305-7c4f94f6f4ea",
      "version": 2,
      "view_items": [
        {
          "content": "4f01a5af-4481-4a81-b995-982aaea91491",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "657405d6-87a7-4c6d-a93f-accf3a914516",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "47b2737a-4419-4139-b164-3abea0b8da45",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        {
          "actions": [],
          "description": null,
          "name": "Example: Network Utilities Windows Shell Command",
          "object_type": "artifact",
          "programmatic_name": "example_network_utilities_windows_shell_command",
          "tags": [],
          "uuid": null,
          "workflow_id": 39
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 13,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1677194621381,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1677194621381,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "industries": null,
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [
        "922e405b-8bec-4a67-91f1-b726c9dcc6a5"
      ],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "fn_network_utilities",
      "name": "fn_network_utilities",
      "programmatic_name": "fn_network_utilities",
      "tags": [],
      "users": [],
      "uuid": "6676e7e5-9fd1-481a-8b47-b27feab5f61c"
    }
  ],
  "notifications": null,
  "overrides": null,
  "phases": [],
  "playbooks": [],
  "regulators": null,
  "roles": [],
  "scripts": [],
  "server_version": {
    "build_number": 7899,
    "major": 45,
    "minor": 0,
    "version": "45.0.7899"
  },
  "tags": [],
  "task_order": [],
  "timeframes": null,
  "types": [],
  "workflows": [
    {
      "actions": [],
      "content": {
        "version": 3,
        "workflow_id": "example_network_utilities_windows_shell_command",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_network_utilities_windows_shell_command\" isExecutable=\"true\" name=\"Example: Network Utilities Windows Shell Command\"\u003e\u003cdocumentation\u003eAn example running shell commands in a Windows machine for integration\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1kabw20\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cendEvent id=\"EndEvent_16pt7af\"\u003e\u003cincoming\u003eSequenceFlow_086uw7e\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1kabw20\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_03oyqcc\"/\u003e\u003cserviceTask id=\"ServiceTask_03oyqcc\" name=\"Network Utilities: Windows Shell ...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"c7da65e5-7760-4e63-9305-7c4f94f6f4ea\"\u003e{\"inputs\":{\"4f01a5af-4481-4a81-b995-982aaea91491\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"psinfo:remote_computer\"}}},\"post_processing_script\":\"# Outputs are:\\n#  - \\\"commandline\\\": the command that ran\\n#  - \\\"start\\\": timestamp, epoch milliseconds\\n#  - \\\"end\\\": timestamp, epoch milliseconds\\n#  - \\\"elapsed\\\": milliseconds\\n#  - \\\"exitcode\\\": nonzero indicates that the command failed\\n#  - \\\"stdout\\\": text output from the command\\n#  - \\\"stderr\\\": error text output from the command\\n#  - \\\"stdout_json\\\": object parsed from JSON output from the command\\n#  - \\\"stderr_json\\\": object parsed from JSON error output from the command\\ncontent = results.content\\nif content.get(\\\"exitcode\\\") == 0:\\n  note_text = u\\\"Command succeeded: {}\\\\nStandard Out: {}\\\\nStandard Error: {}\\\".format(content.get(\\\"commandline\\\"), content.get(\\\"stdout\\\"), content.get(\\\"stderr\\\"))\\nelse:\\n  note_text = u\\\"Command failed: {}\\\\nStandard Out: {}\\\\nStandard Error: {}\\\".format(content.get(\\\"commandline\\\"), content.get(\\\"stdout\\\"), content.get(\\\"stderr\\\"))\\n\\nincident.addNote(helper.createPlainText(note_text))\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"import re\\n\\ninputs.network_utilities_shell_params = artifact.value\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1kabw20\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_086uw7e\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_086uw7e\" sourceRef=\"ServiceTask_03oyqcc\" targetRef=\"EndEvent_16pt7af\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_16pt7af\" id=\"EndEvent_16pt7af_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"537\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"555\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1kabw20\" id=\"SequenceFlow_1kabw20_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"309\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"253.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_03oyqcc\" id=\"ServiceTask_03oyqcc_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"309\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_086uw7e\" id=\"SequenceFlow_086uw7e_di\"\u003e\u003comgdi:waypoint x=\"409\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"537\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"473\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 3,
      "description": "An example running shell commands in a Windows machine for integration",
      "export_key": "example_network_utilities_windows_shell_command",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1677193973790,
      "name": "Example: Network Utilities Windows Shell Command",
      "object_type": "artifact",
      "programmatic_name": "example_network_utilities_windows_shell_command",
      "tags": [],
      "uuid": "59c0f3a9-4b66-4372-b071-c601d7f0eab9",
      "workflow_id": 39
    },
    {
      "actions": [],
      "content": {
        "version": 2,
        "workflow_id": "example_network_utilities_expand_url",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_network_utilities_expand_url\" isExecutable=\"true\" name=\"Example: Network Utilities Expand URL\"\u003e\u003cdocumentation\u003e\u003c![CDATA[Take a url (mostly shortened) and follow it through redirects as it\u0027s expanded]]\u003e\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0rsaa6u\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cendEvent id=\"EndEvent_0gt85sm\"\u003e\u003cincoming\u003eSequenceFlow_1ovqa2x\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0rsaa6u\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1l9v3a5\"/\u003e\u003cserviceTask id=\"ServiceTask_1l9v3a5\" name=\"Network Utilities: Expand URL\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"3aef1c42-2c9e-4a7a-9421-8fab3a45e4f1\"\u003e{\"inputs\":{},\"post_processing_script\":\"# Results: {\u0027urllist\u0027: [\u0027https://community.ibm.com/community/user/security/communities/community-home?CommunityKey=d2f71e8c-108e-4652-b59c-29d61af7163e\u0027, \u0027https://community.ibm.com/community/user/security/communities/community-home\u0027]}\\n\\n# Add the url expansions to the Artifact Description\\nexpansions = results.get(\\\"urllist\\\", [])\\nexpansion_list = u\\\"Expansions:\\\\n\\\\n{0}\\\".format(\\\"\\\\n\\\\n\\\".join(expansions)) if expansions else \\\"No Expansions\\\"\\n\\nif artifact.description:\\n  artifact.description = \\\"{}\\\\n\\\\n{}\\\".format(artifact.description.content, expansion_list)\\nelse:\\n  artifact.description = expansion_list\\n  \\nfor url in expansions:\\n  incident.addArtifact(\\\"URL\\\", url, u\\\"expansion from {}\\\".format(artifact.value))\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.network_utilities_resilient_url = artifact.value\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0rsaa6u\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1ovqa2x\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1ovqa2x\" sourceRef=\"ServiceTask_1l9v3a5\" targetRef=\"EndEvent_0gt85sm\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0az2xwd\"\u003e\u003ctext\u003eNew artifacts are created and results update Artifact description\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1d7k0x8\" sourceRef=\"ServiceTask_1l9v3a5\" targetRef=\"TextAnnotation_0az2xwd\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0gt85sm\" id=\"EndEvent_0gt85sm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"565\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"583\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0rsaa6u\" id=\"SequenceFlow_0rsaa6u_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"314\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"256\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1l9v3a5\" id=\"ServiceTask_1l9v3a5_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"314\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1ovqa2x\" id=\"SequenceFlow_1ovqa2x_di\"\u003e\u003comgdi:waypoint x=\"414\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"565\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"489.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0az2xwd\" id=\"TextAnnotation_0az2xwd_di\"\u003e\u003comgdc:Bounds height=\"70\" width=\"129\" x=\"463\" y=\"21\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1d7k0x8\" id=\"Association_1d7k0x8_di\"\u003e\u003comgdi:waypoint x=\"406\" xsi:type=\"omgdc:Point\" y=\"168\"/\u003e\u003comgdi:waypoint x=\"490\" xsi:type=\"omgdc:Point\" y=\"91\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 2,
      "description": "Take a url (mostly shortened) and follow it through redirects as it\u0027s expanded",
      "export_key": "example_network_utilities_expand_url",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1677194475792,
      "name": "Example: Network Utilities Expand URL",
      "object_type": "artifact",
      "programmatic_name": "example_network_utilities_expand_url",
      "tags": [],
      "uuid": "58ee8181-0e55-427f-b54b-0ab7036ca4bf",
      "workflow_id": 35
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "example_network_utilities_extract_ssl_cert_from_url",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_network_utilities_extract_ssl_cert_from_url\" isExecutable=\"true\" name=\"Example: Network Utilities Extract SSL Cert from URL\"\u003e\u003cdocumentation\u003e\u003c![CDATA[This workflow takes in a HTTPS URL and attempts to acquire its Certificate, saving it as an artifact.\nThe workflow runs at the artifact level.]]\u003e\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1d73kfl\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cendEvent id=\"EndEvent_11no9n6\"\u003e\u003cincoming\u003eSequenceFlow_0hg3mxs\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1d73kfl\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0cm7wu6\"/\u003e\u003cserviceTask id=\"ServiceTask_0cm7wu6\" name=\"Network Utilities: Extract SSL Ce...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"7808f13e-7f37-4694-8303-66df82e8d958\"\u003e{\"inputs\":{},\"post_processing_script\":\"incident.addArtifact(\u0027X509 Certificate File\u0027, results.certificate, \u0027A certificate file gathered from provided the provided URL\u0027)\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.network_utilities_https_url = artifact.value\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1d73kfl\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0hg3mxs\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0hg3mxs\" sourceRef=\"ServiceTask_0cm7wu6\" targetRef=\"EndEvent_11no9n6\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_11no9n6\" id=\"EndEvent_11no9n6_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"642\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"660\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1d73kfl\" id=\"SequenceFlow_1d73kfl_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"357\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"277.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0cm7wu6\" id=\"ServiceTask_0cm7wu6_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"357\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0hg3mxs\" id=\"SequenceFlow_0hg3mxs_di\"\u003e\u003comgdi:waypoint x=\"457\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"642\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"549.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "description": "This workflow takes in a HTTPS URL and attempts to acquire its Certificate, saving it as an artifact.\nThe workflow runs at the artifact level.",
      "export_key": "example_network_utilities_extract_ssl_cert_from_url",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1677077352387,
      "name": "Example: Network Utilities Extract SSL Cert from URL",
      "object_type": "artifact",
      "programmatic_name": "example_network_utilities_extract_ssl_cert_from_url",
      "tags": [],
      "uuid": "01c1138c-4f61-4af2-9ae1-a44766855d5f",
      "workflow_id": 36
    },
    {
      "actions": [],
      "content": {
        "version": 8,
        "workflow_id": "example_network_utilities_domain_distance",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_network_utilities_domain_distance\" isExecutable=\"true\" name=\"Example: Network Utilities Domain Distance\"\u003e\u003cdocumentation\u003eAn example testing for confusable domain names\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_188jmgr\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cendEvent id=\"EndEvent_1jhl2gc\"\u003e\u003cincoming\u003eSequenceFlow_0ds0qnz\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_188jmgr\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0nn7czm\"/\u003e\u003cserviceTask id=\"ServiceTask_0nn7czm\" name=\"Network Utilities: Domain Distanc...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"862f0096-cf1d-4f56-89bb-750e1c794221\"\u003e{\"inputs\":{},\"post_processing_script\":\"# The result includes:\\n#   \\\"domain_name\\\" - the name being tested\\n#   \\\"distances\\\" - a dicctionary of all the distances\\n#   \\\"closest\\\" - the closest match from the list.\\n# If the match distance is only 1 or 0, the domain name is very easily confused with one on the list!\\n\\nif results.closest.get(\\\"distance\\\") \u0026lt;= 1:\\n  html = u\\\"\u0026lt;div\u0026gt;Warning!  Domain {} is easily confused with {}!\u0026lt;/div\u0026gt;\\\".format(results.get(\\\"domain_name\\\"), results.closest.get(\\\"name\\\"))\\n  incident.addNote(helper.createRichText(html))\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"# if email address, return only domain portion\\nif \\\"email\\\" in artifact.type.lower():\\n  split_email = artifact.value.split(\\\"@\\\")\\n  if len(split_email) \u0026gt; 1:\\n    inputs.network_utilities_domain_name = split_email[1]\\n  else:\\n    inputs.network_utilities_domain_name = artifact.value\\nelse:\\n  # The domain name being tested\\n  inputs.network_utilities_domain_name = artifact.value\\n\\n# The list of domains to test against\\ninputs.network_utilities_domain_list = \\\"ibm.com, resilientsystems.com, ibmcloud.com, bluemix.com\\\"\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_188jmgr\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0ds0qnz\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0ds0qnz\" sourceRef=\"ServiceTask_0nn7czm\" targetRef=\"EndEvent_1jhl2gc\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_07r70ac\"\u003e\u003ctext\u003e\u003c![CDATA[Calculates the \"word distance\" between a suspect name and a list of names.\u00a0 This can be useful for detecting spoofed URLs.\n\nThe distance is small if the names are similar.\u00a0 For each different or switched character, the distance increases.\u00a0 But \"confusable Unicode characters\" are treated as identical (they have zero distance).]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1095shk\" sourceRef=\"ServiceTask_0nn7czm\" targetRef=\"TextAnnotation_07r70ac\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1jhl2gc\" id=\"EndEvent_1jhl2gc_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"590\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"608\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_188jmgr\" id=\"SequenceFlow_188jmgr_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"331\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"264.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0nn7czm\" id=\"ServiceTask_0nn7czm_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"331\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0ds0qnz\" id=\"SequenceFlow_0ds0qnz_di\"\u003e\u003comgdi:waypoint x=\"431\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"590\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"510.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_07r70ac\" id=\"TextAnnotation_07r70ac_di\"\u003e\u003comgdc:Bounds height=\"153\" width=\"245\" x=\"473\" y=\"-25\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1095shk\" id=\"Association_1095shk_di\"\u003e\u003comgdi:waypoint x=\"428\" xsi:type=\"omgdc:Point\" y=\"173\"/\u003e\u003comgdi:waypoint x=\"490\" xsi:type=\"omgdc:Point\" y=\"128\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 8,
      "description": "An example testing for confusable domain names",
      "export_key": "example_network_utilities_domain_distance",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1677187821850,
      "name": "Example: Network Utilities Domain Distance",
      "object_type": "artifact",
      "programmatic_name": "example_network_utilities_domain_distance",
      "tags": [],
      "uuid": "8cb9d581-9bc0-42ca-a8ca-9cb538a32742",
      "workflow_id": 34
    },
    {
      "actions": [],
      "content": {
        "version": 7,
        "workflow_id": "example_network_utilities_local_command",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_network_utilities_local_command\" isExecutable=\"true\" name=\"Example: Network Utilities Local Command\"\u003e\u003cdocumentation\u003eAn example of running a local shell command for integration.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_084by47\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cendEvent id=\"EndEvent_0plmuwn\"\u003e\u003cincoming\u003eSequenceFlow_03d4mym\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_084by47\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_025ltc7\"/\u003e\u003cserviceTask id=\"ServiceTask_025ltc7\" name=\"Network Utilities: Local Shell Co...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"bdcffebf-b4ae-4566-a2e9-5d68c3f43ce4\"\u003e{\"inputs\":{\"4f01a5af-4481-4a81-b995-982aaea91491\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"traceroute\"}}},\"post_processing_script\":\"# Outputs are:\\n#  - \\\"commandline\\\": the command that ran\\n#  - \\\"start\\\": timestamp, epoch milliseconds\\n#  - \\\"end\\\": timestamp, epoch milliseconds\\n#  - \\\"elapsed\\\": milliseconds\\n#  - \\\"exitcode\\\": nonzero indicates that the command failed\\n#  - \\\"stdout\\\": text output from the command\\n#  - \\\"stderr\\\": error text output from the command\\n#  - \\\"stdout_json\\\": object parsed from JSON output from the command\\n#  - \\\"stderr_json\\\": object parsed from JSON error output from the command\\ncontent = results.content\\nif content.get(\\\"exitcode\\\") == 0:\\n  note_text = u\\\"Command succeeded: {}\\\\nStandard Out: {}\\\\nStandard Error: {}\\\".format(content.get(\\\"commandline\\\"), content.get(\\\"stdout\\\"), content.get(\\\"stderr\\\"))\\nelse:\\n  note_text = u\\\"Command failed: {}\\\\nStandard Out: {}\\\\nStandard Error: {}\\\".format(content.get(\\\"commandline\\\"), content.get(\\\"stdout\\\"), content.get(\\\"stderr\\\"))\\n\\nincident.addNote(helper.createPlainText(note_text))\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"import re\\n\\ninputs.network_utilities_shell_params = artifact.value\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_084by47\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_03d4mym\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_03d4mym\" sourceRef=\"ServiceTask_025ltc7\" targetRef=\"EndEvent_0plmuwn\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0plmuwn\" id=\"EndEvent_0plmuwn_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"546\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"564\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_084by47\" id=\"SequenceFlow_084by47_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"326\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"262\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_025ltc7\" id=\"ServiceTask_025ltc7_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"326\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_03d4mym\" id=\"SequenceFlow_03d4mym_di\"\u003e\u003comgdi:waypoint x=\"426\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"546\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"486\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 7,
      "description": "An example of running a local shell command for integration.",
      "export_key": "example_network_utilities_local_command",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1677190004744,
      "name": "Example: Network Utilities Local Command",
      "object_type": "artifact",
      "programmatic_name": "example_network_utilities_local_command",
      "tags": [],
      "uuid": "bc467ba5-27f4-4a4a-8841-9bc55c05c24b",
      "workflow_id": 38
    },
    {
      "actions": [],
      "content": {
        "version": 6,
        "workflow_id": "example_network_utilities_linux_shell_command",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_network_utilities_linux_shell_command\" isExecutable=\"true\" name=\"Example: Network Utilities Linux Shell Command\"\u003e\u003cdocumentation\u003eAn example running shell commands in a Linux machine for integration\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1yf1ay9\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cendEvent id=\"EndEvent_10jhy3g\"\u003e\u003cincoming\u003eSequenceFlow_08sw25v\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1yf1ay9\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_19g7uoc\"/\u003e\u003cserviceTask id=\"ServiceTask_19g7uoc\" name=\"Network Utilities: Linux Shell Co...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"743e7638-20e7-4cc5-ab80-f669d641c438\"\u003e{\"inputs\":{\"4f01a5af-4481-4a81-b995-982aaea91491\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"remote_command_linux:remote_computer\"}}},\"post_processing_script\":\"# Outputs are:\\n#  - \\\"commandline\\\": the command that ran\\n#  - \\\"start\\\": timestamp, epoch milliseconds\\n#  - \\\"end\\\": timestamp, epoch milliseconds\\n#  - \\\"elapsed\\\": milliseconds\\n#  - \\\"exitcode\\\": nonzero indicates that the command failed\\n#  - \\\"stdout\\\": text output from the command\\n#  - \\\"stderr\\\": error text output from the command\\n#  - \\\"stdout_json\\\": object parsed from JSON output from the command\\n#  - \\\"stderr_json\\\": object parsed from JSON error output from the command\\ncontent = results.content\\nif content.get(\\\"exitcode\\\") == 0:\\n  note_text = u\\\"Command succeeded: {}\\\\nStandard Out: {}\\\\nStandard Error: {}\\\".format(content.get(\\\"commandline\\\"), content.get(\\\"stdout\\\"), content.get(\\\"stderr\\\"))\\nelse:\\n  note_text = u\\\"Command failed: {}\\\\nStandard Out: {}\\\\nStandard Error: {}\\\".format(content.get(\\\"commandline\\\"), content.get(\\\"stdout\\\"), content.get(\\\"stderr\\\"))\\n\\nincident.addNote(helper.createPlainText(note_text))\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"import re\\n# You can set the command on the \\\"Input\\\" panel or dynamically\\n# NOTE: The administrator must configure each command before you can run it!\\n#inputs..network_utilities_shell_commandshell_command = \\\"traceroute\\\"\\n\\ninputs.network_utilities_shell_params = artifact.value\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1yf1ay9\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_08sw25v\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_08sw25v\" sourceRef=\"ServiceTask_19g7uoc\" targetRef=\"EndEvent_10jhy3g\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_10jhy3g\" id=\"EndEvent_10jhy3g_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"527\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"545\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1yf1ay9\" id=\"SequenceFlow_1yf1ay9_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"312\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"255\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_19g7uoc\" id=\"ServiceTask_19g7uoc_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"312\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_08sw25v\" id=\"SequenceFlow_08sw25v_di\"\u003e\u003comgdi:waypoint x=\"412\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"527\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"469.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 6,
      "description": "An example running shell commands in a Linux machine for integration",
      "export_key": "example_network_utilities_linux_shell_command",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1677188950232,
      "name": "Example: Network Utilities Linux Shell Command",
      "object_type": "artifact",
      "programmatic_name": "example_network_utilities_linux_shell_command",
      "tags": [],
      "uuid": "92deb553-ca81-4a62-a130-0a0780dd5ee7",
      "workflow_id": 37
    }
  ],
  "workspaces": []
}
