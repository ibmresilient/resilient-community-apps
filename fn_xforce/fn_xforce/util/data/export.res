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
            "IP Address",
            "DNS Name",
            "URL",
            "Malware MD5 Hash",
            "Malware SHA-1 Hash",
            "String",
            "Malware SHA-256 Hash"
          ]
        }
      ],
      "enabled": true,
      "export_key": "Example: X-Force Query Collection by ID",
      "id": 237,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: X-Force Query Collection by ID",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "9c29b431-d7cd-4c3f-baee-7e9c102dfc0a",
      "view_items": [],
      "workflows": [
        "example_xforce_collection_by_id"
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
            "URL",
            "Malware MD5 Hash",
            "Malware SHA-1 Hash",
            "String",
            "Malware SHA-256 Hash"
          ]
        }
      ],
      "enabled": true,
      "export_key": "Example: X-Force Query from Artifact",
      "id": 238,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: X-Force Query from Artifact",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "f88a88e6-7c2b-4cee-8ed8-5b093515082d",
      "view_items": [],
      "workflows": [
        "example_xforce_query_collections"
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
            "URL",
            "Malware MD5 Hash",
            "Malware SHA-1 Hash",
            "String",
            "Malware SHA-256 Hash"
          ]
        }
      ],
      "enabled": true,
      "export_key": "Example: X-Force Return Top 3 from Collection(s)",
      "id": 239,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: X-Force Return Top 3 from Collection(s)",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "dfaae51d-5123-4a3c-991f-a5d693b26d21",
      "view_items": [],
      "workflows": [
        "example_return_top_3_entries_from_collections"
      ]
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "export_date": 1683578848199,
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
      "export_key": "__function/xforce_collection_type",
      "hide_notification": false,
      "id": 4368,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "xforce_collection_type",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "xforce_collection_type",
      "tooltip": "Which type of collections to search. Public or private collections available.",
      "type_id": 11,
      "uuid": "ce99b64a-5259-439c-ab60-7137f3b88806",
      "values": [
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "public",
          "properties": null,
          "uuid": "022ba2a8-90d6-433e-bea4-e2cc8ca0bb74",
          "value": 870
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "private",
          "properties": null,
          "uuid": "6f57b1c6-d066-4185-b317-8161d877389b",
          "value": 871
        }
      ]
    },
    {
      "allow_default_value": false,
      "blank_option": false,
      "calculated": false,
      "changeable": true,
      "chosen": false,
      "default_chosen_by_server": false,
      "deprecated": false,
      "export_key": "__function/xforce_collection_id",
      "hide_notification": false,
      "id": 4367,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "xforce_collection_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "xforce_collection_id",
      "tooltip": "A collection ID for use with the XForce API",
      "type_id": 11,
      "uuid": "55c686a5-4611-40ba-bc87-2524141760e1",
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
      "export_key": "__function/xforce_query",
      "hide_notification": false,
      "id": 4369,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "xforce_query",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "xforce_query",
      "tooltip": "A query to submit for searching XForce Collections",
      "type_id": 11,
      "uuid": "6439ec40-9c26-475e-9abe-b738422ca9d0",
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
      "created_date": 1683566156016,
      "description": {
        "content": "A function that takes in a parameter of a xforce_collection_id and then submits this to the X-Force API to gather data for the provided case.",
        "format": "text"
      },
      "destination_handle": "fn_xforce",
      "display_name": "X-Force Utilities: Get Collection by ID",
      "export_key": "xforce_get_collection_by_id",
      "id": 29,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 29,
        "name": "g@example.com",
        "type": "user"
      },
      "last_modified_time": 1683566156059,
      "name": "xforce_get_collection_by_id",
      "tags": [],
      "uuid": "b792f6ec-2dac-439e-9504-15cf23061499",
      "version": 1,
      "view_items": [
        {
          "content": "55c686a5-4611-40ba-bc87-2524141760e1",
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
          "name": "Example: X-Force Get Collection by ID",
          "object_type": "artifact",
          "programmatic_name": "example_xforce_collection_by_id",
          "tags": [],
          "uuid": null,
          "workflow_id": 46
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: X-Force Return Top 3 from Collection(s)",
          "object_type": "artifact",
          "programmatic_name": "example_return_top_3_entries_from_collections",
          "tags": [],
          "uuid": null,
          "workflow_id": 45
        }
      ]
    },
    {
      "created_date": 1683566156086,
      "description": {
        "content": "A function that allows a user to submit a query to the X-Force Collections API. Supports searching either public or private collections.",
        "format": "text"
      },
      "destination_handle": "fn_xforce",
      "display_name": "X-Force Utilities: Query Collection",
      "export_key": "xforce_query_collection",
      "id": 30,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 29,
        "name": "g@example.com",
        "type": "user"
      },
      "last_modified_time": 1683566156127,
      "name": "xforce_query_collection",
      "tags": [],
      "uuid": "a6473838-d1fe-4d40-b284-c48d3b6a91f6",
      "version": 1,
      "view_items": [
        {
          "content": "6439ec40-9c26-475e-9abe-b738422ca9d0",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ce99b64a-5259-439c-ab60-7137f3b88806",
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
          "name": "Example: X-Force Query Collection(s)",
          "object_type": "artifact",
          "programmatic_name": "example_xforce_query_collections",
          "tags": [],
          "uuid": null,
          "workflow_id": 47
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: X-Force Return Top 3 from Collection(s)",
          "object_type": "artifact",
          "programmatic_name": "example_return_top_3_entries_from_collections",
          "tags": [],
          "uuid": null,
          "workflow_id": 45
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 18,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1683578846263,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1683578846263,
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
      "export_key": "fn_xforce",
      "name": "fn_xforce",
      "programmatic_name": "fn_xforce",
      "tags": [],
      "users": [
        "g@example.com"
      ],
      "uuid": "9125153a-7a5d-4ba2-b963-701cc6f8a3d0"
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
    "build_number": 8131,
    "major": 46,
    "minor": 0,
    "version": "46.0.8131"
  },
  "tags": [],
  "task_order": [],
  "timeframes": null,
  "types": [],
  "workflows": [
    {
      "actions": [],
      "content": {
        "version": 30,
        "workflow_id": "example_return_top_3_entries_from_collections",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_return_top_3_entries_from_collections\" isExecutable=\"true\" name=\"Example: X-Force Return Top 3 from Collection(s)\"\u003e\u003cdocumentation\u003eAn example workflow that takes in a query string as a param. \nIt then submits this query to the X-Force API returning case file IDs for each.\nThe top 3 ID\u0027s returned are then queried to return information about the threat saving the info as a note.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1nsihnt\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_00npucf\" name=\"X-Force Utilities: Query Collecti...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"a6473838-d1fe-4d40-b284-c48d3b6a91f6\"\u003e{\"inputs\":{\"ce99b64a-5259-439c-ab60-7137f3b88806\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"022ba2a8-90d6-433e-bea4-e2cc8ca0bb74\"}}},\"post_processing_script\":\"if results.get(\\\"content\\\", {}).get(\\\"num_of_casefiles\\\") != 0:\\n  noteText = \\\"\\\"\\\"\u0026lt;b\u0026gt;X-Force Query status\u0026lt;/b\u0026gt;\u0026lt;br\u0026gt;Total matched case files :\u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;\u0026lt;br\u0026gt;Now searching top 3 results\\\"\\\"\\\".format(results.get(\\\"content\\\", {}).get(\\\"num_of_casefiles\\\"))\\n  incident.addNote(helper.createRichText(noteText))\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"if artifact.value is not None:\\n  inputs.xforce_query = artifact.value\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"xforcecasefiles\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1nsihnt\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1tibeat\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1nsihnt\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_00npucf\"/\u003e\u003cparallelGateway id=\"ParallelGateway_1a56czp\"\u003e\u003cincoming\u003eSequenceFlow_1tibeat\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_12m77s9\u003c/outgoing\u003e\u003coutgoing\u003eSequenceFlow_0je6199\u003c/outgoing\u003e\u003coutgoing\u003eSequenceFlow_1dhjnlc\u003c/outgoing\u003e\u003c/parallelGateway\u003e\u003cserviceTask id=\"ServiceTask_065xgt3\" name=\"X-Force Utilities: Get Collection...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"b792f6ec-2dac-439e-9504-15cf23061499\"\u003e{\"inputs\":{},\"post_processing_script\":\"if results.get(\\\"success\\\"):\\n  content = results.get(\\\"content\\\", {})\\n  noteText = \\\"\\\"\\\"\u0026lt;br\u0026gt;Title :\u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;\\n  \u0026lt;b\u0026gt;Created :\u0026lt;/b\u0026gt;{1}\u0026lt;/a\u0026gt;\\n  \u0026lt;b\u0026gt;Tags:\u0026lt;/b\u0026gt; {2}\u0026lt;/b\u0026gt;\\n  \\\"\\\"\\\".format(content.get(\\\"title\\\"), content.get(\\\"created\\\"), content.get(\\\"tags\\\"))\\n  \\n  incident.addNote(helper.createRichText(f\u0027{noteText}\\\\n{results.get(\\\"wiki\\\")}\u0027))\\n  \\n  #We have access to an attribute in results called \u0027wiki\u0027\\n  # As an enhancement you could save this \u0027wiki\u0027 to an attachment to have a HTML or TXT description of the threat\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"if workflow.properties.xforcecasefiles.get(\\\"content\\\", {}).get(\\\"num_of_casefiles\\\") \u0026gt; 0:\\n  inputs.xforce_collection_id = workflow.properties.xforcecasefiles.get(\\\"content\\\", {}).get(\\\"casefiles\\\", [])[0].get(\\\"caseFileID\\\")\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_12m77s9\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1v01xob\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1tibeat\" sourceRef=\"ServiceTask_00npucf\" targetRef=\"ParallelGateway_1a56czp\"/\u003e\u003csequenceFlow id=\"SequenceFlow_12m77s9\" sourceRef=\"ParallelGateway_1a56czp\" targetRef=\"ServiceTask_065xgt3\"/\u003e\u003cserviceTask id=\"ServiceTask_09x84kb\" name=\"X-Force Utilities: Get Collection...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"b792f6ec-2dac-439e-9504-15cf23061499\"\u003e{\"inputs\":{},\"post_processing_script\":\"if results.get(\\\"success\\\"):\\n  content = results.get(\\\"content\\\", {})\\n  noteText = \\\"\\\"\\\"\u0026lt;br\u0026gt;Title :\u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;\\n  \u0026lt;b\u0026gt;Created :\u0026lt;/b\u0026gt;{1}\u0026lt;/a\u0026gt;\\n  \u0026lt;b\u0026gt;Tags:\u0026lt;/b\u0026gt; {2}\u0026lt;/b\u0026gt;\\n  \\\"\\\"\\\".format(content.get(\\\"title\\\"), content.get(\\\"created\\\"), content.get(\\\"tags\\\"))\\n  \\n  incident.addNote(helper.createRichText(f\u0027{noteText}\\\\n{results.get(\\\"wiki\\\")}\u0027))\\n  \\n  #We have access to an attribute in results called \u0027wiki\u0027\\n  # As an enhancement you could save this \u0027wiki\u0027 to an attachment to have a HTML or TXT description of the threat\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"if workflow.properties.xforcecasefiles.get(\\\"content\\\", {}).get(\\\"num_of_casefiles\\\") \u0026gt;= 2:\\n  inputs.xforce_collection_id = workflow.properties.xforcecasefiles.get(\\\"content\\\", {}).get(\\\"casefiles\\\", [])[1].get(\\\"caseFileID\\\")\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0je6199\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_19wkis2\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0je6199\" sourceRef=\"ParallelGateway_1a56czp\" targetRef=\"ServiceTask_09x84kb\"/\u003e\u003cserviceTask id=\"ServiceTask_0blsyrq\" name=\"X-Force Utilities: Get Collection...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"b792f6ec-2dac-439e-9504-15cf23061499\"\u003e{\"inputs\":{},\"post_processing_script\":\"if results.get(\\\"success\\\"):\\n  content = results.get(\\\"content\\\", {})\\n  noteText = \\\"\\\"\\\"\u0026lt;br\u0026gt;Title :\u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;\\n  \u0026lt;b\u0026gt;Created :\u0026lt;/b\u0026gt;{1}\u0026lt;/a\u0026gt;\\n  \u0026lt;b\u0026gt;Tags:\u0026lt;/b\u0026gt; {2}\u0026lt;/b\u0026gt;\\n  \\\"\\\"\\\".format(content.get(\\\"title\\\"), content.get(\\\"created\\\"), content.get(\\\"tags\\\"))\\n  \\n  incident.addNote(helper.createRichText(f\u0027{noteText}\\\\n{results.get(\\\"wiki\\\")}\u0027))\\n  \\n  #We have access to an attribute in results called \u0027wiki\u0027\\n  # As an enhancement you could save this \u0027wiki\u0027 to an attachment to have a HTML or TXT description of the threat\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"if workflow.properties.xforcecasefiles.get(\\\"content\\\", {}).get(\\\"num_of_casefiles\\\") \u0026gt;= 3:\\n  inputs.xforce_collection_id = workflow.properties.xforcecasefiles.get(\\\"content\\\", {}).get(\\\"casefiles\\\", [])[2].get(\\\"caseFileID\\\")\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1dhjnlc\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1to8mn0\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1dhjnlc\" sourceRef=\"ParallelGateway_1a56czp\" targetRef=\"ServiceTask_0blsyrq\"/\u003e\u003cendEvent id=\"EndEvent_0ultch5\"\u003e\u003cincoming\u003eSequenceFlow_1v01xob\u003c/incoming\u003e\u003cincoming\u003eSequenceFlow_19wkis2\u003c/incoming\u003e\u003cincoming\u003eSequenceFlow_1to8mn0\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1v01xob\" sourceRef=\"ServiceTask_065xgt3\" targetRef=\"EndEvent_0ultch5\"/\u003e\u003csequenceFlow id=\"SequenceFlow_19wkis2\" sourceRef=\"ServiceTask_09x84kb\" targetRef=\"EndEvent_0ultch5\"/\u003e\u003csequenceFlow id=\"SequenceFlow_1to8mn0\" sourceRef=\"ServiceTask_0blsyrq\" targetRef=\"EndEvent_0ultch5\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1ftqxdf\"\u003e\u003ctext\u003eQuery top 3 case files concurrently.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0xn5qh7\" sourceRef=\"ParallelGateway_1a56czp\" targetRef=\"TextAnnotation_1ftqxdf\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_00npucf\" id=\"ServiceTask_00npucf_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"259\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1nsihnt\" id=\"SequenceFlow_1nsihnt_di\"\u003e\u003comgdi:waypoint x=\"198\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"259\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"228.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ParallelGateway_1a56czp\" id=\"ParallelGateway_1a56czp_di\"\u003e\u003comgdc:Bounds height=\"50\" width=\"50\" x=\"427\" y=\"181\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"452\" y=\"234\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_065xgt3\" id=\"ServiceTask_065xgt3_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"550\" y=\"56\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1tibeat\" id=\"SequenceFlow_1tibeat_di\"\u003e\u003comgdi:waypoint x=\"359\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"427\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"393\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_12m77s9\" id=\"SequenceFlow_12m77s9_di\"\u003e\u003comgdi:waypoint x=\"452\" y=\"181\"/\u003e\u003comgdi:waypoint x=\"452\" y=\"96\"/\u003e\u003comgdi:waypoint x=\"550\" y=\"96\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"467\" y=\"131.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_09x84kb\" id=\"ServiceTask_09x84kb_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"550\" y=\"178\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0je6199\" id=\"SequenceFlow_0je6199_di\"\u003e\u003comgdi:waypoint x=\"477\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"514\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"514\" y=\"218\"/\u003e\u003comgdi:waypoint x=\"550\" y=\"218\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"529\" y=\"205\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0blsyrq\" id=\"ServiceTask_0blsyrq_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"550\" y=\"329\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1dhjnlc\" id=\"SequenceFlow_1dhjnlc_di\"\u003e\u003comgdi:waypoint x=\"452\" y=\"231\"/\u003e\u003comgdi:waypoint x=\"452\" y=\"369\"/\u003e\u003comgdi:waypoint x=\"550\" y=\"369\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"467\" y=\"293\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0ultch5\" id=\"EndEvent_0ultch5_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"824\" y=\"200\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"842\" y=\"239\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1v01xob\" id=\"SequenceFlow_1v01xob_di\"\u003e\u003comgdi:waypoint x=\"650\" y=\"96\"/\u003e\u003comgdi:waypoint x=\"737\" y=\"96\"/\u003e\u003comgdi:waypoint x=\"737\" y=\"218\"/\u003e\u003comgdi:waypoint x=\"824\" y=\"218\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"752\" y=\"150\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_19wkis2\" id=\"SequenceFlow_19wkis2_di\"\u003e\u003comgdi:waypoint x=\"650\" y=\"218\"/\u003e\u003comgdi:waypoint x=\"824\" y=\"218\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"737\" y=\"196\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1to8mn0\" id=\"SequenceFlow_1to8mn0_di\"\u003e\u003comgdi:waypoint x=\"650\" y=\"369\"/\u003e\u003comgdi:waypoint x=\"737\" y=\"369\"/\u003e\u003comgdi:waypoint x=\"737\" y=\"218\"/\u003e\u003comgdi:waypoint x=\"824\" y=\"218\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"752\" y=\"286.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1ftqxdf\" id=\"TextAnnotation_1ftqxdf_di\"\u003e\u003comgdc:Bounds height=\"64\" width=\"155\" x=\"284\" y=\"61\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0xn5qh7\" id=\"Association_0xn5qh7_di\"\u003e\u003comgdi:waypoint x=\"441\" y=\"192\"/\u003e\u003comgdi:waypoint x=\"387\" y=\"125\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 30,
      "description": "An example workflow that takes in a query string as a param. \nIt then submits this query to the X-Force API returning case file IDs for each.\nThe top 3 ID\u0027s returned are then queried to return information about the threat saving the info as a note.",
      "export_key": "example_return_top_3_entries_from_collections",
      "last_modified_by": "g@example.com",
      "last_modified_time": 1683578527754,
      "name": "Example: X-Force Return Top 3 from Collection(s)",
      "object_type": "artifact",
      "programmatic_name": "example_return_top_3_entries_from_collections",
      "tags": [],
      "uuid": "8f689f10-10a0-49bd-b75d-f18e850e8bf3",
      "workflow_id": 45
    },
    {
      "actions": [],
      "content": {
        "version": 19,
        "workflow_id": "example_xforce_collection_by_id",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_xforce_collection_by_id\" isExecutable=\"true\" name=\"Example: X-Force Get Collection by ID\"\u003e\u003cdocumentation\u003eAn example workflow that takes in a parameter of a xforce_collection_id and then attempts to gather enriching information for that collection via the X-Force API.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_07pnq8s\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0ckwibm\" name=\"X-Force Utilities: Get Collection...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"b792f6ec-2dac-439e-9504-15cf23061499\"\u003e{\"inputs\":{},\"post_processing_script\":\"if results.get(\\\"success\\\"):\\n  content = results.get(\\\"content\\\", {})\\n  try:\\n    noteText = \\\"\\\"\\\"\u0026lt;b\u0026gt;Title:\u0026lt;/b\u0026gt; {0}\\n    \u0026lt;b\u0026gt;Created:\u0026lt;/b\u0026gt; {1}\\n    \u0026lt;b\u0026gt;Tags:\u0026lt;/b\u0026gt; {2}\\n    \\\"\\\"\\\".format(content.get(\\\"title\\\"), content.get(\\\"created\\\"), content.get(\\\"tags\\\"))\\n  \\n    incident.addNote(helper.createRichText(f\u0027{noteText}\\\\n{content.get(\\\"contents\\\", {}).get(\\\"wiki\\\")}\u0027))\\n  except:\\n    # no incident matched the provided id\\n    # add a note with results.content, which will inform the user of this\\n    incident.addNote(results.get(\\\"content\\\"))\\n  \\n  # We have access to an attribute in results called \u0027wiki\u0027\\n  # As an enhancement you could save this \u0027wiki\u0027 to an attachment to have a HTML or TXT description of the threat\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.xforce_collection_id = artifact.value\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_07pnq8s\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1f96ooz\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndEvent_1kr34gp\"\u003e\u003cincoming\u003eSequenceFlow_1f96ooz\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_07pnq8s\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0ckwibm\"/\u003e\u003csequenceFlow id=\"SequenceFlow_1f96ooz\" sourceRef=\"ServiceTask_0ckwibm\" targetRef=\"EndEvent_1kr34gp\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0ckwibm\" id=\"ServiceTask_0ckwibm_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"419\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1kr34gp\" id=\"EndEvent_1kr34gp_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"741\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"759\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_07pnq8s\" id=\"SequenceFlow_07pnq8s_di\"\u003e\u003comgdi:waypoint x=\"198\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"419\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"308.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1f96ooz\" id=\"SequenceFlow_1f96ooz_di\"\u003e\u003comgdi:waypoint x=\"519\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"741\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"630\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 19,
      "description": "An example workflow that takes in a parameter of a xforce_collection_id and then attempts to gather enriching information for that collection via the X-Force API.",
      "export_key": "example_xforce_collection_by_id",
      "last_modified_by": "g@example.com",
      "last_modified_time": 1683575769018,
      "name": "Example: X-Force Get Collection by ID",
      "object_type": "artifact",
      "programmatic_name": "example_xforce_collection_by_id",
      "tags": [],
      "uuid": "0f54e27f-8c4d-4280-aa6b-6d20bbd2fb7f",
      "workflow_id": 46
    },
    {
      "actions": [],
      "content": {
        "version": 13,
        "workflow_id": "example_xforce_query_collections",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_xforce_query_collections\" isExecutable=\"true\" name=\"Example: X-Force Query Collection(s)\"\u003e\u003cdocumentation\u003eAn example workflow that takes in a provided artifact as a query and then submits this to the X-Force API searching collections for casefiles relevant to the query.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0bl1rnp\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cendEvent id=\"EndEvent_1jbcejm\"\u003e\u003cincoming\u003eSequenceFlow_0t72ki4\u003c/incoming\u003e\u003c/endEvent\u003e\u003cserviceTask id=\"ServiceTask_1csl1db\" name=\"X-Force Utilities: Query Collecti...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"a6473838-d1fe-4d40-b284-c48d3b6a91f6\"\u003e{\"inputs\":{\"ce99b64a-5259-439c-ab60-7137f3b88806\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"6f57b1c6-d066-4185-b317-8161d877389b\"}}},\"post_processing_script\":\"if results.get(\\\"success\\\"):\\n  if results.get(\\\"content\\\", {}).get(\\\"num_of_casefiles\\\") \u0026gt; 0:\\n    noteText = \\\"\\\"\\\"\u0026lt;b\u0026gt;X-Force Query status\u0026lt;/b\u0026gt;\u0026lt;br\u0026gt;Total matched case files: \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;\\\"\\\"\\\".format(results.get(\\\"content\\\", {}).get(\\\"num_of_casefiles\\\"))\\n    incident.addNote(helper.createRichText(noteText))\\n  else:\\n    noteText = \\\"\\\"\\\"\u0026lt;b\u0026gt;X-Force Query status\u0026lt;/b\u0026gt;\u0026lt;br\u0026gt;{0}\\\"\\\"\\\".format(results.get(\\\"content\\\"))\\n    incident.addNote(helper.createRichText(noteText))\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.xforce_query = artifact.value\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0bl1rnp\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0t72ki4\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0bl1rnp\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1csl1db\"/\u003e\u003csequenceFlow id=\"SequenceFlow_0t72ki4\" sourceRef=\"ServiceTask_1csl1db\" targetRef=\"EndEvent_1jbcejm\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1jbcejm\" id=\"EndEvent_1jbcejm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"728\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"746\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1csl1db\" id=\"ServiceTask_1csl1db_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"403\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0bl1rnp\" id=\"SequenceFlow_0bl1rnp_di\"\u003e\u003comgdi:waypoint x=\"198\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"403\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"300.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0t72ki4\" id=\"SequenceFlow_0t72ki4_di\"\u003e\u003comgdi:waypoint x=\"503\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"728\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"615.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 13,
      "description": "An example workflow that takes in a provided artifact as a query and then submits this to the X-Force API searching collections for casefiles relevant to the query.",
      "export_key": "example_xforce_query_collections",
      "last_modified_by": "g@example.com",
      "last_modified_time": 1683577735952,
      "name": "Example: X-Force Query Collection(s)",
      "object_type": "artifact",
      "programmatic_name": "example_xforce_query_collections",
      "tags": [],
      "uuid": "5bccb460-8f57-4621-aab6-474151b7c5c2",
      "workflow_id": 47
    }
  ],
  "workspaces": []
}
