# -*- coding: utf-8 -*-
import copy

from fn_google_cloud_scc.lib.scc_common import GoogleSCCCommon
from google.cloud import securitycenter

config_data = {
    "google_application_credentials_path":"fake/path",
    "google_cloud_organization_id":123456789,
    "google_cloud_base_url": "https://console.cloud.google.com",
    "findings_filter":None,
    "polling_interval":10,
    "polling_lookback":120,
}

config_data_str = """[fn_google_cloud_scc]
google_application_credentials_path="fake/path"
google_cloud_organization_id=123456789
google_cloud_base_url=https://console.cloud.google.com
findings_filter=
polling_interval=10
polling_lookback=120
"""


findings = [{
    "finding": {
      "name": "organizations/<org_id>/sources/<source_id>/findings/<finding_id>",
      "parent": "organizations/<org_id>/sources/<source_id>",
      "resource_name": "//container.googleapis.com/<resource_path>",
      "state": "INACTIVE",
      "category": "LEGACY_AUTHORIZATION_ENABLED",
      "external_uri": "https://console.cloud.google.com/link_to_solution",
      "source_properties": {
        "compliance_standards": {
          "pci": [
            {
              "ids": [
                "4.1"
              ]
            }
          ],
          "cis": [
            {
              "ids": [
                "7.3"
              ],
              "version": "1.0"
            },
            {
              "version": "1.0",
              "ids": [
                "6.8.3"
              ]
            }
          ]
        },
        "ReactivationCount": 0.0,
        "ResourcePath": [
          "projects/<project_name>/",
          "organizations/<org_id>/"
        ],
        "Recommendation": "recommendation. follow link: https://example.com/dot_at_end_not_included.",
        "ScannerName": "CONTAINER_SCANNER",
        "ExceptionInstructions": "exception",
        "Explanation": "explanation",
        "DeactivationReason": "The issue has been remediated."
      },
      "security_marks": {
        "name": "organizations/<org_id>/sources/<source_id>/findings/<finding_id>/securityMarks",
        "marks": {
          "IBM_SOAR_ID": "2190",
          "UP": "DATE"
        },
        "canonical_name": ""
      },
      "severity": "HIGH",
      "canonical_name": "projects/<project_id>/sources/<source_id>/findings/<finding_id>",
      "mute": "UNDEFINED",
      "finding_class": "MISCONFIGURATION",
      "description": "description",
      "external_systems": {},
      "connections": [],
      "mute_initiator": "",
      "iam_bindings": [],
      "next_steps": ""
    },
    "resource": {
      "name": "//container.googleapis.com/<resource-path>",
      "project_name": "//cloudresourcemanager.googleapis.com/projects/<project_id>",
      "project_display_name": "<project_display_name>",
      "parent_name": "//cloudresourcemanager.googleapis.com/projects/<project_id>",
      "parent_display_name": "<project_display_name>",
      "type_": "google.container.Cluster",
      "display_name": "<resource_name>",
      "folders": []
    },
    "state_change": "UNUSED"
}]

