# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use, line-too-long

import logging
import json
from retry import retry
from threading import Lock, current_thread
#make this conditional for environments which only use sqlite
try:
    import pyodbc
except:
    pass

from .db_sync_common import DBSyncInterface

RETRY_LOCK = Lock()
SYNC_LOCK = Lock()

LOG = logging.getLogger(__name__)

class PostgresDBSync(DBSyncInterface):
    """
    Class for maintaining mapping table in sqlite
    """

    def __init__(self, org_id, connection_info, connection_user, connection_pwd):
        """
        setup the sqlite environment
        :param org_id:
        :param sqlite_file:
        """
        super(PostgresDBSync, self).__init__('NOW()')
        self.connect_str = connection_info
        self.uid = connection_user
        self.pwd = connection_pwd

        self.org_id = org_id

        try:
            # retain a connection pool per thread
            self.THREAD_CONNECTION = {}

            self.create_tables(DBSyncInterface.SYNC_TABLE_DEF, DBSyncInterface.RETRY_TABLE_DEF)
        except pyodbc.Error as err:
            LOG.error("Unable to connect to PostgreSql db: %s", err)

    @retry(pyodbc.OperationalError, tries=10, delay=5, backoff=3, logger=LOG)
    def _reinit(self, connect_str, uid, pwd):
        LOG.info(f"Initializing database connection: {connect_str}")
        # pylint: disable=c-extension-no-member
        connection = pyodbc.connect(connect_str, uid=uid, pwd=pwd, autocommit=True)

        return connection
    
    def create_tables(self, *args):
        """ create db tables
        :param args: CREATE TABLE statement(s)
        :return:
        """
        try:
            cur = self._start_transaction()
            for arg in args:
                cur.execute(arg)
        except pyodbc.Error as err:
            LOG.error("Unable to create table for data feeder sync: %s", err)
        finally:
            cur and cur.close()

    def _start_transaction(self):
        """Creates a new cursor and returns it to the caller.
        :returns A new DB cursor."""
        # is there a connection pool for this thread?
        thread_id = current_thread().ident
        if not thread_id in self.THREAD_CONNECTION:
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
        :param orig_org_id:
        :param orig_inc_id:
        :param type_name:
        :param orig_type_id:
        :return: target_inc_id, target_type_id
        """

        try:
            cur = self._start_transaction()
            cur.execute(self.SYNC_SELECT, (orig_org_id, orig_inc_id, type_name, orig_type_id, self.org_id))

            data = cur.fetchone()
            # row: type_name, org1, org1_inc_id, org1_type_id, org2, org2_inc_id, org2_type_id, last_sync, status
            if data is None:
                return None, None, None

            sync_inc_id = data[5]
            sync_type_id = data[6]
            sync_state = data[8]

            if sync_state == "deleted":
                LOG.debug("%s %s:%s->%s", sync_state, orig_inc_id, type_name, orig_type_id or orig_inc_id)

            return sync_inc_id, sync_type_id, sync_state
        except pyodbc.Error as err:
            LOG.error("find_sync_row err %s", err)
            return None, None, None
        finally:
            cur and cur.close()

    def create_sync_row(self, orig_org_id, orig_inc_id,
                        type_name, orig_type_id,
                        new_inc_id, new_type_id, status):
        """
        add a row or update an existing row to the mapping db to map the source object with the destination object
        :param orig_org_id:
        :param orig_inc_id:
        :param type_name:
        :param orig_type_id:
        :param new_inc_id:
        :param new_type_id:
        :param status: active, filtered, deleted, bypassed
        :return: None
        """

        with SYNC_LOCK:
            try:
                cur = self._start_transaction()

                cur.execute(self.SYNC_UPSERT, (orig_org_id, orig_inc_id, type_name, orig_type_id,
                                               self.org_id, new_inc_id, new_type_id, status,
                                               new_inc_id, new_type_id, status))


                self._commit_transaction()
            except pyodbc.Error as err:
                LOG.error("create_sync_row err %s", err)
            finally:
                cur and cur.close()

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
        except pyodbc.Error as err:
            LOG.error("update_existing_sync_row err %s", err)
        finally:
            cur and cur.close()

    def find_incident(self, orig_org_id, orig_inc_id):
        """
        determine if the incident has been previous synchronized
        :param orig_org_id:
        :param orig_inc_id:
        :return: found inc_id or None
        """
        sync_inc_id, _, sync_state = self.find_sync_row(orig_org_id, orig_inc_id, "incident", orig_inc_id)

        return sync_inc_id, sync_state

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
        except pyodbc.Error as err:
            LOG.error("delete_type err %s", err)
        finally:
            cur and cur.close()

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
        except pyodbc.Error as err:
            LOG.error("delete_type err %s", err)
        finally:
            cur and cur.close()


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
            except pyodbc.Error as err:
                LOG.error("create_retry_row err %s", err)
            finally:
                cur and cur.close()

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
        except pyodbc.Error as err:
            LOG.error("find_retry_rows failure to get retries. err %s", err)
            return []
        finally:
            cur and cur.close()

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
        except pyodbc.Error as err:
            LOG.error("delete_retry_rows err %s", err)
        finally:
            cur and cur.close()
