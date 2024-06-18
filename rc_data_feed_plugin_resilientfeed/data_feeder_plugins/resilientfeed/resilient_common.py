# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# pragma pylint: disable=unused-argument, line-too-long

import io
import logging
import mimetypes
import os
import resilient
import tempfile
import traceback
from data_feeder_plugins.resilientfeed.lib.db_sync_sqlite import SQLiteDBSync
from data_feeder_plugins.resilientfeed.lib.db_sync_postgres import PostgresDBSync
from cachetools import cached, TTLCache
from resilient_lib import IntegrationError, get_file_attachment, write_file_attachment
try:
    from urlparse import urlparse  # Python 2 import
except:
    from urllib.parse import urlparse  # Python 3 import

RETRY_MAX = 5

BYPASS_FIELDS = ["actions", "artifacts", "assessment", "creator_id", "create_date", "inc_last_modified_date",
                 "org_handle", "org_id", "owner_id", "phase_id", "perms", "playbooks", "regulators",
                 "task_changes", "vers"]

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

MAX_RETRY_TEMPLATE = "Max retry exceeded for type: %s %s->%s:%s to %s payload %s"

LOG = logging.getLogger(__name__)

class DBSyncFactory:
    @staticmethod
    def get_dbsync(org_id, sqllite_file, db_connection, db_user, db_pwd, sync_role_source):
        """
        build the object associated the type of sync data source
        If in the future another type of db is supported, this factory can be modified
        :param org_id:
        :param sqllite_file:
        :param db_connection: connection string
        :param db_user: database user
        :param db_pwd: database user password
        :param sync_role_source: role of resilientfeed: true = source, false = target
        :return: object for sync datasource
        """
        if sqllite_file:
            return SQLiteDBSync(org_id, sqllite_file, sync_role_source)

        return PostgresDBSync(org_id, db_connection, db_user, db_pwd, sync_role_source)

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
    GET_TASK_URI = "/tasks"
    GET_USERS_URI = "/users/query_paged?return_level=partial"
    GET_GROUPS_URI = "/groups"
    GET_FIELDS_URI = "/types/{}/fields"

    def __init__(self, opts, rest_client_helper, sync_role_source):
        """
        configure the rest_client for the destination resilient
        :param opts: used for Resilient target
        :param rest_client_helper: used for Resilient source
        :param sync_role_source: true = 'source', false = 'target'
        """
        self.opts = opts
        self.my_sync_role_source = sync_role_source

        # rest_client_helper is None for destination Resilient org
        try:
            if rest_client_helper:
                self.rest_client = rest_client_helper.get_inst_rest_client()     # source resilient
            else:
                self.rest_client = resilient.get_client(self.opts)      # target resilient
        except Exception as err:
            raise IntegrationError(str(err))

        # get the class to maintain the reference map: either datatable or sqlite
        # only needed for target Resilient
        if not rest_client_helper:
            self.dbsync = DBSyncFactory.get_dbsync(self.rest_client.org_id,
                                                   self.opts.get("sqlite_sync_file", None),
                                                   self.opts.get("postgresql_connect", None),
                                                   self.opts.get("postgresql_uid", None),
                                                   self.opts.get("postgresql_pwd", None),
                                                   sync_role_source
                                                   )
            if not self.dbsync:
                raise IntegrationError("Unable to create DBSync object")

    def return_type_parent(self, type_id, default_type="incident"):
        """note and attachments for tasks will use a different type name"""
        return "task" if type_id in ("tasknote", "taskattachment") else default_type

    def delete_type(self, orig_org_id, orig_inc_id, type_name, payload, orig_type_id, delete=True):
        """
        Delete an object and update the sync db to reflect change.
        If deleting an incident, need to also delete db entries for all child objects
        :param orig_inc_id:
        :param orig_org_id:
        :param type_name:
        :param payload:
        :param orig_type_id:
        :param delete: True|False, pertains to incident objects
        :return: type_id deleted
        """
        # determine if this is a task comment or attachment
        _orig_task_id, sync_task_id, mapped_type_name, _is_child_note = self._map_parent(orig_org_id, orig_inc_id,
                                                                                         type_name, payload)

        # this is current limitation in the platform
        if not sync_task_id and mapped_type_name == "taskattachment":
            LOG.info("Unable to delete task attachments: %s:%s->%s", orig_inc_id, mapped_type_name, orig_type_id)
            return None

        # find the sync record, based on org, type_id and incident_id
        sync_inc_id, sync_type_id, sync_state, _sync_role_source = \
            self.dbsync.find_sync_row(orig_org_id, orig_inc_id, mapped_type_name, orig_type_id)

        # do nothing if already deleted or bypassed
        if sync_state in ['deleted', 'bypassed']:
            LOG.debug("No action on %s: %s:%s->%s", sync_state, orig_inc_id, mapped_type_name, orig_type_id)
            return None

        if not sync_inc_id:
            LOG.warning("Not found to delete: %s:%s->%s", orig_inc_id, mapped_type_name, orig_type_id)
            return None

        uri, _ = get_url(sync_task_id or sync_inc_id, mapped_type_name, True)
        # fill in object id for delete
        uri = f"{uri}/{sync_type_id}"

        try:
            if not delete and type_name == "incident":
                LOG.info("Bypassing deleting %s:%s->%s", mapped_type_name, sync_inc_id, sync_type_id)
                # mark record for incident and all child objects as bypassed
                self.dbsync.delete_type(self.rest_client.org_id, sync_inc_id, type_name, sync_type_id, status='bypassed')
                self.dbsync.delete_incident_types(self.rest_client.org_id, sync_inc_id, status='bypassed')
            else:
                LOG.debug("Deleting %s:%s->%s", sync_inc_id, mapped_type_name, sync_type_id)
                self.rest_client.delete(uri)
                LOG.info("Deleted %s:%s->%s", sync_inc_id, mapped_type_name, sync_type_id)

                # mark the sync record deleted
                self.dbsync.delete_type(self.rest_client.org_id, sync_inc_id, mapped_type_name, sync_type_id)

                if type_name == "incident":
                    LOG.info("Deleting all associate tasks, notes, artifacts, etc. for %s:%s->%s", mapped_type_name, sync_inc_id, sync_type_id)
                    # remove record for all child objects
                    self.dbsync.delete_incident_types(self.rest_client.org_id, sync_inc_id)
        except Exception as err:
            LOG.error(err)
            sync_inc_id = None

        return sync_inc_id

    def create_update_type(self, orig_org_id, orig_inc_id, type_name, payload, orig_type_id, retry_count=0):
        """
        create a new object if it doesn't already have a mapping in the target org
        :param orig_org_id:
        :param orig_inc_id:
        :param type_name: 'incident', 'task', 'artifact', etc.
        :param payload:
        :param orig_type_id: such as task_id, artifact_id, task_note_id, etc.
        :param retry_count: for retries, the number we started with
        :return: id of newly created object
        """

        # determine if this is a task note or attachment
        orig_task_id, sync_task_id, mapped_type_name, is_child_note = self._map_parent(orig_org_id, orig_inc_id, 
                                                                                       type_name, payload)

        # determine if we have seen this object before
        sync_inc_id, sync_type_id, sync_state, sync_role_source = \
            self.dbsync.find_sync_row(orig_org_id, orig_inc_id, mapped_type_name, orig_type_id)

        # do nothing if already deleted or bypassed
        if sync_state in ['deleted', 'bypassed']:
            LOG.debug("No action on %s: %s:%s->%s", sync_state, orig_inc_id, mapped_type_name, orig_type_id)
            return None, None

        opr_type = None
        # update operation?
        if sync_type_id and sync_inc_id != 0:
            opr_type = "updated"
            # do not allow updates to existing objects originating elsewhere (except incidents)
            if not self.dbsync.is_sync_role_match(sync_role_source) and mapped_type_name != 'incident':
                # allow tasks to update bidirectionally if changes have been made
                object_changed = False
                if mapped_type_name == "task":
                    existing_task_object = self.get_incident_task(sync_type_id)
                    object_changed = self._has_task_changes(existing_task_object, payload)

                if not object_changed:
                    LOG.info("Suppressed bidirectional change to %s:%s->%s", orig_inc_id, mapped_type_name, orig_type_id)
                    return None, None

            LOG.info('updating %s:%s->%s to %s:%s->%s', orig_inc_id, mapped_type_name, orig_type_id,
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
                if type_name != "incident":
                    if retry_count < RETRY_MAX:
                        LOG.warning('[create_update_type] queued to retry %s:%s->%s to %s:%s',
                                    orig_inc_id, mapped_type_name, orig_type_id,
                                    self.rest_client.org_id, sync_inc_id)
                        # notes can have parent_id
                        self.dbsync.create_retry_row(orig_org_id, orig_inc_id,
                                                     self.return_type_parent(mapped_type_name, default_type="note" if is_child_note else "incident"),
                                                     orig_type_id,
                                                     mapped_type_name, sync_task_id if sync_task_id else orig_inc_id,
                                                     sync_inc_id, payload, retry_count+1)
                    else:
                        LOG.error(MAX_RETRY_TEMPLATE,
                                  mapped_type_name, orig_org_id, orig_inc_id, orig_type_id, sync_inc_id, payload)
        else:
            opr_type = "created"
            # all types to be created
            # make sure the incident already exists for child objects
            if mapped_type_name != 'incident':
                sync_inc_id, sync_state, incident_sync_role_source = self.dbsync.find_incident(orig_org_id, orig_inc_id)

                # do nothing if already deleted, bypassed or filtered
                if sync_state in ['deleted', 'bypassed', 'filtered']:
                    LOG.debug("No action on %s: %s:%s->%s", sync_state, orig_inc_id, mapped_type_name, orig_type_id)
                    return None, None

                # a missing incident means the order of creating the child is incorrect.
                # this happens when creating an incident with incident_type_ids and the tasks show up first in the
                # message destination
                if sync_inc_id is None:
                    if retry_count < RETRY_MAX:
                        LOG.warning('[create_update_type] Incident not found. Queued to retry %s:%s->%s to %s', orig_inc_id, type_name, orig_type_id,
                                    self.rest_client.org_id)
                        self.dbsync.create_retry_row(orig_org_id, orig_inc_id,
                                                     self.return_type_parent(mapped_type_name, default_type="note" if is_child_note else "incident"),
                                                     orig_type_id,
                                                     mapped_type_name, orig_task_id if orig_task_id else orig_inc_id,
                                                     orig_inc_id, payload, retry_count+1)
                    else:
                        LOG.error(MAX_RETRY_TEMPLATE,
                                  type_name, orig_org_id, orig_inc_id, orig_type_id, sync_inc_id, payload)

                    return None, None

                if sync_inc_id == 0:
                    # this is a child object to an incident which was filtered
                    LOG.info("filtering %s:%s->%s", type_name, orig_inc_id, orig_type_id)
                    return None, None

            # creating a task? may already have one created when the incident was created
            if mapped_type_name == "task":
                # Is this an unmapped task created with the incident?
                new_task_type_id = self._find_task(sync_inc_id, payload)
                # duplicates occur when incident types automatically create tasks
                if not new_task_type_id:
                    # creating a task doesn't use instr_text field
                    payload.pop('instr_text', None)

                    sync_inc_id, new_type_id = self.create_type(orig_org_id, orig_inc_id, orig_type_id,
                                                                mapped_type_name, type_name,
                                                                sync_inc_id, sync_task_id, payload, retry_count)
                else:
                    LOG.debug('duplicate %s:%s->%s of %s:%s->%s', type_name, orig_inc_id, orig_type_id,
                              self.rest_client.org_id, sync_inc_id, new_task_type_id)
                    LOG.debug(payload)

                    # create sync row, duplicates are mapped too
                    self.dbsync.create_sync_row(orig_org_id, orig_inc_id, type_name, orig_type_id,
                                                sync_inc_id, new_task_type_id, 'active',
                                                sync_role_source = incident_sync_role_source)

                    new_type_id = new_task_type_id # value triggers retry on dependent objects

            else:
                # all types not an incident or task
                if payload or sync_inc_id:
                    if mapped_type_name in ('tasknote', 'taskattachment') and not sync_task_id:
                        LOG.warning('[create_update_type] task not yet created, queued to retry %s:%s->%s:%s to %s:%s',
                                    orig_inc_id, mapped_type_name,
                                    orig_task_id, orig_type_id,
                                    self.rest_client.org_id, sync_inc_id)
                        self.dbsync.create_retry_row(orig_org_id, orig_inc_id,
                                                     self.return_type_parent(mapped_type_name), orig_type_id,
                                                     mapped_type_name, orig_task_id,
                                                     sync_inc_id, payload, 1)
                        new_type_id = 0
                    else:
                        sync_inc_id, new_type_id = self.create_type(orig_org_id, orig_inc_id, orig_type_id,
                                                                    mapped_type_name, type_name,
                                                                    sync_inc_id, sync_task_id, payload, retry_count)

                else:
                    # filtered objects occur when matching criteria fails
                    LOG.info("filtering %s:%s->%s", type_name, orig_inc_id, orig_type_id)
                    sync_inc_id = new_type_id = 0

                    # create sync row - even if filtered
                    self.dbsync.create_sync_row(orig_org_id, orig_inc_id, type_name, orig_type_id,
                                                sync_inc_id, new_type_id, 'filtered')

        return new_type_id, opr_type

    def create_type(self, orig_org_id, orig_inc_id, orig_type_id,
                    mapped_type_name, type_name,
                    sync_inc_id, sync_task_id, payload, retry_count):
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
        :param retry_count
        :return: sync_inc_id, new_type_id
        """
        # create object
        if sync_task_id:
            LOG.debug('adding %s:%s->%s to %s:%s->%s',
                      orig_inc_id, mapped_type_name, orig_type_id,
                      self.rest_client.org_id, sync_inc_id, sync_task_id)
        else:
            LOG.debug('adding %s:%s->%s to %s:%s',
                      orig_inc_id, mapped_type_name, orig_type_id,
                      self.rest_client.org_id, sync_inc_id)

        try:
            sync_inc_id, new_type_id = self._create_type(sync_inc_id, sync_task_id, mapped_type_name, payload)

            if new_type_id:
                # create sync row, duplicates are now mapped too
                self.dbsync.create_sync_row(orig_org_id, orig_inc_id, mapped_type_name, orig_type_id,
                                            sync_inc_id, new_type_id, 'active')
                LOG.info('added %s:%s->%s to %s:%s->%s',
                         orig_inc_id, mapped_type_name, orig_type_id,
                         self.rest_client.org_id, sync_inc_id, new_type_id)
        except (IntegrationError, Exception):
            new_type_id = None
            # can't requeue incidents as nothing triggers a retry
            if type_name != "incident":
                if retry_count < RETRY_MAX:
                    LOG.warning('[create_type] queued to retry %s:%s->%s to %s:%s', orig_inc_id, mapped_type_name, orig_type_id,
                                self.rest_client.org_id, sync_inc_id)
                    self.dbsync.create_retry_row(orig_org_id, orig_inc_id, self.return_type_parent(mapped_type_name), orig_type_id,
                                                 mapped_type_name, orig_inc_id,
                                                 sync_inc_id, payload, retry_count+1)
                else:
                    LOG.error(MAX_RETRY_TEMPLATE,
                              mapped_type_name, orig_org_id, orig_inc_id, orig_type_id, sync_inc_id, payload)


        return sync_inc_id, new_type_id

    def _create_type(self, sync_inc_id, sync_task_id, mapped_type_name, payload):
        """
        create the new object: incident, note, artifact, milestone, task
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
            extra_msg = None
            if "Invalid field name" in str(err):
                extra_msg = "Make sure all custom fields are imported into the target organization."

            LOG.error("Unable to create %s, Incident %s, %s. %s", mapped_type_name, sync_inc_id,
                      err, extra_msg)
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
        response = self.get_incident_tasks(sync_inc_id)

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
        update_uri = f"{uri}/{sync_type_id}?handle_format=names"

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
        if not existing_object:
            LOG.error("Unable to find existing object to update %s %s, Incident %s", mapped_type_name, sync_type_id, sync_inc_id)
            return None

        # check if changes to incidents to avoid endless bidirectional updates
        if mapped_type_name == 'incident' and not self._has_incident_changes(existing_object, payload):
            LOG.info("No changes available for %s:%s->%s", mapped_type_name, sync_inc_id, existing_object["id"])
            return None

        # some objects have 'vers' and others have 'version'
        key = [vers for vers in ['vers', 'version'] if vers in existing_object]
        if key:
            ## collect the version number
            version = existing_object[key[0]]
            ## add correct version number
            payload[key[0]] = version

        try:
            _response = self.rest_client.put(update_uri, payload)

        except Exception as err:
            LOG.warning("Unable to update %s %s, Incident %s, %s", mapped_type_name, sync_type_id, sync_inc_id, err)
            LOG.debug(update_uri)
            LOG.debug(payload)
            raise IntegrationError(str(err))

        return None

    def _has_incident_changes(self, existing_incident_payload, new_incident_payload):
        """ _has_incident_changes will compare incident payloads for any changes.
        :param existing_incident_payload: dictionary of existing incident data
        ;param new_incident_payload: dictionary of changes to sync (if any).
        :return: True if changes found, False otherwise
        """
        has_changes = False

        try:
            # Iterate over payload dict.
            for name, value in new_incident_payload.items():
                # some fields will be different which we shouldn't track
                if name in BYPASS_FIELDS:
                    continue

                if isinstance(value, dict) and isinstance(existing_incident_payload, dict):
                    it_changed = self._has_incident_changes(existing_incident_payload.get(name, {}), value)
                elif isinstance(existing_incident_payload, dict):
                    it_changed = bool(value != existing_incident_payload.get(name))
                else:
                    it_changed = bool(value != existing_incident_payload)

                if it_changed:
                    LOG.debug(f"{name}: {value}/{existing_incident_payload.get(name) if isinstance(existing_incident_payload, dict) else existing_incident_payload}")
                has_changes |= it_changed
            return has_changes
        except Exception as err:
            LOG.error(str(err))
            LOG.error(traceback.format_exc())
            return False

    def _has_task_changes(self, existing_task_object, updated_task_object):
        """certain fields for a task need to change in order to sync.

        :param existing_task_object: existing task
        :type existing_task_object: dict
        :param updated_task_object: updated task
        :type updated_task_object: dict
        :return: true if the task has changed
        :rtype: bool
        """
        return any([updated_task_object[field] != existing_task_object[field] \
                           for field in ["due_date", "status", "owner_id"]])

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
    
    def _return_mapped_type_name(self, type_name, payload):
        """ determine the correct type_name based on parent type """
        if type_name in ["note", "attachment"] and payload.get("type", "") == "task":
            return f"task{type_name}"

        return type_name

    def _map_parent(self, orig_org_id, orig_inc_id, type_name, payload):
        """
        task notes and attachments, and notes have parent_ids. Find them in the sync_row db
        :param orig_org_id
        :param orig_inc_id
        :param type_name:
        :param payload:
        :return: "tasknote" for task notes, otherwise the original value
        """
        child_note = False
        sync_state = orig_task_id = sync_task_id = None
        mapped_type_name = self._return_mapped_type_name(type_name, payload)

        # child note?
        if mapped_type_name in ["note", "tasknote"] and payload.get("parent_id"):
            child_note = True
            # notes can be hierarchical. Look for the parent note and update the payload if found
            _, sync_parent_note_id, sync_state, _sync_role_source = self.dbsync.find_sync_row(orig_org_id, orig_inc_id,
                                                                                         mapped_type_name, payload.get("parent_id"))
            if sync_parent_note_id:
                payload['parent_id'] = sync_parent_note_id

        # task object? retries come back as "tasknote" and "taskattachment"
        if mapped_type_name in ["tasknote", "note", "taskattachment", "attachment"] and payload.get("type", "") == "task":
            # get the sync_task_id for this task comment/attachment
            _, sync_task_id, sync_state, _sync_role_source = self.dbsync.find_sync_row(orig_org_id, orig_inc_id,
                                                                                       "task", payload.get("task_id"))
            # set the org2 task_id
            if sync_task_id:
                orig_task_id = payload["task_id"]
                payload["task_id"] = sync_task_id

        # do nothing if already deleted or bypassed
        if sync_state in ['deleted', 'bypassed']:
            LOG.debug("No action on %s: %s:%s", sync_state, orig_inc_id, mapped_type_name)
            return None, None, None, child_note

        return orig_task_id, sync_task_id, mapped_type_name, child_note

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
        new_type_id = None

        src_artifact_id = src_attachment_id = src_task_id = dst_task_id = None
        if payload.get('attachment', {}).get('content_type', None):
            src_artifact_id = orig_type_id
        else:
            src_attachment_id = orig_type_id

        # find the incident for this attachment
        sync_inc_id, sync_state, _sync_role_source = self.dbsync.find_incident(orig_org_id, orig_inc_id)

        # do nothing if incident already deleted, bypassed or filtered
        if sync_state in ['deleted', 'bypassed', 'filtered']:
            LOG.debug("No action on %s: %s:%s->%s", sync_state, orig_inc_id, type_name, orig_type_id)
            return None

        # is this a task based attachment?
        if payload.get("task_id", None):
            src_task_id = payload.get("task_id")
            _, dst_task_id, sync_state, _sync_role_source = self.dbsync.find_sync_row(orig_org_id, orig_inc_id,
                                                                                      "task", src_task_id)
            # if the task doesn't exist, the attachment will be requeued
            if not dst_task_id:
                LOG.warning('task:%s not found. Queued to retry %s:%s->%s to %s', src_task_id,
                            orig_inc_id, type_name, orig_type_id,
                            self.rest_client.org_id)
                self.dbsync.create_retry_row(orig_org_id, orig_inc_id, "task", orig_type_id,
                                             type_name if 'task' in type_name else f"task{type_name}", src_task_id,
                                             sync_inc_id, payload, 1)
                return None

        # get the target attachment, if it exists
        _, sync_type_id, _, _sync_role_source = self.dbsync.find_sync_row(orig_org_id, orig_inc_id,
                                                                          type_name, orig_type_id)
        # attachments cannot be updated
        if sync_type_id:
            return None

        # incident missing?
        if not sync_inc_id:
            parent_type_name = "task" if src_task_id else "incident"
            dep_type_id = src_task_id if src_task_id else orig_inc_id
            LOG.warning('%s:%s not found. Queued to retry %s:%s->%s to %s', parent_type_name, dep_type_id,
                        orig_inc_id, type_name, orig_type_id,
                        self.rest_client.org_id)
            self.dbsync.create_retry_row(orig_org_id, orig_inc_id, parent_type_name, orig_type_id,
                                         type_name, dep_type_id,
                                         None, payload, 1)
            return None

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
                response = None

        # create sync row
        if response:
            new_type_id = response.get('id', None)
            self.dbsync.create_sync_row(orig_org_id, orig_inc_id, type_name, orig_type_id,
                                        sync_inc_id, new_type_id, 'active')

            LOG.info('added %s:%s->%s to %s:%s->%s', type_name, orig_inc_id, orig_type_id,
                     self.rest_client.org_id, sync_inc_id, new_type_id)
        else:
            LOG.error('error adding %s:%s->%s to %s:%s', type_name, orig_inc_id, orig_type_id,
                      self.rest_client.org_id, sync_inc_id)

        return new_type_id

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

                # preserve the actual name of the attachment
                file_name_link = os.path.join(os.path.dirname(temp_file.name), file_name)
                os.link(temp_file.name, file_name_link)

                # Create a new artifact attachment by calling resilient REST API
                uri, _ = get_url(incident_id, "artifact")
                artifact_uri = f"{uri}/files"

                new_attachment = self.rest_client.post_artifact_file(artifact_uri,
                                                                     payload.get("type", None),
                                                                     file_name_link,
                                                                     description=payload.get("description", None),
                                                                     value=file_name,
                                                                     mimetype=content_type)
            except Exception as err:
                LOG.exception(err)
                LOG.error("Unable to create attachment for file: %s", file_name)
                LOG.error(artifact_uri)
                LOG.error(payload)
            finally:
                os.unlink(temp_file.name)
                if os.path.exists(file_name_link):
                    os.unlink(file_name_link)

        if isinstance(new_attachment, list):
            new_attachment = new_attachment[0]

        return new_attachment

    def get_source_host(self):
        """ Return the source organization url for API calls"""
        parsed_uri = urlparse(self.rest_client.base_url)
        return parsed_uri.hostname

    @cached(cache=TTLCache(maxsize=10, ttl=600))
    def get_type_info(self, type_name):
        """
        get the field definitions for the object type
        :return: dictionary of field names
        """

        uri = Resilient.GET_FIELDS_URI.format(type_name)
        try:
            fields_by_name = {}
            response = self.rest_client.get(uri)

            for field in response:
                fields_by_name[field['name']] = {
                    "prefix": field['prefix'],
                    "input_type": field['input_type'],
                    "values": field['values']
                }
        except Exception as err:
            LOG.error("get_type_info")
            LOG.error(err)

        return fields_by_name

    @cached(cache=TTLCache(maxsize=128, ttl=60))
    def get_incident_tasks(self, sync_inc_id):
        """
        get all tasks for an incident, if not yet cached or the cache has expired
        :param sync_inc_id:
        :return: list of tasks
        """
        uri = Resilient.GET_INCIDENT_TASKS_URI.format(sync_inc_id)
        return self.rest_client.get(uri)

    def get_incident_task(self, task_id):
        """ return the full task information for the target task"""
        uri = f"{Resilient.GET_TASK_URI}/{task_id}?handle_format=names"
        return self.rest_client.get(uri)

    @cached(cache=TTLCache(maxsize=10, ttl=600))
    def get_users_and_groups(self):
        """
        build list of users from the target organization
        :return: dictionary based on email
        """

        user_list = {}
        group_list = {}
        try:
            response = self.get_users()
            # invert the list by ID
            user_list = {user['email']: user for user in response['data']}

            response = self.rest_client.get(Resilient.GET_GROUPS_URI)
            # invert the list by ID
            group_list = {group['export_key']: group for group in response}
        except Exception as err:
            LOG.error("get_users_and_groups")
            LOG.error(err)

        user_and_group_list = user_list.copy()
        user_and_group_list.update(group_list)

        return user_and_group_list

    @cached(cache=TTLCache(maxsize=1000, ttl=600))
    def get_users_by_user_id(self, user_id):
        """get a user's email based on their id

        :param user_id: user id
        :type user_id: int
        :return: email values
        :rtype: str
        """
        try:
            response = self.get_users()

            for usr in response.get("data", []):
                if user_id == usr.get("id"):
                    return usr.get("email")
        except Exception as err:
            LOG.error("get_users_by_user_id")
            LOG.error(err)

        return None

    @cached(cache=TTLCache(maxsize=2, ttl=600))
    def get_users(self):
        """get all users in an org

        :return: dictionary of responses as:
            "data": [
                { "id", "email", ...}
            ]
        :rtype: dict
        """
        return self.rest_client.post(Resilient.GET_USERS_URI, {})

    def register_configuration(self, source_base_url, source_org_name):
        """ attempt to register this configuration. It's a critical error if this 
        combination exists in reverse as that would be a source/source entry

        :param source_base_url: source host url
        :type source_base_url: host
        :param source_org_name: source host org
        :type source_org_name: host
        :return: True if successful registration, False means source/source configuration detected
        :rtype: bool
        """
        # reverse the lookup as target cannot already be a source
        if self.dbsync.find_registry_entry(self.rest_client.org_name,
                                           self.rest_client.base_url,
                                           source_org_name,
                                           source_base_url):
            return False
        
        self.dbsync.register_source_destination(source_org_name,
                                                source_base_url,
                                                self.rest_client.org_name,
                                                self.rest_client.base_url)

        return True

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
