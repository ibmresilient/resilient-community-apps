# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# pragma pylint: disable=unused-argument, line-too-long

import logging
import json
import sqlite3
from sqlite3 import Error
from threading import Lock
from .db_sync_common import DBSyncInterface, SyncRowError

RETRY_LOCK = Lock()
SYNC_LOCK = Lock()

LOG = logging.getLogger(__name__)
NOW ="datetime('now')"

class SQLiteDBSync(DBSyncInterface):
    """
    Class for maintaining mapping table in sqlite
    """

    def __init__(self, org_id, sqlite_file, is_source_role):
        """
        setup the sqlite environment
        :param org_id:
        :param sqlite_file:
        :param is_source_role: True for synchronizing to the target
        """
        super(SQLiteDBSync, self).__init__(NOW, is_source_role)

        self.org_id = org_id
        self.log = logging.getLogger(__name__)

        try:
            self.sqlite_db = sqlite3.connect(sqlite_file, check_same_thread=False)

            self.create_tables(DBSyncInterface.SYNC_TABLE_DEF,
                               DBSyncInterface.SYNC_TABLE_INDEX,
                               DBSyncInterface.SYNC_TABLE_SYNC_ROLE_SOURCE_SQLITE,
                               DBSyncInterface.RETRY_TABLE_DEF,
                               DBSyncInterface.REGISTRY_TABLE_DEF)
        except Error as err:
            self.log.error("Unable to use file for data feeder sync: %s", err)

        self.REGISTRY_INSERT = DBSyncInterface.SQLITE_REGISTRY_INSERT.format(table_name=DBSyncInterface.REGISTRY_DBTABLE, now=NOW)

    def create_tables(self, *args):
        """ create db tables
        :param args: CREATE TABLE statement(s)
        :return:
        """
        try:
            cur = self.sqlite_db.cursor()
            for arg in args:
                try:
                    cur.execute(arg)
                except Error as err:
                    self.log.error("sqlite create_tables error: %s %s", err, arg)
        finally:
            ("cur" in locals()) and cur.close()


    def find_sync_row(self, orig_org_id, orig_inc_id, type_name, orig_type_id):
        """
        determine if we have already synchronized this object in the destination organization
        
        Different queries are used whether this is a source or target 
        :param orig_org_id:
        :param orig_inc_id:
        :param type_name:
        :param orig_type_id:
        :return: target_inc_id, target_type_id, sync_status, sync_role_source
        """

        try:
            cur = self.sqlite_db.cursor()
            cur.execute(self.SYNC_SELECT, (orig_org_id, orig_inc_id, type_name, orig_type_id, self.org_id))

            data = cur.fetchone()
            # row: type_name, org1, org1_inc_id, org1_type_id, org2, org2_inc_id, org2_type_id, last_sync, status, sync_role_source
            if data is None:
                return None, None, None, None

            sync_inc_id = data[5]
            sync_type_id = data[6]
            sync_state = data[8]
            sync_role_source = data[9]

            if sync_state == "deleted":
                LOG.debug("%s %s:%s->%s", sync_state, orig_inc_id, type_name, orig_type_id or orig_inc_id)

            return sync_inc_id, sync_type_id, sync_state, sync_role_source
        except Error as err:
            LOG.error("find_sync_row err %s", err)
            return None, None, None, None
        finally:
            ("cur" in locals()) and cur.close()

    def create_sync_row(self, orig_org_id, orig_inc_id,
                        type_name, orig_type_id,
                        new_inc_id, new_type_id, status,
                        sync_role_source = None):
        """
        add a row or update an existing row to the mapping db to map the source object with the destination object
        :param orig_org_id:
        :param orig_inc_id:
        :param type_name:
        :param orig_type_id:
        :param new_inc_id:
        :param new_type_id:
        :param status: active, filtered, deleted, bypassed
        :param sync_role_source: if an override is needed to the default setting
        :return: None
        """

        with SYNC_LOCK:
            try:
                cur = self.sqlite_db.cursor()

                cur.execute(self.SYNC_UPSERT, (orig_org_id, orig_inc_id, type_name, orig_type_id,
                                               self.org_id, new_inc_id, new_type_id, status,
                                               str(sync_role_source if sync_role_source else self.my_sync_role_source).upper(),
                                               status))

                self.sqlite_db.commit()
            except Error as err:
                self.log.error("create_sync_row err %s", err)
                raise SyncRowError(err)
            finally:
                ("cur" in locals()) and cur.close()

    def update_existing_sync_row(self, target_inc_id, type_name, target_type_id):
        """
        update the existing sync row. For incidents, this could be adding the destination inc_id when the filter
        criteria has been met. Otherwise, the last_sync timestamp is updated.
        :param target_inc_id:
        :param type_name:
        :param target_type_id:
        :return:
        """
        try:
            cur = self.sqlite_db.cursor()
            cur.execute(self.SYNC_UPDATE, (self.org_id, target_inc_id, type_name, target_type_id))

            self.sqlite_db.commit()
        except Error as err:
            self.log.error("update_existing_sync_row err %s", err)
        finally:
            ("cur" in locals()) and cur.close()

    def delete_type(self, org2_id, org2_inc_id, type_name, org2_type_id, status='deleted'):
        """
        delete an entry in the sync table
        :param org2_id:
        :param org2_inc_id:
        :param type_name:
        :param org2_type_id:
        :param status: status value of deleted|bypassed
        :return:
        """
        try:
            cur = self.sqlite_db.cursor()

            cur.execute(self.SYNC_DELETE_TYPE, (status, org2_id, org2_inc_id, type_name, org2_type_id))

            self.sqlite_db.commit()
        except Error as err:
            self.log.error("delete_type err %s", err)
        finally:
            ("cur" in locals()) and cur.close()

    def delete_incident_types(self, org2_id, org2_inc_id, status='deleted'):
        """
        delete all records associated with an incident
        :param org2_id:
        :param org2_inc_id:
        :param status: status value of deleted|bypassed
        :return:
        """
        try:
            cur = self.sqlite_db.cursor()

            cur.execute(self.SYNC_DELETE_INCIDENT, (status, org2_id, org2_inc_id))

            self.sqlite_db.commit()
        except Error as err:
            self.log.error("delete_type err %s", err)
        finally:
            ("cur" in locals()) and cur.close()


    # R E T R Y  F U N C T I O N S
    def create_retry_row(self, orig_org_id, orig_inc_id, type_name, orig_type_id,
                         org1_dep_type_name, org1_dep_type_id,
                         new_inc_id, payload, retry_count):
        """
        add a row and update an existing row to the retry db to map the source object with the dependent object
        :param orig_org_id:
        :param orig_inc_id:
        :param type_name: incident, task - type of object which dep_type_name depends on
        :param orig_type_id: inc_id, task_id, artifact_id, attachment_id
        :param org1_dep_type_name: <datatable>, tasknote, note - dependent object 
        :param org1_dep_type_id: row_id, task_note_id, note_id
        :param new_inc_id:
        :param payload:
        :param retry_count:
        :return: None
        """

        with RETRY_LOCK:
            try:
                cur = self.sqlite_db.cursor()
                # (org1, org1_inc_id, type_name, org1_type_id,
                #     org1_dep_type_name, org1_dep_type_id,
                #     org2, org2_inc_id, payload, last_attempt)

                if isinstance(payload, dict):
                    new_payload = payload.copy()
                    new_payload = json.dumps(new_payload)
                else:
                    new_payload = payload

                cur.execute(self.RETRY_INSERT_OR_REPLACE, (orig_org_id, orig_inc_id, type_name, orig_type_id,
                                                           org1_dep_type_name, org1_dep_type_id,
                                                           self.org_id, new_inc_id, new_payload, retry_count))

                self.sqlite_db.commit()
            except Error as err:
                self.log.error("create_retry_row err %s", err)
            finally:
                ("cur" in locals()) and cur.close()

    def find_retry_rows(self, orig_org_id, orig_inc_id, type_name):
        """
        determine if we have already synchronized this object in the destination organization
        :param orig_org_id:
        :param orig_inc_id:
        :param type_name:
        :param orig_type_id:
        :return: target_inc_id, target_type_id
        """

        try:
            cur = self.sqlite_db.cursor()
            cur.execute(self.RETRY_SELECT, (orig_org_id, orig_inc_id, type_name, self.org_id))

            result_list = cur.fetchall()

            # remove the items as they may be readded
            if result_list:
                cur.execute(self.RETRY_DELETE, (orig_org_id, orig_inc_id, type_name, self.org_id))

            return result_list
        except Error as err:
            self.log.error("find_retry_rows failure to get retries. err %s", err)
            return []
        finally:
            ("cur" in locals()) and cur.close()

    def delete_retry_rows(self, orig_org_id, orig_inc_id, type_name, orig_type_id):
        """
        delete rows from retry table after they have been sync'd
        :param orig_org_id
        :param orig_inc_id
        :param type_name:
        :param orig_type_id:
        :return: None
        """
        try:
            cur = self.sqlite_db.cursor()
            cur.execute(self.RETRY_DELETE, (orig_org_id, orig_inc_id, type_name, orig_type_id, self.org_id))

            self.sqlite_db.commit()
        except Error as err:
            self.log.error("delete_retry_rows err %s", err)
        finally:
            ("cur" in locals()) and cur.close()

    def find_registry_entry(self,
                            source_org_name,
                            source_base_url,
                            destination_org_name,
                            destination_base_url):
        try:
            cur = self.sqlite_db.cursor()
            cur.execute(SQLiteDBSync.REGISTRY_SELECT, (source_org_name, source_base_url, 
                                                       destination_org_name, destination_base_url))
        
            data = cur.fetchone()
            # row: last_restart_ts
            return data[0] if data else None
        except Error as err:
            LOG.error("find_registry_entry err %s", err)
        finally:
            ("cur" in locals()) and cur.close()

    def register_source_destination(self,
                                    source_org_name,
                                    source_base_url,
                                    destination_org_name,
                                    destination_base_url):
        try:
            cur = self.sqlite_db.cursor()

            cur.execute(self.REGISTRY_INSERT, (source_org_name, source_base_url, 
                                               destination_org_name, destination_base_url))

            self.sqlite_db.commit()
        except Error as err:
            LOG.error("register_source_destination err %s", err)
            raise SyncRowError(err)
        finally:
            ("cur" in locals()) and cur.close()
