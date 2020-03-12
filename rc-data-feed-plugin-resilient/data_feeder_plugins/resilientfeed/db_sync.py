# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use, line-too-long

import calendar
import logging
import sqlite3
import time
#from .constants import DF_ORG_ID, DF_INC_ID
from sqlite3 import Error
#from resilient_lib import IntegrationError

class DBSyncFactory:
    @staticmethod
    def get_dbsync(rest_client, sqllite_file):
        if sqllite_file:
            return SQLiteDBSync(rest_client.org_id, sqllite_file)

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

    def make_sync_key(self, orig_org_id, orig_inc_id, type_name, type_id):
        """
        build the key to the data_feeder_sync datatable
        :param orig_org_id:
        :param orig_inc_id:
        :param type_name:
        :param type_id:
        :return: <org_id>:<inc_id>:<type_name>:<type_id>
        """
        return ":".join((str(orig_org_id), str(orig_inc_id), type_name, str(type_id)))

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

    SYNC_TABLE_DEF = """-- mapping table
CREATE TABLE IF NOT EXISTS {table_name} (
    type_name text,
    org1 int,
    org1_inc_id int,
    org1_type_id int,
    org2 int,
    org2_inc_id int,
    org2_type_id int,
    last_sync timestamp,
    PRIMARY KEY (org1, org1_inc_id, type_name, org1_type_id)
);""".format(table_name=DBTABLE)

    SYNC_TABLE_INDEX = """CREATE [UNIQUE] INDEX IF NOT EXISTS ix_{table_name} 
ON table_name(org2, org2_inc_id, type_name, org2_type_id);""".format(table_name=DBTABLE)

    SYNC_INSERT = """INSERT INTO {table_name} (org1, org1_inc_id, type_name, org1_type_id, org2, org2_inc_id, org2_type_id, last_sync) VALUES(?, ?, ?, ?, ?, ?, ?, ?);""".format(table_name=DBTABLE)
    SYNC_UPDATE = """UPDATE {table_name} set last_sync=? where org2=? and org2_inc_id=? and type_name=? and org2_type_id=?""".format(table_name=DBTABLE)
    SYNC_SELECT = """SELECT * FROM {table_name} WHERE org1=? and org1_inc_id=? and type_name=? and org1_type_id=?""".format(table_name=DBTABLE)
    SYNC_SELECT_REVERSE = """SELECT * FROM {table_name} WHERE org2=? and org2_inc_id=? and type_name=? and org2_type_id=?""".format(table_name=DBTABLE)

    def __init__(self, org_id, sqlite_file):
        self.org_id = org_id
        self.log = logging.getLogger(__name__)

        try:
            self.sqlite_db = sqlite3.connect(sqlite_file)

            self.create_table(SQLiteDBSync.SYNC_TABLE_DEF, SQLiteDBSync.SYNC_TABLE_INDEX)
        except Error as e:
            self.log.error("Unable to use file for data feeder sync")

    def create_table(self, *args):
        """ create a table from the create_table_sql statement
        :param create_table_sql: a CREATE TABLE statement
        :return:
        """
        try:
            c = self.sqlite_db.cursor()
            for arg in args:
                c.execute(arg)
        except Error as e:
            self.log.error("Unable to create table for data feeder sync", e)


    def find_sync_row(self, orig_org_id, orig_inc_id, type_name, orig_type_id):
        """

        :param orig_org_id:
        :param orig_inc_id:
        :param type_name:
        :param orig_type_id:
        :return: target_inc_id, target_type_id
        """

        try:
            cur = self.sqlite_db.cursor()
            cur.execute(SQLiteDBSync.SYNC_SELECT, (orig_org_id, orig_inc_id, type_name, orig_type_id))

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
        add a row to the mapping table to map the source object with the destination object
        :param orig_org_id:
        :param orig_inc_id:
        :param type_name:
        :param orig_type_id:
        :param new_inc_id:
        :param new_type_id:
        :return:
        """
        # (src_org_id, src_inc_id, type_name, orig_id,
        # sync_inc_id, new_type_id)

        try:
            cur = self.sqlite_db.cursor()
            cur.execute(SQLiteDBSync.SYNC_INSERT, (orig_org_id, orig_inc_id, type_name, orig_type_id,
                                                   self.org_id, new_inc_id, new_type_id,
                                                   self._get_current_timestamp()))

            self.sqlite_db.commit()
        except Exception as err:
            self.log.error("create_sync_row err %s", err)

    def update_existing_sync_row(self, target_inc_id, type_name, target_type_id):
        try:
            cur = self.sqlite_db.cursor()
            cur.execute(SQLiteDBSync.SYNC_UPDATE, (self.org_id, target_inc_id, type_name, target_type_id,
                                                   self._get_current_timestamp()))

            self.sqlite_db.commit()
        except Exception as err:
            self.log.error("update_existing_sync_row err %s", err)

    def find_incident(self, orig_org_id, orig_inc_id):
        sync_inc_id, _ = self.find_sync_row(orig_org_id, orig_inc_id, "incident", orig_inc_id)

        return sync_inc_id

'''
class ResDBSync(DBSyncInterface):
    """
    Class for maintaining mapping as a Resilient datatable
    """
    SYNC_DATATABLE_URI = "/incidents/{}/table_data/data_feeder_sync/row_data"

    def __init__(self, rest_client):
        self.log = logging.getLogger(__name__)
        self.rest_client = rest_client

    def find_sync_row(self, orig_org_id, orig_inc_id, type_name, type_id):
        key = self.make_sync_key(orig_org_id, orig_inc_id, type_name, type_id)
        query = {
            "org_id": self.rest_client.org_id,
            "query": str(type_id),
            "types": [
                "datatable"
            ],
            "filters": {
                "data_feeder_sync": [
                    {
                        "conditions": [
                            {
                                "field_name": "key",
                                "method": "equals",
                                "value": [
                                    key
                                ]
                            }
                        ]
                    }
                ]
            },
            "min_required_results": 0
        }

        response = self.rest_client.search(query)
        if len(response['results']) > 1:
            raise IntegrationError("Too many results indicates a consistency error")

        if not response['results']:
            return None, None, None, None, None

        result = response['results'][0]

        # get the type_id
        for _, item in result['result']['cells'].items():
            if item['id']['name'] == 'new_id':
                type_id = item['value']
                break

        return result['inc_id'], type_id, result['obj_id'], result['result']['cells'], result['result']['version']

    def update_existing_sync_row(self, inc_id, row_id, cells, version):
        """
        update last_sync time for datarow
        :param inc_id:
        :param row_id:
        :param cells:
        :param version:
        :return:
        """

        new_cells = cells.copy()
        # update the last sync field
        for cell, body in new_cells.items():
            if body['id']['name'] == 'last_sync':
                body['value'] = self._get_current_timestamp()

        payload = {
            "cells": new_cells,
            "version": version
        }

        uri = "{}/{}".format(ResDBSync.SYNC_DATATABLE_URI.format(inc_id), row_id)
        return self.rest_client.put(uri, payload)

    def create_sync_row(self, orig_org_id, orig_inc_id, type_name, orig_type_id,
                        new_inc_id, new_type_id):
        """
        create a new row in our sync datatable to track this information
        :param orig_inc_id:
        :param orig_org_id:
        :param type_name:
        :param orig_type_id:
        :param new_inc_id:
        :param new_type_id:
        :return:
        """
        key = self.make_sync_key(orig_org_id, orig_inc_id, type_name, orig_type_id)
        payload = {
            "cells": {
                "key": {
                    "value": key
                },
                "new_id": {
                    "value": new_type_id
                },
                "last_sync": {
                    "value": self._get_current_timestamp()
                }
            }
        }

        self.log.debug(payload)
        uri = ResDBSync.SYNC_DATATABLE_URI.format(new_inc_id)
        return self.rest_client.post(uri, payload)

    def find_incident(self, orig_org_id, orig_inc_id):
        """
        Find the incident synchronized from a given inc_id and org_id
        :param orig_org_id:
        :param orig_inc_id:
        :return: found inc_id or None
        """
        uri = "/incidents/query"

        query = {
            "filters": [
                {
                    "conditions": [
                        {
                            "field_name": "properties.{}".format(DF_ORG_ID),
                            "method": "equals",
                            "value": orig_org_id
                        },
                        {
                            "field_name": "properties.{}".format(DF_INC_ID),
                            "method": "equals",
                            "value": orig_inc_id
                        }
                    ]
                }
            ]
        }

        self.log.debug(query)

        response = self.rest_client.post(uri, query)
        if response:
            return response[0]['id']

        return None
'''
