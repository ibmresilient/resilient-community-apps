# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.

import logging
import json
from .jinja_common import JinjaEnvironment
from resilient_lib import clean_html
from simplejson.errors import JSONDecodeError

LOG = logging.getLogger(__name__)

PACKAGE_NAME = "fn_siemplify"

DEFAULT_CREATE_CASE = "templates/siemplify_create_case.jinja"

API_VERSION = "api/external/v1"
CREATE_CASE_URL = "cases/CreateManualCase"
UPDATE_CASE_DESCRIPTION_URL = "cases/ChangeCaseDescription"
GET_CASE_URL = "cases/GetCaseFullDetails/{}"
BLOCKLIST_URL = "settings/GetAllModelBlackRecords"
CREATE_ENTITY_URL = "cases/CreateCaseEntity"
CREATE_COMMENT_URL = "cases/AddCaseComment"
CREATE_INSIGHT_URL = "cases/CreateCaseInsight"
CREATE_ARTIFACT_URL = "cases/CreateCaseEntity"
CREATE_ATTACHMENT_URL = "cases/AddEvidence"
CREATE_TASK_URL = "cases/AddOrUpdateCaseTask"
CLOSE_CASE = "cases/CloseCase"
SEARCH_CASE_URL = "search/CaseSearchEverything"

SOAR_HEADER = "IBM SOAR"
IBMSOAR_TAGS = ['IBMSOAR']

ARTIFACT_TYPE_LOOKUPS = {
    "Port": "ADDRESS",
    "MAC Address": "MacAddress",
    "Process Name": "PROCESS",
    "Service": "PROCESS",
    "File Name": "FILENAME",
    "File Path": "FILENAME",
    "Malware MD5 Hash": "FILEHASH",
    "Malware SHA-1 Hash": "FILEHASH",
    "Malware SHA-256 Hash": "FILEHASH",
    "Malware Sample Fuzzy Hash": "FILEHASH",
    "URI PATH": "DestinationURL",
    "URL": "DestinationURL",
    "URL Referer": "DestinationURL",
    "Email Subject": "EMAILSUBJECT",
    "Threat CVE ID": "CVEID",
    "String": "GENERICENTITY",
    "DNS Name": "DESTINATIONDOMAIN",
    "IP Address": "IPSET",
    "User Agent": "USERUNIQNAME",
    "User Account": "USERUNIQNAME",
    "Registry Key": "GENERICENTITY",
    "Password" : "GENERICENTITY",
    "Observed Data": "GENERICENTITY",
    "Network CIDR Range": "IPSET",
    "Mutex": "THREATSIGNATURE",
    "Malware Family/Variant": "GENERICENTITY",
    "HTTP Response Header": "GENERICENTITY",
    "HTTP Request Header": "GENERICENTITY",
    "Email Sender Name": "USERUNIQNAME",
    "Email Sender": "USERUNIQNAME",
    "Email Recipient": "USERUNIQNAME",
    "Email Body": "GENERICENTITY",
    "Email Attachment Name": "FILENAME",
    "Email Attachment": None,
    "Log File": None,
    "Malware Sample": None,
    "Other File": None,
    "RFC 822 Email Message File": None,
    "X509 Certificate File": None
}


