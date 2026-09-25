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
      "export_key": "Example: Geocoding Get Address",
      "id": 552,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Geocoding Get Address",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "8d75c368-8d33-42e3-be0e-111ef5f91435",
      "view_items": [],
      "workflows": [
        "example_geocoding_get_address"
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
          "value": "String"
        }
      ],
      "enabled": true,
      "export_key": "Example: Geocoding Get Coordinates",
      "id": 553,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Geocoding Get Coordinates",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "13b417e9-6d30-4778-953a-205fcd2b4578",
      "view_items": [],
      "workflows": [
        "example_geocoding_get_coordinates"
      ]
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "case_matching_profiles": [],
  "export_date": 1744626570192,
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
      "export_key": "__function/geocoding_data",
      "hide_notification": false,
      "id": 3697,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "geocoding_data",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "geocoding_data",
      "tooltip": "value will be specific to the source field",
      "type_id": 11,
      "uuid": "d36e151c-e17a-4d24-832a-1a2d73862abb",
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
      "export_key": "__function/geocoding_source",
      "hide_notification": false,
      "id": 3698,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "geocoding_source",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "geocoding_source",
      "tooltip": "",
      "type_id": 11,
      "uuid": "696afe53-bfcf-47fb-8b66-ed4807822818",
      "values": [
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "address",
          "properties": null,
          "uuid": "7a604840-d732-466f-a9b9-1510cb213dac",
          "value": 3765
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "latlng",
          "properties": null,
          "uuid": "aa42d8f2-0652-4090-a7b1-948989f897ca",
          "value": 3766
        }
      ]
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
      "created_date": 1744370419654,
      "description": {
        "content": "Provide conversion of addresses and world coordinates",
        "format": "text"
      },
      "destination_handle": "fn_geocoding",
      "display_name": "Geocoding",
      "export_key": "geocoding",
      "id": 370,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 39,
        "name": "shresh@example.com",
        "type": "user"
      },
      "last_modified_time": 1744370419654,
      "name": "geocoding",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "tags": [],
      "uuid": "4011fe9f-334e-47c3-a96a-f99484f78b9b",
      "version": 0,
      "view_items": [
        {
          "content": "696afe53-bfcf-47fb-8b66-ed4807822818",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "d36e151c-e17a-4d24-832a-1a2d73862abb",
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
          "name": "Example: Geocoding Get Address",
          "object_type": "artifact",
          "programmatic_name": "example_geocoding_get_address",
          "tags": [],
          "uuid": null,
          "workflow_id": 521
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: Geocoding Get Coordinates",
          "object_type": "artifact",
          "programmatic_name": "example_geocoding_get_coordinates",
          "tags": [],
          "uuid": null,
          "workflow_id": 520
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 139,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1744626568026,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1744626568026,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [
        "ada6db97-462e-4cc4-8937-4379a186784f"
      ],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "fn_geocoding",
      "name": "fn_geocoding",
      "programmatic_name": "fn_geocoding",
      "tags": [],
      "users": [
        "shresh@example.com"
      ],
      "uuid": "af859a46-29e6-44eb-8792-75e19f5176b1"
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
        "version": 3,
        "workflow_id": "example_geocoding_get_address",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_geocoding_get_address\" isExecutable=\"true\" name=\"Example: Geocoding Get Address\"\u003e\u003cdocumentation\u003eReturn address from latitude/longitude input\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_08tzbnw\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1glnl83\" name=\"Geocoding\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"4011fe9f-334e-47c3-a96a-f99484f78b9b\"\u003e{\"inputs\":{\"696afe53-bfcf-47fb-8b66-ed4807822818\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"aa42d8f2-0652-4090-a7b1-948989f897ca\"}}},\"post_processing_script\":\"# build note\\nif results.get(\u0027response\u0027) and results.get(\u0027response\u0027, {}).get(\u0027results\u0027):\\n    incident.addNote(helper.createRichText(\\\"\u0026lt;div\u0026gt;Artifact: {}\u0026lt;/div\u0026gt;\u0026lt;div\u0026gt;{}\u0026lt;/div\u0026gt;\\\".format(artifact.value, results.get(\u0027response\u0027, {}).get(\u0027results\u0027, [{}])[0].get(\u0027formatted_address\u0027))))\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.geocoding_data = artifact.value\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_08tzbnw\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0r0ja2p\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_08tzbnw\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1glnl83\"/\u003e\u003cendEvent id=\"EndEvent_0sc82mm\"\u003e\u003cincoming\u003eSequenceFlow_0r0ja2p\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0r0ja2p\" sourceRef=\"ServiceTask_1glnl83\" targetRef=\"EndEvent_0sc82mm\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0iz0wo0\"\u003e\u003ctext\u003ecreates a note with results\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1pqt4u4\" sourceRef=\"ServiceTask_1glnl83\" targetRef=\"TextAnnotation_0iz0wo0\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_07rs9xp\"\u003e\u003ctext\u003eInput latitude/longitude\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1cy4dyp\" sourceRef=\"ServiceTask_1glnl83\" targetRef=\"TextAnnotation_07rs9xp\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1glnl83\" id=\"ServiceTask_1glnl83_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"250\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_08tzbnw\" id=\"SequenceFlow_08tzbnw_di\"\u003e\u003comgdi:waypoint x=\"198\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"250\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"224\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0sc82mm\" id=\"EndEvent_0sc82mm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"423\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"441\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0r0ja2p\" id=\"SequenceFlow_0r0ja2p_di\"\u003e\u003comgdi:waypoint x=\"350\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"423\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"386.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0iz0wo0\" id=\"TextAnnotation_0iz0wo0_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"356\" y=\"81\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1pqt4u4\" id=\"Association_1pqt4u4_di\"\u003e\u003comgdi:waypoint x=\"339\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"392\" y=\"111\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_07rs9xp\" id=\"TextAnnotation_07rs9xp_di\"\u003e\u003comgdc:Bounds height=\"48\" width=\"134\" x=\"138\" y=\"72\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1cy4dyp\" id=\"Association_1cy4dyp_di\"\u003e\u003comgdi:waypoint x=\"265\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"226\" y=\"120\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 3,
      "description": "Return address from latitude/longitude input",
      "export_key": "example_geocoding_get_address",
      "last_modified_by": "shresh@example.com",
      "last_modified_time": 1744371198294,
      "name": "Example: Geocoding Get Address",
      "object_type": "artifact",
      "programmatic_name": "example_geocoding_get_address",
      "tags": [],
      "uuid": "86344bd8-8ecc-4c60-b790-315104dccd25",
      "workflow_id": 521
    },
    {
      "actions": [],
      "content": {
        "version": 3,
        "workflow_id": "example_geocoding_get_coordinates",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_geocoding_get_coordinates\" isExecutable=\"true\" name=\"Example: Geocoding Get Coordinates\"\u003e\u003cdocumentation\u003eGet location address from latitude/longitude coordinates\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0cnonxs\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_08fldk2\" name=\"Geocoding\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"4011fe9f-334e-47c3-a96a-f99484f78b9b\"\u003e{\"inputs\":{\"696afe53-bfcf-47fb-8b66-ed4807822818\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"7a604840-d732-466f-a9b9-1510cb213dac\"}}},\"post_processing_script\":\"# build note\\nif results.get(\u0027response\u0027) and results.get(\u0027response\u0027, {}).get(\u0027results\u0027):\\n  latlng = \\\",\\\".join((str(results.get(\u0027response\u0027, {}).get(\u0027results\u0027, [{}])[0].get(\u0027geometry\u0027, {}).get(\u0027location\u0027, {}).get(\u0027lat\u0027)), str(results.get(\u0027response\u0027, {}).get(\u0027results\u0027, [{}])[0].get(\u0027geometry\u0027, {}).get(\u0027location\u0027, {}).get(\u0027lng\u0027))))\\n  incident.addNote(helper.createRichText(\\\"\u0026lt;div\u0026gt;Artifact: {}\u0026lt;/div\u0026gt;\u0026lt;div\u0026gt;{}\u0026lt;/div\u0026gt;\\\".format(artifact.value, latlng)))\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.geocoding_data = artifact.value\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0cnonxs\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0th7buu\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0cnonxs\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_08fldk2\"/\u003e\u003cendEvent id=\"EndEvent_1suq81v\"\u003e\u003cincoming\u003eSequenceFlow_0th7buu\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0th7buu\" sourceRef=\"ServiceTask_08fldk2\" targetRef=\"EndEvent_1suq81v\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_00w5i0r\"\u003e\u003ctext\u003eInput free formatted Address such as: 75 Binney St., Cambridge, MA 02026, USA\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1oee9db\" sourceRef=\"ServiceTask_08fldk2\" targetRef=\"TextAnnotation_00w5i0r\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_07wuo0o\"\u003e\u003ctext\u003eResults displayed in a note\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_10dw2ig\" sourceRef=\"ServiceTask_08fldk2\" targetRef=\"TextAnnotation_07wuo0o\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_08fldk2\" id=\"ServiceTask_08fldk2_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"248\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0cnonxs\" id=\"SequenceFlow_0cnonxs_di\"\u003e\u003comgdi:waypoint x=\"198\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"248\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"223\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1suq81v\" id=\"EndEvent_1suq81v_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"419\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"437\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0th7buu\" id=\"SequenceFlow_0th7buu_di\"\u003e\u003comgdi:waypoint x=\"348\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"419\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"383.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_00w5i0r\" id=\"TextAnnotation_00w5i0r_di\"\u003e\u003comgdc:Bounds height=\"81\" width=\"164\" x=\"155\" y=\"39\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1oee9db\" id=\"Association_1oee9db_di\"\u003e\u003comgdi:waypoint x=\"279\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"257\" y=\"120\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_07wuo0o\" id=\"TextAnnotation_07wuo0o_di\"\u003e\u003comgdc:Bounds height=\"60\" width=\"154\" x=\"387\" y=\"35\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_10dw2ig\" id=\"Association_10dw2ig_di\"\u003e\u003comgdi:waypoint x=\"341\" y=\"169\"/\u003e\u003comgdi:waypoint x=\"429\" y=\"95\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 3,
      "description": "Get location address from latitude/longitude coordinates",
      "export_key": "example_geocoding_get_coordinates",
      "last_modified_by": "shresh@example.com",
      "last_modified_time": 1744372158430,
      "name": "Example: Geocoding Get Coordinates",
      "object_type": "artifact",
      "programmatic_name": "example_geocoding_get_coordinates",
      "tags": [],
      "uuid": "939f0122-509c-4210-b47e-f82cacef4de1",
      "workflow_id": 520
    }
  ],
  "workspaces": []
}
