# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for test"""

from __future__ import print_function
from resilient_circuits.util import *


def customization_data(client):
    """Produce any customization definitions (types, fields, message destinations, etc)
       that should be installed by `resilient-circuits customize`
    """

    # Function-field definitions
    yield TypeDefinition(
        {
            "type_name": "__function",
            "fields": { 'mcafee_tie_hash': { 'blank_option': False,
                       'input_type': 'text',
                       'name': 'mcafee_tie_hash',
                       'placeholder': '',
                       'rich_text': False,
                       'templates': [],
                       'text': 'mcafee_tie_hash',
                       'tooltip': 'The value of the hash',
                       'values': []},
  'mcafee_tie_hash_type': { 'blank_option': False,
                            'input_type': 'text',
                            'name': 'mcafee_tie_hash_type',
                            'placeholder': '',
                            'rich_text': False,
                            'templates': [],
                            'text': 'mcafee_tie_hash_type',
                            'tooltip': 'The type of file hash (md5, sha1, sha256)',
                            'values': []}}
        }
    )

    # Message destination: mcafee_tie_message_destination
    yield MessageDestinationDefinition({ 'destination_type': 0,
  'expect_ack': True,
  'name': 'McAfee TIE Message Destination',
  'programmatic_name': 'mcafee_tie_message_destination'}
    )

    # Function: mcafee_tie_search_hash
    yield FunctionDefinition({ 'description': { 'content': 'A function which takes two inputs:\n\nmcafee_tie_hash_type: The type of file hash (md5, sha1, sha256).\nmcafee_tie_hash: The value of the hash.\n\nThe function returns back a dict of all the available information from the different file providers (Enterprise, GTI, ATD, MWG) along with the list of systems related to it.', 'format': 'text'},
  'destination_handle': 'mcafee_tie_message_destination',
  'display_name': 'McAfee TIE search hash',
  'name': 'mcafee_tie_search_hash',
  'view_items': [ { 'content': 'mcafee_tie_hash_type',
                    'element': 'field',
                    'field_type': '__function'},
                  { 'content': 'mcafee_tie_hash',
                    'element': 'field',
                    'field_type': '__function'}]}
    )
