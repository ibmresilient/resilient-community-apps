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
      "id": 369,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: ElasticSearch Query from Artifact",
      "object_type": "artifact",
      "tags": [],
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
      "id": 370,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: ElasticSearch Query from Incident",
      "object_type": "incident",
      "tags": [],
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
  "case_matching_profiles": [],
  "export_date": 1744730768137,
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
      "id": 2695,
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
      "tags": [],
      "templates": [
        {
          "id": 23,
          "name": "match_term_sorted",
          "template": {
            "content": "{\n    \"sort\" : [\n        { \"\u003cSORT_VALUE\u003e\" : \"desc\" }\n    ],\n    \"query\" : {\n        \"term\" : \u003cTERM_TO_BE_SEARCHED\u003e\n    }\n}",
            "format": "text"
          },
          "uuid": "24a3191b-d1b3-41b1-99c0-1d2290ba36ed"
        },
        {
          "id": 24,
          "name": "match_all",
          "template": {
            "content": "{\n    \"query\": {\n        \"match_all\": {}\n    }\n}",
            "format": "text"
          },
          "uuid": "2457c8d0-2b19-4756-9a1a-4e641069d239"
        },
        {
          "id": 25,
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
      "id": 2696,
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
      "tags": [],
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
      "id": 2697,
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
      "tags": [],
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
      "created_date": 1741351006998,
      "description": {
        "content": "A function that allows a user to query a specified ElasticSearch datastore for data.",
        "format": "text"
      },
      "destination_handle": "fn_elasticsearch",
      "display_name": "ElasticSearch Utilities: Query",
      "export_key": "fn_elasticsearch_query",
      "id": 247,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 39,
        "name": "shresh@example.com",
        "type": "user"
      },
      "last_modified_time": 1741351006998,
      "name": "fn_elasticsearch_query",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "output_json_example": "{\"inputs\": {\"es_query\": \"{\\\"query\\\": {\\\"match_all\\\": {}}}\", \"es_doc_type\": null, \"es_index\": null}, \"query_results\": [{\"_index\": \".ds-logs-app_search.analytics-default-2022.06.23-000001\", \"_id\": \"kS_ekIEBTwR1htd9OD_f\", \"_score\": 1.0, \"_source\": {\"@timestamp\": \"2022-06-23T14:01:30.224Z\", \"data_stream\": {\"type\": \"logs\", \"dataset\": \"app_search.analytics\", \"namespace\": \"default\"}, \"event\": {\"document_ids\": [\"park_rocky-mountain\"], \"tags\": [], \"dataset\": \"app-search-analytics\", \"category\": \"app-search-analytics\", \"action\": \"loco_moco_search\", \"created\": \"2022-06-23T14:01:30Z\", \"query_string\": \"rocky\", \"loco_moco_search_request_id\": \"6sHMDt44SGG_V-p11TXUyw\"}, \"log\": {\"offset\": 58011, \"file\": {\"path\": \"/app/logs/filebeat.log\"}}, \"input\": {\"type\": \"log\"}, \"related\": {\"ip\": \"129.41.46.6\"}, \"ecs\": {\"version\": \"1.7.0\"}, \"labels\": {\"engine_id\": \"62b326c9d0164ee8e257b729\", \"lm_account_id\": \"62b2f277d0164e239457b719\", \"index_date\": \"2022.06.23\"}, \"agent\": {\"ephemeral_id\": \"1ac55df2-51a2-4756-b50e-a4fa638ab155\", \"id\": \"19cfd1c7-99c3-461b-97e2-fd1a1e9e50fa\", \"name\": \"9ee8fac8927c\", \"type\": \"filebeat\", \"version\": \"7.15.1\", \"hostname\": \"9ee8fac8927c\"}, \"host\": {\"name\": \"9ee8fac8927c\"}}}, {\"_index\": \".ds-logs-app_search.analytics-default-2022.06.23-000001\", \"_id\": \"DJXekIEBhfwfcOFNGY18\", \"_score\": 1.0, \"_source\": {\"@timestamp\": \"2022-06-23T14:01:21.239Z\", \"data_stream\": {\"dataset\": \"app_search.analytics\", \"namespace\": \"default\", \"type\": \"logs\"}, \"log\": {\"offset\": 51948, \"file\": {\"path\": \"/app/logs/filebeat.log\"}}, \"input\": {\"type\": \"log\"}, \"host\": {\"name\": \"9ee8fac8927c\"}, \"agent\": {\"hostname\": \"9ee8fac8927c\", \"ephemeral_id\": \"1ac55df2-51a2-4756-b50e-a4fa638ab155\", \"id\": \"19cfd1c7-99c3-461b-97e2-fd1a1e9e50fa\", \"name\": \"9ee8fac8927c\", \"type\": \"filebeat\", \"version\": \"7.15.1\"}, \"event\": {\"dataset\": \"app-search-analytics\", \"category\": \"app-search-analytics\", \"action\": \"loco_moco_search\", \"created\": \"2022-06-23T14:01:21Z\", \"query_string\": \"1075.6\", \"loco_moco_search_request_id\": \"f7z0me0oSeGuUArcVdl9xw\", \"document_ids\": [\"park_rocky-mountain\"], \"tags\": []}, \"ecs\": {\"version\": \"1.7.0\"}, \"labels\": {\"lm_account_id\": \"62b2f277d0164e239457b719\", \"index_date\": \"2022.06.23\", \"engine_id\": \"62b326c9d0164ee8e257b729\"}, \"related\": {\"ip\": \"129.41.46.6\"}}}, {\"_index\": \".ds-logs-app_search.analytics-default-2022.06.23-000001\", \"_id\": \"CpXdkIEBhfwfcOFN5o2w\", \"_score\": 1.0, \"_source\": {\"@timestamp\": \"2022-06-23T14:01:09.381Z\", \"log\": {\"offset\": 47924, \"file\": {\"path\": \"/app/logs/filebeat.log\"}}, \"labels\": {\"index_date\": \"2022.06.23\", \"engine_id\": \"62b326c9d0164ee8e257b729\", \"lm_account_id\": \"62b2f277d0164e239457b719\"}, \"related\": {\"ip\": \"129.41.46.6\"}, \"data_stream\": {\"type\": \"logs\", \"dataset\": \"app_search.analytics\", \"namespace\": \"default\"}, \"event\": {\"tags\": [], \"dataset\": \"app-search-analytics\", \"category\": \"app-search-analytics\", \"action\": \"loco_moco_search\", \"created\": \"2022-06-23T14:01:09Z\", \"query_string\": \"visitors\", \"loco_moco_search_request_id\": \"0DzSQoi5Rz6AwUpa92pp2g\", \"document_ids\": []}, \"ecs\": {\"version\": \"1.7.0\"}, \"input\": {\"type\": \"log\"}, \"host\": {\"name\": \"9ee8fac8927c\"}, \"agent\": {\"id\": \"19cfd1c7-99c3-461b-97e2-fd1a1e9e50fa\", \"name\": \"9ee8fac8927c\", \"type\": \"filebeat\", \"version\": \"7.15.1\", \"hostname\": \"9ee8fac8927c\", \"ephemeral_id\": \"1ac55df2-51a2-4756-b50e-a4fa638ab155\"}}}, {\"_index\": \".ds-logs-app_search.analytics-default-2022.06.23-000001\", \"_id\": \"BZXdkIEBhfwfcOFNx43x\", \"_score\": 1.0, \"_source\": {\"@timestamp\": \"2022-06-23T14:00:54.697Z\", \"related\": {\"ip\": \"129.41.46.6\"}, \"log\": {\"offset\": 38434, \"file\": {\"path\": \"/app/logs/filebeat.log\"}}, \"event\": {\"action\": \"loco_moco_search\", \"created\": \"2022-06-23T14:00:54Z\", \"query_string\": \"\", \"loco_moco_search_request_id\": \"ODdo8JlDToePy0C-iebv-A\", \"document_ids\": [\"park_rocky-mountain\", \"park_saguaro\"], \"tags\": [], \"dataset\": \"app-search-analytics\", \"category\": \"app-search-analytics\"}, \"labels\": {\"index_date\": \"2022.06.23\", \"engine_id\": \"62b326c9d0164ee8e257b729\", \"lm_account_id\": \"62b2f277d0164e239457b719\"}, \"ecs\": {\"version\": \"1.7.0\"}, \"input\": {\"type\": \"log\"}, \"host\": {\"name\": \"9ee8fac8927c\"}, \"agent\": {\"id\": \"19cfd1c7-99c3-461b-97e2-fd1a1e9e50fa\", \"name\": \"9ee8fac8927c\", \"type\": \"filebeat\", \"version\": \"7.15.1\", \"hostname\": \"9ee8fac8927c\", \"ephemeral_id\": \"1ac55df2-51a2-4756-b50e-a4fa638ab155\"}, \"data_stream\": {\"type\": \"logs\", \"dataset\": \"app_search.analytics\", \"namespace\": \"default\"}}}, {\"_index\": \".ds-logs-enterprise_search.api-default-2022.06.22-000001\", \"_id\": \"ki_ekIEBTwR1htd9OD_f\", \"_score\": 1.0, \"_ignored\": [\"http.response.body.content\"], \"_source\": {\"@timestamp\": \"2022-06-23T14:01:30.226Z\", \"data_stream\": {\"dataset\": \"enterprise_search.api\", \"namespace\": \"default\", \"type\": \"logs\"}, \"labels\": {\"engine_id\": \"62b326c9d0164ee8e257b729\", \"lm_account_id\": \"62b2f277d0164e239457b719\", \"index_date\": \"2022.06.23\", \"env\": \"togo_production\"}, \"url\": {\"original\": \"/api/as/v1/engines/mysearchengine/search.json\"}, \"ecs\": {\"version\": \"1.7.0\"}, \"log\": {\"offset\": 58584, \"file\": {\"path\": \"/app/logs/filebeat.log\"}}, \"duration\": 69.342, \"http\": {\"response\": {\"status_code\": 200, \"body\": {\"bytes\": 1566, \"content\": \"{\\\"meta\\\":{\\\"alerts\\\":[],\\\"warnings\\\":[],\\\"precision\\\":2,\\\"engine\\\":{\\\"name\\\":\\\"mysearchengine\\\",\\\"type\\\":\\\"default\\\"},\\\"page\\\":{\\\"current\\\":1,\\\"total_pages\\\":1,\\\"total_results\\\":1,\\\"size\\\":20},\\\"request_id\\\":\\\"6sHMDt44SGG_V-p11TXUyw\\\"},\\\"results\\\":[{\\\"visitors\\\":{\\\"raw\\\":\\\"4517585\\\",\\\"snippet\\\":\\\"4517585\\\"},\\\"square_km\\\":{\\\"raw\\\":\\\"1075.6\\\",\\\"snippet\\\":\\\"1075.6\\\"},\\\"world_heritage_site\\\":{\\\"raw\\\":\\\"false\\\",\\\"snippet\\\":\\\"false\\\"},\\\"date_established\\\":{\\\"raw\\\":\\\"1915-01-26T06:00:00Z\\\",\\\"snippet\\\":\\\"1915-01-26T06:00:00Z\\\"},\\\"description\\\":{\\\"raw\\\":\\\"Bisected north to south by the Continental Divide, this portion of the Rockies has ecosystems varying from over 150 riparian lakes to montane and subalpine forests to treeless alpine tundra. Wildlife including mule deer, bighorn sheep, black bears, and cougars inhabit its igneous mountains and glacial valleys. Longs Peak, a classic Colorado fourteener, and the scenic Bear Lake are popular destinations, as well as the historic Trail Ridge Road, which reaches an elevation of more than 12,000 feet (3,700 m).\\\",\\\"snippet\\\":\\\"Bisected north to south by the Continental Divide, this portion of the \u003cem\u003eRockies\u003c/em\u003e has ecosystems\\\"},\\\"location\\\":{\\\"raw\\\":\\\"40.4,-105.58\\\",\\\"snippet\\\":\\\"40.4,-105.58\\\"},\\\"acres\\\":{\\\"raw\\\":\\\"265795.2\\\",\\\"snippet\\\":\\\"265795.2\\\"},\\\"_meta\\\":{\\\"id\\\":\\\"park_rocky-mountain\\\",\\\"engine\\\":\\\"mysearchengine\\\",\\\"score\\\":0.3164503},\\\"id\\\":{\\\"raw\\\":\\\"park_rocky-mountain\\\",\\\"snippet\\\":null},\\\"title\\\":{\\\"raw\\\":\\\"Rocky Mountain\\\",\\\"snippet\\\":\\\"\u003cem\u003eRocky\u003c/em\u003e Mountain\\\"},\\\"nps_link\\\":{\\\"raw\\\":\\\"https://www.nps.gov/romo/index.htm\\\",\\\"snippet\\\":\\\"https://www.nps.gov/romo/index.htm\\\"},\\\"states\\\":{\\\"raw\\\":[\\\"Colorado\\\"],\\\"snippet\\\":\\\"Colorado\\\"}}]}\"}}, \"request\": {\"body\": {\"bytes\": 746, \"content\": \"{\\\"query\\\":\\\"rocky\\\",\\\"result_fields\\\":{\\\"visitors\\\":{\\\"raw\\\":{},\\\"snippet\\\":{\\\"size\\\":100,\\\"fallback\\\":true}},\\\"square_km\\\":{\\\"raw\\\":{},\\\"snippet\\\":{\\\"size\\\":100,\\\"fallback\\\":true}},\\\"world_heritage_site\\\":{\\\"raw\\\":{},\\\"snippet\\\":{\\\"size\\\":100,\\\"fallback\\\":true}},\\\"date_established\\\":{\\\"raw\\\":{},\\\"snippet\\\":{\\\"size\\\":100,\\\"fallback\\\":true}},\\\"description\\\":{\\\"raw\\\":{},\\\"snippet\\\":{\\\"size\\\":100,\\\"fallback\\\":true}},\\\"location\\\":{\\\"raw\\\":{},\\\"snippet\\\":{\\\"size\\\":100,\\\"fallback\\\":true}},\\\"acres\\\":{\\\"raw\\\":{},\\\"snippet\\\":{\\\"size\\\":100,\\\"fallback\\\":true}},\\\"title\\\":{\\\"raw\\\":{},\\\"snippet\\\":{\\\"size\\\":100,\\\"fallback\\\":true}},\\\"nps_link\\\":{\\\"raw\\\":{},\\\"snippet\\\":{\\\"size\\\":100,\\\"fallback\\\":true}},\\\"states\\\":{\\\"raw\\\":{},\\\"snippet\\\":{\\\"size\\\":100,\\\"fallback\\\":true}},\\\"id\\\":{\\\"raw\\\":{},\\\"snippet\\\":{\\\"size\\\":100,\\\"fallback\\\":true}}},\\\"page\\\":{\\\"size\\\":20,\\\"current\\\":1}}\"}, \"method\": \"POST\"}}, \"user_agent\": {\"original\": \"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:101.0) Gecko/20100101 Firefox/101.0\"}, \"event\": {\"dataset\": \"api\"}, \"input\": {\"type\": \"log\"}, \"host\": {\"name\": \"9ee8fac8927c\"}, \"agent\": {\"type\": \"filebeat\", \"version\": \"7.15.1\", \"hostname\": \"9ee8fac8927c\", \"ephemeral_id\": \"1ac55df2-51a2-4756-b50e-a4fa638ab155\", \"id\": \"19cfd1c7-99c3-461b-97e2-fd1a1e9e50fa\", \"name\": \"9ee8fac8927c\"}}}, {\"_index\": \".ds-logs-enterprise_search.api-default-2022.06.22-000001\", \"_id\": \"jy_ekIEBTwR1htd9ND_X\", \"_score\": 1.0, \"_source\": {\"@timestamp\": \"2022-06-23T14:01:27.808Z\", \"duration\": 54.267999999999994, \"data_stream\": {\"dataset\": \"enterprise_search.api\", \"namespace\": \"default\", \"type\": \"logs\"}, \"input\": {\"type\": \"log\"}, \"host\": {\"name\": \"9ee8fac8927c\"}, \"agent\": {\"ephemeral_id\": \"1ac55df2-51a2-4756-b50e-a4fa638ab155\", \"id\": \"19cfd1c7-99c3-461b-97e2-fd1a1e9e50fa\", \"name\": \"9ee8fac8927c\", \"type\": \"filebeat\", \"version\": \"7.15.1\", \"hostname\": \"9ee8fac8927c\"}, \"url\": {\"original\": \"/api/as/v1/engines/mysearchengine/query_suggestion\"}, \"labels\": {\"engine_id\": \"62b326c9d0164ee8e257b729\", \"lm_account_id\": \"62b2f277d0164e239457b719\", \"index_date\": \"2022.06.23\", \"env\": \"togo_production\"}, \"event\": {\"dataset\": \"api\"}, \"http\": {\"response\": {\"status_code\": 200, \"body\": {\"content\": \"{\\\"results\\\":{\\\"documents\\\":[{\\\"suggestion\\\":\\\"rocky\\\"},{\\\"suggestion\\\":\\\"rocky mountain\\\"},{\\\"suggestion\\\":\\\"rockies\\\"},{\\\"suggestion\\\":\\\"rockies has\\\"},{\\\"suggestion\\\":\\\"rockies has ecosystems\\\"},{\\\"suggestion\\\":\\\"rockies has ecosystems varying\\\"},{\\\"suggestion\\\":\\\"road\\\"},{\\\"suggestion\\\":\\\"road which\\\"},{\\\"suggestion\\\":\\\"road which reaches\\\"},{\\\"suggestion\\\":\\\"road which reaches an\\\"}]},\\\"meta\\\":{\\\"request_id\\\":\\\"5ixNmg-eRBOpROFbkcng1A\\\"}}\", \"bytes\": 396}}, \"request\": {\"body\": {\"bytes\": 14, \"content\": \"{\\\"query\\\":\\\"ro\\\"}\"}, \"method\": \"POST\"}}, \"ecs\": {\"version\": \"1.7.0\"}, \"log\": {\"file\": {\"path\": \"/app/logs/filebeat.log\"}, \"offset\": 55816}, \"user_agent\": {\"original\": \"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:101.0) Gecko/20100101 Firefox/101.0\"}}}, {\"_index\": \".ds-logs-enterprise_search.api-default-2022.06.22-000001\", \"_id\": \"kC_ekIEBTwR1htd9ND_X\", \"_score\": 1.0, \"_source\": {\"@timestamp\": \"2022-06-23T14:01:28.166Z\", \"data_stream\": {\"type\": \"logs\", \"dataset\": \"enterprise_search.api\", \"namespace\": \"default\"}, \"labels\": {\"env\": \"togo_production\", \"engine_id\": \"62b326c9d0164ee8e257b729\", \"lm_account_id\": \"62b2f277d0164e239457b719\", \"index_date\": \"2022.06.23\"}, \"log\": {\"offset\": 56989, \"file\": {\"path\": \"/app/logs/filebeat.log\"}}, \"event\": {\"dataset\": \"api\"}, \"duration\": 53.344, \"input\": {\"type\": \"log\"}, \"ecs\": {\"version\": \"1.7.0\"}, \"url\": {\"original\": \"/api/as/v1/engines/mysearchengine/query_suggestion\"}, \"http\": {\"request\": {\"body\": {\"bytes\": 16, \"content\": \"{\\\"query\\\":\\\"rock\\\"}\"}, \"method\": \"POST\"}, \"response\": {\"status_code\": 200, \"body\": {\"bytes\": 271, \"content\": \"{\\\"results\\\":{\\\"documents\\\":[{\\\"suggestion\\\":\\\"rocky\\\"},{\\\"suggestion\\\":\\\"rocky mountain\\\"},{\\\"suggestion\\\":\\\"rockies\\\"},{\\\"suggestion\\\":\\\"rockies has\\\"},{\\\"suggestion\\\":\\\"rockies has ecosystems\\\"},{\\\"suggestion\\\":\\\"rockies has ecosystems varying\\\"}]},\\\"meta\\\":{\\\"request_id\\\":\\\"ITkIgipWQoecfVnEcUEebw\\\"}}\"}}}, \"user_agent\": {\"original\": \"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:101.0) Gecko/20100101 Firefox/101.0\"}, \"host\": {\"name\": \"9ee8fac8927c\"}, \"agent\": {\"type\": \"filebeat\", \"version\": \"7.15.1\", \"hostname\": \"9ee8fac8927c\", \"ephemeral_id\": \"1ac55df2-51a2-4756-b50e-a4fa638ab155\", \"id\": \"19cfd1c7-99c3-461b-97e2-fd1a1e9e50fa\", \"name\": \"9ee8fac8927c\"}}}, {\"_index\": \".ds-logs-enterprise_search.api-default-2022.06.22-000001\", \"_id\": \"DZXekIEBhfwfcOFNGY18\", \"_score\": 1.0, \"_ignored\": [\"http.response.body.content\"], \"_source\": {\"@timestamp\": \"2022-06-23T14:01:21.242Z\", \"user_agent\": {\"original\": \"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:101.0) Gecko/20100101 Firefox/101.0\"}, \"ecs\": {\"version\": \"1.7.0\"}, \"data_stream\": {\"type\": \"logs\", \"dataset\": \"enterprise_search.api\", \"namespace\": \"default\"}, \"duration\": 99.428, \"agent\": {\"id\": \"19cfd1c7-99c3-461b-97e2-fd1a1e9e50fa\", \"name\": \"9ee8fac8927c\", \"type\": \"filebeat\", \"version\": \"7.15.1\", \"hostname\": \"9ee8fac8927c\", \"ephemeral_id\": \"1ac55df2-51a2-4756-b50e-a4fa638ab155\"}, \"labels\": {\"engine_id\": \"62b326c9d0164ee8e257b729\", \"lm_account_id\": \"62b2f277d0164e239457b719\", \"index_date\": \"2022.06.23\", \"env\": \"togo_production\"}, \"http\": {\"request\": {\"body\": {\"bytes\": 747, \"content\": \"{\\\"query\\\":\\\"1075.6\\\",\\\"result_fields\\\":{\\\"visitors\\\":{\\\"raw\\\":{},\\\"snippet\\\":{\\\"size\\\":100,\\\"fallback\\\":true}},\\\"square_km\\\":{\\\"raw\\\":{},\\\"snippet\\\":{\\\"size\\\":100,\\\"fallback\\\":true}},\\\"world_heritage_site\\\":{\\\"raw\\\":{},\\\"snippet\\\":{\\\"size\\\":100,\\\"fallback\\\":true}},\\\"date_established\\\":{\\\"raw\\\":{},\\\"snippet\\\":{\\\"size\\\":100,\\\"fallback\\\":true}},\\\"description\\\":{\\\"raw\\\":{},\\\"snippet\\\":{\\\"size\\\":100,\\\"fallback\\\":true}},\\\"location\\\":{\\\"raw\\\":{},\\\"snippet\\\":{\\\"size\\\":100,\\\"fallback\\\":true}},\\\"acres\\\":{\\\"raw\\\":{},\\\"snippet\\\":{\\\"size\\\":100,\\\"fallback\\\":true}},\\\"title\\\":{\\\"raw\\\":{},\\\"snippet\\\":{\\\"size\\\":100,\\\"fallback\\\":true}},\\\"nps_link\\\":{\\\"raw\\\":{},\\\"snippet\\\":{\\\"size\\\":100,\\\"fallback\\\":true}},\\\"states\\\":{\\\"raw\\\":{},\\\"snippet\\\":{\\\"size\\\":100,\\\"fallback\\\":true}},\\\"id\\\":{\\\"raw\\\":{},\\\"snippet\\\":{\\\"size\\\":100,\\\"fallback\\\":true}}},\\\"page\\\":{\\\"size\\\":20,\\\"current\\\":1}}\"}, \"method\": \"POST\"}, \"response\": {\"body\": {\"bytes\": 1557, \"content\": \"{\\\"meta\\\":{\\\"alerts\\\":[],\\\"warnings\\\":[],\\\"precision\\\":2,\\\"engine\\\":{\\\"name\\\":\\\"mysearchengine\\\",\\\"type\\\":\\\"default\\\"},\\\"page\\\":{\\\"current\\\":1,\\\"total_pages\\\":1,\\\"total_results\\\":1,\\\"size\\\":20},\\\"request_id\\\":\\\"f7z0me0oSeGuUArcVdl9xw\\\"},\\\"results\\\":[{\\\"visitors\\\":{\\\"raw\\\":\\\"4517585\\\",\\\"snippet\\\":\\\"4517585\\\"},\\\"square_km\\\":{\\\"raw\\\":\\\"1075.6\\\",\\\"snippet\\\":\\\"\u003cem\u003e1075.6\u003c/em\u003e\\\"},\\\"world_heritage_site\\\":{\\\"raw\\\":\\\"false\\\",\\\"snippet\\\":\\\"false\\\"},\\\"date_established\\\":{\\\"raw\\\":\\\"1915-01-26T06:00:00Z\\\",\\\"snippet\\\":\\\"1915-01-26T06:00:00Z\\\"},\\\"description\\\":{\\\"raw\\\":\\\"Bisected north to south by the Continental Divide, this portion of the Rockies has ecosystems varying from over 150 riparian lakes to montane and subalpine forests to treeless alpine tundra. Wildlife including mule deer, bighorn sheep, black bears, and cougars inhabit its igneous mountains and glacial valleys. Longs Peak, a classic Colorado fourteener, and the scenic Bear Lake are popular destinations, as well as the historic Trail Ridge Road, which reaches an elevation of more than 12,000 feet (3,700 m).\\\",\\\"snippet\\\":\\\"Bisected north to south by the Continental Divide, this portion of the Rockies has ecosystems\\\"},\\\"location\\\":{\\\"raw\\\":\\\"40.4,-105.58\\\",\\\"snippet\\\":\\\"40.4,-105.58\\\"},\\\"acres\\\":{\\\"raw\\\":\\\"265795.2\\\",\\\"snippet\\\":\\\"265795.2\\\"},\\\"_meta\\\":{\\\"id\\\":\\\"park_rocky-mountain\\\",\\\"engine\\\":\\\"mysearchengine\\\",\\\"score\\\":0.4284949},\\\"id\\\":{\\\"raw\\\":\\\"park_rocky-mountain\\\",\\\"snippet\\\":null},\\\"title\\\":{\\\"raw\\\":\\\"Rocky Mountain\\\",\\\"snippet\\\":\\\"Rocky Mountain\\\"},\\\"nps_link\\\":{\\\"raw\\\":\\\"https://www.nps.gov/romo/index.htm\\\",\\\"snippet\\\":\\\"https://www.nps.gov/romo/index.htm\\\"},\\\"states\\\":{\\\"raw\\\":[\\\"Colorado\\\"],\\\"snippet\\\":\\\"Colorado\\\"}}]}\"}, \"status_code\": 200}}, \"log\": {\"offset\": 52522, \"file\": {\"path\": \"/app/logs/filebeat.log\"}}, \"url\": {\"original\": \"/api/as/v1/engines/mysearchengine/search.json\"}, \"event\": {\"dataset\": \"api\"}, \"input\": {\"type\": \"log\"}, \"host\": {\"name\": \"9ee8fac8927c\"}}}, {\"_index\": \".ds-logs-enterprise_search.api-default-2022.06.22-000001\", \"_id\": \"ji_ekIEBTwR1htd9DT_L\", \"_score\": 1.0, \"_source\": {\"@timestamp\": \"2022-06-23T14:01:19.294Z\", \"host\": {\"name\": \"9ee8fac8927c\"}, \"user_agent\": {\"original\": \"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:101.0) Gecko/20100101 Firefox/101.0\"}, \"ecs\": {\"version\": \"1.7.0\"}, \"http\": {\"request\": {\"body\": {\"bytes\": 14, \"content\": \"{\\\"query\\\":\\\"10\\\"}\"}, \"method\": \"POST\"}, \"response\": {\"body\": {\"bytes\": 98, \"content\": \"{\\\"results\\\":{\\\"documents\\\":[{\\\"suggestion\\\":\\\"1075.6\\\"}]},\\\"meta\\\":{\\\"request_id\\\":\\\"w239VO6iTTmdeDtNSWUR2w\\\"}}\"}, \"status_code\": 200}}, \"url\": {\"original\": \"/api/as/v1/engines/mysearchengine/query_suggestion\"}, \"labels\": {\"index_date\": \"2022.06.23\", \"env\": \"togo_production\", \"engine_id\": \"62b326c9d0164ee8e257b729\", \"lm_account_id\": \"62b2f277d0164e239457b719\"}, \"log\": {\"offset\": 51122, \"file\": {\"path\": \"/app/logs/filebeat.log\"}}, \"input\": {\"type\": \"log\"}, \"agent\": {\"hostname\": \"9ee8fac8927c\", \"ephemeral_id\": \"1ac55df2-51a2-4756-b50e-a4fa638ab155\", \"id\": \"19cfd1c7-99c3-461b-97e2-fd1a1e9e50fa\", \"name\": \"9ee8fac8927c\", \"type\": \"filebeat\", \"version\": \"7.15.1\"}, \"data_stream\": {\"type\": \"logs\", \"dataset\": \"enterprise_search.api\", \"namespace\": \"default\"}, \"duration\": 56.539, \"event\": {\"dataset\": \"api\"}}}, {\"_index\": \".ds-logs-enterprise_search.api-default-2022.06.22-000001\", \"_id\": \"CZXdkIEBhfwfcOFN5o2w\", \"_score\": 1.0, \"_source\": {\"@timestamp\": \"2022-06-23T14:01:09.340Z\", \"event\": {\"dataset\": \"api\"}, \"ecs\": {\"version\": \"1.7.0\"}, \"duration\": 44.017, \"input\": {\"type\": \"log\"}, \"url\": {\"original\": \"/api/as/v1/engines/mysearchengine/query_suggestion\"}, \"user_agent\": {\"original\": \"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:101.0) Gecko/20100101 Firefox/101.0\"}, \"labels\": {\"engine_id\": \"62b326c9d0164ee8e257b729\", \"lm_account_id\": \"62b2f277d0164e239457b719\", \"index_date\": \"2022.06.23\", \"env\": \"togo_production\"}, \"log\": {\"offset\": 47119, \"file\": {\"path\": \"/app/logs/filebeat.log\"}}, \"host\": {\"name\": \"9ee8fac8927c\"}, \"data_stream\": {\"namespace\": \"default\", \"type\": \"logs\", \"dataset\": \"enterprise_search.api\"}, \"http\": {\"request\": {\"body\": {\"bytes\": 20, \"content\": \"{\\\"query\\\":\\\"visitors\\\"}\"}, \"method\": \"POST\"}, \"response\": {\"status_code\": 200, \"body\": {\"content\": \"{\\\"results\\\":{\\\"documents\\\":[]},\\\"meta\\\":{\\\"request_id\\\":\\\"pEOgQDCxSAqxkiNEFvRUCw\\\"}}\", \"bytes\": 75}}}, \"agent\": {\"id\": \"19cfd1c7-99c3-461b-97e2-fd1a1e9e50fa\", \"name\": \"9ee8fac8927c\", \"type\": \"filebeat\", \"version\": \"7.15.1\", \"hostname\": \"9ee8fac8927c\", \"ephemeral_id\": \"1ac55df2-51a2-4756-b50e-a4fa638ab155\"}}}], \"success\": true, \"matched_records\": {\"value\": 10000, \"relation\": \"gte\"}, \"returned_records\": 10}",
      "output_json_schema": "{\"$schema\": \"http://json-schema.org/draft-06/schema\", \"type\": \"object\", \"properties\": {\"inputs\": {\"type\": \"object\", \"properties\": {\"es_query\": {\"type\": \"string\"}, \"es_doc_type\": {}, \"es_index\": {}}}, \"query_results\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"properties\": {\"_index\": {\"type\": \"string\"}, \"_id\": {\"type\": \"string\"}, \"_score\": {\"type\": \"number\"}, \"_source\": {\"type\": \"object\", \"properties\": {\"@timestamp\": {\"type\": \"string\"}, \"data_stream\": {\"type\": \"object\", \"properties\": {\"type\": {\"type\": \"string\"}, \"dataset\": {\"type\": \"string\"}, \"namespace\": {\"type\": \"string\"}}}, \"event\": {\"type\": \"object\", \"properties\": {\"document_ids\": {\"type\": \"array\", \"items\": {\"type\": \"string\"}}, \"tags\": {\"type\": \"array\"}, \"dataset\": {\"type\": \"string\"}, \"category\": {\"type\": \"string\"}, \"action\": {\"type\": \"string\"}, \"created\": {\"type\": \"string\"}, \"query_string\": {\"type\": \"string\"}, \"loco_moco_search_request_id\": {\"type\": \"string\"}}}, \"log\": {\"type\": \"object\", \"properties\": {\"offset\": {\"type\": \"integer\"}, \"file\": {\"type\": \"object\", \"properties\": {\"path\": {\"type\": \"string\"}}}}}, \"input\": {\"type\": \"object\", \"properties\": {\"type\": {\"type\": \"string\"}}}, \"related\": {\"type\": \"object\", \"properties\": {\"ip\": {\"type\": \"string\"}}}, \"ecs\": {\"type\": \"object\", \"properties\": {\"version\": {\"type\": \"string\"}}}, \"labels\": {\"type\": \"object\", \"properties\": {\"engine_id\": {\"type\": \"string\"}, \"lm_account_id\": {\"type\": \"string\"}, \"index_date\": {\"type\": \"string\"}, \"env\": {\"type\": \"string\"}}}, \"agent\": {\"type\": \"object\", \"properties\": {\"ephemeral_id\": {\"type\": \"string\"}, \"id\": {\"type\": \"string\"}, \"name\": {\"type\": \"string\"}, \"type\": {\"type\": \"string\"}, \"version\": {\"type\": \"string\"}, \"hostname\": {\"type\": \"string\"}}}, \"host\": {\"type\": \"object\", \"properties\": {\"name\": {\"type\": \"string\"}}}, \"url\": {\"type\": \"object\", \"properties\": {\"original\": {\"type\": \"string\"}}}, \"duration\": {\"type\": \"number\"}, \"http\": {\"type\": \"object\", \"properties\": {\"response\": {\"type\": \"object\", \"properties\": {\"status_code\": {\"type\": \"integer\"}, \"body\": {\"type\": \"object\", \"properties\": {\"bytes\": {\"type\": \"integer\"}, \"content\": {\"type\": \"string\"}}}}}, \"request\": {\"type\": \"object\", \"properties\": {\"body\": {\"type\": \"object\", \"properties\": {\"bytes\": {\"type\": \"integer\"}, \"content\": {\"type\": \"string\"}}}, \"method\": {\"type\": \"string\"}}}}}, \"user_agent\": {\"type\": \"object\", \"properties\": {\"original\": {\"type\": \"string\"}}}}}, \"_ignored\": {\"type\": \"array\", \"items\": {\"type\": \"string\"}}}}}, \"success\": {\"type\": \"boolean\"}, \"matched_records\": {\"type\": \"object\", \"properties\": {\"value\": {\"type\": \"integer\"}, \"relation\": {\"type\": \"string\"}}}, \"returned_records\": {\"type\": \"integer\"}}}",
      "tags": [],
      "uuid": "4f103490-595d-4ab9-ba30-8202c8ddfe9d",
      "version": 0,
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
          "tags": [],
          "uuid": null,
          "workflow_id": 334
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: ElasticSearch Query from Incident",
          "object_type": "incident",
          "programmatic_name": "example_elasticsearch_query_from_incident",
          "tags": [],
          "uuid": null,
          "workflow_id": 335
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 144,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1744730765163,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1744730765163,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [
        "7455ef9b-15dc-4673-966b-ded8cc186f46"
      ],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "fn_elasticsearch",
      "name": "fn_elasticsearch",
      "programmatic_name": "fn_elasticsearch",
      "tags": [],
      "users": [
        "shresh@example.com"
      ],
      "uuid": "28e2e8a2-ea65-430b-abc3-48d2bb3d60db"
    }
  ],
  "notifications": null,
  "overrides": null,
  "phases": [],
  "playbooks": [
    {
      "activation_type": "manual",
      "content": {
        "content_version": 13,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_1f224b3c_8c62_4935_b4b2_f13b8e3b2d6b\" isExecutable=\"true\" name=\"playbook_1f224b3c_8c62_4935_b4b2_f13b8e3b2d6b\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_0uq1ypa\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"ElasticSearch Utilities: Query\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"4f103490-595d-4ab9-ba30-8202c8ddfe9d\"\u003e{\"inputs\":{\"1e041775-c9ba-43ae-a8cf-3f4dda9a0681\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"eed55443-7d80-4451-b275-31f2e09c3a84\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"b92cc3ed-2878-4630-81a7-5830780fa5d9\":{\"expression_input\":{\"expression\":\"artifact.value\"},\"input_type\":\"expression\"}},\"result_name\":\"results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0uq1ypa\u003c/incoming\u003e\u003coutgoing\u003eFlow_1jfa4dy\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_0uq1ypa\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003cscriptTask id=\"ScriptTask_2\" name=\"Elastic Search Results\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"4b9716b7-53c8-411b-9aab-db0196ac422c\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1jfa4dy\u003c/incoming\u003e\u003coutgoing\u003eFlow_0kxingk\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_1jfa4dy\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_2\"/\u003e\u003cendEvent id=\"EndPoint_3\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_0kxingk\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_0kxingk\" sourceRef=\"ScriptTask_2\" targetRef=\"EndPoint_3\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_1f224b3c_8c62_4935_b4b2_f13b8e3b2d6b\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0kxingk\" id=\"Flow_0kxingk_di\"\u003e\u003comgdi:waypoint x=\"1050\" y=\"592\"/\u003e\u003comgdi:waypoint x=\"1050\" y=\"674\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1jfa4dy\" id=\"Flow_1jfa4dy_di\"\u003e\u003comgdi:waypoint x=\"1050\" y=\"412\"/\u003e\u003comgdi:waypoint x=\"1050\" y=\"508\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0uq1ypa\" id=\"Flow_0uq1ypa_di\"\u003e\u003comgdi:waypoint x=\"1050\" y=\"216\"/\u003e\u003comgdi:waypoint x=\"1050\" y=\"328\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"181.51600000000002\" x=\"959\" y=\"164\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"952\" y=\"328\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_2\" id=\"ScriptTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"952\" y=\"508\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_3\" id=\"EndPoint_3_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.2188\" x=\"984\" y=\"674\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1744627709293,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 39,
        "name": "shresh@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_1f224b3c_8c62_4935_b4b2_f13b8e3b2d6b",
      "description": {
        "content": null,
        "format": "text"
      },
      "display_name": "ElasticSearch Query from Artifact",
      "export_key": "elasticsearch_query_from_artifact",
      "field_type_handle": "playbook_1f224b3c_8c62_4935_b4b2_f13b8e3b2d6b",
      "fields_type": {
        "actions": [],
        "display_name": "ElasticSearch Query from Artifact",
        "export_key": "playbook_1f224b3c_8c62_4935_b4b2_f13b8e3b2d6b",
        "fields": {},
        "for_actions": false,
        "for_custom_fields": false,
        "for_notifications": false,
        "for_workflows": false,
        "id": null,
        "parent_types": [
          "__playbook"
        ],
        "properties": {
          "can_create": false,
          "can_destroy": false,
          "for_who": []
        },
        "scripts": [],
        "tags": [],
        "type_id": 28,
        "type_name": "playbook_1f224b3c_8c62_4935_b4b2_f13b8e3b2d6b",
        "uuid": "c24875b5-39be-403d-b1c1-506118bb569a"
      },
      "has_logical_errors": false,
      "id": 246,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 39,
        "name": "shresh@example.com",
        "type": "user"
      },
      "last_modified_time": 1744726333368,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1744628576963,
          "description": "",
          "enabled": false,
          "export_key": "Elastic Search Results",
          "id": 232,
          "language": "python3",
          "last_modified_by": "shresh@example.com",
          "last_modified_time": 1744726328922,
          "name": "Elastic Search Results",
          "object_type": "artifact",
          "playbook_handle": "elasticsearch_query_from_artifact",
          "programmatic_name": "elasticsearch_query_from_artifact_elastic_search_results",
          "script_text": "results = playbook.functions.results.results\nif results.success:\n  msg = [f\"ElasticSearch successful for String: {artifact.value}\"]\n  for result in results.query_results:\n    for k, v in result.items():\n        msg.append(f\"\u003cbr\u003e\u003cb\u003e{k}\u003c/b\u003e: {v}\")\n  incident.addNote(helper.createRichText(\"\".join(msg)))\nelse:\n  incident.addNote(f\u0027ElasticSearch String query failed: Artifact value:{artifact.value}\u0027)",
          "tags": [],
          "uuid": "4b9716b7-53c8-411b-9aab-db0196ac422c"
        }
      ],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [
            {
              "evaluation_id": null,
              "field_name": "artifact.type",
              "method": "equals",
              "type": null,
              "value": "String"
            }
          ],
          "logic_type": "all"
        },
        "view_items": []
      },
      "name": "elasticsearch_query_from_artifact",
      "object_type": "artifact",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_1f224b3c-8c62-4935-b4b2-f13b8e3b2d6b",
        "id": 356,
        "name": "playbook_1f224b3c_8c62_4935_b4b2_f13b8e3b2d6b",
        "type": "playbook",
        "uuid": "bf8ab6b1-e7b8-4889-b103-c8aa91b7f80f"
      },
      "tags": [],
      "type": "default",
      "uuid": "1f224b3c-8c62-4935-b4b2-f13b8e3b2d6b",
      "version": 18
    },
    {
      "activation_type": "manual",
      "content": {
        "content_version": 22,
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"playbook_ed45bdf0_b4db_47a9_8d30_b851eb18c29d\" isExecutable=\"true\" name=\"playbook_ed45bdf0_b4db_47a9_8d30_b851eb18c29d\"\u003e\u003cdocumentation/\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eFlow_0127nis\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1\" name=\"ElasticSearch Utilities: Query\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"4f103490-595d-4ab9-ba30-8202c8ddfe9d\"\u003e{\"inputs\":{\"b92cc3ed-2878-4630-81a7-5830780fa5d9\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_content_value\":{\"format\":\"unknown\",\"content\":\"{\\n    \\\"query\\\": {\\n        \\\"match_all\\\": {}\\n    }\\n}\"}}},\"1e041775-c9ba-43ae-a8cf-3f4dda9a0681\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}},\"eed55443-7d80-4451-b275-31f2e09c3a84\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_value\":\"\"}}},\"result_name\":\"results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_0127nis\u003c/incoming\u003e\u003coutgoing\u003eFlow_1ozd4zi\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"Flow_0127nis\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1\"/\u003e\u003cscriptTask id=\"ScriptTask_2\" name=\"Elastic Search Results\"\u003e\u003cextensionElements\u003e\u003cresilient:script uuid=\"7873c05c-f43e-4fce-8ab7-a626e7ac5852\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eFlow_1ozd4zi\u003c/incoming\u003e\u003coutgoing\u003eFlow_0kj8n5d\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"Flow_1ozd4zi\" sourceRef=\"ServiceTask_1\" targetRef=\"ScriptTask_2\"/\u003e\u003cendEvent id=\"EndPoint_3\" resilient:documentation=\"End point\"\u003e\u003cincoming\u003eFlow_0kj8n5d\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"Flow_0kj8n5d\" sourceRef=\"ScriptTask_2\" targetRef=\"EndPoint_3\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"playbook_ed45bdf0_b4db_47a9_8d30_b851eb18c29d\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0kj8n5d\" id=\"Flow_0kj8n5d_di\"\u003e\u003comgdi:waypoint x=\"1040\" y=\"502\"/\u003e\u003comgdi:waypoint x=\"1040\" y=\"574\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_1ozd4zi\" id=\"Flow_1ozd4zi_di\"\u003e\u003comgdi:waypoint x=\"1040\" y=\"342\"/\u003e\u003comgdi:waypoint x=\"1040\" y=\"418\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Flow_0127nis\" id=\"Flow_0127nis_di\"\u003e\u003comgdi:waypoint x=\"1040\" y=\"146\"/\u003e\u003comgdi:waypoint x=\"1040\" y=\"258\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"187.188\" x=\"946\" y=\"94\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"616\" y=\"100\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1\" id=\"ServiceTask_1_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"942\" y=\"258\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_2\" id=\"ScriptTask_2_di\"\u003e\u003comgdc:Bounds height=\"84\" width=\"196\" x=\"942\" y=\"418\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndPoint_3\" id=\"EndPoint_3_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"132.2188\" x=\"974\" y=\"574\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "create_date": 1744630089179,
      "creator_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 39,
        "name": "shresh@example.com",
        "type": "user"
      },
      "deployment_id": "playbook_ed45bdf0_b4db_47a9_8d30_b851eb18c29d",
      "description": {
        "content": null,
        "format": "text"
      },
      "display_name": "ElasticSearch Query from Incident",
      "export_key": "elasticsearch_query_from_incident",
      "field_type_handle": "playbook_ed45bdf0_b4db_47a9_8d30_b851eb18c29d",
      "fields_type": {
        "actions": [],
        "display_name": "ElasticSearch Query from Incident",
        "export_key": "playbook_ed45bdf0_b4db_47a9_8d30_b851eb18c29d",
        "fields": {},
        "for_actions": false,
        "for_custom_fields": false,
        "for_notifications": false,
        "for_workflows": false,
        "id": null,
        "parent_types": [
          "__playbook"
        ],
        "properties": {
          "can_create": false,
          "can_destroy": false,
          "for_who": []
        },
        "scripts": [],
        "tags": [],
        "type_id": 28,
        "type_name": "playbook_ed45bdf0_b4db_47a9_8d30_b851eb18c29d",
        "uuid": "3ab67a55-8360-4581-bf86-bd3caeaf918e"
      },
      "has_logical_errors": false,
      "id": 247,
      "is_deleted": false,
      "is_locked": false,
      "last_modified_principal": {
        "display_name": "Resilient Sysadmin",
        "id": 39,
        "name": "shresh@example.com",
        "type": "user"
      },
      "last_modified_time": 1744729649345,
      "local_scripts": [
        {
          "actions": [],
          "created_date": 1744630308737,
          "description": "",
          "enabled": false,
          "export_key": "Elastic Search Results",
          "id": 233,
          "language": "python3",
          "last_modified_by": "shresh@example.com",
          "last_modified_time": 1744729646809,
          "name": "Elastic Search Results",
          "object_type": "incident",
          "playbook_handle": "elasticsearch_query_from_incident",
          "programmatic_name": "elasticsearch_query_from_incident_elastic_search_results",
          "script_text": "results = playbook.functions.results.results\nif results.success:\n  msg = [f\"ElasticSearch successful for Incident: {incident.id}\\n\"]\n  for result in results.query_results:\n    for k, v in result.items():\n        msg.append(f\"\u003cbr\u003e\u003cb\u003e{k}\u003c/b\u003e: {v}\")\n  incident.addNote(helper.createRichText(\"\".join(msg)))\nelse:\n  incident.addNote(f\u0027ElasticSearch Incident query failed:{results.reason}. Incident ID:{incident.id}\u0027)",
          "tags": [],
          "uuid": "7873c05c-f43e-4fce-8ab7-a626e7ac5852"
        }
      ],
      "manual_settings": {
        "activation_conditions": {
          "conditions": [],
          "logic_type": "all"
        },
        "view_items": []
      },
      "name": "elasticsearch_query_from_incident",
      "object_type": "incident",
      "status": "enabled",
      "tag": {
        "display_name": "Playbook_ed45bdf0-b4db-47a9-8d30-b851eb18c29d",
        "id": 357,
        "name": "playbook_ed45bdf0_b4db_47a9_8d30_b851eb18c29d",
        "type": "playbook",
        "uuid": "008796b9-6293-4340-8a82-806955c5e427"
      },
      "tags": [],
      "type": "default",
      "uuid": "ed45bdf0-b4db-47a9-8d30-b851eb18c29d",
      "version": 26
    }
  ],
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
        "workflow_id": "example_elasticsearch_query_from_artifact",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_elasticsearch_query_from_artifact\" isExecutable=\"true\" name=\"Example: ElasticSearch Query from Artifact\"\u003e\u003cdocumentation\u003eAn example which attempts to query ElasticSearch using data gathered from an artifact. Intended to be used on an artifact of type \u0027String\u0027\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0aetsi3\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0e56r29\" name=\"ElasticSearch Utilities: Query\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"4f103490-595d-4ab9-ba30-8202c8ddfe9d\"\u003e{\"inputs\":{},\"post_processing_script\":\"\\\"\\\"\\\"\\n# An Example of the result object \\n    results = {\\n        \\\"inputs\\\": {\\n          \\\"es_query\\\": { \\\"query\\\": { \\\"match_all\\\": {} } },\\n          \\\"es_doc_type\\\": logs,\\n          \\\"es_index\\\" : my_logstore\\n        },\\n        \\\"query_results\\\": [\\n          \u0026lt;elasticsearch-record\u0026gt;,\\n        \\\"success\\\": True / False,\\n        \\\"matched_records\\\": 1000,\\n        \\\"returned_records\\\": 100\\n    }\\n    Note: The schema of elasticsearch-record; outlined above, will reflect the structure of your data in Elastic itself\\n\\\"\\\"\\\"\\n\\nif results.matched_records:\\n  noteText = \\\"\\\"\\\"\u0026lt;b\u0026gt;ElasticSearch Query status\u0026lt;/b\u0026gt;\\n                \u0026lt;br\u0026gt; Query supplied: \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;\\n                \u0026lt;br\u0026gt; Total matched records :\u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt;\\\"\\\"\\\".format(results.inputs[\\\"es_query\\\"], results.matched_records)\\n  \\n  if results.returned_records:\\n    noteText += \\\"\\\"\\\"\u0026lt;br\u0026gt; Total returned records : \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;\\\"\\\"\\\".format(results.returned_records)\\n  incident.addNote(helper.createRichText(noteText))\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"if artifact.value:\\n  inputs.es_query = artifact.value\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0aetsi3\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1yz77pw\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndEvent_0gizqrd\"\u003e\u003cincoming\u003eSequenceFlow_1yz77pw\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0aetsi3\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0e56r29\"/\u003e\u003csequenceFlow id=\"SequenceFlow_1yz77pw\" sourceRef=\"ServiceTask_0e56r29\" targetRef=\"EndEvent_0gizqrd\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_051atie\"\u003e\u003ctext\u003eTakes in an elasticsearch query and optionally, an index and doc_type to search against\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1ta8zaw\" sourceRef=\"ServiceTask_0e56r29\" targetRef=\"TextAnnotation_051atie\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_00jn6bc\"\u003e\u003ctext\u003eReturns result of query including how many matched and returned records. Saves query information in a rich text note\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0t6x92s\" sourceRef=\"ServiceTask_0e56r29\" targetRef=\"TextAnnotation_00jn6bc\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0e56r29\" id=\"ServiceTask_0e56r29_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"369\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0gizqrd\" id=\"EndEvent_0gizqrd_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"644\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"662\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0aetsi3\" id=\"SequenceFlow_0aetsi3_di\"\u003e\u003comgdi:waypoint x=\"198\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"369\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"283.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1yz77pw\" id=\"SequenceFlow_1yz77pw_di\"\u003e\u003comgdi:waypoint x=\"469\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"644\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"556.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_051atie\" id=\"TextAnnotation_051atie_di\"\u003e\u003comgdc:Bounds height=\"96\" width=\"137\" x=\"209\" y=\"77\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1ta8zaw\" id=\"Association_1ta8zaw_di\"\u003e\u003comgdi:waypoint x=\"369\" y=\"177\"/\u003e\u003comgdi:waypoint x=\"346\" y=\"164\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_00jn6bc\" id=\"TextAnnotation_00jn6bc_di\"\u003e\u003comgdc:Bounds height=\"101\" width=\"129\" x=\"504\" y=\"80\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0t6x92s\" id=\"Association_0t6x92s_di\"\u003e\u003comgdi:waypoint x=\"469\" y=\"181\"/\u003e\u003comgdi:waypoint x=\"504\" y=\"163\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 2,
      "description": "An example which attempts to query ElasticSearch using data gathered from an artifact. Intended to be used on an artifact of type \u0027String\u0027",
      "export_key": "example_elasticsearch_query_from_artifact",
      "last_modified_by": "shresh@example.com",
      "last_modified_time": 1741354930172,
      "name": "Example: ElasticSearch Query from Artifact",
      "object_type": "artifact",
      "programmatic_name": "example_elasticsearch_query_from_artifact",
      "tags": [],
      "uuid": "29afd122-2e24-4516-b779-887c50962f5f",
      "workflow_id": 334
    },
    {
      "actions": [],
      "content": {
        "version": 2,
        "workflow_id": "example_elasticsearch_query_from_incident",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_elasticsearch_query_from_incident\" isExecutable=\"true\" name=\"Example: ElasticSearch Query from Incident\"\u003e\u003cdocumentation\u003eAn example which attempts to query ElasticSearch using a pre-defined query. Query examples are provided during workflow creation.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1e6h4md\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_128lxwv\" name=\"ElasticSearch Utilities: Query\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"4f103490-595d-4ab9-ba30-8202c8ddfe9d\"\u003e{\"inputs\":{\"b92cc3ed-2878-4630-81a7-5830780fa5d9\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"text_content_value\":{\"format\":\"text\",\"content\":\"{\\n    \\\"query\\\": {\\n        \\\"match_all\\\": {}\\n    }\\n}\"}}}},\"post_processing_script\":\"\\\"\\\"\\\"\\n# An Example of the result object \\n    results = {\\n        \\\"inputs\\\": {\\n          \\\"es_query\\\": { \\\"query\\\": { \\\"match_all\\\": {} } },\\n          \\\"es_doc_type\\\": logs,\\n          \\\"es_index\\\" : my_logstore\\n        },\\n        \\\"query_results\\\": [\\n          \u0026lt;elasticsearch-record\u0026gt;,\\n        \\\"success\\\": True / False,\\n        \\\"matched_records\\\": 1000,\\n        \\\"returned_records\\\": 100\\n    }\\n    Note: The schema of elasticsearch-record; outlined above, will reflect the structure of your data in Elastic itself\\n\\\"\\\"\\\"\\n\\nif results.matched_records:\\n  noteText = \\\"\\\"\\\"\u0026lt;b\u0026gt;ElasticSearch Query status\u0026lt;/b\u0026gt;\\n                \u0026lt;br\u0026gt; Query supplied: \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;\\n                \u0026lt;br\u0026gt; Total matched records :\u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt;\\\"\\\"\\\".format(results.inputs[\\\"es_query\\\"], results.matched_records)\\n  \\n  if results.returned_records:\\n    noteText += \\\"\\\"\\\"\u0026lt;br\u0026gt; Total returned records : \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;\\\"\\\"\\\".format(results.returned_records)\\n  incident.addNote(helper.createRichText(noteText))\",\"post_processing_script_language\":\"python3\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1e6h4md\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_08bun20\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndEvent_0nz5r72\"\u003e\u003cincoming\u003eSequenceFlow_08bun20\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1e6h4md\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_128lxwv\"/\u003e\u003csequenceFlow id=\"SequenceFlow_08bun20\" sourceRef=\"ServiceTask_128lxwv\" targetRef=\"EndEvent_0nz5r72\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_17fmnol\"\u003e\u003ctext\u003eTakes in an elasticsearch query and optionally, an index and doc_type to search against\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_09238i3\" sourceRef=\"ServiceTask_128lxwv\" targetRef=\"TextAnnotation_17fmnol\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_000xz6j\"\u003e\u003ctext\u003eReturns result of query including how many matched and returned records. Saves query information in a rich text note\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0457y43\" sourceRef=\"ServiceTask_128lxwv\" targetRef=\"TextAnnotation_000xz6j\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_128lxwv\" id=\"ServiceTask_128lxwv_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"318.07775000000004\" y=\"165.54725000000002\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0nz5r72\" id=\"EndEvent_0nz5r72_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"568.0567441860466\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"586.0567441860466\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1e6h4md\" id=\"SequenceFlow_1e6h4md_di\"\u003e\u003comgdi:waypoint x=\"198\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"318\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"258\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_08bun20\" id=\"SequenceFlow_08bun20_di\"\u003e\u003comgdi:waypoint x=\"418\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"568\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"493\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_17fmnol\" id=\"TextAnnotation_17fmnol_di\"\u003e\u003comgdc:Bounds height=\"72\" width=\"144\" x=\"157\" y=\"72\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_09238i3\" id=\"Association_09238i3_di\"\u003e\u003comgdi:waypoint x=\"321\" y=\"173\"/\u003e\u003comgdi:waypoint x=\"280\" y=\"144\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_000xz6j\" id=\"TextAnnotation_000xz6j_di\"\u003e\u003comgdc:Bounds height=\"94\" width=\"189\" x=\"435\" y=\"61\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0457y43\" id=\"Association_0457y43_di\"\u003e\u003comgdi:waypoint x=\"418\" y=\"176\"/\u003e\u003comgdi:waypoint x=\"453\" y=\"155\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 2,
      "description": "An example which attempts to query ElasticSearch using a pre-defined query. Query examples are provided during workflow creation.",
      "export_key": "example_elasticsearch_query_from_incident",
      "last_modified_by": "shresh@example.com",
      "last_modified_time": 1741355004111,
      "name": "Example: ElasticSearch Query from Incident",
      "object_type": "incident",
      "programmatic_name": "example_elasticsearch_query_from_incident",
      "tags": [],
      "uuid": "90c650a7-da55-4bfd-b409-c938ec608d2b",
      "workflow_id": 335
    }
  ],
  "workspaces": []
}
