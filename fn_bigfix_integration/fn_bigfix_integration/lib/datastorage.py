# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

""" Datastore maintenance functions for Bigfix integration with Resilient circuits Functions  """

import traceback
import sqlite3
import logging
import os

LOG = logging.getLogger(__name__)


class Datastore(object):
    DB_NAME = "resilient_bigfix_integration.db"

    def __init__(self):
        """ Create a connected instance of sqlite connection """
        self.conn = None
        try:
            db_path = self.DB_NAME
            new_db = not os.path.exists(db_path)
            self.conn = sqlite3.connect(db_path, check_same_thread=False)
            if new_db:
                LOG.info("Creating and Configuring new DB")
                self.setup_db()
        except sqlite3.Error as e:
            LOG.error("Failed to connect or configure %s!" % self.DB_NAME)
            LOG.error("Error: %s!" % e.message)

    def setup_db(self):
        """ Create DB tables """
        c = self.conn.cursor()
        c.execute("""CREATE TABLE bigfix_actions (
        bg_action_id integer primary key,
        row_id integer,
        incident_id integer,
        finished integer DEFAULT 0);""")
        self.conn.commit()

    def add_bg_action(self, bg_action_id, row_id, incident_id, finished=0):
        """ Add a new action to the DB, overwriting any row existing for this action id

        :param bg_action_id: Bigfix action id
        :param row_id: Row id of hit in Resilient datatable
        :param incident_id: Resilient incident id
        :param finished: Value to denote if BigFix action completed

        """
        c = self.conn.cursor()
        try:
            c.execute("""INSERT OR REPLACE INTO bigfix_actions (bg_action_id, row_id, incident_id, finished)
            VALUES (?, ?, ?, ?)""", (bg_action_id, row_id, incident_id, finished))
            self.conn.commit()
        except Exception, e:
            LOG.error("Failed to insert bg_action_id %s into DB", str(bg_action_id))
            LOG.error(traceback.format_exc())
            self.conn.rollback()