class SiemplifyCommon():
    def __init__(self, rc, options):
        self.options = options._asdict() if isinstance(options, tuple) else options
        self.base_url = self.options.get('base_url')
        self.api_key = self.options.get('api_key')

        self.headers = _make_headers(self.api_key)
        self.jina_env = JinjaEnvironment()
        self.rc = rc
        self.verify = False if self.options.get('cafile').lower() == "false" else self.options.get('cafile')

    def sync_case(self, incident_info):
        # perform an update to an existing incident
        if incident_info.get('siemplify_case_id'):
            return self.update_case(incident_info)

        return self.create_case(incident_info)

    def create_case(self, incident_info):
        incident_payload = self.jina_env.make_payload_from_template(
            self.options.get('siemplify_create_case_template'),
            DEFAULT_CREATE_CASE,
            incident_info)

        results = self._make_call("POST", CREATE_CASE_URL, incident_payload)
        if isinstance(results, int) and incident_info['description']:
            _description_results = self.update_case_description(results, incident_info['description'])

        return results

    def update_case(self, incident_info):
        # get the existing case to start reviewing changes
        self._diff_case_info(incident_info)

        #_diff_comments(incident_info)

        #_diff_attachments(incident_info)
        return None

    def get_case(self, case_id):
        uri = GET_CASE_URL.format(case_id)
        return self._make_call("GET", uri)

    def get_cases(self, case_list):
        payload = {
            "tags": IBMSOAR_TAGS,
            "title": "Caseids:{}".format(",".join(case_list)),
            "requestedPage": 0,
            "timeRangeFilter": 0
        }
        LOG.debug(payload)

        return self._make_call("POST", SEARCH_CASE_URL, payload)

    def close_case(self, inputs):
        payload = {
            "caseId": str(inputs.get('siemplify_case_id')),
            "alertIdentifier": inputs.get('siemplify_alert_id'),
            "rootCause": inputs.get('siemplify_root_cause'),
            "reason": inputs.get('siemplify_reason'),
            "comment": inputs.get('siemplify_comment') if inputs.get('siemplify_comment') else "Closed by {}".format(SOAR_HEADER)
        }

        return self._make_call("POST", CLOSE_CASE, payload)

    def update_case_description(self, case_id, description):
        payload = {
            "caseId": case_id,
            "description": description.replace('"', '\\"')
        }
        LOG.debug(payload)

        return self._make_call("POST", UPDATE_CASE_DESCRIPTION_URL, payload)

    def _diff_case_info(self, incident_info):
        # get the existing case
        case_info = self.get_case(incident_info["siemplify_case_id"])
        LOG.info(case_info)

    def get_blocklist(self):
        return self._make_call("GET", BLOCKLIST_URL)

    def sync_comment(self, inputs):
        """[summary]

        Args:
            inputs ([dict]): [data to create a comment]

        """
        payload = {
            "caseId": str(inputs['siemplify_case_id']),
            "alertIdentifier": inputs.get('siemplify_alert_id'),
            "comment": "{}\n{}".format(SOAR_HEADER, inputs['siemplify_comment'])
        }

        return self._make_call("POST", CREATE_COMMENT_URL, payload)

    def sync_insight(self, inputs):
        """[summary]

        Args:
            inputs ([dict]): [data to create a comment]

        """
        payload = {
            "caseId": str(inputs['siemplify_case_id']),
            "alertIdentifier": inputs.get('siemplify_alert_id'),
            "triggeredBy": SOAR_HEADER,
            "title": SOAR_HEADER,
            "content": clean_html(inputs['siemplify_comment']),
        }

        results = self._make_call("POST", CREATE_INSIGHT_URL, payload)
        return results if isinstance(results, dict) else {}
        """
        {
            "caseId": "<long>",
            "isFavorite": "<boolean>",
            "alertIdentifier": "<string>",
            "triggeredBy": "<string>",
            "title": "<string>",
            "content": "<string>",
            "entityIdentifier": "<string>",
            "severity": 2,
            "type": 0,
            "additionalDataType": 1,
            "additionalData": "<string>",
            "additionalDataTitle": "<string>",
            "originalRequestingUser": "<string>",
            "id": "<long>",
            "creationTimeUnixTimeInMs": "<long>",
            "modificationTimeUnixTimeInMs": "<long>"
        }
        """

    def sync_artifact(self, inputs):
        """[summary]

        Args:
            inputs ([dict]): [data to create a comment]

        """
        siemplify_entity_type = ARTIFACT_TYPE_LOOKUPS.get(inputs['siemplify_artifact_type'])
        if not siemplify_entity_type:
            LOG.warning("No matching entity type for Artifact type: %s, value: %s",
                    inputs['siemplify_artifact_type'], inputs['siemplify_artifact_value'])
            return None

        payload = {
            "caseId": inputs['siemplify_case_id'],
            "alertIdentifier": inputs['siemplify_alert_id'],
            "entities": [
                {
                "caseId": 0,
                "identifier": inputs['siemplify_artifact_value'],
                "entityType": siemplify_entity_type,
                "isInternal": True,
                "isSuspicious": False,
                "isArtifact": True,
                "isEnriched": False,
                "isVulnerable": False,
                "isPivot": False,
                "environment": inputs['siemplify_environment'],
                "fields": [
                    {
                    "isHighlight": False,
                    "groupName": "Default",
                    "items": [
                        {
                        "originalName": "Type",
                        "name": "Type",
                        "value": siemplify_entity_type
                        },
                        {
                        "originalName": "IsInternalAsset",
                        "name": "IsInternalAsset",
                        "value": "True"
                        },
                        {
                        "originalName": "IsSuspicious",
                        "name": "IsSuspicious",
                        "value": "False"
                        },
                        {
                        "originalName": "IsEnriched",
                        "name": "IsEnriched",
                        "value": "False"
                        },
                        {
                        "originalName": "IsVulnerable",
                        "name": "IsVulnerable",
                        "value": "False"
                        },
                        {
                        "originalName": "IsArtifact",
                        "name": "IsArtifact",
                        "value": "True"
                        },
                        {
                        "originalName": "IsManuallyCreated",
                        "name": "IsManuallyCreated",
                        "value": "True"
                        },
                        {
                        "originalName": "Environment",
                        "name": "Environment",
                        "value": inputs['siemplify_environment']
                        }
                    ]
                    },
                    {
                    "isHighlight": False,
                    "groupName": "Entity",
                    "items": [
                        {
                        "originalName": "IsPivot",
                        "name": "Is Pivot",
                        "value": "False"
                        }
                    ]
                    }
                ],
                "isManuallyCreated": True,
                "isCustom": True,
                "id": "{}_{}".format(inputs['siemplify_artifact_value'].replace(' ', '_'), inputs['siemplify_environment'])
                }
            ]
        }

        return self._make_call("POST", CREATE_ARTIFACT_URL, payload)

    def sync_attachment(self, case_id, b64content, filename, isImportant=False):
        filetype = None
        if '.' in filename:
            filetype = filename[filename.find('.'): ]
            filename = filename[: filename.find('.')]

        #  "AlertIdentifier": alert_id,
        payload = {
            "caseIdentifier": str(case_id),
            "base64Blob": b64content,
            "name": filename,
            "description": "created by IBM SOAR",
            "isImportant": isImportant
        }
        if filetype:
            payload['type'] = filetype

        return self._make_call("POST", CREATE_ATTACHMENT_URL, payload)

    def sync_task(self, siemplify_case_id, siemplify_task_assignee,
                  siemplify_task_id, task_info):
        """[summary]

        Args:
            simplify_case_id ([int]): [description]
            siemplify_task_assignee ([str]): [description]
            siemplify_task_id ([str]): [description]
            task_info ([dict]): [description]
        """
        """ siemplify task
        {
            "caseId": "<long>",
            "priority": "<integer>",
            "isImportant": "<boolean>",
            "status": "<integer>",
            "ownerComment": "<string>",
            "name": "<string>",
            "creatorUserId": "<string>",
            "owner": "<string>",
            "dueDateUnixTimeMs": "<long>",
            "completionComment": "<string>",
            "completionUnixTimeMs": "<long>",
            "isFavorite": "<boolean>",
            "alertIdentifier": "<string>",
            "id": "<long>",
            "creationTimeUnixTimeInMs": "<long>",
            "modificationTimeUnixTimeInMs": "<long>"
        }
        """
        """SOAR Task
        {
            "name": "my task",
            "inc_id": 2298,
            "inc_owner_id": 3,
            "due_date": null,
            "required": true,
            "owner_id": null,
            "user_notes": "",
            "status": "O",
            "frozen": false,
            "owner_fname": null,
            "owner_lname": null,
            "init_date": 1639515019386,
            "active": true,
            "src_name": null,
            "inc_name": "sync27",
            "instr_text": "<div class=\"rte\"><div>this is the content</div></div>",
            "instructions": {
                "format": "html",
                "content": "<div class=\"rte\"><div>this is the content</div></div>"
            },
            "form": null,
            "members": null,
            "perms": {
            },
            "notes": [

            ],
            "closed_date": null,
            "actions": [
            ],
            "phase_id": 1002,
            "category_id": null,
            "notes_count": 2,
            "attachments_count": 0,
            "task_layout": [

            ],
            "auto_deactivate": true,
            "creator_principal": {
                "id": 3,
                "type": "user",
                "name": "a@example.com",
                "display_name": "Resilient Sysadmin"
            },
            "regs": {

            },
            "custom": true,
            "id": 1552,
            "inc_training": false,
            "cat_name": "Initial",
            "description": null,
            "at_id": null,
            "private": null
            }
        """

        payload = {
            "caseId": siemplify_case_id,
            "owner": siemplify_task_assignee,
            "name": "IBM SOAR: {}".format(task_info['name']),
            "dueDateUnixTimeMs": task_info.get('due_date'),
            "ownerComment": task_info.get('instr_text'),
        }
        if siemplify_task_id:
            payload['id'] = siemplify_task_id

        LOG.debug(payload)

        return self._make_call("POST", CREATE_TASK_URL, payload)

    def _make_call(self, method, uri, payload=None):

        url = "/".join([self.base_url, API_VERSION, uri])
        if payload:
            response = self.rc.execute(method, url, data=json.dumps(payload), headers=self.headers, verify=self.verify)
        else:
            response = self.rc.execute(method, url, headers=self.headers, verify=self.verify)

        try:
            return response.json()
        except JSONDecodeError:
            return response.text


def _make_headers(api_key):
    return {
        "Content-Type": "application/json",
        "AppKey": api_key
    }
