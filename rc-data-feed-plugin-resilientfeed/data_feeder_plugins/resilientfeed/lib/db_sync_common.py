# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use, line-too-long


class DBSyncInterface(object):
    """
    Interface class for methods associated with maintaining mappings between the source and destination
    Resilient objects
    This interface is in place to support additional databases
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
        org2_inc_id int,
        org2_type_id int,
        last_sync timestamp,
        status text not null,
        PRIMARY KEY (org1, org1_inc_id, type_name, org1_type_id, org2)
    );""".format(table_name=DBTABLE)

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
        last_attempt timestamp,
        retry_count int,
        PRIMARY KEY (org1, org1_inc_id, org2, type_name, org1_dep_type_name, org1_dep_type_id)
        );""".format(table_name=RETRY_DBTABLE)

    def __init__(self, now_funct):
        self.SYNC_INSERT_OR_REPLACE = """INSERT OR REPLACE INTO {table_name} (org1, org1_inc_id, type_name, org1_type_id, org2, org2_inc_id, org2_type_id, last_sync, status)
                VALUES(?, ?, ?, ?, ?, ?, ?, {now}, ?)""".format(table_name=DBSyncInterface.DBTABLE, now=now_funct)

        self.SYNC_UPSERT = """INSERT INTO {table_name} (org1, org1_inc_id, type_name, org1_type_id, org2, org2_inc_id, org2_type_id, last_sync, status)
                VALUES(?, ?, ?, ?, ?, ?, ?, {now}, ?)
                ON CONFLICT(org1, org1_inc_id, type_name, org1_type_id, org2) DO UPDATE SET
                org2_inc_id = ?,
                org2_type_id = ?,
                last_sync = {now},
                status=?;""".format(table_name=DBSyncInterface.DBTABLE, now=now_funct)
        self.SYNC_UPDATE = """UPDATE {table_name} set last_sync={now} where org2=? and org2_inc_id=? and type_name=? and org2_type_id=?""".format(table_name=DBSyncInterface.DBTABLE, now=now_funct)
        self.SYNC_SELECT = """SELECT type_name, org1, org1_inc_id, org1_type_id, org2, org2_inc_id, org2_type_id, last_sync, status FROM {table_name} WHERE org1=? and org1_inc_id=? and type_name=? and org1_type_id=? and org2=?""".format(table_name=DBSyncInterface.DBTABLE)

        self.SYNC_DELETE_TYPE = """UPDATE {table_name} set last_sync={now}, status=? where org2=? and org2_inc_id=? and type_name=? and org2_type_id=?;""".format(table_name=DBSyncInterface.DBTABLE, now=now_funct)
        self.SYNC_DELETE_INCIDENT = """UPDATE {table_name} set last_sync={now}, status=? where org2=? and org2_inc_id=?;""".format(table_name=DBSyncInterface.DBTABLE, now=now_funct)

        self.RETRY_SELECT = """SELECT org1_type_id, org2_inc_id, org1_dep_type_name, org1_dep_type_id, payload, retry_count FROM {table_name}
                WHERE org1=? and org1_inc_id=? and type_name=? and org2=?;""".format(table_name=DBSyncInterface.RETRY_DBTABLE)
        self.RETRY_INSERT_OR_REPLACE = """INSERT OR REPLACE INTO {table_name} (org1, org1_inc_id, type_name, org1_type_id,
                org1_dep_type_name, org1_dep_type_id, org2, org2_inc_id, payload, last_attempt, retry_count)
                VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, {now}, ?)""".format(table_name=DBSyncInterface.RETRY_DBTABLE, now=now_funct)
        self.RETRY_UPSERT = """INSERT INTO {table_name} (org1, org1_inc_id, type_name, org1_type_id,
                org1_dep_type_name, org1_dep_type_id, org2, org2_inc_id, payload, last_attempt, retry_count)
                VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, {now}, ?)
                ON CONFLICT(org1, org1_inc_id, org2, type_name, org1_dep_type_name, org1_dep_type_id)
                DO UPDATE SET last_attempt = {now};""".format(table_name=DBSyncInterface.RETRY_DBTABLE, now=now_funct)
        self.RETRY_DELETE = """DELETE from {table_name}
                WHERE org1=? and org1_inc_id=? and type_name=? and org2=?;""".format(table_name=DBSyncInterface.RETRY_DBTABLE)


    def find_sync_row(self, orig_org_id, orig_inc_id, type_name, orig_type_id):
        """
        find a sync record for a given object
        """
        raise NotImplementedError("required")

    def update_existing_sync_row(self, target_inc_id, type_name, target_type_id):
        """
        update a sync record for a given object
        """
        raise NotImplementedError("required")

    def create_sync_row(self, orig_org_id, orig_inc_id,
                        type_name, orig_type_id,
                        new_inc_id, new_type_id, status):
        """
        create a sync record for a given object
        """
        raise NotImplementedError("required")

    def find_incident(self, orig_org_id, orig_inc_id):
        """
        find an incident sync record for a given object
        """
        raise NotImplementedError("required")
