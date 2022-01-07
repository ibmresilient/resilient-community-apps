# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

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

All_BLOCKLIST_URL = "settings/GetAllModelBlackRecords"
FILTERED_BLOCKLIST_URL = "settings/GetBlackListDetails"
ADDUPDATE_BLOCKLIST_URL = "settings/AddOrUpdateModelBlackRecords"

ALL_CUSTOMLIST_URL = "settings/GetTrackingListRecords"
ADDUPDATE_CUSTOMLIST_URL = "settings/AddOrUpdateTrackingListRecords"

CREATE_ENTITY_URL = "cases/CreateCaseEntity"
CREATE_COMMENT_URL = "cases/AddCaseComment"
CREATE_INSIGHT_URL = "cases/CreateCaseInsight"
CREATE_ARTIFACT_URL = "cases/CreateCaseEntity"
CREATE_ATTACHMENT_URL = "cases/AddEvidence"
CREATE_TASK_URL = "cases/AddOrUpdateCaseTask"
CLOSE_CASE = "cases/CloseCase"
SEARCH_CASE_URL = "search/CaseSearchEverything"
CASES_MODIFIED_URL = "cases/IsCaseUpdated"
GET_VERSION_URL = "settings/GetSystemVersion"

SOAR_HEADER = "IBM SOAR"
SIEMPLIFY_HEADER="From Siemplify"
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

        results, error_msg = self._make_call("POST", CREATE_CASE_URL, incident_payload)
        if isinstance(results, int) and incident_info['description']:
            _description_results, _ = self.update_case_description(results, incident_info['description'])

        return results, error_msg

    def update_case(self, incident_info):
        # get the existing case to start reviewing changes
        self._diff_case_info(incident_info)

        # TODO

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
        # TODO

    def get_blocklist(self, inputs):

        if inputs.get("siemplify_search"):
            payload = {
                "searchTerm": inputs.get("siemplify_search"),
                "requestedPage": 0,
                "pageSize": str(inputs.get("siemplify_limit", 100))
            }
            return self._make_call("POST", FILTERED_BLOCKLIST_URL, payload)
        else:
            return self._make_call("GET", All_BLOCKLIST_URL)

    def add_update_blocklist(self, inputs):

        payload = {
            "entityIdentifier": inputs['siemplify_artifact_value'],
            "entityType": ARTIFACT_TYPE_LOOKUPS.get(inputs['siemplify_artifact_type'], "GENERICENTITY"),
            "scope": 2,
            "environments": inputs['siemplify_environment']
        }

        result, error_msg = self._make_call("POST", ADDUPDATE_BLOCKLIST_URL, payload) # return blank if successful
        return payload if not error_msg else result, error_msg

    def get_customlist(self):
        return self._make_call("GET", ALL_CUSTOMLIST_URL)

    def add_update_customlist(self, inputs):
        category = inputs.get('siemplify_category') if inputs.get('siemplify_category') else \
            ARTIFACT_TYPE_LOOKUPS.get(inputs['siemplify_artifact_type'], "GENERICENTITY")

        payload = {
            "entityIdentifier": inputs['siemplify_artifact_value'],
            "category": category,
            "environments": inputs['siemplify_environment']
        }

        result, error_msg = self._make_call("POST", ADDUPDATE_CUSTOMLIST_URL, payload) # return blank if successful
        return payload if not error_msg else result, error_msg

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

        results, error_msg = self._make_call("POST", CREATE_INSIGHT_URL, payload)
        return results if isinstance(results, dict) else {}, error_msg

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

    def get_version(self):
        return self._make_call("GET", GET_VERSION_URL)

    def is_case_modified(self, case_id, modified_ts):
        payload = {
            "caseId": str(case_id),
            "currentModificationTimeUnixTimeInMs": str(modified_ts)
        }

        LOG.debug(payload)

        return self._make_call("POST", CASES_MODIFIED_URL, payload)

    def _make_call(self, method, uri, payload=None, ):

        url = "/".join([self.base_url, API_VERSION, uri])
        if payload:
            response, error_msg = self.rc.execute(method,
                                                  url,
                                                  data=json.dumps(payload),
                                                  headers=self.headers,
                                                  verify=self.verify,
                                                  callback=callback)
        else:
            response, error_msg = self.rc.execute(method,
                                                  url,
                                                  headers=self.headers,
                                                  verify=self.verify,
                                                  callback=callback)

        try:
            return response.json(), error_msg
        except JSONDecodeError:
            return response.text, error_msg


def _make_headers(api_key):
    return {
        "Content-Type": "application/json",
        "AppKey": api_key
    }

def callback(response):
    """
    callback needed for certain REST API calls to return a formatted error message
    :param response:
    :return: response, error_msg
    """
    error_msg = None
    if response.status_code < 300 or response.status_code == 2000:
        return response, None
    else:
        resp = response.json()
        msg = resp['ErrorMessage']
        error_msg  = u"Siemplify Error: \n    status code: {0}\n    failure: {1}".format(response.status_code, msg)

        return response, error_msg
