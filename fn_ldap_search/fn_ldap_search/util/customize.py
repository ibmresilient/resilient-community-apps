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
            "fields": { 'param': { 'blank_option': False,
             'input_type': 'text',
             'name': 'param',
             'placeholder': 'artifact.value',
             'rich_text': False,
             'templates': [],
             'text': 'param',
             'tooltip': 'Parameter used in LDAP search',
             'uuid': '846dff4f-71b6-4ab2-bfd3-f9ff02e24641',
             'values': []},
  'search_attributes': { 'blank_option': False,
                         'input_type': 'text',
                         'name': 'search_attributes',
                         'placeholder': '"uid,cn,sn,mail"',
                         'rich_text': False,
                         'templates': [],
                         'text': 'search_attributes',
                         'tooltip': 'A single attribute or a list of attributes to be returned by the LDAP search ',
                         'uuid': 'd449aa53-20e8-4af0-bb61-525f4208b07b',
                         'values': []},
  'search_base': { 'blank_option': False,
                   'input_type': 'text',
                   'name': 'search_base',
                   'placeholder': '"dc=example,dc=com"',
                   'rich_text': False,
                   'templates': [],
                   'text': 'search_base',
                   'tooltip': 'The base of the LDAP search request.',
                   'uuid': 'e72e469e-342e-4ef9-8863-d84dee27758a',
                   'values': []},
  'search_filter': { 'blank_option': False,
                     'input_type': 'textarea',
                     'name': 'search_filter',
                     'placeholder': '"(&(objectClass=person)(uid=%param%))"',
                     'rich_text': False,
                     'templates': [],
                     'text': 'search_filter',
                     'tooltip': 'The filter of the LDAP search request',
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
    yield FunctionDefinition({ 'description': { 'content': 'Resilient Function to do a search or query against an LDAP server.',
                   'format': 'text'},
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
                    'field_type': '__function'},
                  { 'content': 'param',
                    'element': 'field',
                    'field_type': '__function'}]}
    )

