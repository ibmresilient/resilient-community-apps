{
  "action_order": [],
  "actions": [
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Get Popular Tweets For Specified Tag(s)",
      "id": 509,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Get Popular Tweets For Specified Tag(s)",
      "object_type": "incident",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "37c51048-6431-4844-b88c-9afa2a51b764",
      "view_items": [],
      "workflows": [
        "twitter_most_popular_tweets_for_tag"
      ]
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "case_matching_profiles": [],
  "export_date": 1743762483902,
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
      "export_key": "__function/twitter_search_tweet_string",
      "hide_notification": false,
      "id": 3478,
      "input_type": "textarea",
      "internal": false,
      "is_tracked": false,
      "name": "twitter_search_tweet_string",
      "operation_perms": {},
      "operations": [],
      "placeholder": "{ \"hashtags\":[ \"Malware\"] }",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [
        {
          "id": 30,
          "name": "Botnet, Cybersecurity, Malware",
          "template": {
            "content": "{\n\"hashtags\":[ \"Botnet\", \"Cybersecurity\", \"Malware\"]\n}",
            "format": "text"
          },
          "uuid": "c20e17df-b256-4c43-8f27-bcb15a9d7728"
        },
        {
          "id": 31,
          "name": "Cryptocurrency",
          "template": {
            "content": "{\n\"hashtags\":[ \"Cryptocurrency\"]\n}",
            "format": "text"
          },
          "uuid": "2ba0b515-f1ef-4174-b9ba-aca6e520ee73"
        },
        {
          "id": 32,
          "name": "Malware Most Popular",
          "template": {
            "content": "{\n\"hashtags\":[ \"Malware\"]\n}",
            "format": "text"
          },
          "uuid": "de91e8c6-babd-41be-98ee-43ceb881f57e"
        },
        {
          "id": 33,
          "name": "5 types of Threats",
          "template": {
            "content": "{\n\"hashtags\":[ \"Magecart\", \"Wannacry\", \"Spectre\", \"XFTAS\", \"Emotet\"]\n}",
            "format": "text"
          },
          "uuid": "5aeeb601-c00c-4878-b3dc-6569bde25d9c"
        }
      ],
      "text": "twitter_search_tweet_string",
      "tooltip": "A number of hashtags to query for popular tweets. Input is a JSON Object",
      "type_id": 11,
      "uuid": "d7b41d44-35e9-4c4a-9c79-6c3f0fa6a401",
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
      "export_key": "__function/twitter_search_tweet_count",
      "hide_notification": false,
      "id": 3477,
      "input_type": "number",
      "internal": false,
      "is_tracked": false,
      "name": "twitter_search_tweet_count",
      "operation_perms": {},
      "operations": [],
      "placeholder": "15",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "twitter_search_tweet_count",
      "tooltip": "A number of tweets to be returned by the function. If no value is provided, defaults to 15.",
      "type_id": 11,
      "uuid": "f79a5440-17d2-423b-91ff-f0d0f86db2ce",
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
      "created_date": 1743760873944,
      "description": {
        "content": "A function which targets the Twitter Search API. Takes in an input of a multiple possible hashtags and a number of Tweets to be returned and contacts the Twitter Search API to return the results. Requires Twitter Access Key and Secret to obtain a OAuth2 read-only token.",
        "format": "text"
      },
      "destination_handle": "fn_twitter_most_popular",
      "display_name": "Get Popular Tweets For Specified Tag(s)",
      "export_key": "twitter_most_popular_tweets",
      "id": 342,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 39,
        "name": "shresh@example.com",
        "type": "user"
      },
      "last_modified_time": 1743760873944,
      "name": "twitter_most_popular_tweets",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "tags": [],
      "uuid": "a7f538cf-a07c-4d75-95ec-94c1abaae450",
      "version": 0,
      "view_items": [
        {
          "content": "d7b41d44-35e9-4c4a-9c79-6c3f0fa6a401",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "f79a5440-17d2-423b-91ff-f0d0f86db2ce",
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
          "name": "Example Twitter: Popular Tweets For Tag(s)",
          "object_type": "incident",
          "programmatic_name": "twitter_most_popular_tweets_for_tag",
          "tags": [],
          "uuid": null,
          "workflow_id": 475
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 124,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1743762481606,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1743762481606,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [
        "0bf227a6-8d63-4091-9f8e-ebfc3ec5786b"
      ],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "fn_twitter_most_popular",
      "name": "fn_twitter_most_popular",
      "programmatic_name": "fn_twitter_most_popular",
      "tags": [],
      "users": [
        "shresh@example.com"
      ],
      "uuid": "fca5f277-835e-4905-a0d7-47bc9ca117d8"
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
        "workflow_id": "twitter_most_popular_tweets_for_tag",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"twitter_most_popular_tweets_for_tag\" isExecutable=\"true\" name=\"Example Twitter: Popular Tweets For Tag(s)\"\u003e\u003cdocumentation\u003eAn example workflow which is used to retrieve a number of popular tweets for 1 or more provided tags. Default amount returned is 15 however this is customizable using an input variable. Hard limit is 100. Adds a rich text note to the incident with the retrieved tweets\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0rxcjdt\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_129xub9\" name=\"Get Popular Tweets For Specified ...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"a7f538cf-a07c-4d75-95ec-94c1abaae450\"\u003e{\"inputs\":{\"d7b41d44-35e9-4c4a-9c79-6c3f0fa6a401\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_content_value\":{\"format\":\"text\",\"content\":\"{\\n\\\"hashtags\\\":[ \\\"Magecart\\\", \\\"Wannacry\\\", \\\"Spectre\\\", \\\"XFTAS\\\", \\\"Emotet\\\"]\\n}\"}}},\"f79a5440-17d2-423b-91ff-f0d0f86db2ce\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"number_value\":5}}},\"post_processing_script\":\"\\n\\\"\\\"\\\"\\nExample of the results returned by this workflow.\\n\\nresults = {\\n  success = True,\\n  inputs :{\\n    twitter_search_tweet_string: \u0027{\\\"hashtags\\\":[ \\\"Malware\\\", \\\"Ransomware\\\", \\\"Phishing\\\"]}\u0027,\\n    twitter_search_tweet_count: 10\\n  }\\n  tweets: {\\n    statuses: [{\\n      text: \\\"Hello World\\\",\\n      id_str: \\\"123\\\",\\n      entities: {\\n          urls:[{\\n            url : \\\"https://twitter.com/i/web/status/123\\\"\\n          }]\\n        },\\n        ...OtherAttributes\\n      }\\n    }]\\n  }\\n}\\n\\\"\\\"\\\"\\n\\n#Prepare the start of the note text\\nnoteText = \\\"\\\"\\\"\u0026lt;br\u0026gt;\u0026lt;b\u0026gt;Twitter Search:\u0026lt;/b\u0026gt;\\n                \u0026lt;b\u0026gt;Searched Tags: \u0026lt;/b\u0026gt;{0}\\\"\\\"\\\".format(results[\\\"inputs\\\"][\\\"twitter_search_tweet_string\\\"])\\n\\nif (results.success):\\n  # For each returned tweet add the text and URL of the tweet to the noteText\\n  for tweet in results.tweets[\\\"statuses\\\"]:\\n    noteText += \\\"\\\"\\\"\u0026lt;br\u0026gt;\u0026lt;br\u0026gt;\u0026lt;b\u0026gt;Tweet Text:\u0026lt;/b\u0026gt;\u0026lt;br\u0026gt;{0}\\n    \u0026lt;b\u0026gt;Tweet URL\u0026lt;/b\u0026gt;: \u0026lt;a href=\\\"{1}\\\"\u0026gt;{1}\u0026lt;/a\u0026gt;\\\"\\\"\\\".format(tweet[\\\"full_text\\\"],\\\"https://twitter.com/i/web/status/{0}\\\".format(tweet[\\\"id_str\\\"])) \\nelse:\\n  noteText += \\\"\\\"\\\"\u0026lt;b\u0026gt;No Results found\u0026lt;/b\u0026gt;\\\"\\\"\\\"\\n# Now add the note to our incident\\nincident.addNote(helper.createRichText(noteText))\",\"post_processing_script_language\":\"python3\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0rxcjdt\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0sf9twy\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndEvent_06a1sj2\"\u003e\u003cincoming\u003eSequenceFlow_0sf9twy\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0rxcjdt\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_129xub9\"/\u003e\u003csequenceFlow id=\"SequenceFlow_0sf9twy\" sourceRef=\"ServiceTask_129xub9\" targetRef=\"EndEvent_06a1sj2\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"192\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"187\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"196\" y=\"217\"/\u003e\u003comgdi:waypoint x=\"160\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_129xub9\" id=\"ServiceTask_129xub9_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"419\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_06a1sj2\" id=\"EndEvent_06a1sj2_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"689\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"662\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0rxcjdt\" id=\"SequenceFlow_0rxcjdt_di\"\u003e\u003comgdi:waypoint x=\"228\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"419\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"278.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0sf9twy\" id=\"SequenceFlow_0sf9twy_di\"\u003e\u003comgdi:waypoint x=\"519\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"689\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"559\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 2,
      "description": "An example workflow which is used to retrieve a number of popular tweets for 1 or more provided tags. Default amount returned is 15 however this is customizable using an input variable. Hard limit is 100. Adds a rich text note to the incident with the retrieved tweets",
      "export_key": "twitter_most_popular_tweets_for_tag",
      "last_modified_by": "shresh@example.com",
      "last_modified_time": 1743760955440,
      "name": "Example Twitter: Popular Tweets For Tag(s)",
      "object_type": "incident",
      "programmatic_name": "twitter_most_popular_tweets_for_tag",
      "tags": [],
      "uuid": "e03969a5-4935-4dcd-bc61-c18730f9e350",
      "workflow_id": 475
    }
  ],
  "workspaces": []
}