assets = [
  {
    "asset": {
      "link": "https://console.cloud.google.com/security/command-center/assets?organizationId=<org_id>&resourceId=<resource_name>",
      "name": "organizations/259357470209/assets/11712294571846742175",
      "security_center_properties": {
        "resource_name": "//cloudresourcemanager.googleapis.com/projects/216150104097",
        "resource_type": "google.cloud.resourcemanager.Project",
        "resource_parent": "//cloudresourcemanager.googleapis.com/organizations/259357470209",
        "resource_project": "//cloudresourcemanager.googleapis.com/projects/216150104097",
        "resource_owners": [
          "user:<user>"
        ],
        "resource_display_name": "<project>",
        "resource_parent_display_name": "<name>",
        "resource_project_display_name": "<project>",
        "folders": []
      },
      "resource_properties": {
        "projectNumber": "216150104097",
        "name": "<project>",
        "lifecycleState": "ACTIVE",
        "projectId": "<project>",
        "createTime": "2022-05-24T16:13:28.44Z",
        "parent": "{\"id\":\"259357470209\",\"type\":\"organization\"}"
      },
      "security_marks": {
        "name": "organizations/259357470209/assets/11712294571846742175/securityMarks",
        "marks": {},
        "canonical_name": ""
      },
      "create_time": "2022-05-24T16:36:54.136Z",
      "update_time": "2022-06-15T15:04:11.754Z",
      "iam_policy": {
        "policy_blob": "<policy_blob>"
      },
      "canonical_name": "projects/216150104097/assets/11712294571846742175"
    },
    "state_change": "UNUSED"
  },
  {
    "asset": {
      "link": "https://console.cloud.google.com/security/command-center/assets?organizationId=<org_id>&resourceId=<resource_name>",
      "name": "organizations/259357470209/assets/3331741957707965158",
      "security_center_properties": {
        "resource_name": "//compute.googleapis.com/projects/9048930534532860994",
        "resource_type": "google.compute.Project",
        "resource_parent": "//cloudresourcemanager.googleapis.com/projects/216150104097",
        "resource_project": "//cloudresourcemanager.googleapis.com/projects/216150104097",
        "resource_owners": [
          "user:<user>"
        ],
        "resource_display_name": "<project>",
        "resource_parent_display_name": "<name>",
        "resource_project_display_name": "<project>",
        "folders": []
      },
      "resource_properties": {
        "defaultServiceAccount": "216150104097-compute@developer.gserviceaccount.com",
        "xpnProjectStatus": "UNSPECIFIED_XPN_PROJECT_STATUS",
        "name": "<project>",
        "defaultNetworkTier": "PREMIUM",
        "creationTimestamp": "2022-06-15T07:54:37.897-07:00",
        "kind": "compute#project",
        "selfLink": "https://www.googleapis.com/compute/v1/projects/<project>",
        "id": "9048930534532860994"
      },
      "security_marks": {
        "name": "organizations/259357470209/assets/3331741957707965158/securityMarks",
        "marks": {},
        "canonical_name": ""
      },
      "create_time": "2022-06-15T14:54:38.794Z",
      "update_time": "2022-06-15T14:54:38.794Z",
      "iam_policy": {
        "policy_blob": ""
      },
      "canonical_name": "projects/216150104097/assets/3331741957707965158"
    },
    "state_change": "UNUSED"
  }
]


updated_findings = [{
    "finding": {
      "name": "organizations/<org_id>/sources/<source_id>/findings/<finding_id>",
      "parent": "organizations/<org_id>/sources/<source_id>",
      "resource_name": "//container.googleapis.com/<resource_path>",
      "state": "INACTIVE",
      "category": "LEGACY_AUTHORIZATION_ENABLED",
      "external_uri": "https://console.cloud.google.com/link_to_solution",
      "source_properties": {
        "compliance_standards": {
          "pci": [
            {
              "ids": [
                "4.1"
              ]
            }
          ],
          "cis": [
            {
              "ids": [
                "7.3"
              ],
              "version": "1.0"
            },
            {
              "version": "1.0",
              "ids": [
                "6.8.3"
              ]
            }
          ]
        },
        "ReactivationCount": 0.0,
        "ResourcePath": [
          "projects/<project_name>/",
          "organizations/<org_id>/"
        ],
        "Recommendation": "recommendation. follow link: https://example.com/dot_at_end_not_included.",
        "ScannerName": "CONTAINER_SCANNER",
        "ExceptionInstructions": "exception",
        "Explanation": "explanation",
        "DeactivationReason": "The issue has been remediated."
      },
      "security_marks": {
        "name": "organizations/<org_id>/sources/<source_id>/findings/<finding_id>/securityMarks",
        "marks": {
          "IBM_SOAR_ID": "2190",
          "UP": "DATE"
        },
        "canonical_name": ""
      },
      "severity": "HIGH",
      "canonical_name": "projects/<project_id>/sources/<source_id>/findings/<finding_id>",
      "mute": "UNDEFINED",
      "finding_class": "MISCONFIGURATION",
      "description": "description",
      "external_systems": {},
      "connections": [],
      "mute_initiator": "",
      "iam_bindings": [],
      "next_steps": "Nothing to do next"
    },
    "resource": {
      "name": "//container.googleapis.com/<resource-path>",
      "project_name": "//cloudresourcemanager.googleapis.com/projects/<project_id>",
      "project_display_name": "<project_display_name>",
      "parent_name": "//cloudresourcemanager.googleapis.com/projects/<project_id>",
      "parent_display_name": "<project_display_name>",
      "type_": "google.container.Cluster",
      "display_name": "<resource_name>",
      "folders": []
    },
    "state_change": "UNUSED"
}]

class MockSecurityCenterClient():

    @classmethod
    def from_service_account_file(cls, *_args, **_kwargs):
        return cls()

    @staticmethod
    def list_findings(request, *_args, **_kwargs):
        assert "parent" in request
        # have to make a deep copy to allow for parallel processing here
        return copy.deepcopy(findings)

    @staticmethod
    def update_security_marks(request, *_args, **_kwargs):
        return request.get("security_marks")


def to_dict(finding, *_args, **_kwargs):
    return finding
