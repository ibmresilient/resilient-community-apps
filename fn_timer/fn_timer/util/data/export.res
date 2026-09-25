{
  "action_order": [],
  "actions": [
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Timer Epoch",
      "id": 1058,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Timer Epoch",
      "object_type": "incident",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "a2b8d997-2643-4b1e-98ce-4c06b05d40b8",
      "view_items": [
        {
          "content": "4c094a26-96e6-4913-a1d7-2d3327553ce8",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "timer_epoch"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Timer in Parallel",
      "id": 1059,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Timer in Parallel",
      "object_type": "incident",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "4a2ff0d1-65e2-47a8-bfde-b64dcecf6382",
      "view_items": [
        {
          "content": "4e61d8a0-0b90-49fc-81dc-e638860f532c",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "timer_in_parallel"
      ]
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "case_matching_profiles": [],
  "export_date": 1756975166460,
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
      "export_key": "__function/timer_time",
      "hide_notification": false,
      "id": 6328,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "timer_time",
      "operation_perms": {},
      "operations": [],
      "placeholder": "60s",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "timer_time",
      "tooltip": "Specify time to wait as a string value/units where units is \u0027s\u0027 for seconds, \u0027m\u0027 for minutes \u0027h\u0027 for hours and \u0027d\u0027 for days. For example: 60 seconds : \"60s\"; 45 minutes : \"45m\"; 12 hours : 12h",
      "type_id": 11,
      "uuid": "9c38bafe-6b62-4cc8-b4d6-6f79bbea78cb",
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
      "export_key": "__function/timer_epoch",
      "hide_notification": false,
      "id": 6329,
      "input_type": "datetimepicker",
      "internal": false,
      "is_tracked": false,
      "name": "timer_epoch",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "timer_epoch",
      "tooltip": "Epoch specifying the time the timer should end",
      "type_id": 11,
      "uuid": "fd6dc5d1-ff78-492b-92a9-d1d4cce15e54",
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
      "export_key": "actioninvocation/timer_end_time",
      "hide_notification": false,
      "id": 6326,
      "input_type": "datetimepicker",
      "internal": false,
      "is_tracked": false,
      "name": "timer_end_time",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Timer end time",
      "tooltip": "",
      "type_id": 6,
      "uuid": "4c094a26-96e6-4913-a1d7-2d3327553ce8",
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
      "export_key": "actioninvocation/timer_parallel_timers",
      "hide_notification": false,
      "id": 6327,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "timer_parallel_timers",
      "operation_perms": {},
      "operations": [],
      "placeholder": "1m,15s",
      "prefix": "properties",
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "timer parallel timers",
      "tooltip": "A comma separated list containing time to pause for each of 2 Timer instances. Timer string is \"time value\" concatenated with \"time unit\" character: \u2018s\u2019 for seconds; \u2018m\u2019 for minutes; \u2018h\u2019 for hours; \u2018d\u2019 for days",
      "type_id": 6,
      "uuid": "4e61d8a0-0b90-49fc-81dc-e638860f532c",
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
      "created_date": 1756724030213,
      "description": {
        "content": "This function implements a timer (sleep) function that when called from a workflow will cause the workflow to pause for the specified amount of time. The function takes one of two parameters as input: `timer_time` or `timer_epoch`.",
        "format": "text"
      },
      "destination_handle": "fn_timer",
      "display_name": "Timer",
      "export_key": "fn_timer",
      "id": 734,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 39,
        "name": "shresh@example.com",
        "type": "user"
      },
      "last_modified_time": 1756724030213,
      "name": "fn_timer",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "output_json_example": "{\"version\": 2.0, \"success\": true, \"reason\": null, \"content\": {\"Workflow Status\": {\"instance_id\": 1407, \"status\": \"terminated\", \"start_date\": 1661960193764, \"end_date\": 1661960247501, \"reason\": \"The workflow was manually terminated by a user.\", \"is_terminated\": true}}, \"raw\": null, \"inputs\": {\"timer_epoch\": 1661986800000}, \"metrics\": {\"version\": \"1.0\", \"package\": \"fn-timer\", \"package_version\": \"1.0.0\", \"host\": \"My Host\", \"execution_time_ms\": 177, \"timestamp\": \"2022-08-31 11:37:41\"}}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"version\": {\"type\": \"number\"}, \"success\": {\"type\": \"boolean\"}, \"reason\": {}, \"content\": {\"type\": \"object\", \"properties\": {\"Workflow Status\": {\"type\": \"object\", \"properties\": {\"instance_id\": {\"type\": \"integer\"}, \"status\": {\"type\": \"string\"}, \"start_date\": {\"type\": \"integer\"}, \"end_date\": {\"type\": \"integer\"}, \"reason\": {\"type\": \"string\"}, \"is_terminated\": {\"type\": \"boolean\"}}}}}, \"raw\": {}, \"inputs\": {\"type\": \"object\", \"properties\": {\"timer_epoch\": {\"type\": \"integer\"}}}, \"metrics\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}, \"package\": {\"type\": \"string\"}, \"package_version\": {\"type\": \"string\"}, \"host\": {\"type\": \"string\"}, \"execution_time_ms\": {\"type\": \"integer\"}, \"timestamp\": {\"type\": \"string\"}}}}}",
      "tags": [],
      "uuid": "fcdddb32-a1c3-4b61-8181-a9b478b07e84",
      "version": 0,
      "view_items": [
        {
          "content": "9c38bafe-6b62-4cc8-b4d6-6f79bbea78cb",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "fd6dc5d1-ff78-492b-92a9-d1d4cce15e54",
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
          "name": "Timer in Parallel",
          "object_type": "incident",
          "programmatic_name": "timer_in_parallel",
          "tags": [],
          "uuid": null,
          "workflow_id": 1060
        },
        {
          "actions": [],
          "description": null,
          "name": "Timer: Epoch",
          "object_type": "incident",
          "programmatic_name": "timer_epoch",
          "tags": [],
          "uuid": null,
          "workflow_id": 1059
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 331,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1756975162513,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1756975162513,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [
        "a3f0ef4d-02c3-4ed7-8887-5e78e15bf492"
      ],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "fn_timer",
      "name": "fn_timer",
      "programmatic_name": "fn_timer",
      "tags": [],
      "users": [
        "shresh@example.com"
      ],
      "uuid": "1ccdbaa5-3b89-4ecf-a54c-41d233df16c8"
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
        "version": 1,
        "workflow_id": "timer_in_parallel",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"timer_in_parallel\" isExecutable=\"true\" name=\"Timer in Parallel\"\u003e\u003cdocumentation\u003eThis example workflow shows how to use the Timer function to pause a workflow.  The Timer function is called twice in parallel.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_12trcua\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_10oqtla\" name=\"Timer\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"fcdddb32-a1c3-4b61-8181-a9b478b07e84\"\u003e{\"inputs\":{\"9c38bafe-6b62-4cc8-b4d6-6f79bbea78cb\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"30s\"}}},\"pre_processing_script\":\"# Get the timer values from the rule properties custom field\\nlist_time_values = rule.properties.timer_parallel_timers\\n\\n# Get the list of 2 timer values\\ntime_list = list_time_values.split(\u0027,\u0027)\\n\\n# Use the first timer for this function\\ninputs.timer_time = time_list[0]\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1yqbzjb\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_03oygc7\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cserviceTask id=\"ServiceTask_0k8ot4y\" name=\"Timer\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"fcdddb32-a1c3-4b61-8181-a9b478b07e84\"\u003e{\"inputs\":{\"9c38bafe-6b62-4cc8-b4d6-6f79bbea78cb\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"1m\"}}},\"pre_processing_script\":\"# Get the timer values from the rule properties custom field\\nlist_time_values = rule.properties.timer_parallel_timers\\n\\n# Get the list of 2 timer values\\ntime_list = list_time_values.split(\u0027,\u0027)\\n\\n# Use the second timer for this function\\ninputs.timer_time = time_list[1]\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0v96son\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0atuif7\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cparallelGateway id=\"ParallelGateway_1beu572\"\u003e\u003cincoming\u003eSequenceFlow_12trcua\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1yqbzjb\u003c/outgoing\u003e\u003coutgoing\u003eSequenceFlow_0v96son\u003c/outgoing\u003e\u003c/parallelGateway\u003e\u003cparallelGateway id=\"ParallelGateway_0dzwucu\"\u003e\u003cincoming\u003eSequenceFlow_03oygc7\u003c/incoming\u003e\u003cincoming\u003eSequenceFlow_0atuif7\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_09ocy2b\u003c/outgoing\u003e\u003c/parallelGateway\u003e\u003cendEvent id=\"EndEvent_192ok7f\"\u003e\u003cincoming\u003eSequenceFlow_09ocy2b\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_12trcua\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ParallelGateway_1beu572\"/\u003e\u003csequenceFlow id=\"SequenceFlow_1yqbzjb\" sourceRef=\"ParallelGateway_1beu572\" targetRef=\"ServiceTask_10oqtla\"/\u003e\u003csequenceFlow id=\"SequenceFlow_03oygc7\" sourceRef=\"ServiceTask_10oqtla\" targetRef=\"ParallelGateway_0dzwucu\"/\u003e\u003csequenceFlow id=\"SequenceFlow_0v96son\" sourceRef=\"ParallelGateway_1beu572\" targetRef=\"ServiceTask_0k8ot4y\"/\u003e\u003csequenceFlow id=\"SequenceFlow_0atuif7\" sourceRef=\"ServiceTask_0k8ot4y\" targetRef=\"ParallelGateway_0dzwucu\"/\u003e\u003csequenceFlow id=\"SequenceFlow_09ocy2b\" sourceRef=\"ParallelGateway_0dzwucu\" targetRef=\"EndEvent_192ok7f\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_10oqtla\" id=\"ServiceTask_10oqtla_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"355.8342036553525\" y=\"91.47258485639688\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0k8ot4y\" id=\"ServiceTask_0k8ot4y_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"356\" y=\"229\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ParallelGateway_1beu572\" id=\"ParallelGateway_1beu572_di\"\u003e\u003comgdc:Bounds height=\"50\" width=\"50\" x=\"249.8342036553525\" y=\"181\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"274.8342036553525\" y=\"234\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ParallelGateway_0dzwucu\" id=\"ParallelGateway_0dzwucu_di\"\u003e\u003comgdc:Bounds height=\"50\" width=\"50\" x=\"499.83420365535244\" y=\"181.47258485639688\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"524.8342036553524\" y=\"234.47258485639688\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_192ok7f\" id=\"EndEvent_192ok7f_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"613.8342036553524\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"631.8342036553524\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_12trcua\" id=\"SequenceFlow_12trcua_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"250\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"224\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1yqbzjb\" id=\"SequenceFlow_1yqbzjb_di\"\u003e\u003comgdi:waypoint x=\"275\" xsi:type=\"omgdc:Point\" y=\"181\"/\u003e\u003comgdi:waypoint x=\"275\" xsi:type=\"omgdc:Point\" y=\"131\"/\u003e\u003comgdi:waypoint x=\"356\" xsi:type=\"omgdc:Point\" y=\"131\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"290\" y=\"149.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_03oygc7\" id=\"SequenceFlow_03oygc7_di\"\u003e\u003comgdi:waypoint x=\"456\" xsi:type=\"omgdc:Point\" y=\"131\"/\u003e\u003comgdi:waypoint x=\"525\" xsi:type=\"omgdc:Point\" y=\"131\"/\u003e\u003comgdi:waypoint x=\"525\" xsi:type=\"omgdc:Point\" y=\"182\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"490.5\" y=\"109.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0v96son\" id=\"SequenceFlow_0v96son_di\"\u003e\u003comgdi:waypoint x=\"275\" xsi:type=\"omgdc:Point\" y=\"231\"/\u003e\u003comgdi:waypoint x=\"275\" xsi:type=\"omgdc:Point\" y=\"269\"/\u003e\u003comgdi:waypoint x=\"356\" xsi:type=\"omgdc:Point\" y=\"269\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"290\" y=\"243.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0atuif7\" id=\"SequenceFlow_0atuif7_di\"\u003e\u003comgdi:waypoint x=\"456\" xsi:type=\"omgdc:Point\" y=\"269\"/\u003e\u003comgdi:waypoint x=\"525\" xsi:type=\"omgdc:Point\" y=\"269\"/\u003e\u003comgdi:waypoint x=\"525\" xsi:type=\"omgdc:Point\" y=\"231\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"490.5\" y=\"247.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_09ocy2b\" id=\"SequenceFlow_09ocy2b_di\"\u003e\u003comgdi:waypoint x=\"549\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"614\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"581.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "description": "This example workflow shows how to use the Timer function to pause a workflow.  The Timer function is called twice in parallel.",
      "export_key": "timer_in_parallel",
      "last_modified_by": "shresh@example.com",
      "last_modified_time": 1756724032298,
      "name": "Timer in Parallel",
      "object_type": "incident",
      "programmatic_name": "timer_in_parallel",
      "tags": [],
      "uuid": "d4cf7d5f-eb3f-45d1-9906-8f11fff2b019",
      "workflow_id": 1060
    },
    {
      "actions": [],
      "content": {
        "version": 1,
        "workflow_id": "timer_epoch",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"timer_epoch\" isExecutable=\"true\" name=\"Timer: Epoch\"\u003e\u003cdocumentation\u003eThis example workflow demonstrates how to call the Timer function using an epoch time as input to define when the timer should end.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1t7ju9c\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cendEvent id=\"EndEvent_11440rv\"\u003e\u003cincoming\u003eSequenceFlow_1a01qey\u003c/incoming\u003e\u003c/endEvent\u003e\u003cserviceTask id=\"ServiceTask_0iplpae\" name=\"Timer\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"fcdddb32-a1c3-4b61-8181-a9b478b07e84\"\u003e{\"inputs\":{},\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"# Get the input date/time for timer end from the rule activity field\\ninputs.timer_epoch = rule.properties.timer_end_time\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1t7ju9c\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1a01qey\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1t7ju9c\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0iplpae\"/\u003e\u003csequenceFlow id=\"SequenceFlow_1a01qey\" sourceRef=\"ServiceTask_0iplpae\" targetRef=\"EndEvent_11440rv\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0xb2sfg\"\u003e\u003ctext\u003e\u003c![CDATA[Input: utilities_time string indicating how long function should sleep\n\u00a0or utilities_epoch with end timer epoch]]\u003e\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_129lh9h\" sourceRef=\"ServiceTask_0iplpae\" targetRef=\"TextAnnotation_0xb2sfg\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_11440rv\" id=\"EndEvent_11440rv_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"653\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"671\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0iplpae\" id=\"ServiceTask_0iplpae_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"368\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0xb2sfg\" id=\"TextAnnotation_0xb2sfg_di\"\u003e\u003comgdc:Bounds height=\"86\" width=\"150\" x=\"191\" y=\"57\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_129lh9h\" id=\"Association_129lh9h_di\"\u003e\u003comgdi:waypoint x=\"371\" xsi:type=\"omgdc:Point\" y=\"173\"/\u003e\u003comgdi:waypoint x=\"328\" xsi:type=\"omgdc:Point\" y=\"143\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1t7ju9c\" id=\"SequenceFlow_1t7ju9c_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"368\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"283\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1a01qey\" id=\"SequenceFlow_1a01qey_di\"\u003e\u003comgdi:waypoint x=\"468\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"653\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"560.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 1,
      "description": "This example workflow demonstrates how to call the Timer function using an epoch time as input to define when the timer should end.",
      "export_key": "timer_epoch",
      "last_modified_by": "shresh@example.com",
      "last_modified_time": 1756724031639,
      "name": "Timer: Epoch",
      "object_type": "incident",
      "programmatic_name": "timer_epoch",
      "tags": [],
      "uuid": "31b687fc-9084-4d5f-b68b-26398b5d09d9",
      "workflow_id": 1059
    }
  ],
  "workspaces": []
}
