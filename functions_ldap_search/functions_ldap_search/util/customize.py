# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for functions_ldap_search"""

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
            "fields": { 'search_attributes': { 'blank_option': False,
                         'input_type': 'text',
                         'name': 'search_attributes',
                         'placeholder': '',
                         'rich_text': False,
                         'templates': [],
                         'text': 'search_attributes',
                         'tooltip': '',
                         'uuid': 'd449aa53-20e8-4af0-bb61-525f4208b07b',
                         'values': []},
  'search_base': { 'blank_option': False,
                   'input_type': 'text',
                   'name': 'search_base',
                   'placeholder': '',
                   'rich_text': False,
                   'templates': [],
                   'text': 'search_base',
                   'tooltip': '',
                   'uuid': 'e72e469e-342e-4ef9-8863-d84dee27758a',
                   'values': []},
  'search_filter': { 'blank_option': False,
                     'input_type': 'textarea',
                     'name': 'search_filter',
                     'placeholder': '',
                     'rich_text': False,
                     'templates': [],
                     'text': 'search_filter',
                     'tooltip': '',
                     'uuid': 'a550e011-318e-4b7c-a4ee-7ec011ee0447',
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
    yield FunctionDefinition({ 'description': { 'content': '', 'format': 'text'},
  'destination_handle': 'ldap',
  'display_name': 'LDAP Search',
  'name': 'ldap_search',
  'uuid': 'ddff8983-0198-4e9e-a856-fcdea1aa0065',
  'view_items': [ { 'content': 'search_base',
                    'element': 'field',
                    'field_type': '__function'},
                  { 'content': 'search_filter',
                    'element': 'field',
                    'field_type': '__function'},
                  { 'content': 'search_attributes',
                    'element': 'field',
                    'field_type': '__function'}]}
    )

