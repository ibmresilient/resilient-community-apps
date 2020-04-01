# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use, line-too-long

import io
import json
import logging
import mimetypes
import os
import resilient
import tempfile
from data_feeder_plugins.resilientfeed.lib.db_sync import DBSyncFactory
from cachetools import cached, TTLCache
from resilient_lib import IntegrationError, get_file_attachment, write_file_attachment

# URIs for resilient API calls
URI_LOOKUP_BY_TYPE = {
    "incident": "/incidents",
    "artifact": "/incidents/{}/artifacts",
    "note": "/incidents/{}/comments",
    "milestone": "/incidents/{}/milestones",
    "attachment": "/incidents/{}/attachments",
    "task": "/incidents/{}/tasks",
    "tasknote": "/tasks/{}/comments",
    "taskattachment": "/tasks/{}/attachments"
}

LOG = logging.getLogger(__name__)

class Resilient(object):
    """
    Helper class to encapsulate the Resilient API calls
    -- create incident, task, note, milestone, comment, attachment, artifact, datatable
    Different care is needed when creating artifacts which are files and tasks which have notes
    """

    # uri's
    DATATABLE_URI = "/incidents/{}/table_data/{}"
    DATATABLE_ROWDATA_URI = "/".join((DATATABLE_URI, "row_data"))
    TASK_UPDATE_URI = "/tasks"
    GET_INCIDENT_TASKS_URI = "/incidents/{}/tasks"
    GET_USERS_URI = "/users/query_paged?return_level=partial"
    GET_GROUPS_URI = "/groups"
    GET_FIELDS_URI = "/types/{}/fields"

    def __init__(self, opts, rest_client_helper):
        """
        configure the rest_client for the destination resilient
        :param opts: used for Resilient target
        :param rest_client_helper: used for Resilient source
        """
        self.opts = opts

        # rest_client_helper is None for destination Resilient org
        try:
            if rest_client_helper:
                self.rest_client = rest_client_helper.rest_client()     # source resilient
            else:
                self.rest_client = resilient.get_client(self.opts)      # target resilient
        except Exception as err:
            raise IntegrationError(str(err))

        # get the class to maintain the reference map: either datatable or sqlite
        # only needed for target Resilient
        if not rest_client_helper:
            self.dbsync = DBSyncFactory.get_dbsync(self.rest_client.org_id, self.opts.get("db_sync_file", None))
            if not self.dbsync:
                raise IntegrationError("Unable to create DBSync object")


    def delete_type(self, orig_org_id, orig_inc_id, type_name, payload, orig_type_id):
        """
        Delete an object and update the sync db to reflect change.
        If deleting an incident, need to also delete db entries for all child objects
        :param orig_inc_id:
        :param orig_org_id:
        :param type_name:
        :param payload:
        :param orig_type_id:
        :return: None
        """
        # determine if this is a task comment or attachment
        sync_task_id, mapped_type_name = self._map_task_note_attachment(orig_org_id, orig_inc_id, type_name, payload)

        # todo this is current limitation in the platform
        if not sync_task_id and mapped_type_name == "taskattachment":
            LOG.info("Unable to delete task attachments: %s:%s->%s", orig_inc_id, mapped_type_name, orig_type_id)
            return

        # find the sync record, based on org, type_id and incident_id
        sync_inc_id, sync_type_id, sync_state = \
            self.dbsync.find_sync_row(orig_org_id, orig_inc_id, type_name, orig_type_id)

        # do nothing if already deleted
        if sync_state == "deleted":
            return

        if not sync_inc_id:
            LOG.warning("Not found to delete: %s:%s->%s", orig_inc_id, mapped_type_name, orig_type_id)
            return

        uri, _ = get_url(sync_task_id or sync_inc_id, mapped_type_name, False)
        # fill in object id for delete
        uri = "{}/{}".format(uri, sync_type_id)

        try:
            LOG.debug("Deleting %s:%s->%s", mapped_type_name, sync_inc_id, sync_type_id)
            self.rest_client.delete(uri)
            LOG.info("Deleted %s:%s->%s", mapped_type_name, sync_inc_id, sync_type_id)

            # remove the sync record
            self.dbsync.delete_type(self.rest_client.org_id, sync_inc_id, type_name, sync_type_id)

            if type_name == "incident":
                # remove record for all child objects
                self.dbsync.delete_incident_types(self.rest_client.org_id, sync_inc_id)

        except Exception as err:
            LOG.error(err)


    def create_update_type(self, orig_org_id, orig_inc_id, type_name, payload, orig_type_id):
        """
        wrapper to _create_update_type to include logic to retry failures based on parent objects created in
        reverse order
        :param orig_org_id:
        :param orig_inc_id:
        :param type_name:
        :param payload:
        :param orig_type_id:
        :return: list of object Ids created
        """
        id_list = []
        new_id = self._create_update_type(orig_inc_id, orig_org_id, type_name, payload, orig_type_id)

        if new_id:
            id_list.append(new_id)      # track ids of objects created or updated
            # determine if there are any retries needed
            retry_list = self.dbsync.find_retry_rows(orig_org_id, orig_inc_id, type_name)
            # retry any object queued for retry based on a dependency
            # this can occur when tasks show up in msg destination before the incident
            #   and artifacts that have parent artifacts
            for retry_item in retry_list:
                retry_type_name = retry_item[2]
                retry_payload = json.loads(retry_item[4]) # deserialize the payload back to json
                retry_orig_id = retry_item[0]

                LOG.info('retrying %s:%s->%s to %s:%s)', orig_inc_id, retry_type_name, retry_orig_id,
                         self.rest_client.org_id, new_id)
                # org1_type_id, org2_inc_id, org1_dep_type_name, org1_dep_type_id, payload
                new_type_id = self._create_update_type(orig_inc_id, orig_org_id, retry_type_name, retry_payload, retry_orig_id)

                if new_type_id:
                    id_list.append(new_type_id)

        return id_list

    def _create_update_type(self, orig_inc_id, orig_org_id, type_name, payload, orig_type_id):
        """
        create a new object if it doesn't already have a mapping in the target org
        :param orig_inc_id:
        :param orig_org_id:
        :param type_name: 'incident', 'task', 'artifact', etc.
        :param payload:
        :param orig_type_id: such as task_id, artifact_id, etc.
        :return: id of newly created object
        """

        # determine if this is a task comment
        sync_task_id, mapped_type_name = self._map_task_note_attachment(orig_org_id, orig_inc_id, type_name, payload)

        # determine if we have seen this object before
        sync_inc_id, sync_type_id, sync_state = \
            self.dbsync.find_sync_row(orig_org_id, orig_inc_id, mapped_type_name, orig_type_id)

        # do nothing if already deleted
        if sync_state == "deleted":
            return None

        # update operation?
        if sync_type_id and sync_inc_id != 0:
            LOG.info('updating %s:%s->%s to %s:%s->%s)', orig_inc_id, mapped_type_name, orig_type_id,
                     self.rest_client.org_id, sync_inc_id, sync_type_id)
            LOG.debug(payload)
            try:
                self.update_type(mapped_type_name, sync_inc_id, sync_type_id, sync_task_id, payload)
                # update sync row
                self.dbsync.update_existing_sync_row(sync_inc_id, mapped_type_name, sync_type_id)

                new_type_id = sync_type_id
            except IntegrationError as err:
                LOG.warning(str(err))
                new_type_id = None
                LOG.warning('queued to retry %s:%s->%s to %s:%s', type_name, orig_inc_id, orig_type_id,
                            self.rest_client.org_id, sync_inc_id)
                self.dbsync.create_retry_row(orig_org_id, orig_inc_id, type_name, orig_type_id,
                                             type_name, None,
                                             sync_inc_id, payload)
        else:
            # all types to be created
            # make sure the incident already exists for child objects
            if mapped_type_name != 'incident':
                sync_inc_id, sync_state = self.dbsync.find_incident(orig_org_id, orig_inc_id)

                # do nothing if already deleted
                if sync_state == "deleted":
                    return None

                # a missing incident means the order of creating the child is incorrect.
                # this happens when creating an incident with incident_type_ids and the tasks show up first in the
                # message destination
                if sync_inc_id is None:
                    self.dbsync.create_retry_row(orig_org_id, orig_inc_id, 'incident', orig_inc_id,
                                                 mapped_type_name, orig_type_id,
                                                 None, payload)
                    LOG.warning('Incident not found. Queued to retry %s:%s->%s to %s', type_name, orig_inc_id, orig_type_id,
                                self.rest_client.org_id)
                    return None

                if sync_inc_id == 0:
                    # this is a child object to an incident which was filtered
                    LOG.info("filtering %s:%s->%s", type_name, orig_inc_id, orig_type_id)
                    return None

            # creating a task? may already have one created when the incident was created
            if mapped_type_name == "task":
                # Is this an unmapped task created with the incident?
                new_type_id = self._find_task(sync_inc_id, payload)
                if not new_type_id:
                    # creating a task doesn't use instr_text field
                    payload.pop('instr_text', None)

                    sync_inc_id, new_type_id = self.create_type(orig_org_id, orig_inc_id, orig_type_id,
                                                                mapped_type_name, type_name,
                                                                sync_inc_id, sync_task_id, payload)
                else:
                    LOG.debug('duplicate %s:%s->%s of %s:%s->%s', type_name, orig_inc_id, orig_type_id,
                              self.rest_client.org_id, sync_inc_id, new_type_id)
                    LOG.debug(payload)

                    # create sync row, duplicates are mapped too
                    self.dbsync.create_sync_row(orig_org_id, orig_inc_id, type_name, orig_type_id,
                                                sync_inc_id, new_type_id, 'active')

            else:
                # all types not an incident or task
                if payload or sync_inc_id:
                    sync_inc_id, new_type_id = self.create_type(orig_org_id, orig_inc_id, orig_type_id,
                                                                mapped_type_name, type_name,
                                                                sync_inc_id, sync_task_id, payload)

                else:
                    # filtered objects occur when matching criteria fails
                    LOG.info("filtering %s:%s->%s", type_name, orig_inc_id, orig_type_id)
                    sync_inc_id = new_type_id = 0

                    # create sync row - even if filtered
                    self.dbsync.create_sync_row(orig_org_id, orig_inc_id, type_name, orig_type_id,
                                                sync_inc_id, new_type_id, 'filtered')

        return new_type_id

    def create_type(self, orig_org_id, orig_inc_id, orig_type_id,
                    mapped_type_name, type_name,
                    sync_inc_id, sync_task_id, payload):
        """
        create the object type
        :param orig_org_id:
        :param orig_inc_id:
        :param orig_type_id:
        :param mapped_type_name: can be different than type_name as in tasknote or taskattachment
        :param type_name:
        :param sync_inc_id:
        :param sync_task_id:
        :param payload:
        :return: sync_inc_id, new_type_id
        """
        # create object
        LOG.debug('adding %s:%s->%s to %s:%s', mapped_type_name, orig_inc_id, orig_type_id,
                  self.rest_client.org_id, sync_inc_id)

        try:
            sync_inc_id, new_type_id = self._create_type(sync_inc_id, sync_task_id, mapped_type_name, payload)

            LOG.info('added %s:%s->%s to %s:%s->%s', mapped_type_name, orig_inc_id, orig_type_id,
                     self.rest_client.org_id, sync_inc_id, new_type_id)

            # create sync row, duplicates are now mapped too
            self.dbsync.create_sync_row(orig_org_id, orig_inc_id, type_name, orig_type_id,
                                        sync_inc_id, new_type_id, 'active')
        except (IntegrationError, Exception):
            new_type_id = None
            LOG.warning('queued to retry %s:%s->%s to %s:%s', type_name, orig_inc_id, orig_type_id,
                        self.rest_client.org_id, sync_inc_id)
            self.dbsync.create_retry_row(orig_org_id, orig_inc_id, type_name, orig_type_id,
                                         type_name, None,
                                         sync_inc_id, payload)

        return sync_inc_id, new_type_id

    def _create_type(self, sync_inc_id, sync_task_id, mapped_type_name, payload):
        """
        create the new object: incident, artifact, milestone, task
        :param sync_inc_id:
        :param sync_task_id:
        :param mapped_type_name:
        :param payload:
        :return: id of new object and it's type (task comments-> tasknote)
        """
        uri, _ = get_url(sync_task_id or sync_inc_id, mapped_type_name)

        try:
            response = self.rest_client.post(uri, payload)

            # created an incident?
            if not sync_inc_id:
                sync_inc_id = response['id']

            # response a list?
            if isinstance(response, list):
                new_type_id = response[0]['id']  # creating a new artifact returns a list object
            else:
                new_type_id = response['id']
        except Exception as err:
            LOG.warning("Unable to create %s, Incident %s, %s", mapped_type_name, sync_inc_id, err)
            LOG.debug(uri)
            LOG.debug(payload)
            raise IntegrationError(str(err))

        return sync_inc_id, new_type_id

    def _find_task(self, sync_inc_id, payload):
        """
        tasks automatically created with an incident can cause duplicates from the source incident also sync'd.
        This logic will get all the sync incident tasks and make sure there isn't a duplicate
        :param sync_inc_id:
        :param payload: task payload
        :return: new_type_id: task id of found task
        """
        response = get_incident_tasks(self.rest_client, sync_inc_id)

        for task in response:
            # pick a number of comparison fields to ensure duplicate
            if task['name'] == payload['name'] and task['cat_name'] == payload['cat_name']:
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
        uri, is_datatable = get_url(sync_task_id or sync_inc_id, mapped_type_name, update_flag=True)

        # get uri to our record
        update_uri = "{}/{}".format(uri, sync_type_id)

        # datatables need to go row by row to find the existing record to update
        if is_datatable:
            existing_object = self.get_existing_datatable_row(sync_inc_id, mapped_type_name, sync_type_id)
        else:
            # get the existing record
            # some objects, like milestones, cannot be individually referenced
            try:
                existing_object = self.rest_client.get(update_uri)
            except Exception as err:
                existing_object = None

        # set the version of this record, if applicable
        if existing_object:
            # some objects have 'vers' and others have 'version'
            key = [vers for vers in ['vers', 'version'] if vers in existing_object]
            if key:
                ## collect the version number
                version = existing_object[key[0]]
                ## add correct version number
                payload[key[0]] = version

        try:
            response = self.rest_client.put(update_uri, payload)

        except Exception as err:
            LOG.warning("Unable to update %s %s, Incident %s, %s", mapped_type_name, sync_type_id, sync_inc_id, err)
            LOG.debug(update_uri)
            LOG.debug(payload)
            raise IntegrationError(str(err))

    def get_existing_datatable_row(self, inc_id, table_name, row_id):
        """
        datatables cannot be queried for a given row, so we'll need to get the entire table and parse each row to
        find the given row.
        :param inc_id:
        :param table_name:
        :param row_id:
        :return: None or row object
        """
        datatable_list = self.get_datatable(inc_id, table_name)

        if datatable_list:
            for row in datatable_list['rows']:
                if row['id'] == row_id:
                    return row

        return None

    @cached(cache=TTLCache(maxsize=128, ttl=60))
    def get_datatable(self, inc_id, table_name):
        """
        get all rows in a datatable, caching the results
        The API query results will be cached
        :param inc_id:
        :param table_name
        :param row_id:
        :return: None or row found
        """
        try:
            uri = Resilient.DATATABLE_URI.format(inc_id, table_name)
            datatable_list = self.rest_client.get(uri)
            return datatable_list

        except Exception:
            LOG.error("Unable to get datatable '%s' for incident %s", table_name, inc_id)

        return None

    def _map_task_note_attachment(self, orig_org_id, orig_inc_id, type_name, payload):
        """
        task notes and attachments need a different URL
        :param orig_org_id
        :param orig_inc_id
        :param type_name:
        :param payload:
        :return: "tasknote" for task notes, otherwise the original value
        """
        if type_name in ["note", "attachment"] and payload.get("type", "") == "task":
            # get the sync_task_id for this task comment/attachment
            _, sync_task_id, sync_state = self.dbsync.find_sync_row(orig_org_id, orig_inc_id,
                                                                    "task", payload.get("task_id"))

            # do nothing if already deleted
            if sync_state == "deleted":
                return None, None

            # return a different type name for task notes and attachments
            return sync_task_id, "task{}".format(type_name)

        return None, type_name

    def upload_attachment(self, src_rest_client, orig_org_id, orig_inc_id, type_name, payload, orig_type_id):
        """
        attachments may be incident level, associated with tasks, or part of an artifact
        see write_artifact_attachment for artifact file uploads
        :param src_rest_client:
        :param orig_org_id:
        :param orig_inc_id:
        :param type_name:
        :param payload:
        :param orig_type_id:
        :return: None
        """
        src_artifact_id = src_attachment_id = src_task_id = dst_task_id = None
        if payload.get('attachment', {}).get('content_type', None):
            src_artifact_id = orig_type_id
        else:
            src_attachment_id = orig_type_id

        # is this a task based attachment?
        if payload.get("task_id", None):
            src_task_id = payload.get("task_id")
            sync_inc_id, dst_task_id, sync_state = self.dbsync.find_sync_row(orig_org_id, orig_inc_id,
                                                                             "task", src_task_id)
            # if the task doesn't exist, the attachment will be requeued
            if not dst_task_id:
                raise IntegrationError("%s:%s->%s for attachment id {} does not exist".format(type_name, orig_inc_id,
                                                                                              src_task_id, orig_type_id))
        else:
            # find the incident for this attachment
            sync_inc_id, sync_state = self.dbsync.find_incident(orig_org_id, orig_inc_id)

            # do nothing if incident already deleted or filtered
            if sync_state != "active":
                return

            # get the target attachment, if it exists
            _, sync_type_id, _ = self.dbsync.find_sync_row(orig_org_id, orig_inc_id,
                                                           type_name, orig_type_id)
            # attachments cannot be updated
            if sync_type_id:
                return

        # read the attachment from the source Resilient
        attachment_contents = get_file_attachment(src_rest_client, orig_inc_id, attachment_id=src_attachment_id,
                                                  task_id=src_task_id, artifact_id=src_artifact_id)

        file_handle = io.BytesIO(attachment_contents)

        LOG.debug('adding %s:%s->%s to %s:%s', type_name, orig_inc_id, orig_type_id,
                  self.rest_client.org_id, sync_inc_id)

        # artifact as file attachment?
        if src_artifact_id:
            response = self.write_artifact_file(payload['attachment']['name'], file_handle,
                                                sync_inc_id, payload)
        else:
            try:
                response = write_file_attachment(self.rest_client, payload['name'], file_handle, sync_inc_id,
                                                 task_id=dst_task_id, content_type=payload['content_type'])
            except Exception as err:
                LOG.error("Unable to create attachment for file: %s", payload['name'])
                LOG.error(payload)
                LOG.exception(err)
                response = {}

        # create sync row
        new_type_id = response.get('id', None)
        self.dbsync.create_sync_row(orig_org_id, orig_inc_id, type_name, orig_type_id,
                                    sync_inc_id, new_type_id, 'active')

        LOG.info('added %s:%s->%s to %s:%s->%s', type_name, orig_inc_id, orig_type_id,
                 self.rest_client.org_id, sync_inc_id, new_type_id)

    def write_artifact_file(self, file_name, datastream, incident_id, payload):
        """
        call the Resilient REST API to create the attachment on incident or task
        :param file_name: required, name of the attachment
        :param datastream: required, stream of bytes
        :param incident_id: required
        :param payload: required,
        :return: new attachment -dictionary of attachment metadata
        """
        # determine the content_type
        content_type = payload['attachment'].get('content_type', None) \
                       or mimetypes.guess_type(file_name or "")[0] \
                       or "application/octet-stream"

        attachment = datastream.read()
        new_attachment = None

        # create tempfile for submitted attachment to Resilient
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            try:
                temp_file.write(attachment)
                temp_file.close()

                # Create a new artifact attachment by calling resilient REST API
                uri, _ = get_url(incident_id, "artifact")
                artifact_uri = "{}/files".format(uri)

                new_attachment = self.rest_client.post_artifact_file(artifact_uri,
                                                                     payload.get("type", None),
                                                                     temp_file.name,
                                                                     description=payload.get("description", None),
                                                                     value=file_name,
                                                                     mimetype=content_type)
            except Exception as err:
                LOG.error("Unable to create attachment for file: %s", file_name)
                LOG.error(artifact_uri)
                LOG.error(payload)
                LOG.exception(err)
            finally:
                os.unlink(temp_file.name)

        if isinstance(new_attachment, list):
            new_attachment = new_attachment[0]

        return new_attachment

