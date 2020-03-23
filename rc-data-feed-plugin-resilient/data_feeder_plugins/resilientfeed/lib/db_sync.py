# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use, line-too-long

import calendar
import logging
import json
import sqlite3
import time
from sqlite3 import Error

class DBSyncFactory:
    @staticmethod
    def get_dbsync(org_id, sqllite_file):
        if sqllite_file:
            return SQLiteDBSync(org_id, sqllite_file)

        return None

class DBSyncInterface:
    """
    Interface class for methods associated with maintaining mappings between the source and destination
    Resilient objects
    """
    def find_sync_row(self, orig_org_id, orig_inc_id, type_name, orig_type_id):
        pass

    def update_existing_sync_row(self, target_inc_id, type_name, target_type_id):
        pass

    def create_sync_row(self, orig_org_id, orig_inc_id, type_name, orig_type_id,
                        new_inc_id, new_type_id):
        pass

    def find_incident(self, orig_org_id, orig_inc_id):
        pass

    def _get_current_timestamp(self):
        """
        get current epoch value
        """
        return calendar.timegm(time.gmtime())*1000

class SQLiteDBSync(DBSyncInterface):
    """
    Class for maintaining mapping table in sqlite
    """
    DBTABLE = "data_feeder_sync"
    RETRY_DBTABLE = "data_feeder_retry"

    SYNC_TABLE_DEF = """-- mapping table
CREATE TABLE IF NOT EXISTS {table_name} (
    type_name text not null,
    org1 int not null,
    org1_inc_id int not null,
    org1_type_id int not null,
    org2 int not null,
    org2_inc_id int not null,
    org2_type_id int not null,
    last_sync timestamp,
    PRIMARY KEY (org1, org1_inc_id, type_name, org1_type_id, org2, org2_inc_id)
);""".format(table_name=DBTABLE)

    SYNC_TABLE_INDEX = """CREATE UNIQUE INDEX IF NOT EXISTS ix_{table_name} 
ON {table_name}(org2, org2_inc_id, type_name, org2_type_id);""".format(table_name=DBTABLE)

    SYNC_UPSERT = """INSERT INTO {table_name} (org1, org1_inc_id, type_name, org1_type_id, org2, org2_inc_id, org2_type_id, last_sync) 
        VALUES(?, ?, ?, ?, ?, ?, ?, datetime('now'))
        ON CONFLICT(org1, org1_inc_id, type_name, org1_type_id, org2, org2_inc_id) DO UPDATE SET
        org2_inc_id = ?,
        org2_type_id = ?,
        last_sync = datetime('now');""".format(table_name=DBTABLE)
    SYNC_INSERT = """INSERT INTO {table_name} (org1, org1_inc_id, type_name, org1_type_id, org2, org2_inc_id, org2_type_id, last_sync) VALUES(?, ?, ?, ?, ?, ?, ?, datetime('now'));""".format(table_name=DBTABLE)
    SYNC_UPDATE = """UPDATE {table_name} set last_sync=datetime('now') where org2=? and org2_inc_id=? and type_name=? and org2_type_id=?""".format(table_name=DBTABLE)
    SYNC_SELECT = """SELECT type_name, org1, org1_inc_id, org1_type_id, org2, org2_inc_id, org2_type_id, last_sync FROM {table_name} WHERE org1=? and org1_inc_id=? and type_name=? and org1_type_id=? and org2=?""".format(table_name=DBTABLE)

    # R E T R Y  D B
    RETRY_TABLE_DEF = """-- retry table
CREATE TABLE IF NOT EXISTS {table_name} (
    type_name text not null,
    org1 int not null,
    org1_inc_id int not null,
    org1_type_id int not null,
    org1_dep_type_name text not null,
    org1_dep_type_id int,
    org2 int,
    org2_inc_id int,
    payload text,
    last_sync timestamp,
    PRIMARY KEY (org1, org1_inc_id, org2, type_name, org1_dep_type_name, org1_dep_type_id)
    );""".format(table_name=RETRY_DBTABLE)

    RETRY_SELECT = """SELECT org1_type_id, org2_inc_id, org1_dep_type_name, org1_dep_type_id, payload FROM {table_name} 
    WHERE org1=? and org1_inc_id=? and type_name=? and org2=?;""".format(table_name=RETRY_DBTABLE)
    RETRY_UPSERT = """INSERT INTO {table_name} (org1, org1_inc_id, type_name, org1_type_id, 
        org1_dep_type_name, org1_dep_type_id, org2, org2_inc_id, payload, last_sync)
        VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, datetime('now'))
        ON CONFLICT(org1, org1_inc_id, org2, type_name, org1_dep_type_name, org1_dep_type_id) 
        DO UPDATE SET last_sync = datetime('now');""".format(table_name=RETRY_DBTABLE)
    RETRY_DELETE = """DELETE from {table_name}  
        WHERE org1=? and org1_inc_id=? and type_name=? and org2=?;""".format(table_name=RETRY_DBTABLE)


    def __init__(self, org_id, sqlite_file):
        """
        setup the sqlite environment
        :param org_id:
        :param sqlite_file:
        """
        self.org_id = org_id
        self.log = logging.getLogger(__name__)

        try:
            self.sqlite_db = sqlite3.connect(sqlite_file)

            self.create_table(SQLiteDBSync.SYNC_TABLE_DEF, SQLiteDBSync.RETRY_TABLE_DEF, SQLiteDBSync.SYNC_TABLE_INDEX)
        except Error as e:
            self.log.error("Unable to use file for data feeder sync")

    def create_table(self, *args):
        """ create a table from the create_table_sql statement
        :param create_table_sql: a CREATE TABLE statement
        :return:
        """
        try:
            cur = self.sqlite_db.cursor()
            for arg in args:
                cur.execute(arg)
        except Error as e:
            self.log.error("Unable to create table for data feeder sync", e)


    def find_sync_row(self, orig_org_id, orig_inc_id, type_name, orig_type_id):
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
            cur.execute(SQLiteDBSync.SYNC_SELECT, (orig_org_id, orig_inc_id, type_name, orig_type_id, self.org_id))

            data = cur.fetchone()
            # row: type_name, org1, org1_inc_id, org1_type_id, org2, org2_inc_id, org2_type_id, last_sync
            if data is None:
                return None, None

            # return: sync_inc_id, sync_type_id
            return data[5], data[6]
        except Exception as err:
            self.log.error("find_sync_row err %s", err)
            return None, None

    def create_sync_row(self, orig_org_id, orig_inc_id, type_name, orig_type_id,
                        new_inc_id, new_type_id):
        """
        add a row to the mapping db to map the source object with the destination object
        :param orig_org_id:
        :param orig_inc_id:
        :param type_name:
        :param orig_type_id:
        :param new_inc_id:
        :param new_type_id:
        :return: None
        """

        try:
            now = self._get_current_timestamp()
            cur = self.sqlite_db.cursor()
            cur.execute(SQLiteDBSync.SYNC_UPSERT, (orig_org_id, orig_inc_id, type_name, orig_type_id,
                                                   self.org_id, new_inc_id, new_type_id,
                                                   new_inc_id, new_type_id))

            self.sqlite_db.commit()
        except Exception as err:
            self.log.error("create_sync_row err %s", err)

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
            cur.execute(SQLiteDBSync.SYNC_UPDATE, (self.org_id, target_inc_id, type_name, target_type_id))

            self.sqlite_db.commit()
        except Exception as err:
            self.log.error("update_existing_sync_row err %s", err)

    def find_incident(self, orig_org_id, orig_inc_id):
        """
        determine if the incident has been previous synchronized
        :param orig_org_id:
        :param orig_inc_id:
        :return: found inc_id or None
        """
        sync_inc_id, _ = self.find_sync_row(orig_org_id, orig_inc_id, "incident", orig_inc_id)

        return sync_inc_id


    # R E T R Y  F U N C T I O N S
    def create_retry_row(self, orig_org_id, orig_inc_id, type_name, orig_type_id,
                         org1_dep_type_name, org1_dep_type_id,
                         new_inc_id, payload):
        """
        add a row to the retry db to map the source object with the dependent object
        :param orig_org_id:
        :param orig_inc_id:
        :param type_name:
        :param orig_type_id:
        :param org1_dep_type_name:
        :param org1_dep_type_id:
        :param new_inc_id:
        :param payload:
        :return: None
        """

        try:
            now = self._get_current_timestamp()
            cur = self.sqlite_db.cursor()
            # (org1, org1_inc_id, type_name, org1_type_id,
            #     org1_dep_type_name, org1_dep_type_id,
            #     org2, org2_inc_id, payload, last_sync)

            if isinstance(payload, dict):
                new_payload = payload.copy()
                new_payload = json.dumps(new_payload)
            else:
                new_payload = payload

            cur.execute(SQLiteDBSync.RETRY_UPSERT, (orig_org_id, orig_inc_id, type_name, orig_type_id,
                                                    org1_dep_type_name, org1_dep_type_id,
                                                    self.org_id, new_inc_id, new_payload))

            self.sqlite_db.commit()
        except Exception as err:
            self.log.error("create_retry_row err %s", err)

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
            cur.execute(SQLiteDBSync.RETRY_SELECT, (orig_org_id, orig_inc_id, type_name, self.org_id))

            result_list = cur.fetchall()

            # remove the items as they may be readded
            if result_list:
                cur.execute(SQLiteDBSync.RETRY_DELETE, (orig_org_id, orig_inc_id, type_name, self.org_id))

            return result_list
        except Exception as err:
            self.log.error("find_retry_rows failure to get retries. err %s", err)
            return []

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
            cur.execute(SQLiteDBSync.RETRY_DELETE, (orig_org_id, orig_inc_id, type_name, orig_type_id, self.org_id))

            self.sqlite_db.commit()
        except Exception as err:
            self.log.error("delete_retry_rows err %s", err)
