# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.
"""Function implementation"""

import logging
import traceback
from resilient_circuits import ResilientComponent, ActionMessage, handler
from resilient_lib import validate_fields
from fn_microsoft_sentinel.lib.function_common import PACKAGE_NAME, SentinelProfiles, DEFAULT_SENTINEL_INCIDENT_TEMPLATE
from fn_microsoft_sentinel.lib.sentinel_common import SentinelAPI
from fn_microsoft_sentinel.lib.jinja_common import JinjaEnvironment

CHANNEL = "fn_microsoft_sentinel"

INCIDENT_TYPE = 0

LOG = logging.getLogger(__name__)

class FeedComponent(ResilientComponent):
    """This component handles initial population of a feed and ongoing
    modifications from the associated queue."""

    def __init__(self, opts):
        super(FeedComponent, self).__init__(opts)

        try:
            self.options = opts.get(PACKAGE_NAME, {})

            self.sentinel_profiles = SentinelProfiles(opts, self.options)
            self.jinja_env = JinjaEnvironment()

            self.channel = ".".join(["actions", CHANNEL])
        except Exception as err:
            LOG.error("exception: %s", err)
            error_trace = traceback.format_exc()
            LOG.error("Traceback %s", error_trace)

    @handler()
    def _sentinel_update_incident_function(self, event, *args, **kwargs):    # pylint: disable=unused-argument
        """Ingests data of any type that can be sent to a Resilient message destination"""
        # dismiss none Action events
        if not isinstance(event, ActionMessage):
            return

        # make sure to only handle incident changes
        if event.message['object_type'] != INCIDENT_TYPE:
            return

        # get the incident data
        resilient_incident = event.message['type_info']['incident']

        validate_fields(["sentinel_profile", "sentinel_incident_id"], resilient_incident['properties'])

        # Get the function parameters:
        sentinel_profile = resilient_incident['properties'].get("sentinel_profile")  # text
        sentinel_incident_id = resilient_incident['properties'].get("sentinel_incident_id")  # text

        log = logging.getLogger(__name__)
        log.info("sentinel_profile: %s", sentinel_profile)
        log.info("sentinel_incident_id: %s", sentinel_incident_id)

        sentinel_api = SentinelAPI(self.options['tenant_id'],
                                   self.options['client_id'],
                                   self.options['app_secret'],
                                   self.opts, self.options)

        profile_data = self.sentinel_profiles.get_profile(sentinel_profile)
        incident_payload = self.jinja_env.make_payload_from_template(
                                profile_data.get("update_sentinel_incident_template"),
                                DEFAULT_SENTINEL_INCIDENT_TEMPLATE,
                                resilient_incident)

        _, status, reason = sentinel_api.create_update_incident(
                                                profile_data,
                                                sentinel_incident_id,
                                                incident_payload
                                              )
        if status:
            log.info("Sentinel incident updated. incident: %s", sentinel_incident_id)
        else:
            log.error("Sentinel incident failure for incident %s: %s", sentinel_incident_id, reason)

