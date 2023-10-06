# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

from __future__ import print_function
import requests_mock
from pytest_resilient_circuits import BasicResilientMock, resilient_endpoint
import logging
LOG = logging.getLogger(__name__)

MOCK_TYPE_DEFS = {
  'addr': {
    'id': 277,
    'name': 'addr',
    'text': 'Address',
    'prefix': None,
    'type_id': 0,
    'tooltip': 'Physical location of the incident, if applicable',
    'input_type': 'text',
    'uuid': '9540d9b0-2cd9-4347-b013-a1c84b6605b7',
    'values': [
      
    ],
    'rich_text': False
  },
  'alberta_health_risk_assessment': {
    'id': 312,
    'name': 'alberta_health_risk_assessment',
    'text': 'Alberta Health Risk Assessment',
    'prefix': 'pii',
    'type_id': 0,
    'input_type': 'boolean',
    'uuid': '6dd01276-c322-4095-b33c-15d3b33c3540',
    'values': [
      
    ],
    'rich_text': False
  },
  'california_health_risk_assessment': {
    'id': 315,
    'name': 'california_health_risk_assessment',
    'text': 'California Health Risk Assessment',
    'prefix': 'pii',
    'type_id': 0,
    'input_type': 'boolean',
    'uuid': '35868ab2-564c-43e1-94bc-a3f5676bc25a',
    'values': [
      
    ],
    'rich_text': False
  },
  'city': {
    'id': 278,
    'name': 'city',
    'text': 'City',
    'prefix': None,
    'type_id': 0,
    'input_type': 'text',
    'uuid': '488c24db-25a1-4cda-91d1-3865d3639732',
    'values': [
      
    ],
    'rich_text': False
  },
  'confirmed': {
    'id': 285,
    'name': 'confirmed',
    'text': 'Incident Disposition',
    'prefix': None,
    'type_id': 0,
    'tooltip': 'Tag an issue as an unconfirmed (event) vs. a confirmed incident.',
    'input_type': 'boolean',
    'uuid': '9b531f7c-d112-4444-8a91-9ea2d5e47162',
    'values': [
      
    ],
    'label_False': 'Unconfirmed',
    'label_True': 'Confirmed',
    'rich_text': False
  },
  'country': {
    'id': 329,
    'name': 'country',
    'text': 'Country/Region',
    'prefix': None,
    'type_id': 0,
    'input_type': 'select',
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
    'rich_text': False
  },
  'create_date': {
    'id': 340,
    'name': 'create_date',
    'text': 'Date Created',
    'prefix': None,
    'type_id': 0,
    'tooltip': 'The date the incident was created. This field is read-only.',
    'input_type': 'datetimepicker',
    'uuid': 'b4faf728-881a-4e8b-bf0b-d39b720392a1',
    'values': [
      
    ],
    'rich_text': False
  },
  'creator_id': {
    'id': 342,
    'name': 'creator_id',
    'text': 'Created By',
    'prefix': None,
    'type_id': 0,
    'input_type': 'select_owner',
    'uuid': '91f2b232-bb43-4007-ab91-aacfd02d9e7a',
    'values': [
      {
        'value': 8,
        'label': 'Resilient Sysadmin (a@example.com)',
        'enabled': True,
        'properties': None,
        'uuid': 'ef284d94-697c-4397-b818-7ab5a9cb4f37',
        'hidden': False,
        'default': False
      },
      {
        'value': 7,
        'label': 'Default Group',
        'enabled': True,
        'properties': None,
        'uuid': '6f52ab7d-cbca-41ad-ab43-6ee779fe066e',
        'hidden': False,
        'default': False
      },
      {
        'value': 27,
        'label': 'QRadar Enhanced Data Migration',
        'enabled': True,
        'properties': None,
        'uuid': 'b6c55e65-fc7a-4910-ad47-d2aad6ebb948',
        'hidden': False,
        'default': False
      },
      {
        'value': 26,
        'label': 'Network Utilities functions for SOAR',
        'enabled': True,
        'properties': None,
        'uuid': '1ef470dc-1942-4e40-bf09-74a93370221f',
        'hidden': False,
        'default': False
      },
      {
        'value': 9,
        'label': 'fn_task_utils',
        'enabled': True,
        'properties': None,
        'uuid': 'f642b2bd-a912-4fcd-84bf-006df8a6cdc7',
        'hidden': False,
        'default': False
      },
      {
        'value': 11,
        'label': 'Playbook Utils',
        'enabled': True,
        'properties': None,
        'uuid': 'cfec56c5-04f8-4742-859e-72082e6efc85',
        'hidden': False,
        'default': False
      },
      {
        'value': 0,
        'label': 'System User',
        'enabled': True,
        'properties': None,
        'uuid': '379a9f5c-6c8a-4d01-ae72-c4059baaff16',
        'hidden': False,
        'default': False
      },
      {
        'value': 12,
        'label': 'QRadar Enhanced Data Migration',
        'enabled': True,
        'properties': None,
        'uuid': '8e08cf6d-4ed9-4b0c-88d3-9e46f5aaf51e',
        'hidden': False,
        'default': False
      },
      {
        'value': 15,
        'label': 'rc_data_feed_plugin_resilientfeed',
        'enabled': True,
        'properties': None,
        'uuid': '3c390806-2163-40d1-9d15-7d286e7c94d9',
        'hidden': False,
        'default': False
      },
      {
        'value': 10,
        'label': 'Outbound Email',
        'enabled': True,
        'properties': None,
        'uuid': 'a3c0b0f2-70b8-4feb-bd42-462b4942835f',
        'hidden': False,
        'default': False
      },
      {
        'value': 23,
        'label': 'Data Feeder for QRadar SOAR',
        'enabled': True,
        'properties': None,
        'uuid': 'd0e66a5d-2a2d-45f0-99e6-797c7546a3bb',
        'hidden': False,
        'default': False
      },
      {
        'value': 25,
        'label': 'Data Feeder ODBC Plugin for SOAR',
        'enabled': True,
        'properties': None,
        'uuid': 'a5850637-0933-4d79-9d17-a3e0c1e7d845',
        'hidden': False,
        'default': False
      },
      {
        'value': 24,
        'label': 'Data Feeder for QRadar SOAR',
        'enabled': True,
        'properties': None,
        'uuid': '54647c22-c1d1-4cfb-adbf-4bee80a09cb9',
        'hidden': False,
        'default': False
      }
    ],
    'rich_text': False
  },
  'crimestatus_id': {
    'id': 334,
    'name': 'crimestatus_id',
    'text': 'Criminal Activity',
    'prefix': None,
    'type_id': 0,
    'input_type': 'select',
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
    'rich_text': False
  },
  'data_compromised': {
    'id': 274,
    'name': 'data_compromised',
    'text': 'Was personal information or personal data involved?',
    'prefix': 'pii',
    'type_id': 0,
    'tooltip': 'Determine whether personal information/data was foreseeably involved, disclosed, compromised, accessed, altered, destroyed, damaged, lost or inaccessible.',
    'input_type': 'boolean',
    'uuid': '793e1363-79f5-45af-91e2-0e93356cad82',
    'values': [
      
    ],
    'rich_text': False
  },
  'data_contained': {
    'id': 318,
    'name': 'data_contained',
    'text': 'Exposure Resolved',
    'prefix': 'pii',
    'type_id': 0,
    'tooltip': 'Whether the exposure has been addressed and rectified.',
    'input_type': 'boolean',
    'uuid': 'ac1398bd-350d-4072-9754-7f8262119ec0',
    'values': [
      
    ],
    'rich_text': False
  },
  'data_encrypted': {
    'id': 316,
    'name': 'data_encrypted',
    'text': 'Data Encrypted',
    'prefix': 'pii',
    'type_id': 0,
    'tooltip': 'Whether the data in question was encrypted. Data should not be considered encrypted if the encryption keys were also breached.',
    'input_type': 'boolean',
    'uuid': '392851a9-1b28-4913-91cb-2915db7f9d6b',
    'values': [
      
    ],
    'rich_text': False
  },
  'data_format': {
    'id': 291,
    'name': 'data_format',
    'text': 'Data Format',
    'prefix': 'pii',
    'type_id': 0,
    'tooltip': 'Specify the format of the personal information involved.',
    'input_type': 'select',
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
    'rich_text': False
  },
  'data_source_ids': {
    'id': 283,
    'name': 'data_source_ids',
    'text': 'Source of Data',
    'prefix': 'pii',
    'type_id': 0,
    'tooltip': 'Original source of the data, such as the name of the database.',
    'input_type': 'multiselect',
    'uuid': 'e4d65b3a-9dca-492b-acb7-d2b33e3d5913',
    'values': [
      
    ],
    'rich_text': False
  },
  'dc_impact_likely': {
    'id': 323,
    'name': 'dc_impact_likely',
    'text': 'Impact Likely for District of Columbia',
    'prefix': 'pii',
    'type_id': 0,
    'input_type': 'boolean',
    'uuid': 'a97ce7c1-a7ec-4efe-822d-e32443392924',
    'values': [
      
    ],
    'rich_text': False
  },
  'description': {
    'id': 286,
    'name': 'description',
    'text': 'Description',
    'prefix': None,
    'type_id': 0,
    'tooltip': 'A free form text description of the incident.',
    'input_type': 'textarea',
    'uuid': '420d70b1-98f9-4681-a20b-84f36a9e5e48',
    'values': [
      
    ],
    'rich_text': True
  },
  'determined_date': {
    'id': 325,
    'name': 'determined_date',
    'text': 'Date Determined',
    'prefix': 'pii',
    'type_id': 0,
    'tooltip': 'Date you determined whether or not the incident involved a breach of personal information or personal data. Regulatory task timelines will be derived from this date and time.',
    'input_type': 'datetimepicker',
    'uuid': 'aa86ae29-5d3c-4c70-8497-93598a9dc959',
    'values': [
      
    ],
    'rich_text': False
  },
  'df_create_date': {
    'id': 1027,
    'name': 'df_create_date',
    'text': 'Data Feeder Sync Original Create Date',
    'prefix': 'properties',
    'type_id': 0,
    'tooltip': 'Original Incident create date',
    'placeholder': '',
    'input_type': 'datetimepicker',
    'uuid': '9156b378-efd4-4a53-967a-f57c72562396',
    'values': [
      
    ],
    'rich_text': False
  },
  'df_host': {
    'id': 1026,
    'name': 'df_host',
    'text': 'Data Feeder Sync Host',
    'prefix': 'properties',
    'type_id': 0,
    'tooltip': 'Host which originated the sync ',
    'placeholder': '',
    'input_type': 'text',
    'uuid': '6be1b789-913a-4a34-8589-79f8dc9c0efd',
    'values': [
      
    ],
    'rich_text': False
  },
  'df_inc_id': {
    'id': 1028,
    'name': 'df_inc_id',
    'text': 'Data Feeder Sync Incident Id',
    'prefix': 'properties',
    'type_id': 0,
    'tooltip': 'Data Feeder Sync Originating Incident Id',
    'placeholder': '',
    'input_type': 'number',
    'uuid': 'a5f7a637-0d23-463a-b8c2-9a37cab46787',
    'values': [
      
    ],
    'rich_text': False
  },
  'df_org_id': {
    'id': 1029,
    'name': 'df_org_id',
    'text': 'Data Feeder Sync Org Id',
    'prefix': 'properties',
    'type_id': 0,
    'tooltip': 'Data Feeder Sync Originating Org Id',
    'placeholder': '',
    'input_type': 'number',
    'uuid': 'ab62ae7e-7cf2-47b4-8940-f0e1e13a5834',
    'values': [
      
    ],
    'rich_text': False
  },
  'discovered_date': {
    'id': 324,
    'name': 'discovered_date',
    'text': 'Date Discovered',
    'prefix': None,
    'type_id': 0,
    'tooltip': 'Date the incident was discovered/reported.',
    'input_type': 'datetimepicker',
    'required': 'always',
    'uuid': '26cb8fa6-32e2-410d-b8e5-c23af0d09263',
    'values': [
      
    ],
    'rich_text': False
  },
  'due_date': {
    'id': 344,
    'name': 'due_date',
    'text': 'Next Due Date',
    'prefix': None,
    'type_id': 0,
    'tooltip': 'The nearest date for the next task due. This field is read-only.',
    'input_type': 'datetimepicker',
    'uuid': 'f549afb8-eb80-4fbf-96f1-63eac60412c8',
    'values': [
      
    ],
    'rich_text': False
  },
  'email_message_id': {
    'id': 566,
    'name': 'email_message_id',
    'text': 'Email Message-ID',
    'prefix': 'properties',
    'type_id': 0,
    'tooltip': 'message-id associated with the inbound email message',
    'placeholder': '',
    'input_type': 'text',
    'uuid': '6e7c2c42-88f7-443f-8c0d-0e84b2ba6525',
    'values': [
      
    ],
    'rich_text': False
  },
  'employee_involved': {
    'id': 333,
    'name': 'employee_involved',
    'text': 'Employee Involved',
    'prefix': None,
    'type_id': 0,
    'input_type': 'boolean',
    'uuid': 'b37923eb-1ade-48d9-a067-c15a313d3264',
    'values': [
      
    ],
    'rich_text': False
  },
  'end_date': {
    'id': 341,
    'name': 'end_date',
    'text': 'Date Closed',
    'prefix': None,
    'type_id': 0,
    'tooltip': 'The date the incident was closed. This field is read-only.',
    'input_type': 'datetimepicker',
    'uuid': '719d52c7-42a5-4cd6-8ce5-e8cf9317d2d1',
    'values': [
      
    ],
    'rich_text': False
  },
  'exposure_dept_id': {
    'id': 279,
    'name': 'exposure_dept_id',
    'text': 'Department',
    'prefix': None,
    'type_id': 0,
    'input_type': 'select',
    'uuid': '15c23dae-1d17-49ff-aae0-8cb457e27867',
    'values': [
      
    ],
    'rich_text': False
  },
  'exposure_individual_name': {
    'id': 328,
    'name': 'exposure_individual_name',
    'text': 'Individual Name',
    'prefix': None,
    'type_id': 0,
    'placeholder': 'Employee name',
    'input_type': 'text',
    'uuid': '77618fd8-ecd9-40e5-b86f-b42eee53498f',
    'values': [
      
    ],
    'rich_text': False
  },
  'exposure_type_id': {
    'id': 276,
    'name': 'exposure_type_id',
    'text': 'Exposure Type',
    'prefix': None,
    'type_id': 0,
    'tooltip': 'Origin source of the exposure',
    'input_type': 'select',
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
    'rich_text': False
  },
  'exposure_vendor_id': {
    'id': 284,
    'name': 'exposure_vendor_id',
    'text': 'Vendor',
    'prefix': None,
    'type_id': 0,
    'input_type': 'select',
    'uuid': 'c8f2d2c8-c44b-45c7-b4ff-783a8702b074',
    'values': [
      
    ],
    'rich_text': False
  },
  'gdpr_breach_circumstances': {
    'id': 300,
    'name': 'gdpr_breach_circumstances',
    'text': 'GDPR Breach Circumstances',
    'prefix': 'gdpr',
    'type_id': 0,
    'input_type': 'multiselect',
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
    'rich_text': False
  },
  'gdpr_breach_type': {
    'id': 301,
    'name': 'gdpr_breach_type',
    'text': 'GDPR Breach Type',
    'prefix': 'gdpr',
    'type_id': 0,
    'input_type': 'select',
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
    'rich_text': False
  },
  'gdpr_breach_type_comment': {
    'id': 302,
    'name': 'gdpr_breach_type_comment',
    'text': 'GDPR Breach Type Comment',
    'prefix': 'gdpr',
    'type_id': 0,
    'input_type': 'textarea',
    'uuid': '7354ee21-c548-44de-b179-2d45f119f228',
    'values': [
      
    ],
    'rich_text': False
  },
  'gdpr_consequences': {
    'id': 307,
    'name': 'gdpr_consequences',
    'text': 'GDPR Consequences',
    'prefix': 'gdpr',
    'type_id': 0,
    'input_type': 'select',
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
    'rich_text': False
  },
  'gdpr_consequences_comment': {
    'id': 308,
    'name': 'gdpr_consequences_comment',
    'text': 'GDPR Consequences Comment',
    'prefix': 'gdpr',
    'type_id': 0,
    'input_type': 'textarea',
    'uuid': '0064f82d-2ccb-4a5f-8f57-27d1ef95193e',
    'values': [
      
    ],
    'rich_text': False
  },
  'gdpr_final_assessment': {
    'id': 309,
    'name': 'gdpr_final_assessment',
    'text': 'GDPR Final Assessment',
    'prefix': 'gdpr',
    'type_id': 0,
    'input_type': 'select',
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
    'rich_text': False
  },
  'gdpr_final_assessment_comment': {
    'id': 310,
    'name': 'gdpr_final_assessment_comment',
    'text': 'GDPR Final Assessment Comment',
    'prefix': 'gdpr',
    'type_id': 0,
    'input_type': 'textarea',
    'uuid': 'fa91a9b6-6b12-42d6-bd40-68461d2948af',
    'values': [
      
    ],
    'rich_text': False
  },
  'gdpr_harm_risk': {
    'id': 345,
    'name': 'gdpr_harm_risk',
    'text': 'Risk of Harm',
    'prefix': 'pii',
    'type_id': 0,
    'tooltip': 'Likelihood and severity of the risk to the rights and freedoms of the data subject, as defined by the GDPR.',
    'input_type': 'select',
    'uuid': '43b88739-e201-460d-a2f3-ef2073f386d3',
    'values': [
      {
        'value': 62,
        'label': 'Low Risk',
        'enabled': True,
        'properties': None,
        'uuid': '0c5a0656-e0df-422a-8fa3-78c5a79b472d',
        'hidden': False,
        'default': False
      },
      {
        'value': 63,
        'label': 'Risk',
        'enabled': True,
        'properties': None,
        'uuid': '44f4b385-6c51-4ee3-aba8-79fb19a1b1bb',
        'hidden': False,
        'default': False
      },
      {
        'value': 64,
        'label': 'High Risk',
        'enabled': True,
        'properties': None,
        'uuid': '46306313-31c4-4549-9aa3-966b986429af',
        'hidden': False,
        'default': False
      }
    ],
    'rich_text': False
  },
  'gdpr_identification': {
    'id': 305,
    'name': 'gdpr_identification',
    'text': 'GDPR Identification',
    'prefix': 'gdpr',
    'type_id': 0,
    'input_type': 'select',
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
    'rich_text': False
  },
  'gdpr_identification_comment': {
    'id': 306,
    'name': 'gdpr_identification_comment',
    'text': 'GDPR Identification Comment',
    'prefix': 'gdpr',
    'type_id': 0,
    'input_type': 'textarea',
    'uuid': '519cf3ae-c02a-4197-a6f3-b944fe36052c',
    'values': [
      
    ],
    'rich_text': False
  },
  'gdpr_lawful_data_processing_categories': {
    'id': 346,
    'name': 'gdpr_lawful_data_processing_categories',
    'text': 'Lawful Data Processing Categories',
    'prefix': 'pii',
    'type_id': 0,
    'tooltip': 'Under the GDPR, processing of personal or sensitive data is only lawful if one or more of these categories applies.',
    'placeholder': 'Choose Some Categories',
    'input_type': 'multiselect',
    'uuid': '000fa89b-0570-4162-a720-b4b188b06ad3',
    'values': [
      {
        'value': 65,
        'label': 'Consent by data subject',
        'enabled': True,
        'properties': None,
        'uuid': 'b31ffbc5-7e24-4a54-8c8d-e26caf7a96c7',
        'hidden': False,
        'default': False
      },
      {
        'value': 66,
        'label': 'Performance of contract',
        'enabled': True,
        'properties': None,
        'uuid': '447b6e53-ca8a-4cde-ab2c-f529132a1948',
        'hidden': False,
        'default': False
      },
      {
        'value': 67,
        'label': 'Compliance with legal obligation',
        'enabled': True,
        'properties': None,
        'uuid': '82817a05-c4ae-453b-a0ea-52be2fd43d7c',
        'hidden': False,
        'default': False
      },
      {
        'value': 68,
        'label': 'Protection of vital interests of data subject',
        'enabled': True,
        'properties': None,
        'uuid': '4ce0da31-4f52-4308-985a-7a56194617d0',
        'hidden': False,
        'default': False
      },
      {
        'value': 69,
        'label': 'Public interest or official authority',
        'enabled': True,
        'properties': None,
        'uuid': 'e1dcd2f7-4a42-4f87-add6-58d74dee7b58',
        'hidden': False,
        'default': False
      },
      {
        'value': 70,
        'label': 'Legitimate interests of data controller or third party',
        'enabled': True,
        'properties': None,
        'uuid': 'c34f95d3-23a9-46ef-b67c-f795b4928ce5',
        'hidden': False,
        'default': False
      }
    ],
    'rich_text': False
  },
  'gdpr_personal_data': {
    'id': 303,
    'name': 'gdpr_personal_data',
    'text': 'GDPR Personal Data',
    'prefix': 'gdpr',
    'type_id': 0,
    'input_type': 'select',
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
    'rich_text': False
  },
  'gdpr_personal_data_comment': {
    'id': 304,
    'name': 'gdpr_personal_data_comment',
    'text': 'GDPR Personal Data Comment',
    'prefix': 'gdpr',
    'type_id': 0,
    'input_type': 'textarea',
    'uuid': '77b2b8cb-ed5c-427f-a9cc-161b13859cbb',
    'values': [
      
    ],
    'rich_text': False
  },
  'gdpr_subsequent_notification': {
    'id': 311,
    'name': 'gdpr_subsequent_notification',
    'text': 'GDPR Subsequent Notification',
    'prefix': 'gdpr',
    'type_id': 0,
    'input_type': 'boolean',
    'uuid': '09f66a71-8c7a-4279-a669-cc6542d124ef',
    'values': [
      
    ],
    'rich_text': False
  },
  'hard_liability': {
    'id': 289,
    'name': 'hard_liability',
    'text': 'Assessed Liability',
    'prefix': None,
    'type_id': 0,
    'input_type': 'number',
    'uuid': '72c2c73f-620a-4bb6-900a-705a0bdf912d',
    'values': [
      
    ],
    'rich_text': False
  },
  'harmstatus_id': {
    'id': 330,
    'name': 'harmstatus_id',
    'text': 'Is harm/risk/misuse foreseeable?',
    'prefix': 'pii',
    'type_id': 0,
    'tooltip': 'Different jurisdictions use harm, risk, misuse, ID theft, and other standards as safe harbors from notification. Interpretation of these terms has frequently been the subject of litigation.',
    'input_type': 'select',
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
    'rich_text': False
  },
  'id': {
    'id': 343,
    'name': 'id',
    'text': 'ID',
    'prefix': None,
    'type_id': 0,
    'input_type': 'number',
    'uuid': '44d6a6ac-886f-46ff-9683-90a13765862a',
    'values': [
      
    ],
    'rich_text': False
  },
  'impact_likely': {
    'id': 319,
    'name': 'impact_likely',
    'text': 'Impact Likely',
    'prefix': 'pii',
    'type_id': 0,
    'input_type': 'boolean',
    'uuid': '4137fbca-9ec7-42e9-9e39-9ef61197cc9b',
    'values': [
      
    ],
    'rich_text': False
  },
  'inc_last_modified_date': {
    'id': 326,
    'name': 'inc_last_modified_date',
    'text': 'Last Modified',
    'prefix': None,
    'type_id': 0,
    'tooltip': 'The date the incident was last modified.This field is read only.',
    'input_type': 'datetimepicker',
    'uuid': 'a75e8d1d-d940-4c8a-82f1-8839ab60d583',
    'values': [
      
    ],
    'rich_text': False
  },
  'inc_training': {
    'id': 339,
    'name': 'inc_training',
    'text': 'Simulation',
    'prefix': None,
    'type_id': 0,
    'tooltip': 'Whether the incident is a simulation or a regular incident. This field is read-only.',
    'input_type': 'boolean',
    'uuid': 'c3f0e3ed-21e1-4d53-affb-fe5ca3308cca',
    'values': [
      
    ],
    'rich_text': False
  },
  'incident_type_ids': {
    'id': 287,
    'name': 'incident_type_ids',
    'text': 'Incident Type',
    'prefix': None,
    'type_id': 0,
    'tooltip': 'The type of incident',
    'placeholder': 'Choose Some Types',
    'input_type': 'multiselect',
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
        'value': 1002,
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
    'rich_text': False
  },
  'internal_customizations_field': {
    'id': 558,
    'name': 'internal_customizations_field',
    'text': 'Customizations Field (internal)',
    'prefix': 'properties',
    'type_id': 0,
    'input_type': 'text',
    'uuid': 'bfeec2d4-3770-11e8-ad39-4a0004044aa1',
    'values': [
      
    ],
    'rich_text': False
  },
  'jurisdiction_name': {
    'id': 272,
    'name': 'jurisdiction_name',
    'text': 'Jurisdiction',
    'prefix': None,
    'type_id': 0,
    'input_type': 'text',
    'uuid': '658354fe-3bcd-429e-aa08-5998799cc6d2',
    'values': [
      
    ],
    'rich_text': False
  },
  'members': {
    'id': 317,
    'name': 'members',
    'text': 'Members',
    'prefix': None,
    'type_id': 0,
    'input_type': 'multiselect_members',
    'uuid': 'cf473808-ea3b-4e47-833b-3507891bea5e',
    'values': [
      {
        'value': 8,
        'label': 'Resilient Sysadmin (a@example.com)',
        'enabled': True,
        'properties': None,
        'uuid': 'ef284d94-697c-4397-b818-7ab5a9cb4f37',
        'hidden': False,
        'default': False
      },
      {
        'value': 7,
        'label': 'Default Group',
        'enabled': True,
        'properties': None,
        'uuid': '6f52ab7d-cbca-41ad-ab43-6ee779fe066e',
        'hidden': False,
        'default': False
      },
      {
        'value': 27,
        'label': 'QRadar Enhanced Data Migration',
        'enabled': True,
        'properties': None,
        'uuid': 'b6c55e65-fc7a-4910-ad47-d2aad6ebb948',
        'hidden': False,
        'default': False
      },
      {
        'value': 26,
        'label': 'Network Utilities functions for SOAR',
        'enabled': True,
        'properties': None,
        'uuid': '1ef470dc-1942-4e40-bf09-74a93370221f',
        'hidden': False,
        'default': False
      },
      {
        'value': 9,
        'label': 'fn_task_utils',
        'enabled': True,
        'properties': None,
        'uuid': 'f642b2bd-a912-4fcd-84bf-006df8a6cdc7',
        'hidden': False,
        'default': False
      },
      {
        'value': 11,
        'label': 'Playbook Utils',
        'enabled': True,
        'properties': None,
        'uuid': 'cfec56c5-04f8-4742-859e-72082e6efc85',
        'hidden': False,
        'default': False
      },
      {
        'value': 0,
        'label': 'System User',
        'enabled': True,
        'properties': None,
        'uuid': '379a9f5c-6c8a-4d01-ae72-c4059baaff16',
        'hidden': False,
        'default': False
      },
      {
        'value': 12,
        'label': 'QRadar Enhanced Data Migration',
        'enabled': True,
        'properties': None,
        'uuid': '8e08cf6d-4ed9-4b0c-88d3-9e46f5aaf51e',
        'hidden': False,
        'default': False
      },
      {
        'value': 15,
        'label': 'rc_data_feed_plugin_resilientfeed',
        'enabled': True,
        'properties': None,
        'uuid': '3c390806-2163-40d1-9d15-7d286e7c94d9',
        'hidden': False,
        'default': False
      },
      {
        'value': 10,
        'label': 'Outbound Email',
        'enabled': True,
        'properties': None,
        'uuid': 'a3c0b0f2-70b8-4feb-bd42-462b4942835f',
        'hidden': False,
        'default': False
      },
      {
        'value': 23,
        'label': 'Data Feeder for QRadar SOAR',
        'enabled': True,
        'properties': None,
        'uuid': 'd0e66a5d-2a2d-45f0-99e6-797c7546a3bb',
        'hidden': False,
        'default': False
      },
      {
        'value': 25,
        'label': 'Data Feeder ODBC Plugin for SOAR',
        'enabled': True,
        'properties': None,
        'uuid': 'a5850637-0933-4d79-9d17-a3e0c1e7d845',
        'hidden': False,
        'default': False
      },
      {
        'value': 24,
        'label': 'Data Feeder for QRadar SOAR',
        'enabled': True,
        'properties': None,
        'uuid': '54647c22-c1d1-4cfb-adbf-4bee80a09cb9',
        'hidden': False,
        'default': False
      }
    ],
    'rich_text': False
  },
  'name': {
    'id': 288,
    'name': 'name',
    'text': 'Name',
    'prefix': None,
    'type_id': 0,
    'tooltip': 'A unique name to identify this particular incident.',
    'input_type': 'text',
    'required': 'always',
    'uuid': 'ad6ed4f2-8d87-4ba2-81fa-03568a9326cc',
    'values': [
      
    ],
    'rich_text': False
  },
  'negative_pr_likely': {
    'id': 331,
    'name': 'negative_pr_likely',
    'text': 'Negative PR',
    'prefix': None,
    'type_id': 0,
    'tooltip': 'If it is foreseeable that the incident might generate any negative public image or publicity for your company or organization.',
    'input_type': 'boolean',
    'uuid': '94dbbd0e-3c82-4650-bd17-bddb3003a7e6',
    'values': [
      
    ],
    'rich_text': False
  },
  'new_zealand_risk_assessment': {
    'id': 313,
    'name': 'new_zealand_risk_assessment',
    'text': 'New Zealand Risk Assessment',
    'prefix': 'pii',
    'type_id': 0,
    'input_type': 'boolean',
    'uuid': '19d1232b-f78e-4514-88c6-5133a51bc8b1',
    'values': [
      
    ],
    'rich_text': False
  },
  'nist_attack_vectors': {
    'id': 273,
    'name': 'nist_attack_vectors',
    'text': 'NIST Attack Vectors',
    'prefix': None,
    'type_id': 0,
    'tooltip': 'NIST Attack Vectors the incident falls under, if applicable.',
    'placeholder': 'Choose Applicable Vectors',
    'input_type': 'multiselect',
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
    'rich_text': False
  },
  'ny_impact_likely': {
    'id': 320,
    'name': 'ny_impact_likely',
    'text': 'Impact Likely for New York',
    'prefix': 'pii',
    'type_id': 0,
    'input_type': 'boolean',
    'uuid': '688a9bc2-cd38-4a45-b7ff-9344b76597fb',
    'values': [
      
    ],
    'rich_text': False
  },
  'or_impact_likely': {
    'id': 321,
    'name': 'or_impact_likely',
    'text': 'Impact Likely for Oregon',
    'prefix': 'pii',
    'type_id': 0,
    'input_type': 'boolean',
    'uuid': '2203d24c-b5b4-48cb-811c-d27fac5ef09a',
    'values': [
      
    ],
    'rich_text': False
  },
  'org_handle': {
    'id': 347,
    'name': 'org_handle',
    'text': 'Organization',
    'prefix': None,
    'type_id': 0,
    'input_type': 'select',
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
    'rich_text': False
  },
  'owner_id': {
    'id': 332,
    'name': 'owner_id',
    'text': 'Owner',
    'prefix': None,
    'type_id': 0,
    'input_type': 'select_owner',
    'uuid': '97d1d2a1-d25e-4279-9d29-7bc60fd321ce',
    'values': [
      {
        'value': 8,
        'label': 'Resilient Sysadmin (a@example.com)',
        'enabled': True,
        'properties': None,
        'uuid': 'ef284d94-697c-4397-b818-7ab5a9cb4f37',
        'hidden': False,
        'default': False
      },
      {
        'value': 7,
        'label': 'Default Group',
        'enabled': True,
        'properties': None,
        'uuid': '6f52ab7d-cbca-41ad-ab43-6ee779fe066e',
        'hidden': False,
        'default': False
      },
      {
        'value': 27,
        'label': 'QRadar Enhanced Data Migration',
        'enabled': True,
        'properties': None,
        'uuid': 'b6c55e65-fc7a-4910-ad47-d2aad6ebb948',
        'hidden': False,
        'default': False
      },
      {
        'value': 26,
        'label': 'Network Utilities functions for SOAR',
        'enabled': True,
        'properties': None,
        'uuid': '1ef470dc-1942-4e40-bf09-74a93370221f',
        'hidden': False,
        'default': False
      },
      {
        'value': 9,
        'label': 'fn_task_utils',
        'enabled': True,
        'properties': None,
        'uuid': 'f642b2bd-a912-4fcd-84bf-006df8a6cdc7',
        'hidden': False,
        'default': False
      },
      {
        'value': 11,
        'label': 'Playbook Utils',
        'enabled': True,
        'properties': None,
        'uuid': 'cfec56c5-04f8-4742-859e-72082e6efc85',
        'hidden': False,
        'default': False
      },
      {
        'value': 0,
        'label': 'System User',
        'enabled': True,
        'properties': None,
        'uuid': '379a9f5c-6c8a-4d01-ae72-c4059baaff16',
        'hidden': False,
        'default': False
      },
      {
        'value': 12,
        'label': 'QRadar Enhanced Data Migration',
        'enabled': True,
        'properties': None,
        'uuid': '8e08cf6d-4ed9-4b0c-88d3-9e46f5aaf51e',
        'hidden': False,
        'default': False
      },
      {
        'value': 15,
        'label': 'rc_data_feed_plugin_resilientfeed',
        'enabled': True,
        'properties': None,
        'uuid': '3c390806-2163-40d1-9d15-7d286e7c94d9',
        'hidden': False,
        'default': False
      },
      {
        'value': 10,
        'label': 'Outbound Email',
        'enabled': True,
        'properties': None,
        'uuid': 'a3c0b0f2-70b8-4feb-bd42-462b4942835f',
        'hidden': False,
        'default': False
      },
      {
        'value': 23,
        'label': 'Data Feeder for QRadar SOAR',
        'enabled': True,
        'properties': None,
        'uuid': 'd0e66a5d-2a2d-45f0-99e6-797c7546a3bb',
        'hidden': False,
        'default': False
      },
      {
        'value': 25,
        'label': 'Data Feeder ODBC Plugin for SOAR',
        'enabled': True,
        'properties': None,
        'uuid': 'a5850637-0933-4d79-9d17-a3e0c1e7d845',
        'hidden': False,
        'default': False
      },
      {
        'value': 24,
        'label': 'Data Feeder for QRadar SOAR',
        'enabled': True,
        'properties': None,
        'uuid': '54647c22-c1d1-4cfb-adbf-4bee80a09cb9',
        'hidden': False,
        'default': False
      }
    ],
    'rich_text': False
  },
  'phase_id': {
    'id': 290,
    'name': 'phase_id',
    'text': 'Phase',
    'prefix': None,
    'type_id': 0,
    'tooltip': 'The phase of the incident.',
    'input_type': 'select',
    'uuid': 'ea47a365-620d-4419-a767-f1b08f2685d7',
    'values': [
      {
        'value': 1009,
        'label': 'Initial',
        'enabled': True,
        'properties': None,
        'uuid': '5558dfa9-3c70-498b-aa39-c1538c1ae671',
        'hidden': False,
        'default': False
      },
      {
        'value': 1008,
        'label': 'Engage',
        'enabled': True,
        'properties': None,
        'uuid': 'ed053e3a-2d6d-47e1-8240-844ed93d4893',
        'hidden': False,
        'default': False
      },
      {
        'value': 1011,
        'label': 'Detect/Analyze',
        'enabled': True,
        'properties': None,
        'uuid': '44868c86-246e-4e6e-8636-fa2848b2f279',
        'hidden': False,
        'default': False
      },
      {
        'value': 1010,
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
        'value': 1007,
        'label': 'Complete',
        'enabled': True,
        'properties': None,
        'uuid': 'd057ec97-587e-44c0-ae84-c4fadd6d7e40',
        'hidden': False,
        'default': False
      }
    ],
    'rich_text': False
  },
  'pipeda_other_factors': {
    'id': 297,
    'name': 'pipeda_other_factors',
    'text': 'PIPEDA Other Factors',
    'prefix': 'regulator_risk',
    'type_id': 0,
    'input_type': 'select',
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
    'rich_text': False
  },
  'pipeda_other_factors_comment': {
    'id': 296,
    'name': 'pipeda_other_factors_comment',
    'text': 'PIPEDA Other Factors Comment',
    'prefix': 'regulator_risk',
    'type_id': 0,
    'input_type': 'textarea',
    'uuid': '4b493998-e1a3-447c-aa74-d3fa8b0bcfe3',
    'values': [
      
    ],
    'rich_text': False
  },
  'pipeda_overall_assessment': {
    'id': 299,
    'name': 'pipeda_overall_assessment',
    'text': 'PIPEDA Overall Assessment',
    'prefix': 'regulator_risk',
    'type_id': 0,
    'input_type': 'select',
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
    'rich_text': False
  },
  'pipeda_overall_assessment_comment': {
    'id': 298,
    'name': 'pipeda_overall_assessment_comment',
    'text': 'PIPEDA Overall Assessment Comment',
    'prefix': 'regulator_risk',
    'type_id': 0,
    'input_type': 'textarea',
    'uuid': '69fca6b3-c00c-496a-a333-123513ef89e6',
    'values': [
      
    ],
    'rich_text': False
  },
  'pipeda_probability_of_misuse': {
    'id': 295,
    'name': 'pipeda_probability_of_misuse',
    'text': 'PIPEDA Probability of Misuse',
    'prefix': 'regulator_risk',
    'type_id': 0,
    'input_type': 'select',
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
    'rich_text': False
  },
  'pipeda_probability_of_misuse_comment': {
    'id': 294,
    'name': 'pipeda_probability_of_misuse_comment',
    'text': 'PIPEDA Probability of Misuse Comment',
    'prefix': 'regulator_risk',
    'type_id': 0,
    'input_type': 'textarea',
    'uuid': 'b49e6381-2a11-473e-ac9c-c798805cf039',
    'values': [
      
    ],
    'rich_text': False
  },
  'pipeda_sensitivity_of_pi': {
    'id': 293,
    'name': 'pipeda_sensitivity_of_pi',
    'text': 'PIPEDA Sensitivity of PI',
    'prefix': 'regulator_risk',
    'type_id': 0,
    'input_type': 'select',
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
    'rich_text': False
  },
  'pipeda_sensitivity_of_pi_comment': {
    'id': 292,
    'name': 'pipeda_sensitivity_of_pi_comment',
    'text': 'PIPEDA Sensitivity of PI Comment',
    'prefix': 'regulator_risk',
    'type_id': 0,
    'input_type': 'textarea',
    'uuid': '65beb4ea-420e-40e3-b43a-37dee8c1675d',
    'values': [
      
    ],
    'rich_text': False
  },
  'plan_status': {
    'id': 282,
    'name': 'plan_status',
    'text': 'Status',
    'prefix': None,
    'type_id': 0,
    'input_type': 'select',
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
    'rich_text': False
  },
  'qr_assigned': {
    'id': 648,
    'name': 'qr_assigned',
    'text': 'QR Assigned',
    'prefix': 'properties',
    'type_id': 0,
    'tooltip': 'The analyst to whom the QRadar Offense is assigned to.',
    'placeholder': '',
    'input_type': 'textarea',
    'uuid': 'cee826b5-5bab-44ba-a177-3458d25199aa',
    'values': [
      
    ],
    'rich_text': True
  },
  'qr_credibility': {
    'id': 650,
    'name': 'qr_credibility',
    'text': 'QR Credibility',
    'prefix': 'properties',
    'type_id': 0,
    'tooltip': 'Indicates the integrity of the offense as determined by the credibility rating that is configured in the log source.',
    'placeholder': '',
    'input_type': 'textarea',
    'uuid': 'ea93f610-b018-413e-8ffd-24a710172490',
    'values': [
      
    ],
    'rich_text': True
  },
  'qr_destination_ip_count': {
    'id': 659,
    'name': 'qr_destination_ip_count',
    'text': 'QR Destination IP Count',
    'prefix': 'properties',
    'type_id': 0,
    'tooltip': 'The no. of Destination IPs associated with the QRadar Offense',
    'placeholder': '',
    'input_type': 'textarea',
    'uuid': '5be7494c-2776-4df1-8d20-fa994ab11d93',
    'values': [
      
    ],
    'rich_text': True
  },
  'qr_event_count': {
    'id': 657,
    'name': 'qr_event_count',
    'text': 'QR Event Count',
    'prefix': 'properties',
    'type_id': 0,
    'tooltip': 'The no. of events associated with the QRadar Offense',
    'placeholder': '',
    'input_type': 'textarea',
    'uuid': '4f7dfb5c-f38d-471b-b7a7-203e5d5790d9',
    'values': [
      
    ],
    'rich_text': True
  },
  'qr_flow_count': {
    'id': 645,
    'name': 'qr_flow_count',
    'text': 'QR Flow Count',
    'prefix': 'properties',
    'type_id': 0,
    'tooltip': 'The no. of flows associated with the QRadar Offense',
    'placeholder': '',
    'input_type': 'textarea',
    'uuid': '9bd3220a-33f8-4edc-b007-670cc3aaf59f',
    'values': [
      
    ],
    'rich_text': True
  },
  'qr_last_updated_time': {
    'id': 655,
    'name': 'qr_last_updated_time',
    'text': 'QR Incident Last Updated Time',
    'prefix': 'properties',
    'type_id': 0,
    'tooltip': '',
    'placeholder': '',
    'input_type': 'datetimepicker',
    'uuid': '39b1941a-8e62-4c19-a595-c7ab4ec4ec5f',
    'values': [
      
    ],
    'rich_text': False
  },
  'qr_magnitude': {
    'id': 661,
    'name': 'qr_magnitude',
    'text': 'QR Magnitude',
    'prefix': 'properties',
    'type_id': 0,
    'tooltip': 'Indicates the relative importance of the offense. This value is calculated based on the relevance, severity, and credibility ratings.',
    'placeholder': '',
    'input_type': 'textarea',
    'uuid': '73b97697-3400-4bcc-be42-52020a0362a2',
    'values': [
      
    ],
    'rich_text': True
  },
  'qr_offense_domain': {
    'id': 658,
    'name': 'qr_offense_domain',
    'text': 'QR Offense Domain',
    'prefix': 'properties',
    'type_id': 0,
    'tooltip': '',
    'placeholder': '',
    'input_type': 'text',
    'uuid': '568fa360-983f-463d-af2d-01bd8c7a0e25',
    'values': [
      
    ],
    'rich_text': False
  },
  'qr_offense_index_type': {
    'id': 647,
    'name': 'qr_offense_index_type',
    'text': 'QR Offense Index Type',
    'prefix': 'properties',
    'type_id': 0,
    'tooltip': 'The type on which the QRadar Offense is indexed',
    'placeholder': '',
    'input_type': 'text',
    'uuid': 'c34fdc0c-b8e4-4ac8-b149-20f0f30cba01',
    'values': [
      
    ],
    'rich_text': False
  },
  'qr_offense_index_value': {
    'id': 652,
    'name': 'qr_offense_index_value',
    'text': 'QR Offense Index Value',
    'prefix': 'properties',
    'type_id': 0,
    'tooltip': 'The value by which QRadar Offense is indexed',
    'placeholder': '',
    'input_type': 'text',
    'uuid': 'f4354ca9-d038-45a5-a91f-b4beaf3f5f18',
    'values': [
      
    ],
    'rich_text': False
  },
  'qr_offense_last_updated_time': {
    'id': 644,
    'name': 'qr_offense_last_updated_time',
    'text': 'QR Offense Last Updated Time',
    'prefix': 'properties',
    'type_id': 0,
    'tooltip': '',
    'placeholder': '',
    'input_type': 'datetimepicker',
    'uuid': '8e612fca-fa1e-448d-9ecd-541ccb158573',
    'values': [
      
    ],
    'rich_text': False
  },
  'qr_offense_source': {
    'id': 660,
    'name': 'qr_offense_source',
    'text': 'QR Offense Source ',
    'prefix': 'properties',
    'type_id': 0,
    'tooltip': 'The source for the QRadar Offense',
    'placeholder': '',
    'input_type': 'text',
    'uuid': '6af22a10-7581-4faf-afc8-c46fb68057f1',
    'values': [
      
    ],
    'rich_text': False
  },
  'qr_offense_start_time': {
    'id': 653,
    'name': 'qr_offense_start_time',
    'text': 'QR Offense Start Time',
    'prefix': 'properties',
    'type_id': 0,
    'tooltip': '',
    'placeholder': '',
    'input_type': 'datetimepicker',
    'uuid': '11e94c0e-62d5-4ef9-8b5d-7073f487b606',
    'values': [
      
    ],
    'rich_text': False
  },
  'qr_offense_status': {
    'id': 643,
    'name': 'qr_offense_status',
    'text': 'QR Offense Status',
    'prefix': 'properties',
    'type_id': 0,
    'tooltip': '',
    'placeholder': '',
    'input_type': 'text',
    'uuid': '8632d157-312f-49b7-9526-220077ef6131',
    'values': [
      
    ],
    'rich_text': False
  },
  'qr_relevance': {
    'id': 651,
    'name': 'qr_relevance',
    'text': 'QR Relevance',
    'prefix': 'properties',
    'type_id': 0,
    'tooltip': 'Indicates the importance of the destination. QRadar determines the relevance by the weight that the administrator assigned to the networks and assets.',
    'placeholder': '',
    'input_type': 'textarea',
    'uuid': 'ef2b94ed-84b9-4388-9e7b-7cafedf6ea4e',
    'values': [
      
    ],
    'rich_text': True
  },
  'qr_severity': {
    'id': 654,
    'name': 'qr_severity',
    'text': 'QR Severity',
    'prefix': 'properties',
    'type_id': 0,
    'tooltip': 'Indicates the threat that an attack poses in relation to how prepared the destination is for the attack.',
    'placeholder': '',
    'input_type': 'textarea',
    'uuid': '3659f126-c8df-47cb-bcdb-4dcbab3dbd84',
    'values': [
      
    ],
    'rich_text': True
  },
  'qr_source_ip_count': {
    'id': 649,
    'name': 'qr_source_ip_count',
    'text': 'QR Source IP Count',
    'prefix': 'properties',
    'type_id': 0,
    'tooltip': 'The no. of Source IPs associated with the QRadar Offense',
    'placeholder': '',
    'input_type': 'textarea',
    'uuid': 'd9536f5a-3692-466b-b4c8-1045799d19ba',
    'values': [
      
    ],
    'rich_text': True
  },
  'qradar_destination': {
    'id': 656,
    'name': 'qradar_destination',
    'text': 'QRadar Destination',
    'prefix': 'properties',
    'type_id': 0,
    'tooltip': 'QRadar Destination to Sync With',
    'placeholder': '',
    'input_type': 'text',
    'uuid': '3b119adb-7585-44b6-b578-7c5d5ee6958d',
    'values': [
      
    ],
    'rich_text': False
  },
  'qradar_id': {
    'id': 646,
    'name': 'qradar_id',
    'text': 'QR Offense Id',
    'short_text': '',
    'prefix': 'properties',
    'type_id': 0,
    'tooltip': '',
    'placeholder': '',
    'input_type': 'text',
    'uuid': 'aedb7df6-642a-4438-824d-fe24be34cfc0',
    'values': [
      
    ],
    'rich_text': False
  },
  'reporter': {
    'id': 281,
    'name': 'reporter',
    'text': 'Reporting Individual',
    'prefix': None,
    'type_id': 0,
    'tooltip': 'Name of person who reported the event, such as a device owner or his/her manager',
    'placeholder': 'Employee name',
    'input_type': 'text',
    'uuid': '931afc2e-e09d-48e1-8b71-c1cc50e1eba6',
    'values': [
      
    ],
    'rich_text': False
  },
  'resolution_id': {
    'id': 337,
    'name': 'resolution_id',
    'text': 'Resolution',
    'prefix': None,
    'type_id': 0,
    'tooltip': 'Select an option that accurately describes the reason for closing this incident.',
    'input_type': 'select',
    'required': 'close',
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
      }
    ],
    'rich_text': False
  },
  'resolution_summary': {
    'id': 338,
    'name': 'resolution_summary',
    'text': 'Resolution Summary',
    'prefix': None,
    'type_id': 0,
    'tooltip': 'Enter a summary that describes how this incident was resolved.',
    'input_type': 'textarea',
    'required': 'close',
    'uuid': 'f5d18473-03f6-4149-b0d9-1ce9006b4a99',
    'values': [
      
    ],
    'rich_text': True
  },
  'sequence_code': {
    'id': 348,
    'name': 'sequence_code',
    'text': 'Sequence Code',
    'prefix': None,
    'type_id': 0,
    'tooltip': 'The Unique Incident Sequence Code.',
    'input_type': 'text',
    'uuid': '7662e73c-9e92-11e9-bd1f-2745873db71d',
    'values': [
      
    ],
    'rich_text': False
  },
  'severity_code': {
    'id': 336,
    'name': 'severity_code',
    'text': 'Severity',
    'prefix': None,
    'type_id': 0,
    'tooltip': 'Your impression of the events relative severity vs. other events that may be entered into the system.',
    'input_type': 'select',
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
    'rich_text': False
  },
  'singapore_risk_assessment': {
    'id': 314,
    'name': 'singapore_risk_assessment',
    'text': 'Singapore Risk Assessment',
    'prefix': 'pii',
    'type_id': 0,
    'input_type': 'boolean',
    'uuid': 'ea1802d6-008b-4b88-a7d6-fb1fbbd3f839',
    'values': [
      
    ],
    'rich_text': False
  },
  'start_date': {
    'id': 335,
    'name': 'start_date',
    'text': 'Date Occurred',
    'prefix': None,
    'type_id': 0,
    'tooltip': 'Date the incident occurred',
    'input_type': 'datetimepicker',
    'uuid': '90f5a419-e126-48db-888c-80fe09444cfe',
    'values': [
      
    ],
    'rich_text': False
  },
  'state': {
    'id': 275,
    'name': 'state',
    'text': 'State',
    'prefix': None,
    'type_id': 0,
    'input_type': 'select',
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
    'rich_text': False
  },
  'test_multiselect': {
    'id': 1247,
    'name': 'test_multiselect',
    'text': 'test_multiselect',
    'short_text': '',
    'prefix': 'properties',
    'type_id': 0,
    'tooltip': '',
    'placeholder': '',
    'input_type': 'multiselect',
    'uuid': '659e6a20-5e0e-447c-b8c4-7eb6353bbff8',
    'values': [
      {
        'value': 317,
        'label': 'd',
        'enabled': True,
        'properties': None,
        'uuid': '8597d2ca-f9aa-46d6-97f6-e6715c662115',
        'hidden': False,
        'default': True
      },
      {
        'value': 318,
        'label': 'e',
        'enabled': True,
        'properties': None,
        'uuid': '5626301e-4f20-415e-ab9e-8111ef059049',
        'hidden': False,
        'default': False
      },
      {
        'value': 319,
        'label': 'f',
        'enabled': True,
        'properties': None,
        'uuid': '189fa1cb-2dd2-4a8c-8773-fe3567f92fd2',
        'hidden': False,
        'default': False
      }
    ],
    'rich_text': False
  },
  'test_select': {
    'id': 1246,
    'name': 'test_select',
    'text': 'test select',
    'short_text': '',
    'prefix': 'properties',
    'type_id': 0,
    'tooltip': '',
    'placeholder': '',
    'input_type': 'select',
    'uuid': 'd19bb103-1f6d-4ffa-ba0b-b50f434985c3',
    'rich_text': False
  },
  'wa_impact_likely': {
    'id': 322,
    'name': 'wa_impact_likely',
    'text': 'Impact Likely for Washington',
    'prefix': 'pii',
    'type_id': 0,
    'input_type': 'boolean',
    'uuid': '7808b829-23a1-4d99-987c-701602a05069',
    'values': [
      
    ],
    'rich_text': False
  },
  'workspace': {
    'id': 280,
    'name': 'workspace',
    'text': 'Workspace',
    'prefix': None,
    'type_id': 0,
    'input_type': 'select',
    'required': 'always',
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
    'rich_text': False
  },
  'zip': {
    'id': 327,
    'name': 'zip',
    'text': 'Zip',
    'prefix': None,
    'type_id': 0,
    'input_type': 'text',
    'uuid': 'e486619d-b212-43fd-bb1d-785f4cd312ce',
    'values': [
      
    ],
    'rich_text': False
  }
}

