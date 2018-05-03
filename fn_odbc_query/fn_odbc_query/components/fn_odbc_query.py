# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

"""Resilient functions component to execute ODBC queries"""

# Set up:
# Destination: a Queue named "fn_odbc_query".
# Manual Action: Execute an ODBC query.

import logging
import pyodbc
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError

LOG = logging.getLogger(__name__)


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_odbc_query

    The Function executes an ODBC query and takes the following parameters:
        sql_select, sql_field_name, sql_param

    An example of a set of query parameter might look like the following:

        sql_select: "SELECT incident_id, name, description FROM incidents WHERE incident_id = {sql_condition_value}"
        sql_condition_value: artifact.value # Assigned value '1' during run.

    The ODBC query will return a result in JSON format with an entry consisting of a dn and a set of
    attributes for each result.

        {
           "entries": [
                {"dn': "entry1_dn1_value", "entry1_attribute2", "entry1_attribute3", ... },
                {"dn": "entry2_dn2_value", "entry2_attribute2", "entry2_attribute3", ... }
                ...
           ]
        }

    An example of a returned result (Note: some attributes can be arrays):

    """

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_odbc_query", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_odbc_query", {})

    @function("fn_odbc_query")
    def _fn_odbc_query_function(self, event, *args, **kwargs):
        """Resilient Function: A function that makes ODBC queries.

        Inputs:
        sql_select: a query with parameters
        sql_condition_value: condition value

        """

        try:
            # Get the function parameters:
            sql_select = self.get_select_param(kwargs.get("sql_select"))  # select, values: "SELECT incident_id, name, description FROM test.incidents WHERE incident_id = ?"
            sql_condition_value = kwargs.get("sql_condition_value")  # text

            LOG.info("sql_select: %s", sql_select)
            LOG.info("sql_condition_value: %s", sql_condition_value)

            self.search_params = {'sql_select': sql_select, 'sql_condition_value': sql_condition_value}

            yield StatusMessage("starting...")
            # TODO validate data

            yield StatusMessage("Opening ODBC connection...")
            self.setup_odbc_connection()

            yield StatusMessage("Executing an ODBC query...")
            self.execute_odbc_query()

            results = {
                "value": "xyz"
            }

            yield StatusMessage("Closing ODBC connection...")
            self.close_connections()

            yield StatusMessage("done...")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()

    def setup_odbc_connection(self):
        """" Setup ODBC connection to a server database

        Setups up server database and connection objects using credentials obtained from the config file.
        Method also specifies the ODBC driver based on the sql_db_type from the config file.

        For testing purposes I'm connect to MariaDB that lives on my Docker.

        """
        if "sql_server_url" in self.options:
            sql_server_url = self.options["sql_server_url"]
        else:
            raise Exception("Mandatory config setting 'sql_server_url' not set.")

        if "sql_db_type" in self.options:
            sql_db_type = self.options["sql_db_type"]
        else:
            raise Exception("Mandatory config setting 'sql_db_type' not set.")

        if "sql_port" in self.options:
            sql_port = self.options["sql_port"]
        else:
            raise Exception("Mandatory config setting 'sql_port' not set.")

        if "sql_uid" in self.options:
            sql_uid = self.options["sql_uid"]
        else:
            raise Exception("Mandatory config setting 'sql_uid' not set.")

        if "sql_pwd" in self.options:
            sql_pwd = self.options["sql_pwd"]
        else:
            raise Exception("Mandatory config setting 'sql_pwd' not set.")

        # FIXME hardcoded, set driver based on the sql_db_type
        sql_database_driver = "MariaDB ODBC 3.0 Driver"

        pyodbc.pooling = False

        """ FIXME ODBC connection pooling is turned on by default.
        Connections to the SQL server are not closed by default. 
        Some database drivers do not close connections when close() is called in order to save round-trips to the server.
        To close your connection when you call close() you should set pooling to False.
        """

        try:
            connection_string = "DRIVER={{{}}};SERVER={};PORT={};UID={};PWD={};".format(sql_database_driver,
                                                                                            sql_server_url, sql_port,
                                                                                            sql_uid, sql_pwd)


            self.db_connection = pyodbc.connect(connection_string)
            if self.db_connection is None:
                raise Exception("Could not setup the ODBC connection %s, Exception %s", sql_server_url, e)

            self.db_connection.timeout = 60  # FIXME how do we set this? The timeout value, in seconds, for an individual SQL query. Use zero, the default, to disable.

            # This is just an example that works for PostgreSQL and MySQL, with Python 2.7.
            self.db_connection.setdecoding(pyodbc.SQL_WCHAR, encoding='utf-8')

            # Create a cursor from the connection
            self.db_cursor = self.db_connection.cursor()

        # Catch some specific exceptions
        except pyodbc.Error as ex:  # FIXME what exceptions I'm I trying to catch here?
            raise ex

        # Catch any additional errors not specifically checked for
        except Exception as e:
            raise Exception("Could not setup the ODBC connection %s, Exception %s", sql_server_url, e)

        try:
            self.db_cursor
        except Exception as e:
            raise Exception("Could not request ODBC connection cursor for server %s, Exception $s", sql_server_url, e)


    def execute_odbc_query(self):
        """"  Execute SQL statement

        All SQL statements are executed using the Cursor execute() function.
        If the statement returns rows, such as a select statement, you can retrieve them using the Cursor
        fetch functions - fetchone(), fetchall(), fetchmany(). If there are no rows, fetchone() will return None,
        whereas fetchall() and fetchmany() will both return empty lists.

        ODBC supports parameters using a question mark as a place holder in the SQL.
        You provide the values for the question marks by passing them after the SQL

        """
        try:
            sql_select = self.search_params.get("sql_select")
            sql_condition_value = self.search_params.get("sql_condition_value")

            self.db_cursor.execute(sql_select, [sql_condition_value])

            rows = self.db_cursor.fetchall()
            for row in rows:
                if row is None: break

                format_list = [row.incident_id, row.name, row.description]
                print "Incident id: {}, name: {}, description: {}.".format(*format_list)

        # Catch some specific exceptions
        except pyodbc.DatabaseError as err:
            raise err

        # Catch any additional errors not specifically checked for
        except Exception as e:
            raise Exception("Could not execute SQL statement %s, Exception %s", sql_select, e)

    def close_connections(self):
        """"  Close connection to cursor, connection and delete the cursor """
        #self.db_cursor.close() # it should close when we delete it
        del self.db_cursor
        self.db_connection.close()
