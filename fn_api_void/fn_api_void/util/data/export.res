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
          "value": "DNS Name"
        }
      ],
      "enabled": true,
      "export_key": "Example: APIVoid DNS Lookup",
      "id": 125,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: APIVoid DNS Lookup",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "07af2406-d3d4-429d-a248-cfbad192669c",
      "view_items": [],
      "workflows": [
        "example_apivoid_dns_lookup"
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
          "value": "DNS Name"
        }
      ],
      "enabled": true,
      "export_key": "Example: APIVoid Domain Reputation",
      "id": 126,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: APIVoid Domain Reputation",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "ac9a44f7-6418-4c0c-b3ba-60391a585621",
      "view_items": [],
      "workflows": [
        "example_apivoid_domain_reputation"
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
          "value": "Email Recipient"
        },
        {
          "evaluation_id": null,
          "field_name": "artifact.type",
          "method": "equals",
          "type": null,
          "value": "Email Sender"
        }
      ],
      "enabled": true,
      "export_key": "Example: APIVoid Email Verify",
      "id": 127,
      "logic_type": "any",
      "message_destinations": [],
      "name": "Example: APIVoid Email Verify",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "547bc915-236d-4377-b60b-46c018f478d2",
      "view_items": [],
      "workflows": [
        "example_apivoid_email_verify"
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
          "value": "IP Address"
        }
      ],
      "enabled": true,
      "export_key": "Example: APIVoid IP Reputation",
      "id": 128,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: APIVoid IP Reputation",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "050c9491-3460-4195-ad42-e553694afc1f",
      "view_items": [],
      "workflows": [
        "example_apivoid_ip_reputation"
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
          "value": "DNS Name"
        }
      ],
      "enabled": true,
      "export_key": "Example: APIVoid SSL Info",
      "id": 129,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: APIVoid SSL Info",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "e79904d1-0f16-477b-ad33-f035a3a4e802",
      "view_items": [],
      "workflows": [
        "example_apivoid_ssl_info"
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
          "value": "DNS Name"
        }
      ],
      "enabled": true,
      "export_key": "Example: APIVoid ThreatLog",
      "id": 130,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: APIVoid ThreatLog",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "3bae128f-2274-4cc1-8330-6b2cf3c87336",
      "view_items": [],
      "workflows": [
        "example_apivoid_threatlog"
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
          "value": "URL"
        }
      ],
      "enabled": true,
      "export_key": "Example: APIVoid URL Reputation",
      "id": 131,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: APIVoid URL Reputation",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "122ed2a0-ad40-4065-b579-5e2a9c9cd2b1",
      "view_items": [],
      "workflows": [
        "example_apivoid_url_reputation"
      ]
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "export_date": 1698739748478,
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
      "export_key": "__function/api_void_request_type",
      "hide_notification": false,
      "id": 997,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "api_void_request_type",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "api_void_request_type",
      "tooltip": "",
      "type_id": 11,
      "uuid": "a17a314a-2747-4e47-84df-7ca50772c78f",
      "values": [
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "ThreatLog",
          "properties": null,
          "uuid": "de2a6cdf-6cab-4849-b386-8586346f96aa",
          "value": 402
        },
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "IP Reputation",
          "properties": null,
          "uuid": "7ff85ec3-9ccd-4fee-8166-37e816e72385",
          "value": 403
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Domain Reputation",
          "properties": null,
          "uuid": "7e0d15ad-f691-4305-8834-9818a7fa8400",
          "value": 404
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "URL Reputation",
          "properties": null,
          "uuid": "72665ba2-3ec2-4fd4-a2fa-17b2a0f85890",
          "value": 405
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "DNS Lookup",
          "properties": null,
          "uuid": "6fdcb333-c935-4e68-957f-0e230ca911fb",
          "value": 406
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Email Verify",
          "properties": null,
          "uuid": "4314f157-860d-40ba-8b62-84ed627eaab7",
          "value": 407
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "SSL Info",
          "properties": null,
          "uuid": "15185469-692c-4000-8220-2b22dee4a6f3",
          "value": 408
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "selftest",
          "properties": null,
          "uuid": "0a9ec6b9-3b4e-4f1a-b234-23273a4f9b75",
          "value": 409
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
      "export_key": "__function/api_void_artifact_value",
      "hide_notification": false,
      "id": 999,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "api_void_artifact_value",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "api_void_artifact_value",
      "tooltip": "",
      "type_id": 11,
      "uuid": "3fcbdf4a-7a21-4a6f-8faf-210422ed595d",
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
      "export_key": "__function/api_void_artifact_type",
      "hide_notification": false,
      "id": 998,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "api_void_artifact_type",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "api_void_artifact_type",
      "tooltip": "",
      "type_id": 11,
      "uuid": "61430b39-a717-4d0b-a369-0dc5272565c3",
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
      "created_date": 1698651338981,
      "description": {
        "content": "Make an APIVoid API request call.  The API json is returned by the function.",
        "format": "text"
      },
      "destination_handle": "fn_api_void",
      "display_name": "APIVoid Request",
      "export_key": "fn_api_void_request",
      "id": 63,
      "last_modified_by": {
        "display_name": "Resilient Sysadmin",
        "id": 6,
        "name": "dummy@dummy.com",
        "type": "user"
      },
      "last_modified_time": 1698651339051,
      "name": "fn_api_void_request",
      "tags": [],
      "uuid": "39141052-d0b0-4c44-b243-d3eb41d42553",
      "version": 1,
      "view_items": [
        {
          "content": "a17a314a-2747-4e47-84df-7ca50772c78f",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "61430b39-a717-4d0b-a369-0dc5272565c3",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "3fcbdf4a-7a21-4a6f-8faf-210422ed595d",
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
          "name": "Example: APIVoid DNS Lookup",
          "object_type": "artifact",
          "programmatic_name": "example_apivoid_dns_lookup",
          "tags": [],
          "uuid": null,
          "workflow_id": 135
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: APIVoid Domain Reputation",
          "object_type": "artifact",
          "programmatic_name": "example_apivoid_domain_reputation",
          "tags": [],
          "uuid": null,
          "workflow_id": 139
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: APIVoid Email Verify",
          "object_type": "artifact",
          "programmatic_name": "example_apivoid_email_verify",
          "tags": [],
          "uuid": null,
          "workflow_id": 137
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: APIVoid IP Reputation",
          "object_type": "artifact",
          "programmatic_name": "example_apivoid_ip_reputation",
          "tags": [],
          "uuid": null,
          "workflow_id": 138
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: APIVoid SSL Info",
          "object_type": "artifact",
          "programmatic_name": "example_apivoid_ssl_info",
          "tags": [],
          "uuid": null,
          "workflow_id": 136
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: APIVoid ThreatLog",
          "object_type": "artifact",
          "programmatic_name": "example_apivoid_threatlog",
          "tags": [],
          "uuid": null,
          "workflow_id": 134
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: APIVoid URL Reputation",
          "object_type": "artifact",
          "programmatic_name": "example_apivoid_url_reputation",
          "tags": [],
          "uuid": null,
          "workflow_id": 140
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 33,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [],
  "incident_types": [
    {
      "create_date": 1698739745000,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1698739745000,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "industries": null,
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [
        "3be03c51-b800-40ad-a380-1dcf20dcfe87"
      ],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "fn_api_void",
      "name": "fn_api_void",
      "programmatic_name": "fn_api_void",
      "tags": [],
      "users": [],
      "uuid": "f1e68502-be11-4ff2-99f9-10010bf0a5a7"
    }
  ],
  "notifications": null,
  "overrides": null,
  "phases": [],
  "playbooks": [],
  "regulators": null,
  "roles": [],
  "scripts": [
    {
      "actions": [],
      "created_date": 1698670878491,
      "description": "This script converts a json object into a hierarchical display of rich text and adds the rich text to an incident\u0027s rich text (custom) field or an incident note. A workflow property is used to share the json to convert and identify parameters used on how to perform the conversion. Typically, a function will create the workflow property \u0027convert_json_to_rich_text\u0027, and this script will run after that function to perform the conversion.",
      "enabled": false,
      "export_key": "Convert JSON to rich text v1.3",
      "id": 72,
      "language": "python3",
      "last_modified_by": "dummy@dummy.com",
      "last_modified_time": 1698718436659,
      "name": "Convert JSON to rich text v1.3",
      "object_type": "incident",
      "playbook_handle": null,
      "programmatic_name": "convert_json_to_rich_text_v13",
      "script_text": "# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.\nVERSION = 1.3\n\"\"\"\n  This script converts a json object into a hierarchical display of rich text and adds the rich text to an incident\u0027s rich text (custom) field or an incident note.\n  A workflow property is used to define the json to convert and identify parameters used on how to perform the conversion.\n  Typically, a function will create workflow property and this script will run after that function to perform the conversion.\n  Features:\n    * Display the hierarchical nature of json, presenting the json keys as bold labels\n    * Provide links to found URLs\n    * Create either an incident note or add results to an incident (custom) rich text field.\n  \n  In order to use this script, define a workflow property called: convert_json_to_rich_text, to define the json and parameters to use for the conversion.\n  Workflow properties can be added using a command similar to this:\n  workflow.addProperty(\u0027convert_json_to_rich_text\u0027, {\n    \"version\": 1.3,\n    \"header\": \"Artifact scan results for: {}\".format(artifact.value),\n    \"padding\": 10,\n    \"separator\": u\"\u003cbr /\u003e\",\n    \"sort\": True,\n    \"json\": results.content,\n    \"json_omit_list\": [\"omit\"],\n    \"incident_field\": None\n  })\n  \n  Format of workflow.property.convert_json_to_rich_text:\n  { \n    \"version\": 1.3, [this is for future compatibility]\n    \"header\": str, [header line to add to converted json produced or None. Ex: Results from scanning artifact: xxx. The header may contain rich text tags]\n    \"padding\": 10, [padding for nested json elements, or defaults to 10]\n    \"separator\": u\"\u003cbr /\u003e\"|list such as [\u0027\u003cspan\u003e\u0027,\u0027\u003c/span\u003e\u0027], [html separator between json keys and lists or defaults to html break: \u0027\u003cbr /\u003e\u0027. \n                                                If a list, then the data is brackets by the pair specified]\n    \"sort\": True|False, [sort the json keys at each level when displayed]\n    \"json\": json, [required json to convert]\n    \"json_omit_list\": [list of json keys to exclude or None]\n    \"incident_field\": \"\u003cincident_field\u003e\" [indicates a builtin rich text incident field, such as \u0027description\u0027 \n                                          or a custom rich text field in the format: \u0027properties.\u003cfield\u003e\u0027. default: create an incident note]\n  }\n\n  For playbooks, use playbook.addProperty() with the same format as workflow.addProperty()\n\n  Playbooks can also use playbook.functions.results.convert_json_to_rich_text using the standard function output which contains the \u0027content\u0027 json element.\n  When using playbook.functions.results.convert_json_to_rich_text with standard function results, all the defaults for padding, separator, etc. are used.\n\"\"\"\n\nimport re\n\n# needed for python 3\ntry:\n    unicode(\"abc\") # fails in py3\n    py2 = True\nexcept:\n    unicode = str\n    py2 = False\n\n\nrc = re.compile(r\u0027http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.\u0026+#\\?]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+\u0027)\n\nclass ConvertJson:\n    \"\"\"Class to hold the conversion parameters and perform the conversion\"\"\"\n\n    def __init__(self, omit_keys=[], padding=10, separator=u\"\u003cbr /\u003e\", sort_keys=False):\n        self.omit_keys = omit_keys\n        self.padding = padding\n        self.separator = separator\n        self.sort_keys = sort_keys\n\n\n    def format_link(self, item):\n        \"\"\"[summary]\n          Find embedded urls (http(s)) and add html anchor tags to display as links\n          Args:\n              item ([string])\n\n          Returns:\n              [str]: None|original text if no links|text with html links\n        \"\"\"\n        formatted_item = item\n        if py2:\n            num_type = bool(item and isinstance(item, (int, long, bool, float)))\n        else:\n            num_type = bool(item and isinstance(item, (int, bool, float)))\n\n        if item and not num_type:\n            list = rc.findall(item)\n            if list:\n                for link in list:\n                    formatted_item = formatted_item.replace(link, u\"\u003ca target=\u0027blank\u0027 href=\u0027{0}\u0027\u003e{0}\u003c/a\u003e\".format(link))\n\n        return formatted_item\n\n    def expand_list(self, list_value, is_list=False):\n        \"\"\"[summary]\n          convert items to html, adding indents to nested dictionaries.\n          Args:\n              list_value ([dict|list]): json element\n\n          Returns:\n              [str]: html converted code\n        \"\"\"\n        if not isinstance(list_value, list):\n            return self.format_link(list_value)\n        elif not list_value:\n            return u\"None\u003cbr\u003e\"\n\n        try:\n            items_list = []  # this will ensure list starts on second line of key label\n            for item in list_value:\n                if isinstance(item, dict):\n                    result = self.convert_json_to_rich_text(item)\n                    if is_list:\n                        items_list.append(u\"\u003cli\u003e{}\u003c/li\u003e\".format(result))\n                    else:\n                        items_list.append(result)\n                elif isinstance(item, list):\n                    items_list.append(self.expand_list(item, is_list=True))\n                elif is_list:\n                    items_list.append(u\"\u003cli\u003e{}\u003c/li\u003e\".format(self.format_link(unicode(item))))\n                else:\n                    items_list.append(self.format_link(unicode(item)))\n\n            expand_list_result = self.add_separator(self.separator if not is_list else u\"\",\n                                                    items_list,\n                                                    is_list=is_list)\n\n            if is_list:\n                return u\"\u003cul\u003e{}\u003c/ul\u003e\".format(expand_list_result)\n            else:\n                return u\"\u003cdiv style=\u0027padding:5px\u0027\u003e{}\u003c/div\u003e\".format(expand_list_result)\n        except Exception as err:\n            return str(err)\n\n    def convert_json_to_rich_text(self, sub_dict):\n        \"\"\"[summary]\n          Walk dictionary tree and convert to html for better display\n          Args:\n              sub_dict ([type]): [description]\n\n          Returns:\n              [type]: [description]\n        \"\"\"\n        notes = []\n        if sub_dict and isinstance(sub_dict, (list, dict)):\n            if isinstance(sub_dict, list):\n                expanded_list = self.expand_list(sub_dict, is_list=True)\n                notes.append(self.add_separator(self.separator, expanded_list))\n            else:\n                keys = sorted (sub_dict.keys()) if self.sort_keys else sub_dict.keys()\n\n                for key in keys:\n                    if key not in self.omit_keys:\n                        value = sub_dict[key]\n                        is_list = isinstance(value, list)\n                        item_list = [u\"\u003cstrong\u003e{0}\u003c/strong\u003e: \".format(key)]\n                        if isinstance(value, dict):\n                            convert_result = self.convert_json_to_rich_text(value)\n                            if convert_result:\n                                item_list.append(u\"\u003cdiv style=\u0027padding:{}px\u0027\u003e{}\u003c/div\u003e\".format(self.padding, convert_result))\n                            else:\n                                item_list.append(u\"None\u003cbr\u003e\")\n                        else:\n                            item_list.append(self.expand_list(value, is_list=is_list))\n\n                        notes.append(self.add_separator(self.separator, u\"\".join(make_unicode(v) for v in item_list), is_list=is_list))\n\n        result_notes = u\"\".join(notes)\n        if isinstance(self.separator, list):\n            return result_notes\n        else:\n            return result_notes.replace(\n                u\"\u003c/div\u003e{0}\".format(self.separator), u\"\u003c/div\u003e\").replace(\n                u\"{0}\u003c/div\u003e\".format(self.separator), u\"\u003c/div\u003e\"\n            )  # tighten up result\n\n    def add_separator(self, separator, items, is_list=False):\n        \"\"\"\n        apply the separator to the data\n        :param separator: None, str or list such as [\u0027\u003cspan\u003e\u0027, \u0027\u003c/span\u003e\u0027]\n        :param items: str or list to add separator\n        :return: text with separator applied\n        \"\"\"\n        _items = items\n\n        if not _items:\n            return \"\u003cbr\u003e\"\n\n        if not isinstance(_items, list):\n            _items = [_items]\n\n        if isinstance(separator, list):\n            return u\"\".join([u\"{}{}{}\".format(separator[0], item, separator[1]) for item in _items])\n\n        return u\"{}{}\".format(separator.join(_items), separator if not is_list else u\"\")\n\ndef make_unicode(value):\n    if value is None:\n        return \u0027None\u0027\n\n    return unicode(value)\n\ndef get_results(property_name):\n    if playbook and playbook.functions.results[property_name] is not None:\n        return playbook.functions.results[property_name]\n    elif playbook and playbook.properties[property_name] is not None:\n        return playbook.properties[property_name]\n    elif workflow and workflow.properties[property_name] is not None:\n        return workflow.properties[property_name]\n\n    return None\n\ndef get_properties(property_name):\n    \"\"\"\n    Logic to collect the json and parameters from a workflow property.\n    Args:\n      property_name: workflow property to reference\n    Returns:\n      padding, separator, header, json_omit_list, incident_field, json, sort_keys\n    \"\"\"\n    result_properties = get_results(property_name)\n    if not result_properties:\n        helper.fail(\"Playbook/workflow property not found: {}\".format(property_name))\n\n    padding = int(result_properties.get(\"padding\", 10))\n    separator = result_properties.get(\"separator\", u\"\u003cbr /\u003e\")\n    if isinstance(separator, list) and len(separator) != 2:\n        helper.fail(\"list of separators should be specified as a pair such as [\u0027\u003cdiv\u003e\u0027, \u0027\u003c/div\u003e\u0027]: {}\".format(separator))\n\n    header = result_properties.get(\"header\")\n    sort_keys = bool(result_properties.get(\"sort\", False))\n    json_omit_list = result_properties.get(\"json_omit_list\")\n    if not json_omit_list:\n        json_omit_list = []\n    incident_field = result_properties.get(\"incident_field\")\n    \n    # workflow formatted content is \u0027json\u0027. Standard functions is \u0027content\u0027\n    json = result_properties.get(\"json\") if result_properties.get(\"json\") else result_properties.get(\"content\")\n    json_err = None\n    # is there an issue we need handle now?\n    if not json and \\\n        result_properties.get(\"success\") == False and result_properties.get(\"reason\"):\n        json_err = result_properties.get(\"reason\")\n    \n    return padding, separator, header, json_omit_list, incident_field, json, json_err, sort_keys\n\n\n## S T A R T\npadding, separator, header, json_omit_list, incident_field, json, json_err, sort_keys = get_properties(\u0027convert_json_to_rich_text\u0027)\nif json_err:\n    result = \"Result error: {}\".format(json_err)\nelse:\n    if header:\n        if isinstance(separator, list):\n            hdr = u\"{0}{1}{2}\".format(separator[0], header, separator[1])\n        else:\n            hdr = u\"{0}{1}\".format(header, separator)\n    else:\n        hdr = u\"\"\n\n    convert = ConvertJson(omit_keys=json_omit_list, padding=padding, separator=separator, sort_keys=sort_keys)\n    converted_json = convert.convert_json_to_rich_text(json)\n    result = u\"{}{}\".format(hdr, converted_json if converted_json else \"\\nNone\")\n\nrich_text_note = helper.createRichText(result)\nif incident_field:\n    incident[incident_field] = rich_text_note\nelse:\n    incident.addNote(rich_text_note)\n",
      "tags": [],
      "uuid": "559123e6-50df-46a8-b90f-79eaef3211bb"
    }
  ],
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
        "version": 4,
        "workflow_id": "example_apivoid_dns_lookup",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_apivoid_dns_lookup\" isExecutable=\"true\" name=\"Example: APIVoid DNS Lookup\"\u003e\u003cdocumentation\u003eExample workflow calls APIVoid dnslookup API to return DNS records of domain names.  The JSON results are written to an incident note.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1x0rhgh\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0s8m9pf\" name=\"APIVoid Request\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"39141052-d0b0-4c44-b243-d3eb41d42553\"\u003e{\"inputs\":{\"a17a314a-2747-4e47-84df-7ca50772c78f\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"6fdcb333-c935-4e68-957f-0e230ca911fb\"}}},\"post_processing_script\":\"# Put the results json into a workflow property so we can call the \\n# convert_json_to_rich_text script to print readable formatted json in an incident note.\\ninputs = results.get(\\\"inputs\\\")\\nartifact_value = inputs.get(\\\"api_void_artifact_value\\\")\\nheader = u\\\"APIVoid DNS Lookup: {0}\\\".format(artifact_value)\\n\\njson_note = {\\n              \\\"version\\\": \\\"1.1\\\",\\n              \\\"header\\\": header, \\n              \\\"json\\\": results.content,\\n              \\\"sort\\\": False\\n            }\\n\\nworkflow.addProperty(\u0027convert_json_to_rich_text\u0027, json_note)\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.api_void_artifact_value = artifact.value\\ninputs.api_void_artifact_type = artifact.type\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1x0rhgh\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_17submi\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1x0rhgh\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0s8m9pf\"/\u003e\u003cendEvent id=\"EndEvent_1t75qk1\"\u003e\u003cincoming\u003eSequenceFlow_0ie761x\u003c/incoming\u003e\u003c/endEvent\u003e\u003cscriptTask id=\"ScriptTask_0p4y4e9\" name=\"Convert JSON to rich text v1.3\"\u003e\u003cextensionElements\u003e\u003cresilient:script programmaticName=\"convert_json_to_rich_text_v13\" uuid=\"559123e6-50df-46a8-b90f-79eaef3211bb\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_17submi\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0ie761x\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"SequenceFlow_17submi\" sourceRef=\"ServiceTask_0s8m9pf\" targetRef=\"ScriptTask_0p4y4e9\"/\u003e\u003csequenceFlow id=\"SequenceFlow_0ie761x\" sourceRef=\"ScriptTask_0p4y4e9\" targetRef=\"EndEvent_1t75qk1\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_17neccc\"\u003e\u003ctext\u003eInput: APIVoid request type, artifact type and value\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1j6nfj3\" sourceRef=\"ServiceTask_0s8m9pf\" targetRef=\"TextAnnotation_17neccc\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0l0j6o7\"\u003e\u003ctext\u003eOutput: JSON results from the\u00a0 APIVoid endpoint\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1i92xej\" sourceRef=\"ServiceTask_0s8m9pf\" targetRef=\"TextAnnotation_0l0j6o7\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1neb6eh\"\u003e\u003ctext\u003eOutput: Incident note\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1h6ux2f\" sourceRef=\"ScriptTask_0p4y4e9\" targetRef=\"TextAnnotation_1neb6eh\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0s8m9pf\" id=\"ServiceTask_0s8m9pf_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"333\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1x0rhgh\" id=\"SequenceFlow_1x0rhgh_di\"\u003e\u003comgdi:waypoint x=\"198\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"264\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"264\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"333\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"90\" x=\"234\" y=\"199\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1t75qk1\" id=\"EndEvent_1t75qk1_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"878\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"90\" x=\"851\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_17neccc\" id=\"TextAnnotation_17neccc_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"226\" y=\"58\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1j6nfj3\" id=\"Association_1j6nfj3_di\"\u003e\u003comgdi:waypoint x=\"351\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"288\" y=\"88\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0l0j6o7\" id=\"TextAnnotation_0l0j6o7_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"450\" y=\"58\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1i92xej\" id=\"Association_1i92xej_di\"\u003e\u003comgdi:waypoint x=\"418\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"487\" y=\"88\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1neb6eh\" id=\"TextAnnotation_1neb6eh_di\"\u003e\u003comgdc:Bounds height=\"39\" width=\"141\" x=\"716\" y=\"77\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_0p4y4e9\" id=\"ScriptTask_0p4y4e9_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"608\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_17submi\" id=\"SequenceFlow_17submi_di\"\u003e\u003comgdi:waypoint x=\"433\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"608\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"520.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0ie761x\" id=\"SequenceFlow_0ie761x_di\"\u003e\u003comgdi:waypoint x=\"708\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"878\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"793\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1h6ux2f\" id=\"Association_1h6ux2f_di\"\u003e\u003comgdi:waypoint x=\"703\" y=\"168\"/\u003e\u003comgdi:waypoint x=\"765\" y=\"116\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 4,
      "description": "Example workflow calls APIVoid dnslookup API to return DNS records of domain names.  The JSON results are written to an incident note.",
      "export_key": "example_apivoid_dns_lookup",
      "last_modified_by": "dummy@dummy.com",
      "last_modified_time": 1698738116909,
      "name": "Example: APIVoid DNS Lookup",
      "object_type": "artifact",
      "programmatic_name": "example_apivoid_dns_lookup",
      "tags": [],
      "uuid": "d9487efb-95f1-4194-99f8-79337e8b7fcc",
      "workflow_id": 135
    },
    {
      "actions": [],
      "content": {
        "version": 3,
        "workflow_id": "example_apivoid_email_verify",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_apivoid_email_verify\" isExecutable=\"true\" name=\"Example: APIVoid Email Verify\"\u003e\u003cdocumentation\u003eExample workflow calls APIVoid emailverify API to return information about the email address.  The JSON results are written to an incident note.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1x0rhgh\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0s8m9pf\" name=\"APIVoid Request\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"39141052-d0b0-4c44-b243-d3eb41d42553\"\u003e{\"inputs\":{\"a17a314a-2747-4e47-84df-7ca50772c78f\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"4314f157-860d-40ba-8b62-84ed627eaab7\"}}},\"post_processing_script\":\"# Put the results json into a workflow property so we can call the \\n# convert_json_to_rich_text script to print readable formatted json in an incident note.\\ninputs = results.get(\\\"inputs\\\")\\nartifact_value = inputs.get(\\\"api_void_artifact_value\\\")\\nheader = u\\\"APIVoid Email Verify: {0}\\\".format(artifact_value)\\n\\njson_note = {\\n              \\\"version\\\": \\\"1.1\\\",\\n              \\\"header\\\": header, \\n              \\\"json\\\": results.content,\\n              \\\"sort\\\": False\\n            }\\n\\nworkflow.addProperty(\u0027convert_json_to_rich_text\u0027, json_note)\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.api_void_artifact_value = artifact.value\\ninputs.api_void_artifact_type = artifact.type\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1x0rhgh\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0ipp2q4\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1x0rhgh\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0s8m9pf\"/\u003e\u003cendEvent id=\"EndEvent_1t75qk1\"\u003e\u003cincoming\u003eSequenceFlow_0ax336o\u003c/incoming\u003e\u003c/endEvent\u003e\u003cscriptTask id=\"ScriptTask_1h4nvip\" name=\"Convert JSON to rich text v1.3\"\u003e\u003cextensionElements\u003e\u003cresilient:script programmaticName=\"convert_json_to_rich_text_v13\" uuid=\"559123e6-50df-46a8-b90f-79eaef3211bb\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0ipp2q4\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0ax336o\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"SequenceFlow_0ipp2q4\" sourceRef=\"ServiceTask_0s8m9pf\" targetRef=\"ScriptTask_1h4nvip\"/\u003e\u003csequenceFlow id=\"SequenceFlow_0ax336o\" sourceRef=\"ScriptTask_1h4nvip\" targetRef=\"EndEvent_1t75qk1\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_17neccc\"\u003e\u003ctext\u003eInput: APIVoid request type, artifact type and value\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1j6nfj3\" sourceRef=\"ServiceTask_0s8m9pf\" targetRef=\"TextAnnotation_17neccc\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0l0j6o7\"\u003e\u003ctext\u003eOutput: JSON results from the\u00a0 APIVoid endpoint\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1i92xej\" sourceRef=\"ServiceTask_0s8m9pf\" targetRef=\"TextAnnotation_0l0j6o7\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1neb6eh\"\u003e\u003ctext\u003eOutput: Incident note\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_03tiy7h\" sourceRef=\"ScriptTask_1h4nvip\" targetRef=\"TextAnnotation_1neb6eh\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0s8m9pf\" id=\"ServiceTask_0s8m9pf_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"333\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1x0rhgh\" id=\"SequenceFlow_1x0rhgh_di\"\u003e\u003comgdi:waypoint x=\"198\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"264\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"264\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"333\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"90\" x=\"234\" y=\"199\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1t75qk1\" id=\"EndEvent_1t75qk1_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"878\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"90\" x=\"851\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_17neccc\" id=\"TextAnnotation_17neccc_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"226\" y=\"58\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1j6nfj3\" id=\"Association_1j6nfj3_di\"\u003e\u003comgdi:waypoint x=\"351\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"288\" y=\"88\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0l0j6o7\" id=\"TextAnnotation_0l0j6o7_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"450\" y=\"58\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1i92xej\" id=\"Association_1i92xej_di\"\u003e\u003comgdi:waypoint x=\"418\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"487\" y=\"88\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1neb6eh\" id=\"TextAnnotation_1neb6eh_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"692\" y=\"73\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_1h4nvip\" id=\"ScriptTask_1h4nvip_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"575\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0ipp2q4\" id=\"SequenceFlow_0ipp2q4_di\"\u003e\u003comgdi:waypoint x=\"433\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"575\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"504\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0ax336o\" id=\"SequenceFlow_0ax336o_di\"\u003e\u003comgdi:waypoint x=\"675\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"878\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"776.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_03tiy7h\" id=\"Association_03tiy7h_di\"\u003e\u003comgdi:waypoint x=\"665\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"727\" y=\"103\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 3,
      "description": "Example workflow calls APIVoid emailverify API to return information about the email address.  The JSON results are written to an incident note.",
      "export_key": "example_apivoid_email_verify",
      "last_modified_by": "dummy@dummy.com",
      "last_modified_time": 1698738139087,
      "name": "Example: APIVoid Email Verify",
      "object_type": "artifact",
      "programmatic_name": "example_apivoid_email_verify",
      "tags": [],
      "uuid": "161e8e71-1ff8-4289-a7f0-93d6b0ad0574",
      "workflow_id": 137
    },
    {
      "actions": [],
      "content": {
        "version": 3,
        "workflow_id": "example_apivoid_ip_reputation",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_apivoid_ip_reputation\" isExecutable=\"true\" name=\"Example: APIVoid IP Reputation\"\u003e\u003cdocumentation\u003eExample workflow that makes a call the to APIVoid iprep endpoint. The JSON results are written to an incident note.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1181mnz\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_19hqzke\" name=\"APIVoid Request\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"39141052-d0b0-4c44-b243-d3eb41d42553\"\u003e{\"inputs\":{\"a17a314a-2747-4e47-84df-7ca50772c78f\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"7ff85ec3-9ccd-4fee-8166-37e816e72385\"}}},\"post_processing_script\":\"# Put the results json into a workflow property so we can call the \\n# convert_json_to_rich_text script to print readable formatted json in an incident note.\\ninputs = results.get(\\\"inputs\\\")\\nartifact_value = inputs.get(\\\"api_void_artifact_value\\\")\\nheader = u\\\"APIVoid IP Reputation: {0}\\\".format(artifact_value)\\n\\njson_note = {\\n              \\\"version\\\": \\\"1.1\\\",\\n              \\\"header\\\": header, \\n              \\\"json\\\": results.content,\\n              \\\"sort\\\": False\\n            }\\n\\nworkflow.addProperty(\u0027convert_json_to_rich_text\u0027, json_note)\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.api_void_artifact_type = artifact.type\\ninputs.api_void_artifact_value = artifact.value\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1181mnz\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0pbdlxj\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1181mnz\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_19hqzke\"/\u003e\u003cendEvent id=\"EndEvent_1r8pngi\"\u003e\u003cincoming\u003eSequenceFlow_1hlpuek\u003c/incoming\u003e\u003c/endEvent\u003e\u003cscriptTask id=\"ScriptTask_1b9mrme\" name=\"Convert JSON to rich text v1.3\"\u003e\u003cextensionElements\u003e\u003cresilient:script programmaticName=\"convert_json_to_rich_text_v13\" uuid=\"559123e6-50df-46a8-b90f-79eaef3211bb\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0pbdlxj\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1hlpuek\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"SequenceFlow_0pbdlxj\" sourceRef=\"ServiceTask_19hqzke\" targetRef=\"ScriptTask_1b9mrme\"/\u003e\u003csequenceFlow id=\"SequenceFlow_1hlpuek\" sourceRef=\"ScriptTask_1b9mrme\" targetRef=\"EndEvent_1r8pngi\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0h7y4d3\"\u003e\u003ctext\u003eInput: APIVoid request type, artifact type and value\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1i5dgn1\" sourceRef=\"ServiceTask_19hqzke\" targetRef=\"TextAnnotation_0h7y4d3\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0miajjp\"\u003e\u003ctext\u003eOutput: JSON results\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1ch45km\" sourceRef=\"ServiceTask_19hqzke\" targetRef=\"TextAnnotation_0miajjp\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1ejjaxs\"\u003e\u003ctext\u003eOutput: Incident note\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0xe9txn\" sourceRef=\"ScriptTask_1b9mrme\" targetRef=\"TextAnnotation_1ejjaxs\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_19hqzke\" id=\"ServiceTask_19hqzke_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"355\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1181mnz\" id=\"SequenceFlow_1181mnz_di\"\u003e\u003comgdi:waypoint x=\"198\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"355\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"276.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1r8pngi\" id=\"EndEvent_1r8pngi_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"837\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"0\" x=\"855\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0h7y4d3\" id=\"TextAnnotation_0h7y4d3_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"243\" y=\"62\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1i5dgn1\" id=\"Association_1i5dgn1_di\"\u003e\u003comgdi:waypoint x=\"370\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"306\" y=\"92\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0miajjp\" id=\"TextAnnotation_0miajjp_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"443\" y=\"62\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1ch45km\" id=\"Association_1ch45km_di\"\u003e\u003comgdi:waypoint x=\"432\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"483\" y=\"92\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1ejjaxs\" id=\"TextAnnotation_1ejjaxs_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"706\" y=\"62\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_1b9mrme\" id=\"ScriptTask_1b9mrme_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"576\" y=\"154\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0pbdlxj\" id=\"SequenceFlow_0pbdlxj_di\"\u003e\u003comgdi:waypoint x=\"455\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"516\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"516\" y=\"194\"/\u003e\u003comgdi:waypoint x=\"576\" y=\"194\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"531\" y=\"193\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1hlpuek\" id=\"SequenceFlow_1hlpuek_di\"\u003e\u003comgdi:waypoint x=\"676\" y=\"194\"/\u003e\u003comgdi:waypoint x=\"757\" y=\"194\"/\u003e\u003comgdi:waypoint x=\"757\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"837\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"772\" y=\"193\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0xe9txn\" id=\"Association_0xe9txn_di\"\u003e\u003comgdi:waypoint x=\"669\" y=\"155\"/\u003e\u003comgdi:waypoint x=\"739\" y=\"92\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 3,
      "description": "Example workflow that makes a call the to APIVoid iprep endpoint. The JSON results are written to an incident note.",
      "export_key": "example_apivoid_ip_reputation",
      "last_modified_by": "dummy@dummy.com",
      "last_modified_time": 1698738152297,
      "name": "Example: APIVoid IP Reputation",
      "object_type": "artifact",
      "programmatic_name": "example_apivoid_ip_reputation",
      "tags": [],
      "uuid": "9ff44615-0f0c-496a-9399-6916d34d75c6",
      "workflow_id": 138
    },
    {
      "actions": [],
      "content": {
        "version": 4,
        "workflow_id": "example_apivoid_ssl_info",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_apivoid_ssl_info\" isExecutable=\"true\" name=\"Example: APIVoid SSL Info\"\u003e\u003cdocumentation\u003eExample workflow calls APIVoid sslinfo API to returns the details of a website\u0027s SSL certificate.  The JSON results are written to an incident note.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1x0rhgh\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0s8m9pf\" name=\"APIVoid Request\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"39141052-d0b0-4c44-b243-d3eb41d42553\"\u003e{\"inputs\":{\"a17a314a-2747-4e47-84df-7ca50772c78f\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"15185469-692c-4000-8220-2b22dee4a6f3\"}}},\"post_processing_script\":\"# Put the results json into a workflow property so we can call the \\n# convert_json_to_rich_text script to print readable formatted json in an incident note.\\ninputs = results.get(\\\"inputs\\\")\\nartifact_value = inputs.get(\\\"api_void_artifact_value\\\")\\nheader = u\\\"APIVoid SSL Info: {0}\\\".format(artifact_value)\\n\\njson_note = {\\n              \\\"version\\\": \\\"1.1\\\",\\n              \\\"header\\\": header, \\n              \\\"json\\\": results.content,\\n              \\\"sort\\\": False\\n            }\\n\\nworkflow.addProperty(\u0027convert_json_to_rich_text\u0027, json_note)\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.api_void_artifact_value = artifact.value\\ninputs.api_void_artifact_type = artifact.type\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1x0rhgh\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0932qu4\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1x0rhgh\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0s8m9pf\"/\u003e\u003cendEvent id=\"EndEvent_1t75qk1\"\u003e\u003cincoming\u003eSequenceFlow_0v7m37n\u003c/incoming\u003e\u003c/endEvent\u003e\u003cscriptTask id=\"ScriptTask_1fzs48a\" name=\"Convert JSON to rich text v1.3\"\u003e\u003cextensionElements\u003e\u003cresilient:script programmaticName=\"convert_json_to_rich_text_v13\" uuid=\"559123e6-50df-46a8-b90f-79eaef3211bb\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0932qu4\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0v7m37n\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"SequenceFlow_0932qu4\" sourceRef=\"ServiceTask_0s8m9pf\" targetRef=\"ScriptTask_1fzs48a\"/\u003e\u003csequenceFlow id=\"SequenceFlow_0v7m37n\" sourceRef=\"ScriptTask_1fzs48a\" targetRef=\"EndEvent_1t75qk1\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_17neccc\"\u003e\u003ctext\u003eInput: APIVoid request type, artifact type and value\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1j6nfj3\" sourceRef=\"ServiceTask_0s8m9pf\" targetRef=\"TextAnnotation_17neccc\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0l0j6o7\"\u003e\u003ctext\u003eOutput: JSON results from the\u00a0 APIVoid endpoint\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1i92xej\" sourceRef=\"ServiceTask_0s8m9pf\" targetRef=\"TextAnnotation_0l0j6o7\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1neb6eh\"\u003e\u003ctext\u003eOutput: Incident note\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0ddt0iy\" sourceRef=\"ScriptTask_1fzs48a\" targetRef=\"TextAnnotation_1neb6eh\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0s8m9pf\" id=\"ServiceTask_0s8m9pf_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"333\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1x0rhgh\" id=\"SequenceFlow_1x0rhgh_di\"\u003e\u003comgdi:waypoint x=\"198\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"264\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"264\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"333\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"90\" x=\"234\" y=\"199\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1t75qk1\" id=\"EndEvent_1t75qk1_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"878\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"90\" x=\"851\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_17neccc\" id=\"TextAnnotation_17neccc_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"226\" y=\"58\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1j6nfj3\" id=\"Association_1j6nfj3_di\"\u003e\u003comgdi:waypoint x=\"351\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"288\" y=\"88\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0l0j6o7\" id=\"TextAnnotation_0l0j6o7_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"450\" y=\"58\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1i92xej\" id=\"Association_1i92xej_di\"\u003e\u003comgdi:waypoint x=\"418\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"487\" y=\"88\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1neb6eh\" id=\"TextAnnotation_1neb6eh_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"692\" y=\"73\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_1fzs48a\" id=\"ScriptTask_1fzs48a_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"594\" y=\"155\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0932qu4\" id=\"SequenceFlow_0932qu4_di\"\u003e\u003comgdi:waypoint x=\"433\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"514\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"514\" y=\"195\"/\u003e\u003comgdi:waypoint x=\"594\" y=\"195\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"529\" y=\"193.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0v7m37n\" id=\"SequenceFlow_0v7m37n_di\"\u003e\u003comgdi:waypoint x=\"694\" y=\"195\"/\u003e\u003comgdi:waypoint x=\"786\" y=\"195\"/\u003e\u003comgdi:waypoint x=\"786\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"878\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"801\" y=\"193.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0ddt0iy\" id=\"Association_0ddt0iy_di\"\u003e\u003comgdi:waypoint x=\"681\" y=\"155\"/\u003e\u003comgdi:waypoint x=\"728\" y=\"103\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 4,
      "description": "Example workflow calls APIVoid sslinfo API to returns the details of a website\u0027s SSL certificate.  The JSON results are written to an incident note.",
      "export_key": "example_apivoid_ssl_info",
      "last_modified_by": "dummy@dummy.com",
      "last_modified_time": 1698739636012,
      "name": "Example: APIVoid SSL Info",
      "object_type": "artifact",
      "programmatic_name": "example_apivoid_ssl_info",
      "tags": [],
      "uuid": "f6e2c164-b9aa-4cc9-acdc-5cdad90e007d",
      "workflow_id": 136
    },
    {
      "actions": [],
      "content": {
        "version": 3,
        "workflow_id": "example_apivoid_domain_reputation",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_apivoid_domain_reputation\" isExecutable=\"true\" name=\"Example: APIVoid Domain Reputation\"\u003e\u003cdocumentation\u003eExample workflow calls APIVoid domainbl API to check if the domain name is blacklisted.  The JSON results are written to an incident note.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1x0rhgh\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0s8m9pf\" name=\"APIVoid Request\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"39141052-d0b0-4c44-b243-d3eb41d42553\"\u003e{\"inputs\":{\"a17a314a-2747-4e47-84df-7ca50772c78f\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"7e0d15ad-f691-4305-8834-9818a7fa8400\"}}},\"post_processing_script\":\"# Put the results json into a workflow property so we can call the \\n# convert_json_to_rich_text script to print readable formatted json in an incident note.\\ninputs = results.get(\\\"inputs\\\")\\nartifact_value = inputs.get(\\\"api_void_artifact_value\\\")\\nheader = u\\\"APIVoid Domain Reputation: {0}\\\".format(artifact_value)\\n\\njson_note = {\\n              \\\"version\\\": \\\"1.1\\\",\\n              \\\"header\\\": header, \\n              \\\"json\\\": results.content,\\n              \\\"sort\\\": False\\n            }\\n\\nworkflow.addProperty(\u0027convert_json_to_rich_text\u0027, json_note)\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.api_void_artifact_value = artifact.value\\ninputs.api_void_artifact_type = artifact.type\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1x0rhgh\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1i08900\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1x0rhgh\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0s8m9pf\"/\u003e\u003cendEvent id=\"EndEvent_1t75qk1\"\u003e\u003cincoming\u003eSequenceFlow_037akqa\u003c/incoming\u003e\u003c/endEvent\u003e\u003cscriptTask id=\"ScriptTask_0laiu83\" name=\"Convert JSON to rich text v1.3\"\u003e\u003cextensionElements\u003e\u003cresilient:script programmaticName=\"convert_json_to_rich_text_v13\" uuid=\"559123e6-50df-46a8-b90f-79eaef3211bb\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1i08900\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_037akqa\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"SequenceFlow_1i08900\" sourceRef=\"ServiceTask_0s8m9pf\" targetRef=\"ScriptTask_0laiu83\"/\u003e\u003csequenceFlow id=\"SequenceFlow_037akqa\" sourceRef=\"ScriptTask_0laiu83\" targetRef=\"EndEvent_1t75qk1\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_17neccc\"\u003e\u003ctext\u003eInput: APIVoid request type, artifact type and value\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1j6nfj3\" sourceRef=\"ServiceTask_0s8m9pf\" targetRef=\"TextAnnotation_17neccc\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0l0j6o7\"\u003e\u003ctext\u003eOutput: JSON results from the\u00a0 APIVoid endpoint\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1i92xej\" sourceRef=\"ServiceTask_0s8m9pf\" targetRef=\"TextAnnotation_0l0j6o7\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1neb6eh\"\u003e\u003ctext\u003eOutput: Incident note\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_10sovyz\" sourceRef=\"ScriptTask_0laiu83\" targetRef=\"TextAnnotation_1neb6eh\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0s8m9pf\" id=\"ServiceTask_0s8m9pf_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"333\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1x0rhgh\" id=\"SequenceFlow_1x0rhgh_di\"\u003e\u003comgdi:waypoint x=\"198\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"264\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"264\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"333\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"90\" x=\"234\" y=\"199\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1t75qk1\" id=\"EndEvent_1t75qk1_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"878\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"90\" x=\"851\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_17neccc\" id=\"TextAnnotation_17neccc_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"226\" y=\"58\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1j6nfj3\" id=\"Association_1j6nfj3_di\"\u003e\u003comgdi:waypoint x=\"351\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"288\" y=\"88\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0l0j6o7\" id=\"TextAnnotation_0l0j6o7_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"450\" y=\"58\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1i92xej\" id=\"Association_1i92xej_di\"\u003e\u003comgdi:waypoint x=\"418\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"487\" y=\"88\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1neb6eh\" id=\"TextAnnotation_1neb6eh_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"692\" y=\"73\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_0laiu83\" id=\"ScriptTask_0laiu83_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"603\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1i08900\" id=\"SequenceFlow_1i08900_di\"\u003e\u003comgdi:waypoint x=\"433\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"603\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"518\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_037akqa\" id=\"SequenceFlow_037akqa_di\"\u003e\u003comgdi:waypoint x=\"703\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"878\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"790.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_10sovyz\" id=\"Association_10sovyz_di\"\u003e\u003comgdi:waypoint x=\"683\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"731\" y=\"103\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 3,
      "description": "Example workflow calls APIVoid domainbl API to check if the domain name is blacklisted.  The JSON results are written to an incident note.",
      "export_key": "example_apivoid_domain_reputation",
      "last_modified_by": "dummy@dummy.com",
      "last_modified_time": 1698738125772,
      "name": "Example: APIVoid Domain Reputation",
      "object_type": "artifact",
      "programmatic_name": "example_apivoid_domain_reputation",
      "tags": [],
      "uuid": "f3995322-a468-407e-a008-bec3bee074e6",
      "workflow_id": 139
    },
    {
      "actions": [],
      "content": {
        "version": 3,
        "workflow_id": "example_apivoid_threatlog",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_apivoid_threatlog\" isExecutable=\"true\" name=\"Example: APIVoid ThreatLog\"\u003e\u003cdocumentation\u003eExample workflow calls APIVoid threatlog API to query the ThreatLog.com database of malicious domains.  The JSON results are written to an incident note.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1x0rhgh\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0s8m9pf\" name=\"APIVoid Request\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"39141052-d0b0-4c44-b243-d3eb41d42553\"\u003e{\"inputs\":{\"a17a314a-2747-4e47-84df-7ca50772c78f\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"de2a6cdf-6cab-4849-b386-8586346f96aa\"}}},\"post_processing_script\":\"# Put the results json into a workflow property so we can call the \\n# convert_json_to_rich_text script to print readable formatted json in an incident note.\\ninputs = results.get(\\\"inputs\\\")\\nartifact_value = inputs.get(\\\"api_void_artifact_value\\\")\\nheader = u\\\"APIVoid ThreatLog: {0}\\\".format(artifact_value)\\n\\njson_note = {\\n              \\\"version\\\": \\\"1.1\\\",\\n              \\\"header\\\": header, \\n              \\\"json\\\": results.content,\\n              \\\"sort\\\": False\\n            }\\n\\nworkflow.addProperty(\u0027convert_json_to_rich_text\u0027, json_note)\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.api_void_artifact_value = artifact.value\\ninputs.api_void_artifact_type = artifact.type\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1x0rhgh\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0125mfg\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1x0rhgh\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0s8m9pf\"/\u003e\u003cendEvent id=\"EndEvent_1t75qk1\"\u003e\u003cincoming\u003eSequenceFlow_0zv8la6\u003c/incoming\u003e\u003c/endEvent\u003e\u003cscriptTask id=\"ScriptTask_020xcn0\" name=\"Convert JSON to rich text v1.3\"\u003e\u003cextensionElements\u003e\u003cresilient:script programmaticName=\"convert_json_to_rich_text_v13\" uuid=\"559123e6-50df-46a8-b90f-79eaef3211bb\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0125mfg\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0zv8la6\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"SequenceFlow_0125mfg\" sourceRef=\"ServiceTask_0s8m9pf\" targetRef=\"ScriptTask_020xcn0\"/\u003e\u003csequenceFlow id=\"SequenceFlow_0zv8la6\" sourceRef=\"ScriptTask_020xcn0\" targetRef=\"EndEvent_1t75qk1\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_17neccc\"\u003e\u003ctext\u003eInput: APIVoid request type, artifact type and value\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1j6nfj3\" sourceRef=\"ServiceTask_0s8m9pf\" targetRef=\"TextAnnotation_17neccc\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0l0j6o7\"\u003e\u003ctext\u003eOutput: JSON results from the\u00a0 APIVoid endpoint\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1i92xej\" sourceRef=\"ServiceTask_0s8m9pf\" targetRef=\"TextAnnotation_0l0j6o7\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1neb6eh\"\u003e\u003ctext\u003eOutput: Incident note\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_160ow3e\" sourceRef=\"ScriptTask_020xcn0\" targetRef=\"TextAnnotation_1neb6eh\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0s8m9pf\" id=\"ServiceTask_0s8m9pf_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"333\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1x0rhgh\" id=\"SequenceFlow_1x0rhgh_di\"\u003e\u003comgdi:waypoint x=\"198\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"264\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"264\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"333\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"90\" x=\"234\" y=\"199\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1t75qk1\" id=\"EndEvent_1t75qk1_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"878\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"90\" x=\"851\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_17neccc\" id=\"TextAnnotation_17neccc_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"226\" y=\"58\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1j6nfj3\" id=\"Association_1j6nfj3_di\"\u003e\u003comgdi:waypoint x=\"351\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"288\" y=\"88\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0l0j6o7\" id=\"TextAnnotation_0l0j6o7_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"450\" y=\"58\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1i92xej\" id=\"Association_1i92xej_di\"\u003e\u003comgdi:waypoint x=\"418\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"487\" y=\"88\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1neb6eh\" id=\"TextAnnotation_1neb6eh_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"692\" y=\"73\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_020xcn0\" id=\"ScriptTask_020xcn0_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"558\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0125mfg\" id=\"SequenceFlow_0125mfg_di\"\u003e\u003comgdi:waypoint x=\"433\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"558\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"495.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0zv8la6\" id=\"SequenceFlow_0zv8la6_di\"\u003e\u003comgdi:waypoint x=\"658\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"878\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"768\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_160ow3e\" id=\"Association_160ow3e_di\"\u003e\u003comgdi:waypoint x=\"652\" y=\"167\"/\u003e\u003comgdi:waypoint x=\"725\" y=\"103\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 3,
      "description": "Example workflow calls APIVoid threatlog API to query the ThreatLog.com database of malicious domains.  The JSON results are written to an incident note.",
      "export_key": "example_apivoid_threatlog",
      "last_modified_by": "dummy@dummy.com",
      "last_modified_time": 1698738170243,
      "name": "Example: APIVoid ThreatLog",
      "object_type": "artifact",
      "programmatic_name": "example_apivoid_threatlog",
      "tags": [],
      "uuid": "5d7bdd04-c0e8-4ba9-8030-36505533db33",
      "workflow_id": 134
    },
    {
      "actions": [],
      "content": {
        "version": 4,
        "workflow_id": "example_apivoid_url_reputation",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"example_apivoid_url_reputation\" isExecutable=\"true\" name=\"Example: APIVoid URL Reputation\"\u003e\u003cdocumentation\u003eExample workflow calls APIVoid urlrep API to return information on the URL.  The JSON results are written to an incident note.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1x0rhgh\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0s8m9pf\" name=\"APIVoid Request\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"39141052-d0b0-4c44-b243-d3eb41d42553\"\u003e{\"inputs\":{\"a17a314a-2747-4e47-84df-7ca50772c78f\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"72665ba2-3ec2-4fd4-a2fa-17b2a0f85890\"}}},\"post_processing_script\":\"# Put the results json into a workflow property so we can call the \\n# convert_json_to_rich_text script to print readable formatted json in an incident note.\\ninputs = results.get(\\\"inputs\\\")\\nartifact_value = inputs.get(\\\"api_void_artifact_value\\\")\\nheader = u\\\"APIVoid URL Reputation: {0}\\\".format(artifact_value)\\n\\njson_note = {\\n              \\\"version\\\": \\\"1.1\\\",\\n              \\\"header\\\": header, \\n              \\\"json\\\": results.content,\\n              \\\"sort\\\": False\\n            }\\n\\nworkflow.addProperty(\u0027convert_json_to_rich_text\u0027, json_note)\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.api_void_artifact_value = artifact.value\\ninputs.api_void_artifact_type = artifact.type\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1x0rhgh\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1yag6bx\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1x0rhgh\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0s8m9pf\"/\u003e\u003cendEvent id=\"EndEvent_1t75qk1\"\u003e\u003cincoming\u003eSequenceFlow_06a229l\u003c/incoming\u003e\u003c/endEvent\u003e\u003cscriptTask id=\"ScriptTask_0kylfar\" name=\"Convert JSON to rich text v1.3\"\u003e\u003cextensionElements\u003e\u003cresilient:script programmaticName=\"convert_json_to_rich_text_v13\" uuid=\"559123e6-50df-46a8-b90f-79eaef3211bb\"/\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1yag6bx\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_06a229l\u003c/outgoing\u003e\u003cscript\u003escript\u003c/script\u003e\u003c/scriptTask\u003e\u003csequenceFlow id=\"SequenceFlow_1yag6bx\" sourceRef=\"ServiceTask_0s8m9pf\" targetRef=\"ScriptTask_0kylfar\"/\u003e\u003csequenceFlow id=\"SequenceFlow_06a229l\" sourceRef=\"ScriptTask_0kylfar\" targetRef=\"EndEvent_1t75qk1\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_17neccc\"\u003e\u003ctext\u003eInput: APIVoid request type, artifact type and value\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1j6nfj3\" sourceRef=\"ServiceTask_0s8m9pf\" targetRef=\"TextAnnotation_17neccc\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0l0j6o7\"\u003e\u003ctext\u003eOutput: JSON results from the\u00a0 APIVoid endpoint\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1i92xej\" sourceRef=\"ServiceTask_0s8m9pf\" targetRef=\"TextAnnotation_0l0j6o7\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1neb6eh\"\u003e\u003ctext\u003eOutput: Incident note\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0kp8ir6\" sourceRef=\"ScriptTask_0kylfar\" targetRef=\"TextAnnotation_1neb6eh\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0s8m9pf\" id=\"ServiceTask_0s8m9pf_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"333\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1x0rhgh\" id=\"SequenceFlow_1x0rhgh_di\"\u003e\u003comgdi:waypoint x=\"198\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"264\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"264\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"333\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"90\" x=\"234\" y=\"199\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1t75qk1\" id=\"EndEvent_1t75qk1_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"878\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"90\" x=\"851\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_17neccc\" id=\"TextAnnotation_17neccc_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"226\" y=\"58\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1j6nfj3\" id=\"Association_1j6nfj3_di\"\u003e\u003comgdi:waypoint x=\"351\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"288\" y=\"88\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0l0j6o7\" id=\"TextAnnotation_0l0j6o7_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"450\" y=\"58\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1i92xej\" id=\"Association_1i92xej_di\"\u003e\u003comgdi:waypoint x=\"418\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"487\" y=\"88\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1neb6eh\" id=\"TextAnnotation_1neb6eh_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"692\" y=\"73\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ScriptTask_0kylfar\" id=\"ScriptTask_0kylfar_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"577\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1yag6bx\" id=\"SequenceFlow_1yag6bx_di\"\u003e\u003comgdi:waypoint x=\"433\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"577\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"505\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_06a229l\" id=\"SequenceFlow_06a229l_di\"\u003e\u003comgdi:waypoint x=\"677\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"878\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"777.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0kp8ir6\" id=\"Association_0kp8ir6_di\"\u003e\u003comgdi:waypoint x=\"666\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"727\" y=\"103\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 4,
      "description": "Example workflow calls APIVoid urlrep API to return information on the URL.  The JSON results are written to an incident note.",
      "export_key": "example_apivoid_url_reputation",
      "last_modified_by": "dummy@dummy.com",
      "last_modified_time": 1698739734873,
      "name": "Example: APIVoid URL Reputation",
      "object_type": "artifact",
      "programmatic_name": "example_apivoid_url_reputation",
      "tags": [],
      "uuid": "123d4cf4-0cb0-4aeb-9610-88855be1efb8",
      "workflow_id": 140
    }
  ],
  "workspaces": []
}
