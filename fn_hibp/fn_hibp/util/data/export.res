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
            "Email Sender",
            "Email Recipient"
          ]
        }
      ],
      "enabled": true,
      "export_key": "Have I Been Pwned Search",
      "id": 494,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Have I Been Pwned Search",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "dea169b5-0d74-42f6-bcbe-c5b98cd6ddc9",
      "view_items": [],
      "workflows": [
        "have_i_been_pwned_search"
      ]
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "case_matching_profiles": [],
  "export_date": 1745323960607,
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
      "export_key": "__function/email_address",
      "hide_notification": false,
      "id": 3437,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "email_address",
      "operation_perms": {},
      "operations": [],
      "placeholder": "test@example.com",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "email_address",
      "tooltip": "",
      "type_id": 11,
      "uuid": "11327794-a957-44cd-a85b-8b94143bc02c",
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
      "created_date": 1743603631704,
      "description": {
        "content": "Get all verified breaches of an email address from Have I Been Pwned.",
        "format": "text"
      },
      "destination_handle": "hibp",
      "display_name": "Have I Been Pwned Get Breaches",
      "export_key": "have_i_been_pwned_get_breaches",
      "id": 330,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 39,
        "name": "shresh@example.com",
        "type": "user"
      },
      "last_modified_time": 1743603631704,
      "name": "have_i_been_pwned_get_breaches",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "tags": [],
      "uuid": "fe751617-4ee9-43e8-b35d-a6bf419b65d5",
      "version": 0,
      "view_items": [
        {
          "content": "11327794-a957-44cd-a85b-8b94143bc02c",
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
          "name": "Have I Been Pwned Search",
          "object_type": "artifact",
          "programmatic_name": "have_i_been_pwned_search",
          "tags": [],
          "uuid": null,
          "workflow_id": 460
        }
      ]
    },
    {
      "created_date": 1743603631823,
      "description": {
        "content": "Get all pastes of an email account from Have I Been Pwned.",
        "format": "text"
      },
      "destination_handle": "hibp",
      "display_name": "Have I Been Pwned Get Pastes",
      "export_key": "have_i_been_pwned_get_pastes",
      "id": 331,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 39,
        "name": "shresh@example.com",
        "type": "user"
      },
      "last_modified_time": 1743603631823,
      "name": "have_i_been_pwned_get_pastes",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "tags": [],
      "uuid": "d448bee5-d85e-484e-a91c-274ebae67123",
      "version": 0,
      "view_items": [
        {
          "content": "11327794-a957-44cd-a85b-8b94143bc02c",
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
          "name": "Have I Been Pwned Search",
          "object_type": "artifact",
          "programmatic_name": "have_i_been_pwned_search",
          "tags": [],
          "uuid": null,
          "workflow_id": 460
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 165,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1745323958003,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1745323958003,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [
        "1bdc7809-d0ed-4c78-9854-4ce51e3fb231"
      ],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "hibp",
      "name": "hibp",
      "programmatic_name": "hibp",
      "tags": [],
      "users": [
        "shresh@example.com"
      ],
      "uuid": "dcc45f6f-e39c-47c3-ac9e-2079611f4f47"
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
        "workflow_id": "have_i_been_pwned_search",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"have_i_been_pwned_search\" isExecutable=\"true\" name=\"Have I Been Pwned Search\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1f0b29z\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1s5btvn\" name=\"Have I Been Pwned Get Breaches\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"fe751617-4ee9-43e8-b35d-a6bf419b65d5\"\u003e{\"inputs\":{},\"post_processing_script\":\"msg = \\\"Timestamp: \\\" + str(results.metrics[\\\"timestamp\\\"])\\nif results.content[\\\"Breaches\\\"]:\\n  msg = msg + \\\"\\\\nBreaches: \\\" + str(len(results.content[\\\"Breaches\\\"]))\\nelse:\\n  msg = msg + \\\"\\\\nNo Breaches\\\"\\n  \\nif artifact.description:\\n  artifact.description = artifact.description.content + \u0027\\\\n\\\\n\u0027 + msg\\nelse:\\n  artifact.description = msg\\n\\n\\n\u0027\u0027\u0027 Example response\\n{\\n  \\\"Inputs\\\": {\\n    \\\"email_address\\\": \\\"test@email.com\\\"\\n  }, \\n  \\\"Run Time\\\": \\\"2000\\\",\\n  \\\"Breaches\\\":\\n    [  \\n       {  \\n          u\u0027PwnCount\u0027:14936670,\\n          u\u0027Domain\u0027:u\u0027000webhost.com\u0027,\\n          u\u0027IsSensitive\u0027:False,\\n          u\u0027Name\u0027:u\u0027000webhost\u0027,\\n          u\u0027Title\u0027:u\u0027000webhost\u0027,\\n          u\u0027DataClasses\u0027:[  \\n             u\u0027Email addresses\u0027,\\n             u\u0027IP addresses\u0027,\\n             u\u0027Names\u0027,\\n             u\u0027Passwords\u0027\\n          ],\\n          u\u0027LogoType\u0027:u\u0027png\u0027,\\n          u\u0027IsSpamList\u0027:False,\\n          u\u0027IsRetired\u0027:False,\\n          u\u0027BreachDate\u0027:u\u00272015-03-01\u0027,\\n          u\u0027IsFabricated\u0027:False,\\n          u\u0027ModifiedDate\u0027:      u\u00272017-12-10T21:44:27      Z\u0027,\\n          u\u0027AddedDate\u0027:      u\u00272015-10-26T23:35:45      Z\u0027,\\n          u\u0027IsVerified\u0027:True,\\n          u\u0027Description\u0027:u\u0027In approximately March 2015,\\n          the free web hosting provider \u0026lt;a href=\\\"http://www.troyhunt.com/2015/10/breaches-traders-plain-text-passwords.html\\\" target=\\\"_blank\\\" rel=\\\"noopener\\\"\u0026gt;000webhost suffered a major data breach\u0026lt;/a\u0026gt; that exposed almost 15 million customer records. The data was sold and traded before 000webhost was alerted in October. The breach included names,\\n          email addresses and plain text passwords.\u0027\\n       },\\n       {  \\n          u\u0027PwnCount\u0027:7990619,\\n          u\u0027Domain\u0027:u\u00278tracks.com\u0027,\\n          u\u0027IsSensitive\u0027:False,\\n          u\u0027Name\u0027:u\u00278tracks\u0027,\\n          u\u0027Title\u0027:u\u00278tracks\u0027,\\n          u\u0027DataClasses\u0027:[  \\n             u\u0027Email addresses\u0027,\\n             u\u0027Passwords\u0027\\n          ],\\n          u\u0027LogoType\u0027:u\u0027png\u0027,\\n          u\u0027IsSpamList\u0027:False,\\n          u\u0027IsRetired\u0027:False,\\n          u\u0027BreachDate\u0027:u\u00272017-06-27\u0027,\\n          u\u0027IsFabricated\u0027:False,\\n          u\u0027ModifiedDate\u0027:      u\u00272018-02-16T07:09:30      Z\u0027,\\n          u\u0027AddedDate\u0027:      u\u00272018-02-16T07:09:30      Z\u0027,\\n          u\u0027IsVerified\u0027:True,\\n          u\u0027Description\u0027:u\u0027In June 2017,\\n          the online playlists service known as \u0026lt;a href=\\\"https://blog.8tracks.com/2017/06/27/password-security-alert/\\\" target=\\\"_blank\\\" rel=\\\"noopener\\\"\u0026gt;8Tracks suffered a data breach\u0026lt;/a\u0026gt; which impacted 18 million accounts. In their disclosure,\\n          8      Tracks advised that \u0026amp;quot;the vector for the attack was an employee\\\\u2019s GitHub account,\\n          which was not secured using two-factor authentication\u0026amp;quot;. Salted SHA-1 password hashes for users who \u0026lt;em\u0026gt;didn\\\\\u0027t\u0026lt;/em\u0026gt; sign up with either Google or Facebook authentication were also included. The data was provided to HIBP by whitehat security researcher and data analyst Adam Davies and contained almost 8 million unique email addresses.\u0027\\n       },\\n       {  \\n          u\u0027PwnCount\u0027:1372550,\\n          u\u0027Domain\u0027:u\u0027abusewith.us\u0027,\\n          u\u0027IsSensitive\u0027:False,\\n          u\u0027Name\u0027:u\u0027AbuseWithUs\u0027,\\n          u\u0027Title\u0027:u\u0027AbuseWith.Us\u0027,\\n          u\u0027DataClasses\u0027:[  \\n             u\u0027Email addresses\u0027,\\n             u\u0027IP addresses\u0027,\\n             u\u0027Passwords\u0027,\\n             u\u0027Usernames\u0027\\n          ],\\n          u\u0027LogoType\u0027:u\u0027png\u0027,\\n          u\u0027IsSpamList\u0027:False,\\n          u\u0027IsRetired\u0027:False,\\n          u\u0027BreachDate\u0027:u\u00272016-07-01\u0027,\\n          u\u0027IsFabricated\u0027:False,\\n          u\u0027ModifiedDate\u0027:      u\u00272017-10-09T11:08:45      Z\u0027,\\n          u\u0027AddedDate\u0027:      u\u00272017-10-09T11:08:45      Z\u0027,\\n          u\u0027IsVerified\u0027:True,\\n          u\u0027Description\u0027:u\u0027In 2016,\\n          the site dedicated to helping people hack email and online gaming accounts known as Abusewith.us suffered multiple data breaches. The site \u0026lt;a href=\\\"https://krebsonsecurity.com/2017/02/who-ran-leakedsource-com/\\\" target=\\\"_blank\\\" rel=\\\"noopener\\\"\u0026gt;allegedly had an administrator in common with the nefarious LeakedSource site\u0026lt;/a\u0026gt;,\\n          both of which have since been shut down. The exposed data included more than 1.3 million unique email addresses,\\n          often accompanied by usernames,\\n          IP addresses and plain text or hashed passwords retrieved from various sources and intended to be used to compromise the victims\\\\\u0027 accounts.\u0027\\n       }\\n    ]\\n}\\n\\n\u0027\u0027\u0027\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.email_address = artifact.value\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1f0b29z\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1iiee1p\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1f0b29z\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1s5btvn\"/\u003e\u003cserviceTask id=\"ServiceTask_0lvgjwj\" name=\"Have I Been Pwned Get Pastes\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"d448bee5-d85e-484e-a91c-274ebae67123\"\u003e{\"inputs\":{},\"post_processing_script\":\"msg = \\\"Timestamp: \\\" + str(results.metrics[\\\"timestamp\\\"])\\nif results.content[\\\"Pastes\\\"]:\\n  msg = msg + \\\"\\\\nPastes: \\\" + str(len(results.content[\\\"Pastes\\\"]))\\nelse:\\n  msg = msg + \\\"\\\\nNo Pastes\\\"\\n    \\nif artifact.description:\\n  artifact.description = artifact.description.content + \u0027\\\\n\\\\n\u0027 + msg\\nelse:\\n  artifact.description = msg\\n\\n\\n\u0027\u0027\u0027 Example Response\\n{\\n  \\\"Inputs\\\": {\\n    \\\"email_address\\\": \\\"test@email.com\\\"\\n  }, \\n  \\\"Run Time\\\": \\\"2000\\\",\\n  \\\"Pastes\\\":\\n    [  \\n       {  \\n          u\u0027Date\u0027:None,\\n          u\u0027Source\u0027:u\u0027AdHocUrl\u0027,\\n          u\u0027EmailCount\u0027:9893,\\n          u\u0027Id\u0027:      u\u0027http://siph0n.in/exploits.php?id=3670\u0027,\\n          u\u0027Title\u0027:u\u0027siph0n.in\u0027\\n       },\\n       {  \\n          u\u0027Date\u0027:None,\\n          u\u0027Source\u0027:u\u0027AdHocUrl\u0027,\\n          u\u0027EmailCount\u0027:12002,\\n          u\u0027Id\u0027:      u\u0027http://siph0n.in/exploits.php?id=3892\u0027,\\n          u\u0027Title\u0027:u\u0027siph0n.in\u0027\\n       },\\n       {  \\n          u\u0027Date\u0027:None,\\n          u\u0027Source\u0027:u\u0027AdHocUrl\u0027,\\n          u\u0027EmailCount\u0027:99791,\\n          u\u0027Id\u0027:      u\u0027http://siph0n.in/exploits.php?id=4680\u0027,\\n          u\u0027Title\u0027:u\u0027remotestaff.com.au\u0027\\n       }\\n    ]\\n}\\n\u0027\u0027\u0027\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.email_address = artifact.value\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1iiee1p\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0vd0v80\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1iiee1p\" sourceRef=\"ServiceTask_1s5btvn\" targetRef=\"ServiceTask_0lvgjwj\"/\u003e\u003cendEvent id=\"EndEvent_11cg6eu\"\u003e\u003cincoming\u003eSequenceFlow_0vd0v80\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0vd0v80\" sourceRef=\"ServiceTask_0lvgjwj\" targetRef=\"EndEvent_11cg6eu\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1s5btvn\" id=\"ServiceTask_1s5btvn_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"271\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1f0b29z\" id=\"SequenceFlow_1f0b29z_di\"\u003e\u003comgdi:waypoint x=\"198\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"271\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"189.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0lvgjwj\" id=\"ServiceTask_0lvgjwj_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"480\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1iiee1p\" id=\"SequenceFlow_1iiee1p_di\"\u003e\u003comgdi:waypoint x=\"371\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"480\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"425.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_11cg6eu\" id=\"EndEvent_11cg6eu_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"696\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"714\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0vd0v80\" id=\"SequenceFlow_0vd0v80_di\"\u003e\u003comgdi:waypoint x=\"580\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"696\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"638\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 2,
      "description": "",
      "export_key": "have_i_been_pwned_search",
      "last_modified_by": "shresh@example.com",
      "last_modified_time": 1743603992054,
      "name": "Have I Been Pwned Search",
      "object_type": "artifact",
      "programmatic_name": "have_i_been_pwned_search",
      "tags": [],
      "uuid": "267ecb56-3e0d-49c1-a0ae-adaab316b88e",
      "workflow_id": 460
    }
  ],
  "workspaces": []
}