# S T A T I C
def get_url(inc_id, type_name, update_flag=False):
    """
    get the uri based on the type of field to create/update
    :param inc_id: most uri's include incident_id
    :param type_name:
    :param update_flag: task updates use a different uri
    :return: uri, true/false if a datatable
    """
    if type_name == "task" and update_flag:
        return Resilient.TASK_UPDATE_URI, False

    if URI_LOOKUP_BY_TYPE.get(type_name, None):
        return URI_LOOKUP_BY_TYPE[type_name].format(inc_id), False

    # if type not found, it's a datatable
    return Resilient.DATATABLE_ROWDATA_URI.format(inc_id, type_name), True

@cached(cache=TTLCache(maxsize=128, ttl=60))
def get_incident_tasks(rest_client, sync_inc_id):
    """
    get all tasks for an incident, if not yet cached or the cache has expired
    :param sync_inc_id:
    :return: list of tasks
    """
    uri = Resilient.GET_INCIDENT_TASKS_URI.format(sync_inc_id)
    return rest_client.get(uri)

@cached(cache=TTLCache(maxsize=10, ttl=600))
def get_users_and_groups(rest_client):
    """
    build list of users from the target organization
    :return: dictionary based on email
    """

    user_list = {}
    group_list = {}
    try:
        response = rest_client.post(Resilient.GET_USERS_URI, {})
        # invert the list by ID
        user_list = {user['email']: user for user in response['data']}

        response = rest_client.get(Resilient.GET_GROUPS_URI)
        # invert the list by ID
        group_list = {group['export_key']: group for group in response}
    except Exception as err:
        LOG.error("get_users_and_groups")
        LOG.error(err)

    user_and_group_list = user_list.copy()
    user_and_group_list.update(group_list)

    return user_and_group_list
