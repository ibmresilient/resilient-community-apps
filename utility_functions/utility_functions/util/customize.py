# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for utility_functions"""

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
            "fields": { 'artifact_file_type': { 'blank_option': False,
                          'input_type': 'select',
                          'name': 'artifact_file_type',
                          'placeholder': '',
                          'rich_text': False,
                          'templates': [],
                          'text': 'artifact_file_type',
                          'tooltip': '',
                          'uuid': '247c1025-f582-4641-9ce6-5da976797e50',
                          'values': [ { 'label': 'Email Attachment'},
                                      { 'label': 'Malware Sample'},
                                      { 'label': 'Log File'},
                                      { 'label': 'Other File'}]},
  'attachment_id': { 'blank_option': False,
                     'input_type': 'number',
                     'name': 'attachment_id',
                     'placeholder': '',
                     'rich_text': False,
                     'templates': [],
                     'text': 'attachment_id',
                     'tooltip': '',
                     'uuid': '17c3e652-6559-4935-9f95-74374ca37a7b',
                     'values': []},
  'description': { 'blank_option': False,
                   'input_type': 'textarea',
                   'name': 'description',
                   'placeholder': '',
                   'rich_text': False,
                   'templates': [],
                   'text': 'description',
                   'tooltip': '',
                   'uuid': '3c82d51d-265f-464c-aac4-57de599cea8a',
                   'values': []},
  'file_path': { 'blank_option': False,
                 'input_type': 'text',
                 'name': 'file_path',
                 'placeholder': '',
                 'rich_text': False,
                 'templates': [],
                 'text': 'file_path',
                 'tooltip': '',
                 'uuid': 'f9633eec-4afe-4e09-bd9a-8f63a45c55f0',
                 'values': []},
  'incident_id': { 'blank_option': False,
                   'input_type': 'number',
                   'name': 'incident_id',
                   'placeholder': '',
                   'rich_text': False,
                   'templates': [],
                   'text': 'incident_id',
                   'tooltip': '',
                   'uuid': 'ead214c2-13fe-43f6-a3c7-676a88338dbb',
                   'values': []},
  'seconds': { 'blank_option': False,
               'input_type': 'number',
               'name': 'seconds',
               'placeholder': '',
               'rich_text': False,
               'templates': [],
               'text': 'seconds',
               'tooltip': '',
               'uuid': '79cee9ba-be43-4934-997d-c66baf7da81c',
               'values': []},
  'zipfile_password': { 'blank_option': False,
                        'input_type': 'text',
                        'name': 'zipfile_password',
                        'placeholder': '',
                        'rich_text': False,
                        'templates': [],
                        'text': 'zipfile_password',
                        'tooltip': '',
                        'uuid': '9ab219d3-d31e-407c-9cbb-a07c76c649a1',
                        'values': []}}
        }
    )

    # Message destination: 'utility_functions'
    yield MessageDestinationDefinition({ 'destination_type': 0,
  'expect_ack': True,
  'name': 'utility_functions',
  'programmatic_name': 'utility_functions'}
    )

    # Function: 'attachment_zip_extract'
    yield FunctionDefinition({ 'description': { 'content': 'For a zipfile attachment, extract a file.',
                   'format': 'text'},
  'destination_handle': 'utility_functions',
  'display_name': 'Attachment Zip Extract',
  'name': 'attachment_zip_extract',
  'uuid': '4d9fb1df-1eab-494b-8375-c4feb0525429',
  'view_items': [ { 'content': 'incident_id',
                    'element': 'field',
                    'field_type': '__function'},
                  { 'content': 'attachment_id',
                    'element': 'field',
                    'field_type': '__function'},
                  { 'content': 'file_path',
                    'element': 'field',
                    'field_type': '__function'},
                  { 'content': 'zipfile_password',
                    'element': 'field',
                    'field_type': '__function'}]}
    )

    # Function: 'attachment_move_to_artifact'
    yield FunctionDefinition({ 'description': { 'content': '', 'format': 'text'},
  'destination_handle': 'utility_functions',
  'display_name': 'Attachment Move to Artifact',
  'name': 'attachment_move_to_artifact',
  'uuid': 'b0332700-fb72-4a32-bc9f-2e1291170204',
  'view_items': [ { 'content': 'incident_id',
                    'element': 'field',
                    'field_type': '__function'},
                  { 'content': 'attachment_id',
                    'element': 'field',
                    'field_type': '__function'},
                  { 'content': 'artifact_file_type',
                    'element': 'field',
                    'field_type': '__function'},
                  { 'content': 'description',
                    'element': 'field',
                    'field_type': '__function'}]}
    )

    # Function: 'attachment_zip_list'
    yield FunctionDefinition({ 'description': { 'content': 'For a zipfile attachment, return a list of its contents.',
                   'format': 'text'},
  'destination_handle': 'utility_functions',
  'display_name': 'Attachment Zip List',
  'name': 'attachment_zip_list',
  'uuid': 'c28c15ac-ecd2-4cd8-ba85-8f8c2bb307d2',
  'view_items': [ { 'content': 'incident_id',
                    'element': 'field',
                    'field_type': '__function'},
                  { 'content': 'attachment_id',
                    'element': 'field',
                    'field_type': '__function'},
                  { 'content': 'zipfile_password',
                    'element': 'field',
                    'field_type': '__function'}]}
    )

    # Function: 'attachment_hash'
    yield FunctionDefinition({ 'description': { 'content': 'Calculate hashes for a file attachment.',
                   'format': 'text'},
  'destination_handle': 'utility_functions',
  'display_name': 'Attachment Hash',
  'name': 'attachment_hash',
  'uuid': '9e0f46f4-ae8c-4aa6-a296-3a0662a53386',
  'view_items': [ { 'content': 'incident_id',
                    'element': 'field',
                    'field_type': '__function'},
                  { 'content': 'attachment_id',
                    'element': 'field',
                    'field_type': '__function'}]}
    )

    # Function: 'attachment_zip_extract_to_artifact'
    yield FunctionDefinition({ 'description': { 'content': '', 'format': 'text'},
  'destination_handle': 'utility_functions',
  'display_name': 'Attachment Zip Extract to Artifact',
  'name': 'attachment_zip_extract_to_artifact',
  'uuid': '6361b8ed-88c6-428f-949e-3e9d9ffa6bfd',
  'view_items': [ { 'content': 'incident_id',
                    'element': 'field',
                    'field_type': '__function'},
                  { 'content': 'attachment_id',
                    'element': 'field',
                    'field_type': '__function'},
                  { 'content': 'file_path',
                    'element': 'field',
                    'field_type': '__function'},
                  { 'content': 'zipfile_password',
                    'element': 'field',
                    'field_type': '__function'},
                  { 'content': 'artifact_file_type',
                    'element': 'field',
                    'field_type': '__function'}]}
    )

    # Function: 'wait'
    yield FunctionDefinition({ 'description': { 'content': 'Waits for a given number of seconds',
                   'format': 'text'},
  'destination_handle': 'utility_functions',
  'display_name': 'Wait',
  'name': 'wait',
  'uuid': 'f17025e5-5437-477f-b7ce-6d1f38a67cac',
  'view_items': [ { 'content': 'seconds',
                    'element': 'field',
                    'field_type': '__function'}]}
    )

