# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

import logging
import json
import os
from .jinja_common import JinjaEnvironment
from resilient_lib import clean_html, IntegrationError
from simplejson.errors import JSONDecodeError

LOG = logging.getLogger(__name__)

PACKAGE_NAME = "fn_siemplify"

DEFAULT_CREATE_CASE = "templates/siemplify_create_case.jinja"
SIEMPLIFY_CREATE_ENTITY_TEMPLATE = "templates/siemplify_create_entity.jinja"

API_VERSION = "api/external/v1"

All_BLOCKLIST_URL = "settings/GetAllModelBlackRecords"
FILTERED_BLOCKLIST_URL = "settings/GetBlackListDetails"
ADDUPDATE_BLOCKLIST_URL = "settings/AddOrUpdateModelBlackRecords"
ALL_CUSTOMLIST_URL = "settings/GetTrackingListRecords"
ADDUPDATE_CUSTOMLIST_URL = "settings/AddOrUpdateTrackingListRecords"
GET_VERSION_URL = "settings/GetSystemVersion"

CREATE_CASE_URL = "cases/CreateManualCase"
UPDATE_CASE_DESCRIPTION_URL = "cases/ChangeCaseDescription"
GET_CASE_URL = "cases/GetCaseFullDetails/{}"
CREATE_ENTITY_URL = "cases/CreateCaseEntity"
CREATE_COMMENT_URL = "cases/AddCaseComment"
CREATE_INSIGHT_URL = "cases/CreateCaseInsight"
CREATE_ARTIFACT_URL = "cases/CreateCaseEntity"
CREATE_ATTACHMENT_URL = "cases/AddEvidence"
CREATE_TASK_URL = "cases/AddOrUpdateCaseTask"
CLOSE_CASE = "cases/CloseCase"
CASES_MODIFIED_URL = "cases/IsCaseUpdated"

SEARCH_CASE_URL = "search/CaseSearchEverything"

SOAR_HEADER = "IBM SOAR"
CREATED_BY_SOAR = "Created by {}".format(SOAR_HEADER)
SIEMPLIFY_HEADER="From Siemplify"
IBMSOAR_TAGS = ['IBMSOAR']

GENERICENTITY = "GENERICENTITY"

# lookup table between SOAR artifact types and Siemplify entity types
ARTIFACT_TYPE_LOOKUPS_FILE = "artifact_type_lookup.json"

