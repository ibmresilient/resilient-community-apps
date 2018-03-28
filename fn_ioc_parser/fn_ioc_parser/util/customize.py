# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_ioc_parser"""

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
            "fields": { '37917fe9-5746-446e-9d34-773865813c71': { 'blank_option': False,
                                            'input_type': 'select',
                                            'name': 'inputType',
                                            'placeholder': '',
                                            'rich_text': False,
                                            'templates': [],
                                            'text': 'inputType',
                                            'tooltip': '',
                                            'uuid': '37917fe9-5746-446e-9d34-773865813c71',
                                            'values': [ { 'label': 'pdf'},
                                                        { 'label': 'txt'},
                                                        { 'label': 'html'}]},
  '6a949931-42b1-4640-9742-f6c40c98a45e': { 'blank_option': False,
                                            'input_type': 'number',
                                            'name': 'incidentId',
                                            'placeholder': '',
                                            'rich_text': False,
                                            'templates': [],
                                            'text': 'incidentId',
                                            'tooltip': '',
                                            'uuid': '6a949931-42b1-4640-9742-f6c40c98a45e',
                                            'values': []},
  'e82d8f21-e77f-4ea3-8616-5581191f0c48': { 'blank_option': False,
                                            'input_type': 'number',
                                            'name': 'artifactId',
                                            'placeholder': '',
                                            'rich_text': False,
                                            'templates': [],
                                            'text': 'artifactId',
                                            'tooltip': '',
                                            'uuid': 'e82d8f21-e77f-4ea3-8616-5581191f0c48',
                                            'values': []}}
        }
    )

    # Message destination: 'iocpdest'
    yield MessageDestinationDefinition({ 'destination_type': 0,
  'expect_ack': True,
  'name': 'iocpdest',
  'programmatic_name': 'iocpdest'}
    )

    # Function: 'ioc_parser'
    yield FunctionDefinition({ 'description': { 'content': '', 'format': 'text'},
  'destination_handle': 'iocpdest',
  'display_name': 'ioc_parser',
  'name': 'ioc_parser',
  'uuid': '864cc043-47f5-4261-b658-39f4712b269d',
  'view_items': [ { 'content': '37917fe9-5746-446e-9d34-773865813c71',
                    'element': 'field_uuid',
                    'field_type': '__function'},
                  { 'content': 'e82d8f21-e77f-4ea3-8616-5581191f0c48',
                    'element': 'field_uuid',
                    'field_type': '__function'},
                  { 'content': '6a949931-42b1-4640-9742-f6c40c98a45e',
                    'element': 'field_uuid',
                    'field_type': '__function'}]}
    )

