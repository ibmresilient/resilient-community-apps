# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use, line-too-long

class SyncRowError(Exception):
    """
    Class used to signal DB create Sync Errors. This is critical for bidirectional synchronization
    as errors to create the sync row will cause updates to continue to bounce back and forth between
    the source and target organization environments.

    .. code-block:: python
        raise SyncRowError("Example raising custom error")
    """
    def __init__(self, value=None):
        self.value = value

        # Add a __qualname__ attribute if does not exist - needed for PY27 retry
        if not hasattr(SyncRowError, "__qualname__"):
            setattr(SyncRowError, "__qualname__", SyncRowError.__name__)

    def __str__(self):
        return repr(self.value)


class DBSyncInterface(object):
    """
    Interface class for methods associated with maintaining mappings between the source and destination
    Resilient objects
    This interface is in place to support additional databases
    """
    DBTABLE = "data_feeder_sync"
    RETRY_DBTABLE = "data_feeder_retry"
    REGISTRY_DBTABLE = "data_feeder_registry"

    SYNC_TABLE_DEF = """-- mapping table
    CREATE TABLE IF NOT EXISTS {table_name} (
        type_name text NOT NULL,
        org1 int NOT NULL,
        org1_inc_id int NOT NULL,
        org1_type_id int NOT NULL,
        org2 int NOT NULL,
        org2_inc_id int,
        org2_type_id int,
        last_sync timestamp,
        status text NOT NULL,
        sync_role_source bool,
        PRIMARY KEY (org1, org1_inc_id, type_name, org1_type_id, org2)
    );""".format(table_name=DBTABLE)
    SYNC_TABLE_INDEX = """CREATE UNIQUE INDEX IF NOT EXISTS org2_index on {table_name}
        (org2, org2_inc_id, type_name, org2_type_id, org1);""".format(table_name=DBTABLE)
    SYNC_TABLE_SYNC_ROLE_SOURCE_POSTGRES = """ALTER TABLE {table_name} add column IF NOT EXISTS sync_role_source bool;""".format(table_name=DBTABLE)
    SYNC_TABLE_SYNC_ROLE_SOURCE_SQLITE = """ALTER TABLE {table_name} add column sync_role_source bool;""".format(table_name=DBTABLE)

    # R E T R Y  D B
    RETRY_TABLE_DEF = """-- retry table
    CREATE TABLE IF NOT EXISTS {table_name} (
        type_name text NOT NULL,
        org1 int NOT NULL,
        org1_inc_id int NOT NULL,
        org1_type_id int NOT NULL,
        org1_dep_type_name text NOT NULL,
        org1_dep_type_id int,
        org2 int,
        org2_inc_id int,
        payload text,
        last_attempt timestamp,
        retry_count int,
        PRIMARY KEY (org1, org1_inc_id, org2, type_name, org1_type_id, org1_dep_type_name, org1_dep_type_id)
        );""".format(table_name=RETRY_DBTABLE)

    # R E G I S T R Y  D B
    REGISTRY_TABLE_DEF = """--- registry table
    CREATE TABLE IF NOT EXISTS {table_name} (
        source_org text NOT NULL,
        source_host text NOT NULL,
        destination_org text NOT NULL,
        destination_host text NOT NULL,
        last_restart_ts timestamp,
        PRIMARY KEY (source_org, source_host, destination_org, destination_host)
        );""".format(table_name=REGISTRY_DBTABLE)

    SQLITE_REGISTRY_INSERT = """INSERT OR REPLACE INTO {table_name} (source_org, source_host, destination_org, destination_host, last_restart_ts) 
        VALUES (?, ?, ?, ?, {now});"""
    POSTGRES_REGISTRY_INSERT = """INSERT INTO {table_name} (source_org, source_host, destination_org, destination_host, last_restart_ts)
    VALUES (?, ?, ?, ?, {now})
    ON CONFLICT (source_org, source_host, destination_org, destination_host)
    DO UPDATE SET last_restart_ts={now}"""
    REGISTRY_SELECT = """SELECT last_restart_ts
        FROM {table_name}
        WHERE source_org=? and source_host=? 
        AND destination_org=? and destination_host=?;""".format(table_name=REGISTRY_DBTABLE)
    #V2.0
    """
    alter table data_feeder_sync add column sync_role_source bool;
    """

    def __init__(self, now_funct, sync_role_source):
        # sync_role_source value = target if source_role==source
        # this removes infinite updates from occurring
        self.my_sync_role_source = sync_role_source
        # different queries are create based on role (source or target)
        if self.my_sync_role_source:
            self.SYNC_SELECT = """SELECT type_name, org1, org1_inc_id, org1_type_id, org2, org2_inc_id, org2_type_id, last_sync, status, sync_role_source
                FROM {table_name}
                WHERE org1=? and org1_inc_id=? and type_name=? and org1_type_id=? and org2=?""".format(table_name=DBSyncInterface.DBTABLE)
            self.SYNC_UPSERT = """INSERT INTO {table_name} (org1, org1_inc_id, type_name, org1_type_id, org2, org2_inc_id, org2_type_id, last_sync, status, sync_role_source)
                VALUES(?, ?, ?, ?, ?, ?, ?, {now}, ?, ?)
                ON CONFLICT(org1, org1_inc_id, type_name, org1_type_id, org2) DO UPDATE SET
                last_sync = {now},
                status= ?;""".format(table_name=DBSyncInterface.DBTABLE,
                                     now=now_funct)
            self.SYNC_UPDATE = """UPDATE {table_name} set last_sync={now}
                WHERE org2=? and org2_inc_id=? and type_name=? and org2_type_id=?""".format(table_name=DBSyncInterface.DBTABLE,
                                                                                            now=now_funct)

            self.SYNC_DELETE_TYPE = """UPDATE {table_name} set last_sync={now}, status=?
                WHERE org2=? and org2_inc_id=? and type_name=? and org2_type_id=?;""".format(table_name=DBSyncInterface.DBTABLE, now=now_funct)
            self.SYNC_DELETE_INCIDENT = """UPDATE {table_name} set last_sync={now}, status=?
                WHERE org2=? and org2_inc_id=?;""".format(table_name=DBSyncInterface.DBTABLE, now=now_funct)
        else:
            self.SYNC_SELECT = """SELECT type_name, org2, org2_inc_id, org2_type_id, org1, org1_inc_id, org1_type_id, last_sync, status, sync_role_source
                FROM {table_name}
                WHERE org2=? and org2_inc_id=? and type_name=? and org2_type_id=? and org1=?""".format(table_name=DBSyncInterface.DBTABLE)
            self.SYNC_UPSERT = """INSERT INTO {table_name} (org2, org2_inc_id, type_name, org2_type_id, org1, org1_inc_id, org1_type_id, last_sync, status, sync_role_source)
                VALUES(?, ?, ?, ?, ?, ?, ?, {now}, ?, ?)
                ON CONFLICT(org2, org2_inc_id, type_name, org2_type_id, org1) DO UPDATE SET
                last_sync = {now},
                status= ?;""".format(table_name=DBSyncInterface.DBTABLE,
                                     now=now_funct)
            self.SYNC_UPDATE = """UPDATE {table_name} set last_sync={now}
                WHERE org1=? and org1_inc_id=? and type_name=? and org1_type_id=?""".format(table_name=DBSyncInterface.DBTABLE,
                                                                                            now=now_funct)

            self.SYNC_DELETE_TYPE = """UPDATE {table_name} set last_sync={now}, status=?
                WHERE org1=? and org1_inc_id=? and type_name=? and org1_type_id=?;""".format(table_name=DBSyncInterface.DBTABLE, now=now_funct)
            self.SYNC_DELETE_INCIDENT = """UPDATE {table_name} set last_sync={now}, status=?
                WHERE org1=? and org1_inc_id=?;""".format(table_name=DBSyncInterface.DBTABLE, now=now_funct)

        #common
        self.RETRY_SELECT = """SELECT org1_type_id, org2_inc_id, org1_dep_type_name, org1_dep_type_id, payload, retry_count FROM {table_name}
                WHERE org1=? and org1_inc_id=? and type_name=? and org2=?;""".format(table_name=DBSyncInterface.RETRY_DBTABLE)
        self.RETRY_INSERT_OR_REPLACE = """INSERT OR REPLACE INTO {table_name} (org1, org1_inc_id, type_name, org1_type_id,
                org1_dep_type_name, org1_dep_type_id, org2, org2_inc_id, payload, last_attempt, retry_count)
                VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, {now}, ?)""".format(table_name=DBSyncInterface.RETRY_DBTABLE, now=now_funct)
        self.RETRY_UPSERT = """INSERT INTO {table_name} (org1, org1_inc_id, type_name, org1_type_id,
                org1_dep_type_name, org1_dep_type_id, org2, org2_inc_id, payload, last_attempt, retry_count)
                VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, {now}, ?)
                ON CONFLICT(org1, org1_inc_id, org2, type_name, org1_type_id, org1_dep_type_name, org1_dep_type_id)
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
        determine if the incident has been previous synchronized
        :param orig_org_id:
        :param orig_inc_id:
        :return: found inc_id or None
        """
        sync_inc_id, _, sync_state, sync_role_source = self.find_sync_row(orig_org_id, orig_inc_id, "incident", orig_inc_id)

        return sync_inc_id, sync_state, sync_role_source

    def is_sync_role_match(self, sync_role_source):
        """determine if configuration role matches the resilientfeed role.
           The intent is to make sure no updates are made from objects in the 'target' which
           originated in the 'source'. Does not apply to incidents

        :param sync_role_source: true= "source", false= "target"
        :type sync_role_source: bool
        :return: True if values match
        :rtype: bool
        """
        return bool(self.my_sync_role_source == sync_role_source)
    
    def find_registry_entry(self,
                            source_org_name,
                            source_base_url,
                            destination_org_name,
                            destination_base_url):
        raise NotImplementedError("required")
    
    def register_source_destination(self,
                                    source_org_name,
                                    source_base_url,
                                    destination_org_name,
                                    destination_base_url):
        raise NotImplementedError("required")
