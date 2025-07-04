# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.
# pragma pylint: disable=unused-argument, line-too-long, wrong-import-order

from cachetools import cached, TTLCache
from typing import Union
from urllib.parse import urlencode, quote
from resilient import SimpleHTTPException
from resilient_lib import IntegrationError

DATATABLE = "search_for_py2_results"

SCRIPTS_URL = "/scripts"
SCRIPTS_QUERY_PAGED_URL = "/scripts/query_paged?return_level=full&handle_format=names"
DELETE_DATATABLE_ROWS = "/incidents/{inc_id}/table_data/{dt_name}/row_data"
PLAYBOOKS_URL = "/playbooks"
WORKFLOWS_URL = "/workflows"

HEADERS = {
    "handle_format": "names"
}

SKIP_RETRY_NOT_FOUND = [404]

class SOARHelper():
    def __init__(self, rest_client):
        self.rest_client = rest_client
        self.scripts_by_uuid = None
        self.scripts_by_id = None

    @cached(cache=TTLCache(maxsize=2024, ttl=600))
    def get_scripts(self):
        script_list = self.rest_client.post(SCRIPTS_QUERY_PAGED_URL, {}, headers=HEADERS)

        script_data = script_list.get("data", [])
        # build the index by uuid
        self.scripts_by_uuid = {script.get("uuid"): script for script in script_data}
        self.scripts_by_id = {script.get("id"): script.get("uuid") for script in script_data}

        return script_data

    def get_script_by_uuid(self, script_uuid:str) -> Union[None, dict]:
        if not self.scripts_by_uuid:
            self.get_scripts()

        return self.scripts_by_uuid.get(script_uuid)

    def get_script(self, script_id: int) -> list:
        """ use the script_id to lookup the index by uuid to get the full script """
        if not self.scripts_by_id:
            self.get_scripts()

        return self.scripts_by_uuid.get(self.scripts_by_id.get(script_id))

    def put_script(self, script_id, script_json):
        url = f"{SCRIPTS_URL}/{script_id}"
        return self.rest_client.put(url, script_json)

    def get_workflows(self):
        url = f"{WORKFLOWS_URL}?handle_format=names"
        return self.rest_client.get(url)

    def get_workflow(self, workflow_id):
        try:
            url = f"{WORKFLOWS_URL}/{workflow_id}?handle_format=names"
            return self.rest_client.get(url, skip_retry=SKIP_RETRY_NOT_FOUND)
        except SimpleHTTPException as err:
            raise IntegrationError(f"Unable to locate workflow id: {workflow_id}")    

    def put_workflow(self, workflow_id, workflow_json):
        url = f"{WORKFLOWS_URL}/{workflow_id}"
        return self.rest_client.put(url, workflow_json)

    def get_playbooks(self):
        url = f"{PLAYBOOKS_URL}/query_paged?return_level=full"
        return self.rest_client.post(url, {}, headers=HEADERS)

    def get_playbook(self, playbook_id, add_headers=True):
        try:
            url = f"{PLAYBOOKS_URL}/{playbook_id}?include_contents=true"
            return self.rest_client.get(url, headers=HEADERS if add_headers else None, skip_retry=SKIP_RETRY_NOT_FOUND)
        except SimpleHTTPException as err:
            raise IntegrationError(f"Unable to locate playbook id: {playbook_id}") 

    def put_playbook(self, playbook_id, playbook_json):
        url = f"{PLAYBOOKS_URL}/{playbook_id}"
        return self.rest_client.put(url, playbook_json)

    def delete_datatable_rows(self, inc_id, datatable=DATATABLE):
        url = DELETE_DATATABLE_ROWS.format(inc_id=inc_id, dt_name=datatable)
        return self.rest_client.delete(url)