class IncidentMock(BasicResilientMock):
    incident_id = 123
    incident_1 = {
        "id": incident_id,
        "name": "some title",
        "description": "some description",
        "vers": 5,
        "discovered_date": 1664571300000,
        "create_date": 1664571301083,
        "owner_id": 68,
        "severity_code": None
    }

    mock_incident_fields = {
        "id": incident_id,
        "type_id": 0,
        "type_name": "incident",
        "fields": {
            "country": {"name": "country", "input_type": "select"},
            "resolution_id": {"name": "resolution_id", "input_type": "select", "required": "close"},
            "resolution_summary": {"name": "resolution_summary", "input_type": "textarea", "required": "close"},
            "workspace": {"name": "resolution_id", "input_type": "select", "required": "always"}
        },
        "vers": 5
    }

    mock_incident_attachments = {
        "attachments": [],
        "max_results_exceeded": False
    }

    @resilient_endpoint("GET", "/types/incident$")
    def incident_types_get(self, request):
        """ Callback for GET to /orgs/<org_id>/types/incident """
        LOG.info("incident_types_get")
        return requests_mock.create_response(request, status_code=200, json=IncidentMock.mock_incident_fields)

    @resilient_endpoint("GET", "/incidents/[0-9]+\?handle_format=names$")
    def incident_get(self, request):
        """ Callback for GET to /orgs/<org_id>/incidents/<inc_id> """
        LOG.info("incident_get")
        return requests_mock.create_response(request, status_code=200, json=IncidentMock.incident_1)

    @resilient_endpoint("POST", "/incidents/[0-9]+/attachments/query*")
    def incident_attachment_post(self, request):
        LOG.info("incident_attachment_post")
        return requests_mock.create_response(request, status_code=200, json=IncidentMock.mock_incident_attachments)
