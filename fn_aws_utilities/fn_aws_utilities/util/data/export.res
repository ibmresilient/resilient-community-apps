{
  "action_order": [],
  "actions": [
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: Invoke AWS Lambda: Python Addition",
      "id": 281,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Invoke AWS Lambda: Python Addition",
      "object_type": "incident",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "99336c11-d664-4f11-b21b-433ddfb20d9f",
      "view_items": [],
      "workflows": [
        "example_invoke_aws_lambda_python_addition"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: Invoke AWS Step Function: Asynchronous",
      "id": 282,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Invoke AWS Step Function: Asynchronous",
      "object_type": "incident",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "6a34d9a0-3f60-4c0c-93aa-3889fcc17677",
      "view_items": [],
      "workflows": [
        "example_invoke_step_function_asynchronous"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: Invoke AWS Step Function: Synchronous",
      "id": 283,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Invoke AWS Step Function: Synchronous",
      "object_type": "incident",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "1617b3c7-e749-4b03-ab4b-81b71fa67b82",
      "view_items": [],
      "workflows": [
        "example_invoke_step_function_synchronous"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: Send AWS SMS",
      "id": 284,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Send AWS SMS",
      "object_type": "incident",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "aa2c7000-2d15-43ff-9804-11da487a5749",
      "view_items": [
        {
          "content": "82492d2e-f204-40f5-a61a-9e577316bdb8",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "example_send_sms_incident"
      ]
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "case_matching_profiles": [],
  "export_date": 1736347674319,
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
      "export_key": "__function/lambda_payload",
      "hide_notification": false,
      "id": 5789,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "lambda_payload",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "lambda_payload",
      "tooltip": "The payload to send to the AWS Lambda function",
      "type_id": 11,
      "uuid": "8efdf646-682c-4598-97c0-9fd9a402e5b3",
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
      "export_key": "__function/state_machine_name",
      "hide_notification": false,
      "id": 5790,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "state_machine_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "state_machine_name",
      "tooltip": "Name of state machine to invoke",
      "type_id": 11,
      "uuid": "9e57bf10-5426-4c48-aa8c-9d33a583ba38",
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
      "export_key": "__function/state_machine_async",
      "hide_notification": false,
      "id": 5791,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "state_machine_async",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "state_machine_async",
      "tooltip": "Whether or not to wait for execution to complete",
      "type_id": 11,
      "uuid": "a8449ba9-f510-41ad-9b8f-f04ec019cd22",
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
      "export_key": "__function/lambda_function_name",
      "hide_notification": false,
      "id": 5792,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "lambda_function_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "lambda_function_name",
      "tooltip": "Name of the AWS function to execute",
      "type_id": 11,
      "uuid": "d773d35a-f441-4521-8718-77f88864e360",
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
      "export_key": "__function/state_machine_payload",
      "hide_notification": false,
      "id": 5793,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "state_machine_payload",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "state_machine_payload",
      "tooltip": "Payload to give the state machine",
      "type_id": 11,
      "uuid": "09c0c85c-ea62-4e04-b9b6-b48f5bf463ad",
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
      "export_key": "__function/msg_body",
      "hide_notification": false,
      "id": 5794,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "msg_body",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "msg_body",
      "tooltip": "",
      "type_id": 11,
      "uuid": "5890a587-e632-4900-af9f-3671984243f8",
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
      "export_key": "__function/execution_arn",
      "hide_notification": false,
      "id": 5795,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "execution_arn",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "execution_arn",
      "tooltip": "State machine execution identifier",
      "type_id": 11,
      "uuid": "67ac58f5-ae79-47b3-8d6e-c749db326081",
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
      "export_key": "__function/phone_numbers",
      "hide_notification": false,
      "id": 5796,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "phone_numbers",
      "operation_perms": {},
      "operations": [],
      "placeholder": "[\"11234567890\",\"19876543211\"]",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "phone_numbers",
      "tooltip": "JSON array of phone numbers to text",
      "type_id": 11,
      "uuid": "6e14b737-ada0-4566-81a7-f045a4d3e01b",
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
      "export_key": "actioninvocation/aws_utilities_phone_number",
      "hide_notification": false,
      "id": 5797,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "aws_utilities_phone_number",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "short_text": "",
      "tags": [],
      "templates": [],
      "text": "phone number",
      "tooltip": "A phone number to send the SMS to.",
      "type_id": 6,
      "uuid": "82492d2e-f204-40f5-a61a-9e577316bdb8",
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
      "created_date": 1736252497321,
      "description": {
        "content": "Returns information about a step function execution",
        "format": "text"
      },
      "destination_handle": "fn_aws_utilities",
      "display_name": "Get AWS Step Function Execution",
      "export_key": "fn_get_step_function_execution",
      "id": 124,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 48,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1736252497321,
      "name": "fn_get_step_function_execution",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "tags": [],
      "uuid": "d90cae6e-ac76-4c13-b6cd-ff2d75dda26d",
      "version": 0,
      "view_items": [
        {
          "content": "67ac58f5-ae79-47b3-8d6e-c749db326081",
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
          "name": "Example: Invoke AWS Step Function: Asynchronous",
          "object_type": "incident",
          "programmatic_name": "example_invoke_step_function_asynchronous",
          "tags": [],
          "uuid": null,
          "workflow_id": 117
        }
      ]
    },
    {
      "created_date": 1736252497531,
      "description": {
        "content": "Invokes an AWS Lambda function synchronously and returns the function output",
        "format": "text"
      },
      "destination_handle": "fn_aws_utilities",
      "display_name": "Invoke AWS Lambda",
      "export_key": "fn_invoke_lambda",
      "id": 125,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 48,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1736252497531,
      "name": "fn_invoke_lambda",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "tags": [],
      "uuid": "3bacbd68-d5a6-4a44-a385-c126595f599b",
      "version": 0,
      "view_items": [
        {
          "content": "d773d35a-f441-4521-8718-77f88864e360",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "8efdf646-682c-4598-97c0-9fd9a402e5b3",
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
          "name": "Example: Invoke AWS Lambda: Python Addition",
          "object_type": "incident",
          "programmatic_name": "example_invoke_aws_lambda_python_addition",
          "tags": [],
          "uuid": null,
          "workflow_id": 118
        }
      ]
    },
    {
      "created_date": 1736252497754,
      "description": {
        "content": "Invokes a step function (state machine)",
        "format": "text"
      },
      "destination_handle": "fn_aws_utilities",
      "display_name": "Invoke AWS Step Function",
      "export_key": "fn_invoke_step_function",
      "id": 126,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 48,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1736252497754,
      "name": "fn_invoke_step_function",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "tags": [],
      "uuid": "18ec522b-bb19-473d-9ee5-d9738e68d72e",
      "version": 0,
      "view_items": [
        {
          "content": "9e57bf10-5426-4c48-aa8c-9d33a583ba38",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "a8449ba9-f510-41ad-9b8f-f04ec019cd22",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "09c0c85c-ea62-4e04-b9b6-b48f5bf463ad",
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
          "name": "Example: Invoke AWS Step Function: Asynchronous",
          "object_type": "incident",
          "programmatic_name": "example_invoke_step_function_asynchronous",
          "tags": [],
          "uuid": null,
          "workflow_id": 117
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: Invoke AWS Step Function: Synchronous",
          "object_type": "incident",
          "programmatic_name": "example_invoke_step_function_synchronous",
          "tags": [],
          "uuid": null,
          "workflow_id": 115
        }
      ]
    },
    {
      "created_date": 1736252498000,
      "description": {
        "content": "Sends an SMS message to a list of phone numbers using AWS SNS",
        "format": "text"
      },
      "destination_handle": "fn_aws_utilities",
      "display_name": "Send SMS using AWS SNS",
      "export_key": "fn_send_sms_via_sns",
      "id": 127,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 48,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1736252498000,
      "name": "fn_send_sms_via_sns",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "tags": [],
      "uuid": "bb5c9a60-caf2-48dc-8d25-1acb6f0750fc",
      "version": 0,
      "view_items": [
        {
          "content": "6e14b737-ada0-4566-81a7-f045a4d3e01b",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "5890a587-e632-4900-af9f-3671984243f8",
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
          "name": "Example: Send SMS: Incident",
          "object_type": "incident",
          "programmatic_name": "example_send_sms_incident",
          "tags": [],
          "uuid": null,
          "workflow_id": 116
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 54,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1736347672542,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1736347672542,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "fn_aws_utilities",
      "name": "fn_aws_utilities",
      "programmatic_name": "fn_aws_utilities",
      "tags": [],
      "users": [
        "admin@example.com"
      ],
      "uuid": "119726ac-0af0-46c7-96b4-9f1e133f2f99"
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
    "build_number": 9339,
    "f": 0,
    "m": 0,
    "major": 0,
    "minor": 0,
    "r": 0,
    "v": 51,
    "version": "51.0.0.0.9339"
  },
  "tags": [],
  "task_order": [],
  "timeframes": null,
  "types": [],
  "workflows": [
    {
      "actions": [],
      "content": {
        "version": 2,
        "workflow_id": "example_invoke_step_function_synchronous",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_invoke_step_function_synchronous\" isExecutable=\"true\" name=\"Example: Invoke AWS Step Function: Synchronous\"\u003e\u003cdocumentation\u003eInvokes a step function synchronously using a simple demonstration function\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1kk18u3\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_03ymwff\" name=\"Invoke AWS Step Function\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"18ec522b-bb19-473d-9ee5-d9738e68d72e\"\u003e{\"inputs\":{\"a8449ba9-f510-41ad-9b8f-f04ec019cd22\":{\"input_type\":\"static\",\"static_input\":{\"boolean_value\":false,\"multiselect_value\":[]}}},\"post_processing_script\":\"if results and results.get(\\\"output\\\"):\\n  text = \\\"Step Function (Synchronous) Result: \\\\n\\\\t\\\" + str(results.get(\\\"output\\\"))\\n  note = helper.createPlainText(text)\\n  incident.addNote(note)\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.state_machine_name = \\\"Helloworld\\\"\\ninputs.state_machine_async = False\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1kk18u3\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0mnpyzx\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndEvent_0vo6rqh\"\u003e\u003cincoming\u003eSequenceFlow_0mnpyzx\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1kk18u3\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_03ymwff\"/\u003e\u003csequenceFlow id=\"SequenceFlow_0mnpyzx\" sourceRef=\"ServiceTask_03ymwff\" targetRef=\"EndEvent_0vo6rqh\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_03ymwff\" id=\"ServiceTask_03ymwff_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"310\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0vo6rqh\" id=\"EndEvent_0vo6rqh_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"534\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"552\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1kk18u3\" id=\"SequenceFlow_1kk18u3_di\"\u003e\u003comgdi:waypoint x=\"198\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"310\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"254\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0mnpyzx\" id=\"SequenceFlow_0mnpyzx_di\"\u003e\u003comgdi:waypoint x=\"410\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"534\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"472\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 2,
      "description": "Invokes a step function synchronously using a simple demonstration function",
      "export_key": "example_invoke_step_function_synchronous",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1736345395594,
      "name": "Example: Invoke AWS Step Function: Synchronous",
      "object_type": "incident",
      "programmatic_name": "example_invoke_step_function_synchronous",
      "tags": [],
      "uuid": "c10113ca-bacd-4b1e-b524-d8b925c62af3",
      "workflow_id": 115
    },
    {
      "actions": [],
      "content": {
        "version": 3,
        "workflow_id": "example_send_sms_incident",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_send_sms_incident\" isExecutable=\"true\" name=\"Example: Send SMS: Incident\"\u003e\u003cdocumentation\u003eSends an SMS to members of an incident using AWS SNS\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_06vpi4i\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0jnots8\" name=\"Send SMS using AWS SNS\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"bb5c9a60-caf2-48dc-8d25-1acb6f0750fc\"\u003e{\"inputs\":{},\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.phone_numbers = rule.properties.aws_utilities_phone_number\\ninputs.msg_body = \\\"[Example Workflow, Send SMS: Incident] New incident, \\\" + incident.name + \\\", which you are a member of, has been created.\\\"\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_06vpi4i\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_16oov50\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndEvent_10oudi0\"\u003e\u003cincoming\u003eSequenceFlow_16oov50\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_16oov50\" sourceRef=\"ServiceTask_0jnots8\" targetRef=\"EndEvent_10oudi0\"/\u003e\u003csequenceFlow id=\"SequenceFlow_06vpi4i\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0jnots8\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_14v09u2\"\u003e\u003ctext\u003einputs: phone_numbers and msg_body\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0ssxwrb\" sourceRef=\"ServiceTask_0jnots8\" targetRef=\"TextAnnotation_14v09u2\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0f9df8k\"\u003e\u003ctext\u003eoutputs: message_id\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_094t14g\" sourceRef=\"ServiceTask_0jnots8\" targetRef=\"TextAnnotation_0f9df8k\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"330\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"325\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"268\" y=\"262\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"338\" y=\"221\"/\u003e\u003comgdi:waypoint x=\"321\" y=\"262\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0jnots8\" id=\"ServiceTask_0jnots8_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"486\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_10oudi0\" id=\"EndEvent_10oudi0_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"694\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"712\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_16oov50\" id=\"SequenceFlow_16oov50_di\"\u003e\u003comgdi:waypoint x=\"586\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"694\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"640\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_14v09u2\" id=\"TextAnnotation_14v09u2_di\"\u003e\u003comgdc:Bounds height=\"34\" width=\"156\" x=\"426\" y=\"47\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0ssxwrb\" id=\"Association_0ssxwrb_di\"\u003e\u003comgdi:waypoint x=\"527\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"509\" y=\"81\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0f9df8k\" id=\"TextAnnotation_0f9df8k_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"588\" y=\"49\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_094t14g\" id=\"Association_094t14g_di\"\u003e\u003comgdi:waypoint x=\"565\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"627\" y=\"79\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_06vpi4i\" id=\"SequenceFlow_06vpi4i_di\"\u003e\u003comgdi:waypoint x=\"366\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"486\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"426\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 3,
      "description": "Sends an SMS to members of an incident using AWS SNS",
      "export_key": "example_send_sms_incident",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1736253188379,
      "name": "Example: Send SMS: Incident",
      "object_type": "incident",
      "programmatic_name": "example_send_sms_incident",
      "tags": [],
      "uuid": "e6488620-5a06-4053-9cbf-9ab446b50a3e",
      "workflow_id": 116
    },
    {
      "actions": [],
      "content": {
        "version": 7,
        "workflow_id": "example_invoke_aws_lambda_python_addition",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_invoke_aws_lambda_python_addition\" isExecutable=\"true\" name=\"Example: Invoke AWS Lambda: Python Addition\"\u003e\u003cdocumentation\u003eAdds two numbers by executing an AWS Lambda function created in Python. Any Lambda function can be used in a similar fashion.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0qm9xnc\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0wfr3yu\" name=\"Invoke AWS Lambda\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"3bacbd68-d5a6-4a44-a385-c126595f599b\"\u003e{\"inputs\":{},\"post_processing_script\":\"if results and results.get(\\\"response_payload\\\"):\\n  text = \\\"Python Addition Result: \\\" + str(results.get(\\\"response_payload\\\"))\\n  note = helper.createPlainText(text)\\n  incident.addNote(note)\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.lambda_function_name = \\\"resilient_example_python_addition\\\"\\ninputs.lambda_payload = \u0027\u0027\u0027{ \\\"x\\\": 1, \\\"y\\\": 2 }\u0027\u0027\u0027\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0qm9xnc\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0bbksfg\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndEvent_05m5fvi\"\u003e\u003cincoming\u003eSequenceFlow_0bbksfg\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0qm9xnc\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0wfr3yu\"/\u003e\u003csequenceFlow id=\"SequenceFlow_0bbksfg\" sourceRef=\"ServiceTask_0wfr3yu\" targetRef=\"EndEvent_05m5fvi\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_16cfyir\"\u003e\u003ctext\u003einputs: lambda_function_name and lambda_payload\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1vpsnj3\" sourceRef=\"ServiceTask_0wfr3yu\" targetRef=\"TextAnnotation_16cfyir\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_00m0c0z\"\u003e\u003ctext\u003eoutputs: sum in an incident note\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0rxja7p\" sourceRef=\"ServiceTask_0wfr3yu\" targetRef=\"TextAnnotation_00m0c0z\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0wfr3yu\" id=\"ServiceTask_0wfr3yu_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"281\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_05m5fvi\" id=\"EndEvent_05m5fvi_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"475\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"493\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0qm9xnc\" id=\"SequenceFlow_0qm9xnc_di\"\u003e\u003comgdi:waypoint x=\"198\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"281\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"239.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0bbksfg\" id=\"SequenceFlow_0bbksfg_di\"\u003e\u003comgdi:waypoint x=\"381\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"475\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"428\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_16cfyir\" id=\"TextAnnotation_16cfyir_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"189\" x=\"146\" y=\"101\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1vpsnj3\" id=\"Association_1vpsnj3_di\"\u003e\u003comgdi:waypoint x=\"291\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"256\" y=\"131\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_00m0c0z\" id=\"TextAnnotation_00m0c0z_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"192\" x=\"364\" y=\"101\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0rxja7p\" id=\"Association_0rxja7p_di\"\u003e\u003comgdi:waypoint x=\"378\" y=\"173\"/\u003e\u003comgdi:waypoint x=\"439\" y=\"131\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 7,
      "description": "Adds two numbers by executing an AWS Lambda function created in Python. Any Lambda function can be used in a similar fashion.",
      "export_key": "example_invoke_aws_lambda_python_addition",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1736347661764,
      "name": "Example: Invoke AWS Lambda: Python Addition",
      "object_type": "incident",
      "programmatic_name": "example_invoke_aws_lambda_python_addition",
      "tags": [],
      "uuid": "b8442c4d-efd0-48f1-8637-708096123a3c",
      "workflow_id": 118
    },
    {
      "actions": [],
      "content": {
        "version": 4,
        "workflow_id": "example_invoke_step_function_asynchronous",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_invoke_step_function_asynchronous\" isExecutable=\"true\" name=\"Example: Invoke AWS Step Function: Asynchronous\"\u003e\u003cdocumentation\u003eInvokes a step function asynchronously using a simple demonstration function\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0d1cpx9\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0tf99yv\" name=\"Invoke AWS Step Function\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"18ec522b-bb19-473d-9ee5-d9738e68d72e\"\u003e{\"inputs\":{\"a8449ba9-f510-41ad-9b8f-f04ec019cd22\":{\"input_type\":\"static\",\"static_input\":{\"boolean_value\":true,\"multiselect_value\":[]}}},\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.state_machine_name = \\\"Helloworld\\\"\\ninputs.state_machine_async = True\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"execution_details\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0d1cpx9\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1ay969o\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cserviceTask id=\"ServiceTask_05g1ud3\" name=\"Get AWS Step Function Execution\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"d90cae6e-ac76-4c13-b6cd-ff2d75dda26d\"\u003e{\"inputs\":{},\"post_processing_script\":\"if results and results.get(\\\"output\\\"):\\n  text = \\\"Step Function (Asynchronous) Result: \\\\n\\\\t\\\" + str(results.get(\\\"output\\\"))\\n  note = helper.createPlainText(text)\\n  incident.addNote(note)\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"if workflow.properties.execution_details and workflow.properties.execution_details.executionArn:\\n  inputs.execution_arn = workflow.properties.execution_details.executionArn\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1ay969o\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1mrrjf2\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndEvent_0e7ewom\"\u003e\u003cincoming\u003eSequenceFlow_1mrrjf2\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0d1cpx9\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0tf99yv\"/\u003e\u003csequenceFlow id=\"SequenceFlow_1ay969o\" sourceRef=\"ServiceTask_0tf99yv\" targetRef=\"ServiceTask_05g1ud3\"/\u003e\u003csequenceFlow id=\"SequenceFlow_1mrrjf2\" sourceRef=\"ServiceTask_05g1ud3\" targetRef=\"EndEvent_0e7ewom\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1anlp0x\"\u003e\u003ctext\u003eoutput retained in\u00a0execution_details workflow property\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0azemtl\" sourceRef=\"ServiceTask_0tf99yv\" targetRef=\"TextAnnotation_1anlp0x\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0qx8vh7\"\u003e\u003ctext\u003ecreate an incident result based on the step function results\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1smv5cr\" sourceRef=\"ServiceTask_05g1ud3\" targetRef=\"TextAnnotation_0qx8vh7\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0tf99yv\" id=\"ServiceTask_0tf99yv_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"277\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_05g1ud3\" id=\"ServiceTask_05g1ud3_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"480\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0e7ewom\" id=\"EndEvent_0e7ewom_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"675\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"693\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0d1cpx9\" id=\"SequenceFlow_0d1cpx9_di\"\u003e\u003comgdi:waypoint x=\"198\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"277\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"237.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1ay969o\" id=\"SequenceFlow_1ay969o_di\"\u003e\u003comgdi:waypoint x=\"377\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"480\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"428.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1mrrjf2\" id=\"SequenceFlow_1mrrjf2_di\"\u003e\u003comgdi:waypoint x=\"580\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"675\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"627.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1anlp0x\" id=\"TextAnnotation_1anlp0x_di\"\u003e\u003comgdc:Bounds height=\"64\" width=\"187\" x=\"356\" y=\"67\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0azemtl\" id=\"Association_0azemtl_di\"\u003e\u003comgdi:waypoint x=\"370\" y=\"169\"/\u003e\u003comgdi:waypoint x=\"413\" y=\"131\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0qx8vh7\" id=\"TextAnnotation_0qx8vh7_di\"\u003e\u003comgdc:Bounds height=\"51\" width=\"193\" x=\"584\" y=\"71\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1smv5cr\" id=\"Association_1smv5cr_di\"\u003e\u003comgdi:waypoint x=\"576\" y=\"172\"/\u003e\u003comgdi:waypoint x=\"646\" y=\"122\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 4,
      "description": "Invokes a step function asynchronously using a simple demonstration function",
      "export_key": "example_invoke_step_function_asynchronous",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1736345384612,
      "name": "Example: Invoke AWS Step Function: Asynchronous",
      "object_type": "incident",
      "programmatic_name": "example_invoke_step_function_asynchronous",
      "tags": [],
      "uuid": "bedb444c-f846-476a-8f9c-c8f197f90dc6",
      "workflow_id": 117
    }
  ],
  "workspaces": []
}
