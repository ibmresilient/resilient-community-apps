{
  "action_order": [],
  "actions": [
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "artifact.type",
          "method": "equals",
          "type": null,
          "value": "String"
        }
      ],
      "enabled": true,
      "export_key": "Example: ElasticSearch Query from Artifact",
      "id": 45,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: ElasticSearch Query from Artifact",
      "object_type": "artifact",
      "tags": [
        {
          "tag_handle": "fn_elasticsearch",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "1d0d50e3-2bfc-45de-90ec-f2f44a7199f4",
      "view_items": [],
      "workflows": [
        "example_elasticsearch_query_from_artifact"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: ElasticSearch Query from Incident",
      "id": 46,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: ElasticSearch Query from Incident",
      "object_type": "incident",
      "tags": [
        {
          "tag_handle": "fn_elasticsearch",
          "value": null
        }
      ],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "5625226a-3919-4e16-966e-2d89fa21d217",
      "view_items": [],
      "workflows": [
        "example_elasticsearch_query_from_incident"
      ]
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "export_date": 1656347812073,
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
      "export_key": "__function/es_query",
      "hide_notification": false,
      "id": 331,
      "input_type": "textarea",
      "internal": false,
      "is_tracked": false,
      "name": "es_query",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_elasticsearch",
          "value": null
        }
      ],
      "templates": [
        {
          "id": 13,
          "name": "match_all",
          "template": {
            "content": "{\n    \"query\": {\n        \"match_all\": {}\n    }\n}",
            "format": "text"
          },
          "uuid": "2457c8d0-2b19-4756-9a1a-4e641069d239"
        },
        {
          "id": 14,
          "name": "match_term_sorted",
          "template": {
            "content": "{\n    \"sort\" : [\n        { \"\u003cSORT_VALUE\u003e\" : \"desc\" }\n    ],\n    \"query\" : {\n        \"term\" : \u003cTERM_TO_BE_SEARCHED\u003e\n    }\n}",
            "format": "text"
          },
          "uuid": "24a3191b-d1b3-41b1-99c0-1d2290ba36ed"
        },
        {
          "id": 15,
          "name": "match_term",
          "template": {
            "content": "{\n    \"query\" : {\n        \"term\" : {\u003cTERM_TO_BE_SEARCHED\u003e}\n    }\n}",
            "format": "text"
          },
          "uuid": "2c99d804-36b7-4da7-a8cb-afa024ed6b5d"
        }
      ],
      "text": "es_query",
      "tooltip": "The query that will be submitted to ElasticSearch",
      "type_id": 11,
      "uuid": "b92cc3ed-2878-4630-81a7-5830780fa5d9",
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
      "export_key": "__function/es_index",
      "hide_notification": false,
      "id": 332,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "es_index",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_elasticsearch",
          "value": null
        }
      ],
      "templates": [],
      "text": "es_index",
      "tooltip": "The index that will be searched for data. If left blank all indices will be searched.",
      "type_id": 11,
      "uuid": "eed55443-7d80-4451-b275-31f2e09c3a84",
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
      "export_key": "__function/es_doc_type",
      "hide_notification": false,
      "id": 330,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "es_doc_type",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [
        {
          "tag_handle": "fn_elasticsearch",
          "value": null
        }
      ],
      "templates": [],
      "text": "es_doc_type",
      "tooltip": "The document type that will be search.",
      "type_id": 11,
      "uuid": "1e041775-c9ba-43ae-a8cf-3f4dda9a0681",
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
      "created_date": 1656342284129,
      "description": {
        "content": "A function that allows a user to query a specified ElasticSearch datastore for data.",
        "format": "text"
      },
      "destination_handle": "fn_elasticsearch",
      "display_name": "ElasticSearch Utilities: Query",
      "export_key": "fn_elasticsearch_query",
      "id": 27,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1656342284154,
      "name": "fn_elasticsearch_query",
      "tags": [
        {
          "tag_handle": "fn_elasticsearch",
          "value": null
        }
      ],
      "uuid": "4f103490-595d-4ab9-ba30-8202c8ddfe9d",
      "version": 1,
      "view_items": [
        {
          "content": "b92cc3ed-2878-4630-81a7-5830780fa5d9",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "1e041775-c9ba-43ae-a8cf-3f4dda9a0681",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "eed55443-7d80-4451-b275-31f2e09c3a84",
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
          "name": "Example: ElasticSearch Query from Artifact",
          "object_type": "artifact",
          "programmatic_name": "example_elasticsearch_query_from_artifact",
          "tags": [
            {
              "tag_handle": "fn_elasticsearch",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 34
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: ElasticSearch Query from Incident",
          "object_type": "incident",
          "programmatic_name": "example_elasticsearch_query_from_incident",
          "tags": [
            {
              "tag_handle": "fn_elasticsearch",
              "value": null
            }
          ],
          "uuid": null,
          "workflow_id": 33
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 4,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1656581598145,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1656581598145,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "industries": null,
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [
        "2c45bf47-b432-4142-ad1c-cc54246a86bb"
      ],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "fn_elasticsearch",
      "name": "fn_elasticsearch",
      "programmatic_name": "fn_elasticsearch",
      "tags": [
        {
          "tag_handle": "fn_elasticsearch",
          "value": null
        }
      ],
      "users": [],
      "uuid": "28e2e8a2-ea65-430b-abc3-48d2bb3d60db"
    }
  ],
  "notifications": null,
  "overrides": [],
  "phases": [],
  "playbooks": [],
  "regulators": null,
  "roles": [],
  "scripts": [],
  "server_version": {
    "build_number": 0,
    "major": 43,
    "minor": 0,
    "version": "43.0.0"
  },
  "tags": [],
  "task_order": [],
  "timeframes": null,
  "types": [],
  "workflows": [
    {
      "actions": [],
      "content": {
        "version": 10,
        "workflow_id": "example_elasticsearch_query_from_artifact",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_elasticsearch_query_from_artifact\" isExecutable=\"true\" name=\"Example: ElasticSearch Query from Artifact\"\u003e\u003cdocumentation\u003e\u003c![CDATA[An example which attempts to query ElasticSearch using data gathered from an artifact. Intended to be used on an artifact of type \u0027String\u0027]]\u003e\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0aetsi3\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0e56r29\" name=\"ElasticSearch Utilities: Query\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"4f103490-595d-4ab9-ba30-8202c8ddfe9d\"\u003e{\"inputs\":{},\"post_processing_script\":\"\\\"\\\"\\\"\\n# An Example of the result object \\n    results = {\\n        \\\"inputs\\\": {\\n          \\\"es_query\\\": { \\\"query\\\": { \\\"match_all\\\": {} } },\\n          \\\"es_doc_type\\\": logs,\\n          \\\"es_index\\\" : my_logstore\\n        },\\n        \\\"query_results\\\": [\\n          \u0026lt;elasticsearch-record\u0026gt;,\\n        \\\"success\\\": True / False,\\n        \\\"matched_records\\\": 1000,\\n        \\\"returned_records\\\": 100\\n    }\\n    Note: The schema of elasticsearch-record; outlined above, will reflect the structure of your data in Elastic itself\\n\\\"\\\"\\\"\\n\\nif results.matched_records:\\n  noteText = \\\"\\\"\\\"\u0026lt;b\u0026gt;ElasticSearch Query status\u0026lt;/b\u0026gt;\\n                \u0026lt;br\u0026gt; Query supplied: \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;\\n                \u0026lt;br\u0026gt; Total matched records :\u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt;\\\"\\\"\\\".format(results.inputs[\\\"es_query\\\"], results.matched_records)\\n  \\n  if results.returned_records != 0:\\n    noteText += \\\"\\\"\\\"\u0026lt;br\u0026gt; Total returned records : \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;\\\"\\\"\\\".format(results.returned_records)\\n  incident.addNote(helper.createRichText(noteText))\",\"pre_processing_script\":\"if artifact.value is not None:\\n  inputs.es_query = artifact.value\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0aetsi3\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1yz77pw\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndEvent_0gizqrd\"\u003e\u003cincoming\u003eSequenceFlow_1yz77pw\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0aetsi3\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0e56r29\"/\u003e\u003csequenceFlow id=\"SequenceFlow_1yz77pw\" sourceRef=\"ServiceTask_0e56r29\" targetRef=\"EndEvent_0gizqrd\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_051atie\"\u003e\u003ctext\u003eTakes in an elasticsearch query and optionally, an index and doc_type to search against\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1ta8zaw\" sourceRef=\"ServiceTask_0e56r29\" targetRef=\"TextAnnotation_051atie\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_00jn6bc\"\u003e\u003ctext\u003eReturns result of query including how many matched and returned records. Saves query information in a rich text note\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0t6x92s\" sourceRef=\"ServiceTask_0e56r29\" targetRef=\"TextAnnotation_00jn6bc\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0e56r29\" id=\"ServiceTask_0e56r29_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"369\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0gizqrd\" id=\"EndEvent_0gizqrd_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"644\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"662\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0aetsi3\" id=\"SequenceFlow_0aetsi3_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"369\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"283.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1yz77pw\" id=\"SequenceFlow_1yz77pw_di\"\u003e\u003comgdi:waypoint x=\"469\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"644\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"556.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_051atie\" id=\"TextAnnotation_051atie_di\"\u003e\u003comgdc:Bounds height=\"96\" width=\"137\" x=\"209\" y=\"77\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1ta8zaw\" id=\"Association_1ta8zaw_di\"\u003e\u003comgdi:waypoint x=\"369\" xsi:type=\"omgdc:Point\" y=\"177\"/\u003e\u003comgdi:waypoint x=\"346\" xsi:type=\"omgdc:Point\" y=\"164\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_00jn6bc\" id=\"TextAnnotation_00jn6bc_di\"\u003e\u003comgdc:Bounds height=\"101\" width=\"129\" x=\"504\" y=\"80\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0t6x92s\" id=\"Association_0t6x92s_di\"\u003e\u003comgdi:waypoint x=\"469\" xsi:type=\"omgdc:Point\" y=\"181\"/\u003e\u003comgdi:waypoint x=\"504\" xsi:type=\"omgdc:Point\" y=\"163\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 10,
      "description": "An example which attempts to query ElasticSearch using data gathered from an artifact. Intended to be used on an artifact of type \u0027String\u0027",
      "export_key": "example_elasticsearch_query_from_artifact",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1656342284431,
      "name": "Example: ElasticSearch Query from Artifact",
      "object_type": "artifact",
      "programmatic_name": "example_elasticsearch_query_from_artifact",
      "tags": [
        {
          "tag_handle": "fn_elasticsearch",
          "value": null
        }
      ],
      "uuid": "29afd122-2e24-4516-b779-887c50962f5f",
      "workflow_id": 34
    },
    {
      "actions": [],
      "content": {
        "version": 7,
        "workflow_id": "example_elasticsearch_query_from_incident",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_elasticsearch_query_from_incident\" isExecutable=\"true\" name=\"Example: ElasticSearch Query from Incident\"\u003e\u003cdocumentation\u003eAn example which attempts to query ElasticSearch using a pre-defined query. Query examples are provided during workflow creation.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1e6h4md\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_128lxwv\" name=\"ElasticSearch Utilities: Query\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"4f103490-595d-4ab9-ba30-8202c8ddfe9d\"\u003e{\"inputs\":{\"b92cc3ed-2878-4630-81a7-5830780fa5d9\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_content_value\":{\"format\":\"text\",\"content\":\"{\\n    \\\"query\\\": {\\n        \\\"match_all\\\": {}\\n    }\\n}\"}}}},\"post_processing_script\":\"\\\"\\\"\\\"\\n# An Example of the result object \\n    results = {\\n        \\\"inputs\\\": {\\n          \\\"es_query\\\": { \\\"query\\\": { \\\"match_all\\\": {} } },\\n          \\\"es_doc_type\\\": logs,\\n          \\\"es_index\\\" : my_logstore\\n        },\\n        \\\"query_results\\\": [\\n          \u0026lt;elasticsearch-record\u0026gt;,\\n        \\\"success\\\": True / False,\\n        \\\"matched_records\\\": 1000,\\n        \\\"returned_records\\\": 100\\n    }\\n    Note: The schema of elasticsearch-record; outlined above, will reflect the structure of your data in Elastic itself\\n\\\"\\\"\\\"\\n\\nif results.matched_records:\\n  noteText = \\\"\\\"\\\"\u0026lt;b\u0026gt;ElasticSearch Query status\u0026lt;/b\u0026gt;\\n                \u0026lt;br\u0026gt; Query supplied: \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;\\n                \u0026lt;br\u0026gt; Total matched records :\u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt;\\\"\\\"\\\".format(results.inputs[\\\"es_query\\\"], results.matched_records)\\n  \\n  if results.returned_records != 0:\\n    noteText += \\\"\\\"\\\"\u0026lt;br\u0026gt; Total returned records : \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;\\\"\\\"\\\".format(results.returned_records)\\n  incident.addNote(helper.createRichText(noteText))\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1e6h4md\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_08bun20\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndEvent_0nz5r72\"\u003e\u003cincoming\u003eSequenceFlow_08bun20\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1e6h4md\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_128lxwv\"/\u003e\u003csequenceFlow id=\"SequenceFlow_08bun20\" sourceRef=\"ServiceTask_128lxwv\" targetRef=\"EndEvent_0nz5r72\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_17fmnol\"\u003e\u003ctext\u003eTakes in an elasticsearch query and optionally, an index and doc_type to search against\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_09238i3\" sourceRef=\"ServiceTask_128lxwv\" targetRef=\"TextAnnotation_17fmnol\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_000xz6j\"\u003e\u003ctext\u003eReturns result of query including how many matched and returned records. Saves query information in a rich text note\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0457y43\" sourceRef=\"ServiceTask_128lxwv\" targetRef=\"TextAnnotation_000xz6j\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_128lxwv\" id=\"ServiceTask_128lxwv_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"318.07775000000004\" y=\"165.54725000000002\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0nz5r72\" id=\"EndEvent_0nz5r72_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"568.0567441860466\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"586.0567441860466\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1e6h4md\" id=\"SequenceFlow_1e6h4md_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"318\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"258\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_08bun20\" id=\"SequenceFlow_08bun20_di\"\u003e\u003comgdi:waypoint x=\"418\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"568\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"493\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_17fmnol\" id=\"TextAnnotation_17fmnol_di\"\u003e\u003comgdc:Bounds height=\"72\" width=\"144\" x=\"157\" y=\"72\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_09238i3\" id=\"Association_09238i3_di\"\u003e\u003comgdi:waypoint x=\"321\" xsi:type=\"omgdc:Point\" y=\"173\"/\u003e\u003comgdi:waypoint x=\"280\" xsi:type=\"omgdc:Point\" y=\"144\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_000xz6j\" id=\"TextAnnotation_000xz6j_di\"\u003e\u003comgdc:Bounds height=\"94\" width=\"189\" x=\"435\" y=\"61\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0457y43\" id=\"Association_0457y43_di\"\u003e\u003comgdi:waypoint x=\"418\" xsi:type=\"omgdc:Point\" y=\"176\"/\u003e\u003comgdi:waypoint x=\"453\" xsi:type=\"omgdc:Point\" y=\"155\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 7,
      "description": "An example which attempts to query ElasticSearch using a pre-defined query. Query examples are provided during workflow creation.",
      "export_key": "example_elasticsearch_query_from_incident",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1656342284340,
      "name": "Example: ElasticSearch Query from Incident",
      "object_type": "incident",
      "programmatic_name": "example_elasticsearch_query_from_incident",
      "tags": [
        {
          "tag_handle": "fn_elasticsearch",
          "value": null
        }
      ],
      "uuid": "90c650a7-da55-4bfd-b409-c938ec608d2b",
      "workflow_id": 33
    }
  ],
  "workspaces": []
}
