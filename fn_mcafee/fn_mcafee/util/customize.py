# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_mcafee"""

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
            "fields": { 'mcafee_epo_systems': { 'blank_option': False,
                          'input_type': 'text',
                          'name': 'mcafee_epo_systems',
                          'placeholder': '',
                          'rich_text': False,
                          'templates': [],
                          'text': 'mcafee_epo_systems',
                          'tooltip': 'Comma separated list of Hostnames/IpAddress. These systems must be managed on ePO',
                          'uuid': 'bf25606e-96aa-4328-aa15-1cd5a8b8dc02',
                          'values': []},
  'mcafee_epo_tag': { 'blank_option': False,
                      'input_type': 'text',
                      'name': 'mcafee_epo_tag',
                      'placeholder': '',
                      'rich_text': False,
                      'templates': [],
                      'text': 'mcafee_epo_tag',
                      'tooltip': 'Tag managed on ePO',
                      'uuid': '134bfbe6-821d-4c29-9492-d594c38125d7',
                      'values': []}}
        }
    )

    # Message destination: 'mcafee_message_destination'
    yield MessageDestinationDefinition({ 'destination_type': 0,
  'expect_ack': True,
  'name': 'mcafee_Message Destination',
  'programmatic_name': 'mcafee_message_destination'}
    )

    # Function: 'mcafee_tag_an_epo_asset'
    yield FunctionDefinition({ 'description': { 'content': 'A function which takes two inputs:\n\nmcafee_epo_system: Comma separated list of Hostnames/IpAddress. These systems must be managed on ePO.\nmcafee_epo_tag: A Tag managed on ePO.\n\nApplies tag to the systems in ePO.',
                   'format': 'text'},
  'destination_handle': 'mcafee_message_destination',
  'display_name': 'mcafee_Tag an ePO asset',
  'name': 'mcafee_tag_an_epo_asset',
  'uuid': '67c5b852-f38f-40f7-8a68-1ae8e8a78549',
  'view_items': [ { 'content': 'mcafee_epo_systems',
                    'element': 'field',
                    'field_type': '__function'},
                  { 'content': 'mcafee_epo_tag',
                    'element': 'field',
                    'field_type': '__function'}]}
    )