class SiemplifyCommon():
    def __init__(self, rc, options):
        self.options = options._asdict() if isinstance(options, tuple) else options
        self.base_url = self.options.get('base_url')
        self.api_key = self.options.get('api_key')

        self.headers = _make_headers(self.api_key)
        self.jina_env = JinjaEnvironment()
        self.rc = rc
        self.verify = False if self.options.get('cafile').lower() == "false" else self.options.get('cafile')

        self.ARTIFACT_TYPE_LOOKUPS = self._init_artifact_type_lookup(self.options.get('artifact_type_lookup'))

    def _init_artifact_type_lookup(self, override_file):
        # Initialize the artifact type lookup file. Use an optional customer specified file
        default_lookup = os.path.join(os.path.dirname(__file__), ARTIFACT_TYPE_LOOKUPS_FILE)
        if override_file:
            if not os.path.exists(override_file):
                LOG.warning("app.config file 'artifact_type_lookup' cannot be found: %s. Using default mapping", override_file)
                lookup_file = default_lookup
            else:
                lookup_file = override_file
        else:
            lookup_file = default_lookup

        try:
            with open(lookup_file, 'r') as f:
                return json.load(f)
        except JSONDecodeError as err:
            LOG.error("Unable to use artifact type lookup file: %s. Using default mapping")
            with open(default_lookup, 'r') as f:
                return json.load(f)

    def sync_case(self, incident_info):
        # perform an update to an existing incident
        if incident_info.get('siemplify_case_id'):
            raise IntegrationError("Update Siemplify Case currently not supported")

        return self.create_case(incident_info)

    def create_case(self, incident_info):
        # create a Siemlify case with a payload of case fields
        incident_payload = self.jina_env.make_payload_from_template(
            self.options.get('siemplify_create_case_template'),
            DEFAULT_CREATE_CASE,
            incident_info)

        results, error_msg = self._make_call("POST", CREATE_CASE_URL, incident_payload)
        # The description field needs to be updated separately
        if isinstance(results, int) and incident_info['description']:
            _description_results, _ = self.update_case_description(results, incident_info['description'])

        return results, error_msg

    def get_case(self, case_id):
        # Get a specific Siemplify case based on it case_id
        uri = GET_CASE_URL.format(case_id)
        return self._make_call("GET", uri)

    def get_cases(self, case_list):
        # API call get all siemplify cases associated with a list of SOAR incidents
        payload = {
            "tags": IBMSOAR_TAGS,
            "title": "Caseids:{}".format(",".join(case_list)),
            "requestedPage": 0,
            "timeRangeFilter": 0
        }
        LOG.debug("Search case payload: %s", payload)

        return self._make_call("POST", SEARCH_CASE_URL, payload)

    def close_case(self, inputs):
        # API call to close the Siemplify case
        payload = {
            "caseId": str(inputs.get('siemplify_case_id')),
            "alertIdentifier": inputs.get('siemplify_alert_id'),
            "rootCause": inputs.get('siemplify_root_cause'),
            "reason": inputs.get('siemplify_reason'),
            "comment": inputs.get('siemplify_comment') if inputs.get('siemplify_comment') else "Closed by {}".format(SOAR_HEADER)
        }

        return self._make_call("POST", CLOSE_CASE, payload)

    def update_case_description(self, case_id, description):
        # API call to update the Siemplify case description
        payload = {
            "caseId": case_id,
            "description": description.replace('"', '\\"')
        }

        return self._make_call("POST", UPDATE_CASE_DESCRIPTION_URL, payload)

    def get_blocklist(self, inputs):
        # get the contents of the Siemlify block list
        if inputs.get("siemplify_search"):
            payload = {
                "searchTerm": inputs.get("siemplify_search"),
                "requestedPage": 0,
                "pageSize": str(inputs.get("siemplify_limit", 100))
            }
            return self._make_call("POST", FILTERED_BLOCKLIST_URL, payload)

        return self._make_call("GET", All_BLOCKLIST_URL)

    def add_update_blocklist(self, inputs):
        """[add a SOAR artifact to the block list]

        Args:
            inputs ([dict]): [all fields needed to capture the SOAR artifact]

        Returns:
            [dict]: [Results of the API call]
        """
        payload = {
            "entityIdentifier": inputs['siemplify_artifact_value'],
            "entityType": self.ARTIFACT_TYPE_LOOKUPS.get(inputs.get('siemplify_artifact_type'), GENERICENTITY),
            "scope": 2,
            "environments": inputs['siemplify_environment']
        }

        result, error_msg = self._make_call("POST", ADDUPDATE_BLOCKLIST_URL, payload) # return blank if successful
        return payload if not error_msg else result, error_msg

    def get_customlist(self):
        # get the contents of the Siemlify custom list
        return self._make_call("GET", ALL_CUSTOMLIST_URL)

    def add_update_customlist(self, inputs):
        """[add a SOAR artifact to the custom list]

        Args:
            inputs ([dict]): [all fields needed to capture the SOAR artifact]

        Returns:
            [dict]: [Results of the API call]
        """
        category = inputs.get('siemplify_category') if inputs.get('siemplify_category') else \
            self.ARTIFACT_TYPE_LOOKUPS.get(inputs.get('siemplify_artifact_type'), GENERICENTITY)

        payload = {
            "entityIdentifier": inputs['siemplify_artifact_value'],
            "category": category,
            "environments": inputs['siemplify_environment']
        }

        result, error_msg = self._make_call("POST", ADDUPDATE_CUSTOMLIST_URL, payload) # return blank if successful
        return payload if not error_msg else result, error_msg

    def sync_comment(self, inputs, header=True):
        """[Sync SOAR incident note with siemplify as a wall comment]

        Args:
            inputs ([dict]): [data to create a comment]

        Returns:
            [dict]: [Results of API call]
        """
        payload = {
            "caseId": str(inputs['siemplify_case_id']),
            "alertIdentifier": inputs.get('siemplify_alert_id'),
            "comment": "{}\n{}".format(SOAR_HEADER, inputs['siemplify_comment']) if header else inputs['siemplify_comment']
        }

        return self._make_call("POST", CREATE_COMMENT_URL, payload)

    def sync_insight(self, inputs):
        """[Sync SOAR incident note with siemplify as an insight]

        Args:
            inputs ([dict]): [data to create an insight]

        Returns:
            [dict]: [Results of API call]
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
        """[Sync a SOAR artifact with Siemplify]

        Args:
            inputs ([dict]): [fields representing the Siemplify Case ID and SOAR artifact to sync]

        Returns:
            [dict]: [Results of API call]
        """
        inputs['siemplify_entity_type'] = self.ARTIFACT_TYPE_LOOKUPS.get(inputs.get('siemplify_artifact_type'))
        if not inputs['siemplify_entity_type']:
            LOG.warning("No matching entity type for Artifact type: %s, value: %s",
                        inputs['siemplify_artifact_type'],
                        inputs['siemplify_artifact_value'])
            return None

        payload = self.jina_env.make_payload_from_template(None, SIEMPLIFY_CREATE_ENTITY_TEMPLATE, inputs)

        return self._make_call("POST", CREATE_ARTIFACT_URL, payload)

    def sync_attachment(self, case_id, b64content, filename, isImportant=False):
        """[Sync the contents of a SOAR attachment with a Siemplify case]

        Args:
            case_id ([int]): [Siemplify Case]
            b64content ([bool]): [True if content is in base64 format]
            filename ([str]): [attachment name]
            isImportant (bool, optional): [True if attachment should be set as Important]. Defaults to False.

        Returns:
            [dict]: [Results of Siemplify API call]
        """
        filetype = None
        file_info = os.path.splitext(filename)
        if file_info[1]:
            filetype = file_info[1]
            filename = file_info[0]

        #  "AlertIdentifier": alert_id,
        payload = {
            "caseIdentifier": str(case_id),
            "base64Blob": b64content,
            "name": filename,
            "description": CREATED_BY_SOAR,
            "isImportant": isImportant
        }
        if filetype:
            payload['type'] = filetype

        return self._make_call("POST", CREATE_ATTACHMENT_URL, payload)

    def sync_task(self, siemplify_case_id, siemplify_task_assignee,
                  siemplify_task_id, task_info):
        """[Sync a SOAR task with Siemply's Insight]

        Args:
            simplify_case_id ([int]): [description]
            siemplify_task_assignee ([str]): [description]
            siemplify_task_id ([str]): [description]
            task_info ([dict]): [description]
        """

        payload = {
            "caseId": siemplify_case_id,
            "owner": siemplify_task_assignee,
            "name": "{}: {}".format(SOAR_HEADER, task_info.get('name')),
            "dueDateUnixTimeMs": task_info.get('due_date'),
            "ownerComment": task_info.get('instr_text'),
        }
        if siemplify_task_id:
            payload['id'] = siemplify_task_id

        return self._make_call("POST", CREATE_TASK_URL, payload)

    def get_version(self):
        # Get the version of the Siemplify platform. Used in Selftest
        return self._make_call("GET", GET_VERSION_URL)

    def is_case_modified(self, case_id, modified_ts):
        """[make a Siemplify API call to determine if the case was modified. Only a small number of
            Siemplify fields will trigger this check]

        Args:
            case_id ([int]): [Siemplify case ID]
            modified_ts ([int]): [timestamp of when to determine if changes have been made]

        Returns:
            [bool]: [True if the case was recently modified]
        """
        payload = {
            "caseId": str(case_id),
            "currentModificationTimeUnixTimeInMs": str(modified_ts)
        }

        LOG.debug("is_case_modified payload: %s", payload)

        result, err_msg = self._make_call("POST", CASES_MODIFIED_URL, payload)
        return result if not err_msg else False

    def _make_call(self, method, uri, payload=None, ):
        # perform a Siemplify API call, returning the results of that call
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
    # return headers used for Siemply API calls
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

    resp = response.json()
    msg = resp.get('ErrorMessage', '')
    error_msg  = u"Siemplify Error: \n    status code: {0}\n    failure: {1}".format(response.status_code, msg)

    return response, error_msg
