# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# pragma pylint: disable=unused-argument, line-too-long

import logging
import json
from .db_sync_common import DBSyncInterface, SyncRowError
from retry import retry
from threading import Lock, current_thread
#make this conditional for environments which only use sqlite
try:
    from pyodbc import Error, OperationalError, connect
except:
    # these are stubs so the app will not fail during initialization
    class Error(Exception):
        pass
    class OperationalError(Exception):
        pass
    def connect(*args, **kwargs):
        raise NotImplementedError()

RETRY_LOCK = Lock()
SYNC_LOCK = Lock()

LOG = logging.getLogger(__name__)

NOW = "NOW()"

class PostgresDBSync(DBSyncInterface):
    """
    Class for maintaining mapping table in sqlite
    """

    def __init__(self, org_id, connection_info, connection_user, connection_pwd, sync_role_source):
        """
        setup the sqlite environment
        :param org_id:
        :param sqlite_file:
        :param sync_role_source: true = 'source', false = 'destination'
        """
        super(PostgresDBSync, self).__init__(NOW, sync_role_source)
        self.connect_str = connection_info
        self.uid = connection_user
        self.pwd = connection_pwd

        self.org_id = org_id

        try:
            # retain a connection pool per thread
            self.THREAD_CONNECTION = {}

            self.create_tables(DBSyncInterface.SYNC_TABLE_DEF,
                               DBSyncInterface.SYNC_TABLE_INDEX,
                               DBSyncInterface.SYNC_TABLE_SYNC_ROLE_SOURCE_POSTGRES,
                               DBSyncInterface.RETRY_TABLE_DEF,
                               DBSyncInterface.REGISTRY_TABLE_DEF)
        except Error as err:
            LOG.error("Unable to connect to PostgreSQL db: %s", err)

        self.REGISTRY_INSERT = DBSyncInterface.POSTGRES_REGISTRY_INSERT.format(table_name=DBSyncInterface.REGISTRY_DBTABLE, now=NOW)

    @retry(OperationalError, tries=10, delay=5, backoff=3, logger=LOG)
    def _reinit(self, connect_str, uid, pwd):
        LOG.info(f"Initializing database connection: {connect_str}")
        # pylint: disable=c-extension-no-member
        connection = connect(connect_str, uid=uid, pwd=pwd, autocommit=True)

        return connection

    def create_tables(self, *args):
        """ create db tables
        :param args: CREATE TABLE statement(s)
        :return:
        """
        try:
            cur = self._start_transaction()
            for arg in args:
                try:
                    cur.execute(arg)
                except Error as err:
                    LOG.error("postgres create_tables error: %s, %s", err, arg)
        finally:
            ("cur" in locals()) and cur.close()

    def _start_transaction(self):
        """Creates a new cursor and returns it to the caller.
        :returns A new DB cursor."""
        # is there a connection pool for this thread?
        thread_id = current_thread().ident
        if thread_id not in self.THREAD_CONNECTION:
            self.THREAD_CONNECTION[thread_id] = self._reinit(self.connect_str, self.uid, self.pwd)

        LOG.debug(f"thread: {thread_id} connection: {self.connect_str} {id(self.THREAD_CONNECTION[thread_id])}")
        return self.THREAD_CONNECTION[thread_id].cursor()

    def _commit_transaction(self):
        """Commits the currently open transaction."""
        thread_id = current_thread().ident
        self.THREAD_CONNECTION[thread_id].commit()

    def _rollback_transaction(self):
        """Rolls back the currently open transaction."""
        thread_id = current_thread().ident
        self.THREAD_CONNECTION[thread_id].rollback()

    def _close_connection(self):
        """Close the connection to the database"""
        thread_id = current_thread().ident
        self.THREAD_CONNECTION[thread_id].close()

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
            cur = self._start_transaction()
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
            raise SyncRowError(err)
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
                cur = self._start_transaction()

                cur.execute(self.SYNC_UPSERT, (orig_org_id, orig_inc_id, type_name, orig_type_id,
                                               self.org_id, new_inc_id, new_type_id, status,
                                               str(sync_role_source if sync_role_source else self.my_sync_role_source).upper(),
                                               status))

                self._commit_transaction()
            except Error as err:
                LOG.error("create_sync_row err %s", err)
                LOG.error(f"cmd: {self.SYNC_UPSERT}")
                LOG.error((orig_org_id, orig_inc_id, type_name, orig_type_id,
                           self.org_id, new_inc_id, new_type_id, status))
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
            cur = self._start_transaction()
            cur.execute(self.SYNC_UPDATE, (self.org_id, target_inc_id, type_name, target_type_id))

            self._commit_transaction()
        except Error as err:
            LOG.error("update_existing_sync_row err %s", err)
            raise SyncRowError(err)
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
            cur = self._start_transaction()

            cur.execute(self.SYNC_DELETE_TYPE, (status, org2_id, org2_inc_id, type_name, org2_type_id))

            self._commit_transaction()
        except Error as err:
            LOG.error("delete_type err %s", err)
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
            cur = self._start_transaction()

            cur.execute(self.SYNC_DELETE_INCIDENT, (status, org2_id, org2_inc_id))

            self._commit_transaction()
        except Error as err:
            LOG.error("delete_type err %s", err)
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
                cur = self._start_transaction()
                # (org1, org1_inc_id, type_name, org1_type_id,
                #     org1_dep_type_name, org1_dep_type_id,
                #     org2, org2_inc_id, payload, last_attempt)

                if isinstance(payload, dict):
                    new_payload = payload.copy()
                    new_payload = json.dumps(new_payload)
                else:
                    new_payload = payload

                cur.execute(self.RETRY_UPSERT, (orig_org_id, orig_inc_id, type_name, orig_type_id,
                                                org1_dep_type_name, org1_dep_type_id,
                                                self.org_id, new_inc_id, new_payload, retry_count))

                self._commit_transaction()
            except Error as err:
                LOG.error("create_retry_row err %s", err)
                raise SyncRowError(err)
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
            cur = self._start_transaction()
            cur.execute(self.RETRY_SELECT, (orig_org_id, orig_inc_id, type_name, self.org_id))

            result_list = cur.fetchall()

            # remove the items as they may be readded
            if result_list:
                cur.execute(self.RETRY_DELETE, (orig_org_id, orig_inc_id, type_name, self.org_id))

            return result_list
        except Error as err:
            LOG.error("find_retry_rows failure to get retries. err %s", err)
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
            cur = self._start_transaction()
            cur.execute(self.RETRY_DELETE, (orig_org_id, orig_inc_id, type_name, orig_type_id, self.org_id))

            self._commit_transaction()
        except Error as err:
            LOG.error("delete_retry_rows err %s", err)
        finally:
            ("cur" in locals()) and cur.close()

    def find_registry_entry(self,
                            source_org_name,
                            source_base_url,
                            destination_org_name,
                            destination_base_url):
        try:
            cur = self._start_transaction()
            cur.execute(PostgresDBSync.REGISTRY_SELECT, (source_org_name, source_base_url, 
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
            cur = self._start_transaction()

            cur.execute(self.REGISTRY_INSERT, (source_org_name, source_base_url, 
                                               destination_org_name, destination_base_url))

            self._commit_transaction()
        except Error as err:
            LOG.error("register_source_destination err %s", err)
            raise SyncRowError(err)
        finally:
            ("cur" in locals()) and cur.close()
