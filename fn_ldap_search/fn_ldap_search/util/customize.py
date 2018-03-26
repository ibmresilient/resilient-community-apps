# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_ldap_search"""

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
            "fields": { '846dff4f-71b6-4ab2-bfd3-f9ff02e24641': { 'blank_option': False,
                                            'input_type': 'text',
                                            'name': 'param',
                                            'placeholder': '',
                                            'rich_text': False,
                                            'templates': [],
                                            'text': 'param',
                                            'tooltip': 'Parameter used in LDAP search',
                                            'uuid': '846dff4f-71b6-4ab2-bfd3-f9ff02e24641',
                                            'values': []},
  'a550e011-318e-4b7c-a4ee-7ec011ee0447': { 'blank_option': False,
                                            'input_type': 'textarea',
                                            'name': 'search_filter',
                                            'placeholder': '',
                                            'rich_text': False,
                                            'templates': [],
                                            'text': 'search_filter',
                                            'tooltip': 'The filter of the LDAP search request',
                                            'uuid': 'a550e011-318e-4b7c-a4ee-7ec011ee0447',
                                            'values': []},
  'd449aa53-20e8-4af0-bb61-525f4208b07b': { 'blank_option': False,
                                            'input_type': 'text',
                                            'name': 'search_attributes',
                                            'placeholder': '',
                                            'rich_text': False,
                                            'templates': [],
                                            'text': 'search_attributes',
                                            'tooltip': 'A single attribute or a list of attributes to be returned by the LDAP search ',
                                            'uuid': 'd449aa53-20e8-4af0-bb61-525f4208b07b',
                                            'values': []},
  'e72e469e-342e-4ef9-8863-d84dee27758a': { 'blank_option': False,
                                            'input_type': 'text',
                                            'name': 'search_base',
                                            'placeholder': '',
                                            'rich_text': False,
                                            'templates': [],
                                            'text': 'search_base',
                                            'tooltip': 'The base of the LDAP search request.',
                                            'uuid': 'e72e469e-342e-4ef9-8863-d84dee27758a',
                                            'values': []}}
        }
    )

    # Message destination: 'ldap'
    yield MessageDestinationDefinition({ 'destination_type': 0,
  'expect_ack': True,
  'name': 'ldap',
  'programmatic_name': 'ldap'}
    )

    # Function: 'ldap_search'
    yield FunctionDefinition({ 'description': { 'content': 'Resilient Function to do a search or query against an LDAP server.',
                   'format': 'text'},
  'destination_handle': 'ldap',
  'display_name': 'ldap_search',
  'name': 'ldap_search',
  'uuid': '5b240886-6cc1-44d4-997b-652401fdaff6',
  'view_items': [ { 'content': 'e72e469e-342e-4ef9-8863-d84dee27758a',
                    'element': 'field_uuid',
                    'field_type': '__function'},
                  { 'content': 'a550e011-318e-4b7c-a4ee-7ec011ee0447',
                    'element': 'field_uuid',
                    'field_type': '__function'},
                  { 'content': 'd449aa53-20e8-4af0-bb61-525f4208b07b',
                    'element': 'field_uuid',
                    'field_type': '__function'},
                  { 'content': '846dff4f-71b6-4ab2-bfd3-f9ff02e24641',
                    'element': 'field_uuid',
                    'field_type': '__function'}]}
    )

