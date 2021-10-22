{
  "action_order": [],
  "actions": [
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "SentinelOne: Get Agents",
      "id": 14,
      "logic_type": "all",
      "message_destinations": [],
      "name": "SentinelOne: Get Agents",
      "object_type": "incident",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "b0f441e9-af7d-42df-8a3d-9864b27e8f53",
      "view_items": [],
      "workflows": [
        "sentinelone_get_agents"
      ]
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "export_date": 1634941709439,
  "export_format_version": 2,
  "fields": [
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
      "created_date": 1634937335004,
      "creator": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "description": {
        "content": null,
        "format": "text"
      },
      "destination_handle": "fn_sentinelone",
      "display_name": "SenitinelOne: Get Agents",
      "export_key": "senitinelone_get_agents",
      "id": 1,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1634937335080,
      "name": "senitinelone_get_agents",
      "tags": [],
      "uuid": "efbfb628-1bfb-4ec3-a7c1-7acfeb079246",
      "version": 1,
      "view_items": [],
      "workflows": [
        {
          "actions": [],
          "description": null,
          "name": "SentinelOne: Get Agents",
          "object_type": "incident",
          "programmatic_name": "sentinelone_get_agents",
          "tags": [],
          "uuid": null,
          "workflow_id": 1
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 2,
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1634941707720,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1634941707720,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "industries": null,
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "fn_sentinelone",
      "name": "fn_sentinelone",
      "programmatic_name": "fn_sentinelone",
      "tags": [],
      "users": [
        "admin@example.com"
      ],
      "uuid": "8864c644-67aa-4bd4-a7d3-6e5896b469db"
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
        "version": 1,
        "workflow_id": "sentinelone_get_agents",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"sentinelone_get_agents\" isExecutable=\"true\" name=\"SentinelOne: Get Agents\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0zu1d90\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_022e7nj\" name=\"SenitinelOne: Get Agents\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"efbfb628-1bfb-4ec3-a7c1-7acfeb079246\"\u003e{\"inputs\":{}}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0zu1d90\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1nmzvb4\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0zu1d90\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_022e7nj\"/\u003e\u003cendEvent id=\"EndEvent_1sq3bx9\"\u003e\u003cincoming\u003eSequenceFlow_1nmzvb4\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1nmzvb4\" sourceRef=\"ServiceTask_022e7nj\" targetRef=\"EndEvent_1sq3bx9\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_022e7nj\" id=\"ServiceTask_022e7nj_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"454.33487297921477\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0zu1d90\" id=\"SequenceFlow_0zu1d90_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"454\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"326\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1sq3bx9\" id=\"EndEvent_1sq3bx9_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"810.2401847575057\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"828.2401847575057\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1nmzvb4\" id=\"SequenceFlow_1nmzvb4_di\"\u003e\u003comgdi:waypoint x=\"554\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"810\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"682\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "creator_id": "admin@example.com",
      "description": "",
      "export_key": "sentinelone_get_agents",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1634937437987,
      "name": "SentinelOne: Get Agents",
      "object_type": "incident",
      "programmatic_name": "sentinelone_get_agents",
      "tags": [],
      "uuid": "c279ab29-8782-452c-8fe4-6e5e324cf2ca",
      "workflow_id": 1
    }
  ],
  "workspaces": []
}