"""
{
    "name":
    "description"
    "status": "Resolved",
    "assignedTo": "secop2@contoso.com",
    "classification": "TruePositive",
    "determination": "Malware",
    "tags": ["Yossi's playground", "Don't mess with the Zohan"]
    "labels":
}
properties.severity
properties.status
properties.title
etag
properties.classification
properties.classificationComment
properties.classificationReason
properties.description
properties.firstActivityTimeUtc
properties.labels
properties.lastActivityTimeUtc
properties.owner

"action_id": 226,
  "artifact": null,
  "attachment": null,
  "emailmessage": null,
  "incident": {
    "artifacts": null,
    "cm": {
      "geo_counts": {},
      "total": 0,
      "unassigneds": []
    },
    "dtm": {},
    "hipaa": {
      "hipaa_acquired": null,
      "hipaa_acquired_comment": null,
      "hipaa_additional_misuse": null,
      "hipaa_additional_misuse_comment": null,
      "hipaa_adverse": null,
      "hipaa_adverse_comment": null,
      "hipaa_breach": null,
      "hipaa_breach_comment": null,
      "hipaa_misused": null,
      "hipaa_misused_comment": null
    },
    "regulators": {
      "ids": []
    },
    "tasks": null,
    "actions": [],
    "addr": null,
    "admin_id": null,
    "assessment": "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>\n<assessment>\n    <rollups/>\n    <optional>There are 1 required and 0 optional tasks from 1 regulators.</optional>\n</assessment>\n",
    "city": null,
    "comments": null,
    "confirmed": false,
    "country": null,
    "create_date": 1611189405294,
    "creator": {
      "cell": "",
      "display_name": "Resilient Sysadmin",
      "email": "a@example.com",
      "fname": "Resilient",
      "id": 3,
      "is_external": false,
      "lname": "Sysadmin",
      "locked": false,
      "password_changed": false,
      "phone": "",
      "status": "A",
      "title": "",
      "ui_theme": "darkmode"
    },
    "creator_id": 3,
    "creator_principal": {
      "display_name": "Resilient Sysadmin",
      "id": 3,
      "name": "a@example.com",
      "type": "user"
    },
    "crimestatus_id": 1,
    "data_compromised": null,
    "description": "<div>some description</div>",
    "discovered_date": 1611190933000,
    "draft": false,
    "due_date": null,
    "employee_involved": null,
    "end_date": null,
    "exposure": 0,
    "exposure_dept_id": null,
    "exposure_individual_name": null,
    "exposure_type_id": 1,
    "exposure_vendor_id": null,
    "gdpr": {
      "gdpr_breach_circumstances": [],
      "gdpr_breach_type": null,
      "gdpr_breach_type_comment": null,
      "gdpr_consequences": null,
      "gdpr_consequences_comment": null,
      "gdpr_final_assessment": null,
      "gdpr_final_assessment_comment": null,
      "gdpr_identification": null,
      "gdpr_identification_comment": null,
      "gdpr_personal_data": null,
      "gdpr_personal_data_comment": null,
      "gdpr_subsequent_notification": null
    },
    "hard_liability": 0,
    "id": 4517,
    "inc_last_modified_date": 1611332924721,
    "inc_start": 1611172932000,
    "inc_training": false,
    "incident_type_ids": [],
    "is_scenario": false,
    "jurisdiction_name": null,
    "jurisdiction_reg_id": null,
    "members": [],
    "name": "Sentinel Incident - incident 2021-01-20 20:02:12.908173",
    "negative_pr_likely": null,
    "nist_attack_vectors": [],
    "org_handle": 201,
    "org_id": 201,
    "owner_id": 3,
    "perms": null,
    "phase_id": 1006,
    "pii": {
      "alberta_health_risk_assessment": null,
      "assessment": "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>\n<assessment>\n    <rollups/>\n    <optional>There are 1 required and 0 optional tasks from 1 regulators.</optional>\n</assessment>\n",
      "data_compromised": null,
      "data_contained": null,
      "data_encrypted": null,
      "data_format": null,
      "data_source_ids": [],
      "dc_impact_likely": null,
      "determined_date": 1611190933000,
      "exposure": 0,
      "gdpr_harm_risk": null,
      "gdpr_lawful_data_processing_categories": [],
      "harmstatus_id": 2,
      "impact_likely": null,
      "ny_impact_likely": null,
      "or_impact_likely": null,
      "wa_impact_likely": null
    },
    "plan_status": "A",
    "properties": {
      "grd_inc_field_source_program": null,
      "sentinel_incident_classification_reason": "",
      "high_volume_privacy_event": null,
      "grd_inc_field_high_volume_outlier": null,
      "qradar_id": null,
      "grd_inc_field_error_outlier": null,
      "sentinel_incident_assigned_to": "None",
      "sentinel_incident_id": "4bb815ba-5b84-11eb-b782-8c8590577e7a",
      "sentinel_profile": "profile_a",
      "grd_inc_field_unusual_working_hours": null,
      "grd_inc_field_server": null,
      "grd_inc_field_os_user": null,
      "sentinel_incident_url": "<a href=\"https://portal.azure.com/#asset/Microsoft_Azure_Security_Insights/Incident/subscriptions/567dddd6-80a5-42a7-b39a-b2ceba0533f4/resourceGroups/Resilient/providers/Microsoft.OperationalInsights/workspaces/Resiliient/providers/Microsoft.SecurityInsights/Incidents/4bb815ba-5b84-11eb-b782-8c8590577e7a\">Sentinel Incident</a>",
      "grd_inc_field_client_ip": null,
      "grd_inc_field_db_user": null,
      "grd_inc_field_rare_or_new_behavior": null,
      "grd_inc_field_database_type": null,
      "grd_inc_field_client_hostname": null,
      "sentinel_incident_tactics": "",
      "internal_customizations_field": null,
      "sentinel_incident_status": "New",
      "grd_inc_field_ongoing_outlier": null,
      "grd_inc_field_diverse_behavior": null,
      "sentinel_incident_classification": "",
      "grd_inc_field_confidence_score": null,
      "grd_inc_field_database": null,
      "sentinel_incident_classification_comment": "",
      "grd_inc_field_vulnerable_obj_outlier": null,
      "sentinel_incident_labels": "",
      "grd_inc_field_privileged_user": null
    },
    "regulator_risk": {},
    "reporter": null,
    "resolution_id": null,
    "resolution_summary": null,
    "sequence_code": "C815-2419",
    "severity_code": 6,
    "start_date": 1611172932000,
    "state": null,
    "task_changes": {
      "added": [],
      "removed": []
    },
    "timer_field_summarized_incident_data": [],
    "vers": 5,
    "workspace": 1,
    "zip": null
  },
  "milestone": null,
  "note": null,
  "object_type": 0,
  "operation_type": "modified",
  "principal": {
    "display_name": "Resilient Sysadmin",
    "id": 3,
    "name": "a@example.com",
    "type": "user"
  },
  "properties": {},
  "row": null,
  "task": null,
  "type_info": {
    "incident": {
      "fields": {
        "gdpr_lawful_data_processing_categories": {
          "id": 72,
          "values": {}
        },
        "owner_id": {
          "id": 58,
          "values": {
            "3": {
              "default": false,
              "enabled": true,
              "hidden": false,
              "label": "Resilient Sysadmin (a@example.com)",
              "properties": null,
              "uuid": "2143ea46-4dca-44a4-ae8f-d53462d93920",
              "value": 3
            }
          }
        },
        "impact_likely": {
          "id": 45,
          "values": {}
        },
        "sentinel_incident_id": {
          "id": 751,
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
        "sentinel_incident_url": {
          "id": 752,
          "values": {}
        },
        "id": {
          "id": 69,
          "values": {}
        },
        "state": {
          "id": 4,
          "values": {}
        },
        "grd_inc_field_rare_or_new_behavior": {
          "id": 470,
          "values": {}
        },
        "zip": {
          "id": 53,
          "values": {}
        },
        "dc_impact_likely": {
          "id": 49,
          "values": {}
        },
        "internal_customizations_field": {
          "id": 550,
          "values": {}
        },
        "inc_last_modified_date": {
          "id": 52,
          "values": {}
        },
        "discovered_date": {
          "id": 50,
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
        "sentinel_incident_status": {
          "id": 759,
          "values": {}
        },
        "sentinel_incident_classification": {
          "id": 753,
          "values": {}
        },
        "creator_id": {
          "id": 68,
          "values": {
            "3": {
              "default": false,
              "enabled": true,
              "hidden": false,
              "label": "Resilient Sysadmin (a@example.com)",
              "properties": null,
              "uuid": "2143ea46-4dca-44a4-ae8f-d53462d93920",
              "value": 3
            }
          }
        },
        "crimestatus_id": {
          "id": 60,
          "values": {
            "1": {
              "default": false,
              "enabled": true,
              "hidden": false,
              "label": "No",
              "properties": null,
              "uuid": null,
              "value": 1
            }
          }
        },
        "sentinel_incident_labels": {
          "id": 757,
          "values": {}
        },
        "plan_status": {
          "id": 11,
          "values": {
            "A": {
              "default": false,
              "enabled": true,
              "hidden": false,
              "label": "Active",
              "properties": null,
              "uuid": null,
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
        "gdpr_final_assessment_comment": {
          "id": 39,
          "values": {}
        },
        "city": {
          "id": 7,
          "values": {}
        },
        "phase_id": {
          "id": 19,
          "values": {
            "1006": {
              "default": false,
              "enabled": true,
              "hidden": false,
              "label": "Respond",
              "properties": null,
              "uuid": "ebad851d-5b5e-4d19-af79-fae53cc1f659",
              "value": 1006
            }
          }
        },
        "confirmed": {
          "id": 14,
          "values": {}
        },
        "sentinel_incident_assigned_to": {
          "id": 756,
          "values": {}
        },
        "sentinel_profile": {
          "id": 776,
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
              "default": false,
              "enabled": true,
              "hidden": false,
              "label": "Unknown",
              "properties": null,
              "uuid": null,
              "value": 2
            }
          }
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
        "start_date": {
          "id": 61,
          "values": {}
        },
        "data_format": {
          "id": 20,
          "values": {}
        },
        "grd_inc_field_database_type": {
          "id": 484,
          "values": {}
        },
        "exposure_dept_id": {
          "id": 8,
          "values": {}
        },
        "pipeda_probability_of_misuse_comment": {
          "id": 23,
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
        "grd_inc_field_confidence_score": {
          "id": 474,
          "values": {}
        },
        "pipeda_sensitivity_of_pi_comment": {
          "id": 21,
          "values": {}
        },
        "wa_impact_likely": {
          "id": 48,
          "values": {}
        },
        "pipeda_overall_assessment_comment": {
          "id": 27,
          "values": {}
        },
        "country": {
          "id": 55,
          "values": {}
        },
        "workspace": {
          "id": 9,
          "values": {
            "1": {
              "default": true,
              "enabled": true,
              "hidden": false,
              "label": "Default workspace",
              "properties": null,
              "uuid": "47350579-3795-4d7f-907f-c2d1fd329816",
              "value": 1
            }
          }
        },
        "sentinel_incident_classification_reason": {
          "id": 754,
          "values": {}
        },
        "high_volume_privacy_event": {
          "id": 693,
          "values": {}
        },
        "grd_inc_field_high_volume_outlier": {
          "id": 483,
          "values": {}
        },
        "qradar_id": {
          "id": 653,
          "values": {}
        },
        "gdpr_consequences": {
          "id": 36,
          "values": {}
        },
        "severity_code": {
          "id": 62,
          "values": {
            "6": {
              "default": false,
              "enabled": true,
              "hidden": false,
              "label": "High",
              "properties": null,
              "uuid": "93e5c99c-563b-48b9-80a3-9572307622d8",
              "value": 6
            }
          }
        },
        "data_encrypted": {
          "id": 42,
          "values": {}
        },
        "grd_inc_field_error_outlier": {
          "id": 479,
          "values": {}
        },
        "members": {
          "id": 43,
          "values": {}
        },
        "grd_inc_field_unusual_working_hours": {
          "id": 476,
          "values": {}
        },
        "or_impact_likely": {
          "id": 47,
          "values": {}
        },
        "grd_inc_field_os_user": {
          "id": 478,
          "values": {}
        },
        "grd_inc_field_client_ip": {
          "id": 473,
          "values": {}
        },
        "create_date": {
          "id": 66,
          "values": {}
        },
        "hard_liability": {
          "id": 18,
          "values": {}
        },
        "pipeda_probability_of_misuse": {
          "id": 24,
          "values": {}
        },
        "sentinel_incident_tactics": {
          "id": 758,
          "values": {}
        },
        "sequence_code": {
          "id": 74,
          "values": {}
        },
        "grd_inc_field_ongoing_outlier": {
          "id": 471,
          "values": {}
        },
        "grd_inc_field_diverse_behavior": {
          "id": 480,
          "values": {}
        },
        "gdpr_final_assessment": {
          "id": 38,
          "values": {}
        },
        "grd_inc_field_database": {
          "id": 475,
          "values": {}
        },
        "gdpr_identification": {
          "id": 34,
          "values": {}
        },
        "name": {
          "id": 17,
          "values": {}
        },
        "exposure_vendor_id": {
          "id": 13,
          "values": {}
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
              "default": false,
              "enabled": true,
              "hidden": false,
              "label": "resilient",
              "properties": {
                "configuration_type": "standard"
              },
              "uuid": null,
              "value": 201
            }
          }
        },
        "grd_inc_field_source_program": {
          "id": 469,
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
        "description": {
          "id": 15,
          "values": {}
        },
        "gdpr_personal_data_comment": {
          "id": 33,
          "values": {}
        },
        "gdpr_harm_risk": {
          "id": 71,
          "values": {}
        },
        "gdpr_personal_data": {
          "id": 32,
          "values": {}
        },
        "grd_inc_field_server": {
          "id": 482,
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
        "grd_inc_field_db_user": {
          "id": 468,
          "values": {}
        },
        "exposure_individual_name": {
          "id": 54,
          "values": {}
        },
        "grd_inc_field_client_hostname": {
          "id": 481,
          "values": {}
        },
        "pipeda_other_factors_comment": {
          "id": 25,
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
        "pipeda_sensitivity_of_pi": {
          "id": 22,
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
              "default": false,
              "enabled": true,
              "hidden": false,
              "label": "Unknown",
              "properties": null,
              "uuid": null,
              "value": 1
            }
          }
        },
        "sentinel_incident_classification_comment": {
          "id": 755,
          "values": {}
        },
        "gdpr_consequences_comment": {
          "id": 37,
          "values": {}
        },
        "grd_inc_field_vulnerable_obj_outlier": {
          "id": 472,
          "values": {}
        },
        "nist_attack_vectors": {
          "id": 2,
          "values": {}
        },
        "grd_inc_field_privileged_user": {
          "id": 477,
          "values": {}
        },
        "jurisdiction_name": {
          "id": 1,
          "values": {}
        }
      },
      "type_id": 0
    }
  },
  "user": {
    "cell": "",
    "display_name": "Resilient Sysadmin",
    "email": "a@example.com",
    "fname": "Resilient",
    "id": 3,
    "is_external": false,
    "lname": "Sysadmin",
    "locked": false,
    "password_changed": false,
    "phone": "",
    "status": "A",
    "title": "",
    "ui_theme": "darkmode"
  },
  "workflow": null,
  "workflow_instance": null
}

"""