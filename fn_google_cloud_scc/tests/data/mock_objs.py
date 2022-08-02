# -*- coding: utf-8 -*-
import copy

from fn_google_cloud_scc.util.scc_common import GoogleSCCCommon
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
