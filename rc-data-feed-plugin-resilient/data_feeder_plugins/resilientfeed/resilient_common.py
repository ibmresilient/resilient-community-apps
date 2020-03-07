# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use, line-too-long

import calendar
import io
import logging
import mimetypes
import os
import resilient
import sys
import tempfile
import time
from .db_sync import DBSyncFactory
from .constants import DF_INC_ID, DF_ORG_ID
from resilient_lib import IntegrationError, get_file_attachment, write_file_attachment
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

    def __init__(self, opts, rest_client_helper):
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

        # get the class to maintain the reference map: either datatable or sqlite
        self.dbsync = DBSyncFactory.get_dbsync(self.rest_client, self.opts.get("db_sync_file", None))
        if not self.dbsync:
            raise IntegrationError("Unable to create DBSync object")


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
            self.dbsync.find_sync_row(src_org_id, src_inc_id, mapped_type_name, orig_id)

        # update operation?
        if sync_type_id:
            self.log.info('updating %s(%s->%s): %s', mapped_type_name, orig_id, sync_type_id, payload)
            self.update_type(mapped_type_name, sync_inc_id, sync_type_id, sync_task_id, payload)
            # update sync row
            self.dbsync.update_existing_sync_row(sync_inc_id, row_id, sync_row, sync_row_version)

        else:
            # make sure the incident already exists for child objects
            if mapped_type_name != 'incident':
                sync_inc_id = self.dbsync.find_incident(src_org_id, src_inc_id)
                if not sync_inc_id:
                    raise IntegrationError("Incident for source Id {} does not exist".format(src_inc_id))

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
                self.dbsync.create_sync_row(sync_inc_id, src_org_id, src_inc_id, mapped_type_name, orig_id, new_type_id)
            else:
                if mapped_type_name == "incident":
                    set_sync_fields(payload, src_org_id, src_inc_id)

                # create object
                self.log.info('adding %s(%s): %s', type_name, orig_id, payload)
                sync_inc_id, new_type_id = self.create_type(mapped_type_name, sync_inc_id, sync_task_id, payload)

                # create sync row
                self.dbsync.create_sync_row(sync_inc_id, src_org_id, src_inc_id, mapped_type_name, orig_id, new_type_id)


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
        """
        update the object. This will require reading the current record to collect the existing version number
        :param mapped_type_name:
        :param sync_inc_id:
        :param sync_type_id:
        :param sync_task_id:
        :param payload:
        :return:
        """
        uri = get_url(sync_task_id or sync_inc_id, mapped_type_name, update_flag=True)
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
        """
        create the new object
        :param mapped_type_name:
        :param sync_inc_id:
        :param sync_task_id:
        :param payload:
        :return:
        """
        uri = get_url(sync_task_id or sync_inc_id, mapped_type_name)

        response = self.rest_client.post(uri, payload)
        self.log.debug(response)

        # created an incident?
        if sync_inc_id is None:
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
                self.dbsync.find_sync_row(src_org_id, src_inc_id, "task", payload.get("task_id"))

            return sync_task_id, "tasknote"

        return None, type_name

    def upload_attachment(self, src_rest_client, src_inc_id, src_org_id, type_name, payload, orig_id):
        """
        attachments may be incident level, associated with tasks, or part of an artifact
        see write_artifact_attachment for artifact file uploads
        :param src_rest_client:
        :param src_inc_id:
        :param src_org_id:
        :param type_name:
        :param payload:
        :param orig_id:
        :return:
        """
        src_artifact_id = src_attachment_id = None
        if payload.get('attachment', {}).get('content_type', None):
            src_artifact_id = orig_id
        else:
            src_attachment_id = orig_id

        # is this a task based attachment?
        if payload.get("task_id", None):
            src_task_id = payload.get("task_id")
            sync_inc_id, sync_type_id, row_id, sync_row, sync_row_version = \
                self.dbsync.find_sync_row(src_org_id, src_inc_id, "task", src_task_id)
            dst_task_id = sync_type_id
        else:
            src_task_id = None
            dst_task_id = None
            # get the target incident
            sync_inc_id, sync_type_id, row_id, sync_row, sync_row_version = \
                self.dbsync.find_sync_row(src_org_id, src_inc_id, "incident", src_inc_id)

        if not sync_type_id:
            raise IntegrationError("{} for Id {} does not exist".format(type_name, src_task_id if src_task_id else src_inc_id))

        # read the attachment from the source Resilient
        attachment_contents = get_file_attachment(src_rest_client, src_inc_id, attachment_id=src_attachment_id,
                                                  task_id=src_task_id, artifact_id=src_artifact_id)

        if sys.version_info.major < 3:
            file_handle = io.StringIO(attachment_contents)
        else:
            file_handle = io.BytesIO(attachment_contents)

        if src_artifact_id:
            response = self.write_artifact_file(payload['attachment']['name'], file_handle,
                                                sync_inc_id, payload)
        else:
            response = write_file_attachment(self.rest_client, payload['name'], file_handle, sync_inc_id,
                                             task_id=dst_task_id, content_type=payload['content_type'])

        # create sync row
        self.dbsync.create_sync_row(sync_inc_id, src_org_id, src_inc_id, type_name, orig_id, response.get('id', None))

    def write_artifact_file(self, file_name, datastream, incident_id, payload):
        """
        call the Resilient REST API to create the attachment on incident or task
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
                artifact_uri = "{}/files".format(get_url(incident_id, "artifact"))

                new_attachment = self.rest_client.post_artifact_file(artifact_uri,
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


    '''
    def get_object_schema(self, object_type):
        """
        
        :param object_type: 
        :return: 
        """
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
    '''

# S T A T I C
def get_url(inc_id, type_name, update_flag=False):
    """
    get the uri based on the type of field to create/update
    :param inc_id: most uri's include incident_id
    :param type_name:
    :param update_flag: task updates use a different uri
    :return: uri
    """
    if type_name == "task" and update_flag:
        return Resilient.TASK_UPDATE

    if URI_LOOKUP_BY_TYPE.get(type_name, None):
        return URI_LOOKUP_BY_TYPE[type_name].format(inc_id)

    return Resilient.DATATABLE.format(inc_id, type_name) # if type not found, it's a datatable

def set_sync_fields(payload, orig_org_id, orig_inc_id):
    """
    keep a record of which incident created the copy
    :param payload:
    :param orig_org_id:
    :param orig_inc_id:
    :return:
    """
    payload['properties'][DF_ORG_ID] = orig_org_id
    payload['properties'][DF_INC_ID] = orig_inc_id

