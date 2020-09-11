# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use, line-too-long

import logging
import json
import sqlite3
from sqlite3 import Error
from .db_sync_common import DBSyncInterface

class SQLiteDBSync(DBSyncInterface):
    """
    Class for maintaining mapping table in sqlite
    """

    def __init__(self, org_id, sqlite_file):
        """
        setup the sqlite environment
        :param org_id:
        :param sqlite_file:
        """
        super("SQLiteDBSync").__init__("datetime('now')")

        self.org_id = org_id
        self.log = logging.getLogger(__name__)

        try:
            self.sqlite_db = sqlite3.connect(sqlite_file)

            self.create_tables(DBSyncInterface.SYNC_TABLE_DEF, DBSyncInterface.RETRY_TABLE_DEF)
        except Error as err:
            self.log.error("Unable to use file for data feeder sync: %s", err)

    def create_tables(self, *args):
        """ create db tables
        :param args: CREATE TABLE statement(s)
        :return:
        """
        try:
            cur = self.sqlite_db.cursor()
            for arg in args:
                cur.execute(arg)
        except Error as err:
            self.log.error("Unable to create table for data feeder sync: %s", err)
        finally:
            cur and cur.close()


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
            cur = self.sqlite_db.cursor()
            cur.execute(self.SYNC_SELECT, (orig_org_id, orig_inc_id, type_name, orig_type_id, self.org_id))

            data = cur.fetchone()
            # row: type_name, org1, org1_inc_id, org1_type_id, org2, org2_inc_id, org2_type_id, last_sync, status
            if data is None:
                return None, None, None

            sync_inc_id = data[5]
            sync_type_id = data[6]
            sync_state = data[8]

            if sync_state == "deleted":
                self.log.debug("%s %s:%s->%s", sync_state, orig_inc_id, type_name, orig_type_id or orig_inc_id)

            return sync_inc_id, sync_type_id, sync_state
        except Error as err:
            self.log.error("find_sync_row err %s", err)
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

        try:
            cur = self.sqlite_db.cursor()
            """
            cur.execute(self.SYNC_UPSERT, (orig_org_id, orig_inc_id, type_name, orig_type_id,
                                                   self.org_id, new_inc_id, new_type_id, status,
                                                   new_inc_id, new_type_id, status))
            """
            cur.execute(self.SYNC_INSERT_OR_REPLACE, (orig_org_id, orig_inc_id, type_name, orig_type_id,
                                                              self.org_id, new_inc_id, new_type_id, status))

            self.sqlite_db.commit()
        except Error as err:
            self.log.error("create_sync_row err %s", err)
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
            cur = self.sqlite_db.cursor()
            cur.execute(self.SYNC_UPDATE, (self.org_id, target_inc_id, type_name, target_type_id))

            self.sqlite_db.commit()
        except Error as err:
            self.log.error("update_existing_sync_row err %s", err)
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
            cur = self.sqlite_db.cursor()

            cur.execute(self.SYNC_DELETE_TYPE, (status, org2_id, org2_inc_id, type_name, org2_type_id))

            self.sqlite_db.commit()
        except Error as err:
            self.log.error("delete_type err %s", err)
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
            cur = self.sqlite_db.cursor()

            cur.execute(self.SYNC_DELETE_INCIDENT, (status, org2_id, org2_inc_id))

            self.sqlite_db.commit()
        except Error as err:
            self.log.error("delete_type err %s", err)
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
        :param type_name:
        :param orig_type_id:
        :param org1_dep_type_name:
        :param org1_dep_type_id:
        :param new_inc_id:
        :param payload:
        :param retry_count:
        :return: None
        """

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
            cur and cur.close()

    def find_retry_rows(self, orig_org_id, orig_inc_id, type_name):
        """
        determine if we have already syncrhonized this object in the destination organization
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
            cur = self.sqlite_db.cursor()
            cur.execute(self.RETRY_DELETE, (orig_org_id, orig_inc_id, type_name, orig_type_id, self.org_id))

            self.sqlite_db.commit()
        except Error as err:
            self.log.error("delete_retry_rows err %s", err)
        finally:
            cur and cur.close()
