{
  "action_order": [],
  "actions": [
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: Call gRPC Service",
      "id": 15,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Call gRPC Service",
      "object_type": "artifact",
      "tags": [
        {
          "tag_handle": "fn_grpc_interface",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "fb59372d-1700-4d3b-b019-0c654f0f17db",
      "view_items": [],
      "workflows": [
        "example_grpc_communication_interface"
      ]
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "export_date": 1631567559793,
  "export_format_version": 2,
  "fields": [
    {
      "allow_default_value": false,
      "blank_option": false,
      "calculated": false,
      "changeable": true,
      "chosen": false,
      "default_chosen_by_server": false,
      "deprecated": false,
      "export_key": "__function/grpc_function_data",
      "hide_notification": false,
      "id": 232,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "grpc_function_data",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_grpc_interface",
          "value": null
        }
      ],
      "templates": [],
      "text": "grpc_function_data",
      "tooltip": "Additional data Fields to send data from client to server. data format will be in json and key should match the request function parameter.",
      "type_id": 11,
      "uuid": "9ddddf62-60f7-450a-a9ac-2fdb85e3c4a3",
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
      "export_key": "__function/grpc_function",
      "hide_notification": false,
      "id": 233,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "grpc_function",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_grpc_interface",
          "value": null
        }
      ],
      "templates": [],
      "text": "grpc_function",
      "tooltip": "This fields contains data from .proto file i.e package_name : rpc function name(grpc request function) ex: helloword : SayHello(HelloRequest)",
      "type_id": 11,
      "uuid": "d09878dc-d11f-4e2e-b112-d53e5882e25f",
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
      "export_key": "__function/grpc_channel",
      "hide_notification": false,
      "id": 231,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "grpc_channel",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_grpc_interface",
          "value": null
        }
      ],
      "templates": [],
      "text": "grpc_channel",
      "tooltip": "this field contain the channel info of the GRPC Server Running ex:hostIP:Port",
      "type_id": 11,
      "uuid": "33bf7c41-1f45-4d2c-b915-911453db1d5e",
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
      "apps": [],
      "created_date": 1631564266118,
      "creator": {
        "display_name": "Local Integration Server",
        "id": 4,
        "name": "ad261c1f-f1cc-4115-bbce-a151f88bac5e",
        "type": "apikey"
      },
      "description": {
        "content": "Function that allows you to call a gRPC Service that is being served on your Integrations Server",
        "format": "text"
      },
      "destination_handle": "fn_grpc",
      "display_name": "GRPC",
      "export_key": "function_grpc",
      "id": 2,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1631566159939,
      "name": "function_grpc",
      "tags": [
        {
          "tag_handle": "fn_grpc_interface",
          "value": null
        }
      ],
      "uuid": "0f969608-f22f-4a6b-a743-af01a21d693c",
      "version": 2,
      "view_items": [
        {
          "content": "33bf7c41-1f45-4d2c-b915-911453db1d5e",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "d09878dc-d11f-4e2e-b112-d53e5882e25f",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "9ddddf62-60f7-450a-a9ac-2fdb85e3c4a3",
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
          "name": "Example: GRPC Communication Interface",
          "object_type": "artifact",
          "programmatic_name": "example_grpc_communication_interface",
          "tags": [
            {
              "tag_handle": "fn_grpc_interface",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 2
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 5,
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1631567558117,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1631567558117,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "industries": null,
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [
        "098b02d7-3907-4791-bacc-7a6d4e85e66c",
        "ad261c1f-f1cc-4115-bbce-a151f88bac5e"
      ],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "fn_grpc",
      "name": "fn_grpc",
      "programmatic_name": "fn_grpc",
      "tags": [
        {
          "tag_handle": "fn_grpc_interface",
          "value": null
        }
      ],
      "users": [],
      "uuid": "b087f33a-21c7-4a9c-b605-02c719976392"
    }
  ],
  "notifications": null,
  "overrides": [],
  "phases": [],
  "regulators": null,
  "roles": [],
  "scripts": [],
  "server_version": {
    "build_number": 6554,
    "major": 40,
    "minor": 0,
    "version": "40.0.6554"
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
        "workflow_id": "example_grpc_communication_interface",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_grpc_communication_interface\" isExecutable=\"true\" name=\"Example: GRPC Communication Interface\"\u003e\u003cdocumentation\u003eAn example workflow how showing to call a gRPC Service from an IBM Resilient Workflow\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_14kskfm\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1nfcftf\" name=\"GRPC\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"0f969608-f22f-4a6b-a743-af01a21d693c\"\u003e{\"inputs\":{},\"post_processing_script\":\"\\ngrpc_response_data = results[\u0027content\u0027]\\ngrpc_channel = results[\u0027channel\u0027]\\n\\nrich_text = helper.createRichText(u\\\"\\\"\\\"A gRPC Response has been received from \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;\u0026lt;br\u0026gt;\\n                                      \u0026lt;b\u0026gt;Response:\u0026lt;/b\u0026gt; {1}\\\"\\\"\\\".format(grpc_channel, grpc_response_data))\\n\\nincident.addNote(rich_text)\",\"pre_processing_script\":\"def dict_to_json_str(d):\\n  \\\"\\\"\\\"Function that converts a dictionary into a JSON string.\\n     Supports types: basestring, unicode, bool, int and nested dicts.\\n     Does not support lists.\\n     If the value is None, it sets it to False.\\\"\\\"\\\"\\n\\n  json_entry = u\u0027\\\"{0}\\\":{1}\u0027\\n  json_entry_str = u\u0027\\\"{0}\\\":\\\"{1}\\\"\u0027\\n  entries = []\\n\\n  for entry in d:\\n    key = entry\\n    value = d[entry]\\n\\n    if value is None:\\n      value = False\\n\\n    if isinstance(value, list):\\n      helper.fail(\u0027dict_to_json_str does not support Python Lists\u0027)\\n\\n    if isinstance(value, basestring):\\n      value = value.replace(u\u0027\\\"\u0027, u\u0027\\\\\\\\\\\"\u0027)\\n      entries.append(json_entry_str.format(unicode(key), unicode(value)))\\n\\n    elif isinstance(value, unicode):\\n      entries.append(json_entry.format(unicode(key), unicode(value)))\\n    \\n    elif isinstance(value, bool):\\n      value = \u0027true\u0027 if value == True else \u0027false\u0027\\n      entries.append(json_entry.format(key, value))\\n\\n    elif isinstance(value, int):\\n      entries.append(json_entry.format(unicode(key), value))\\n\\n    elif isinstance(value, dict):\\n      entries.append(json_entry.format(key, dict_to_json_str(value)))\\n\\n    else:\\n      helper.fail(\u0027dict_to_json_str does not support this type: {0}\u0027.format(type(value)))\\n\\n  return u\u0027{0} {1} {2}\u0027.format(u\u0027{\u0027, \u0027,\u0027.join(entries), u\u0027}\u0027)\\n\\n# Define Inputs assuming grpc_channel is defined in app.config\\n\\n# The gRPC Function to call\\ninputs.grpc_function = \\\"helloworld:SayHello(HelloRequest)\\\"\\n\\n# The gRPC Function Request Data\\ninputs.grpc_function_data = dict_to_json_str({\\\"name\\\": artifact.value})\",\"pre_processing_script_language\":\"python\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_14kskfm\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0tuv6tz\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_14kskfm\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1nfcftf\"/\u003e\u003cendEvent id=\"EndEvent_1ukhvxp\"\u003e\u003cincoming\u003eSequenceFlow_0tuv6tz\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0tuv6tz\" sourceRef=\"ServiceTask_1nfcftf\" targetRef=\"EndEvent_1ukhvxp\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_06mmee6\"\u003e\u003ctext\u003e\u003c![CDATA[A general purpose wrapper to call a gRPC Service\n]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_05xcd6a\" sourceRef=\"ServiceTask_1nfcftf\" targetRef=\"TextAnnotation_06mmee6\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"185\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"180\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1nfcftf\" id=\"ServiceTask_1nfcftf_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"331\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_14kskfm\" id=\"SequenceFlow_14kskfm_di\"\u003e\u003comgdi:waypoint x=\"221\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"331\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"12\" width=\"90\" x=\"231\" y=\"185\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1ukhvxp\" id=\"EndEvent_1ukhvxp_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"531\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"12\" width=\"90\" x=\"504\" y=\"228\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0tuv6tz\" id=\"SequenceFlow_0tuv6tz_di\"\u003e\u003comgdi:waypoint x=\"431\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"531\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"12\" width=\"90\" x=\"436\" y=\"185\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_06mmee6\" id=\"TextAnnotation_06mmee6_di\"\u003e\u003comgdc:Bounds height=\"54\" width=\"173\" x=\"462\" y=\"82\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_05xcd6a\" id=\"Association_05xcd6a_di\"\u003e\u003comgdi:waypoint x=\"431\" xsi:type=\"omgdc:Point\" y=\"177\"/\u003e\u003comgdi:waypoint x=\"503\" xsi:type=\"omgdc:Point\" y=\"136\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 3,
      "creator_id": "ad261c1f-f1cc-4115-bbce-a151f88bac5e",
      "description": "An example workflow how showing to call a gRPC Service from an IBM Resilient Workflow",
      "export_key": "example_grpc_communication_interface",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1631566160246,
      "name": "Example: GRPC Communication Interface",
      "object_type": "artifact",
      "programmatic_name": "example_grpc_communication_interface",
      "tags": [
        {
          "tag_handle": "fn_grpc_interface",
          "value": null
        }
      ],
      "uuid": "b765e312-554f-43e8-9d6b-37e48d044765",
      "workflow_id": 2
    }
  ],
  "workspaces": []
}
