# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
from json import JSONDecodeError, loads

from fn_odbc_query.util.odbc_utils import odbcDBs

PACKAGE_NAME = "fn_odbc_query"

def validate_data(sql_restricted_sql_statements, sql_query):
    """
    Validate if query is allowed.
    :param sql_restricted_sql_statements: string of restricted SQL statements - configuration settings
    :param sql_query: sql statement - function input
    """
    # Convert to a list/call json.loads if sql_restricted_sql_statements is not None and is not empty string.
    if sql_restricted_sql_statements:
        # Make sure user defined restricted sql statements are in valid JSON format.
        # Defined as a list using square brackets, separated by a comma.
        # Example ["delete", "update", "insert"]
        try:
            restricted_list = loads(sql_restricted_sql_statements)
        except JSONDecodeError as e:
            raise ValueError(f"Restricted SQL statements must be defined in valid JSON  format. Error: {str(e)}")

        if type(restricted_list) is not list:
            raise ValueError("Restricted SQL statements must be defined in valid JSON format as a list using square brackets.")

        # Check if any of NOT allowed statement are included in the sql_query
        for item in restricted_list:
            if item.strip().lower() in sql_query.lower():
                raise ValueError(f"User does not have permission to perform {item.strip()} action.")

def prepare_results(cursor_description, rows):
    """
    Generate result in JSON format with an entry consisting of key value pairs.
    :param cursor_description: a tuple with query result columns
    :param rows: list of returned sql query values
    :return: dictionary
    """
    if not rows or len(rows) == 0:
        return {"entries": None}

    # List of column names from SQL result to use as dictionary keys
    dt_column_keys = [column[0] for column in cursor_description]

    # Build dictionary: key-value pairs consisting of column name - row value
    entries_data_list = [dict(zip(dt_column_keys, row)) for row in rows]

    return {"entries": [entry for entry in entries_data_list]}

def get_database_settings(opts, db_label):
    """
    Used for initilizing or reloading the options variable
    :param opts: List of options
    :return: ODBC settings for specified database
    """
    db_list = {PACKAGE_NAME} if opts.get(PACKAGE_NAME, {}) else odbcDBs(opts).get_database_name_list()

    # Creates a dictionary that is filled with the databases
    # and there configurations
    dbs_list = {db_name:opts.get(db_name, {}) for db_name in db_list}

    # Return configuration for database specified
    return odbcDBs.database_label_test(db_label, dbs_list)
