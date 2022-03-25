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
            "Malware MD5 Hash",
            "Malware SHA-1 Hash"
          ]
        }
      ],
      "enabled": true,
      "export_key": "ShadowServer Hash Query",
      "id": 20,
      "logic_type": "all",
      "message_destinations": [],
      "name": "ShadowServer Hash Query",
      "object_type": "artifact",
      "tags": [
        {
          "tag_handle": "fn_shadowserver",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 0,
      "uuid": "650926ec-af3d-411a-9e5b-e8782cc4947a",
      "view_items": [],
      "workflows": [
        "shadowserver_hash_query"
      ]
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "export_date": 1648236857331,
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
      "export_key": "__function/shadowserver_artifact_type",
      "hide_notification": false,
      "id": 283,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "shadowserver_artifact_type",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_shadowserver",
          "value": null
        }
      ],
      "templates": [],
      "text": "shadowserver_artifact_type",
      "tooltip": "",
      "type_id": 11,
      "uuid": "0c28525f-f229-4a83-ab35-bd40d897ca06",
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
      "export_key": "__function/shadowserver_artifact_value",
      "hide_notification": false,
      "id": 284,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "shadowserver_artifact_value",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_shadowserver",
          "value": null
        }
      ],
      "templates": [],
      "text": "shadowserver_artifact_value",
      "tooltip": "",
      "type_id": 11,
      "uuid": "66bc575f-6a76-4564-9a0f-53e349c7fae4",
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
      "created_date": 1647546922392,
      "creator": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "description": {
        "content": "Queries ShadowServer to check if the hash provided matches an entry in the ShadowServer database. Returns details on the data source if there is a match.",
        "format": "text"
      },
      "destination_handle": "shadowserver",
      "display_name": "ShadowServer",
      "export_key": "fn_shadowserver",
      "id": 8,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1648232943767,
      "name": "fn_shadowserver",
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {\"application_type\": \"Graphic/Drawing\", \"mfg_name\": \"Corel Corporation\", \"os_mfg\": \"Microsoft\", \"filename\": \"00br2026.gif\", \"md5\": \"0E53C14A3E48D94FF596A2824307B492\", \"os_name\": \"Windows NT\", \"sha1\": \"0000004DA6391F7F5D2F7FCCF36CEBDA60C6EA02\", \"filesize\": \"2226\", \"os_version\": \"Generic\", \"product_name\": \"Gallery\", \"crc32\": \"AA6A7B16\", \"product_version\": \"750,000\", \"source_version\": \"$version\", \"source\": \"NIST\", \"language\": \"English\"}, \"raw\": null, \"inputs\": {\"shadowserver_artifact_type\": \"Malware MD5 Hash\", \"shadowserver_artifact_value\": \"0E53C14A3E48D94FF596A2824307B492\"}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-shadowserver\", \"package_version\": \"1.0.0\", \"host\": \"My Host\", \"execution_time_ms\": 210, \"timestamp\": \"2022-03-23 16:37:34\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"application_type\": {\"type\": \"string\"}, \"mfg_name\": {\"type\": \"string\"}, \"os_mfg\": {\"type\": \"string\"}, \"filename\": {\"type\": \"string\"}, \"md5\": {\"type\": \"string\"}, \"os_name\": {\"type\": \"string\"}, \"sha1\": {\"type\": \"string\"}, \"filesize\": {\"type\": \"string\"}, \"os_version\": {\"type\": \"string\"}, \"product_name\": {\"type\": \"string\"}, \"crc32\": {\"type\": \"string\"}, \"product_version\": {\"type\": \"string\"}, \"source_version\": {\"type\": \"string\"}, \"source\": {\"type\": \"string\"}, \"language\": {\"type\": \"string\"}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"shadowserver_artifact_type\": {\"type\": \"string\"}, \"shadowserver_artifact_value\": {\"type\": \"string\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [
        {
          "tag_handle": "fn_shadowserver",
          "value": null
        }
      ],
      "uuid": "abe5446a-2db6-4a02-aaa0-73777d5754a1",
      "version": 5,
      "view_items": [
        {
          "content": "0c28525f-f229-4a83-ab35-bd40d897ca06",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "66bc575f-6a76-4564-9a0f-53e349c7fae4",
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
          "name": "ShadowServer Hash Query",
          "object_type": "artifact",
          "programmatic_name": "shadowserver_hash_query",
          "tags": [
            {
              "tag_handle": "fn_shadowserver",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 12
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 68,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1648236855237,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1648236855237,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "industries": null,
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [
        "0228e00e-2c47-43e6-a736-550f104c94ea",
        "ba28e56f-5e89-44ec-8fdd-5be0e93f119c"
      ],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "shadowserver",
      "name": "ShadowServer",
      "programmatic_name": "shadowserver",
      "tags": [
        {
          "tag_handle": "fn_shadowserver",
          "value": null
        }
      ],
      "users": [],
      "uuid": "04db7b38-a2ef-476b-a8f2-9b894238f590"
    }
  ],
  "notifications": null,
  "overrides": [],
  "phases": [],
  "playbooks": null,
  "regulators": null,
  "roles": [],
  "scripts": [],
  "server_version": {
    "build_number": 49,
    "major": 43,
    "minor": 1,
    "version": "43.1.49"
  },
  "tags": [],
  "task_order": [],
  "timeframes": null,
  "types": [],
  "workflows": [
    {
      "actions": [],
      "content": {
        "version": 11,
        "workflow_id": "shadowserver_hash_query",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"shadowserver_hash_query\" isExecutable=\"true\" name=\"ShadowServer Hash Query\"\u003e\u003cdocumentation\u003eQueries ShadowServer to check if the hash provided matches an entry in the ShadowServer database. Returns details on the data source if there is a match which is turned into a hit in the post-processing script.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1jn45go\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cendEvent id=\"EndEvent_0hf0qjm\"\u003e\u003cincoming\u003eSequenceFlow_0b9lq90\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1jn45go\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1qc77kp\"/\u003e\u003cserviceTask id=\"ServiceTask_1qc77kp\" name=\"ShadowServer\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"abe5446a-2db6-4a02-aaa0-73777d5754a1\"\u003e{\"inputs\":{},\"post_processing_script\":\"if results:\\n  if results.success:\\n    if results.content:\\n      resp = results.content\\n      hit_list = []\\n      for attribute, attribute_value in resp.items():\\n        hit = {\\n          \\\"name\\\": attribute,\\n          \\\"type\\\": \\\"string\\\",\\n          \\\"value\\\": \\\"{}\\\".format(attribute_value)\\n        }\\n        hit_list.append(hit)\\n      artifact.addHit(\\\"ShadowServer Function\\\", hit_list)\\n  else:\\n    incident.addNote(\\\"ShadowServer Hash check failed: {}\\\".format(results.reason))\\n    \",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.shadowserver_artifact_type = artifact.type\\ninputs.shadowserver_artifact_value = artifact.value\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1jn45go\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0b9lq90\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0b9lq90\" sourceRef=\"ServiceTask_1qc77kp\" targetRef=\"EndEvent_0hf0qjm\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0hf0qjm\" id=\"EndEvent_0hf0qjm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"490\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"508\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1jn45go\" id=\"SequenceFlow_1jn45go_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"292\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"245\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1qc77kp\" id=\"ServiceTask_1qc77kp_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"292\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0b9lq90\" id=\"SequenceFlow_0b9lq90_di\"\u003e\u003comgdi:waypoint x=\"392\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"490\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"441\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 11,
      "creator_id": "admin@example.com",
      "description": "Queries ShadowServer to check if the hash provided matches an entry in the ShadowServer database. Returns details on the data source if there is a match which is turned into a hit in the post-processing script.",
      "export_key": "shadowserver_hash_query",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1648236322922,
      "name": "ShadowServer Hash Query",
      "object_type": "artifact",
      "programmatic_name": "shadowserver_hash_query",
      "tags": [
        {
          "tag_handle": "fn_shadowserver",
          "value": null
        }
      ],
      "uuid": "cd8ab2eb-5ba8-43d2-bbc9-c7fd035dac76",
      "workflow_id": 12
    }
  ],
  "workspaces": []
}
