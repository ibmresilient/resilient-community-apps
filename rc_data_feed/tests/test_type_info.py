# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

import pytest
from rc_data_feed.lib.type_info import TypeInfo, ActionMessageTypeInfo

TYPE_INFO_MAP = {
      "fields": {
        "country": {
          "id": 55,
          "values": {}
        },
        "workspace": {
          "id": 9,
          "values": {
            "1": {
              "default": True,
              "enabled": True,
              "hidden": False,
              "label": "Default workspace",
              "properties": None,
              "uuid": "47350579-3795-4d7f-907f-c2d1fd329816",
              "value": 1
            }
          }
        },
        "df_create_date": {
          "id": 193,
          "values": {}
        },
        "owner_id": {
          "id": 58,
          "values": {
            "3": {
              "default": False,
              "enabled": True,
              "hidden": False,
              "label": "Resilient Sysadmin (a@example.com)",
              "properties": None,
              "uuid": "ec5f0df2-132a-46f5-8ec1-08dbfaaf59c9",
              "value": 3
            }
          }
        },
        "gdpr_lawful_data_processing_categories": {
          "id": 72,
          "values": {}
        },
        "impact_likely": {
          "id": 45,
          "values": {}
        },
        "gdpr_consequences": {
          "id": 36,
          "values": {}
        },
        "severity_code": {
          "id": 62,
          "values": {
            "4": {
              "default": True,
              "enabled": True,
              "hidden": False,
              "label": "Low",
              "properties": None,
              "uuid": "97cae239-963d-4e36-be34-07e47ef2cc86",
              "value": 4
            }
          }
        },
        "data_encrypted": {
          "id": 42,
          "values": {}
        },
        "resolution_id": {
          "id": 63,
          "values": {}
        },
        "gdpr_subsequent_notification": {
          "id": 40,
          "values": {}
        },
        "incident_type_ids": {
          "id": 16,
          "values": {}
        },
        "members": {
          "id": 43,
          "values": {}
        },
        "or_impact_likely": {
          "id": 47,
          "values": {}
        },
        "on_close_datetime": {
          "id": 624,
          "values": {}
        },
        "state": {
          "id": 4,
          "values": {}
        },
        "id": {
          "id": 69,
          "values": {}
        },
        "create_date": {
          "id": 66,
          "values": {}
        },
        "custom_int": {
          "id": 472,
          "values": {}
        },
        "zip": {
          "id": 53,
          "values": {}
        },
        "on_close_number": {
          "id": 622,
          "values": {}
        },
        "pipeda_probability_of_misuse": {
          "id": 24,
          "values": {}
        },
        "hard_liability": {
          "id": 18,
          "values": {}
        },
        "dc_impact_likely": {
          "id": 49,
          "values": {}
        },
        "sequence_code": {
          "id": 74,
          "values": {}
        },
        "inc_last_modified_date": {
          "id": 52,
          "values": {}
        },
        "on_close_multiselect": {
          "id": 625,
          "values": {}
        },
        "internal_customizations_field": {
          "id": 196,
          "values": {}
        },
        "on_close_bool": {
          "id": 623,
          "values": {}
        },
        "discovered_date": {
          "id": 50,
          "values": {}
        },
        "df_host": {
          "id": 192,
          "values": {}
        },
        "ny_impact_likely": {
          "id": 46,
          "values": {}
        },
        "data_contained": {
          "id": 44,
          "values": {}
        },
        "gdpr_final_assessment": {
          "id": 38,
          "values": {}
        },
        "df_inc_id": {
          "id": 194,
          "values": {}
        },
        "custom_text": {
          "id": 394,
          "values": {}
        },
        "gdpr_identification": {
          "id": 34,
          "values": {}
        },
        "exposure_vendor_id": {
          "id": 13,
          "values": {}
        },
        "name": {
          "id": 17,
          "values": {}
        },
        "creator_id": {
          "id": 68,
          "values": {
            "3": {
              "default": False,
              "enabled": True,
              "hidden": False,
              "label": "Resilient Sysadmin (a@example.com)",
              "properties": None,
              "uuid": "ec5f0df2-132a-46f5-8ec1-08dbfaaf59c9",
              "value": 3
            }
          }
        },
        "crimestatus_id": {
          "id": 60,
          "values": {
            "5": {
              "default": False,
              "enabled": True,
              "hidden": False,
              "label": "Unknown",
              "properties": None,
              "uuid": None,
              "value": 5
            }
          }
        },
        "negative_pr_likely": {
          "id": 57,
          "values": {}
        },
        "employee_involved": {
          "id": 59,
          "values": {}
        },
        "alberta_health_risk_assessment": {
          "id": 41,
          "values": {}
        },
        "org_handle": {
          "id": 73,
          "values": {
            "201": {
              "default": False,
              "enabled": True,
              "hidden": False,
              "label": "resilient",
              "properties": {
                "configuration_type": "standard"
              },
              "uuid": None,
              "value": 201
            }
          }
        },
        "plan_status": {
          "id": 11,
          "values": {
            "A": {
              "default": False,
              "enabled": True,
              "hidden": False,
              "label": "Active",
              "properties": None,
              "uuid": None,
              "value": "A"
            }
          }
        },
        "end_date": {
          "id": 67,
          "values": {}
        },
        "gdpr_breach_type_comment": {
          "id": 31,
          "values": {}
        },
        "determined_date": {
          "id": 51,
          "values": {}
        },
        "pipeda_overall_assessment": {
          "id": 28,
          "values": {}
        },
        "gdpr_final_assessment_comment": {
          "id": 39,
          "values": {}
        },
        "city": {
          "id": 7,
          "values": {}
        },
        "gdpr_personal_data_comment": {
          "id": 33,
          "values": {}
        },
        "description": {
          "id": 15,
          "values": {}
        },
        "phase_id": {
          "id": 19,
          "values": {
            "1005": {
              "default": False,
              "enabled": True,
              "hidden": False,
              "label": "Respond",
              "properties": None,
              "uuid": "ebad851d-5b5e-4d19-af79-fae53cc1f659",
              "value": 1005
            }
          }
        },
        "gdpr_harm_risk": {
          "id": 71,
          "values": {}
        },
        "confirmed": {
          "id": 14,
          "values": {}
        },
        "custom_select": {
          "id": 475,
          "values": {}
        },
        "data_compromised": {
          "id": 3,
          "values": {}
        },
        "harmstatus_id": {
          "id": 56,
          "values": {
            "2": {
              "default": False,
              "enabled": True,
              "hidden": False,
              "label": "Unknown",
              "properties": None,
              "uuid": None,
              "value": 2
            }
          }
        },
        "gdpr_personal_data": {
          "id": 32,
          "values": {}
        },
        "data_source_ids": {
          "id": 12,
          "values": {}
        },
        "pipeda_other_factors": {
          "id": 26,
          "values": {}
        },
        "gdpr_identification_comment": {
          "id": 35,
          "values": {}
        },
        "gdpr_breach_circumstances": {
          "id": 29,
          "values": {}
        },
        "addr": {
          "id": 6,
          "values": {}
        },
        "start_date": {
          "id": 61,
          "values": {}
        },
        "data_format": {
          "id": 20,
          "values": {}
        },
        "exposure_individual_name": {
          "id": 54,
          "values": {}
        },
        "exposure_dept_id": {
          "id": 8,
          "values": {}
        },
        "custom_number": {
          "id": 473,
          "values": {}
        },
        "pipeda_other_factors_comment": {
          "id": 25,
          "values": {}
        },
        "pipeda_probability_of_misuse_comment": {
          "id": 23,
          "values": {}
        },
        "inc_training": {
          "id": 65,
          "values": {}
        },
        "due_date": {
          "id": 70,
          "values": {}
        },
        "resolution_summary": {
          "id": 64,
          "values": {}
        },
        "reporter": {
          "id": 10,
          "values": {}
        },
        "pipeda_sensitivity_of_pi": {
          "id": 22,
          "values": {}
        },
        "df_org_id": {
          "id": 195,
          "values": {}
        },
        "gdpr_breach_type": {
          "id": 30,
          "values": {}
        },
        "exposure_type_id": {
          "id": 5,
          "values": {
            "1": {
              "default": False,
              "enabled": True,
              "hidden": False,
              "label": "Unknown",
              "properties": None,
              "uuid": None,
              "value": 1
            }
          }
        },
        "pipeda_sensitivity_of_pi_comment": {
          "id": 21,
          "values": {}
        },
        "gdpr_consequences_comment": {
          "id": 37,
          "values": {}
        },
        "nist_attack_vectors": {
          "id": 2,
          "values": {}
        },
        "wa_impact_likely": {
          "id": 48,
          "values": {}
        },
        "cust_bool": {
          "id": 476,
          "values": {}
        },
        "jurisdiction_name": {
          "id": 1,
          "values": {}
        },
        "pipeda_overall_assessment_comment": {
          "id": 27,
          "values": {}
        }
      },
      "type_id": 0
    }

TYPE_INFO = ActionMessageTypeInfo(0, TYPE_INFO_MAP, None)


class TestDataFeederSyncIncidents:
    """ Tests for the data_feeder_sync_incidents function"""

    @pytest.mark.parametrize("typeinfo, field, value, expected_result", [
        (None, {'input_type': 'text'}, None, None),
        (None, {'input_type': 'text'}, "abc", "abc"),
        (None, {'input_type': 'bool'}, False, False),
        (None, {'input_type': 'text'}, ["abc","def"], "abc, def"),
        (None, {'input_type': 'textarea'}, {"content": "abc"}, "abc"),
        (None, {'input_type': 'number'}, {"id": 5}, 5),
        (None, {'input_type': 'datepicker'}, 1607107208000, "2020-12-04T18:40:08"),
        (None, {'input_type': 'datetimepicker'}, 1607107208000, "2020-12-04T18:40:08+00:00"),
        (None, {'input_type': 'datetimepicker'}, 1607107208000, "2020-12-04T18:40:08+00:00")
    ])
    def test_success(self, typeinfo, field, value, expected_result):
        result_value = TypeInfo.translate_value(typeinfo, field, value)
        assert(result_value == expected_result)
