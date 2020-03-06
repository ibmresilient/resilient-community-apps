#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2019, Mark Scherfling <mark.scherfling@ibm.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

import calendar
import io
import logging
import mimetypes
import os
import resilient
import sys
import tempfile
import time
from resilient_lib import IntegrationError, get_file_attachment, write_file_attachment
from rc_data_feed.lib.type_info import TypeInfo
from cachetools import TTLCache

CACHE_TTL = 30*60   # 30 minutes

URI_LOOKUP_BY_TYPE = {
    "incident": "/incidents",
    "artifact": "/incidents/{}/artifacts",
    "note": "/incidents/{}/comments",
    "milestone": "/incidents/{}/milestones",
    "attachment": "/incidents/{}/attachments",
    "task": "/incidents/{}/tasks",
    "tasknote": "/tasks/{}/comments"
}

class Resilient(object):
    """
    Helper class to encapsulate the Resilient API calls:
    -- create incident
    -- update incident
    -- delete incident
    -- add note
    -- add artifact
    """

    # uri's
    INCIDENT_URI = "/incidents/{}"
    COMMENT_URI = "comments"
    ARTIFACT_URI = "artifacts"
    TYPES_URI = "/types/{}"
    SYNC_DATATABLE_URI = "/incidents/{}/table_data/data_feeder_sync/row_data"
    DATATABLE = "/incidents/{}/table_data/{}/row_data"
    TASK_UPDATE = "/tasks"
    GET_INCIDENT_TASKS = "/incidents/{}/tasks"

    # sync properties for incident
    DF_INC_ID = "df_inc_id"
    DF_ORG_ID = "df_org_id"

    def __init__(self, opts, rest_client_helper=None):
        self.opts = opts
        self.types = None

        try:
            if rest_client_helper:
                self.rest_client = rest_client_helper.rest_client()
            else:
                self.rest_client = resilient.get_client(self.opts)
        except Exception as err:
            raise IntegrationError(err)

        self.cache = TTLCache(maxsize=1, ttl=CACHE_TTL)
        self.log = logging.getLogger(__name__)

    def _init_types(self):
        """
        Update an incident and datatables to include the custom definitions.
        Incident types and Artifact types and playbook Tasks are also synchronized
        :return: true/false for success
        """
        if self.rest_client:
            types_map = self.rest_client.get('/types')

            for (type_name, type_dto) in list(types_map.items()):
                pretty_type_name = TypeInfo.pretify_type_name(type_name)

                parent_types = type_dto['parent_types']

                if not pretty_type_name in self.cache:
                    self.cache[pretty_type_name] = type_dto

    def create_update_type(self, src_inc_id, src_org_id, type_name, payload, orig_id):
        """
        create a new object if it doesn't already have a mapping in the target org
        :param src_inc_id:
        :param src_org_id:
        :param type_name:
        :param payload:
        :param orig_id:
        :return:
        """

        sync_task_id, mapped_type_name = self._map_task_comment(type_name, payload, src_inc_id, src_org_id)

        # determine if we have seen this object before
        #
        sync_inc_id, sync_type_id, row_id, sync_row, sync_row_version = \
            self.find_sync_row(src_inc_id, src_org_id, mapped_type_name, orig_id)

        # update operation?
        if sync_row:
            self.log.info('updating %s(%s->%s): %s', mapped_type_name, orig_id, sync_type_id, payload)
            self.update_type(mapped_type_name, sync_inc_id, sync_type_id, sync_task_id, payload)
            # update sync row
            self.update_existing_sync_row(sync_inc_id, row_id, sync_row, sync_row_version)

        else:
            # make sure the incident already exists for child objects
            if not mapped_type_name == 'incident':
                #sync_inc_id, sync_type_id, row_id, sync_row, sync_row_version = \
                #    self.find_sync_row(src_inc_id, src_org_id, "incident", src_inc_id)
                sync_inc_id = self._find_incident(src_org_id, src_inc_id)
                if not sync_inc_id:
                    raise IntegrationError("Incident for Id {} does not exist".format(src_inc_id))

            # creating a task? may already have one created when the incident was created
            if mapped_type_name == "task":
                # Is this an unmapped task created with the incident?
                new_type_id = self._find_task(sync_inc_id, payload)
                if not new_type_id:
                    # create object
                    self.log.info('adding %s(%s): %s', type_name, orig_id, payload)
                    sync_inc_id, new_type_id = self.create_type(mapped_type_name, sync_inc_id, sync_task_id, payload)
                else:
                    self.log.info('duplicate %s(%s->%s): %s', type_name, orig_id, new_type_id, payload)

                # create sync row
                self.create_sync_row(sync_inc_id, src_inc_id, src_org_id, mapped_type_name, orig_id, new_type_id)
            else:
                if mapped_type_name == "incident":
                    self.set_sync_fields(payload, src_org_id, src_inc_id)

                # create object
                self.log.info('adding %s(%s): %s', type_name, orig_id, payload)
                sync_inc_id, new_type_id = self.create_type(mapped_type_name, sync_inc_id, sync_task_id, payload)

                # create sync row
                self.create_sync_row(sync_inc_id, src_inc_id, src_org_id, mapped_type_name, orig_id, new_type_id)


    def _find_task(self, sync_inc_id, payload):
        """
        tasks automatically created with an incident can cause duplicates from the source incident also sync'd.
        This logic will get all the sync incident tasks and make sure there isn't a duplicate
        :param sync_inc_id:
        :param payload: task payload
        :return: new_type_id: task id of found task
        """
        uri = Resilient.GET_INCIDENT_TASKS.format(sync_inc_id)
        response = self.rest_client.get(uri)

        for task in response:
            # pick a number of fields to ensure duplicate
            if task['name'] == payload['name'] and task['cat_name'] == payload['cat_name'] \
                    and task['instructions'] == payload['instructions']:
                return task['id']

        return None


    def update_type(self, mapped_type_name, sync_inc_id, sync_type_id, sync_task_id, payload):
        uri = self._get_url(sync_task_id or sync_inc_id, mapped_type_name, update_flag=True)
        # get uri to our record
        update_uri = "{}/{}".format(uri, sync_type_id)

        # get the existing record
        try:
            existing_incident = self.rest_client.get(update_uri)

            if existing_incident.get('vers', None):
                ## collect the version number
                version = existing_incident['vers']
                ## add correct version number
                payload['vers'] = version

            response = self.rest_client.put(update_uri, payload)
            self.log.debug(response)

        except Exception as e:
            self.log.error("Unable to update %s %s, Incident %s", mapped_type_name, sync_type_id, sync_inc_id)
            self.log.exception(e)

    def create_type(self, mapped_type_name, sync_inc_id, sync_task_id, payload):
        uri = self._get_url(sync_task_id or sync_inc_id, mapped_type_name)

        response = self.rest_client.post(uri, payload)
        self.log.debug(response)

        # created an incident?
        if sync_inc_id == None:
            sync_inc_id = response['id']

        # response a list?
        if isinstance(response, list):
            new_type_id = response[0]['id']  # creating a new artifact returns a list object
        else:
            new_type_id = response['id']

        return sync_inc_id, new_type_id

    def _map_task_comment(self, type_name, payload, src_inc_id, src_org_id):
        """
        task notes need a different URL
        :param type_name:
        :param payload:
        :return: "tasknote" for task notes, otherwise the original value
        """
        if type_name == "note" and payload.get("type", "") == "task":
            # get the sync_task_id for this task comment
            sync_inc_id, sync_task_id, row_id, sync_row, sync_row_version = \
                self.find_sync_row(src_inc_id, src_org_id, "task", payload.get("task_id"))

            return sync_task_id, "tasknote"
        else:
            return None, type_name

    def upload_attachment(self, src_rest_client, src_inc_id, src_org_id, type_name, payload, orig_id):
        src_artifact_id = src_attachment_id = None
        if payload.get('attachment', {}).get('content_type', None):
            src_artifact_id = orig_id
        else:
            src_attachment_id = orig_id

        # is this a task based attachment?
        if payload.get("task_id", None):
            src_task_id = payload.get("task_id")
            sync_inc_id, sync_type_id, row_id, sync_row, sync_row_version = \
                self.find_sync_row(src_inc_id, src_org_id, "task", src_task_id)
            dst_task_id = sync_type_id
        else:
            src_task_id = None
            dst_task_id = None
            # get the target incident
            sync_inc_id, sync_type_id, row_id, sync_row, sync_row_version = \
                self.find_sync_row(src_inc_id, src_org_id, "incident", src_inc_id)

        if not sync_row:
            raise IntegrationError("{} for Id {} does not exist".format(type_name, src_task_id if src_task_id else src_inc_id))
        else:
            attachment_contents = get_file_attachment(src_rest_client, src_inc_id, attachment_id=src_attachment_id,
                                                      task_id=src_task_id, artifact_id=src_artifact_id)

            if sys.version_info.major < 3:
                file_handle = io.StringIO(attachment_contents)
            else:
                file_handle = io.BytesIO(attachment_contents)

            if src_artifact_id:
                response = self.write_artifact_attachment(self.rest_client, payload['attachment']['name'], file_handle,
                                                          sync_inc_id, payload)
            else:
                response = write_file_attachment(self.rest_client, payload['name'], file_handle, sync_inc_id,
                                                 task_id=dst_task_id, content_type=payload['content_type'])

            # create sync row
            self.create_sync_row(sync_inc_id, src_inc_id, src_org_id, type_name, orig_id, response.get('id', None))

    def write_artifact_attachment(self, res_client, file_name, datastream, incident_id, payload):
        """
        call the Resilient REST API to create the attachment on incident or task

        :param res_client: required for communication back to resilient
        :param file_name: required, name of the attachment
        :param datastream: required, stream of bytes
        :param incident_id: required
        :param payload: required,
        :return: new attachment -dictionary of attachment metadata
        """

        content_type = payload['attachment'].get('content_type', None) \
                       or mimetypes.guess_type(file_name or "")[0] \
                       or "application/octet-stream"

        attachment = datastream.read()

        """
        Writing to temp path so that the REST API client can use this file path 
        to read and POST the attachment
        """

        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            try:
                temp_file.write(attachment)
                temp_file.close()

                # Create a new artifact attachment by calling resilient REST API
                artifact_uri = "{}/files".format(self._get_url(incident_id, "artifact"))

                new_attachment = res_client.post_artifact_file(artifact_uri,
                                                               payload.get("type", None),
                                                               temp_file.name,
                                                               description=payload.get("description", None),
                                                               value=file_name,
                                                               mimetype=content_type)
            finally:
                os.unlink(temp_file.name)

        if isinstance(new_attachment, list):
            new_attachment = new_attachment[0]

        return new_attachment

    def _get_url(self, inc_id, type_name, update_flag=False):
        if type_name == "task" and update_flag:
            return Resilient.TASK_UPDATE

        if URI_LOOKUP_BY_TYPE.get(type_name, None):
            return URI_LOOKUP_BY_TYPE[type_name].format(inc_id)
        else:
            return Resilient.DATATABLE.format(inc_id, type_name) # if type not found, it's a datatable

    def format_datatable_cells(self, payload):
        """
        {'id': 456, 'reported_on': 'Thu Feb 13 16:44:53 UTC 2020', 'template_id': 12, 'template_project': '2nd Project', 'template_name': 'panorama_add_malicious_ip', 'template_description': '', 'template_playbook': 'panorama_add_malicious_ip.yml', 'template_last_run': '2019-12-10 04:32:52.861234Z'}
        :param payload:
        :return:
        """
        cells = {}
        for k, v in payload.items():
            if not k == "id":
                cells[k] = { "value": v }

        return payload['id'], cells


    def create_incident(self, payload):
        """
        call the resilient api to create an incident
        :param payload:
        :return:
        """
        uri = Resilient.INCIDENT_URI
        return self._post(uri, payload)

    def update_incident(self, inc_id, incident_data):
        """
        call the Resilient API to update an incident
        This function uses the resilient library Patch object to compose the json needed for
        the update operation
        :param inc_id:
        :param upgrade_record:
        :return: result payload of the patch operation
        """
        try:
            incident_uri = "/".join((Resilient.INCIDENT_URI, str(inc_id)))

            # get the existing record with current values
            current_inc = self.rest_client.get(incident_uri)

            patch = resilient.Patch(current_inc)

            result = None
            changes = False
            if incident_data.get_param_attributes() and incident_data.get_param_attributes():
                for name, value in incident_data.get_param_attributes().items():
                    if name not in ('notes', 'artifacts', 'customfields'):
                        patch.add_value(name, incident_data.get_param_value(name, value))
                        changes = True

                if incident_data.get_customfields():
                    for name, value in incident_data.get_customfields().items():
                        patch.add_value(name, value)
                        changes = True

                if changes:
                    patch_result = self.rest_client.patch(incident_uri, patch)
                    result = self._chk_status(patch_result)

            # adding notes and artifacts?
            if incident_data.get_notes():
                comments_uri = "/".join((incident_uri, "comments"))
                for note_payload in incident_data.get_notes():
                    note_result = self.rest_client.post(comments_uri, note_payload)
                    self._chk_status(note_result)

            if incident_data.get_artifacts():
                artifacts_uri = "/".join((incident_uri, "artifacts"))
                for artifact_payload in incident_data.get_artifacts():
                    artifact_result = self.rest_client.post(artifacts_uri, artifact_payload)
                    self._chk_status(artifact_result)

            return result if result else {}

        except Exception as err:
            # incident not found
            raise IntegrationError(err)

    def delete_incident(self, inc_id):
        """
        call the Resilient API to delete an incident
        :param inc_id:
        :return:
        """
        uri = "/".join((Resilient.INCIDENT_URI, str(inc_id)))

        try:
            result = self.rest_client.delete(uri)
        except Exception as err:
            raise IntegrationError(err)

        return result

    def add_artifact(self, inc_id, payload):
        """
        call the Resilient API to add an artifact to an existing incident
        :param inc_id:
        :param payload:
        :return:
        """
        uri = "/".join((Resilient.INCIDENT_URI, str(inc_id), Resilient.ARTIFACT_URI))

        return self._post(uri, payload)

    def add_note(self, inc_id, payload):
        """
        call the Resilient API to add a note to an existing incident
        :param inc_id:
        :param payload:
        :return:
        """
        uri = "/".join((Resilient.INCIDENT_URI, str(inc_id), Resilient.COMMENT_URI))

        return self._post(uri, payload)

    def _post(self, uri, payload):
        """
        internal function to call the Resilient POST operation
        :param uri:
        :param payload:
        :return:
        """
        try:
            result = self.rest_client.post(uri, payload)
        except Exception as err:
            raise IntegrationError(err)

        return result

    def _chk_status(self, resp, rc=200):
        """
        check the return status. If return code is not met, raise IntegrationError,
        if success, return the json payload
        :param resp:
        :param rc:
        :return:
        """
        if hasattr(resp, "status_code"):
            if isinstance(rc, list):
                if resp.status_code < rc[0] or resp.status_code > rc[1]:
                    raise IntegrationError("status code failure: {}".format(resp.status_code))
            elif resp.status_code != rc:
                raise IntegrationError("status code failure: {}".format(resp.status_code))

            return resp.json()

        return {}

    def get_object_schema(self, object_type):
        if not self.cache.get(object_type, None):
            self.cache[object_type] = self.rest_client.get(Resilient.TYPES_URI.format(object_type))

        return self.cache[object_type]

    def get_custom_fields(self, object_type):
        """
        get the custom fields for a given org
        :param rest_client_helper:
        :return: list of custom fields
        """
        types_map = self.get_object_schema(object_type)
        # get all the custom fields
        custom_fields = [field_type \
            for field_type in types_map if field_type['prefix'] == 'properties']

        return custom_fields

    def create_field(self, object_type, field_list):
        for field in field_list:
            try:
                uri = "{}/fields".format(Resilient.TYPES_URI.format(object_type))
                self.rest_client.post(uri, field)
            except Exception:
                # check that we got a 400
                pass

    def get_field_value(self, object_type, field_name, field_value):
        """
        convert a field value used for select values to a value
        :param field_name: name of field
        :param field_value: value for field, may be an ID for select fields
        :return: select value or original value
        """

        field = self.get_field(object_type, field_name)

        if field and field['input_type'] == 'select':
            for select_item in field['values']:
                if select_item['value'] == field_value:
                    return select_item['label']

        return field_value

    def get_select_field_id(self, object_type, field_name, field_value):
        """
        return the select ID for a field based on it's value.
        This is the reserse of get_field_value
        :param object_type:
        :param field_name:
        :param field_value:
        :return: select value ID or original value
        """
        field = self.get_field(object_type, field_name)

        if field and field['input_type'] == 'select':
            for select_item in field['values']:
                if select_item['label'] == field_value:
                    return select_item['value']

        return field_value

    def get_field(self, object_type, field_name):
        """
        return the schema for a field based on object type and field_name
        :param object_type:
        :param field_name:
        :return: json schema for field
        """
        return self.get_object_schema(object_type)['fields'].get(field_name, None)

    def find_sync_row(self, orig_incident_id, orig_org_id, type_name, type_id):
        key = self.make_sync_key(orig_org_id, orig_incident_id, type_name, type_id)
        query = {
            "org_id": self.rest_client.org_id,
            "query": str(type_id),
            "types": [
                "datatable"
            ],
            "filters": {
                "data_feeder_sync": [
                    {
                        "conditions": [
                            {
                                "field_name": "key",
                                "method": "equals",
                                "value": [
                                    key
                                ]
                            }
                        ]
                    }
                ]
            },
            "min_required_results": 0
        }

        response = self.rest_client.search(query)
        if len(response['results']) > 1:
            raise IntegrationError("Too many results indicates a consistency error")

        if not response['results']:
            return None, None, None, None, None

        result = response['results'][0]

        # get the type_id
        for _, item in result['result']['cells'].items():
            if item['id']['name'] == 'new_id':
                type_id = item['value']
                break

        return result['inc_id'], type_id, result['obj_id'], result['result']['cells'], result['result']['version']

    def make_sync_key(self, orig_org_id, orig_incident_id, type_name, type_id):
        """
        build the key to the data_feeder_sync datatable
        :param orig_org_id:
        :param orig_incident_id:
        :param type_name:
        :param type_id:
        :return: <org_id>:<inc_id>:<type_name>:<type_id>
        """
        return ":".join((str(orig_org_id), str(orig_incident_id), type_name, str(type_id)))

    def update_existing_sync_row(self, inc_id, row_id, cells, version):
        """
        update last_sync time for datarow
        :param inc_id:
        :param row_id:
        :param cells:
        :param version:
        :return:
        """

        new_cells = cells.copy()
        # update the last sync field
        for cell, body in new_cells.items():
            if body['id']['name'] == 'last_sync':
                body['value'] = self._get_current_timestamp()

        payload = {
            "cells": new_cells,
            "version": version
        }

        uri = "{}/{}".format(Resilient.SYNC_DATATABLE_URI.format(inc_id), row_id)
        return self.rest_client.put(uri, payload)

    def create_sync_row(self, inc_id, orig_inc_id, orig_org_id, type_name, orig_id, new_id):
        """
        create a new row in our sync datatable to track this information
        :param inc_id:
        :param orig_inc_id:
        :param orig_org_id:
        :param type_name:
        :param orig_id:
        :param new_id:
        :return:
        """
        key = self.make_sync_key(orig_org_id, orig_inc_id, type_name, orig_id)
        payload = {
            "cells": {
                "key": {
                    "value": key
                },
                "new_id": {
                    "value": new_id
                },
                "last_sync": {
                    "value": self._get_current_timestamp()
                }
            }
        }

        self.log.debug(payload)
        uri = Resilient.SYNC_DATATABLE_URI.format(inc_id)
        return self.rest_client.post(uri, payload)

    def _find_incident(self, src_org_id, src_inc_id):
        """
        Find the incident synchronized from a given inc_id and org_id
        :param src_org_id:
        :param src_inc_id:
        :return: found inc_id or None
        """
        uri = "/incidents/query"

        query = {
            "filters": [
                {
                    "conditions": [
                        {
                            "field_name": "properties.{}".format(Resilient.DF_ORG_ID),
                            "method": "equals",
                            "value": src_org_id
                        },
                        {
                            "field_name": "properties.{}".format(Resilient.DF_INC_ID),
                            "method": "equals",
                            "value": src_inc_id
                        }
                    ]
                }
            ]
        }

        self.log.debug(query)

        response = self.rest_client.post(uri, query)
        if response:
            return response[0]['id']

        return None

    def set_sync_fields(self, payload, orig_org_id, orig_inc_id):
        payload['properties'][Resilient.DF_ORG_ID] = orig_org_id
        payload['properties'][Resilient.DF_INC_ID] = orig_inc_id

    def _get_current_timestamp(self):
        return calendar.timegm(time.gmtime())*1000
