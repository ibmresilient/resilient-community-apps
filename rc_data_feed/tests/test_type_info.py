# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
# pragma pylint: disable=unused-argument, line-too-long
"""Tests using pytest_resilient_circuits"""

import pytest
from rc_data_feed.lib.type_info import TypeInfo, ActionMessageTypeInfo

TYPE_INFO_MAP = {
  'incident': {
    'id': 0,
    'type_id': 0,
    'type_name': 'incident',
    'fields': {
      'acknowledged_netskope': {
        'id': 2284,
        'name': 'acknowledged_netskope',
        'text': 'Acknowledged (Netskope)',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': 'Whether user acknowledged the alert or not',
        'placeholder': '',
        'input_type': 'text',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': '5b55ffa3-b064-401e-b0e1-04e440437e24',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'action_netskope': {
        'id': 2279,
        'name': 'action_netskope',
        'text': 'Action (Netskope)',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': 'Action taken on the event for the policy',
        'placeholder': '',
        'input_type': 'text',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': 'ff9e01b2-a5ab-4d44-b87f-070ccfad1272',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'activity_netskope': {
        'id': 2282,
        'name': 'activity_netskope',
        'text': 'Activity (Netskope)',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': 'Description of the user performed activity',
        'placeholder': '',
        'input_type': 'text',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': '180dcf87-0561-49de-9d66-78502c23d6ed',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'addr': {
        'id': 327,
        'name': 'addr',
        'text': 'Address',
        'prefix': None,
        'type_id': 0,
        'tooltip': 'Physical location of the incident, if applicable',
        'input_type': 'text',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': True,
        'uuid': '9540d9b0-2cd9-4347-b013-a1c84b6605b7',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'alberta_health_risk_assessment': {
        'id': 362,
        'name': 'alberta_health_risk_assessment',
        'text': 'Alberta Health Risk Assessment',
        'prefix': 'pii',
        'type_id': 0,
        'input_type': 'boolean',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': True,
        'uuid': '6dd01276-c322-4095-b33c-15d3b33c3540',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'alert_id_netskope': {
        'id': 2281,
        'name': 'alert_id_netskope',
        'text': 'Alert ID (Netskope)',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': 'ID of the alert',
        'placeholder': '',
        'input_type': 'text',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': '11db6568-3598-46e5-8176-d13a90135e15',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'alert_type_netskope': {
        'id': 2278,
        'name': 'alert_type_netskope',
        'text': 'Alert Type (Netskope)',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': 'Type of the alert',
        'placeholder': '',
        'input_type': 'text',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': 'e5acaf32-70f6-47b9-b50d-2da9163f3769',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'application_netskope': {
        'id': 2275,
        'name': 'application_netskope',
        'text': 'Application (Netskope)',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': 'Specific cloud application used by the user',
        'placeholder': '',
        'input_type': 'text',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': 'c41b914c-6ff8-437e-9750-9546f6b73691',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'automatic_score': {
        'id': 397,
        'name': 'automatic_score',
        'text': 'Automatic Score',
        'prefix': None,
        'type_id': 0,
        'tooltip': 'A numerical representation of the case severity. Values range from -10 to 10.',
        'input_type': 'number',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': True,
        'uuid': '6472a494-8991-4ace-a095-0918bf594544',
        'values': [
          
        ],
        'read_only': True,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'aws_guardduty_archived': {
        'id': 2383,
        'name': 'aws_guardduty_archived',
        'text': 'AWS GuardDuty Archived',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': ' A True or False value that indicates whether this is GuardDuty finding has been archived. ',
        'placeholder': '',
        'input_type': 'text',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': '6d5742bd-1e74-47c3-b20f-0a786a9fcfa3',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'aws_guardduty_count': {
        'id': 2377,
        'name': 'aws_guardduty_count',
        'text': 'AWS GuardDuty Count',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': 'The number of times GuardDuty has aggregated an activity matching this pattern to this finding ID. ',
        'placeholder': '',
        'input_type': 'text',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': 'a64d69ca-fb01-4bc1-a102-2ceea30b6b6b',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'aws_guardduty_detector_id': {
        'id': 2381,
        'name': 'aws_guardduty_detector_id',
        'text': 'AWS GuardDuty Detector Id',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': 'The detector ID where the GuardDuty finding was detected.',
        'placeholder': '',
        'input_type': 'text',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': '5e191046-c9ce-4e74-b5be-f7277f93792b',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'aws_guardduty_finding_arn': {
        'id': 2379,
        'name': 'aws_guardduty_finding_arn',
        'text': 'AWS GuardDuty Finding Arn',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': 'Arn of the GuardDuty finding.',
        'placeholder': '',
        'input_type': 'text',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': 'f1c8fa20-ffc3-4942-98bb-1d84fdc92f32',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'aws_guardduty_finding_id': {
        'id': 2378,
        'name': 'aws_guardduty_finding_id',
        'text': 'AWS GuardDuty Finding Id',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': 'A unique Finding ID for this GuardDuty finding type and set of parameters. New occurrences of activity matching this pattern will be aggregated to the same ID. ',
        'placeholder': '',
        'input_type': 'text',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': 'e380c315-601d-4052-90b5-78efe75d7eab',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'aws_guardduty_finding_type': {
        'id': 2384,
        'name': 'aws_guardduty_finding_type',
        'text': 'AWS GuardDuty Finding Type',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': 'The type of activity that triggered the GuardDuty finding.',
        'placeholder': '',
        'input_type': 'text',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': '6fc421a3-c414-48de-9d39-bb833b777d00',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'aws_guardduty_finding_updated_at': {
        'id': 2382,
        'name': 'aws_guardduty_finding_updated_at',
        'text': 'AWS GuardDuty Resource Updated At',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': 'The last time this finding was updated with new activity matching the pattern that prompted GuardDuty to generate this finding. ',
        'placeholder': '',
        'input_type': 'text',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': '63d7c51c-ab4d-417e-9173-6d366d05f6d5',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'aws_guardduty_region': {
        'id': 2376,
        'name': 'aws_guardduty_region',
        'text': 'AWS GuardDuty Region',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': 'The AWS Region in which the GuardDuty finding was generated. ',
        'placeholder': '',
        'input_type': 'text',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': 'a5789c35-3e6f-4229-a671-2fe7ba6f3457',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'aws_guardduty_resource_type': {
        'id': 2380,
        'name': 'aws_guardduty_resource_type',
        'text': 'AWS GuardDuty Resource Type',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': 'The type of the affected resource of the GuardDuty finding. This value is either AccessKey, S3 bucket or Instance. ',
        'placeholder': '',
        'input_type': 'text',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': '251c8f2a-9a9d-4b0e-b9a2-ed15e022754c',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'aws_guardduty_severity': {
        'id': 2375,
        'name': 'aws_guardduty_severity',
        'text': 'AWS GuardDuty Severity',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': 'The severity of the affected resource of the GuardDuty finding. ',
        'placeholder': '',
        'input_type': 'text',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': '9b26f0fc-bfca-467b-8c21-be0edc22768d',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'aws_guardduty_trigger_refresh': {
        'id': 2385,
        'name': 'aws_guardduty_trigger_refresh',
        'text': 'AWS GuardDuty Trigger Refresh',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': 'Used by integration to trigger an refresh of GuardDuty incidents.',
        'placeholder': 'False',
        'input_type': 'boolean',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': '766a53c2-6684-44bb-9808-2cc774c56747',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'california_health_risk_assessment': {
        'id': 365,
        'name': 'california_health_risk_assessment',
        'text': 'California Health Risk Assessment',
        'prefix': 'pii',
        'type_id': 0,
        'input_type': 'boolean',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': True,
        'uuid': '35868ab2-564c-43e1-94bc-a3f5676bc25a',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'chronicle_alert_assetname': {
        'id': 1220,
        'name': 'chronicle_alert_assetname',
        'text': 'Chronicle Alert Assetname',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': 'Asset name of the chronicle alert.',
        'placeholder': '',
        'input_type': 'textarea',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': 'f8d1cd61-5709-4832-a67d-688e787f623e',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': True,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'chronicle_alert_username': {
        'id': 1224,
        'name': 'chronicle_alert_username',
        'text': 'Chronicle Alert Username',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': 'User name of the chronicle alert.',
        'placeholder': '',
        'input_type': 'textarea',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': '3e3c8cfe-fdf9-4207-99c2-ce99e155bbbd',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': True,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'chronicle_collection_elements': {
        'id': 1219,
        'name': 'chronicle_collection_elements',
        'text': 'Chronicle Collection Elements',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': 'A list of references to sample UDM events causing this detection.',
        'placeholder': '',
        'input_type': 'text',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': 'efc08471-4a7a-43b0-a500-9d8cd2667b71',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'chronicle_detection_created_time': {
        'id': 1222,
        'name': 'chronicle_detection_created_time',
        'text': 'Chronicle Detection Created Time',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': 'Time the detection was created.',
        'placeholder': '',
        'input_type': 'textarea',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': '27534651-5b86-407b-98be-0e8bd51c0424',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': True,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'chronicle_detection_state': {
        'id': 1227,
        'name': 'chronicle_detection_state',
        'text': 'Chronicle Detection State',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': 'Indicates whether the rule generating this detection currently has alerting enabled or disabled.',
        'placeholder': '',
        'input_type': 'textarea',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': '57064228-fed4-414c-97a6-13d3fbb04a3e',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': True,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'chronicle_detection_time': {
        'id': 1216,
        'name': 'chronicle_detection_time',
        'text': 'Chronicle Detection Time',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': 'The time period the detection was found in.',
        'placeholder': '',
        'input_type': 'textarea',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': 'becd95a4-3a32-4822-a685-3b79638fe5f8',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': True,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'chronicle_detection_type': {
        'id': 1217,
        'name': 'chronicle_detection_type',
        'text': 'Chronicle Detection Type',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': 'Type of detection.',
        'placeholder': '',
        'input_type': 'textarea',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': 'c273fe7e-edba-496a-a9a3-6c8d6569c54d',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': True,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'chronicle_detection_window_end_time': {
        'id': 1228,
        'name': 'chronicle_detection_window_end_time',
        'text': 'Chronicle Detection Window End Time',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': 'The end of the time window in which the detection was found, in RFC 3339 format.',
        'placeholder': '',
        'input_type': 'textarea',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': '7afb5358-5302-4b61-9c6e-9d200deceeff',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': True,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'chronicle_detection_window_start_time': {
        'id': 1214,
        'name': 'chronicle_detection_window_start_time',
        'text': 'Chronicle Detection Window Start Time',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': 'The start of the time window in which the detection was found, in RFC 3339 format.',
        'placeholder': '',
        'input_type': 'textarea',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': '9d52a451-6c25-4743-aad2-393e6bcc0aeb',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': True,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'chronicle_ioc_domain': {
        'id': 1226,
        'name': 'chronicle_ioc_domain',
        'text': 'Chronicle IOC Domain',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': 'Domain name for the incident.',
        'placeholder': '',
        'input_type': 'textarea',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': '4a7c5449-3536-4676-b86c-cad3518e5c95',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': True,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'chronicle_ioc_first_seen_time': {
        'id': 1223,
        'name': 'chronicle_ioc_first_seen_time',
        'text': 'Chronicle IOC First Seen Time',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': 'Time(UTC) the artifact was first seen within your enterprise.',
        'placeholder': '',
        'input_type': 'textarea',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': '340f077c-911a-4eb2-b401-5a81af1c9da7',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': True,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'chronicle_ioc_ingest_time': {
        'id': 1215,
        'name': 'chronicle_ioc_ingest_time',
        'text': 'Chronicle IOC Ingest Time',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': 'Time(UTC) the IoC was first seen by Chronicle.',
        'placeholder': '',
        'input_type': 'textarea',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': 'b732e13b-5fd2-4c61-9111-80e613dbda0d',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': True,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'chronicle_ioc_last_seen_time': {
        'id': 1218,
        'name': 'chronicle_ioc_last_seen_time',
        'text': 'Chronicle IOC Last Seen Time',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': 'Time(UTC) the artifact was most recently seen within your enterprise.',
        'placeholder': '',
        'input_type': 'textarea',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': 'd2d50abf-98eb-4787-be27-58964f95db0c',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': True,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'chronicle_rule_name': {
        'id': 1225,
        'name': 'chronicle_rule_name',
        'text': 'Chronicle Rule Name',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': 'Name of the rule generating the detection.',
        'placeholder': '',
        'input_type': 'textarea',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': '48f99b6f-5bb5-4f0a-a542-d1babf23e94f',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': True,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'chronicle_rule_type': {
        'id': 1221,
        'name': 'chronicle_rule_type',
        'text': 'Chronicle Rule Type',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': 'Whether the rule generating this detection is a single event or multi-event rule.',
        'placeholder': '',
        'input_type': 'textarea',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': '01cfb8e9-5303-4524-b53e-00dac9b49b41',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': True,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'city': {
        'id': 328,
        'name': 'city',
        'text': 'City',
        'prefix': None,
        'type_id': 0,
        'input_type': 'text',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': True,
        'uuid': '488c24db-25a1-4cda-91d1-3865d3639732',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'confirmed': {
        'id': 335,
        'name': 'confirmed',
        'text': 'Incident Disposition',
        'prefix': None,
        'type_id': 0,
        'tooltip': 'Tag an issue as an unconfirmed (event) vs. a confirmed incident.',
        'input_type': 'boolean',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': True,
        'uuid': '9b531f7c-d112-4444-8a91-9ea2d5e47162',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'label_False': 'Unconfirmed',
        'label_True': 'Confirmed',
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'country': {
        'id': 379,
        'name': 'country',
        'text': 'Country/Region',
        'prefix': None,
        'type_id': 0,
        'input_type': 'select',
        'hide_notification': False,
        'chosen': True,
        'default_chosen_by_server': False,
        'blank_option': True,
        'internal': True,
        'uuid': 'f9e3d12e-43b4-43c0-a8ae-89b5df9a5add',
        'values': [
          {
            'value': 1017,
            'label': 'Afghanistan',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1261,
            'label': 'Åland Islands',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1018,
            'label': 'Albania',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1019,
            'label': 'Algeria',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1020,
            'label': 'American Samoa',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1021,
            'label': 'Andorra',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1022,
            'label': 'Angola',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1023,
            'label': 'Anguilla',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1024,
            'label': 'Antarctica',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1025,
            'label': 'Antigua and Barbuda',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1026,
            'label': 'Argentina',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1027,
            'label': 'Armenia',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1028,
            'label': 'Aruba',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1029,
            'label': 'Ascension and Tristan Da Cunha Saint Helena',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1030,
            'label': 'Australia',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1031,
            'label': 'Austria',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1032,
            'label': 'Azerbaijan',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1033,
            'label': 'Bahamas',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1034,
            'label': 'Bahrain',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1035,
            'label': 'Bangladesh',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1036,
            'label': 'Barbados',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1037,
            'label': 'Belarus',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1038,
            'label': 'Belgium',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1039,
            'label': 'Belize',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1040,
            'label': 'Benin',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1041,
            'label': 'Bermuda',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1042,
            'label': 'Bhutan',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1043,
            'label': 'Bolivarian Republic of Venezuela',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1044,
            'label': 'Bosnia and Herzegovina',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1045,
            'label': 'Botswana',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1046,
            'label': 'Bouvet Island',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1047,
            'label': 'Brazil',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1048,
            'label': 'British Indian Ocean Territory',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1049,
            'label': 'British Virgin Islands',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1050,
            'label': 'Brunei Darussalam',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1051,
            'label': 'Bulgaria',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1052,
            'label': 'Burkina Faso',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1053,
            'label': 'Burundi',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1054,
            'label': 'Cambodia',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1055,
            'label': 'Cameroon',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1001,
            'label': 'Canada',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1056,
            'label': 'Cape Verde',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1057,
            'label': 'Cayman Islands',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1058,
            'label': 'Central African Republic',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1059,
            'label': 'Chad',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1060,
            'label': 'Chile',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1061,
            'label': 'China',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1062,
            'label': 'Christmas Island',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1063,
            'label': 'Cocos (Keeling) Islands',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1064,
            'label': 'Colombia',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1065,
            'label': 'Comoros',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1066,
            'label': 'Congo',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1067,
            'label': 'Cook Islands',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1068,
            'label': 'Costa Rica',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1069,
            'label': 'Croatia',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1070,
            'label': 'Cuba',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1071,
            'label': 'Curaçao',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1072,
            'label': 'Cyprus',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1073,
            'label': 'Czech Republic',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1075,
            'label': "Democratic People's Republic of Korea",
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1076,
            'label': 'Denmark',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1077,
            'label': 'Djibouti',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1078,
            'label': 'Dominica',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1079,
            'label': 'Dominican Republic',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1080,
            'label': 'Ecuador',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1081,
            'label': 'Egypt',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1082,
            'label': 'El Salvador',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1083,
            'label': 'Equatorial Guinea',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1084,
            'label': 'Eritrea',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1085,
            'label': 'Estonia',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1086,
            'label': 'Ethiopia',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1087,
            'label': 'Falkland Islands (Malvinas)',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1088,
            'label': 'Faroe Islands',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1089,
            'label': 'Federated States of Micronesia',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1090,
            'label': 'Fiji',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1091,
            'label': 'Finland',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1092,
            'label': 'France',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1093,
            'label': 'French Guiana',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1094,
            'label': 'French Polynesia',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1095,
            'label': 'French Southern Territories',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1096,
            'label': 'Gabon',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1097,
            'label': 'Gambia',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1098,
            'label': 'Georgia (Country)',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1099,
            'label': 'Germany',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1100,
            'label': 'Ghana',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1101,
            'label': 'Gibraltar',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1102,
            'label': 'Greece',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1103,
            'label': 'Greenland',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1104,
            'label': 'Grenada',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1105,
            'label': 'Guadeloupe',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1107,
            'label': 'Guatemala',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1108,
            'label': 'Guernsey',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1109,
            'label': 'Guinea',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1110,
            'label': 'Guinea-Bissau',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1111,
            'label': 'Guyana',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1112,
            'label': 'Haiti',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1113,
            'label': 'Heard Island and Mcdonald Islands',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1114,
            'label': 'Holy See (Vatican City State)',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1115,
            'label': 'Honduras',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1116,
            'label': 'Hong Kong S.A.R. of the PRC',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1117,
            'label': 'Hungary',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1118,
            'label': 'Iceland',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1119,
            'label': 'India',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1120,
            'label': 'Indonesia',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1121,
            'label': 'Iraq',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1122,
            'label': 'Ireland',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1123,
            'label': 'Islamic Republic of Iran',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1124,
            'label': 'Isle of Man',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1125,
            'label': 'Israel',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1126,
            'label': 'Italy',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1127,
            'label': 'Jamaica',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1128,
            'label': 'Japan',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1129,
            'label': 'Jersey',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1130,
            'label': 'Jordan',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1131,
            'label': 'Kazakhstan',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1132,
            'label': 'Kenya',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1133,
            'label': 'Kiribati',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1134,
            'label': 'Kuwait',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1135,
            'label': 'Kyrgyzstan',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1136,
            'label': "Lao People's Democratic Republic",
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1137,
            'label': 'Latvia',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1138,
            'label': 'Lebanon',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1139,
            'label': 'Lesotho',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1140,
            'label': 'Liberia',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1141,
            'label': 'Libya',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1142,
            'label': 'Liechtenstein',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1143,
            'label': 'Lithuania',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1144,
            'label': 'Luxembourg',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1145,
            'label': 'Macao S.A.R. of the PRC',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1146,
            'label': 'Madagascar',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1147,
            'label': 'Malawi',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1148,
            'label': 'Malaysia',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1149,
            'label': 'Maldives',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1150,
            'label': 'Mali',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1151,
            'label': 'Malta',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1152,
            'label': 'Marshall Islands',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1153,
            'label': 'Martinique',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1154,
            'label': 'Mauritania',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1155,
            'label': 'Mauritius',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1156,
            'label': 'Mayotte',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1157,
            'label': 'Mexico',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1158,
            'label': 'Monaco',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1159,
            'label': 'Mongolia',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1160,
            'label': 'Montenegro',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1161,
            'label': 'Montserrat',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1162,
            'label': 'Morocco',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1163,
            'label': 'Mozambique',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1164,
            'label': 'Myanmar',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1165,
            'label': 'Namibia',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1166,
            'label': 'Nauru',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1167,
            'label': 'Nepal',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1168,
            'label': 'Netherlands',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1169,
            'label': 'New Caledonia',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1170,
            'label': 'New Zealand',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1171,
            'label': 'Nicaragua',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1172,
            'label': 'Niger',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1173,
            'label': 'Nigeria',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1174,
            'label': 'Niue',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1175,
            'label': 'Norfolk Island',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1177,
            'label': 'Norway',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1178,
            'label': 'Oman',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1179,
            'label': 'Pakistan',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1180,
            'label': 'Palau',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1181,
            'label': 'Panama',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1182,
            'label': 'Papua New Guinea',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1183,
            'label': 'Paraguay',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1184,
            'label': 'Peru',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1185,
            'label': 'Philippines',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1186,
            'label': 'Pitcairn',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1187,
            'label': 'Plurinational State of Bolivia',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1188,
            'label': 'Poland',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1189,
            'label': 'Portugal',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1191,
            'label': 'Qatar',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1192,
            'label': 'Republic of Korea',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1193,
            'label': 'Republic of Moldova',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1235,
            'label': 'Republic of North Macedonia',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1197,
            'label': 'Réunion',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1194,
            'label': 'Romania',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1195,
            'label': 'Russian Federation',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1196,
            'label': 'Rwanda',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1198,
            'label': 'Saint Barthélemy',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1199,
            'label': 'Saint Kitts and Nevis',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1200,
            'label': 'Saint Lucia',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1201,
            'label': 'Saint Martin (French Part)',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1202,
            'label': 'Saint Pierre and Miquelon',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1203,
            'label': 'Saint Vincent and the Grenadines',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1204,
            'label': 'Samoa',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1205,
            'label': 'San Marino',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1206,
            'label': 'Sao Tome and Principe',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1207,
            'label': 'Saudi Arabia',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1208,
            'label': 'Senegal',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1209,
            'label': 'Serbia',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1210,
            'label': 'Seychelles',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1211,
            'label': 'Sierra Leone',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1212,
            'label': 'Singapore',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1213,
            'label': 'Sint Eustatius and Saba Bonaire',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1214,
            'label': 'Sint Maarten (Dutch Part)',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1215,
            'label': 'Slovakia',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1216,
            'label': 'Slovenia',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1217,
            'label': 'Solomon Islands',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1218,
            'label': 'Somalia',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1219,
            'label': 'South Africa',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1220,
            'label': 'South Georgia and the South Sandwich Islands',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1221,
            'label': 'South Sudan',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1222,
            'label': 'Spain',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1223,
            'label': 'Sri Lanka',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1224,
            'label': 'State of Palestine',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1225,
            'label': 'Sudan',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1226,
            'label': 'Suriname',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1227,
            'label': 'Svalbard and Jan Mayen',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1228,
            'label': 'Swaziland',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1229,
            'label': 'Sweden',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1230,
            'label': 'Switzerland',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1231,
            'label': 'Syrian Arab Republic',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1190,
            'label': 'Taiwan',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1232,
            'label': 'Tajikistan',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1233,
            'label': 'Thailand',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1234,
            'label': 'The Democratic Republic of the Congo',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1074,
            'label': "The Republic of Côte d'Ivoire",
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1236,
            'label': 'Timor-Leste',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1237,
            'label': 'Togo',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1238,
            'label': 'Tokelau',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1239,
            'label': 'Tonga',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1240,
            'label': 'Trinidad and Tobago',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1241,
            'label': 'Tunisia',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1242,
            'label': 'Turkey',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1243,
            'label': 'Turkmenistan',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1244,
            'label': 'Turks and Caicos Islands',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1245,
            'label': 'Tuvalu',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1246,
            'label': 'Uganda',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1247,
            'label': 'Ukraine',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1248,
            'label': 'United Arab Emirates',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1249,
            'label': 'United Kingdom',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1250,
            'label': 'United Republic of Tanzania',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1000,
            'label': 'United States',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1251,
            'label': 'United States Minor Outlying Islands',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1252,
            'label': 'Uruguay',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1253,
            'label': 'Uzbekistan',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1254,
            'label': 'Vanuatu',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1255,
            'label': 'Viet Nam',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1256,
            'label': 'Wallis and Futuna',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1257,
            'label': 'Western Sahara',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1258,
            'label': 'Yemen',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1259,
            'label': 'Zambia',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1260,
            'label': 'Zimbabwe',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          }
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': True
      },
      'create_date': {
        'id': 390,
        'name': 'create_date',
        'text': 'Date Created',
        'prefix': None,
        'type_id': 0,
        'tooltip': 'The date the incident was created. This field is read-only.',
        'input_type': 'datetimepicker',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': True,
        'uuid': 'b4faf728-881a-4e8b-bf0b-d39b720392a1',
        'values': [
          
        ],
        'read_only': True,
        'changeable': False,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'creator_id': {
        'id': 392,
        'name': 'creator_id',
        'text': 'Created By',
        'prefix': None,
        'type_id': 0,
        'input_type': 'select_owner',
        'hide_notification': False,
        'chosen': True,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': True,
        'uuid': '91f2b232-bb43-4007-ab91-aacfd02d9e7a',
        'values': [
          {
            'value': 7,
            'label': 'Resilient Sysadmin (a@example.com)',
            'enabled': True,
            'properties': None,
            'uuid': '41be6245-bd72-46e3-bbd5-a156e9c35068',
            'hidden': False,
            'default': False
          },
          {
            'value': 16,
            'label': 'Resilient Sysadmin (b@example.com)',
            'enabled': True,
            'properties': None,
            'uuid': 'bebf9f38-061b-4008-948f-dfc709935212',
            'hidden': False,
            'default': False
          },
          {
            'value': 17,
            'label': 'Resilient Sysadmin (c@example.com)',
            'enabled': True,
            'properties': None,
            'uuid': '577ab0e9-4933-4458-b554-8f97a53ea91a',
            'hidden': False,
            'default': False
          },
          {
            'value': 23,
            'label': 'Resilient Sysadmin (d@example.com)',
            'enabled': True,
            'properties': None,
            'uuid': '841e054d-c338-4c5d-ae9f-004c6bbbcc45',
            'hidden': False,
            'default': False
          },
          {
            'value': 6,
            'label': 'Default Group',
            'enabled': True,
            'properties': None,
            'uuid': '6f52ab7d-cbca-41ad-ab43-6ee779fe066e',
            'hidden': False,
            'default': False
          },
          {
            'value': 43,
            'label': 'fn_aws_guardduty',
            'enabled': True,
            'properties': None,
            'uuid': 'dc3bc875-9711-4d0a-a031-95111ec52695',
            'hidden': False,
            'default': False
          },
          {
            'value': 34,
            'label': 'IBM SOAR LDAP Utilities',
            'enabled': True,
            'properties': None,
            'uuid': 'a8785ad4-77b0-41d6-88e3-da2f5b492cf3',
            'hidden': False,
            'default': False
          },
          {
            'value': 41,
            'label': 'Netskope App for IBM SOAR',
            'enabled': True,
            'properties': None,
            'uuid': 'df057dc2-cbb8-4e08-95ec-0034e8a9d0c2',
            'hidden': False,
            'default': False
          },
          {
            'value': 37,
            'label': 'Microsoft Defender',
            'enabled': True,
            'properties': None,
            'uuid': 'ac251c59-57a9-4f25-8fe5-efdb82c7208e',
            'hidden': False,
            'default': False
          },
          {
            'value': 21,
            'label': 'Chronicle App for IBM SOAR',
            'enabled': True,
            'properties': None,
            'uuid': 'a76b3fda-dfaa-4d81-a298-4b5ca419be8f',
            'hidden': False,
            'default': False
          },
          {
            'value': 27,
            'label': 'Outbound Email',
            'enabled': True,
            'properties': None,
            'uuid': '1df6e58b-22ae-4b99-8cb3-9b422f00b24b',
            'hidden': False,
            'default': False
          },
          {
            'value': 32,
            'label': 'QRadar Enhanced Data Migration',
            'enabled': True,
            'properties': None,
            'uuid': 'c2a1268a-3175-4af0-8b30-ece93ffd29af',
            'hidden': False,
            'default': False
          },
          {
            'value': 48,
            'label': 'low_code',
            'enabled': True,
            'properties': None,
            'uuid': '7a0fb813-5d28-4b95-8764-fd867228b95f',
            'hidden': False,
            'default': False
          },
          {
            'value': 29,
            'label': 'VirusTotal',
            'enabled': True,
            'properties': None,
            'uuid': 'fc3d48d0-17bc-40da-9ef8-abefbdc44ca7',
            'hidden': False,
            'default': False
          },
          {
            'value': 40,
            'label': 'fn_mimecast',
            'enabled': True,
            'properties': None,
            'uuid': 'f3d8a237-6ed9-4660-b23b-ed62191d1d0d',
            'hidden': False,
            'default': False
          },
          {
            'value': 47,
            'label': 'fn_whois_rdap',
            'enabled': True,
            'properties': None,
            'uuid': 'e1fa35c2-101f-4a75-84cd-c86abc3a08c0',
            'hidden': False,
            'default': False
          },
          {
            'value': 42,
            'label': 'Trend Micro Deep Security',
            'enabled': True,
            'properties': None,
            'uuid': 'c4b9bd8b-27c3-4ff9-b9d0-8f36f166aa68',
            'hidden': False,
            'default': False
          },
          {
            'value': 44,
            'label': 'ITS Inventory & IBM SOAR',
            'enabled': True,
            'properties': None,
            'uuid': 'eed41111-efc5-4f1b-aa4d-d19d40f7e4d7',
            'hidden': False,
            'default': False
          },
          {
            'value': 38,
            'label': 'fn_task_utils',
            'enabled': True,
            'properties': None,
            'uuid': 'cf1a0f3f-d487-4dc8-946b-4f0438b8df2e',
            'hidden': False,
            'default': False
          },
          {
            'value': 24,
            'label': 'pipeline test',
            'enabled': True,
            'properties': None,
            'uuid': 'b386c859-f97b-4f1e-a2ee-ffcc72de6697',
            'hidden': False,
            'default': False
          },
          {
            'value': 31,
            'label': 'Ansible for SOAR',
            'enabled': True,
            'properties': None,
            'uuid': 'c1ef9add-1181-43f9-a73b-4a8b0be87c44',
            'hidden': False,
            'default': False
          },
          {
            'value': 36,
            'label': 'Axonius',
            'enabled': True,
            'properties': None,
            'uuid': 'a666334f-0b94-4a5b-8b2a-abf40a00c93a',
            'hidden': False,
            'default': False
          },
          {
            'value': 33,
            'label': 'Scheduler',
            'enabled': True,
            'properties': None,
            'uuid': '2675c895-a233-4179-b383-84bb7d6a7669',
            'hidden': False,
            'default': False
          },
          {
            'value': 39,
            'label': 'Microsoft Sentinel',
            'enabled': True,
            'properties': None,
            'uuid': '4aed886e-95c8-4fb3-98f7-a7fc1296edaf',
            'hidden': False,
            'default': False
          },
          {
            'value': 0,
            'label': 'System User',
            'enabled': True,
            'properties': None,
            'uuid': 'd82191c4-8171-4110-91db-0c1aa3235a88',
            'hidden': False,
            'default': False
          },
          {
            'value': 26,
            'label': 'ODBC Functions for SOAR',
            'enabled': True,
            'properties': None,
            'uuid': '36a03cfc-f237-457a-8e0f-d2a8da1a34e5',
            'hidden': False,
            'default': False
          },
          {
            'value': 45,
            'label': 'Microsoft Teams',
            'enabled': True,
            'properties': None,
            'uuid': '4c742b35-252f-4df7-9278-ce29ced7cfc7',
            'hidden': False,
            'default': False
          },
          {
            'value': 8,
            'label': 'Microsoft Teams',
            'enabled': True,
            'properties': None,
            'uuid': '932e6235-f4dc-4e9b-b791-7c5d29524704',
            'hidden': False,
            'default': False
          },
          {
            'value': 9,
            'label': 'QRadar Integration',
            'enabled': True,
            'properties': None,
            'uuid': 'b4074d2b-32d8-4410-9bb5-2fe9630230f7',
            'hidden': False,
            'default': False
          },
          {
            'value': 20,
            'label': 'REST API Functions for SOAR',
            'enabled': True,
            'properties': None,
            'uuid': 'b96c09c6-001e-4bf2-ae73-d313f3cee4bc',
            'hidden': False,
            'default': False
          },
          {
            'value': 46,
            'label': 'fn_urlhaus',
            'enabled': True,
            'properties': None,
            'uuid': 'c89c1b95-c8a9-47e9-9434-702d1aef6846',
            'hidden': False,
            'default': False
          },
          {
            'value': 30,
            'label': 'Data Feeder ODBC Plugin for SOAR',
            'enabled': True,
            'properties': None,
            'uuid': '0f25e515-c89f-435c-be8a-b52c74e95f70',
            'hidden': False,
            'default': False
          },
          {
            'value': 28,
            'label': 'ODBC Functions for SOAR',
            'enabled': True,
            'properties': None,
            'uuid': '567467f9-f162-49d0-af95-70e02d51345d',
            'hidden': False,
            'default': False
          },
          {
            'value': 12,
            'label': 'Data Feeder for QRadar SOAR',
            'enabled': True,
            'properties': None,
            'uuid': 'c5f590c0-9316-48dc-a5f2-de0b009a8c21',
            'hidden': False,
            'default': False
          },
          {
            'value': 35,
            'label': 'fn_stix_shifter_wrapper',
            'enabled': True,
            'properties': None,
            'uuid': '9471345b-c9e3-460a-a76b-cd82edb16a68',
            'hidden': False,
            'default': False
          },
          {
            'value': 14,
            'label': 'bidirectional resilientfeed',
            'enabled': True,
            'properties': None,
            'uuid': '5e65575a-d3b2-4f43-9a88-e46fa80544d9',
            'hidden': False,
            'default': False
          },
          {
            'value': 18,
            'label': 'Parent/Child Relationships',
            'enabled': True,
            'properties': None,
            'uuid': 'e150eb93-7996-42d4-bbd2-590a69fba3be',
            'hidden': False,
            'default': False
          },
          {
            'value': 25,
            'label': 'CheckPoint Next Generation Firewalls',
            'enabled': True,
            'properties': None,
            'uuid': '5999f876-d487-44c9-9fd1-b9505894a197',
            'hidden': False,
            'default': False
          }
        ],
        'read_only': True,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'crimestatus_id': {
        'id': 384,
        'name': 'crimestatus_id',
        'text': 'Criminal Activity',
        'prefix': None,
        'type_id': 0,
        'input_type': 'select',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': True,
        'uuid': '994180bf-ee21-488e-9b99-3a3159642851',
        'values': [
          {
            'value': 1,
            'label': 'No',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 2,
            'label': 'Yes',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 3,
            'label': 'Yes - Freeze Tasks',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 4,
            'label': 'Completed',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 5,
            'label': 'Unknown',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          }
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'cumulative_score': {
        'id': 396,
        'name': 'cumulative_score',
        'text': 'XDR Severity Score',
        'prefix': None,
        'type_id': 0,
        'tooltip': '[Deprecated, please use Automatic Score] A numerical representation of the XDR severity. Values range from 0.0 to 1.0, where 0.0 indicates absence of risk and 1.0 indicates maximum risk.',
        'input_type': 'number',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': True,
        'uuid': '4ed928b7-6cf6-436d-a216-edefde5e59f2',
        'values': [
          
        ],
        'read_only': True,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': True,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'custom_text': {
        'id': 1089,
        'name': 'custom_text',
        'text': 'custom_text',
        'short_text': '',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': '',
        'placeholder': '',
        'input_type': 'text',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': '170ba652-1c21-4f1f-8274-920646a677f1',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'data_compromised': {
        'id': 324,
        'name': 'data_compromised',
        'text': 'Was personal information or personal data involved?',
        'prefix': 'pii',
        'type_id': 0,
        'tooltip': 'Determine whether personal information/data was foreseeably involved, disclosed, compromised, accessed, altered, destroyed, damaged, lost or inaccessible.',
        'input_type': 'boolean',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': True,
        'uuid': '793e1363-79f5-45af-91e2-0e93356cad82',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'data_contained': {
        'id': 368,
        'name': 'data_contained',
        'text': 'Exposure Resolved',
        'prefix': 'pii',
        'type_id': 0,
        'tooltip': 'Whether the exposure has been addressed and rectified.',
        'input_type': 'boolean',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': True,
        'uuid': 'ac1398bd-350d-4072-9754-7f8262119ec0',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'data_encrypted': {
        'id': 366,
        'name': 'data_encrypted',
        'text': 'Data Encrypted',
        'prefix': 'pii',
        'type_id': 0,
        'tooltip': 'Whether the data in question was encrypted. Data should not be considered encrypted if the encryption keys were also breached.',
        'input_type': 'boolean',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': True,
        'uuid': '392851a9-1b28-4913-91cb-2915db7f9d6b',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'data_format': {
        'id': 341,
        'name': 'data_format',
        'text': 'Data Format',
        'prefix': 'pii',
        'type_id': 0,
        'tooltip': 'Specify the format of the personal information involved.',
        'input_type': 'select',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': True,
        'internal': True,
        'uuid': 'af9cd3c2-ca43-48ab-b37e-e9d7ede15c15',
        'values': [
          {
            'value': 0,
            'label': 'Electronic',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1,
            'label': 'Paper',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 2,
            'label': 'Verbal',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          }
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'data_source_ids': {
        'id': 333,
        'name': 'data_source_ids',
        'text': 'Source of Data',
        'prefix': 'pii',
        'type_id': 0,
        'tooltip': 'Original source of the data, such as the name of the database.',
        'input_type': 'multiselect',
        'hide_notification': False,
        'chosen': True,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': True,
        'uuid': 'e4d65b3a-9dca-492b-acb7-d2b33e3d5913',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'dc_impact_likely': {
        'id': 373,
        'name': 'dc_impact_likely',
        'text': 'Impact Likely for District of Columbia',
        'prefix': 'pii',
        'type_id': 0,
        'input_type': 'boolean',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': True,
        'uuid': 'a97ce7c1-a7ec-4efe-822d-e32443392924',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': True,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'defender_classification': {
        'id': 1866,
        'name': 'defender_classification',
        'text': 'Defender Classification',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': '',
        'placeholder': '',
        'input_type': 'select',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': True,
        'internal': False,
        'uuid': '664be662-7287-425b-be99-288834c719ef',
        'values': [
          {
            'value': 403,
            'label': 'Unknown',
            'enabled': True,
            'properties': None,
            'uuid': '790517f2-a4cf-49b1-bf2d-fb33c124a20c',
            'hidden': False,
            'default': True
          },
          {
            'value': 404,
            'label': 'FalsePositive',
            'enabled': True,
            'properties': None,
            'uuid': 'd2a3e477-7275-42ab-9cec-6a7d69f42187',
            'hidden': False,
            'default': False
          },
          {
            'value': 405,
            'label': 'TruePositive',
            'enabled': True,
            'properties': None,
            'uuid': '799a7aee-b262-45d9-9023-d270d87d800d',
            'hidden': False,
            'default': False
          }
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'defender_determination': {
        'id': 1862,
        'name': 'defender_determination',
        'text': 'Defender Determination',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': '',
        'placeholder': '',
        'input_type': 'select',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': True,
        'internal': False,
        'uuid': 'e834b645-b403-4803-a0f6-e1f176e7f4c1',
        'values': [
          {
            'value': 396,
            'label': 'NotAvailable',
            'enabled': True,
            'properties': None,
            'uuid': '783d3720-1457-4742-85f5-7b913f476449',
            'hidden': False,
            'default': True
          },
          {
            'value': 397,
            'label': 'Apt',
            'enabled': True,
            'properties': None,
            'uuid': '811e9520-4ffe-4a24-a022-a0736846af0d',
            'hidden': False,
            'default': False
          },
          {
            'value': 398,
            'label': 'Malware',
            'enabled': True,
            'properties': None,
            'uuid': '712a9895-3e17-4a97-a77a-d00ab04f7c0f',
            'hidden': False,
            'default': False
          },
          {
            'value': 399,
            'label': 'SecurityPersonnel',
            'enabled': True,
            'properties': None,
            'uuid': '9aeffada-9bbc-4102-9e20-a0599ab0f18a',
            'hidden': False,
            'default': False
          },
          {
            'value': 400,
            'label': 'SecurityTesting',
            'enabled': True,
            'properties': None,
            'uuid': '378fbc0d-2347-4d0b-a4ce-360d3e2b5c04',
            'hidden': False,
            'default': False
          },
          {
            'value': 401,
            'label': 'UnwantedSoftware',
            'enabled': True,
            'properties': None,
            'uuid': 'c6879450-1d49-4e2d-8084-1d9ce27ed9b0',
            'hidden': False,
            'default': False
          },
          {
            'value': 402,
            'label': 'Other',
            'enabled': True,
            'properties': None,
            'uuid': '02725beb-1072-4590-b32c-a7adc79f8a0b',
            'hidden': False,
            'default': False
          }
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'defender_incident_createtime': {
        'id': 1865,
        'name': 'defender_incident_createtime',
        'text': 'Defender Incident CreateTime',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': '',
        'placeholder': '',
        'input_type': 'datetimepicker',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': '38595dca-758c-4262-af29-003e2d28702a',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'defender_incident_id': {
        'id': 1864,
        'name': 'defender_incident_id',
        'text': 'Defender Incident Id',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': '',
        'placeholder': '',
        'input_type': 'number',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': '21e17c1f-d21f-41b2-bdd8-2ba42d8c62f7',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'defender_incident_lastupdatetime': {
        'id': 1860,
        'name': 'defender_incident_lastupdatetime',
        'text': 'Defender Incident LastUpdateTime',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': '',
        'placeholder': '',
        'input_type': 'datepicker',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': '9ffdfe40-77b7-4233-b3c9-51e6ce377966',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'defender_incident_url': {
        'id': 1863,
        'name': 'defender_incident_url',
        'text': 'Defender Incident Url',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': '',
        'placeholder': '',
        'input_type': 'textarea',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': '12e093cf-2138-4a5c-a676-14854df356e5',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': True,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'defender_tags': {
        'id': 1861,
        'name': 'defender_tags',
        'text': 'Defender Tags',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': 'comma separated list of Defender tags',
        'placeholder': '',
        'input_type': 'text',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': 'ce4b9e0f-ddeb-4ed1-ba27-e44753d0d9d6',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'description': {
        'id': 336,
        'name': 'description',
        'text': 'Description',
        'prefix': None,
        'type_id': 0,
        'tooltip': 'A free form text description of the incident.',
        'input_type': 'textarea',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': True,
        'uuid': '420d70b1-98f9-4681-a20b-84f36a9e5e48',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': True,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'determined_date': {
        'id': 375,
        'name': 'determined_date',
        'text': 'Date Determined',
        'prefix': 'pii',
        'type_id': 0,
        'tooltip': 'Date you determined whether or not the incident involved a breach of personal information or personal data. Regulatory task timelines will be derived from this date and time.',
        'input_type': 'datetimepicker',
        'hide_notification': True,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': True,
        'uuid': 'aa86ae29-5d3c-4c70-8497-93598a9dc959',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'df_create_date': {
        'id': 1557,
        'name': 'df_create_date',
        'text': 'df_create_date',
        'short_text': '',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': '',
        'placeholder': '',
        'input_type': 'datetimepicker',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': 'ca14847e-2ddd-42d9-a111-2f65ed561d38',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'df_host': {
        'id': 1556,
        'name': 'df_host',
        'text': 'df_host',
        'short_text': '',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': '',
        'placeholder': '',
        'input_type': 'text',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': 'fe10f86c-fbe0-4abf-a709-5c3735328355',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'df_inc_id': {
        'id': 1555,
        'name': 'df_inc_id',
        'text': 'df_inc_id',
        'short_text': '',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': '',
        'placeholder': '',
        'input_type': 'number',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': '992ec599-5d1f-4f67-a8ff-946d5c5b088d',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'df_org_id': {
        'id': 1554,
        'name': 'df_org_id',
        'text': 'df_org_id',
        'short_text': '',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': '',
        'placeholder': '',
        'input_type': 'number',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': '34ad1805-ee9a-4028-97c9-4b0ab17d40d6',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'discovered_date': {
        'id': 374,
        'name': 'discovered_date',
        'text': 'Date Discovered',
        'prefix': None,
        'type_id': 0,
        'tooltip': 'Date the incident was discovered/reported.',
        'input_type': 'datetimepicker',
        'required': 'always',
        'hide_notification': True,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': True,
        'uuid': '26cb8fa6-32e2-410d-b8e5-c23af0d09263',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'due_date': {
        'id': 394,
        'name': 'due_date',
        'text': 'Next Due Date',
        'prefix': None,
        'type_id': 0,
        'tooltip': 'The nearest date for the next task due. This field is read-only.',
        'input_type': 'datetimepicker',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': True,
        'uuid': 'f549afb8-eb80-4fbf-96f1-63eac60412c8',
        'values': [
          
        ],
        'read_only': True,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'email_message_id': {
        'id': 1398,
        'name': 'email_message_id',
        'text': 'Email Message-ID',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': 'message-id associated with the inbound email message',
        'placeholder': '',
        'input_type': 'text',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': '6e7c2c42-88f7-443f-8c0d-0e84b2ba6525',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'employee_involved': {
        'id': 383,
        'name': 'employee_involved',
        'text': 'Employee Involved',
        'prefix': None,
        'type_id': 0,
        'input_type': 'boolean',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': True,
        'uuid': 'b37923eb-1ade-48d9-a067-c15a313d3264',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'end_date': {
        'id': 391,
        'name': 'end_date',
        'text': 'Date Closed',
        'prefix': None,
        'type_id': 0,
        'tooltip': 'The date the incident was closed. This field is read-only.',
        'input_type': 'datetimepicker',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': True,
        'uuid': '719d52c7-42a5-4cd6-8ce5-e8cf9317d2d1',
        'values': [
          
        ],
        'read_only': True,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'exposure_dept_id': {
        'id': 329,
        'name': 'exposure_dept_id',
        'text': 'Department',
        'prefix': None,
        'type_id': 0,
        'input_type': 'select',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': True,
        'internal': True,
        'uuid': '15c23dae-1d17-49ff-aae0-8cb457e27867',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'exposure_individual_name': {
        'id': 378,
        'name': 'exposure_individual_name',
        'text': 'Individual Name',
        'prefix': None,
        'type_id': 0,
        'placeholder': 'Employee name',
        'input_type': 'text',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': True,
        'uuid': '77618fd8-ecd9-40e5-b86f-b42eee53498f',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'exposure_type_id': {
        'id': 326,
        'name': 'exposure_type_id',
        'text': 'Exposure Type',
        'prefix': None,
        'type_id': 0,
        'tooltip': 'Origin source of the exposure',
        'input_type': 'select',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': True,
        'uuid': '5d88cef9-ce77-4618-b946-e547607a777f',
        'values': [
          {
            'value': 2,
            'label': 'External Party',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 3,
            'label': 'Individual',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1,
            'label': 'Unknown',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          }
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'exposure_vendor_id': {
        'id': 334,
        'name': 'exposure_vendor_id',
        'text': 'Vendor',
        'prefix': None,
        'type_id': 0,
        'input_type': 'select',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': True,
        'internal': True,
        'uuid': 'c8f2d2c8-c44b-45c7-b4ff-783a8702b074',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'file_path': {
        'id': 1672,
        'name': 'file_path',
        'text': 'file path',
        'short_text': '',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': '',
        'placeholder': '',
        'input_type': 'textarea',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': '74fd4b9f-b6ee-419b-8b53-b9b8713dbd22',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'gdpr_breach_circumstances': {
        'id': 350,
        'name': 'gdpr_breach_circumstances',
        'text': 'GDPR Breach Circumstances',
        'prefix': 'gdpr',
        'type_id': 0,
        'input_type': 'multiselect',
        'hide_notification': False,
        'chosen': True,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': True,
        'uuid': '5fb35a45-855f-4acc-8cea-c3d620094c2d',
        'values': [
          {
            'value': 52,
            'label': 'Confidentiality Breach',
            'enabled': True,
            'properties': None,
            'uuid': 'dedbfaf1-407d-4351-81fe-6392389a707a',
            'hidden': False,
            'default': False
          },
          {
            'value': 53,
            'label': 'Integrity Breach',
            'enabled': True,
            'properties': None,
            'uuid': 'bc24ebeb-ff67-4869-b65b-aeac64f87c77',
            'hidden': False,
            'default': False
          },
          {
            'value': 54,
            'label': 'Availability Breach',
            'enabled': True,
            'properties': None,
            'uuid': '28a5fd8b-21cf-45ae-812e-8c30e77fa1c4',
            'hidden': False,
            'default': False
          }
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'gdpr_breach_type': {
        'id': 351,
        'name': 'gdpr_breach_type',
        'text': 'GDPR Breach Type',
        'prefix': 'gdpr',
        'type_id': 0,
        'input_type': 'select',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': True,
        'internal': True,
        'uuid': '1a287fef-4b99-4a96-a8b4-7ccc3c6366fb',
        'values': [
          {
            'value': 0,
            'label': 'NoRisk',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1,
            'label': 'Risk',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 2,
            'label': 'HighRisk',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          }
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'gdpr_breach_type_comment': {
        'id': 352,
        'name': 'gdpr_breach_type_comment',
        'text': 'GDPR Breach Type Comment',
        'prefix': 'gdpr',
        'type_id': 0,
        'input_type': 'textarea',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': True,
        'uuid': '7354ee21-c548-44de-b179-2d45f119f228',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'gdpr_consequences': {
        'id': 357,
        'name': 'gdpr_consequences',
        'text': 'GDPR Consequences',
        'prefix': 'gdpr',
        'type_id': 0,
        'input_type': 'select',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': True,
        'internal': True,
        'uuid': 'd49ba8aa-3311-49e9-bfc9-440b768f0b19',
        'values': [
          {
            'value': 0,
            'label': 'NoRisk',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1,
            'label': 'Risk',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 2,
            'label': 'HighRisk',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          }
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'gdpr_consequences_comment': {
        'id': 358,
        'name': 'gdpr_consequences_comment',
        'text': 'GDPR Consequences Comment',
        'prefix': 'gdpr',
        'type_id': 0,
        'input_type': 'textarea',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': True,
        'uuid': '0064f82d-2ccb-4a5f-8f57-27d1ef95193e',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'gdpr_final_assessment': {
        'id': 359,
        'name': 'gdpr_final_assessment',
        'text': 'GDPR Final Assessment',
        'prefix': 'gdpr',
        'type_id': 0,
        'input_type': 'select',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': True,
        'internal': True,
        'uuid': 'df05d513-b972-4201-8bbb-050ce1db5cb3',
        'values': [
          {
            'value': 0,
            'label': 'NoRisk',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1,
            'label': 'Risk',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 2,
            'label': 'HighRisk',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          }
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'gdpr_final_assessment_comment': {
        'id': 360,
        'name': 'gdpr_final_assessment_comment',
        'text': 'GDPR Final Assessment Comment',
        'prefix': 'gdpr',
        'type_id': 0,
        'input_type': 'textarea',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': True,
        'uuid': 'fa91a9b6-6b12-42d6-bd40-68461d2948af',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'gdpr_harm_risk': {
        'id': 398,
        'name': 'gdpr_harm_risk',
        'text': 'Risk of Harm',
        'prefix': 'pii',
        'type_id': 0,
        'tooltip': 'Likelihood and severity of the risk to the rights and freedoms of the data subject, as defined by the GDPR.',
        'input_type': 'select',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': True,
        'internal': True,
        'uuid': '43b88739-e201-460d-a2f3-ef2073f386d3',
        'values': [
          {
            'value': 67,
            'label': 'Low Risk',
            'enabled': True,
            'properties': None,
            'uuid': '0c5a0656-e0df-422a-8fa3-78c5a79b472d',
            'hidden': False,
            'default': False
          },
          {
            'value': 68,
            'label': 'Risk',
            'enabled': True,
            'properties': None,
            'uuid': '44f4b385-6c51-4ee3-aba8-79fb19a1b1bb',
            'hidden': False,
            'default': False
          },
          {
            'value': 69,
            'label': 'High Risk',
            'enabled': True,
            'properties': None,
            'uuid': '46306313-31c4-4549-9aa3-966b986429af',
            'hidden': False,
            'default': False
          }
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': True,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'gdpr_identification': {
        'id': 355,
        'name': 'gdpr_identification',
        'text': 'GDPR Identification',
        'prefix': 'gdpr',
        'type_id': 0,
        'input_type': 'select',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': True,
        'internal': True,
        'uuid': '518e9d3a-d9d2-4211-af19-5c87049af157',
        'values': [
          {
            'value': 0,
            'label': 'NoRisk',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1,
            'label': 'Risk',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 2,
            'label': 'HighRisk',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          }
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'gdpr_identification_comment': {
        'id': 356,
        'name': 'gdpr_identification_comment',
        'text': 'GDPR Identification Comment',
        'prefix': 'gdpr',
        'type_id': 0,
        'input_type': 'textarea',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': True,
        'uuid': '519cf3ae-c02a-4197-a6f3-b944fe36052c',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'gdpr_lawful_data_processing_categories': {
        'id': 399,
        'name': 'gdpr_lawful_data_processing_categories',
        'text': 'Lawful Data Processing Categories',
        'prefix': 'pii',
        'type_id': 0,
        'tooltip': 'Under the GDPR, processing of personal or sensitive data is only lawful if one or more of these categories applies.',
        'placeholder': 'Choose Some Categories',
        'input_type': 'multiselect',
        'hide_notification': False,
        'chosen': True,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': True,
        'uuid': '000fa89b-0570-4162-a720-b4b188b06ad3',
        'values': [
          {
            'value': 70,
            'label': 'Consent by data subject',
            'enabled': True,
            'properties': None,
            'uuid': 'b31ffbc5-7e24-4a54-8c8d-e26caf7a96c7',
            'hidden': False,
            'default': False
          },
          {
            'value': 71,
            'label': 'Performance of contract',
            'enabled': True,
            'properties': None,
            'uuid': '447b6e53-ca8a-4cde-ab2c-f529132a1948',
            'hidden': False,
            'default': False
          },
          {
            'value': 72,
            'label': 'Compliance with legal obligation',
            'enabled': True,
            'properties': None,
            'uuid': '82817a05-c4ae-453b-a0ea-52be2fd43d7c',
            'hidden': False,
            'default': False
          },
          {
            'value': 73,
            'label': 'Protection of vital interests of data subject',
            'enabled': True,
            'properties': None,
            'uuid': '4ce0da31-4f52-4308-985a-7a56194617d0',
            'hidden': False,
            'default': False
          },
          {
            'value': 74,
            'label': 'Public interest or official authority',
            'enabled': True,
            'properties': None,
            'uuid': 'e1dcd2f7-4a42-4f87-add6-58d74dee7b58',
            'hidden': False,
            'default': False
          },
          {
            'value': 75,
            'label': 'Legitimate interests of data controller or third party',
            'enabled': True,
            'properties': None,
            'uuid': 'c34f95d3-23a9-46ef-b67c-f795b4928ce5',
            'hidden': False,
            'default': False
          }
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': True,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'gdpr_personal_data': {
        'id': 353,
        'name': 'gdpr_personal_data',
        'text': 'GDPR Personal Data',
        'prefix': 'gdpr',
        'type_id': 0,
        'input_type': 'select',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': True,
        'internal': True,
        'uuid': '55066e35-1ec8-4466-954c-0a4386971a73',
        'values': [
          {
            'value': 0,
            'label': 'NoRisk',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1,
            'label': 'Risk',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 2,
            'label': 'HighRisk',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          }
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'gdpr_personal_data_comment': {
        'id': 354,
        'name': 'gdpr_personal_data_comment',
        'text': 'GDPR Personal Data Comment',
        'prefix': 'gdpr',
        'type_id': 0,
        'input_type': 'textarea',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': True,
        'uuid': '77b2b8cb-ed5c-427f-a9cc-161b13859cbb',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'gdpr_subsequent_notification': {
        'id': 361,
        'name': 'gdpr_subsequent_notification',
        'text': 'GDPR Subsequent Notification',
        'prefix': 'gdpr',
        'type_id': 0,
        'input_type': 'boolean',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': True,
        'uuid': '09f66a71-8c7a-4279-a669-cc6542d124ef',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'hard_liability': {
        'id': 339,
        'name': 'hard_liability',
        'text': 'Assessed Liability',
        'prefix': None,
        'type_id': 0,
        'input_type': 'number',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': True,
        'uuid': '72c2c73f-620a-4bb6-900a-705a0bdf912d',
        'values': [
          
        ],
        'read_only': True,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': True,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'harmstatus_id': {
        'id': 380,
        'name': 'harmstatus_id',
        'text': 'Is harm/risk/misuse foreseeable?',
        'prefix': 'pii',
        'type_id': 0,
        'tooltip': 'Different jurisdictions use harm, risk, misuse, ID theft, and other standards as safe harbors from notification. Interpretation of these terms has frequently been the subject of litigation.',
        'input_type': 'select',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': True,
        'uuid': '549e822b-37ac-43c0-8e93-ddcebf533189',
        'values': [
          {
            'value': 1,
            'label': 'No',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 2,
            'label': 'Unknown',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 3,
            'label': 'Yes',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          }
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'high_volume_privacy_event': {
        'id': 1970,
        'name': 'high_volume_privacy_event',
        'text': 'High Volume Privacy Event',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': '',
        'placeholder': '',
        'input_type': 'boolean',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': '83e0e700-c8e7-414e-95da-8a02756ca42a',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'id': {
        'id': 393,
        'name': 'id',
        'text': 'ID',
        'prefix': None,
        'type_id': 0,
        'input_type': 'number',
        'hide_notification': True,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': True,
        'uuid': '44d6a6ac-886f-46ff-9683-90a13765862a',
        'values': [
          
        ],
        'read_only': True,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'impact_likely': {
        'id': 369,
        'name': 'impact_likely',
        'text': 'Impact Likely',
        'prefix': 'pii',
        'type_id': 0,
        'input_type': 'boolean',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': True,
        'uuid': '4137fbca-9ec7-42e9-9e39-9ef61197cc9b',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'inc_last_modified_date': {
        'id': 376,
        'name': 'inc_last_modified_date',
        'text': 'Last Modified',
        'prefix': None,
        'type_id': 0,
        'tooltip': 'The date the incident was last modified.This field is read only.',
        'input_type': 'datetimepicker',
        'hide_notification': True,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': True,
        'uuid': 'a75e8d1d-d940-4c8a-82f1-8839ab60d583',
        'values': [
          
        ],
        'read_only': True,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': True,
        'is_tracked': False,
        'allow_default_value': False
      },
      'inc_training': {
        'id': 389,
        'name': 'inc_training',
        'text': 'Simulation',
        'prefix': None,
        'type_id': 0,
        'tooltip': 'Whether the incident is a simulation or a regular incident.  This field is read-only.',
        'input_type': 'boolean',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': True,
        'uuid': 'c3f0e3ed-21e1-4d53-affb-fe5ca3308cca',
        'values': [
          
        ],
        'read_only': True,
        'changeable': False,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'incident_type_ids': {
        'id': 337,
        'name': 'incident_type_ids',
        'text': 'Incident Type',
        'prefix': None,
        'type_id': 0,
        'tooltip': 'The type of incident',
        'placeholder': 'Choose Some Types',
        'input_type': 'multiselect',
        'hide_notification': False,
        'chosen': True,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': True,
        'uuid': '11ed8b8a-8ffc-4dea-9699-28a351b4f212',
        'values': [
          {
            'value': 17,
            'label': 'Communication error (fax; email)',
            'enabled': True,
            'properties': None,
            'uuid': '4a8d22f7-d89e-4403-85c7-2bafe3b7f2ae',
            'hidden': False,
            'default': False
          },
          {
            'value': 1001,
            'label': 'Customization Packages (internal)',
            'enabled': False,
            'properties': None,
            'uuid': 'bfeec2d4-3770-11e8-ad39-4a0004044aa0',
            'hidden': False,
            'default': False
          },
          {
            'value': 21,
            'label': 'Denial of Service',
            'enabled': True,
            'properties': None,
            'uuid': 'e1b10c0c-21f8-4e3f-9f0f-40668ddd2a01',
            'hidden': False,
            'default': False
          },
          {
            'value': 6,
            'label': 'Improper disposal: digital asset(s)',
            'enabled': True,
            'properties': None,
            'uuid': 'a468d23f-960f-44ca-8918-4429a5aa4fa1',
            'hidden': False,
            'default': False
          },
          {
            'value': 7,
            'label': 'Improper disposal: documents / files',
            'enabled': True,
            'properties': None,
            'uuid': '5b190a80-c960-4040-bcae-15565f8c77ae',
            'hidden': False,
            'default': False
          },
          {
            'value': 4,
            'label': 'Lost documents / files / records',
            'enabled': True,
            'properties': None,
            'uuid': 'ee9b74ff-52ea-4a5d-9267-6648c8996950',
            'hidden': False,
            'default': False
          },
          {
            'value': 3,
            'label': 'Lost PC / laptop / tablet',
            'enabled': True,
            'properties': None,
            'uuid': '9235ae9f-bfb1-4c34-8022-96a86c79e677',
            'hidden': False,
            'default': False
          },
          {
            'value': 1,
            'label': 'Lost PDA / smartphone',
            'enabled': True,
            'properties': None,
            'uuid': 'b038d098-837c-4c0d-8f3d-ea639f42a1bf',
            'hidden': False,
            'default': False
          },
          {
            'value': 8,
            'label': 'Lost storage device / media',
            'enabled': True,
            'properties': None,
            'uuid': '8bbfc278-f58b-453d-874f-8dcad1ba3253',
            'hidden': False,
            'default': False
          },
          {
            'value': 19,
            'label': 'Malware',
            'enabled': True,
            'properties': None,
            'uuid': 'f441538a-2f23-48ca-9af6-45ce7b3971f1',
            'hidden': False,
            'default': False
          },
          {
            'value': 23,
            'label': 'Not an Issue',
            'enabled': True,
            'properties': None,
            'uuid': 'c8a80794-47ba-4708-983f-d6e56905b587',
            'hidden': False,
            'default': False
          },
          {
            'value': 18,
            'label': 'Other',
            'enabled': True,
            'properties': None,
            'uuid': '48e1b3b6-e5a6-44a5-a5d1-dd9c6bfdfa9e',
            'hidden': False,
            'default': False
          },
          {
            'value': 22,
            'label': 'Phishing',
            'enabled': True,
            'properties': None,
            'uuid': 'bbb113d4-86f3-4cbf-94e0-931aa693e62a',
            'hidden': False,
            'default': False
          },
          {
            'value': 11,
            'label': 'Stolen documents / files / records',
            'enabled': True,
            'properties': None,
            'uuid': 'e7105d3b-f7bc-4680-8c2d-55d32e6787bb',
            'hidden': False,
            'default': False
          },
          {
            'value': 12,
            'label': 'Stolen PC / laptop / tablet',
            'enabled': True,
            'properties': None,
            'uuid': '2b25f669-82a1-4138-9371-0843f5b674b4',
            'hidden': False,
            'default': False
          },
          {
            'value': 13,
            'label': 'Stolen PDA / smartphone',
            'enabled': True,
            'properties': None,
            'uuid': '21b6cc0d-fb98-47cd-9882-cb854ebe641a',
            'hidden': False,
            'default': False
          },
          {
            'value': 14,
            'label': 'Stolen storage device / media',
            'enabled': True,
            'properties': None,
            'uuid': 'da239c99-f0c6-4e61-99aa-b968eda85434',
            'hidden': False,
            'default': False
          },
          {
            'value': 20,
            'label': 'System Intrusion',
            'enabled': True,
            'properties': None,
            'uuid': '2caf1eca-2463-4e9c-8885-16637fc91f3f',
            'hidden': False,
            'default': False
          },
          {
            'value': 16,
            'label': 'TBD / Unknown',
            'enabled': True,
            'properties': None,
            'uuid': '8a506ca3-b848-4019-8c20-203543d907fe',
            'hidden': False,
            'default': False
          },
          {
            'value': 15,
            'label': 'Vendor / 3rd party error',
            'enabled': True,
            'properties': None,
            'uuid': 'afd3e485-178f-496d-8cd8-639b791ca0a6',
            'hidden': False,
            'default': False
          }
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'internal_customizations_field': {
        'id': 643,
        'name': 'internal_customizations_field',
        'text': 'Customizations Field (internal)',
        'prefix': 'properties',
        'type_id': 0,
        'input_type': 'text',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': 'bfeec2d4-3770-11e8-ad39-4a0004044aa1',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'jurisdiction_name': {
        'id': 322,
        'name': 'jurisdiction_name',
        'text': 'Jurisdiction',
        'prefix': None,
        'type_id': 0,
        'input_type': 'text',
        'hide_notification': False,
        'chosen': True,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': True,
        'uuid': '658354fe-3bcd-429e-aa08-5998799cc6d2',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'ldap_base_dn': {
        'id': 1761,
        'name': 'ldap_base_dn',
        'text': 'LDAP Base DN',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': '',
        'placeholder': 'DC=example,DC=com',
        'input_type': 'text',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': 'cbbaeed3-20a6-4bd8-a293-a0ab05c5e887',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'ldap_domain_name': {
        'id': 1762,
        'name': 'ldap_domain_name',
        'text': 'LDAP Domain Name',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': 'Domain name label given to the LDAP server you wish to use',
        'placeholder': '',
        'input_type': 'text',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': '4201f42b-e7a0-49c6-a8d5-ac16649f40a5',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'members': {
        'id': 367,
        'name': 'members',
        'text': 'Members',
        'prefix': None,
        'type_id': 0,
        'input_type': 'multiselect_members',
        'hide_notification': False,
        'chosen': True,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': True,
        'uuid': 'cf473808-ea3b-4e47-833b-3507891bea5e',
        'values': [
          {
            'value': 7,
            'label': 'Resilient Sysadmin (a@example.com)',
            'enabled': True,
            'properties': None,
            'uuid': '41be6245-bd72-46e3-bbd5-a156e9c35068',
            'hidden': False,
            'default': False
          },
          {
            'value': 16,
            'label': 'Resilient Sysadmin (b@example.com)',
            'enabled': True,
            'properties': None,
            'uuid': 'bebf9f38-061b-4008-948f-dfc709935212',
            'hidden': False,
            'default': False
          },
          {
            'value': 17,
            'label': 'Resilient Sysadmin (c@example.com)',
            'enabled': True,
            'properties': None,
            'uuid': '577ab0e9-4933-4458-b554-8f97a53ea91a',
            'hidden': False,
            'default': False
          },
          {
            'value': 23,
            'label': 'Resilient Sysadmin (d@example.com)',
            'enabled': True,
            'properties': None,
            'uuid': '841e054d-c338-4c5d-ae9f-004c6bbbcc45',
            'hidden': False,
            'default': False
          },
          {
            'value': 6,
            'label': 'Default Group',
            'enabled': True,
            'properties': None,
            'uuid': '6f52ab7d-cbca-41ad-ab43-6ee779fe066e',
            'hidden': False,
            'default': False
          },
          {
            'value': 43,
            'label': 'fn_aws_guardduty',
            'enabled': True,
            'properties': None,
            'uuid': 'dc3bc875-9711-4d0a-a031-95111ec52695',
            'hidden': False,
            'default': False
          },
          {
            'value': 34,
            'label': 'IBM SOAR LDAP Utilities',
            'enabled': True,
            'properties': None,
            'uuid': 'a8785ad4-77b0-41d6-88e3-da2f5b492cf3',
            'hidden': False,
            'default': False
          },
          {
            'value': 41,
            'label': 'Netskope App for IBM SOAR',
            'enabled': True,
            'properties': None,
            'uuid': 'df057dc2-cbb8-4e08-95ec-0034e8a9d0c2',
            'hidden': False,
            'default': False
          },
          {
            'value': 37,
            'label': 'Microsoft Defender',
            'enabled': True,
            'properties': None,
            'uuid': 'ac251c59-57a9-4f25-8fe5-efdb82c7208e',
            'hidden': False,
            'default': False
          },
          {
            'value': 21,
            'label': 'Chronicle App for IBM SOAR',
            'enabled': True,
            'properties': None,
            'uuid': 'a76b3fda-dfaa-4d81-a298-4b5ca419be8f',
            'hidden': False,
            'default': False
          },
          {
            'value': 27,
            'label': 'Outbound Email',
            'enabled': True,
            'properties': None,
            'uuid': '1df6e58b-22ae-4b99-8cb3-9b422f00b24b',
            'hidden': False,
            'default': False
          },
          {
            'value': 32,
            'label': 'QRadar Enhanced Data Migration',
            'enabled': True,
            'properties': None,
            'uuid': 'c2a1268a-3175-4af0-8b30-ece93ffd29af',
            'hidden': False,
            'default': False
          },
          {
            'value': 48,
            'label': 'low_code',
            'enabled': True,
            'properties': None,
            'uuid': '7a0fb813-5d28-4b95-8764-fd867228b95f',
            'hidden': False,
            'default': False
          },
          {
            'value': 29,
            'label': 'VirusTotal',
            'enabled': True,
            'properties': None,
            'uuid': 'fc3d48d0-17bc-40da-9ef8-abefbdc44ca7',
            'hidden': False,
            'default': False
          },
          {
            'value': 40,
            'label': 'fn_mimecast',
            'enabled': True,
            'properties': None,
            'uuid': 'f3d8a237-6ed9-4660-b23b-ed62191d1d0d',
            'hidden': False,
            'default': False
          },
          {
            'value': 47,
            'label': 'fn_whois_rdap',
            'enabled': True,
            'properties': None,
            'uuid': 'e1fa35c2-101f-4a75-84cd-c86abc3a08c0',
            'hidden': False,
            'default': False
          },
          {
            'value': 42,
            'label': 'Trend Micro Deep Security',
            'enabled': True,
            'properties': None,
            'uuid': 'c4b9bd8b-27c3-4ff9-b9d0-8f36f166aa68',
            'hidden': False,
            'default': False
          },
          {
            'value': 44,
            'label': 'ITS Inventory & IBM SOAR',
            'enabled': True,
            'properties': None,
            'uuid': 'eed41111-efc5-4f1b-aa4d-d19d40f7e4d7',
            'hidden': False,
            'default': False
          },
          {
            'value': 38,
            'label': 'fn_task_utils',
            'enabled': True,
            'properties': None,
            'uuid': 'cf1a0f3f-d487-4dc8-946b-4f0438b8df2e',
            'hidden': False,
            'default': False
          },
          {
            'value': 24,
            'label': 'pipeline test',
            'enabled': True,
            'properties': None,
            'uuid': 'b386c859-f97b-4f1e-a2ee-ffcc72de6697',
            'hidden': False,
            'default': False
          },
          {
            'value': 31,
            'label': 'Ansible for SOAR',
            'enabled': True,
            'properties': None,
            'uuid': 'c1ef9add-1181-43f9-a73b-4a8b0be87c44',
            'hidden': False,
            'default': False
          },
          {
            'value': 36,
            'label': 'Axonius',
            'enabled': True,
            'properties': None,
            'uuid': 'a666334f-0b94-4a5b-8b2a-abf40a00c93a',
            'hidden': False,
            'default': False
          },
          {
            'value': 33,
            'label': 'Scheduler',
            'enabled': True,
            'properties': None,
            'uuid': '2675c895-a233-4179-b383-84bb7d6a7669',
            'hidden': False,
            'default': False
          },
          {
            'value': 39,
            'label': 'Microsoft Sentinel',
            'enabled': True,
            'properties': None,
            'uuid': '4aed886e-95c8-4fb3-98f7-a7fc1296edaf',
            'hidden': False,
            'default': False
          },
          {
            'value': 0,
            'label': 'System User',
            'enabled': True,
            'properties': None,
            'uuid': 'd82191c4-8171-4110-91db-0c1aa3235a88',
            'hidden': False,
            'default': False
          },
          {
            'value': 26,
            'label': 'ODBC Functions for SOAR',
            'enabled': True,
            'properties': None,
            'uuid': '36a03cfc-f237-457a-8e0f-d2a8da1a34e5',
            'hidden': False,
            'default': False
          },
          {
            'value': 45,
            'label': 'Microsoft Teams',
            'enabled': True,
            'properties': None,
            'uuid': '4c742b35-252f-4df7-9278-ce29ced7cfc7',
            'hidden': False,
            'default': False
          },
          {
            'value': 8,
            'label': 'Microsoft Teams',
            'enabled': True,
            'properties': None,
            'uuid': '932e6235-f4dc-4e9b-b791-7c5d29524704',
            'hidden': False,
            'default': False
          },
          {
            'value': 9,
            'label': 'QRadar Integration',
            'enabled': True,
            'properties': None,
            'uuid': 'b4074d2b-32d8-4410-9bb5-2fe9630230f7',
            'hidden': False,
            'default': False
          },
          {
            'value': 20,
            'label': 'REST API Functions for SOAR',
            'enabled': True,
            'properties': None,
            'uuid': 'b96c09c6-001e-4bf2-ae73-d313f3cee4bc',
            'hidden': False,
            'default': False
          },
          {
            'value': 46,
            'label': 'fn_urlhaus',
            'enabled': True,
            'properties': None,
            'uuid': 'c89c1b95-c8a9-47e9-9434-702d1aef6846',
            'hidden': False,
            'default': False
          },
          {
            'value': 30,
            'label': 'Data Feeder ODBC Plugin for SOAR',
            'enabled': True,
            'properties': None,
            'uuid': '0f25e515-c89f-435c-be8a-b52c74e95f70',
            'hidden': False,
            'default': False
          },
          {
            'value': 28,
            'label': 'ODBC Functions for SOAR',
            'enabled': True,
            'properties': None,
            'uuid': '567467f9-f162-49d0-af95-70e02d51345d',
            'hidden': False,
            'default': False
          },
          {
            'value': 12,
            'label': 'Data Feeder for QRadar SOAR',
            'enabled': True,
            'properties': None,
            'uuid': 'c5f590c0-9316-48dc-a5f2-de0b009a8c21',
            'hidden': False,
            'default': False
          },
          {
            'value': 35,
            'label': 'fn_stix_shifter_wrapper',
            'enabled': True,
            'properties': None,
            'uuid': '9471345b-c9e3-460a-a76b-cd82edb16a68',
            'hidden': False,
            'default': False
          },
          {
            'value': 14,
            'label': 'bidirectional resilientfeed',
            'enabled': True,
            'properties': None,
            'uuid': '5e65575a-d3b2-4f43-9a88-e46fa80544d9',
            'hidden': False,
            'default': False
          },
          {
            'value': 18,
            'label': 'Parent/Child Relationships',
            'enabled': True,
            'properties': None,
            'uuid': 'e150eb93-7996-42d4-bbd2-590a69fba3be',
            'hidden': False,
            'default': False
          },
          {
            'value': 25,
            'label': 'CheckPoint Next Generation Firewalls',
            'enabled': True,
            'properties': None,
            'uuid': '5999f876-d487-44c9-9fd1-b9505894a197',
            'hidden': False,
            'default': False
          }
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'name': {
        'id': 338,
        'name': 'name',
        'text': 'Name',
        'prefix': None,
        'type_id': 0,
        'tooltip': 'A unique name to identify this particular incident.',
        'input_type': 'text',
        'required': 'always',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': True,
        'uuid': 'ad6ed4f2-8d87-4ba2-81fa-03568a9326cc',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'negative_pr_likely': {
        'id': 381,
        'name': 'negative_pr_likely',
        'text': 'Negative PR',
        'prefix': None,
        'type_id': 0,
        'tooltip': 'If it is foreseeable that the incident might generate any negative public image or publicity for your company or organization.',
        'input_type': 'boolean',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': True,
        'uuid': '94dbbd0e-3c82-4650-bd17-bddb3003a7e6',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'new_zealand_risk_assessment': {
        'id': 363,
        'name': 'new_zealand_risk_assessment',
        'text': 'New Zealand Risk Assessment',
        'prefix': 'pii',
        'type_id': 0,
        'input_type': 'boolean',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': True,
        'uuid': '19d1232b-f78e-4514-88c6-5133a51bc8b1',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': True,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'nist_attack_vectors': {
        'id': 323,
        'name': 'nist_attack_vectors',
        'text': 'NIST Attack Vectors',
        'prefix': None,
        'type_id': 0,
        'tooltip': 'NIST Attack Vectors the incident falls under, if applicable.',
        'placeholder': 'Choose Applicable Vectors',
        'input_type': 'multiselect',
        'hide_notification': False,
        'chosen': True,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': True,
        'uuid': '6fd423e6-2817-407f-b950-f66cb2e58d2c',
        'values': [
          {
            'value': 2,
            'label': 'Attrition (Denial-of-Service and Brute-Force Attacks)',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 4,
            'label': 'E-mail',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1,
            'label': 'External/Removable Media',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 5,
            'label': 'Impersonation',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 6,
            'label': 'Improper Usage',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 7,
            'label': 'Loss or Theft of Equipment',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 8,
            'label': 'Other',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 3,
            'label': 'Web',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          }
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'ny_impact_likely': {
        'id': 370,
        'name': 'ny_impact_likely',
        'text': 'Impact Likely for New York',
        'prefix': 'pii',
        'type_id': 0,
        'input_type': 'boolean',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': True,
        'uuid': '688a9bc2-cd38-4a45-b7ff-9344b76597fb',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': True,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'object_netskope': {
        'id': 2276,
        'name': 'object_netskope',
        'text': 'Object (Netskope)',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': 'Name of the object which is being acted on',
        'placeholder': '',
        'input_type': 'text',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': 'd17ce37b-294f-4828-8211-911f325cf43c',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'object_type_netskope': {
        'id': 2277,
        'name': 'object_type_netskope',
        'text': 'Object Type (Netskope)',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': 'Type of the object which is being acted on',
        'placeholder': '',
        'input_type': 'text',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': 'd566051c-70e8-45a9-886f-e90e06aa778e',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'offense_name': {
        'id': 1359,
        'name': 'offense_name',
        'text': 'offense_name',
        'short_text': '',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': '',
        'placeholder': '',
        'input_type': 'text',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': 'e89e41a5-853b-4355-bab7-60e3592cb834',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'offense_type': {
        'id': 1360,
        'name': 'offense_type',
        'text': 'offense_type',
        'short_text': '',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': '',
        'placeholder': '',
        'input_type': 'text',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': 'c9f1ec93-2ecc-477c-8a2f-f8c170b7a05a',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'or_impact_likely': {
        'id': 371,
        'name': 'or_impact_likely',
        'text': 'Impact Likely for Oregon',
        'prefix': 'pii',
        'type_id': 0,
        'input_type': 'boolean',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': True,
        'uuid': '2203d24c-b5b4-48cb-811c-d27fac5ef09a',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': True,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'org_handle': {
        'id': 400,
        'name': 'org_handle',
        'text': 'Organization',
        'prefix': None,
        'type_id': 0,
        'input_type': 'select',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': True,
        'uuid': '3cff6aa4-b7a1-4f52-9109-69f75996edbd',
        'values': [
          {
            'value': 202,
            'label': 'resilient',
            'enabled': True,
            'properties': {
              'configuration_type': 'standard'
            },
            'uuid': None,
            'hidden': False,
            'default': False
          }
        ],
        'read_only': True,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'owner_id': {
        'id': 382,
        'name': 'owner_id',
        'text': 'Owner',
        'prefix': None,
        'type_id': 0,
        'input_type': 'select_owner',
        'hide_notification': False,
        'chosen': True,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': True,
        'uuid': '97d1d2a1-d25e-4279-9d29-7bc60fd321ce',
        'values': [
          {
            'value': 7,
            'label': 'Resilient Sysadmin (a@example.com)',
            'enabled': True,
            'properties': None,
            'uuid': '41be6245-bd72-46e3-bbd5-a156e9c35068',
            'hidden': False,
            'default': False
          },
          {
            'value': 16,
            'label': 'Resilient Sysadmin (b@example.com)',
            'enabled': True,
            'properties': None,
            'uuid': 'bebf9f38-061b-4008-948f-dfc709935212',
            'hidden': False,
            'default': False
          },
          {
            'value': 17,
            'label': 'Resilient Sysadmin (c@example.com)',
            'enabled': True,
            'properties': None,
            'uuid': '577ab0e9-4933-4458-b554-8f97a53ea91a',
            'hidden': False,
            'default': False
          },
          {
            'value': 23,
            'label': 'Resilient Sysadmin (d@example.com)',
            'enabled': True,
            'properties': None,
            'uuid': '841e054d-c338-4c5d-ae9f-004c6bbbcc45',
            'hidden': False,
            'default': False
          },
          {
            'value': 6,
            'label': 'Default Group',
            'enabled': True,
            'properties': None,
            'uuid': '6f52ab7d-cbca-41ad-ab43-6ee779fe066e',
            'hidden': False,
            'default': False
          },
          {
            'value': 43,
            'label': 'fn_aws_guardduty',
            'enabled': True,
            'properties': None,
            'uuid': 'dc3bc875-9711-4d0a-a031-95111ec52695',
            'hidden': False,
            'default': False
          },
          {
            'value': 34,
            'label': 'IBM SOAR LDAP Utilities',
            'enabled': True,
            'properties': None,
            'uuid': 'a8785ad4-77b0-41d6-88e3-da2f5b492cf3',
            'hidden': False,
            'default': False
          },
          {
            'value': 41,
            'label': 'Netskope App for IBM SOAR',
            'enabled': True,
            'properties': None,
            'uuid': 'df057dc2-cbb8-4e08-95ec-0034e8a9d0c2',
            'hidden': False,
            'default': False
          },
          {
            'value': 37,
            'label': 'Microsoft Defender',
            'enabled': True,
            'properties': None,
            'uuid': 'ac251c59-57a9-4f25-8fe5-efdb82c7208e',
            'hidden': False,
            'default': False
          },
          {
            'value': 21,
            'label': 'Chronicle App for IBM SOAR',
            'enabled': True,
            'properties': None,
            'uuid': 'a76b3fda-dfaa-4d81-a298-4b5ca419be8f',
            'hidden': False,
            'default': False
          },
          {
            'value': 27,
            'label': 'Outbound Email',
            'enabled': True,
            'properties': None,
            'uuid': '1df6e58b-22ae-4b99-8cb3-9b422f00b24b',
            'hidden': False,
            'default': False
          },
          {
            'value': 32,
            'label': 'QRadar Enhanced Data Migration',
            'enabled': True,
            'properties': None,
            'uuid': 'c2a1268a-3175-4af0-8b30-ece93ffd29af',
            'hidden': False,
            'default': False
          },
          {
            'value': 48,
            'label': 'low_code',
            'enabled': True,
            'properties': None,
            'uuid': '7a0fb813-5d28-4b95-8764-fd867228b95f',
            'hidden': False,
            'default': False
          },
          {
            'value': 29,
            'label': 'VirusTotal',
            'enabled': True,
            'properties': None,
            'uuid': 'fc3d48d0-17bc-40da-9ef8-abefbdc44ca7',
            'hidden': False,
            'default': False
          },
          {
            'value': 40,
            'label': 'fn_mimecast',
            'enabled': True,
            'properties': None,
            'uuid': 'f3d8a237-6ed9-4660-b23b-ed62191d1d0d',
            'hidden': False,
            'default': False
          },
          {
            'value': 47,
            'label': 'fn_whois_rdap',
            'enabled': True,
            'properties': None,
            'uuid': 'e1fa35c2-101f-4a75-84cd-c86abc3a08c0',
            'hidden': False,
            'default': False
          },
          {
            'value': 42,
            'label': 'Trend Micro Deep Security',
            'enabled': True,
            'properties': None,
            'uuid': 'c4b9bd8b-27c3-4ff9-b9d0-8f36f166aa68',
            'hidden': False,
            'default': False
          },
          {
            'value': 44,
            'label': 'ITS Inventory & IBM SOAR',
            'enabled': True,
            'properties': None,
            'uuid': 'eed41111-efc5-4f1b-aa4d-d19d40f7e4d7',
            'hidden': False,
            'default': False
          },
          {
            'value': 38,
            'label': 'fn_task_utils',
            'enabled': True,
            'properties': None,
            'uuid': 'cf1a0f3f-d487-4dc8-946b-4f0438b8df2e',
            'hidden': False,
            'default': False
          },
          {
            'value': 24,
            'label': 'pipeline test',
            'enabled': True,
            'properties': None,
            'uuid': 'b386c859-f97b-4f1e-a2ee-ffcc72de6697',
            'hidden': False,
            'default': False
          },
          {
            'value': 31,
            'label': 'Ansible for SOAR',
            'enabled': True,
            'properties': None,
            'uuid': 'c1ef9add-1181-43f9-a73b-4a8b0be87c44',
            'hidden': False,
            'default': False
          },
          {
            'value': 36,
            'label': 'Axonius',
            'enabled': True,
            'properties': None,
            'uuid': 'a666334f-0b94-4a5b-8b2a-abf40a00c93a',
            'hidden': False,
            'default': False
          },
          {
            'value': 33,
            'label': 'Scheduler',
            'enabled': True,
            'properties': None,
            'uuid': '2675c895-a233-4179-b383-84bb7d6a7669',
            'hidden': False,
            'default': False
          },
          {
            'value': 39,
            'label': 'Microsoft Sentinel',
            'enabled': True,
            'properties': None,
            'uuid': '4aed886e-95c8-4fb3-98f7-a7fc1296edaf',
            'hidden': False,
            'default': False
          },
          {
            'value': 0,
            'label': 'System User',
            'enabled': True,
            'properties': None,
            'uuid': 'd82191c4-8171-4110-91db-0c1aa3235a88',
            'hidden': False,
            'default': False
          },
          {
            'value': 26,
            'label': 'ODBC Functions for SOAR',
            'enabled': True,
            'properties': None,
            'uuid': '36a03cfc-f237-457a-8e0f-d2a8da1a34e5',
            'hidden': False,
            'default': False
          },
          {
            'value': 45,
            'label': 'Microsoft Teams',
            'enabled': True,
            'properties': None,
            'uuid': '4c742b35-252f-4df7-9278-ce29ced7cfc7',
            'hidden': False,
            'default': False
          },
          {
            'value': 8,
            'label': 'Microsoft Teams',
            'enabled': True,
            'properties': None,
            'uuid': '932e6235-f4dc-4e9b-b791-7c5d29524704',
            'hidden': False,
            'default': False
          },
          {
            'value': 9,
            'label': 'QRadar Integration',
            'enabled': True,
            'properties': None,
            'uuid': 'b4074d2b-32d8-4410-9bb5-2fe9630230f7',
            'hidden': False,
            'default': False
          },
          {
            'value': 20,
            'label': 'REST API Functions for SOAR',
            'enabled': True,
            'properties': None,
            'uuid': 'b96c09c6-001e-4bf2-ae73-d313f3cee4bc',
            'hidden': False,
            'default': False
          },
          {
            'value': 46,
            'label': 'fn_urlhaus',
            'enabled': True,
            'properties': None,
            'uuid': 'c89c1b95-c8a9-47e9-9434-702d1aef6846',
            'hidden': False,
            'default': False
          },
          {
            'value': 30,
            'label': 'Data Feeder ODBC Plugin for SOAR',
            'enabled': True,
            'properties': None,
            'uuid': '0f25e515-c89f-435c-be8a-b52c74e95f70',
            'hidden': False,
            'default': False
          },
          {
            'value': 28,
            'label': 'ODBC Functions for SOAR',
            'enabled': True,
            'properties': None,
            'uuid': '567467f9-f162-49d0-af95-70e02d51345d',
            'hidden': False,
            'default': False
          },
          {
            'value': 12,
            'label': 'Data Feeder for QRadar SOAR',
            'enabled': True,
            'properties': None,
            'uuid': 'c5f590c0-9316-48dc-a5f2-de0b009a8c21',
            'hidden': False,
            'default': False
          },
          {
            'value': 35,
            'label': 'fn_stix_shifter_wrapper',
            'enabled': True,
            'properties': None,
            'uuid': '9471345b-c9e3-460a-a76b-cd82edb16a68',
            'hidden': False,
            'default': False
          },
          {
            'value': 14,
            'label': 'bidirectional resilientfeed',
            'enabled': True,
            'properties': None,
            'uuid': '5e65575a-d3b2-4f43-9a88-e46fa80544d9',
            'hidden': False,
            'default': False
          },
          {
            'value': 18,
            'label': 'Parent/Child Relationships',
            'enabled': True,
            'properties': None,
            'uuid': 'e150eb93-7996-42d4-bbd2-590a69fba3be',
            'hidden': False,
            'default': False
          },
          {
            'value': 25,
            'label': 'CheckPoint Next Generation Firewalls',
            'enabled': True,
            'properties': None,
            'uuid': '5999f876-d487-44c9-9fd1-b9505894a197',
            'hidden': False,
            'default': False
          }
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': True,
        'allow_default_value': False
      },
      'phase_id': {
        'id': 340,
        'name': 'phase_id',
        'text': 'Phase',
        'prefix': None,
        'type_id': 0,
        'tooltip': 'The phase of the incident.',
        'input_type': 'select',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': True,
        'uuid': 'ea47a365-620d-4419-a767-f1b08f2685d7',
        'values': [
          {
            'value': 1008,
            'label': 'Initial',
            'enabled': True,
            'properties': None,
            'uuid': '5558dfa9-3c70-498b-aa39-c1538c1ae671',
            'hidden': False,
            'default': False
          },
          {
            'value': 1009,
            'label': 'Engage',
            'enabled': True,
            'properties': None,
            'uuid': 'ed053e3a-2d6d-47e1-8240-844ed93d4893',
            'hidden': False,
            'default': False
          },
          {
            'value': 1010,
            'label': 'Detect/Analyze',
            'enabled': True,
            'properties': None,
            'uuid': '44868c86-246e-4e6e-8636-fa2848b2f279',
            'hidden': False,
            'default': False
          },
          {
            'value': 1007,
            'label': 'Respond',
            'enabled': True,
            'properties': None,
            'uuid': 'ebad851d-5b5e-4d19-af79-fae53cc1f659',
            'hidden': False,
            'default': False
          },
          {
            'value': 1012,
            'label': 'Post-Incident',
            'enabled': True,
            'properties': None,
            'uuid': '280a7bbe-3d93-4191-973f-2723b282a7e0',
            'hidden': False,
            'default': False
          },
          {
            'value': 1013,
            'label': 'Custom',
            'enabled': True,
            'properties': None,
            'uuid': '247d4b79-1762-4d70-bb95-67d83b104eff',
            'hidden': False,
            'default': False
          },
          {
            'value': 1011,
            'label': 'Complete',
            'enabled': True,
            'properties': None,
            'uuid': 'd057ec97-587e-44c0-ae84-c4fadd6d7e40',
            'hidden': False,
            'default': False
          }
        ],
        'read_only': True,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': True,
        'allow_default_value': False
      },
      'pipeda_other_factors': {
        'id': 347,
        'name': 'pipeda_other_factors',
        'text': 'PIPEDA Other Factors',
        'prefix': 'regulator_risk',
        'type_id': 0,
        'input_type': 'select',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': True,
        'internal': True,
        'uuid': 'd74446c8-2c14-4302-a3e0-694b43440f5b',
        'values': [
          {
            'value': 0,
            'label': 'NO',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1,
            'label': 'YES',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          }
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'pipeda_other_factors_comment': {
        'id': 346,
        'name': 'pipeda_other_factors_comment',
        'text': 'PIPEDA Other Factors Comment',
        'prefix': 'regulator_risk',
        'type_id': 0,
        'input_type': 'textarea',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': True,
        'internal': True,
        'uuid': '4b493998-e1a3-447c-aa74-d3fa8b0bcfe3',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'pipeda_overall_assessment': {
        'id': 349,
        'name': 'pipeda_overall_assessment',
        'text': 'PIPEDA Overall Assessment',
        'prefix': 'regulator_risk',
        'type_id': 0,
        'input_type': 'select',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': True,
        'internal': True,
        'uuid': 'f3121d96-903a-4e4f-8d44-ccab00e9081f',
        'values': [
          {
            'value': 0,
            'label': 'NO',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1,
            'label': 'YES',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          }
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'pipeda_overall_assessment_comment': {
        'id': 348,
        'name': 'pipeda_overall_assessment_comment',
        'text': 'PIPEDA Overall Assessment Comment',
        'prefix': 'regulator_risk',
        'type_id': 0,
        'input_type': 'textarea',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': True,
        'internal': True,
        'uuid': '69fca6b3-c00c-496a-a333-123513ef89e6',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'pipeda_probability_of_misuse': {
        'id': 345,
        'name': 'pipeda_probability_of_misuse',
        'text': 'PIPEDA Probability of Misuse',
        'prefix': 'regulator_risk',
        'type_id': 0,
        'input_type': 'select',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': True,
        'internal': True,
        'uuid': 'fdefcc18-b394-4550-a713-ab744ef4419a',
        'values': [
          {
            'value': 0,
            'label': 'NO',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1,
            'label': 'YES',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          }
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'pipeda_probability_of_misuse_comment': {
        'id': 344,
        'name': 'pipeda_probability_of_misuse_comment',
        'text': 'PIPEDA Probability of Misuse Comment',
        'prefix': 'regulator_risk',
        'type_id': 0,
        'input_type': 'textarea',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': True,
        'internal': True,
        'uuid': 'b49e6381-2a11-473e-ac9c-c798805cf039',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'pipeda_sensitivity_of_pi': {
        'id': 343,
        'name': 'pipeda_sensitivity_of_pi',
        'text': 'PIPEDA Sensitivity of PI',
        'prefix': 'regulator_risk',
        'type_id': 0,
        'input_type': 'select',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': True,
        'internal': True,
        'uuid': 'e6185fbe-85a6-4485-bca9-a36866b77df0',
        'values': [
          {
            'value': 0,
            'label': 'NO',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1,
            'label': 'YES',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          }
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'pipeda_sensitivity_of_pi_comment': {
        'id': 342,
        'name': 'pipeda_sensitivity_of_pi_comment',
        'text': 'PIPEDA Sensitivity of PI Comment',
        'prefix': 'regulator_risk',
        'type_id': 0,
        'input_type': 'textarea',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': True,
        'internal': True,
        'uuid': '65beb4ea-420e-40e3-b43a-37dee8c1675d',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'plan_status': {
        'id': 332,
        'name': 'plan_status',
        'text': 'Status',
        'prefix': None,
        'type_id': 0,
        'input_type': 'select',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': True,
        'uuid': '2df00085-f5f2-4289-844b-6ea014f77ac3',
        'values': [
          {
            'value': 'A',
            'label': 'Active',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 'C',
            'label': 'Closed',
            'enabled': True,
            'properties': None,
            'uuid': None,
            'hidden': False,
            'default': False
          }
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'qr_assigned': {
        'id': 1577,
        'name': 'qr_assigned',
        'text': 'QR Assigned',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': 'The analyst to whom the QRadar Offense is assigned to.',
        'placeholder': '',
        'input_type': 'textarea',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': 'cee826b5-5bab-44ba-a177-3458d25199aa',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': True,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'qr_credibility': {
        'id': 1579,
        'name': 'qr_credibility',
        'text': 'QR Credibility',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': 'Indicates the integrity of the offense as determined by the credibility rating that is configured in the log source.',
        'placeholder': '',
        'input_type': 'textarea',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': 'ea93f610-b018-413e-8ffd-24a710172490',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': True,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'qr_destination_ip_count': {
        'id': 1586,
        'name': 'qr_destination_ip_count',
        'text': 'QR Destination IP Count',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': 'The no. of Destination IPs associated with the QRadar Offense',
        'placeholder': '',
        'input_type': 'textarea',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': '5be7494c-2776-4df1-8d20-fa994ab11d93',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': True,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'qr_event_count': {
        'id': 1585,
        'name': 'qr_event_count',
        'text': 'QR Event Count',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': 'The no. of events associated with the QRadar Offense',
        'placeholder': '',
        'input_type': 'textarea',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': '4f7dfb5c-f38d-471b-b7a7-203e5d5790d9',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': True,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'qr_flow_count': {
        'id': 1575,
        'name': 'qr_flow_count',
        'text': 'QR Flow Count',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': 'The no. of flows associated with the QRadar Offense',
        'placeholder': '',
        'input_type': 'textarea',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': '9bd3220a-33f8-4edc-b007-670cc3aaf59f',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': True,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'qr_last_updated_time': {
        'id': 1584,
        'name': 'qr_last_updated_time',
        'text': 'QR Incident Last Updated Time',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': '',
        'placeholder': '',
        'input_type': 'datetimepicker',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': '39b1941a-8e62-4c19-a595-c7ab4ec4ec5f',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'qr_magnitude': {
        'id': 1588,
        'name': 'qr_magnitude',
        'text': 'QR Magnitude',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': 'Indicates the relative importance of the offense. This value is calculated based on the relevance, severity, and credibility ratings.',
        'placeholder': '',
        'input_type': 'textarea',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': '73b97697-3400-4bcc-be42-52020a0362a2',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': True,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'qr_offense_domain': {
        'id': 1361,
        'name': 'qr_offense_domain',
        'text': 'QR Offense Domain',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': '',
        'placeholder': '',
        'input_type': 'text',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': '568fa360-983f-463d-af2d-01bd8c7a0e25',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'qr_offense_index_type': {
        'id': 1576,
        'name': 'qr_offense_index_type',
        'text': 'QR Offense Index Type',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': 'The type on which the QRadar Offense is indexed',
        'placeholder': '',
        'input_type': 'text',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': 'c34fdc0c-b8e4-4ac8-b149-20f0f30cba01',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'qr_offense_index_value': {
        'id': 1581,
        'name': 'qr_offense_index_value',
        'text': 'QR Offense Index Value',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': 'The value by which QRadar Offense is indexed',
        'placeholder': '',
        'input_type': 'text',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': 'f4354ca9-d038-45a5-a91f-b4beaf3f5f18',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'qr_offense_last_updated_time': {
        'id': 1574,
        'name': 'qr_offense_last_updated_time',
        'text': 'QR Offense Last Updated Time',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': '',
        'placeholder': '',
        'input_type': 'datetimepicker',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': '8e612fca-fa1e-448d-9ecd-541ccb158573',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'qr_offense_source': {
        'id': 1587,
        'name': 'qr_offense_source',
        'text': 'QR Offense Source ',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': 'The source for the QRadar Offense',
        'placeholder': '',
        'input_type': 'text',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': '6af22a10-7581-4faf-afc8-c46fb68057f1',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'qr_offense_start_time': {
        'id': 1582,
        'name': 'qr_offense_start_time',
        'text': 'QR Offense Start Time',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': '',
        'placeholder': '',
        'input_type': 'datetimepicker',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': '11e94c0e-62d5-4ef9-8b5d-7073f487b606',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'qr_offense_status': {
        'id': 1573,
        'name': 'qr_offense_status',
        'text': 'QR Offense Status',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': '',
        'placeholder': '',
        'input_type': 'text',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': '8632d157-312f-49b7-9526-220077ef6131',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'qr_relevance': {
        'id': 1580,
        'name': 'qr_relevance',
        'text': 'QR Relevance',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': 'Indicates the importance of the destination. QRadar determines the relevance by the weight that the administrator assigned to the networks and assets.',
        'placeholder': '',
        'input_type': 'textarea',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': 'ef2b94ed-84b9-4388-9e7b-7cafedf6ea4e',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': True,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'qr_severity': {
        'id': 1583,
        'name': 'qr_severity',
        'text': 'QR Severity',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': 'Indicates the threat that an attack poses in relation to how prepared the destination is for the attack.',
        'placeholder': '',
        'input_type': 'textarea',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': '3659f126-c8df-47cb-bcdb-4dcbab3dbd84',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': True,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'qr_source_ip_count': {
        'id': 1578,
        'name': 'qr_source_ip_count',
        'text': 'QR Source IP Count',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': 'The no. of Source IPs associated with the QRadar Offense',
        'placeholder': '',
        'input_type': 'textarea',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': 'd9536f5a-3692-466b-b4c8-1045799d19ba',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': True,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'qradar_destination': {
        'id': 679,
        'name': 'qradar_destination',
        'text': 'QRadar Destination',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': 'QRadar Destination to Sync With',
        'placeholder': '',
        'input_type': 'text',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': '3b119adb-7585-44b6-b578-7c5d5ee6958d',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'qradar_id': {
        'id': 678,
        'name': 'qradar_id',
        'text': 'QR Offense Id',
        'short_text': '',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': '',
        'placeholder': '',
        'input_type': 'text',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': 'aedb7df6-642a-4438-824d-fe24be34cfc0',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'relations_level': {
        'id': 1092,
        'name': 'relations_level',
        'text': 'Relation Level',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': 'Is this incident considered a Parent or Child incident?',
        'placeholder': '',
        'input_type': 'select',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': 'b9fb9107-3a78-41ef-bf5b-cf15715e2a20',
        'values': [
          {
            'value': 162,
            'label': 'None',
            'enabled': True,
            'properties': None,
            'uuid': 'bbbab623-a925-4748-a18a-b62e3094efea',
            'hidden': False,
            'default': True
          },
          {
            'value': 163,
            'label': 'Parent',
            'enabled': True,
            'properties': None,
            'uuid': '4164bab9-49d5-4fda-8581-2da1185e1f1c',
            'hidden': False,
            'default': False
          },
          {
            'value': 164,
            'label': 'Child',
            'enabled': True,
            'properties': None,
            'uuid': '5c7c5a82-f105-4551-9c7e-e39a781fc051',
            'hidden': False,
            'default': False
          }
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'relations_parent_id': {
        'id': 1091,
        'name': 'relations_parent_id',
        'text': 'Parent ID',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': 'Incident Number of the Parent Incident',
        'placeholder': '',
        'input_type': 'textarea',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': 'b7a5848c-0aee-46ca-8c26-7610c95b0f43',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': True,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'reporter': {
        'id': 331,
        'name': 'reporter',
        'text': 'Reporting Individual',
        'prefix': None,
        'type_id': 0,
        'tooltip': 'Name of person who reported the event, such as a device owner or his/her manager',
        'placeholder': 'Employee name',
        'input_type': 'text',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': True,
        'uuid': '931afc2e-e09d-48e1-8b71-c1cc50e1eba6',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'resolution_id': {
        'id': 387,
        'name': 'resolution_id',
        'text': 'Resolution',
        'short_text': '',
        'prefix': None,
        'type_id': 0,
        'tooltip': 'Select an option that accurately describes the reason for closing this incident.',
        'placeholder': '',
        'input_type': 'select',
        'required': 'close',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': True,
        'internal': True,
        'uuid': '4f9589d1-4828-4841-951e-16179198c518',
        'values': [
          {
            'value': 58,
            'label': 'Unresolved',
            'enabled': True,
            'properties': None,
            'uuid': '9b7e136e-c79a-4481-9a93-175ce36d9778',
            'hidden': False,
            'default': False
          },
          {
            'value': 59,
            'label': 'Duplicate',
            'enabled': True,
            'properties': None,
            'uuid': '5cf3ca21-0afe-40e3-9198-ba88ed7d26da',
            'hidden': False,
            'default': False
          },
          {
            'value': 60,
            'label': 'Not an Issue',
            'enabled': True,
            'properties': None,
            'uuid': 'e81e412c-96f7-4223-815c-64d1310c8bb7',
            'hidden': False,
            'default': False
          },
          {
            'value': 61,
            'label': 'Resolved',
            'enabled': True,
            'properties': None,
            'uuid': '86ba01c3-aad7-4363-b170-085b7cbf8bc0',
            'hidden': False,
            'default': False
          },
          {
            'value': 279,
            'label': 'RESILIENT - closed in Qradar',
            'enabled': True,
            'properties': None,
            'uuid': '4d117c5d-fcdc-4cb0-8b5b-53670426df5f',
            'hidden': False,
            'default': False
          }
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'resolution_summary': {
        'id': 388,
        'name': 'resolution_summary',
        'text': 'Resolution Summary',
        'prefix': None,
        'type_id': 0,
        'tooltip': 'Enter a summary that describes how this incident was resolved.',
        'input_type': 'textarea',
        'required': 'close',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': True,
        'uuid': 'f5d18473-03f6-4149-b0d9-1ce9006b4a99',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': True,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'score': {
        'id': 395,
        'name': 'score',
        'text': 'Automated Severity',
        'prefix': None,
        'type_id': 0,
        'tooltip': 'The automated assessment of the case.',
        'input_type': 'select',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': True,
        'internal': True,
        'uuid': '1f6014a3-9d3b-492d-8b71-d400873bc0ed',
        'values': [
          {
            'value': 62,
            'label': 'Benign',
            'enabled': True,
            'properties': None,
            'uuid': '2f41036a-dfda-4aaa-a282-b6f40996868b',
            'hidden': False,
            'default': False
          },
          {
            'value': 63,
            'label': 'Low',
            'enabled': True,
            'properties': None,
            'uuid': '325101ff-e2bc-487e-b11f-751b114ef01a',
            'hidden': False,
            'default': False
          },
          {
            'value': 64,
            'label': 'Medium',
            'enabled': True,
            'properties': None,
            'uuid': 'a7a7b191-7645-4882-a5c7-0f1d3e81d133',
            'hidden': False,
            'default': False
          },
          {
            'value': 65,
            'label': 'High',
            'enabled': True,
            'properties': None,
            'uuid': '5aabdfc9-9f8a-465f-8e3b-c55cc3757428',
            'hidden': False,
            'default': False
          },
          {
            'value': 66,
            'label': 'Critical',
            'enabled': True,
            'properties': None,
            'uuid': '4701a687-7c39-42fe-9e5a-4008c67596d7',
            'hidden': False,
            'default': False
          }
        ],
        'read_only': True,
        'changeable': False,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'sentinel_incident_assigned_to': {
        'id': 2095,
        'name': 'sentinel_incident_assigned_to',
        'text': 'Sentinel Incident Assigned To',
        'short_text': '',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': '',
        'placeholder': '',
        'input_type': 'text',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': 'c34e6ac7-cdcf-4de3-a1ad-e472928b0a66',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'sentinel_incident_classification': {
        'id': 2096,
        'name': 'sentinel_incident_classification',
        'text': 'Sentinel Incident Classification',
        'short_text': '',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': '',
        'placeholder': '',
        'input_type': 'text',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': 'e06a30d5-3015-4f8c-844c-8d37d409126a',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'sentinel_incident_classification_comment': {
        'id': 2094,
        'name': 'sentinel_incident_classification_comment',
        'text': 'Sentinel Incident Classification Comment',
        'short_text': '',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': '',
        'placeholder': '',
        'input_type': 'text',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': 'aa039b8d-bd8d-4ba3-ad18-863a5e37fc0b',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'sentinel_incident_classification_reason': {
        'id': 2098,
        'name': 'sentinel_incident_classification_reason',
        'text': 'Sentinel Incident Classification Reason',
        'short_text': '',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': '',
        'placeholder': '',
        'input_type': 'text',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': 'f8ff2574-1cfd-4af5-8d8f-f7126c7dc78e',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'sentinel_incident_id': {
        'id': 2100,
        'name': 'sentinel_incident_id',
        'text': 'Sentinel Incident ID',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': '',
        'placeholder': '',
        'input_type': 'text',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': '1bae2697-feb5-48a8-8792-e2a0698adebb',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'sentinel_incident_labels': {
        'id': 2105,
        'name': 'sentinel_incident_labels',
        'text': 'Sentinel Incident Labels',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': '',
        'placeholder': '',
        'input_type': 'text',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': '7c63205c-6dab-40e4-8924-028f00b21c27',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'sentinel_incident_number': {
        'id': 2099,
        'name': 'sentinel_incident_number',
        'text': 'Sentinel Incident Number',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': '',
        'placeholder': '',
        'input_type': 'text',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': 'f9f36a0d-7bec-4383-ab72-40283116c104',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'sentinel_incident_status': {
        'id': 2097,
        'name': 'sentinel_incident_status',
        'text': 'Sentinel Incident Status',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': '',
        'placeholder': '',
        'input_type': 'text',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': 'e6710b80-81bb-49ba-a121-7a33488f6046',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'sentinel_incident_tactics': {
        'id': 2101,
        'name': 'sentinel_incident_tactics',
        'text': 'Sentinel Incident Tactics',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': '',
        'placeholder': '',
        'input_type': 'text',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': '2d748cf6-d484-47c5-8074-4092cd551540',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'sentinel_incident_url': {
        'id': 2103,
        'name': 'sentinel_incident_url',
        'text': 'Sentinel Incident URL',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': '',
        'placeholder': '',
        'input_type': 'textarea',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': '353dbf6a-b077-4813-8660-5313c801c903',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': True,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'sentinel_label': {
        'id': 2104,
        'name': 'sentinel_label',
        'text': 'Sentinel Server Label',
        'short_text': '',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': 'Label give to the Sentinel server in the app.config. Example in app.config [fn_microsoft_sentinel:label1] the label here is label1.',
        'placeholder': '',
        'input_type': 'text',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': '41451b48-082f-414d-80f5-50c61053bfea',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'sentinel_profile': {
        'id': 2102,
        'name': 'sentinel_profile',
        'text': 'Sentinel Profile',
        'short_text': '',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': '',
        'placeholder': '',
        'input_type': 'text',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': '2fa680d9-d625-48bf-973f-48834d5ea47b',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'sequence_code': {
        'id': 401,
        'name': 'sequence_code',
        'text': 'Sequence Code',
        'prefix': None,
        'type_id': 0,
        'tooltip': 'The Unique Incident Sequence Code.',
        'input_type': 'text',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': True,
        'uuid': '7662e73c-9e92-11e9-bd1f-2745873db71d',
        'values': [
          
        ],
        'read_only': True,
        'changeable': False,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'severity_code': {
        'id': 386,
        'name': 'severity_code',
        'text': 'Severity',
        'prefix': None,
        'type_id': 0,
        'tooltip': 'Your impression of the events relative severity vs. other events that may be entered into the system.',
        'input_type': 'select',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': True,
        'uuid': '153e9e55-d7ba-43b8-8894-e3340935ba99',
        'values': [
          {
            'value': 55,
            'label': 'Low',
            'enabled': True,
            'properties': None,
            'uuid': '97cae239-963d-4e36-be34-07e47ef2cc86',
            'hidden': False,
            'default': True
          },
          {
            'value': 56,
            'label': 'Medium',
            'enabled': True,
            'properties': None,
            'uuid': 'c2c354c9-6d1e-4a48-82e5-bd5dc5068339',
            'hidden': False,
            'default': False
          },
          {
            'value': 57,
            'label': 'High',
            'enabled': True,
            'properties': None,
            'uuid': '93e5c99c-563b-48b9-80a3-9572307622d8',
            'hidden': False,
            'default': False
          }
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': True,
        'allow_default_value': False
      },
      'singapore_risk_assessment': {
        'id': 364,
        'name': 'singapore_risk_assessment',
        'text': 'Singapore Risk Assessment',
        'prefix': 'pii',
        'type_id': 0,
        'input_type': 'boolean',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': True,
        'uuid': 'ea1802d6-008b-4b88-a7d6-fb1fbbd3f839',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': True,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'start_date': {
        'id': 385,
        'name': 'start_date',
        'text': 'Date Occurred',
        'prefix': None,
        'type_id': 0,
        'tooltip': 'Date the incident occurred',
        'input_type': 'datetimepicker',
        'hide_notification': True,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': True,
        'uuid': '90f5a419-e126-48db-888c-80fe09444cfe',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'state': {
        'id': 325,
        'name': 'state',
        'text': 'State',
        'prefix': None,
        'type_id': 0,
        'input_type': 'select',
        'hide_notification': True,
        'chosen': True,
        'default_chosen_by_server': False,
        'blank_option': True,
        'internal': True,
        'uuid': '37a7f680-9ea3-4703-8e86-3846ef14397f',
        'values': [
          {
            'value': 1,
            'label': 'Alabama',
            'enabled': True,
            'properties': {
              'country': 1000,
              'type': 1
            },
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 2,
            'label': 'Alaska',
            'enabled': True,
            'properties': {
              'country': 1000,
              'type': 1
            },
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1003,
            'label': 'Alberta',
            'enabled': True,
            'properties': {
              'country': 1001,
              'type': 2
            },
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 4,
            'label': 'Arizona',
            'enabled': True,
            'properties': {
              'country': 1000,
              'type': 1
            },
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 5,
            'label': 'Arkansas',
            'enabled': True,
            'properties': {
              'country': 1000,
              'type': 1
            },
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1010,
            'label': 'British Columbia',
            'enabled': True,
            'properties': {
              'country': 1001,
              'type': 2
            },
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 6,
            'label': 'California',
            'enabled': True,
            'properties': {
              'country': 1000,
              'type': 1
            },
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 7,
            'label': 'Colorado',
            'enabled': True,
            'properties': {
              'country': 1000,
              'type': 1
            },
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 8,
            'label': 'Connecticut',
            'enabled': True,
            'properties': {
              'country': 1000,
              'type': 1
            },
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 9,
            'label': 'Delaware',
            'enabled': True,
            'properties': {
              'country': 1000,
              'type': 1
            },
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 10,
            'label': 'District of Columbia',
            'enabled': True,
            'properties': {
              'country': 1000,
              'type': 1
            },
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 12,
            'label': 'Florida',
            'enabled': True,
            'properties': {
              'country': 1000,
              'type': 1
            },
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 13,
            'label': 'Georgia',
            'enabled': True,
            'properties': {
              'country': 1000,
              'type': 1
            },
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1106,
            'label': 'Guam',
            'enabled': True,
            'properties': {
              'country': 1000,
              'type': 1
            },
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 15,
            'label': 'Hawaii',
            'enabled': True,
            'properties': {
              'country': 1000,
              'type': 1
            },
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 16,
            'label': 'Idaho',
            'enabled': True,
            'properties': {
              'country': 1000,
              'type': 1
            },
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 17,
            'label': 'Illinois',
            'enabled': True,
            'properties': {
              'country': 1000,
              'type': 1
            },
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 18,
            'label': 'Indiana',
            'enabled': True,
            'properties': {
              'country': 1000,
              'type': 1
            },
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 19,
            'label': 'Iowa',
            'enabled': True,
            'properties': {
              'country': 1000,
              'type': 1
            },
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 20,
            'label': 'Kansas',
            'enabled': True,
            'properties': {
              'country': 1000,
              'type': 1
            },
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 21,
            'label': 'Kentucky',
            'enabled': True,
            'properties': {
              'country': 1000,
              'type': 1
            },
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 22,
            'label': 'Louisiana',
            'enabled': True,
            'properties': {
              'country': 1000,
              'type': 1
            },
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 23,
            'label': 'Maine',
            'enabled': True,
            'properties': {
              'country': 1000,
              'type': 1
            },
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1007,
            'label': 'Manitoba',
            'enabled': True,
            'properties': {
              'country': 1001,
              'type': 2
            },
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 25,
            'label': 'Maryland',
            'enabled': True,
            'properties': {
              'country': 1000,
              'type': 1
            },
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 26,
            'label': 'Massachusetts',
            'enabled': True,
            'properties': {
              'country': 1000,
              'type': 1
            },
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 27,
            'label': 'Michigan',
            'enabled': True,
            'properties': {
              'country': 1000,
              'type': 1
            },
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 28,
            'label': 'Minnesota',
            'enabled': True,
            'properties': {
              'country': 1000,
              'type': 1
            },
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 29,
            'label': 'Mississippi',
            'enabled': True,
            'properties': {
              'country': 1000,
              'type': 1
            },
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 30,
            'label': 'Missouri',
            'enabled': True,
            'properties': {
              'country': 1000,
              'type': 1
            },
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 31,
            'label': 'Montana',
            'enabled': True,
            'properties': {
              'country': 1000,
              'type': 1
            },
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 32,
            'label': 'Nebraska',
            'enabled': True,
            'properties': {
              'country': 1000,
              'type': 1
            },
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 33,
            'label': 'Nevada',
            'enabled': True,
            'properties': {
              'country': 1000,
              'type': 1
            },
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1004,
            'label': 'New Brunswick',
            'enabled': True,
            'properties': {
              'country': 1001,
              'type': 2
            },
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1005,
            'label': 'Newfoundland and Labrador',
            'enabled': True,
            'properties': {
              'country': 1001,
              'type': 2
            },
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 34,
            'label': 'New Hampshire',
            'enabled': True,
            'properties': {
              'country': 1000,
              'type': 1
            },
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 35,
            'label': 'New Jersey',
            'enabled': True,
            'properties': {
              'country': 1000,
              'type': 1
            },
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 36,
            'label': 'New Mexico',
            'enabled': True,
            'properties': {
              'country': 1000,
              'type': 1
            },
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 37,
            'label': 'New York',
            'enabled': True,
            'properties': {
              'country': 1000,
              'type': 1
            },
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 38,
            'label': 'North Carolina',
            'enabled': True,
            'properties': {
              'country': 1000,
              'type': 1
            },
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 39,
            'label': 'North Dakota',
            'enabled': True,
            'properties': {
              'country': 1000,
              'type': 1
            },
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1176,
            'label': 'Northern Mariana Islands',
            'enabled': True,
            'properties': {
              'country': 1000,
              'type': 1
            },
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1014,
            'label': 'Northwest Territories',
            'enabled': True,
            'properties': {
              'country': 1001,
              'type': 2
            },
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1009,
            'label': 'Nova Scotia',
            'enabled': True,
            'properties': {
              'country': 1001,
              'type': 2
            },
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1015,
            'label': 'Nunavut',
            'enabled': True,
            'properties': {
              'country': 1001,
              'type': 2
            },
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 41,
            'label': 'Ohio',
            'enabled': True,
            'properties': {
              'country': 1000,
              'type': 1
            },
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 42,
            'label': 'Oklahoma',
            'enabled': True,
            'properties': {
              'country': 1000,
              'type': 1
            },
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1006,
            'label': 'Ontario',
            'enabled': True,
            'properties': {
              'country': 1001,
              'type': 2
            },
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 43,
            'label': 'Oregon',
            'enabled': True,
            'properties': {
              'country': 1000,
              'type': 1
            },
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 45,
            'label': 'Pennsylvania',
            'enabled': True,
            'properties': {
              'country': 1000,
              'type': 1
            },
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1011,
            'label': 'Prince Edward Island',
            'enabled': True,
            'properties': {
              'country': 1001,
              'type': 2
            },
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 77,
            'label': 'Puerto Rico',
            'enabled': True,
            'properties': {
              'country': 1000,
              'type': 1
            },
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1008,
            'label': 'Quebec',
            'enabled': True,
            'properties': {
              'country': 1001,
              'type': 2
            },
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 47,
            'label': 'Rhode Island',
            'enabled': True,
            'properties': {
              'country': 1000,
              'type': 1
            },
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1012,
            'label': 'Saskatchewan',
            'enabled': True,
            'properties': {
              'country': 1001,
              'type': 2
            },
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 48,
            'label': 'South Carolina',
            'enabled': True,
            'properties': {
              'country': 1000,
              'type': 1
            },
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 49,
            'label': 'South Dakota',
            'enabled': True,
            'properties': {
              'country': 1000,
              'type': 1
            },
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 50,
            'label': 'Tennessee',
            'enabled': True,
            'properties': {
              'country': 1000,
              'type': 1
            },
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 51,
            'label': 'Texas',
            'enabled': True,
            'properties': {
              'country': 1000,
              'type': 1
            },
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 52,
            'label': 'Utah',
            'enabled': True,
            'properties': {
              'country': 1000,
              'type': 1
            },
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 53,
            'label': 'Vermont',
            'enabled': True,
            'properties': {
              'country': 1000,
              'type': 1
            },
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 55,
            'label': 'Virginia',
            'enabled': True,
            'properties': {
              'country': 1000,
              'type': 1
            },
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 54,
            'label': 'Virgin Islands',
            'enabled': True,
            'properties': {
              'country': 1000,
              'type': 1
            },
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 56,
            'label': 'Washington',
            'enabled': True,
            'properties': {
              'country': 1000,
              'type': 1
            },
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 57,
            'label': 'West Virginia',
            'enabled': True,
            'properties': {
              'country': 1000,
              'type': 1
            },
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 58,
            'label': 'Wisconsin',
            'enabled': True,
            'properties': {
              'country': 1000,
              'type': 1
            },
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 59,
            'label': 'Wyoming',
            'enabled': True,
            'properties': {
              'country': 1000,
              'type': 1
            },
            'uuid': None,
            'hidden': False,
            'default': False
          },
          {
            'value': 1013,
            'label': 'Yukon',
            'enabled': True,
            'properties': {
              'country': 1001,
              'type': 2
            },
            'uuid': None,
            'hidden': False,
            'default': False
          }
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'test_exclusion_list_field': {
        'id': 1560,
        'name': 'test_exclusion_list_field',
        'text': 'test_exclusion_list_field',
        'short_text': '',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': '',
        'placeholder': '',
        'input_type': 'text',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': '051501c2-a628-4d81-991b-9c009810afb2',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'tp_reporting_tag': {
        'id': 1572,
        'name': 'tp_reporting_tag',
        'text': 'tp_reporting_tag',
        'short_text': '',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': '',
        'placeholder': '',
        'input_type': 'text',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': '259b34c4-d7c4-490e-a8c9-671a20247ed4',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'traffic_type_netskope': {
        'id': 2280,
        'name': 'traffic_type_netskope',
        'text': 'Traffic Type (Netskope)',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': 'Type of the traffic',
        'placeholder': '',
        'input_type': 'text',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': '0be63fb7-2b35-419e-ac5c-20ef5f83fe5a',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'ts_bool': {
        'id': 2455,
        'name': 'ts_bool',
        'text': 'ts_bool',
        'short_text': '',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': '',
        'placeholder': '',
        'input_type': 'boolean',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': 'bf59e545-d8ad-4bd8-a381-8074b7e23fef',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': True,
        'allow_default_value': False
      },
      'ts_select': {
        'id': 2454,
        'name': 'ts_select',
        'text': 'ts_select',
        'short_text': '',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': '',
        'placeholder': '',
        'input_type': 'select',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': 'a2d46f12-a665-47ba-bb8d-0d02420cec8a',
        'values': [
          {
            'value': 655,
            'label': 'select_a',
            'enabled': True,
            'properties': None,
            'uuid': 'a5c09b05-dac8-4285-bb0f-96359dfd8e75',
            'hidden': False,
            'default': True
          },
          {
            'value': 656,
            'label': 'select_b',
            'enabled': True,
            'properties': None,
            'uuid': '4266e32a-304e-4cec-a78d-5fe55cc8fc0a',
            'hidden': False,
            'default': False
          },
          {
            'value': 657,
            'label': 'select_c',
            'enabled': True,
            'properties': None,
            'uuid': '7812f09a-64bb-447e-9bf9-117948fce3b6',
            'hidden': False,
            'default': False
          }
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': True,
        'allow_default_value': False
      },
      'user_id_netskope': {
        'id': 2283,
        'name': 'user_id_netskope',
        'text': 'User ID (Netskope)',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': 'User email',
        'placeholder': '',
        'input_type': 'text',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': '23fb82ae-16e5-4262-8a9e-c173b3b45f9b',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'username_netskope': {
        'id': 2285,
        'name': 'username_netskope',
        'text': 'Username (Netskope)',
        'prefix': 'properties',
        'type_id': 0,
        'tooltip': 'Name of the user',
        'placeholder': '',
        'input_type': 'text',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': False,
        'uuid': '64961f6c-a0a0-4500-b497-197e718c7e29',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'wa_impact_likely': {
        'id': 372,
        'name': 'wa_impact_likely',
        'text': 'Impact Likely for Washington',
        'prefix': 'pii',
        'type_id': 0,
        'input_type': 'boolean',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': True,
        'uuid': '7808b829-23a1-4d99-987c-701602a05069',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': True,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'workspace': {
        'id': 330,
        'name': 'workspace',
        'text': 'Workspace',
        'prefix': None,
        'type_id': 0,
        'input_type': 'select',
        'required': 'always',
        'hide_notification': False,
        'chosen': False,
        'default_chosen_by_server': True,
        'blank_option': False,
        'internal': True,
        'uuid': 'eeab7544-25d3-4189-84fc-8988a6ab1abf',
        'values': [
          {
            'value': 2,
            'label': 'Default workspace',
            'enabled': True,
            'properties': None,
            'uuid': '47350579-3795-4d7f-907f-c2d1fd329816',
            'hidden': False,
            'default': True
          }
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      },
      'zip': {
        'id': 377,
        'name': 'zip',
        'text': 'Zip',
        'prefix': None,
        'type_id': 0,
        'input_type': 'text',
        'hide_notification': True,
        'chosen': False,
        'default_chosen_by_server': False,
        'blank_option': False,
        'internal': True,
        'uuid': 'e486619d-b212-43fd-bb1d-785f4cd312ce',
        'values': [
          
        ],
        'read_only': False,
        'changeable': True,
        'rich_text': False,
        'templates': [
          
        ],
        'deprecated': False,
        'calculated': False,
        'is_tracked': False,
        'allow_default_value': False
      }
    },
    'properties': {
      'can_create': True,
      'can_destroy': True,
      'for_who': [
        'added_members',
        'added_owners',
        'members',
        'owners',
        'removed_members',
        'removed_owners'
      ]
    },
    'parent_types': [
      
    ],
    'display_name': 'Incident',
    'for_notifications': True,
    'for_actions': True,
    'for_custom_fields': True,
    'for_workflows': True,
    'uuid': 'fcc6dabc-e465-4311-96e2-c143845d939a',
    'actions': [
      
    ],
    'playbooks': [
      
    ],
    'tags': [
      
    ]
  }
}

INCIDENT_PAYLOAD = {
    "artifacts": None,
    "cm": {
      "geo_counts": {},
      "total": 0,
      "unassigneds": []
    },
    "dtm": {},
    "hipaa": {
      "hipaa_acquired": None,
      "hipaa_acquired_comment": "",
      "hipaa_additional_misuse": None,
      "hipaa_additional_misuse_comment": "",
      "hipaa_adverse": None,
      "hipaa_adverse_comment": "",
      "hipaa_breach": None,
      "hipaa_breach_comment": "",
      "hipaa_misused": None,
      "hipaa_misused_comment": ""
    },
    "regulators": {
      "ids": [
        149
      ]
    },
    "tasks": None,
    "actions": [],
    "addr": None,
    "admin_id": None,
    "assessment": "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>\n<assessment>\n    <rollups/>\n    <optional>There are 1 required and 0 optional tasks from 1 regulators.</optional>\n</assessment>\n",
    "city": None,
    "comments": None,
    "confirmed": True,
    "country": None,
    "create_date": 1727377358285,
    "creator": {
      "display_name": "Resilient Sysadmin",
      "email": "a@example.com",
      "fname": "Resilient",
      "id": 7,
      "is_external": False,
      "is_ldap": False,
      "is_saml": False,
      "lname": "Sysadmin",
      "locked": False,
      "password_changed": False,
      "status": "A",
      "ui_theme": "verydarkmode"
    },
    "creator_id": 7,
    "creator_principal": {
      "display_name": "Resilient Sysadmin",
      "id": 7,
      "name": "a@example.com",
      "type": "user"
    },
    "crimestatus_id": 5,
    "data_compromised": None,
    "description": "<div class=\"soar-rte-content\"><p>some description here</p></div>",
    "discovered_date": 1727377339269,
    "draft": False,
    "due_date": None,
    "employee_involved": None,
    "end_date": None,
    "exposure": 0,
    "exposure_dept_id": None,
    "exposure_individual_name": None,
    "exposure_type_id": 1,
    "exposure_vendor_id": None,
    "gdpr": {
      "gdpr_breach_circumstances": [],
      "gdpr_breach_type": None,
      "gdpr_breach_type_comment": None,
      "gdpr_consequences": None,
      "gdpr_consequences_comment": None,
      "gdpr_final_assessment": None,
      "gdpr_final_assessment_comment": None,
      "gdpr_identification": None,
      "gdpr_identification_comment": None,
      "gdpr_personal_data": None,
      "gdpr_personal_data_comment": None,
      "gdpr_subsequent_notification": None
    },
    "hard_liability": 0,
    "id": 3074,
    "inc_last_modified_date": 1727459818001,
    "inc_start": None,
    "inc_training": False,
    "incident_type_ids": [],
    "is_scenario": False,
    "jurisdiction_name": None,
    "jurisdiction_reg_id": None,
    "members": [],
    "name": "test artifact_type",
    "negative_pr_likely": None,
    "nist_attack_vectors": [],
    "org_handle": 202,
    "org_id": 202,
    "owner_id": 7,
    "perms": None,
    "phase_id": 1007,
    "pii": {
      "alberta_health_risk_assessment": None,
      "assessment": "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>\n<assessment>\n    <rollups/>\n    <optional>There are 1 required and 0 optional tasks from 1 regulators.</optional>\n</assessment>\n",
      "california_health_risk_assessment": None,
      "data_compromised": None,
      "data_contained": None,
      "data_encrypted": None,
      "data_format": None,
      "data_source_ids": [],
      "dc_impact_likely": None,
      "determined_date": 1727377339269,
      "exposure": 0,
      "gdpr_harm_risk": None,
      "gdpr_lawful_data_processing_categories": [],
      "harmstatus_id": 2,
      "impact_likely": None,
      "new_zealand_risk_assessment": None,
      "ny_impact_likely": None,
      "or_impact_likely": None,
      "singapore_risk_assessment": None,
      "wa_impact_likely": None
    },
    "plan_status": "A",
    "playbooks": [],
    "properties": {
      "file_path": "/path/to/something",
      "df_create_date": None,
      "sentinel_incident_classification_reason": None,
      "high_volume_privacy_event": None,
      "defender_incident_lastupdatetime": None,
      "chronicle_collection_elements": None,
      "qr_offense_index_value": None,
      "aws_guardduty_resource_type": None,
      "user_id_netskope": None,
      "qradar_id": None,
      "chronicle_detection_created_time": None,
      "qr_offense_index_type": None,
      "chronicle_rule_type": None,
      "chronicle_ioc_last_seen_time": None,
      "defender_classification": None,
      "sentinel_incident_id": None,
      "qr_offense_domain": None,
      "chronicle_alert_username": None,
      "relations_level": None,
      "acknowledged_netskope": None,
      "defender_incident_createtime": None,
      "sentinel_incident_url": None,
      "sentinel_label": None,
      "qr_destination_ip_count": None,
      "qr_event_count": None,
      "qr_offense_status": None,
      "qradar_destination": None,
      "aws_guardduty_severity": None,
      "chronicle_alert_assetname": None,
      "email_message_id": None,
      "test_exclusion_list_field": "a,b,c",
      "chronicle_rule_name": None,
      "ts_select": 657,
      "sentinel_incident_tactics": None,
      "aws_guardduty_finding_arn": None,
      "application_netskope": None,
      "internal_customizations_field": None,
      "aws_guardduty_count": None,
      "qr_assigned": None,
      "df_host": None,
      "sentinel_incident_status": None,
      "tp_reporting_tag": "tag1",
      "alert_type_netskope": None,
      "ldap_domain_name": None,
      "sentinel_incident_classification": None,
      "defender_incident_id": None,
      "aws_guardduty_trigger_refresh": None,
      "df_inc_id": None,
      "custom_text": None,
      "qr_offense_last_updated_time": None,
      "sentinel_incident_labels": None,
      "qr_magnitude": None,
      "qr_flow_count": None,
      "relations_parent_id": None,
      "object_netskope": None,
      "qr_relevance": None,
      "chronicle_detection_time": None,
      "aws_guardduty_finding_id": None,
      "activity_netskope": None,
      "chronicle_detection_state": None,
      "defender_determination": None,
      "offense_type": None,
      "qr_offense_source": None,
      "aws_guardduty_detector_id": None,
      "ts_bool": True,
      "sentinel_incident_assigned_to": None,
      "sentinel_profile": None,
      "qr_offense_start_time": None,
      "aws_guardduty_archived": None,
      "chronicle_ioc_first_seen_time": None,
      "qr_last_updated_time": None,
      "offense_name": None,
      "aws_guardduty_region": None,
      "chronicle_detection_window_end_time": None,
      "ldap_base_dn": None,
      "action_netskope": None,
      "chronicle_detection_window_start_time": None,
      "alert_id_netskope": None,
      "sentinel_incident_number": None,
      "qr_credibility": None,
      "df_org_id": None,
      "username_netskope": None,
      "qr_source_ip_count": None,
      "chronicle_detection_type": None,
      "qr_severity": None,
      "object_type_netskope": None,
      "aws_guardduty_finding_updated_at": None,
      "sentinel_incident_classification_comment": None,
      "chronicle_ioc_ingest_time": None,
      "aws_guardduty_finding_type": None,
      "defender_tags": None,
      "chronicle_ioc_domain": None,
      "defender_incident_url": None,
      "traffic_type_netskope": None
    },
    "regulator_risk": {},
    "reporter": None,
    "resolution_id": None,
    "resolution_summary": None,
    "score": None,
    "sequence_code": None,
    "severity_code": 55,
    "start_date": None,
    "state": None,
    "task_changes": {
      "added": [],
      "removed": []
    },
    "timer_field_summarized_incident_data": [],
    "vers": 10,
    "workspace": 2,
    "zip": None,
    "time_series": {
      'timeseries__owner_id__resilient_sysadmin': 63679,
      'timeseries__phase_id__respond': 63679,
      'timeseries__severity_code__low': 63679,
      'timeseries__ts_bool__false': 34,
      'timeseries__ts_bool__true': 22,
      'timeseries__ts_select__select_a': 22,
      'timeseries__ts_select__select_b': 34
    }
}

class MockRESTAPI:
    def get(self, url):
        if "fields" in url:
          return list(TYPE_INFO_MAP["incident"]["fields"].values())
        if "types" in url:
          return TYPE_INFO_MAP["incident"]
    
mock_rest_api = MockRESTAPI()

TYPE_INFO = ActionMessageTypeInfo(0, TYPE_INFO_MAP, mock_rest_api)


class TestDataFeederSyncIncidents:
    """ Tests for the data_feeder_sync_incidents function"""

    @pytest.mark.parametrize("typeinfo, field, value, expected_result", [
        (None, {'input_type': 'text'}, None, None),
        (None, {'input_type': 'text'}, "abc", "abc"),
        (None, {'input_type': 'bool'}, False, False),
        (None, {'input_type': 'text'}, ["abc","def"], "abc, def"),
        (None, {'input_type': 'textarea'}, {"content": "abc"}, "abc"),
        (None, {'input_type': 'number'}, {"id": 5}, 5),
        (None, {'input_type': 'datepicker'}, 1607107208000, "2020-12-04T18:40:08+00:00"),
        (None, {'input_type': 'datetimepicker'}, 1607107208000, "2020-12-04T18:40:08+00:00")
    ])
    def test_success(self, typeinfo, field, value, expected_result):
        result_value = TypeInfo.translate_value(typeinfo, field, value)
        assert(result_value == expected_result)

    @pytest.mark.parametrize("flattened_incident, exclude_list, expected_result", [
        ({'inc_a':'a', 'inc_b':'b', 'inc_c':'c', 'xxx':'xxx'}, ['xxx', 'blah'], ['inc_a', 'inc_b', 'inc_c']),
        ({'inc_a1':'a', 'inc_b1':'b', 'inc_c1':'c', 'xxx1':'xxx'}, ['inc*', ''], ['xxx1']),
        ({'inc_a2':'a', 'inc_b2':'b', 'inc_c2':'c', 'xxx2':'xxx'}, ['inc_??'], ['xxx2']),
        ({'inc_a1':'a', 'inc_b1':'b', 'inc_c1':'c', 'xxx1':'xxx'}, ['inc_??', 'inc*', 'inc_c1'], ['xxx1']),
        ({'inc_a3':'a', 'inc_b3':'b', 'inc_c3':'c', 'xxx3':'xxx'}, [], ['inc_a3', 'inc_b3', 'inc_c3', 'xxx3']),
        ({'inc_a4':'a', 'inc_b4':'b', 'inc_c4':'c', 'xxx4':'xxx'}, None, ['inc_a4', 'inc_b4', 'inc_c4', 'xxx4']),
        ({'inc_a4':'a', 'inc_b4':'b', 'inc_c4':'c'}, ['inc*'], []),
        ({'inc_a4':'a', 'inc_b4':'b', 'inc_c4':'c'}, ['inc_a4', 'inc_b4', 'inc_c4'], []),
        ({'inc_a4':'a', 'inc_b4':'b', 'inc_c4':'c'}, ['inc_a4 ', ' inc_b4', 'INC_c4'], []),
        ({'inc_a':'a', 'inc_b':'b', 'inc_c':'c', 'xxx':'xxx'}, ['nomatch'], ['inc_a', 'inc_b', 'inc_c', 'xxx']),
        (None, None, []),
        ({'INC_A':'a', 'inc_b':'c', 'INC_C':'c'}, ['inc_a', 'INC_B'], ['inc_c']),
        ({}, ['something'], [])
    ])
    def test_exclude_incident_fields(self, flattened_incident, exclude_list, expected_result):
        t = TypeInfo("incident", None)
        actual_result = t.filter_incident_fields(flattened_incident, exclude_list)

        assert set(actual_result.keys()) == set(expected_result)

    def test_flatten(self):
        result = TYPE_INFO.flatten(INCIDENT_PAYLOAD, TypeInfo.translate_value)

        # get the list of all possible incident fields
        incident_fields = set(TYPE_INFO_MAP["incident"]["fields"].keys())
        payload_fields = set(result.keys())

        diff_set = incident_fields.difference(payload_fields)

        # should be no fields not indicated in the field schema
        assert not diff_set
