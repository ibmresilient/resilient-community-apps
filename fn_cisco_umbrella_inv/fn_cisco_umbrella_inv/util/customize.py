# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_cisco_umbrella_inv"""

from __future__ import print_function
from resilient_circuits.util import *


def customization_data(client=None):
    """Produce any customization definitions (types, fields, message destinations, etc)
       that should be installed by `resilient-circuits customize`
    """

    # Function-field definitions
    yield TypeDefinition(
        {
            "type_name": "__function",
            "fields": { '29bf736d-87de-48fc-85b7-4dcc04670c48': { 'blank_option': False,
                                            'input_type': 'text',
                                            'name': 'resource',
                                            'placeholder': '',
                                            'required': 'always',
                                            'rich_text': False,
                                            'templates': [],
                                            'text': 'resource',
                                            'tooltip': 'Input parameter for Cisco Umbrella investigate.Commonly will be ipaddress, domain or URL',
                                            'uuid': '29bf736d-87de-48fc-85b7-4dcc04670c48',
                                            'values': []},
  '2b9d77ae-efaa-45ef-a64f-8a3f763ba58d': { 'blank_option': False,
                                            'input_type': 'datetimepicker',
                                            'name': 'start_epoch',
                                            'placeholder': '',
                                            'rich_text': False,
                                            'templates': [],
                                            'text': 'start_epoch',
                                            'tooltip': 'Start time in Unix epoch',
                                            'uuid': '2b9d77ae-efaa-45ef-a64f-8a3f763ba58d',
                                            'values': []},
  '583d07bc-4086-48b8-a07f-287765b735a8': { 'blank_option': False,
                                            'input_type': 'text',
                                            'name': 'domain',
                                            'placeholder': '',
                                            'required': 'always',
                                            'rich_text': False,
                                            'templates': [],
                                            'text': 'domain',
                                            'tooltip': 'Domains Input parameter for Cisco Umbrella investigate. Will be a domain name.',
                                            'uuid': '583d07bc-4086-48b8-a07f-287765b735a8',
                                            'values': []},
  '8834d538-cabd-4d3e-a822-c89f4f96a3d7': { 'blank_option': False,
                                            'input_type': 'text',
                                            'name': 'start_relative',
                                            'placeholder': '',
                                            'rich_text': False,
                                            'templates': [],
                                            'text': 'start_relative',
                                            'tooltip': 'Start time in relative format.',
                                            'uuid': '8834d538-cabd-4d3e-a822-c89f4f96a3d7',
                                            'values': []},
  '9e516a4b-9785-4802-bdac-575a6a51f430': { 'blank_option': False,
                                            'input_type': 'number',
                                            'name': 'limit',
                                            'placeholder': '',
                                            'rich_text': False,
                                            'templates': [],
                                            'text': 'limit',
                                            'tooltip': 'Maximum number of results for endpoint',
                                            'uuid': '9e516a4b-9785-4802-bdac-575a6a51f430',
                                            'values': []},
  'a193c91a-66fa-43f1-a67c-3f080f51f894': { 'blank_option': False,
                                            'input_type': 'text',
                                            'name': 'domains',
                                            'placeholder': '',
                                            'rich_text': False,
                                            'templates': [],
                                            'text': 'domains',
                                            'tooltip': 'Domains Input parameter for Cisco Umbrella investigate. Will be domain name or  list of domains.',
                                            'uuid': 'a193c91a-66fa-43f1-a67c-3f080f51f894',
                                            'values': []},
  'a5e6e21f-b9f0-4168-beb8-0a41c778705c': { 'blank_option': False,
                                            'input_type': 'text',
                                            'name': 'regex',
                                            'placeholder': '',
                                            'rich_text': False,
                                            'templates': [],
                                            'text': 'regex',
                                            'tooltip': 'Search pattern regular expression',
                                            'uuid': 'a5e6e21f-b9f0-4168-beb8-0a41c778705c',
                                            'values': []},
  'a6861c26-9f13-4aef-921c-26cc0d4d3016': { 'blank_option': False,
                                            'input_type': 'select',
                                            'name': 'dns_type',
                                            'placeholder': '',
                                            'rich_text': False,
                                            'templates': [],
                                            'text': 'dns_type',
                                            'tooltip': 'NS record query type for a domain or ip address.',
                                            'uuid': 'a6861c26-9f13-4aef-921c-26cc0d4d3016',
                                            'values': [ { 'label': 'A'},
                                                        { 'label': 'NS'},
                                                        { 'label': 'MX'},
                                                        { 'label': 'TXT'},
                                                        { 'label': 'CNAME'}]},
  'ace816e4-59f1-4df1-8356-5dfe300c35f7': { 'blank_option': False,
                                            'input_type': 'boolean',
                                            'name': 'include_category',
                                            'placeholder': '',
                                            'rich_text': False,
                                            'templates': [],
                                            'text': 'include_category',
                                            'tooltip': 'If set to true this will include security categories in the results.',
                                            'uuid': 'ace816e4-59f1-4df1-8356-5dfe300c35f7',
                                            'values': []},
  'e589cb42-c2a7-4220-a50f-ad24b75bfdad': { 'blank_option': False,
                                            'input_type': 'text',
                                            'name': 'ipaddr',
                                            'placeholder': '',
                                            'required': 'always',
                                            'rich_text': False,
                                            'templates': [],
                                            'text': 'ipaddr',
                                            'tooltip': 'Domains Input parameter for Cisco Umbrella investigate. Will be an id address..',
                                            'uuid': 'e589cb42-c2a7-4220-a50f-ad24b75bfdad',
                                            'values': []},
  'e5fdd9e4-3dfe-471d-8677-75242b78dc55': { 'blank_option': False,
                                            'input_type': 'select',
                                            'name': 'status_endpoint',
                                            'placeholder': '',
                                            'required': 'always',
                                            'rich_text': False,
                                            'templates': [],
                                            'text': 'status_endpoint',
                                            'tooltip': 'Chose between list categories or query categorizations.',
                                            'uuid': 'e5fdd9e4-3dfe-471d-8677-75242b78dc55',
                                            'values': [ { 'label': 'categorization'},
                                                        { 'label': 'categories'}]},
  'fbf6a1a1-31a2-4ff4-ad53-3756657c841f': { 'blank_option': True,
                                            'input_type': 'boolean',
                                            'name': 'showlabels',
                                            'placeholder': '',
                                            'required': 'always',
                                            'rich_text': False,
                                            'templates': [],
                                            'text': 'showlabels',
                                            'tooltip': 'Boolean - Get human-readable labels',
                                            'uuid': 'fbf6a1a1-31a2-4ff4-ad53-3756657c841f',
                                            'values': []}}
        }
    )

    # Message destination: 'umbrella_investigate'
    yield MessageDestinationDefinition({ 'destination_type': 0,
  'expect_ack': True,
  'name': 'umbrella_investigate',
  'programmatic_name': 'umbrella_investigate'}
    )

    # Function: 'umbrella_pattern_search'
    yield FunctionDefinition({ 'description': { 'content': 'Resilient Function : Cisco Umbrella Investigate for Pattern Search.',
                   'format': 'text'},
  'destination_handle': 'umbrella_investigate',
  'display_name': 'umbrella_pattern_search',
  'name': 'umbrella_pattern_search',
  'uuid': '6a572468-0503-4d01-bd46-83fb5b0e735e',
  'view_items': [ { 'content': 'a5e6e21f-b9f0-4168-beb8-0a41c778705c',
                    'element': 'field_uuid',
                    'field_type': '__function'},
                  { 'content': '2b9d77ae-efaa-45ef-a64f-8a3f763ba58d',
                    'element': 'field_uuid',
                    'field_type': '__function'},
                  { 'content': '8834d538-cabd-4d3e-a822-c89f4f96a3d7',
                    'element': 'field_uuid',
                    'field_type': '__function'},
                  { 'content': '9e516a4b-9785-4802-bdac-575a6a51f430',
                    'element': 'field_uuid',
                    'field_type': '__function'},
                  { 'content': 'ace816e4-59f1-4df1-8356-5dfe300c35f7',
                    'element': 'field_uuid',
                    'field_type': '__function'}]}
    )

    # Function: 'umbrella_domain_status_and_category'
    yield FunctionDefinition({ 'description': { 'content': 'Resilient Function : Cisco Umbrella Investigate for Domain Status and Categorization.',
                   'format': 'text'},
  'destination_handle': 'umbrella_investigate',
  'display_name': 'umbrella_domain_status_and_category',
  'name': 'umbrella_domain_status_and_category',
  'uuid': '854eb807-339a-41fb-b589-cf693b8d8de9',
  'view_items': [ { 'content': 'a193c91a-66fa-43f1-a67c-3f080f51f894',
                    'element': 'field_uuid',
                    'field_type': '__function'},
                  { 'content': 'fbf6a1a1-31a2-4ff4-ad53-3756657c841f',
                    'element': 'field_uuid',
                    'field_type': '__function'},
                  { 'content': 'e5fdd9e4-3dfe-471d-8677-75242b78dc55',
                    'element': 'field_uuid',
                    'field_type': '__function'}]}
    )

    # Function: 'umbrella_ip_latest_malicious_domains'
    yield FunctionDefinition({ 'description': { 'content': 'Resilient Function : Cisco Umbrella Investigate for Latest Malicious Domains for an IP.',
                   'format': 'text'},
  'destination_handle': 'umbrella_investigate',
  'display_name': 'umbrella_ip_latest_malicious_domains',
  'name': 'umbrella_ip_latest_malicious_domains',
  'uuid': '34bcb96e-a637-4bbe-8afe-e7190498c3ad',
  'view_items': [ { 'content': 'e589cb42-c2a7-4220-a50f-ad24b75bfdad',
                    'element': 'field_uuid',
                    'field_type': '__function'}]}
    )

    # Function: 'umbrella_dns_rr_hist'
    yield FunctionDefinition({ 'description': { 'content': 'Resilient Function : Cisco Umbrella Investigate for DNS RR History for a IP, Type and Domain Name',
                   'format': 'text'},
  'destination_handle': 'umbrella_investigate',
  'display_name': 'umbrella_dns_rr_hist',
  'name': 'umbrella_dns_rr_hist',
  'uuid': '17d63049-9b1e-41d3-97a5-49fd32d6a74d',
  'view_items': [ { 'content': '29bf736d-87de-48fc-85b7-4dcc04670c48',
                    'element': 'field_uuid',
                    'field_type': '__function'},
                  { 'content': 'a6861c26-9f13-4aef-921c-26cc0d4d3016',
                    'element': 'field_uuid',
                    'field_type': '__function'}]}
    )

    # Function: 'umbrella_timeline'
    yield FunctionDefinition({ 'description': { 'content': 'Resilient Function : Cisco Umbrella Investigate Investigate for  Timeline.',
                   'format': 'text'},
  'destination_handle': 'umbrella_investigate',
  'display_name': 'umbrella_timeline',
  'name': 'umbrella_timeline',
  'uuid': 'fc6f0418-ab50-4346-9d7e-c45774c5d7a6',
  'view_items': [ { 'content': '29bf736d-87de-48fc-85b7-4dcc04670c48',
                    'element': 'field_uuid',
                    'field_type': '__function'}]}
    )

    # Function: 'umbrella_domain_security_info'
    yield FunctionDefinition({ 'description': { 'content': 'Resilient Function : Cisco Umbrella Security Investigate for Information for a Domain',
                   'format': 'text'},
  'destination_handle': 'umbrella_investigate',
  'display_name': 'umbrella_domain_security_info',
  'name': 'umbrella_domain_security_info',
  'uuid': '6ee72d17-5c6a-4874-b31c-c256de983791',
  'view_items': [ { 'content': '583d07bc-4086-48b8-a07f-287765b735a8',
                    'element': 'field_uuid',
                    'field_type': '__function'}]}
    )

    # Function: 'umbrella_domain_co_occurrences'
    yield FunctionDefinition({ 'description': { 'content': 'Resilient Function : Cisco Umbrella Investigate for Co-Occurrences for a Domain.',
                   'format': 'text'},
  'destination_handle': 'umbrella_investigate',
  'display_name': 'umbrella_domain_co_occurrences',
  'name': 'umbrella_domain_co_occurrences',
  'uuid': '6e38d35c-e6d3-4fac-9b45-f189eecc26e5',
  'view_items': [ { 'content': '583d07bc-4086-48b8-a07f-287765b735a8',
                    'element': 'field_uuid',
                    'field_type': '__function'}]}
    )

