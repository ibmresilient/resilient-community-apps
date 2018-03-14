# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for jira"""

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
            "fields": {
                        'incidentID': { 'blank_option': False,
                                        'input_type': 'number',
                                        'name': 'incidentID',
                                        'placeholder': '',
                                        'rich_text': False,
                                        'templates': [],
                                        'text': 'incidentID',
                                        'tooltip': '',
                                        'uuid': '47cd0f65-b766-47be-8735-f309851d1515',
                                        'values': []},
                        'jira_comment': { 'blank_option': False,
                                          'input_type': 'text',
                                          'name': 'jira_comment',
                                          'placeholder': '',
                                          'rich_text': False,
                                          'templates': [],
                                          'text': 'jira_comment',
                                          'tooltip': '',
                                          'uuid': 'c55a9961-2b9e-4186-b32d-5ce1f0f5def5',
                                          'values': []},
                        'jira_description': { 'blank_option': False,
                                              'input_type': 'text',
                                              'name': 'jira_description',
                                              'placeholder': '',
                                              'required': 'always',
                                              'rich_text': False,
                                              'templates': [],
                                              'text': 'jira_description',
                                              'tooltip': '',
                                              'uuid': '9e6b98cc-3724-442e-8197-0394dbeef698',
                                              'values': []},
                        'jira_issuetype': { 'blank_option': False,
                                            'input_type': 'textarea',
                                            'name': 'jira_issuetype',
                                            'placeholder': 'Bug',
                                            'required': 'always',
                                            'rich_text': False,
                                            'templates': [{ 'name': 'Bug', 'template': 'Bug'}],
                                            'text': 'jira_issuetype',
                                            'tooltip': '',
                                            'uuid': '6dae56fe-44d7-45f5-990a-c67c4139f1ef',
                                            'values': []},
                        'jira_project': { 'blank_option': False,
                                          'input_type': 'textarea',
                                          'name': 'jira_project',
                                          'placeholder': '',
                                          'required': 'always',
                                          'rich_text': False,
                                          'templates': [ { 'name': 'Resilient',
                                                           'template': 'RES'},
                                                         { 'name': 'Discovery',
                                                           'template': 'DISCO'}],
                                          'text': 'jira_project',
                                          'tooltip': '',
                                          'uuid': 'e4311ce4-4fc3-4ad2-935f-89a6e78c49a5',
                                          'values': []},
                        'jira_summary': { 'blank_option': False,
                                          'input_type': 'text',
                                          'name': 'jira_summary',
                                          'placeholder': '',
                                          'required': 'always',
                                          'rich_text': False,
                                          'templates': [],
                                          'text': 'jira_summary',
                                          'tooltip': '',
                                          'uuid': '39ca7aa9-4944-4769-ab8a-91d3160486d7',
                                          'values': []},
                        'jira_transition_id': { 'blank_option': False,
                                                'input_type': 'text',
                                                'name': 'jira_transition_id',
                                                'placeholder': '5',
                                                'required': 'always',
                                                'rich_text': False,
                                                'templates': [],
                                                'text': 'jira_transition_id',
                                                'tooltip': '',
                                                'uuid': '7e1c7fa9-7a44-4b31-9090-6679531ed32c',
                                                'values': []},
                        'jira_url': { 'blank_option': False,
                                      'input_type': 'text',
                                      'name': 'jira_url',
                                      'placeholder': '',
                                      'required': 'always',
                                      'rich_text': False,
                                      'templates': [],
                                      'text': 'jira_url',
                                      'tooltip': '',
                                      'uuid': '3f64f620-e7e2-47b2-ba4a-e8813b67d524',
                                      'values': []}}
        }
    )

    # Message destination: 'jira'
    yield MessageDestinationDefinition({ 'destination_type': 0,
                                         'expect_ack': True,
                                         'name': 'jira',
                                         'programmatic_name': 'jira'}
                                       )

    # Function: 'jira_open_issue'
    yield FunctionDefinition({ 'description': { 'content': 'Create a jira issue. To be used when a Resilient Incident is created.\nSee source code for configuration of function pre-processor and post-processor scripts', 'format': 'text'},
                               'destination_handle': 'jira',
                               'display_name': 'Jira Open Issue',
                               'name': 'jira_open_issue',
                               'uuid': '84476441-4b16-40fe-96c4-d07f94bda06a',
                               'view_items': [ { 'content': 'incidentID',
                                                 'element': 'field',
                                                 'field_type': '__function'},
                                               { 'content': 'jira_project',
                                                 'element': 'field',
                                                 'field_type': '__function'},
                                               { 'content': 'jira_issuetype',
                                                 'element': 'field',
                                                 'field_type': '__function'},
                                               { 'content': 'jira_summary',
                                                 'element': 'field',
                                                 'field_type': '__function'},
                                               { 'content': 'jira_description',
                                                 'element': 'field',
                                                 'field_type': '__function'}]}
                             )

    # Function: 'jira_transition_issue'
    yield FunctionDefinition({ 'description': { 'content': 'Transition a jira issue. To be used when a Resilient Incident is closed.\nSee source code for configuration of function pre-processor and post-processor scripts', 'format': 'text'},
                               'destination_handle': 'jira',
                               'display_name': 'Jira Transition Issue',
                               'name': 'jira_transition_issue',
                               'uuid': '94056ccf-b3ad-4a17-9760-93b3c24b71d8',
                               'view_items': [ { 'content': 'jira_transition_id',
                                                 'element': 'field',
                                                 'field_type': '__function'},
                                               { 'content': 'jira_url',
                                                 'element': 'field',
                                                 'field_type': '__function'},
                                               { 'content': 'jira_comment',
                                                 'element': 'field',
                                                 'field_type': '__function'}]}
                             )

    # Function: 'jira_create_comment'
    yield FunctionDefinition({ 'description': {'content': 'Create a jira comment. To be used when a Resilient Note is created.\nSee source code for configuration of function pre-processor and post-processor scripts', 'format': 'text'},
                               'destination_handle': 'jira',
                               'display_name': 'Jira Create Comment',
                               'name': 'jira_create_comment',
                               'uuid': 'd0e6089a-69f7-469d-8e51-a840ec2c493a',
                               'view_items': [ { 'content': 'jira_url',
                                                 'element': 'field',
                                                 'field_type': '__function'},
                                               { 'content': 'jira_comment',
                                                 'element': 'field',
                                                 'field_type': '__function'}]}
                             )

