{
  "action_order": [],
  "actions": [
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "incident.properties.sdlp_incident_id",
          "method": "has_a_value",
          "type": null,
          "value": null
        }
      ],
      "enabled": true,
      "export_key": "Example: Symantec DLP - Send a note to a DLP Incident",
      "id": 34,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Symantec DLP - Send a note to a DLP Incident",
      "object_type": "incident",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "44f50a78-4b62-4965-a23f-84c63fd526ae",
      "view_items": [
        {
          "content": "308c8880-cdad-410c-9640-6dd3613f12f2",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "sdlp_send_note_to_incident"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "incident.plan_status",
          "method": "equals",
          "type": null,
          "value": "Closed"
        },
        {
          "evaluation_id": null,
          "field_name": "incident.properties.sdlp_incident_id",
          "method": "has_a_value",
          "type": null,
          "value": null
        }
      ],
      "enabled": true,
      "export_key": "Example: Symantec DLP - Update DLP when this Incident is closed ",
      "id": 35,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: Symantec DLP - Update DLP when this Incident is closed ",
      "object_type": "incident",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 0,
      "uuid": "4562cf17-6ac6-4a09-b2ee-91dd12fab662",
      "view_items": [],
      "workflows": [
        "sdlp_set_incident_status"
      ]
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "export_date": 1643739975358,
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
      "export_key": "__function/sdlp_update_payload",
      "hide_notification": false,
      "id": 297,
      "input_type": "textarea",
      "internal": false,
      "is_tracked": false,
      "name": "sdlp_update_payload",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "sdlp_update_payload",
      "tooltip": "A JSON-like object which contains values to be updated on a given Symantec DLP Incident",
      "type_id": 11,
      "uuid": "b15871eb-b436-4266-b1bb-8368b743972b",
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
      "export_key": "actioninvocation/sdlp_note_to_be_sent",
      "hide_notification": false,
      "id": 296,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "sdlp_note_to_be_sent",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "SDLP Note Text",
      "tooltip": "A Activity Field to take a user entered piece of text to be sent to DLP. Only plaintext can be sent",
      "type_id": 6,
      "uuid": "308c8880-cdad-410c-9640-6dd3613f12f2",
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
      "export_key": "incident/sdlp_incident_url",
      "hide_notification": false,
      "id": 295,
      "input_type": "textarea",
      "internal": false,
      "is_tracked": false,
      "name": "sdlp_incident_url",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": true,
      "tags": [],
      "templates": [],
      "text": "Symantec DLP Incident URL ",
      "tooltip": "",
      "type_id": 0,
      "uuid": "49598693-2ac3-43af-a26b-011cdbe7bd4a",
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
      "export_key": "incident/sdlp_incident_id",
      "hide_notification": false,
      "id": 294,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "sdlp_incident_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Symantec DLP Incident ID",
      "tooltip": "The ID of a Symantec DLP Incident",
      "type_id": 0,
      "uuid": "55f35e22-1610-42b0-accc-f65974e86e4e",
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
      "created_date": 1643732716400,
      "creator": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "description": {
        "content": "A function which is used to update the details of a Symantec DLP Incident. Takes 1 input which is a dictionary of things to be changed. To enable to updating of multiple custom attributes, provide a list or dictionary of all the attributes to be changed in the format: \u003cattribute_name\u003e: \u003cnew_value\u003e",
        "format": "text"
      },
      "destination_handle": "fn_symantec_dlp",
      "display_name": "Symantec DLP: Update Incident",
      "export_key": "fn_symantec_dlp_update_incident",
      "id": 17,
      "last_modified_by": {
        "display_name": "Admin User",
        "id": 1,
        "name": "admin@example.com",
        "type": "user"
      },
      "last_modified_time": 1643734109733,
      "name": "fn_symantec_dlp_update_incident",
      "tags": [],
      "uuid": "8962f715-6114-4e8f-a247-29c40623b98c",
      "version": 2,
      "view_items": [
        {
          "content": "b15871eb-b436-4266-b1bb-8368b743972b",
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
          "name": "Example: Symantec DLP - Send Note to Incident",
          "object_type": "incident",
          "programmatic_name": "sdlp_send_note_to_incident",
          "tags": [],
          "uuid": null,
          "workflow_id": 22
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: Symantec DLP - Set Incident Status to Closed",
          "object_type": "incident",
          "programmatic_name": "sdlp_set_incident_status",
          "tags": [],
          "uuid": null,
          "workflow_id": 21
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 208,
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1643739973844,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1643739973844,
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
      "export_key": "fn_symantec_dlp",
      "name": "Symantec DLP Message Destination",
      "programmatic_name": "fn_symantec_dlp",
      "tags": [],
      "users": [
        "admin@example.com"
      ],
      "uuid": "d75c8560-64d2-44ca-87ce-4db510a3c5d1"
    }
  ],
  "notifications": null,
  "overrides": [],
  "phases": [],
  "regulators": null,
  "roles": [],
  "scripts": [],
  "server_version": {
    "build_number": 81,
    "major": 40,
    "minor": 2,
    "version": "40.2.81"
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
        "workflow_id": "sdlp_send_note_to_incident",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"sdlp_send_note_to_incident\" isExecutable=\"true\" name=\"Example: Symantec DLP - Send Note to Incident\"\u003e\u003cdocumentation\u003eAn example workflow which can be used to send a Note to a DLP Incident. This workflow gets its note text from an associated Rule which has an activity field. If no value is given with the activity field then it sends a default piece of text.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_04k82tk\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0gjgecb\" name=\"Symantec DLP: Update Incident\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"8962f715-6114-4e8f-a247-29c40623b98c\"\u003e{\"inputs\":{},\"pre_processing_script\":\"#######################################\\n### Define pre-processing functions ###\\n#######################################\\ndef dict_to_json_str(d):\\n  \\\"\\\"\\\"Function that converts a dictionary into a JSON stringself.\\n     Supports basestring, bool and int.\\n     If the value is None, it sets it to False\\\"\\\"\\\"\\n\\n  json_str = \u0027\\\"{ {0} }\\\"\u0027\\n  json_entry = \u0027\\\"{0}\\\":{1}\u0027\\n  json_entry_str = \u0027\\\"{0}\\\":\\\"{1}\\\"\u0027\\n  json_entry_unicode = u\u0027\\\"{0}\\\":\\\"{1}\\\"\u0027\\n  entries = [] \\n  \\n  for entry in d:\\n    key = entry\\n    value = d[entry]\\n    \\n      \\n    if value is None:\\n      value = False\\n      \\n    if isinstance(value, unicode):\\n      entries.append(json_entry_unicode.format(key, value))\\n      \\n    elif isinstance(value, basestring):\\n      entries.append(json_entry_str.format(key, value))\\n    \\n    elif isinstance(value, bool):\\n      value = \u0027true\u0027 if value == True else \u0027false\u0027\\n      entries.append(json_entry.format(key, value))\\n    \\n    else:\\n      entries.append(json_entry.format(key, value))\\n  \\n  return \u0027{\u0027 + \u0027,\u0027.join(entries) + \u0027}\u0027\\n\\nfrom java.util import Date\\n\\n# Prepare the payload which will be sent to DLP as an update request\\npayload = {\\n\\\"note\\\": u\\\"Note Sent via Resilient Integration with DLP. [{}]{}\\\".format(Date(), rule.properties.sdlp_note_to_be_sent or \\\"Default Note from Resilient\\\"),\\n\\\"incident_id\\\": incident.properties.sdlp_incident_id\\n}\\n\\n\\ninputs.sdlp_update_payload = dict_to_json_str(payload)\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_04k82tk\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1e2bbhi\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_04k82tk\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0gjgecb\"/\u003e\u003cendEvent id=\"EndEvent_1dvnfht\"\u003e\u003cincoming\u003eSequenceFlow_1e2bbhi\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1e2bbhi\" sourceRef=\"ServiceTask_0gjgecb\" targetRef=\"EndEvent_1dvnfht\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0bwojy3\"\u003e\u003ctext\u003eInputs: The SDLP Update Payload takes key:value pairs which represent which parts of the incident we want to update.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0q3ws4z\" sourceRef=\"ServiceTask_0gjgecb\" targetRef=\"TextAnnotation_0bwojy3\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1cpcp9y\"\u003e\u003ctext\u003eThe results of the API call are not returned to the Post-Processing script as all the information we send to DLP is found in the Inputs part of the payload.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0f3swr7\" sourceRef=\"ServiceTask_0gjgecb\" targetRef=\"TextAnnotation_1cpcp9y\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0gjgecb\" id=\"ServiceTask_0gjgecb_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"408\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_04k82tk\" id=\"SequenceFlow_04k82tk_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"408\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"303\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1dvnfht\" id=\"EndEvent_1dvnfht_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"744\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"762\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1e2bbhi\" id=\"SequenceFlow_1e2bbhi_di\"\u003e\u003comgdi:waypoint x=\"508\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"744\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"626\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0bwojy3\" id=\"TextAnnotation_0bwojy3_di\"\u003e\u003comgdc:Bounds height=\"86\" width=\"140\" x=\"234\" y=\"34\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0q3ws4z\" id=\"Association_0q3ws4z_di\"\u003e\u003comgdi:waypoint x=\"414\" xsi:type=\"omgdc:Point\" y=\"170\"/\u003e\u003comgdi:waypoint x=\"355\" xsi:type=\"omgdc:Point\" y=\"120\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1cpcp9y\" id=\"TextAnnotation_1cpcp9y_di\"\u003e\u003comgdc:Bounds height=\"75\" width=\"222\" x=\"595\" y=\"39\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0f3swr7\" id=\"Association_0f3swr7_di\"\u003e\u003comgdi:waypoint x=\"508\" xsi:type=\"omgdc:Point\" y=\"180\"/\u003e\u003comgdi:waypoint x=\"635\" xsi:type=\"omgdc:Point\" y=\"114\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 2,
      "creator_id": "admin@example.com",
      "description": "An example workflow which can be used to send a Note to a DLP Incident. This workflow gets its note text from an associated Rule which has an activity field. If no value is given with the activity field then it sends a default piece of text.",
      "export_key": "sdlp_send_note_to_incident",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1643734110464,
      "name": "Example: Symantec DLP - Send Note to Incident",
      "object_type": "incident",
      "programmatic_name": "sdlp_send_note_to_incident",
      "tags": [],
      "uuid": "1f44df54-2d2d-4df9-9583-461947d74dc1",
      "workflow_id": 22
    },
    {
      "actions": [],
      "content": {
        "version": 2,
        "workflow_id": "sdlp_set_incident_status",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"sdlp_set_incident_status\" isExecutable=\"true\" name=\"Example: Symantec DLP - Set Incident Status to Closed\"\u003e\u003cdocumentation\u003eAn example workflow which is used to update a DLP Incidents Status to Closed.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0dzyxvb\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1fby33m\" name=\"Symantec DLP: Update Incident\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"8962f715-6114-4e8f-a247-29c40623b98c\"\u003e{\"inputs\":{},\"pre_processing_script\":\"#######################################\\n### Define pre-processing functions ###\\n#######################################\\ndef dict_to_json_str(d):\\n  \\\"\\\"\\\"Function that converts a dictionary into a JSON stringself.\\n     Supports basestring, bool and int.\\n     If the value is None, it sets it to False\\\"\\\"\\\"\\n\\n  json_str = \u0027\\\"{ {0} }\\\"\u0027\\n  json_entry = \u0027\\\"{0}\\\":{1}\u0027\\n  json_entry_str = \u0027\\\"{0}\\\":\\\"{1}\\\"\u0027\\n  json_entry_unicode = u\u0027\\\"{0}\\\":\\\"{1}\\\"\u0027\\n  entries = [] \\n  \\n  for entry in d:\\n    key = entry\\n    value = d[entry]\\n    \\n      \\n    if value is None:\\n      value = False\\n      \\n    if isinstance(value, unicode):\\n      entries.append(json_entry_unicode.format(key, value))\\n    elif isinstance(value, basestring):\\n      entries.append(json_entry_str.format(key, value))\\n    \\n    elif isinstance(value, bool):\\n      value = \u0027true\u0027 if value == True else \u0027false\u0027\\n      entries.append(json_entry.format(key, value))\\n    \\n    else:\\n      entries.append(json_entry.format(key, value))\\n  \\n  return \u0027{\u0027 + \u0027,\u0027.join(entries) + \u0027}\u0027\\n\\nfrom java.util import Date\\n\\n\\npayload = {\\n\\\"status\\\": \\\"Closed\\\",\\n\\\"incident_id\\\": incident.properties.sdlp_incident_id\\n}\\n\\npayload[\u0027note\u0027] = u\\\"[{}] Resilient sent an Update Request to this Incident. Status was changed to {}\\\".format(Date(), payload[\\\"status\\\"])\\n\\n\\ninputs.sdlp_update_payload = dict_to_json_str(payload)\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0dzyxvb\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0vrfby7\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0dzyxvb\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1fby33m\"/\u003e\u003cendEvent id=\"EndEvent_1c2r23k\"\u003e\u003cincoming\u003eSequenceFlow_0vrfby7\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0vrfby7\" sourceRef=\"ServiceTask_1fby33m\" targetRef=\"EndEvent_1c2r23k\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" xsi:type=\"omgdc:Point\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" xsi:type=\"omgdc:Point\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1fby33m\" id=\"ServiceTask_1fby33m_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"376\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0dzyxvb\" id=\"SequenceFlow_0dzyxvb_di\"\u003e\u003comgdi:waypoint x=\"198\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"376\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"287\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1c2r23k\" id=\"EndEvent_1c2r23k_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"659\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"677\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0vrfby7\" id=\"SequenceFlow_0vrfby7_di\"\u003e\u003comgdi:waypoint x=\"476\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"659\" xsi:type=\"omgdc:Point\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"567.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 2,
      "creator_id": "admin@example.com",
      "description": "An example workflow which is used to update a DLP Incidents Status to Closed.",
      "export_key": "sdlp_set_incident_status",
      "last_modified_by": "admin@example.com",
      "last_modified_time": 1643734110283,
      "name": "Example: Symantec DLP - Set Incident Status to Closed",
      "object_type": "incident",
      "programmatic_name": "sdlp_set_incident_status",
      "tags": [],
      "uuid": "68af500f-fb0a-490a-b438-5f90024dfe1e",
      "workflow_id": 21
    }
  ],
  "workspaces": []
}
